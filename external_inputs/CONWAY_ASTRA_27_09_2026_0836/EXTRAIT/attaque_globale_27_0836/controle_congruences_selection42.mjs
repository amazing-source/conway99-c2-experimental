import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const input=JSON.parse(fs.readFileSync(path.join(here,'controle_selection42_golay.json'),'utf8'));
const assert=(p,m)=>{if(!p)throw new Error(m);};
const mod2=x=>(x%2+2)%2;
const mod16=x=>(x%16+16)%16;
const pop=x=>{let n=0;while(x){x&=x-1;n++;}return n;};
const signs=c=>Array.from({length:24},(_,j)=>1-2*((c>>>j)&1));
const generators=input.code.generator_masks;
const code=new Set();for(let m=0;m<4096;m++){
  let w=0;for(let i=0;i<12;i++)if((m>>i)&1)w^=generators[i];code.add(w);
}
const mask=row=>row.reduce((w,x,j)=>w|(mod2(x)<<j),0);
const dot=(a,b)=>a.reduce((s,x,j)=>s+x*b[j],0);
const B=input.B;
const d=B.map(row=>row.map(x=>mod2((1-x)/2)));
const k=B.map((row,i)=>row.map((x,j)=>(x-1+2*d[i][j])/4));
assert(d.every(row=>code.has(mask(row))),'d_i dans code');
assert(k.every(row=>row.every(Number.isInteger)),'k_i entiers');
const delta=d[0].map((x,j)=>x+d[1][j]);
const K=k[0].map((x,j)=>x+k[1][j]);
function audit(witness){
  const S=witness.selected_codeword_masks,E=S.map(signs);
  assert(S.length===42&&new Set(S).size===42,'selection42');
  const n=Array.from({length:24},(_,j)=>S.reduce((s,c)=>s+((c>>>j)&1),0));
  const F=Array.from({length:24},(_,j)=>Array.from({length:24},(_,h)=>
    (j===h?56:0)-E.reduce((s,row)=>s+row[j]*row[h],0)-B[0][j]*B[0][h]-B[1][j]*B[1][h]));
  const Qintegral=F.every(row=>row.every(x=>x%4===0));
  const tau=mod2(n[0]+delta[0]);
  const xorOK=n.every((x,j)=>mod2(x+delta[j])===tau);
  assert(Qintegral===xorOK,'equivalence XOR entier');
  const output={selected42_masks:S,Q_integral:Qintegral,xor_condition:xorOK,
    number_dodecads:S.filter(c=>pop(c)===12).length,
    characteristic_sum_mod16:mod16(E.reduce((s,row)=>s+row.reduce((a,b)=>a+b,0),0)
      +B.flat().reduce((s,x)=>s+x,0))};
  if(!Qintegral)return output;
  const Q=F.map(row=>row.map(x=>x/4));
  const a=n.map((x,j)=>(x+delta[j]-tau)/2);
  const single=a.map((x,j)=>x+K[j]);
  const singleMask=mask(single);
  const rows=Q.map(mask);
  for(let j=0;j<24;j++)for(const g of generators){
    const gb=Array.from({length:24},(_,i)=>(g>>>i)&1);
    assert(mod2(dot(Q[j],gb))===mod2(dot(single,gb)),'syndrome identique sur24lignes');
  }
  assert(rows.every(r=>code.has(r))===code.has(singleMask),'condition mot unique');
  const x=Array.from({length:24},(_,j)=>(E.reduce((s,row)=>s+row[j],0)+B[0][j]+B[1][j])/2);
  assert(x.every(z=>mod2(z)===tau),'parite demi-caracteristique');
  const halfMask=mask(x.map(z=>(z-tau)/2));
  assert(code.has(halfMask)===code.has(singleMask),'code demi-caracteristique');
  Object.assign(output,{tau,one_codeword_mask:singleMask,one_codeword_in_code:code.has(singleMask),
    all_Q_rows_in_code:rows.every(r=>code.has(r)),Q_row_syndromes_verified:24*12,
    half_characteristic_codeword_mask:halfMask,
    half_characteristic_sum_mod8:((x.reduce((s,z)=>s+z,0)%8)+8)%8});
  return output;
}
const witnesses={wrong_xor:audit(input.witness_wrong_xor),
  correct_xor_wrong_rows:audit(input.witness_correct_xor_wrong_Q_rows)};
assert(!witnesses.wrong_xor.Q_integral,'premier temoin');
assert(witnesses.correct_xor_wrong_rows.one_codeword_mask===7218972,'mot imprime');
assert(witnesses.correct_xor_wrong_rows.characteristic_sum_mod16===8,'checksum passe');
const result={exact:true,scope:'Deux selections existantes uniquement ; aucune nouvelle recherche de graphe.',
  d_masks:d.map(mask),generators,witnesses,
  theorem:'Q integral iff XOR; Q rows in C iff one class in C; physical characteristic checksum is 8 mod16.',
  limitations:'Degree ten, CT and common-neighbor budgets are not asserted for the witnesses.'};
fs.writeFileSync(path.join(here,'controle_congruences_selection42.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({exact:true,word:witnesses.correct_xor_wrong_rows.one_codeword_mask,
  all24syndromes_verified:true,dodecads:witnesses.correct_xor_wrong_rows.number_dodecads,
  checksum:witnesses.correct_xor_wrong_rows.characteristic_sum_mod16}));
