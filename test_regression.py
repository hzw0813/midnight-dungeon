"""Core Midnight Dungeon v0.2 engine and mobile smoke tests."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import json
index = Path(__file__).with_name("index.html")
with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True,executable_path="/usr/bin/chromium",args=["--no-sandbox"])
    page=browser.new_page(viewport={"width":390,"height":844},is_mobile=True,has_touch=True)
    errors=[]
    page.on("pageerror",lambda e:errors.append(str(e)))
    page.set_content(index.read_text(encoding="utf-8"))
    assert page.title()=="深夜地牢 | Midnight Dungeon v0.2"
    result=page.evaluate("""() => {
      const api=window.MidnightDungeonTest, out={seeds:2000,unreachable:0,invalid:0,replay:0,boss:0,flows:0};
      for(let seed=1;seed<=2000;seed++){
        const a=api.createState(seed),b=api.createState(seed),d=api.distances(a,1,1);
        if(d[a.exit.y][a.exit.x]<0||[...a.enemies,...a.loot].some(x=>d[x.y][x.x]<0))out.unreachable++;
        if(!api.validateSave(a))out.invalid++;
        const actions=["up","right","down","left","wait","potion"];
        for(let i=0;i<20;i++){const c=actions[(i+seed)%actions.length];api.applyAction(a,c);api.applyAction(b,c);}
        if(JSON.stringify(a)!==JSON.stringify(b))out.replay++;
      }
      const s=api.createState(66);
      for(let f=1;f<=12;f++){
        const boss=s.enemies.find(e=>e.boss);
        const dirs=[["up",0,1],["down",0,-1],["left",1,0],["right",-1,0]];
        const q=dirs.find(([_,dx,dy])=>s.map[s.exit.y+dy]?.[s.exit.x+dx]===0);
        s.hero={x:s.exit.x+q[1],y:s.exit.y+q[2]};
        if(boss&&!api.applyAction(s,q[0]))out.boss++;
        s.enemies=[];if(!api.applyAction(s,q[0])||s.status!=="choosing")throw Error("floor "+f);
        if(s.pendingBlessings.length!==3)throw Error("blessings "+f);
        if(!api.applyAction(s,"blessing:"+s.pendingBlessings[0]))throw Error("choice "+f);
        out.flows++;
      }
      const lost=api.createState(101);lost.coins=30;lost.hp=1;
      lost.enemies=[{x:2,y:1,hp:3,maxHp:3,damage:1,boss:false,id:"test"}];
      api.applyAction(lost,"wait");
      if(lost.status!=="lost"||lost.meta.shards!==2)throw Error("death settlement");
      if(!api.applyAction(lost,"talent:life"))throw Error("talent");
      if(api.createState(102,lost.meta).maxHp!==13)throw Error("persistent talent");
      const shop=api.createState(103);shop.coins=20;
      if(!api.applyAction(shop,"shop:attack")||shop.coins!==8)throw Error("shop");
      return out;
    }""")
    assert result["unreachable"]==result["invalid"]==result["replay"]==0,result
    assert result["boss"]==2 and result["flows"]==12,result
    page.locator('[data-dir="right"]').click()
    assert page.locator("#turnBadge").inner_text()=="TURN 1"
    page.locator("#debugBtn").click()
    assert json.loads(page.locator("#debugText").input_value())["version"]=="0.2.0"
    assert not errors,errors
    print(json.dumps(result,ensure_ascii=False))
    browser.close()
