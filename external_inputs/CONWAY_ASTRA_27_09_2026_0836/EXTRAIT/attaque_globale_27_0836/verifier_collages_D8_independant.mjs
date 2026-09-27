import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const parity=x=>{let p=0;while(x){p^=1;x&=x-1;}return p;};
// Each component has symbols s,c, with 2b(s,c)=1, b(s,s)=b(c,c)=0.
const bilinear=(x,y)=>parity((((x&21)<<1)^((x&42)>>1))&y);
const symbols=x=>Array.from({length:3},(_,i)=>(x>>(2*i))&3);
const cost=x=>symbols(x).reduce((s,c)=>s+(c===0?0:c===3?1:2),0);
let spaces=[[0]],stages=[];
for(let dim=1;dim<=3;dim++){
  const output=new Map();
  for(const H of spaces)for(let v=1;v<64;v++){
    if(H.includes(v)||H.some(h=>bilinear(v,h)))continue;
    const J=H.concat(H.map(h=>h^v)).sort((a,b)=>a-b);output.set(J.join(','),J);
  }
  spaces=[...output.values()];stages.push({dimension:dim,count:spaces.length});
}
assert.equal(spaces.length,135);
const counts={even:0,odd:0,min1:0,singleton_spinor_E8:0,double_vector_D16:0,
  admissible:0,only_vvv:0,two_vector_spinor_same_centre:0};
const survivors=[];
for(const H of spaces){
  assert(H.length===8&&H.every(x=>H.every(y=>!bilinear(x,y))));
  const odd=H.some(x=>cost(x)%2);counts[odd?'odd':'even']++;
  if(!odd)continue;
  if(H.some(x=>cost(x)===1)){counts.min1++;continue;}
  if(H.some(x=>{const s=symbols(x);return s.filter(c=>c!==0).length===1&&s.some(c=>c===1||c===2);})){counts.singleton_spinor_E8++;continue;}
  if(H.some(x=>{const s=symbols(x);return s.filter(c=>c===3).length===2&&s.filter(c=>c!==0).length===2;})){counts.double_vector_D16++;continue;}
  const shellClasses=H.filter(x=>cost(x)===3);
  assert(shellClasses.length>0);
  const integerComponents=[];
  for(let i=0;i<3;i++)if(shellClasses.every(x=>[0,3].includes(symbols(x)[i])))integerComponents.push(i);
  assert(integerComponents.length>0);
  let vectors=0;for(const word of shellClasses)vectors+=symbols(word).reduce((s,c)=>s*(c===0?1:c===3?16:128),1);
  assert.equal(vectors,4096);counts.admissible++;
  if(shellClasses.includes(63)){assert.deepEqual(shellClasses,[63]);counts.only_vvv++;}
  else{
    assert.equal(shellClasses.length,2);
    const centres=shellClasses.map(x=>symbols(x).findIndex(c=>c===3));
    assert.equal(centres[0],centres[1]);counts.two_vector_spinor_same_centre++;
  }
  survivors.push({H,shellClasses,integerComponents,shell_vectors:vectors});
}
assert.deepEqual(counts,{even:30,odd:105,min1:37,singleton_spinor_E8:24,
  double_vector_D16:12,admissible:32,only_vvv:8,two_vector_spinor_same_centre:24});
// The direct human reduction needs only the 13 possible class-minima of norm3.
const norm3=Array.from({length:63},(_,i)=>i+1).filter(x=>cost(x)===3);
assert.equal(norm3.length,13);
const pairChecks=[];
for(const a of norm3)for(const b of norm3){
  if(bilinear(a,b))continue;
  const initial=[0,a,b,a^b],independent=a!==b;
  if(!independent)continue;
  const commonVector=symbols(a).some((s,i)=>s===3&&symbols(b)[i]===3);
  if(commonVector)continue;
  // An orthogonal pair with displaced centre either adds two vector classes,
  // or fills the Lagrangian on two components, whose extension is a singleton.
  let forbidden=cost(a^b)<=2;
  const union=symbols(a|b).map(c=>c!==0).filter(Boolean).length;
  const singletonForced=union===2;
  assert(forbidden||singletonForced);
  pairChecks.push({a,b,forbidden_sum:forbidden,full_two_component_Lagrangian:singletonForced});
}
const result={exact:true,stages,counts,survivors,norm3_class_count:norm3.length,
  displaced_centre_pair_checks:pairChecks.length,
  theorem:'Every admissible odd D8^3 glue has a component containing only classes 0/v in its complete norm-3 shell; eight orthogonal unit directions pair integrally with all physical u, contradicting the dual gap and codimension two.',
  source_sha256:crypto.createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex'),
  scope:'Entire ambient family containing D8^3 is excluded for the physical frame; no general classification of all odd rank-24 lattices.'};
fs.writeFileSync(path.join(here,'verifier_collages_D8_independant.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({exact:true,lagrangians:spaces.length,counts,displaced_pair_checks:pairChecks.length}));
