import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';import {createHash} from 'node:crypto';
const here=path.dirname(fileURLToPath(import.meta.url));const assert=(x,s)=>{if(!x)throw new Error(s);};
assert(42*3/2+6*3+2*3/2===84,'traceAC exactly full');
const normalProfiles=[];for(let heavy=0;heavy<=2;heavy++)for(let integerUnits=0;integerUnits<=4;integerUnits++)if(2*heavy+integerUnits===4){
  const maxSum=(heavy?.5+1:.5)+(integerUnits?1:0);
  const chiAllowed=maxSum<=1.5,rootAllowed=heavy<2;
  normalProfiles.push({heavy,integerUnits,chiAllowed,rootAllowed,pass:chiAllowed&&rootAllowed});
}
assert(normalProfiles.filter(x=>x.pass).length===1&&normalProfiles.find(x=>x.pass).integerUnits===4,'only H1');
const patterns=[];let compositions=0;
function explore(prefix,remaining){if(prefix.length===7){const m=[...prefix,remaining];compositions++;
  const tB=[1,1,1,1,m[0],m[1]],mD=m.slice(2);
  if(tB.every(b=>mD.every(d=>b+d===1||b+d===3)))patterns.push({m,tB,mD});return;}
  for(let n=0;n<=remaining;n++)explore([...prefix,n],remaining-n);
}
explore([],6);assert(compositions===1716&&patterns.length===16,'all six-center compositions independent integer counters');
const unitSets=[];for(let a=0;a<6;a++)for(let b=a+1;b<6;b++)unitSets.push(Array.from({length:6},(_,i)=>i).filter(i=>i!==a&&i!==b));
let first=0,second=0;
for(const p of patterns){const normalSupports=[];
  for(const units of unitSets){
    if(p.tB.every(b=>units.every(j=>b+p.mD[j]===1)))normalSupports.push({half:'B',units:'D',support:units});
    if(p.mD.every(d=>units.every(j=>p.tB[j]+d===1)))normalSupports.push({half:'D',units:'B',support:units});
  }
  assert(normalSupports.length===1,'each center pattern forces a unique common normal four-support');p.normalSupport=normalSupports[0];
  if(p.m[0]===1&&p.m[1]===1){first++;assert(p.mD.filter(x=>x===2).length===2&&p.normalSupport.half==='B','2singles/2doubles case');}
  else{second++;assert(p.m[0]===3&&p.m[1]===3&&p.mD.every(x=>x===0)&&p.normalSupport.half==='D','2triples case');}
}
assert(first===15&&second===1,'two complete cases');
for(let mask=0;mask<16;mask++){const ratios=Array.from({length:4},(_,i)=>mask>>i&1?-1:1);assert(ratios.some((x,i)=>ratios.some((y,j)=>j>i&&x===y)),'four signratios contain an equal pair');}
assert(2*7-4-4===6&&6<8,'projection norm6/7 below8/7');
const orthCandidates=[];for(let mask=0;mask<64;mask++){
  const v=Array.from({length:6},(_,i)=>mask>>i&1?-1:1);
  if(v.reduce((s,x)=>s+x,0)===0&&v.reduce((s,x,i)=>s+x*(i<3?1:-1),0)===0)orthCandidates.push(v);
}
assert(orthCandidates.length===0,'no third signvector orthogonal to ones and three-plus/three-minus');
const out={exact:true,scope:'D6^4 six fractionary blocks in ONE opposite pair; mixed2+4 remains open',
  trace_AC:84,normal_profiles:normalProfiles,center_compositions:compositions,valid_patterns:patterns,
  normal_same_support_forced:true,ratio_tests:16,root_projection_norm:'6/7',dual_gap:'8/7',
  family_fA6_fB0_excluded:true,D6_full_not_excluded:true,mixed_fA2_fB4_open:true,
  source_sha256:createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};
fs.writeFileSync(path.join(here,'verifier_D6_fA6_independant.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({exact:true,compositions:1716,valid_patterns:16,fA6_same_pair_excluded:true,mixed2plus4_open:true}));
