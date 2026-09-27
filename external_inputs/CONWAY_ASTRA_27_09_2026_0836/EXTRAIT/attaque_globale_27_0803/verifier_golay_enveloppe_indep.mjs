// Independent Golay array-span and exact rational Schur determinant. No Bareiss or matching search.
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';import assert from 'node:assert/strict';import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url)),sha=b=>crypto.createHash('sha256').update(b).digest('hex'),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),sum=a=>a.reduce((s,x)=>s+x,0),mod=(x,p)=>((x%p)+p)%p;
const exponents=[0,1,5,6,7,9,11],generators=Array.from({length:12},(_,shift)=>{
 const row=Array(24).fill(0);for(const e of exponents)row[e+shift]=1;row[23]=sum(row)%2;return row;
});
// Recursive doubling in F2^24. Words are coordinate arrays, never integer masks.
let code=[Array(24).fill(0)];for(const row of generators){const translated=code.map(c=>c.map((x,i)=>x^row[i]));code=code.concat(translated);}
const keys=new Set(code.map(c=>c.join('')));assert.equal(code.length,4096);assert.equal(keys.size,4096);assert(keys.has('1'.repeat(24)));
assert(generators.every(a=>generators.every(b=>dot(a,b)%2===0)));
const weights={};code.forEach(c=>{const w=sum(c);weights[w]=(weights[w]||0)+1;});assert.deepEqual(weights,{0:1,8:759,12:2576,16:759,24:1});
const set=a=>new Set(a),V=set([0,1,3,4,5,6,7,8,10,11,12,14]),D=set([0,1,2,9]),Dp=set([3,4,13,15]);
assert(keys.has(Array.from({length:24},(_,i)=>+V.has(i)).join('')));
const y1=Array.from({length:24},(_,i)=>D.has(i)?-3:1),y2=Array.from({length:24},(_,i)=>(V.has(i)?-1:1)*(Dp.has(i)?-3:1));
function latticeContains(x){
 const parity=mod(x[0],2);if(!x.every(t=>mod(t,2)===parity))return false;
 const cw=x.map(t=>+(mod(t-parity,4)===2));return keys.has(cw.join(''))&&mod(sum(x),8)===0;
}
assert(latticeContains(y1)&&latticeContains(y2));assert.equal(dot(y1,y1),56);assert.equal(dot(y2,y2),56);assert.equal(dot(y1,y2),0);
const norm3=code.map(c=>c.map(x=>1-2*x)),inM=[],projection={};let simultaneousAbs3=0;
for(const x of norm3){
 assert(latticeContains(x));assert.equal(dot(x,x),24);
 const a=dot(x,y1),b=dot(x,y2);assert.equal(mod(a,8),0);assert.equal(mod(b,8),0);
 const ia=a/8,ib=b/8,numerator=21-ia*ia-ib*ib;
 projection[numerator]=(projection[numerator]||0)+1;
 if(Math.abs(ia)===3&&Math.abs(ib)===3)simultaneousAbs3++;
 if(a===0&&b===0)inM.push(x);
}
assert.equal(inM.length,704);assert.equal(simultaneousAbs3,0);assert.equal(Math.min(...Object.keys(projection).map(Number)),11);
// Supplied 22-vector certificate is checked against the independently reconstructed shell.
const suppliedBytes=fs.readFileSync(path.join(here,'controle_enveloppe_g20_golay.json')),supplied=JSON.parse(suppliedBytes),basis=supplied.basis_integer_coordinates_over_sqrt8;
assert.equal(basis.length,22);assert(new Set(basis.map(x=>x.join(','))).size===22);
const Mkeys=new Set(inM.map(x=>x.join(',')));assert(basis.every(x=>Mkeys.has(x.join(','))));
const Gram=basis.map(a=>basis.map(b=>{const q=dot(a,b);assert.equal(mod(q,8),0);return q/8;}));
assert.deepEqual(Gram,supplied.Gram);assert.deepEqual(projection,supplied.projection_squared_numerators_over7);
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;};
const f=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);assert(d!==0n);if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return[n/g,d/g];};
const mul=(a,b)=>f(a[0]*b[0],a[1]*b[1]),div=(a,b)=>f(a[0]*b[1],a[1]*b[0]),sub=(a,b)=>f(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);
const A=Gram.map(row=>row.map(x=>f(x))),pivots=[];let determinant=f(1);
for(let k=0;k<22;k++){
 const pivot=A[k][k];assert(pivot[0]>0n);pivots.push(pivot.map(String));determinant=mul(determinant,pivot);
 for(let i=k+1;i<22;i++)for(let j=i;j<22;j++){
  const updated=sub(A[i][j],div(mul(A[i][k],A[j][k]),pivot));A[i][j]=A[j][i]=updated;
 }
}
assert.deepEqual(determinant,[49n,1n]);
const seen=new Set([0]),todo=[0];let edges=0;
for(let i=0;i<22;i++)for(let j=i+1;j<22;j++)if(Gram[i][j])edges++;
for(let k=0;k<todo.length;k++)for(let j=0;j<22;j++)if(Gram[todo[k]][j]&&j!==todo[k]&&!seen.has(j)){seen.add(j);todo.push(j);}
assert.equal(seen.size,22);assert.equal(edges,131);
const out={exact:true,word_count:4096,weights,code_self_dual:true,y_norms:[7,7],y_inner:0,shell3_L:4096,shell3_M:704,
 projection_numerators_over7:projection,simultaneous_abs3:simultaneousAbs3,certificate_basis:22,Gram,exact_rational_pivots:pivots,determinant:'49',Gram_support_edges:131,connected:true,
 supplied_certificate_sha256:sha(suppliedBytes),producer_source_sha256:sha(fs.readFileSync(path.join(here,'controle_enveloppe_g20_golay.mjs'))),source_sha256:sha(fs.readFileSync(fileURLToPath(import.meta.url))),
 scope:'Second implementation of all finite ingredients of the lattice-envelope control. Array-span generation and reduced rational Schur pivots are independent of the producer bitmask span/Bareiss. Supplied basis is replayed as a certificate. No SRG49 tight7 frame or graph is asserted.'};
fs.writeFileSync(path.join(here,'verifier_golay_enveloppe_indep.json'),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({exact:true,words:4096,shell_M:704,determinant:'49',connected:true,projection_minimum:'11/7',basis_certificate_replayed:true}));
