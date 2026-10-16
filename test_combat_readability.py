"""v0.5.2: damage text must stay below the game board."""
from pathlib import Path
from playwright.sync_api import sync_playwright
html=Path(__file__).with_name("index.html").read_text(encoding="utf-8")
with sync_playwright() as pw:
    b=pw.chromium.launch(headless=True,executable_path="/usr/bin/chromium",args=["--no-sandbox"])
    for width in (320,375,390,430):
        for reduce in (False,True):
            p=b.new_page(viewport={"width":width,"height":844},is_mobile=True,has_touch=True,
              reduced_motion="reduce" if reduce else "no-preference")
            p.set_content(html)
            assert p.title()=="深夜地牢 | Midnight Dungeon v0.5.2"
            p.locator("#fxTestBtn").click()
            assert p.locator("#combatFeed .fx-float").count()>=1
            assert p.locator("#fxLayer .fx-float").count()==0
            result=p.evaluate("""() => {
              const arena=document.querySelector("#arena").getBoundingClientRect();
              return [...document.querySelectorAll("#combatFeed .fx-float")].every(el=>
                el.getBoundingClientRect().top>=arena.bottom-0.1)
                &&document.documentElement.scrollWidth<=innerWidth;
            }""")
            assert result,(width,reduce)
            if reduce:assert p.locator("#combatFeed .fx-static").count()>=1
            p.close()
    p=b.new_page(viewport={"width":390,"height":844},is_mobile=True,has_touch=True)
    p.evaluate("""() => {
      const m=new Map();Object.defineProperty(window,"localStorage",{configurable:true,get:()=>({
        getItem:k=>m.get(k)??null,setItem:(k,v)=>m.set(k,String(v)),removeItem:k=>m.delete(k)
      })});
    }""")
    p.set_content(html)
    p.evaluate("""() => {
      let s=MidnightDungeonTest.createState(90);s.version="0.5.1";
      s.floor=4;s.coins=32;s.meta.shards=13;s.relics.echo=2;
      localStorage.setItem("midnight-dungeon-v0.5.1",JSON.stringify(s));
      localStorage.removeItem("midnight-dungeon-v0.5.2");
    }""")
    p.set_content(html)
    cur=p.evaluate("""() => ({
      old:JSON.parse(localStorage.getItem("midnight-dungeon-v0.5.1")),
      now:JSON.parse(localStorage.getItem("midnight-dungeon-v0.5.2"))
    })""")
    assert cur["old"]["version"]=="0.5.1"
    assert cur["now"]["version"]=="0.5.2"
    assert cur["now"]["floor"]==4 and cur["now"]["coins"]==32
    assert cur["now"]["meta"]["shards"]==13 and cur["now"]["relics"]["echo"]==2
    b.close()
print("Readable feedback lane and v0.5.1 save migration PASS")
