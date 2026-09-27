// Petits contrôles exacts de la preuve candidate; aucune classification
// de graphes ou de réseaux n'est exécutée par ce source.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const check=(ok,label)=>{if(!ok)throw Error(label);};
const isoPairs=[];
for(const coeff of [[6,6],[5,6]]){
  let count=0;
  for(let x=0;x<7;x++)for(let y=0;y<7;y++)
    if((x||y)&&(coeff[0]*x*x+coeff[1]*y*y)%7===0)count++;
  check(count===0,'A6^2 / A13+A6 anisotropes');
  isoPairs.push({coefficients:coeff,nonzero_isotropic_vectors:count});
}
const classNumerator=k=>k*(7-k);
const isotropic=[];
for(let a=1;a<7;a++)for(let b=1;b<7;b++)for(let c=1;c<7;c++){
  const n=classNumerator(a)+classNumerator(b)+classNumerator(c);
  if(n%7===0)isotropic.push({classes:[a,b,c],norm_numerator:n});
}
check(isotropic.length===48,'48 vecteurs isotropes A6^3');
check(isotropic.every(x=>x.norm_numerator===28),'minimum projection4');
const A3=Array.from({length:4},(_,k)=>({class:k,numerator:k*(4-k),denominator:4}));
const A2A1=[];
for(let k=0;k<3;k++)for(let l=0;l<2;l++)
  A2A1.push({classes:[k,l],numerator:2*k*(3-k)+3*l,denominator:6});
const A1cube=[];
for(let mask=1;mask<8;mask++){
  const weight=mask.toString(2).replaceAll('0','').length;
  A1cube.push({mask,numerator:weight,denominator:2});
}
check(A3.filter(x=>x.class&&x.numerator%4===0).every(x=>x.numerator===4),'A3 saturation norme1');
check(A2A1.filter(x=>x.classes.some(Boolean)).every(x=>x.numerator%6!==0),'A2+A1 aucune classe intégrale');
check(A1cube.filter(x=>x.numerator%2===0).every(x=>x.numerator===2),'A1^3 saturation norme1');
check(A3.filter(x=>x.class).every(x=>2*x.numerator>=x.denominator),'R3 minclasse>=1/2');
check(A2A1.filter(x=>x.classes.some(Boolean)).every(x=>2*x.numerator>=x.denominator),'R3 minclasse>=1/2');
const determinantRows=[];
for(let ap=0;ap<=3;ap++)for(let j=0;j<=1;j++){
  const b=2-ap+2*j;
  if(b<0||j&&(!ap||!b))continue;
  let status='candidate';
  if(ap===0)status='cyclic rank1 incompatible with elementary rank2';
  if(ap===1&&j===1||ap===2&&j===1)status='anisotropic M7, integral J order7 class';
  determinantRows.push({a_prime:ap,b,j,status});
}
check(18*2+7>3*14,'18/7+1/2>3');
check(18+4>21&&18+6>21,'18/7+d/7>3');
const result={scope:'Petits calculs propres associés à une preuve candidate de corang1; pas de reconstruction SRG',
  anisotropic_pairs:isoPairs,A6_cube_isotropic_nonzero:isotropic.length,
  A6_cube_all_isotropic_projection_norm:4,
  rank3_class_minima:{A3,A2_A1:A2A1,A1_cube:A1cube},
  primitive_determinant_rows:determinantRows,
  cost_bounds:['18/7+1/2=43/14>3','18/7+4/7=22/7>3','18/7+6/7=24/7>3']};
fs.writeFileSync(path.join(path.dirname(fileURLToPath(import.meta.url)),'verifier_racines_corang_un.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result));
