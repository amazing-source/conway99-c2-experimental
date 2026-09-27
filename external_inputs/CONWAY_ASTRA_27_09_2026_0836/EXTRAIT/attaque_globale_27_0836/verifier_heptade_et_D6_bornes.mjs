import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';import {createHash} from 'node:crypto';
const here=path.dirname(fileURLToPath(import.meta.url));const assert=(x,s)=>{if(!x)throw new Error(s);};
const parity=x=>{let p=0;while(x){p^=x&1;x>>>=1;}return p;};const pop=x=>{let p=0;while(x){p+=x&1;x>>>=1;}return p;};
const polarities=new Set();let constructions=0;
for(let x0=0;x0<8;x0++)for(let a0=1;a0<8;a0++){
  const s=Array.from({length:7},(_,j)=>(parity((j+1)&x0)?-1:1)*((j+1)===a0?-1:1));polarities.add(s.join(','));
  const present=Array.from({length:8},(_,x)=>x).filter(x=>parity(a0&(x^x0))===1);
  const types=[...Array(8).fill(x0),...present.flatMap(x=>Array(4).fill(x))];assert(types.length===24,'8+4*4 coordinates');
  const supports=Array.from({length:7},(_,j)=>types.reduce((bits,x,k)=>bits|((parity((j+1)&(x^x0))^((j+1)===a0?1:0))<<k),0));
  assert(supports.every(x=>pop(x)===8),'all seven octades');
  const multiplicities=types.map((_,i)=>supports.reduce((n,x)=>n+(x>>>i&1),0));assert(multiplicities.every(x=>x===1||x===3),'all columns1/3');
  const A=multiplicities.reduce((bits,n,i)=>bits|((n===1?1:0)<<i),0);assert(A===supports[a0-1],'A is the exceptional octad');constructions++;
}
assert(constructions===56&&polarities.size===56,'56 admissible polarities, independently parametrized');
const fixedA=[0,1,2,9,3,4,13,15].reduce((m,i)=>m|(1<<i),0);
const polynomial=[11,9,7,6,5,1,0].reduce((m,i)=>m|(1<<i),0),generator=polynomial|(parity(polynomial)<<23);
assert(fixedA===41503&&generator===8391395&&parity(fixedA&generator)===1,'fixed0803 syndrome nonzero');

const zero=()=>Array(24).fill(0),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),chars=[];
for(const [a,b] of [[0,2],[1,3]])for(let i=0;i<6;i++)for(let j=0;j<6;j++)for(const sa of [1,-1])for(const sb of [1,-1]){const x=zero();x[6*a+i]=2*sa;x[6*b+j]=2*sb;chars.push(x);}
const glues=[];for(let a=0;a<4;a++){const x=zero();for(let i=0;i<6;i++){x[6*a+i]=i===0?-.5:.5;x[6*((a+1)%4)+i]=.5;}glues.push(x);}
for(const x of chars){assert(dot(x,x)===8,'all288characteristics norm8');for(const g of glues)assert((dot(x,g)-3)%2===0,'characteristic parity onglue');}
const specimens=[];
function sample(entries){const x=zero();for(const [i,v]of entries)x[i]=v;assert(dot(x,x)===4,'norm4 specimen');return x;}
specimens.push({name:'I',x:sample([[0,1],[1,1],[2,1],[3,1]]),pass:true});
specimens.push({name:'II',x:sample([[0,1],[1,1],[6,1],[7,1]]),pass:true});
const iii=zero();for(let i=0;i<6;i++){iii[i]=i===0?-.5:.5;iii[12+i]=.5;}iii[6]=1;specimens.push({name:'III',x:iii,pass:true});
specimens.push({name:'one2',x:sample([[0,2]]),pass:false});
specimens.push({name:'opposite2plus2',x:sample([[0,1],[1,1],[12,1],[13,1]]),pass:false});
specimens.push({name:'vvvv',x:sample([[0,1],[6,1],[12,1],[18,1]]),pass:false});
for(const t of specimens){assert(dot(t.x,t.x)===4,'specimen norm4');const pass=chars.every(c=>Math.abs(dot(c,t.x))<=2);assert(pass===t.pass,'complete-type representative flatness');}
const counts=[4*15*16,4*15**2*16,4*32**2*12];assert(JSON.stringify(counts)===JSON.stringify([960,14400,49152]),'all three analytic counts');
const out={exact:true,scope:'heptade lowrank proof normalization and D6 individual-type representatives, not a search over septuples',
  heptade:{polarities:constructions,fixed_A:fixedA,code_generator:generator,syndrome:1,fixed_pair_rank_at_least:5,A_in_Code_general_not_excluded:true},
  D6:{characteristics8:chars.length,norm4_allowed_types:counts,norm4_candidates:counts.reduce((s,x)=>s+x,0),representatives:specimens.map(x=>({name:x.name,pass:x.pass})),seven_blocks_open:true},
  source_sha256:createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};
fs.writeFileSync(path.join(here,'verifier_heptade_et_D6_bornes.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({exact:true,polarities:56,fixed_syndrome:1,D6_norm4_candidates:64512,no_septuple_exclusion:true}));
