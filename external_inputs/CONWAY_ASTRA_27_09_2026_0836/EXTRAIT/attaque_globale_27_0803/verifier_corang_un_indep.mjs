// Independent exact rational costs for the corank-one human proof. No lattice search.
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';import assert from 'node:assert/strict';import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url)),sha=b=>crypto.createHash('sha256').update(b).digest('hex'),mod=x=>((x%7)+7)%7;
const minimumA=(n,k)=>[k*(n+1-k),n+1];
const classNormNumerator=Array.from({length:7},(_,k)=>k*(7-k));
const isotropicTriples=[],allTriples=[];
for(let a=1;a<7;a++)for(let b=1;b<7;b++)for(let c=1;c<7;c++){
 const norm7=classNormNumerator[a]+classNormNumerator[b]+classNormNumerator[c];
 const r={classes:[a,b,c],seven_minimum:norm7,isotropic:mod(a*a+b*b+c*c)===0};allTriples.push(r);
 if(r.isotropic){assert.equal(norm7,28);isotropicTriples.push(r);}
}
assert.equal(allTriples.length,216);assert.equal(isotropicTriples.length,48);
const minThreeNonzero=Math.min(...allTriples.map(r=>r.seven_minimum));assert.equal(minThreeNonzero,18);
// Forms of the two possible pairs of 7-components, from A6 and A13.
const planes=[];
for(const diagonal of[[6,6],[6,5]]){
 const zeros=[];for(let x=0;x<7;x++)for(let y=0;y<7;y++)if(mod(diagonal[0]*x*x+diagonal[1]*y*y)===0)zeros.push([x,y]);
 assert.deepEqual(zeros,[[0,0]]);planes.push({diagonal,only_zero_isotropic:true});
}
// Primitive glue valuation: no copied table and no projective-space routine.
const allValuations=[];
for(let aprime=0;aprime<=3;aprime++)for(let j=0;j<=1;j++)for(let b=0;b<=5;b++){
 if(aprime+b-2*j!==2|| (j===1&&(aprime===0||b===0)))continue;
 const reason=aprime===0?'cyclic discriminant49 is not elementary rank2':j===1&&b>=2?'J order7 class has integral norm; anisotropic M forbids it':null;
 allValuations.push({aprime,b,j,reason});
}
assert.deepEqual(allValuations.filter(r=>!r.reason).map(({aprime,b,j})=>[aprime,b,j]),[[1,1,0],[2,0,0],[3,1,1]]);
// Rank-three root discriminants. Store norms as rational numerator/denominator.
const A3=Array.from({length:4},(_,k)=>({class:k,norm:minimumA(3,k)}));
assert.deepEqual(A3.filter(r=>r.class&&r.norm[0]%r.norm[1]===0),[{class:2,norm:[4,4]}]);
const A2A1=[];for(let a=0;a<3;a++)for(let b=0;b<2;b++)A2A1.push({class:[a,b],norm:[2*a*(3-a)+3*b,6]});
assert(A2A1.filter(r=>r.class.some(x=>x)).every(r=>r.norm[0]%r.norm[1]!==0));
const A1cube=[];for(let mask=0;mask<8;mask++){
 const weight=Array.from({length:3},(_,i)=>(mask>>i)&1).reduce((s,x)=>s+x,0);A1cube.push({class:mask,norm:[weight,2]});
}
assert(A1cube.filter(r=>r.class&&r.norm[0]%r.norm[1]===0).every(r=>r.norm[0]===2));
const otherPrimeCosts={A13_order2:minimumA(13,7),A20_order3:[minimumA(20,7),minimumA(20,14)]};
assert(otherPrimeCosts.A13_order2[0]>3*otherPrimeCosts.A13_order2[1]);
assert(otherPrimeCosts.A20_order3.every(([n,d])=>n>3*d));
const finalCosts=[];for(const d of[4,6]){
 const nonzero_R3_cost=[18*2+7,14];assert(nonzero_R3_cost[0]>3*nonzero_R3_cost[1]);
 const zero_R3_cost=[18+d,7];assert(zero_R3_cost[0]>3*zero_R3_cost[1]);
 finalCosts.push({R3_det:d,J_norm:7*d,nonzero_R3_cost,zero_R3_cost});
}
const out={exact:true,A6_class_minimum_numerators:classNormNumerator,all_nonzero_triples:216,isotropicTriples,minimum_three_nonzero:[18,7],planes,
 valuation_cases:allValuations,A3,A2A1,A1cube,otherPrimeCosts,finalCosts,
 source_sha256:sha(fs.readFileSync(fileURLToPath(import.meta.url))),
 producer_note_sha256:sha(fs.readFileSync(path.join(here,'RACINES_CORANG_UN_CANDIDAT.md'))),
 scope:'Finite rational costs accompanying an independent human proof. Hypotheses: rank22 integral minimum2, determinant49, elementary rank2 discriminant7, and the physical frame spanning rank22. No assertion for arbitrary determinant49 genus or for every root-free lattice.'};
fs.writeFileSync(path.join(here,'verifier_corang_un_indep.json'),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({exact:true,triples:216,isotropic_triples:48,all_isotropic_minimum:4,primitive_strata:3,final_costs_above3:true}));
