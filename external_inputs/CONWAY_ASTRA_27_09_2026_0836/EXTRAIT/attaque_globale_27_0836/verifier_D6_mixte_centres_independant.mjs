import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
function compositions(total,width,prefix=[],out=[]){if(width===1){out.push([...prefix,total]);return out;}
  for(let x=0;x<=total;x++)compositions(total-x,width-1,[...prefix,x],out);return out;}
const supports=[];
for(let a=0;a<3;a++)for(let b=a+1;b<4;b++)for(let c=b+1;c<5;c++)for(let d=c+1;d<6;d++){
  const v=Array(6).fill(0);for(const i of[a,b,c,d])v[i]=1;supports.push(v);}
assert.equal(supports.length,15);
const stats={distributions:0,distributions_with_repeat:0,diagonal_surviving_distributions:0,
  diagonal_surviving_repeated_distributions:0,normal_support_pairs_before_root_cut:0,
  repeated_normal_support_pairs:0,minimum_common_axes_for_repeated:6};
const examples=[];
for(const m of compositions(4,12)){
  stats.distributions++;
  const repeated=m.some(x=>x>=2);if(repeated)stats.distributions_with_repeat++;
  const B=m.slice(0,6),D=m.slice(6);
  let surviving=false,survivingRepeated=false;
  // q is the number of normals whose four integral units are in B.
  // Their minimal spinor is then in D. Diagonal sums determine q exactly.
  for(let q=0;q<=2;q++){
    const mB=B.reduce((s,x)=>s+x,0),mD=D.reduce((s,x)=>s+x,0);
    if((mB+4*q)%6||(mD+4*(2-q))%6)continue;
    const tB=(mB+4*q)/6,tD=(mD+4*(2-q))/6;
    if(tB+tD!==2)continue;
    const types=q===0?[[0,0]]:q===2?[[1,1]]:[[1,0],[0,1]];
    for(const [unitB1,unitB2] of types)for(const s1 of supports)for(const s2 of supports){
      const coverageB=Array.from({length:6},(_,i)=>unitB1*s1[i]+unitB2*s2[i]);
      const coverageD=Array.from({length:6},(_,i)=>(1-unitB1)*s1[i]+(1-unitB2)*s2[i]);
      // Exact 36 paired coordinate equations; no producer bitsets or centre masks.
      let good=true;
      for(let i=0;i<6;i++)for(let j=0;j<6;j++)
        if(B[i]+coverageB[i]+D[j]+coverageD[j]!==2)good=false;
      if(!good)continue;
      surviving=true;stats.normal_support_pairs_before_root_cut++;
      if(!repeated)continue;
      survivingRepeated=true;stats.repeated_normal_support_pairs++;
      assert.equal(unitB1,unitB2);
      const common=s1.reduce((s,x,i)=>s+x*s2[i],0);
      assert(common>=3);
      stats.minimum_common_axes_for_repeated=Math.min(stats.minimum_common_axes_for_repeated,common);
      if(examples.length<2)examples.push({centre_multiplicities:m,unit_component:unitB1?'B':'D',s1,s2,common_axes:common});
      // Every pair of sign lists on >=3 common axes has two equal sign ratios.
      // Check the eight relative sign patterns on a three-axis subset directly.
      for(let ratios=0;ratios<8;ratios++){
        const r=Array.from({length:3},(_,i)=>((ratios>>i)&1)?-1:1);
        assert(r[0]===r[1]||r[0]===r[2]||r[1]===r[2]);
      }
    }
  }
  if(surviving)stats.diagonal_surviving_distributions++;
  if(survivingRepeated)stats.diagonal_surviving_repeated_distributions++;
}
assert.equal(stats.distributions,1365);
assert.equal(stats.diagonal_surviving_repeated_distributions,150);
assert.equal(stats.repeated_normal_support_pairs,270);
assert.equal(stats.minimum_common_axes_for_repeated,3);
assert.equal(stats.diagonal_surviving_distributions,405);
assert.equal(stats.normal_support_pairs_before_root_cut,900);
let localCases=0;const splitChecks=[];
for(let mB=0;mB<=1;mB++)for(let mD=0;mD<=1;mD++)
for(const b1 of[-1,1])for(const b2 of[-1,1])for(const d1 of[-1,1])for(const d2 of[-1,1]){
  let allKAllowed=true;
  for(const direction of[-1,1]){
    const r=(b1===direction*d1?1:0)+(b2===direction*d2?1:0);
    const k=mB+mD+r;if(k!==1&&k!==3)allKAllowed=false;
  }
  assert.equal(allKAllowed,b1*b2*d1*d2===-((-1)**(mB+mD)));localCases++;
}
for(let b=0;b<=4;b++)for(const epsilon of[-1,1]){
  const d=4-b;
  const sigma=Array.from({length:6},(_,i)=>epsilon*(i<b?-1:1));
  const tau=Array.from({length:6},(_,i)=>-epsilon*(i<d?-1:1));
  const spinorInner=(sigma.reduce((s,x)=>s+x,0)+tau.reduce((s,x)=>s+x,0))/4;
  assert(spinorInner===epsilon*(2-b));assert.equal(spinorInner===0,b===2);
  splitChecks.push({centres_B:b,centres_D:d,epsilon,spinor_inner:spinorInner,orthogonal:b===2});
}
const output={exact:true,stats,examples,
  hypothesis:'Four h have spinors on AC, two on BD, and h7 is integral and supported on AC; full physical frame and common normal root-dual bound.',
  conclusion:'The four centres of the AC spinor blocks must be distinct and split as two in B and two in D. The mixed regime is not wholly refuted.',
  orthogonality_corollary:{local_cases:localCases,split_checks:splitChecks,only_split:[2,2]},
  source_sha256:crypto.createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};
fs.writeFileSync(path.join(here,'verifier_D6_mixte_centres_independant.json'),JSON.stringify(output,null,2)+'\n');
console.log(JSON.stringify({exact:true,...stats,mixed_regime_excluded:false}));
