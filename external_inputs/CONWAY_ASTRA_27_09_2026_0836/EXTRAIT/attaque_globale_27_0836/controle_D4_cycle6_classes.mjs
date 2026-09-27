import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const assert=(p,m)=>{if(!p)throw new Error(m);};
const pop=x=>{let n=0;while(x){x&=x-1;n++;}return n;};
const adjacency=Array.from({length:6},(_,i)=>(1<<((i+1)%6))|(1<<((i+5)%6)));
function describe(a){
  let b=0;for(let i=0;i<6;i++)if((a>>i)&1)b^=adjacency[i];
  const symbols=Array.from({length:6},(_,j)=>((a>>j)&1)+2*((b>>j)&1));
  return {mask:a,v_mask:a,s_mask:b,symbols,weight:symbols.filter(Boolean).length};
}
const classes=Array.from({length:64},(_,a)=>describe(a));
const hist={};for(const c of classes)hist[c.weight]=(hist[c.weight]||0)+1;
assert(classes.slice(1).every(c=>c.weight>=3),'aucune classe poids un ou deux');
const norm3=classes.filter(c=>c.weight===3);
const orderedMasks=[1,2,4,8,16,32,21,42];
assert(norm3.length===8&&norm3.every(c=>orderedMasks.includes(c.mask)),'huit classes exactes');
const ordered=orderedMasks.map(a=>describe(a));
assert(ordered.every(c=>!c.symbols.includes(3)),'pas de lettre c dans la coque trois');

// Produits exacts de six generateurs de collage, coordonnees doublees.
const glueVectors=Array.from({length:6},(_,i)=>{
  const x=Array(24).fill(0);x[4*i]=2;
  for(const j of [(i+1)%6,(i+5)%6])for(let k=0;k<4;k++)x[4*j+k]=1;
  return x;
});
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const gram=glueVectors.map(a=>glueVectors.map(b=>dot(a,b)/4));
assert(gram.every(row=>row.every(Number.isInteger)),'collage integral');
assert(gram.every((row,i)=>row[i]===3),'collage impair');
for(const g of glueVectors)for(let b=0;b<6;b++)for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)
  for(const s of [-1,1])for(const t of [-1,1])assert((s*g[4*b+i]+t*g[4*b+j])%2===0,'produit racine D4 entier');

const valid=[],rejected=[],byBases={},byClassCount={};
for(let m=0;m<256;m++){
  const present=Array(6).fill(0);
  for(let i=0;i<8;i++)if((m>>i)&1)for(let j=0;j<6;j++){
    const sym=ordered[i].symbols[j];if(sym)present[j]|=1<<(sym-1);
  }
  const deficient=present.findIndex(x=>(x&3)!==3);
  if(deficient>=0){
    const missing=(present[deficient]&1)?'s':'v';
    rejected.push({mask:m,component:deficient,missing_class:missing,present_symbol_mask:present[deficient]});
    continue;
  }
  const bases=pop(m&63),size=pop(m);
  assert(bases>=4,'quatre bases minimales');
  assert(pop(m&21)>=2&&pop(m&42)>=2,'deux bases par part');
  assert(size>=6,'six classes minimales');
  valid.push({mask:m,bases,size});byBases[bases]=(byBases[bases]||0)+1;
  byClassCount[size]=(byClassCount[size]||0)+1;
}
assert(valid.length===25&&rejected.length===231,'couverture256');
assert(byBases[4]===9&&byBases[5]===12&&byBases[6]===4,'formule9+12+4');
assert(byClassCount[6]===16&&byClassCount[7]===8&&byClassCount[8]===1,'tailles6/7/8');
const result={exact:true,
  scope:'Collage D4^6 du cycle C6 et classes utilisees par la meme selection42 ; aucune realisation physique annoncee.',
  adjacency,glue_generator_Gram:gram,glue_index:64,determinant:1,
  glue_class_weight_histogram:hist,norm3_classes:ordered,
  norm3_shell_count:8*8**3,all_glue_classes:classes,
  families_tested:256,qualifying_families:25,refuted_families:231,
  minimum_used_classes:6,qualifying_by_number_bases:byBases,
  qualifying_by_total_classes:byClassCount,valid,rejected,
  rejection_principle:'Une composante uniforme 0/v ou0/s donne quatre directions de norme1 integralement duales aux42u, contredisant le petit polaire de dimension2.'};
fs.writeFileSync(path.join(path.dirname(fileURLToPath(import.meta.url)),'controle_D4_cycle6_classes.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({exact:true,shell4096:result.norm3_shell_count,
  qualifying25:valid.length,refuted231:rejected.length,
  byBases,byClassCount,minimumClasses:6}));
