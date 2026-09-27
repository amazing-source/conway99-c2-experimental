import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const assert=(p,m)=>{if(!p)throw new Error(m);};
const pop=x=>{let n=0;while(x){x&=x-1;n++;}return n;};
function rank2(rows,ncols){
  const a=rows.slice();let r=0;
  for(let j=0;j<ncols;j++){
    const p=a.findIndex((x,i)=>i>=r&&((x>>>j)&1));if(p<0)continue;
    [a[r],a[p]]=[a[p],a[r]];
    for(let i=0;i<a.length;i++)if(i!==r&&((a[i]>>>j)&1))a[i]^=a[r];r++;
  }
  return r;
}

// Sept classes non nulles de V/<1>=F2^3. Les multiplicites sont <=3.
const profiles={},oddCardCounts={};
let multisets=0;
function walk(c,left){
  if(c.length===7){
    if(left)return;let sum=0,odd=0;
    for(let i=0;i<7;i++)if(c[i]&1){sum^=i+1;odd++;}
    if(sum)return;multisets++;oddCardCounts[odd]=(oddCardCounts[odd]||0)+1;
    assert(odd===3||odd===7,'nombre impair de supports');
    const profile=c.filter(Boolean).sort((a,b)=>b-a).join(',');
    profiles[profile]=(profiles[profile]||0)+1;return;
  }
  for(let n=0;n<=Math.min(3,left);n++)walk([...c,n],left-n);
}
walk([],7);
const expected=['3,3,1','3,2,1,1','2,2,1,1,1','1,1,1,1,1,1,1'];
assert(Object.keys(profiles).every(p=>expected.includes(p)),'profils couvrants');

// Inversion Fourier du cas sept supports distincts.
const polarities=[];
for(let m=0;m<128;m++){
  const sigma=Array.from({length:7},(_,i)=>(m>>i)&1?-1:1);
  const sums=Array.from({length:8},(_,x)=>sigma.reduce((s,t,i)=>s+t*((pop((i+1)&x)&1)?-1:1),0));
  const multiplicities=sums.map(s=>3+s);
  if(multiplicities.some(n=>n<0))continue;
  if(sums.some((s,x)=>multiplicities[x]>0&&s!==1&&s!==5))continue;
  assert(sums.filter(s=>s===5).length===1,'type unique gros huit');
  assert(sums.filter(s=>s===1).length===4,'quatre tetrades');
  assert(sums.filter(s=>s===-3).length===3,'trois types absents');
  const labels=[];for(let x=0;x<8;x++)for(let k=0;k<multiplicities[x];k++)labels.push(x);
  assert(labels.length===24,'vingt-quatre coordonnees');
  const octads=Array.from({length:7},(_,i)=>labels.reduce((w,x,j)=>{
    const bit=sigma[i]*((pop((i+1)&x)&1)?-1:1)===-1;return bit?w|(1<<j):w;
  },0));
  assert(octads.every(w=>pop(w)===8),'sept poids huit');
  assert(rank2(octads,24)===4,'rang quatre');
  const A=labels.reduce((w,x,j)=>sums[x]===5?w|(1<<j):w,0);
  assert(pop(A)===8&&octads.includes(A),'A est une des octades');
  polarities.push({mask:m,multiplicities,octad_index_of_A:octads.indexOf(A)});
}
assert(polarities.length===56,'cinquante-six polarites couvrantes');

// Notre code propre 0803, reconstruit sans appel au producteur de domaines.
const exponents=[0,1,5,6,7,9,11];
const gp=exponents.reduce((w,e)=>w|(1<<e),0);
const generators=Array.from({length:12},(_,i)=>{let w=gp<<i;if(pop(w)&1)w|=1<<23;return w;});
assert(rank2(generators,24)===12,'rang code');
for(const g of generators)for(const h of generators)assert((pop(g&h)&1)===0,'code autodual');
const words=[];for(let m=0;m<4096;m++){
  let w=0;for(let i=0;i<12;i++)if((m>>i)&1)w^=generators[i];words.push(w);
}
assert(new Set(words).size===4096,'4096 mots');
const weightHist={};for(const w of words)weightHist[pop(w)]=(weightHist[pop(w)]||0)+1;
assert(Math.min(...words.filter(Boolean).map(pop))===8,'minimum huit');
const D1=[0,1,2,9],D2=[3,4,13,15];
const A=[...D1,...D2].reduce((w,j)=>w|(1<<j),0);
const syndrome=generators.map(g=>pop(g&A)&1);
assert(pop(A)===8&&A===41503&&!words.includes(A),'gros support hors code');
const offendingIndex=syndrome.indexOf(1);assert(offendingIndex>=0,'certificat dual');
const result={exact:true,
  scope:'Lemme sept appuis de rang binaire <=4 et paire de normales fixe 0803. Aucun balayage de septuplets.',
  quotient_classes:7,multiplicity_bound:3,multisets_with_odd_xor_zero:multisets,
  odd_support_cardinalities:oddCardCounts,multiplicity_profiles:profiles,
  polarities_tested:128,admissible_polarities:polarities.length,polarities,
  binary_generator_exponents:exponents,generators,code_weight_histogram:weightHist,
  large_coefficient_support:{D1,D2,mask:A,in_code:false,syndrome,
    offending_generator_index:offendingIndex,offending_generator_mask:generators[offendingIndex]},
  physical_seven_support_minimum_binary_rank_for_this_pair:5,
  remaining_scope:'Support ranks 5,6,7 and other normal pairs are not excluded.'};
const here=path.dirname(fileURLToPath(import.meta.url));
fs.writeFileSync(path.join(here,'controle_sept_octades_rang4.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({exact:true,profiles,polarities:polarities.length,A,
  offending_generator:generators[offendingIndex],required_support_rank:5}));
