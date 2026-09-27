import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const parity=x=>{let s=0;while(x){s^=1;x&=x-1;}return s;};
const weight=x=>{let s=0;while(x){s++;x&=x-1;}return s;};
const mod=(x,n)=>(x%n+n)%n;
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);

// Independent binary subspace enumeration: contain the mandatory word 11111111,
// then extend an orthogonal subspace, canonicalizing its entire list of vectors.
// No perfect-matching generator is used.
let spaces=[[0,255]], stages=[];
for(let dimension=2;dimension<=4;dimension++){
  const next=new Map();
  for(const H of spaces)for(let v=1;v<256;v++){
    if(parity(v)||H.includes(v)||H.some(h=>parity(v&h)))continue;
    const J=H.concat(H.map(h=>h^v)).sort((a,b)=>a-b);
    next.set(J.join(','),J);
  }
  spaces=[...next.values()];stages.push({dimension,spaces:spaces.length});
}
assert.equal(spaces.length,135);
const counts={even:0,odd_with_loop:0,odd_two_double_edges:0,odd_cycle4:0};
for(const H of spaces){
  assert(H.length===16&&H.every(x=>H.every(y=>!parity(x&y))));
  const odd=H.some(x=>weight(x)%4===2);
  if(!odd){counts.even++;continue;}
  const pairs=H.filter(x=>weight(x)===2);
  assert.equal(pairs.length,4);
  assert.equal(pairs.reduce((a,b)=>a|b,0),255);
  assert(pairs.every((p,i)=>pairs.every((q,j)=>i===j||!(p&q))));
  for(const word of H){
    let doubled=0;
    for(let i=0;i<4;i++)if(((word>>2*i)&3)===3)doubled++;
    const numerator=3*weight(word)-4*doubled;
    assert.equal(mod(numerator/2,2),mod(weight(word)/2,2));
  }
  if(pairs.some(p=>[3,12,48,192].includes(p))){counts.odd_with_loop++;continue;}
  const adjacency=Array.from({length:4},()=>new Set());
  for(const p of pairs){const vertices=[];for(let i=0;i<8;i++)if(p&(1<<i))vertices.push(i>>1);
    assert(vertices.length===2&&vertices[0]!==vertices[1]);
    adjacency[vertices[0]].add(vertices[1]);adjacency[vertices[1]].add(vertices[0]);}
  const seen=new Set([0]);for(let changed=true;changed;){changed=false;
    for(const i of [...seen])for(const j of adjacency[i])if(!seen.has(j)){seen.add(j);changed=true;}}
  if(seen.size===4)counts.odd_cycle4++;else counts.odd_two_double_edges++;
}
assert.deepEqual(counts,{even:30,odd_with_loop:45,odd_two_double_edges:12,odd_cycle4:48});

// Replay only the two existing selection fixtures, using direct integer matrix
// multiplication and the separately derived mod-2 expansion of Q.
const inputPath=path.join(here,'controle_selection42_golay.json');
const inputBytes=fs.readFileSync(inputPath),data=JSON.parse(inputBytes);
const generators=data.code.generator_masks;
assert.equal(generators.length,12);
assert(generators.every(a=>generators.every(b=>!parity(a&b))));
let code=[0];for(const g of generators)code=code.concat(code.map(x=>x^g));
assert.equal(new Set(code).size,4096);const codeSet=new Set(code);
assert(code.every(c=>weight(c)%4===0)&&codeSet.has((1<<24)-1));
const B=data.B,d=B.map(row=>row.map(x=>mod((1-x)/2,2)));
const k=B.map((row,i)=>row.map((x,j)=>(x-1+2*d[i][j])/4));
assert(k.flat().every(Number.isInteger));
const delta=d[0].map((x,j)=>x+d[1][j]),K=k[0].map((x,j)=>x+k[1][j]);
const toMask=row=>row.reduce((m,x,j)=>m|(mod(x,2)<<j),0);
assert(d.every(row=>codeSet.has(toMask(row))));
const witnesses=[];
for(const key of ['witness_wrong_xor','witness_correct_xor_wrong_Q_rows']){
  const words=data[key].selected_codeword_masks;
  assert.equal(words.length,42);assert.equal(new Set(words).size,42);
  assert(words.every(w=>codeSet.has(w)));
  const c=words.map(w=>Array.from({length:24},(_,j)=>(w>>j)&1));
  const E=c.map(row=>row.map(x=>1-2*x));
  const n=Array.from({length:24},(_,j)=>c.reduce((s,row)=>s+row[j],0));
  const F=Array.from({length:24},(_,i)=>Array.from({length:24},(_,j)=>
    (i===j?56:0)-E.reduce((s,row)=>s+row[i]*row[j],0)-B.reduce((s,row)=>s+row[i]*row[j],0)));
  const tau=mod(n[0]+delta[0],2);
  const xorOK=n.every((x,j)=>mod(x+delta[j],2)===tau);
  const integral=F.flat().every(x=>x%4===0);assert.equal(integral,xorOK);
  const checksum=mod(E.flat().reduce((s,x)=>s+x,0)+B.flat().reduce((s,x)=>s+x,0),16);
  const dodecads=words.filter(w=>weight(w)===12).length;
  assert.equal(checksum===8,dodecads%2===0);
  const item={key,Q_integral:integral,xor_condition:xorOK,checksum,dodecads};
  if(integral){
    const Q=F.map(row=>row.map(x=>x/4));
    const a=n.map((x,j)=>(x+delta[j]-tau)/2),single=a.map((x,j)=>x+K[j]);
    for(let i=0;i<24;i++)for(let j=0;j<24;j++){
      const expansion=1+tau+single[i]+single[j]
        +c.reduce((s,row)=>s+row[i]*row[j],0)+d.reduce((s,row)=>s+row[i]*row[j],0);
      assert.equal(mod(Q[i][j],2),mod(expansion,2));
    }
    let syndromes=0;
    for(const gen of generators){const gb=Array.from({length:24},(_,i)=>(gen>>i)&1);
      const scalar=mod(dot(single,gb),2);
      for(const row of Q){assert.equal(mod(dot(row,gb),2),scalar);syndromes++;}}
    const singleMask=toMask(single),x=Array.from({length:24},(_,j)=>
      (E.reduce((s,row)=>s+row[j],0)+B[0][j]+B[1][j])/2);
    assert(x.every(z=>mod(z,2)===tau));
    const shadowMask=toMask(x.map(z=>(z-tau)/2));
    assert.equal(codeSet.has(shadowMask),codeSet.has(singleMask));
    assert.equal(Q.every(row=>codeSet.has(toMask(row))),codeSet.has(singleMask));
    Object.assign(item,{singleMask,singleInCode:codeSet.has(singleMask),syndromes,
      shadowMask,shadowSumMod8:mod(x.reduce((s,z)=>s+z,0),8)});
  }
  witnesses.push(item);
}
assert(!witnesses[0].Q_integral);
assert.equal(witnesses[1].singleMask,7218972);assert(!witnesses[1].singleInCode);
const output={exact:true,method:'Orthogonal subspace enumeration, then direct integer Q expansion on two existing fixtures.',
  binary_space_stages:stages,D6_selfdual_codes:counts,Q42_witnesses:witnesses,
  input_sha256:hash(inputBytes),source_sha256:hash(fs.readFileSync(fileURLToPath(import.meta.url))),
  scope:'Classification of odd integral D6^4 ambient glue and congruences of two fixed selections; no physical frame existence or whole-g18/g20 exclusion.'};
fs.writeFileSync(path.join(here,'verifier_Q42_et_collage_D6_independant.json'),JSON.stringify(output,null,2)+'\n');
console.log(JSON.stringify({exact:true,codes135:spaces.length,counts,Q42_syndromes:witnesses[1].syndromes,singleMask:witnesses[1].singleMask}));
