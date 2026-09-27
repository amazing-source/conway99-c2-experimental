// Tiny exact checks of the two capacity obstructions, not a graph search.
import fs from 'node:fs';
import assert from 'node:assert/strict';
const heavy=[];
for(const k of [2,3]){
 const m=14-3*k, valid=[];
 for(let mask=0;mask<(1<<m);mask++){
  let size=0,weight=0;
  for(let j=0;j<m;j++)if(mask&(1<<j)){size++;weight+=j<k?2:1;}
  if(weight>=8)valid.push({mask,size,weight});
 }
 let minCommon=Infinity,pairs=0;
 for(const a of valid)for(const b of valid){
  let n=0,x=a.mask&b.mask;while(x){x&=x-1;n++;}
  pairs++;minCommon=Math.min(minCommon,n);assert(n>=2+k);
 }
 assert.equal(minCommon,2+k);
 heavy.push({k,m,subset_checks:1<<m,valid_subsets:valid.length,pair_checks:pairs,minimum_common:minCommon,srg_maximum:2,contradiction:true});
}
let reflectionChecks=0;
for(const eps of [-1,1])for(const c of [-1,1])for(const a of [-1,0,1]){
 const allowed=Math.abs(a+eps*c)<=1;
 assert.equal(allowed,a===0||a===-eps*c);reflectionChecks++;
}
const exterior=[];
for(const alpha of [-1,1])for(const beta of [-1,1]){
 const charges=[alpha+beta,alpha-beta];
 assert(charges.some(x=>x===0));assert(!charges.every(x=>Math.abs(x)>=2));
 exterior.push({coefficients:[alpha,beta],charges});
}
let incidentPairChecks=0;
for(const eps of [-1,1])for(const first of [0,1])for(const second of [0,1]){
 const charge=-eps*(first-second);assert(Math.abs(charge)<=1);incidentPairChecks++;
}
let parityChecks=0;
for(const eps of [-1,1])for(const light of [-1,1]){
 assert.notEqual((-3*(2*eps+light))%2,0);parityChecks++;
}
for(const c1 of [-1,1])for(const c2 of [-1,1]){assert((c1+c2)%2===0);parityChecks++;}
const result={exact:true,heavy,reflection_checks:reflectionChecks,incident_pair_checks:incidentPairChecks,exterior,parity_checks:parityChecks,
 heavy_remaining:{other_interior_active:0,incident_roots:6,external_roots:4},ternary_interior_active:[0,2,4],
 scope:'Capacity and sign identities only. No graph/whole-type exclusion or g>=21 bound.',
 prerequisites:{heavy:'Odd eigenvector -4, F49 coefficient norm14, all coefficients0,+/-1,+/-2, SRG maximum common2',
 network:'Integral lattice minimum>=2 containing seven h norm4 and42u norm3, Gram3I-S, tight frame7'}};
fs.writeFileSync(new URL('./G18_G20_NORME14_LOURDS.json',import.meta.url),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result));
