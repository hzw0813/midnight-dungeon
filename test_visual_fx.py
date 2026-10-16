"""Midnight Dungeon v0.5 visual effects smoke tests (Chromium/Playwright)."""
from pathlib import Path
from playwright.sync_api import sync_playwright
html=Path(__file__).with_name("index.html").read_text(encoding="utf-8")
def fake_storage(p):
    p.evaluate("""() => {
      const saves=new Map();
      Object.defineProperty(window,"localStorage",{configurable:true,get:()=>({
        getItem:k=>saves.get(k)??null,setItem:(k,v)=>saves.set(k,String(v)),removeItem:k=>saves.delete(k)
      })});
    }""")
with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True,executable_path="/usr/bin/chromium",args=["--no-sandbox"])
    p=browser.new_page(viewport={"width":390,"height":844},is_mobile=True,has_touch=True)
    errs=[];p.on("pageerror",lambda e:errs.append(str(e)))
    fake_storage(p);p.set_content(html)
    assert p.title()=="深夜地牢 | Midnight Dungeon v0.5"
    check=p.evaluate("""() => {
      const a=MidnightDungeonTest,s=a.createState(4);s.enemies=[];s.loot=[];
      s.enemies=[{id:"k",x:2,y:1,hp:1,maxHp:1,damage:1,boss:false}];
      const b=a.beforeVisual(s),seed=s.rng;
      a.applyAction(s,"right");
      const before=JSON.stringify(s),fx=a.visualEvents(b,s,"right");
      const old={...a.createState(6),version:"0.4.0"},up=a.migrateV4(old);
      return {kill:fx.some(e=>e.kind==="kill"),coin:fx.some(e=>e.kind==="gold"),
        pure:before===JSON.stringify(s),migrated:up&&a.validateSave(up)&&up.version==="0.5.0",rng:seed};
    }""")
    assert check["kill"] and check["coin"] and check["pure"] and check["migrated"],check
    p.evaluate("""() => {
      const s=MidnightDungeonTest.createState(20);
      s.enemies=[{id:"a",x:2,y:1,hp:1,maxHp:1,damage:1,boss:false}];s.loot=[];
      localStorage.setItem("midnight-dungeon-v0.5",JSON.stringify(s));
    }""")
    p.set_content(html);p.locator('[data-dir="right"]').click()
    assert p.locator("#fxLayer .fx-float").count()>0
    assert p.locator("#fxLayer").evaluate("(el)=>getComputedStyle(el).pointerEvents")=="none"
    p.wait_for_timeout(1350)
    assert p.locator("#fxLayer .fx-float").count()==0
    assert not errs,errs
    print("Visual feedback, purity, save migration, DOM cleanup PASS")
    browser.close()
