// Exact elementary E8 check; x2 and r2 mean twice each vector.
import fs from 'node:fs';
import assert from 'node:assert/strict';
const roots=[];
for(let i=0;i<8;i++)for(let j=i+1;j<8;j++)for(const a of [-2,2])for(const b of [-2,2]){
 const r=Array(8).fill(0);r[i]=a;r[j]=b;roots.push(r);
}
const integerRoots=roots.slice();
for(let mask=0;mask<256;mask++){
 let n=0;for(let j=0;j<8;j++)if(mask&(1<<j))n++;
 if(n%2===0)roots.push(Array.from({length:8},(_,j)=>mask&(1<<j)?-1:1));
}
assert.equal(roots.length,240);
const dot=(a,b)=>a.reduce((z,x,j)=>z+x*b[j],0),candidates=[];
let integerChecks=0;
for(let code=0;code<3**8;code++){
 let q=code;const x=[];for(let j=0;j<8;j++){x.push(2*((q%3)-1));q=Math.floor(q/3);}
 integerChecks++;if(integerRoots.every(r=>Math.abs(dot(x,r))<=4))candidates.push(x);
}
assert.equal(candidates.length,17);
for(let mask=0;mask<256;mask++)candidates.push(Array.from({length:8},(_,j)=>mask&(1<<j)?-1:1));
assert.equal(candidates.length,273);
const integral=candidates.filter(x=>roots.every(r=>dot(x,r)%4===0));
const minuscule=integral.filter(x=>roots.every(r=>Math.abs(dot(x,r))<=4));
assert.equal(integral.length,129);assert.deepEqual(minuscule,[Array(8).fill(0)]);
const out={exact:true,roots:roots.length,integer_candidate_checks:integerChecks,post_pair_bound_candidates:candidates.length,
 integral_candidates:integral.length,minuscule_candidates:minuscule,
 scope:'Uniform E8 sub-system obstruction in any integral extension of dimension<=29, using dual gap8/7; not g>=21 or whole-type exclusion.'};
fs.writeFileSync(new URL('./G18_G20_E8_MINUSCULE.json',import.meta.url),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out));
