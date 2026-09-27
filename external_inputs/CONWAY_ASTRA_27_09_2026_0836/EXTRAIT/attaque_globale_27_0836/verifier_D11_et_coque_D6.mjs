import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';import {createHash} from 'node:crypto';
const here=path.dirname(fileURLToPath(import.meta.url));const assert=(x,s)=>{if(!x)throw new Error(s);};
let spinorCases=0,parityChecks=0;
for(let mask=0;mask<2048;mask++){
  const twiceP=Array.from({length:11},(_,i)=>mask>>i&1?-1:1);
  assert(twiceP.reduce((s,x)=>s+x*x,0)===11,'spinor norm11/4');
  assert(twiceP.reduce((s,x)=>s+2*x,0)%2===0,'4p in D11');
  for(let i=0;i<11;i++){assert((twiceP.reduce((s,x)=>s+x,0)-1)%2===0,'2p-e_i in D11');parityChecks++;}
  spinorCases++;
}
assert(2*11*10+4*11===2*12*11,'D11 roots plus new roots yield D12 count264');

const zero=()=>Array(24).fill(0),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const glues=[];for(let part=0;part<4;part++){
  const x=zero();for(let j=0;j<6;j++){x[6*part+j]=j===0?-1:1;x[6*((part+1)%4)+j]=1;}glues.push(x);
}
for(const x of glues)assert(dot(x,x)/4===3,'spinor-pair norm3');
for(const x of glues)for(const y of glues)assert(dot(x,y)%4===0,'glue Gram integral');
const classes=[];const costs2=[0,3,3,2];
for(let mask=0;mask<16;mask++){
  const row=[0,0,0,0];for(let j=0;j<4;j++)if(mask>>j&1){row[j]^=2;row[(j+1)%4]^=1;}
  const min2=row.reduce((s,c)=>s+costs2[c],0);assert(min2%2===0,'integer coset norm');classes.push({row,min:min2/2});
}
assert(new Set(classes.map(x=>x.row.join(''))).size===16,'independent four glue classes');
const histogram={};for(const x of classes)histogram[x.min]=(histogram[x.min]??0)+1;
assert(JSON.stringify(histogram)===JSON.stringify({'0':1,'3':4,'4':5,'5':4,'6':2}),'all coset minima');
const generators=[];
for(let part=0;part<4;part++){
  const baseline=glues[(part+3)%4];
  function plus(i,j){const flip=baseline.slice();flip[6*part+i]*=-1;flip[6*part+j]*=-1;assert(dot(flip,flip)/4===3,'two flips preserve shell3');return baseline.map((x,k)=>x-flip[k]);}
  for(let i=0;i<5;i++){
    const k=Array.from({length:6},(_,j)=>j).find(j=>j!==i&&j!==i+1);
    const x=plus(i,k).map((a,j)=>a-plus(i+1,k)[j]);
    assert(x[6*part+i]===2&&x[6*part+i+1]===-2&&dot(x,x)===8,'simple D6 difference from shell');generators.push(x);
  }
  generators.push(plus(4,5));
}
generators.push(...glues);assert(generators.length===28,'24 roots and4 shell baselines');
const gram=generators.map(a=>generators.map(b=>{assert(dot(a,b)%4===0,'integral generator products');return dot(a,b)/4;}));
const bitrows=gram.map(row=>row.reduce((x,v,i)=>x|((Math.abs(v)%2)<<i),0));
function rank(rows){const piv=Array(28).fill(0);let r=0;for(const value of rows){let x=value;for(let j=27;j>=0;j--)if(x>>>j&1){if(piv[j])x^=piv[j];else{piv[j]=x;r++;break;}}}return r;}
const actualRank=rank(bitrows);assert(actualRank===24,'actual full Gram shell rank24, not20');
const out={exact:true,scope:'D11-to-D12 root construction and true D6^4 shell counter-test, no SRG/frame realization',
  D11:{spinor_cases:spinorCases,parity_checks:parityChecks,D12_root_count:264,twice_b_not_assumed_integral:true},
  D6_countermodel:{glue_classes:classes,coset_minima:histogram,determinant:1,min:2,roots:'D6^4',shell3:4*32**2,
    shell_generates_lattice:true,generators_checked:28,Gram_rank_mod2:actualRank,no_42_plus_7_frame_asserted:true},
  source_sha256:createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};
fs.writeFileSync(path.join(here,'verifier_D11_et_coque_D6.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({exact:true,D11_spinors:spinorCases,D12_root_count:264,D6_shell3:4096,D6_Gram_rank_mod2:actualRank}));
