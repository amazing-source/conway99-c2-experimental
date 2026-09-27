import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const assert=(p,m)=>{if(!p)throw new Error(m);};
const minima=[0,1,2,2],minimalCounts=[1,16,128,128];
const classes=x=>[0,1,2].map(i=>(x>>(2*i))&3);
const mask=c=>c.reduce((x,z,i)=>x|(z<<(2*i)),0);
const cost=x=>classes(x).reduce((s,c)=>s+minima[c],0);
function symp(x,y){
  let a=0;for(let i=0;i<3;i++)a^=(((x>>(2*i))&1)*((y>>(2*i+1))&1))
    ^(((x>>(2*i+1))&1)*((y>>(2*i))&1));return a;
}
function span(rows){return Array.from({length:8},(_,m)=>rows.reduce((x,r,i)=>x^(((m>>i)&1)?r:0),0)).sort((a,b)=>a-b);}
const records=[];let grassmann=0;
for(let p0=0;p0<4;p0++)for(let p1=p0+1;p1<5;p1++)for(let p2=p1+1;p2<6;p2++){
  const pivots=[p0,p1,p2],slots=[];
  for(let i=0;i<3;i++)for(let j=pivots[i]+1;j<6;j++)if(!pivots.includes(j))slots.push([i,j]);
  for(let m=0;m<(1<<slots.length);m++){
    grassmann++;const rows=pivots.map(j=>1<<j);
    for(let k=0;k<slots.length;k++)if((m>>k)&1)rows[slots[k][0]]|=1<<slots[k][1];
    if(rows.some((x,i)=>rows.some((y,j)=>i<j&&symp(x,y))))continue;
    const words=span(rows);assert(new Set(words).size===8,'dimension trois');
    for(const x of words)for(const y of words){
      assert(symp(x,y)===0,'Lagrangien');
      assert((cost(x)+cost(y)-cost(x^y))%2===0,'parite lineaire sur L');
    }
    const descriptors=words.map(x=>({mask:x,classes:classes(x),minimum:cost(x)}));
    const odd=words.some(x=>cost(x)%2===1);
    const norm1=descriptors.find(w=>w.minimum===1);
    const spin=descriptors.find(w=>w.classes.filter(Boolean).length===1&&w.classes.some(c=>c===2||c===3));
    const vv=descriptors.find(w=>w.classes.filter(Boolean).length===2&&w.classes.filter(Boolean).every(c=>c===1));
    const shell3=descriptors.filter(w=>w.minimum===3);
    const integerComponents=[0,1,2].filter(i=>shell3.every(w=>w.classes[i]===0||w.classes[i]===1));
    let obstruction,certificate;
    if(!odd)obstruction='even_no_norm3';
    else if(norm1){obstruction='minimum1';certificate=norm1;}
    else if(spin){obstruction='singleton_spinor_E8';certificate=spin;}
    else if(vv){obstruction='double_v_D16';certificate=vv;}
    else{
      obstruction='integer_component_shelltrap';
      assert(shell3.length>0&&integerComponents.length>0,'piege local pour toute glue restante');
      certificate={components:integerComponents,coque3_class_masks:shell3.map(w=>w.mask)};
    }
    const shellCount=shell3.reduce((s,w)=>s+w.classes.reduce((n,c)=>n*minimalCounts[c],1),0);
    records.push({RREF_basis:rows,word_masks:words,words:descriptors,odd,obstruction,certificate,
      norm3_classes:shell3,norm3_shell_count:shellCount,integer_components_for_shell3:integerComponents});
  }
}
assert(grassmann===1395&&records.length===135,'comptage Grassmann/Lagrangiens');
const counts={};for(const r of records)counts[r.obstruction]=(counts[r.obstruction]||0)+1;
assert(counts.even_no_norm3===30&&counts.minimum1===37&&counts.singleton_spinor_E8===24
  &&counts.double_v_D16===12&&counts.integer_component_shelltrap===32,'strates135');
const survivors=records.filter(r=>r.obstruction==='integer_component_shelltrap');
assert(survivors.every(r=>r.norm3_shell_count===4096),'4096 normes trois restantes');
const perms=[[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]];
function orbit(words){
  const keys=new Set();for(const p of perms)for(let f=0;f<8;f++){
    const changed=words.map(x=>{const c=classes(x),d=p.map(i=>c[i]);
      for(let j=0;j<3;j++)if(((f>>j)&1)&&(d[j]&2))d[j]^=1;
      return mask(d);}).sort((a,b)=>a-b);keys.add(changed.join(','));
  }return keys;
}
const A=orbit(span([mask([2,2,0]),mask([0,2,2]),mask([1,1,1])]));
const B=orbit(span([mask([1,2,0]),mask([1,0,2]),mask([2,1,1])]));
assert(A.size===8&&B.size===24,'orbites8/24');
for(const k of A)assert(!B.has(k),'orbites disjointes');
for(const r of survivors){
  const k=r.word_masks.join(',');assert(A.has(k)||B.has(k),'classification complete');
  r.canonical_type=A.has(k)?'A_vvv':'B_common_v_center';
}
const example=span([mask([1,2,0]),mask([1,0,3]),mask([2,3,2])]);
assert(B.has(example.join(',')),'exemple du parent');
const result={exact:true,
  scope:'Tous les135 collages unimodulaires de D8^3 ; fermeture physique par min1/E8/D16 acquis ou coque locale entiere.',
  convention:'Digits0,v,s,c encoded0,1,2,3 per component; discriminant symplectic 2 inner product mod2.',
  Grassmann_subspaces:grassmann,Lagrangians:135,odd:105,even:30,ordered_obstruction_counts:counts,
  residual_glues:32,canonical_orbits:{A:8,B:24},all_residual_glues_have_integer_component:true,
  parent_example:{generators:[[1,2,0],[1,0,3],[2,3,2]],word_masks:example,type:'B'},records,
  limitation:'No classification of all rank24 unimodular lattices or global exclusion of g18/g20.'};
const here=path.dirname(fileURLToPath(import.meta.url));
fs.writeFileSync(path.join(here,'classifier_collages_D8_trois.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({exact:true,Lagrangians:135,odd:105,counts,orbits:{A:8,B:24},allInteger:true}));
