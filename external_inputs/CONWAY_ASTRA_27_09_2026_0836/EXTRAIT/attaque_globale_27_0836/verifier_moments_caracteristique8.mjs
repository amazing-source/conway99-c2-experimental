import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
const here=path.dirname(fileURLToPath(import.meta.url));
const assert=(x,s)=>{if(!x)throw new Error(s);};
const N=8,z=()=>Array(N+1).fill(0n),one=()=>{const x=z();x[0]=1n;return x;};
const add=(a,b)=>a.map((x,i)=>x+b[i]),scale=(a,c)=>a.map(x=>x*BigInt(c));
function mul(a,b){const x=z();for(let i=0;i<=N;i++)for(let j=0;i+j<=N;j++)x[i+j]+=a[i]*b[j];return x;}
function pow(a,n){let x=one();while(n--)x=mul(x,a);return x;}
function div(a,d){assert(a.every(x=>x%BigInt(d)===0n),'exact series division');return a.map(x=>x/BigInt(d));}
const t3=one(),t4=one(),series=z();for(let i=1;i*i<=N;i++){t3[i*i]=2n;t4[i*i]=i%2?-2n:2n;}for(let i=0;i*(i+1)<=N;i++)series[i*(i+1)]++;
const a=z(),s4=pow(series,4);for(let i=0;i<N;i++)a[i+1]=16n*s4[i];
const b=pow(t4,4),c=pow(t3,4),delta=div(mul(a,b),16),d=add(a,scale(b,-1));
const bases=[],shadows4096=[];
const fSh=[scale(pow(a,6),4096),scale(mul(pow(a,4),mul(b,c)),-256),scale(mul(pow(a,2),mul(pow(b,2),pow(c,2))),16),scale(mul(pow(b,3),pow(c,3)),-1)];
for(let j=0;j<4;j++){bases.push(mul(d,mul(pow(t3,24-8*j),pow(delta,j))));shadows4096.push(mul(add(b,c),fSh[j]));}
for(let j=0;j<4;j++)for(let i=0;i<=j;i++)assert(bases[j][i]===(i===j?-1n:0n),'weighted triangular leading -q^j');
assert(shadows4096[3][0]===-2n&&shadows4096.slice(0,3).every(x=>x[0]===0n),'weighted shadow constant -2d3/4096');
assert(bases[2][2]===-1n&&shadows4096[2][2]===8192n,'harmonic shadow/roots factor -2');
assert(bases[2][3]===24n,'harmonic norm3/roots factor -24');

const v=()=>Array(24).fill(0),dot=(x,y)=>x.reduce((s,t,i)=>s+t*y[i],0);
const roots=[];
for(let part=0;part<3;part++)for(let i=0;i<8;i++)for(let j=i+1;j<8;j++)for(const si of [1,-1])for(const sj of [1,-1]){const x=v();x[8*part+i]=si;x[8*part+j]=sj;roots.push(x);}
const countBits=mask=>{let n=0;for(let i=0;i<8;i++)n+=mask>>i&1;return n;};
for(let mask=0;mask<256;mask++)if(countBits(mask)%2===0){const x=v();for(let i=0;i<8;i++)x[i]=mask>>i&1?-.5:.5;roots.push(x);}
assert(roots.length===464&&roots.every(x=>dot(x,x)===2),'all norm2 roots of E8 + odd U16');
const chars=[];
for(let part=1;part<=2;part++)for(let mask=0;mask<256;mask++)if(countBits(mask)%2===1){const x=v();for(let i=0;i<8;i++)x[8*part+i]=mask>>i&1?-1:1;chars.push(x);}
for(let i=0;i<8;i++)for(let j=0;j<8;j++)for(const si of [1,-1])for(const sj of [1,-1]){const x=v();x[8+i]=2*si;x[16+j]=2*sj;chars.push(x);}
const glueA=v(),glueB=v();for(let i=0;i<8;i++){glueA[8+i]=.5;glueB[16+i]=.5;}glueA[16]=1;glueB[8]=1;
assert(dot(glueA,glueA)===3&&dot(glueB,glueB)===3&&dot(glueA,glueB)===1,'odd U16 glue');
for(const x of chars){assert(dot(x,x)===8,'characteristic norm8');for(const r of roots)assert(dot(x,r)%2===0,'root characteristic parity');for(const g of [glueA,glueB])assert((dot(x,g)-3)%2===0,'odd glue characteristic parity');}
assert(chars.length===512&&chars.length===48+roots.length,'actual shell count');
const R=Array.from({length:24},()=>v()),M=Array.from({length:24},()=>v());
for(const r of roots)for(let i=0;i<24;i++)for(let j=0;j<24;j++)R[i][j]+=r[i]*r[j];
for(const x of chars)for(let i=0;i<24;i++)for(let j=0;j<24;j++)M[i][j]+=x[i]*x[j]/4;
let wrong=0;for(let i=0;i<24;i++)for(let j=0;j<24;j++){
  assert(R[i][j]===(i===j?(i<8?60:28):0),'root moment block diagonal');
  assert(M[i][j]===(i===j?(i<8?0:64):0),'shadow moment block diagonal');
  assert(M[i][j]===(i===j?4+464/4:0)-2*R[i][j],'correct universal harmonic operator');
  if(M[i][j]!==((i===j?4:0)+R[i][j]))wrong++;
}
assert(wrong===24,'candidate 4I+R falsified on every diagonal');
const out={exact:true,scope:'harmonic theta normalization and a true explicit lattice counter-test, no physical graph exclusion',
  weighted_basis_q0_q3:bases.map(x=>x.slice(0,4).map(String)),weighted_shadow_common4096:shadows4096.map(x=>x.map(String)),
  harmonic_ratio:-2,correct_operator:'(4+r/4)I - 2R',wrong_operator:'4I+R',norm3_operator:'(512+2r)I - 24R',
  positive:{lattice:'E8 orthogonal [D8^2+<(s,v),(v,s)>]',rank:24,min:2,odd:true,unimodular:true,roots:464,characteristics8:512,
    root_moment_diagonal:R.map((x,i)=>x[i]),shadow_moment_diagonal:M.map((x,i)=>x[i]),wrong_operator_diagonals:wrong},
  source_sha256:createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};
fs.writeFileSync(path.join(here,'verifier_moments_caracteristique8.json'),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({exact:true,harmonic_ratio:-2,roots:464,characteristics8:512,candidate_plus_R_falsified:true}));
