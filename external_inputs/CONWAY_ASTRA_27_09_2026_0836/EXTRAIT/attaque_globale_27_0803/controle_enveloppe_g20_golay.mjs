import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const wt=x=>{let n=0;while(x){n++;x&=x-1;}return n;};
const g=[11,9,7,6,5,1,0].reduce((a,b)=>a|(1<<b),0),words=[];
for(let m=0;m<4096;m++){let w=0;for(let j=0;j<12;j++)if(m>>j&1)w^=g<<j;if(wt(w)%2)w|=1<<23;words.push(w);}
assert.equal(new Set(words).size,4096);
const enumerator={};for(const w of words)enumerator[wt(w)]=(enumerator[wt(w)]||0)+1;
assert.deepEqual(enumerator,{0:1,8:759,12:2576,16:759,24:1});
const generators=Array.from({length:12},(_,j)=>words[1<<j]);
for(const a of generators)for(const b of generators)assert.equal(wt(a&b)%2,0);
assert(words.includes((1<<24)-1));
const mask=a=>a.reduce((s,i)=>s|(1<<i),0),indices=w=>Array.from({length:24},(_,i)=>i).filter(i=>w>>i&1);
const V=mask([0,1,3,4,5,6,7,8,10,11,12,14]),D=mask([0,1,2,9]),Dp=mask([3,4,13,15]);
assert(words.includes(V));assert.equal(wt(V),12);assert.equal(wt(D&V),2);assert.equal(wt(Dp&V),2);assert.equal(D&Dp,0);
const x=Array.from({length:24},(_,i)=>1-4*(D>>i&1)),y=Array.from({length:24},(_,i)=>(1-2*(V>>i&1))*(1-4*(Dp>>i&1)));
const inner=(a,b)=>a.reduce((s,z,i)=>s+z*b[i],0)/8;
assert.equal(inner(x,x),7);assert.equal(inner(y,y),7);assert.equal(inner(x,y),0);
function belongs(z){const m=(z[0]%2+2)%2;if(z.some(t=>(t%2+2)%2!==m))return false;let code=0;for(let i=0;i<24;i++)if(((z[i]-m)%4+4)%4===2)code|=1<<i;return words.includes(code)&&z.reduce((a,b)=>a+b,0)%8===0;}
assert(belongs(x));assert(belongs(y));
const all=words.map(w=>Array.from({length:24},(_,i)=>1-2*(w>>i&1))),norm3=[];const projectionNumerators={};let simultaneous3=0;
for(const z of all){assert(belongs(z));const a=inner(z,x),b=inner(z,y);assert(Number.isInteger(a)&&Number.isInteger(b));if(Math.abs(a)===3&&Math.abs(b)===3)simultaneous3++;const numerator=21-a*a-b*b;projectionNumerators[numerator]=(projectionNumerators[numerator]||0)+1;if(a===0&&b===0)norm3.push(z);}
assert.equal(simultaneous3,0);assert.equal(norm3.length,704);
const inv=a=>{let v=1;for(let j=0;j<99;j++)v=v*a%101;return v;};const pivots=[],basis=[];
for(const z of norm3){let row=z.map(a=>(a+101)%101);for(const [p,r] of pivots){const c=row[p];if(c)row=row.map((a,j)=>(a-c*r[j]%101+101)%101);}const p=row.findIndex(a=>a);if(p>=0){const c=inv(row[p]);row=row.map(a=>a*c%101);pivots.push([p,row]);basis.push(z);if(pivots.length===22)break;}}
assert.equal(basis.length,22);const Gram=basis.map(a=>basis.map(b=>inner(a,b)));
assert(Gram.every(r=>r.every(Number.isInteger)));
function bareiss(mat){const A=mat.map(r=>r.map(BigInt));let d=1n,sign=1n;for(let i=0;i<A.length-1;i++){let p=i;while(p<A.length&&A[p][i]===0n)p++;if(p===A.length)return 0n;if(p!==i){[A[p],A[i]]=[A[i],A[p]];sign=-sign;}const q=A[i][i];for(let j=i+1;j<A.length;j++)for(let k=i+1;k<A.length;k++){const n=A[j][k]*q-A[j][i]*A[i][k];assert.equal(n%d,0n);A[j][k]=n/d;}for(let j=i+1;j<A.length;j++)A[j][i]=0n;d=q;}return sign*A.at(-1).at(-1);}
const determinant=bareiss(Gram);assert.equal(determinant,49n);
const seen=new Set([0]),queue=[0];while(queue.length){const a=queue.shift();for(let b=0;b<22;b++)if(a!==b&&Gram[a][b]&&!seen.has(b)){seen.add(b);queue.push(b);}}assert.equal(seen.size,22);
const result={status:'VERIFIE EXACTEMENT; lattice-envelope control, NOT a graph',binary_generator_exponents:[11,9,7,6,5,1,0],weight_enumerator:enumerator,V:indices(V),D:indices(D),D_prime:indices(Dp),norm_y:[7,7],inner_y:0,norm3_shell_of_L:4096,simultaneous_abs3:simultaneous3,norm3_shell_of_M:704,projection_squared_numerators_over7:projectionNumerators,basis_rank:22,basis_Gram_support_connected:true,basis_Gram_determinant:determinant.toString(),basis_integer_coordinates_over_sqrt8:basis,Gram,
mathematical_consequences_verified_by_written_proof:['M positive integral rank22 determinant49','discriminant group (Z/7)^2','minimum M=3','M generated integrally by norm3 vectors','minimum M* >=10/7','characteristic minimum M >=10','M orthogonally indecomposable'],not_claimed:['49-column tight7 frame','42 vectors with exactly ten nonzero root pairings each','seven norm4 blocks with C incidence D7','SRG completion','involution existence'],source_sha256:crypto.createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};
fs.writeFileSync(path.join(here,'controle_enveloppe_g20_golay.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({exact:true,enumerator,basis_rank:22,determinant:'49',norm3_M:704,simultaneous3,projectionNumerators,scope:result.not_claimed}));
