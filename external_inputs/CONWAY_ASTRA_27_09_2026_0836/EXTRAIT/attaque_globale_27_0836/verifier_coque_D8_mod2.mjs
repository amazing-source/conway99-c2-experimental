import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';import {createHash} from 'node:crypto';
const here=path.dirname(fileURLToPath(import.meta.url));const assert=(x,s)=>{if(!x)throw new Error(s);};
const C=[];for(let i=0;i<7;i++)for(let j=i+1;j<7;j++)for(const sign of [1,-1]){const col=Array(7).fill(0);col[i]=1;col[j]=sign;C.push(col);}
let integerCzChecks=0;for(let i=0;i<7;i++){
  let found=false;for(let a=0;a<42&&!found;a++)for(let b=a+1;b<42;b++){
    const plus=C[a].map((x,k)=>x+C[b][k]);const minus=C[a].map((x,k)=>x-C[b][k]);
    for(const sum of [plus,minus])if(sum.every((x,k)=>x===(k===i?2:0))){found=true;integerCzChecks++;break;}
    if(found)break;
  }assert(found,'every block has two signed sisters giving Cz=2e_i');
}
const words=[];for(let i=0;i<8;i++)for(let j=0;j<8;j++)for(let k=0;k<8;k++)words.push((1<<i)|(1<<(8+j))|(1<<(16+k)));
function basis(words,width){const piv=Array(width).fill(0),rows=[];for(const value of words){let x=value;for(let j=width-1;j>=0;j--)if(x>>>j&1){if(piv[j])x^=piv[j];else{piv[j]=x;rows.push(x);break;}}}return rows;}
const rows=basis(words,24);assert(rows.length===22,'parity span22');
const parity=x=>{let p=0;while(x){p^=x&1;x>>>=1;}return p;};
const gram=rows.map(a=>rows.reduce((mask,b,j)=>mask|(parity(a&b)<<j),0));
const gramRank=basis(gram,rows.length).length;assert(gramRank===20,'Gram modulo2 rank20');
const block0=255,block1=255<<8,block2=255<<16,rad=[block0^block1,block1^block2];
for(const r of rad){assert(words.every(x=>parity(r&x)===0),'radical orthogonal to all shell words');assert(basis([...rows,r],24).length===22,'radical contained in span');}
assert(basis(rad,24).length===2,'radical dimension2');
const out={exact:true,scope:'D8^3 shell parity Gram and integer D7 generator coefficients; no general shell rank bound',
  D7_columns:C.length,integer_Cz_checks:integerCzChecks,parity_words:words.length,coordinate_rank:rows.length,Gram_rank_mod2:gramRank,
  radical_dimension:2,required_physical_Gram_rank:22,frame_excluded:true,
  source_sha256:createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};
fs.writeFileSync(path.join(here,'verifier_coque_D8_mod2.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out));
