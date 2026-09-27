import fs from 'node:fs';
import assert from 'node:assert/strict';
import {golayWords,membership,prepareShell,pairCapacitiesFromBins,sevenCapacity}
  from './G18_G20_SEPT_BLOCS_CAPACITE.mjs';
const signature=[];
for(let i=0;i<7;i++)for(let j=i+1;j<7;j++)for(const sign of [1,-1]){
  const v=Array(7).fill(0);v[i]=1;v[j]=sign;signature.push(v);
}
signature.push([1,0,0,0,0,0,0],[1,1,1,0,0,0,0],[2,1,0,0,0,0,0]);
const bins=Array.from({length:7},(_,i)=>({zero:0n,positive:0n,negative:0n}));
for(let j=0;j<signature.length;j++)for(let i=0;i<7;i++){
  const x=signature[j][i],b=1n<<BigInt(j);
  if(x===0)bins[i].zero|=b;else if(x===1)bins[i].positive|=b;else if(x===-1)bins[i].negative|=b;
}
const profiles=pairCapacitiesFromBins(bins,signature.length);
for(const p of profiles){
  const candidates=sign=>signature.map((v,j)=>({v,j})).filter(({v})=>v[p.c]&&Math.abs(v[p.c])===1&&
    Math.abs(v[p.d])===1&&v[p.c]*v[p.d]===sign&&v.every((a,i)=>i===p.c||i===p.d||a===0)).map(({j})=>j);
  for(const [key,s] of [['plus',1],['minus',-1]]){
    const mask=candidates(s).reduce((a,j)=>a|(1n<<BigInt(j)),0n);
    assert.equal(p[key],mask.toString(16));assert.equal(p[`${key}_count`],1);
  }
}
const removed=bins.map(row=>Object.fromEntries(Object.entries(row).map(([key,b])=>[key,b&~1n])));
const failures=pairCapacitiesFromBins(removed,signature.length).filter(p=>!p.plus_count||!p.minus_count);
assert.deepEqual(failures.map(p=>[p.c,p.d,p.plus_count,p.minus_count]),[[0,1,0,1]]);
const words=golayWords(),code=new Set(words);
assert.equal(code.size,4096);
const V=[0,1,3,4,5,6,7,8,10,11,12,14],D=[0,1,2,9],Dp=[3,4,13,15];
const B=[Array.from({length:24},(_,j)=>1-4*+D.includes(j)),
  Array.from({length:24},(_,j)=>(1-2*+V.includes(j))*(1-4*+Dp.includes(j)))];
assert(B.every(row=>membership(row,code).member));
const broken=B[0].slice();broken[23]*=-1;assert(!membership(broken,code).member);
const prepared=prepareShell(B);assert.equal(prepared.line_count,352);assert.equal(prepared.oriented_shell_size,704);
const zeroM=Array.from({length:7},()=>Array(24).fill(0));
assert.equal(sevenCapacity(zeroM,prepared).kind,'block_weight');
const out={exact:true,bitset_profiles_compared:42,abstract_noise_profiles_ignored:3,
  one_class_removal_detected:true,golden_Golay_charges_membership:true,
  golden_complete_shell_size:704,golden_line_count:352,
  code_sha256:prepared.code_sha256,B_sha256:prepared.B_sha256,shell_sha256:prepared.shell_sha256,
  scope:'Source fixtures and reconstruction only; no seven-block coverage, physical49-frame or graph claimed.'};
fs.writeFileSync(new URL('./G18_G20_TEST_SEPT_BLOCS.json',import.meta.url),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify(out));
