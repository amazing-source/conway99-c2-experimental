// Exact, bounded formal-series check. It does not replace the Poisson/valence proof.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';

const here=path.dirname(fileURLToPath(import.meta.url));
const N=8;
const assert=(test,message)=>{if(!test)throw new Error(message);};
const zero=()=>Array(N+1).fill(0n);
const unit=()=>{const a=zero();a[0]=1n;return a;};
const add=(a,b)=>a.map((x,i)=>x+b[i]);
const scale=(a,c)=>a.map(x=>x*BigInt(c));
function mul(a,b){const c=zero();for(let i=0;i<=N;i++)for(let j=0;i+j<=N;j++)c[i+j]+=a[i]*b[j];return c;}
function pow(a,k){let c=unit();for(let i=0;i<k;i++)c=mul(c,a);return c;}
function divide(a,d){const D=BigInt(d);assert(a.every(x=>x%D===0n),'nonintegral exact division');return a.map(x=>x/D);}
const equal=(a,b)=>a.every((x,i)=>x===b[i]);
const strings=a=>a.map(String);
const sha=bytes=>createHash('sha256').update(bytes).digest('hex');

const theta3=unit(),theta4=unit(),s=zero();
for(let n=1;n*n<=N;n++){theta3[n*n]=2n;theta4[n*n]=n%2?-2n:2n;}
for(let n=0;n*(n+1)<=N;n++)s[n*(n+1)]+=1n;
const A=zero(),s4=pow(s,4);
for(let i=0;i<N;i++)A[i+1]=16n*s4[i];
const B=pow(theta4,4),C=pow(theta3,4);
assert(equal(C,add(A,B)),'Jacobi theta3^4 = theta2^4 + theta4^4');
const delta=divide(mul(A,B),16);
assert(delta[1]===1n&&delta[2]===-8n&&delta[3]===28n,'Delta8 normalization');

const base=[];
for(let j=0;j<=3;j++)base.push(mul(pow(theta3,24-8*j),pow(delta,j)));
for(let j=0;j<=3;j++)for(let i=0;i<=j;i++)assert(base[j][i]===(i===j?1n:0n),'triangular orders q^j');

// The four TS transforms, with common denominator 4096.
const shadow4096=[
  scale(pow(A,6),4096),
  scale(mul(pow(A,4),mul(B,C)),-256),
  scale(mul(pow(A,2),mul(pow(B,2),pow(C,2))),16),
  scale(mul(pow(B,3),pow(C,3)),-1),
];
const combine=(parts,coeff)=>parts.reduce((a,b,i)=>add(a,scale(b,coeff[i])),zero());
assert(base[0][1]===48n&&base[1][1]===1n,'coefficient a=-48');
assert(base[0][2]===1104n&&base[1][2]===24n&&base[2][2]===1n,'roots=b-48');
assert(base[0][3]-48n*base[1][3]===4096n&&base[2][3]===0n,'universal shell3=4096 when c=0');
assert(shadow4096[3][0]===-1n&&shadow4096.slice(0,3).every(a=>a[0]===0n),'constant=-c/4096');
assert(shadow4096[2][2]===4096n&&shadow4096[0][2]===0n&&shadow4096[1][2]===0n,'shadow q^2=b when c=0');
assert(shadow4096.every(a=>a.every((x,i)=>i%2===0||x===0n)),'shadow exponents even');

const old=path.resolve(here,'../attaque_globale_27_0803');
const positiveFile=path.join(old,'verifier_golay_enveloppe_indep.json');
const positiveBytes=fs.readFileSync(positiveFile);
const positive=JSON.parse(positiveBytes);
assert(positive.exact===true&&positive.word_count===4096&&positive.weights['8']===759,'frozen true Golay positive');
assert(positive.shell3_L===4096,'frozen shell3');

const golayTheta=combine(base,[1,-48,48,0]);
const golayShadow=divide(combine(shadow4096,[1,-48,48,0]),4096);
const directShell4=BigInt(positive.weights['8'])*128n+4n*24n*23n/2n;
assert(golayTheta[0]===1n&&golayTheta[1]===0n&&golayTheta[2]===0n,'odd positive min3');
assert(golayTheta[3]===4096n&&golayTheta[4]===directShell4&&directShell4===98256n,'independent norm4 octad/sign and 4^2 count');
assert(golayShadow[2]===48n,'48 explicit +/-sqrt(8)e_i characteristics');
const D8cubeTheta=combine(base,[1,-48,384,0]);
assert(D8cubeTheta[2]===336n&&D8cubeTheta[3]===4096n&&D8cubeTheta[4]===90192n,'D8^3 glue shell counts agree with exact series');

const e8=divide(add(add(pow(A,2),pow(B,2)),pow(C,2)),2);
const evenTheta=pow(e8,3);
assert(equal(evenTheta,combine(base,[1,-48,768,-4096])),'even E8^3 boundary coefficients');
const evenShadow=divide(combine(shadow4096,[1,-48,768,-4096]),4096);
assert(equal(evenTheta,evenShadow)&&evenShadow[0]===1n,'even boundary shadow includes zero');
assert(evenTheta[2]===720n,'even boundary roots 720');

// SL2(F2), the three left cosets H\G for H={I,S}.
const mm=(a,b)=>[(a[0]*b[0]+a[1]*b[2])%2,(a[0]*b[1]+a[1]*b[3])%2,(a[2]*b[0]+a[3]*b[2])%2,(a[2]*b[1]+a[3]*b[3])%2];
const I=[1,0,0,1],S=[0,1,1,0],T=[1,1,0,1];
const reps=[I,T,mm(T,S)];
const cosets=reps.map(r=>[r,mm(S,r)].map(x=>x.join('')).sort());
const six=new Set(cosets.flat());assert(six.size===6,'three disjoint cosets in SL2(F2)');

const inputBindings=[positiveFile,path.join(old,'controles_positifs_cadre_global.json')].map(p=>({file:path.relative(here,p).replaceAll('\\','/'),sha256:sha(fs.readFileSync(p))}));
const output={
  exact:true,scope:'finite exact series and normalization checks; analytic proof is in THEOREME_CARACTERISTIQUE8_THETA.md',
  truncation_q:N,theta3:strings(theta3),theta4:strings(theta4),A:strings(A),delta8:strings(delta),
  basis_q0_q3:base.map(a=>strings(a.slice(0,4))),shadow_basis_common4096:shadow4096.map(strings),
  universal_formula:{a:-48,c:0,b:'48 + number of norm2 vectors',number_characteristics_norm8:'b'},
  golay_positive:{theta:strings(golayTheta),shadow:strings(golayShadow),shell4_direct:String(directShell4),characteristics_norm8:48},
  D8_cube_positive:{coefficients:[1,-48,384,0],theta:strings(D8cubeTheta),roots:336,shell3:4096,shell4:90192},
  even_boundary:{coefficients:[1,-48,768,-4096],theta:strings(evenTheta),shadow_constant:1},
  cosets_mod2:cosets,input_bindings:inputBindings,source_sha256:sha(fs.readFileSync(fileURLToPath(import.meta.url))),
  no_shadowframe_claim:true,no_graph_exclusion:true,
};
fs.writeFileSync(path.join(here,'verifier_theta_caracteristique8.json'),JSON.stringify(output,null,2)+'\n');
console.log(JSON.stringify({exact:true,basis_dimension_proved_in_note:4,golay_characteristics8:48,golay_shell4:String(directShell4),even_shadow_constant:1,no_shadowframe_claim:true}));
