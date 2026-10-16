"""Core Midnight Dungeon v0.5.1 engine and mobile smoke tests."""
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
    assert page.title()=="深夜地牢 | Midnight Dungeon v0.5.1"
    result=page.evaluate("""() => {
      const api=window.MidnightDungeonTest, out={seeds:2000,unreachable:0,invalid:0,replay:0,boss:0,flows:0,relicOffers:0};
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
        if(api.relicRewardFloor(f)){
          if(s.status!=="relic"||s.pendingRelics.length!==3)throw Error("relic offer "+f);
          const chosen=s.pendingRelics[0];
          if(!api.applyAction(s,"relic:"+chosen)||s.relics[chosen]<1)throw Error("relic claim "+f);
          out.relicOffers++;
        }else if(s.status!=="playing")throw Error("unexpected reward "+f);
        if(!api.validateSave(s))throw Error("invalid save "+f);
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
      const s2=api.createState(19);s2.floor=2;api.makeFloor(s2);
      if(s2.enemies.filter(e=>e.eliteType).length!==1)throw Error("elite spawn F2");
      const elite=s2.enemies.find(e=>e.eliteType);api.defeatEnemy(s2,elite);
      if(!s2.loot.some(l=>l.type==="cache"))throw Error("elite chest drop");
      const guard=api.createState(41);guard.enemies=[];guard.loot=[];
      const shield={id:"g",x:2,y:1,hp:10,maxHp:10,damage:2,boss:false,eliteType:"guard",armor:1,windup:false};
      guard.enemies=[shield];api.strike(guard,shield,5);
      if(shield.hp!==7||shield.armor!==0)throw Error("elite guard armor");
      const brute=api.createState(42);brute.enemies=[{id:"b",x:2,y:1,hp:10,maxHp:10,damage:2,boss:false,eliteType:"brute",armor:0,windup:false}];brute.loot=[];
      api.applyAction(brute,"wait");if(!brute.enemies[0].windup||brute.hp!==10)throw Error("brute telegraph");
      api.applyAction(brute,"wait");if(brute.hp!==6)throw Error("brute smash");
      const chest=api.createState(45);chest.enemies=[];chest.loot=[{x:2,y:1,type:"cache",prize:"relic"}];
      api.applyAction(chest,"right");
      if(chest.status!=="relic"||chest.relicSource!=="elite"||chest.pendingRelics.length!==3)throw Error("elite relic reward");
      const choice=chest.pendingRelics[0];api.applyAction(chest,"relic:"+choice);
      if(chest.status!=="playing"||chest.relics[choice]!==1||!api.validateSave(chest))throw Error("claim elite relic");
      const prev=api.createState(46);prev.version="0.3.0";delete prev.relicSource;
      if(!api.migrateV3(prev)||api.migrateV3(prev).version!=="0.5.1")throw Error("v0.3 migrate");
      out.eliteChecks=7;
      return out;
    }""")
    assert result["unreachable"]==result["invalid"]==result["replay"]==0,result
    assert result["boss"]==2 and result["flows"]==12 and result["relicOffers"]==4,result
    page.locator('[data-dir="right"]').click()
    assert page.locator("#turnBadge").inner_text()=="TURN 1"
    page.locator("#debugBtn").click()
    assert json.loads(page.locator("#debugText").input_value())["version"]=="0.5.1"
    assert not errors,errors
    print(json.dumps(result,ensure_ascii=False))
    browser.close()
