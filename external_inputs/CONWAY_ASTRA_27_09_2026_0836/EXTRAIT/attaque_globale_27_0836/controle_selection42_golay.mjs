// Sélections42+7 dans l'enveloppe Golay explicite du fil.
// 4096 mots seulement; aucun solveur, aucun graphe SRG construit.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const check=(ok,label)=>{if(!ok)throw Error(label);};
const pop=n=>{let k=0;while(n){n&=n-1;k++;}return k;};
const ALL=(1<<24)-1;
const poly=[11,9,7,6,5,1,0].reduce((s,k)=>s|(1<<k),0);
const code=[];
for(let m=0;m<4096;m++){
  let c=0;for(let i=0;i<12;i++)if((m>>>i)&1)c^=poly<<i;
  c|=(pop(c)&1)<<23;code.push(c);
}
const codeSet=new Set(code);
const generators=Array.from({length:12},(_,i)=>code[1<<i]);
check(codeSet.size===4096,'code4096');
check(code.every(c=>[0,8,12,16,24].includes(pop(c))),'poids du code');
check(generators.every(a=>generators.every(b=>pop(a&b)%2===0)),'code autodual');
const Vindices=[0,1,3,4,5,6,7,8,10,11,12,14];
const V=Vindices.reduce((s,k)=>s|(1<<k),0);
const D=[0,1,2,9],Dp=[3,4,13,15];
const b1=Array.from({length:24},(_,j)=>D.includes(j)?-3:1);
const b2=Array.from({length:24},(_,j)=>(((V>>>j)&1)?-1:1)*(Dp.includes(j)?-3:1));
const signs=c=>Array.from({length:24},(_,j)=>1-2*((c>>>j)&1));
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
check(codeSet.has(V),'V dans code');
check(dot(b1,b1)===56&&dot(b2,b2)===56&&dot(b1,b2)===0,'deux y norm7');
const shell=code.filter(c=>dot(signs(c),b1)===0&&dot(signs(c),b2)===0);
check(shell.length===704,'shell704');
const canonical=shell.filter(c=>c<(c^ALL)).sort((a,b)=>a-b),canSet=new Set(canonical);
check(canonical.length===352,'sans antipodes');
const xor=S=>S.reduce((a,c)=>a^c,0);
const modulus=101;
const power=(x,k)=>{let a=1;while(k){if(k&1)a=a*x%modulus;x=x*x%modulus;k>>=1;}return a;};
const pivots=[],basis=[];
for(const c of canonical){
  let r=signs(c).map(x=>(x+modulus)%modulus);
  for(const p of pivots){const z=r[p.col];if(z)r=r.map((x,j)=>(x-z*p.row[j]%modulus+modulus)%modulus);}
  const col=r.findIndex(x=>x);if(col<0)continue;
  const z=power(r[col],modulus-2);r=r.map(x=>x*z%modulus);
  pivots.push({col,row:r});basis.push(c);if(basis.length===22)break;
}
check(basis.length===22,'rang22 modulo101');
const basisSet=new Set(basis),others=canonical.filter(c=>!basisSet.has(c));
function defect(S){
  const E=S.map(signs);
  const F=Array.from({length:24},(_,j)=>Array.from({length:24},(_,k)=>
    (j===k?56:0)-E.reduce((s,r)=>s+r[j]*r[k],0)-b1[j]*b1[k]-b2[j]*b2[k]));
  if(F.some(r=>r.some(x=>x%4))){
    const j=F.findIndex(r=>r.some(x=>x%4)),k=F[j].findIndex(x=>x%4);
    return{integral:false,F,nonintegral_entry:{row:j,column:k,numerator:F[j][k],denominator:4}};
  }
  const Q=F.map(r=>r.map(x=>x/4));
  const row_masks=Q.map(r=>r.reduce((m,x,j)=>m|(((x%2+2)%2)<<j),0));
  const rows_not_in_code=row_masks.flatMap((c,j)=>codeSet.has(c)?[]:[j]);
  let first_bad_row_certificate;
  if(rows_not_in_code.length){
    const j=rows_not_in_code[0],k=generators.findIndex(g=>pop(g&row_masks[j])%2);
    check(k>=0,'syndrome horscode');
    first_bad_row_certificate={row:j,row_mask:row_masks[j],generator_number:k,
      generator_mask:generators[k],intersection_parity:1};
  }
  return{integral:true,Q,row_masks,rows_not_in_code,first_bad_row_certificate};
}
const badXor=[...basis,...others.slice(0,20)];
check(xor(badXor)!==V&&xor(badXor)!==(V^ALL),'sélectionXOR fausse');
check(!defect(badXor).integral,'Q non entier');
let badRows;
for(let shift=0;shift<32&&!badRows;shift++){
  const base=[...basis,...others.slice(shift,shift+18)],used=new Set(base),target=xor(base)^V;
  for(const c of canonical){
    const d=c^target;
    if(c!==d&&canSet.has(d)&&!used.has(c)&&!used.has(d)){
      const S=[...base,c,d],r=defect(S);
      if(r.integral&&r.rows_not_in_code.length){badRows=S;break;}
    }
  }
}
check(badRows,'sélectionXOR correcte mais lignesQ incorrectes');
check(xor(badRows)===V,'XORV');
function certificate(S){
  check(new Set(S).size===42,'42 distincts');
  check(basis.every(c=>S.includes(c)),'contient22indépendants');
  const E=S.map(signs),histogram={};
  for(let i=0;i<42;i++)for(let j=i+1;j<42;j++){
    const n=dot(E[i],E[j]);check(n%8===0&&Math.abs(n)<=8,'Gram pair0/±1');
    const a=n/8;histogram[a]=(histogram[a]??0)+1;
  }
  const degree=E.map((r,i)=>E.filter((s,j)=>i!==j&&dot(r,s)!==0).length);
  return{selected_codeword_masks:S,basis22_masks:basis,
    exact_real_rank:22,rank_justification:'rang>=22mod101 et <=22 par les deux orthogonaux indépendants',
    pair_Gram_histogram:histogram,nonzero_pair_degrees:degree,
    xor_mask:xor(S),xor_allowed:xor(S)===V||xor(S)===(V^ALL),
    ...defect(S),
    limitations:'Normes3, orthogonalité aux deux y, span22 et pairings0/±1 seulement; degré10, CT et budgets SRG non revendiqués'};
}
// Un h de type coordonnées, de norme4 et orthogonal aux deux y, existe
// réellement dans l'enveloppe. Toute sélection physique contenant h est impossible.
const h=Array(24).fill(0);h[2]=4;h[9]=-4;
check(dot(h,h)===32&&dot(h,b1)===0&&dot(h,b2)===0,'h norm4 dans complément');
check(h.reduce((s,x)=>s+x,0)%8===0&&h.every(x=>x%4===0),'h dans réseau Golay');
const result={scope:'Filtres sur la MEME sélection42+7 dans le Golay explicite; aucune exclusion globale g18/g20',
  code:{size:4096,polynomial_exponents:[11,9,7,6,5,1,0],generator_masks:generators},
  B:[b1,b2],V_mask:V,V_indices:Vindices,shell704:shell.length,
  witness_wrong_xor:certificate(badXor),
  witness_correct_xor_wrong_Q_rows:certificate(badRows),
  forbidden_block:{coordinates_numerator_over_sqrt8:h,norm:4,orthogonal_to_y:true,
    offending_coordinate:2,M_value:2,B_square_sum:10,
    column_energy:10+4*2*2,physical_target:14,
    limitation:'Un h réel de l’enveloppe; aucun cadre de sept h ni SRG n’est construit'},
  proof_conditions:['Tout h physique est octade, M0/±1',
    'XOR42=d1 XOR d2 ou son complément',
    'Q=(56I-EtE-BtB)/4 entier et toutes ses lignes modulo2 appartiennent au code',
    'Q=MtM, rank7 et Q^2=8Q sont aussi nécessaires mais non attestés par ces témoins']};
fs.writeFileSync(path.join(path.dirname(fileURLToPath(import.meta.url)),'controle_selection42_golay.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({exact:true,shell704:shell.length,
  witness1_xor:result.witness_wrong_xor.xor_mask,witness1_integral:result.witness_wrong_xor.integral,
  witness2_xor:result.witness_correct_xor_wrong_Q_rows.xor_mask,
  witness2_bad_Q_rows:result.witness_correct_xor_wrong_Q_rows.rows_not_in_code,
  both_rank:22,forbidden_h_energy:result.forbidden_block.column_energy,physical_target:14}));
