// Contrôles finis propres : code 2-adique des sept blocs, profil tournoi,
// témoin K11^2. Ils ne construisent pas de graphe SRG99.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const check=(ok,label)=>{if(!ok)throw Error(label);};
const enc=a=>a.reduce((s,x,i)=>s+x*4**i,0);
const dec=n=>Array.from({length:7},(_,i)=>Math.floor(n/4**i)%4);
const code=a=>{
  a=a.map(x=>((x%4)+4)%4);
  return Math.min(enc(a),enc(a.map(x=>(x+2)%4)));
};
const classes=new Set();
for(let n=0;n<4**7;n++){
  const a=dec(n);if(a.reduce((s,x)=>s+x,0)%2===0)classes.add(code(a));
}
let order2=0;
for(const n of classes)if(code(dec(n).map(x=>2*x))===0)order2++;
check(classes.size===4096,'|A_P|');check(order2===64,'A_P[2]');
const roots=[];
for(let i=0;i<7;i++)for(let j=i+1;j<7;j++)for(const s of [1,-1]){
  const r=Array(7).fill(0);r[i]=1;r[j]=s;roots.push(r);
}
const rootClasses=roots.map(code);
check(new Set(rootClasses).size===42,'42 classes distinctes');
check(rootClasses.every(n=>code(dec(n).map(x=>2*x))!==0),'ordre4');
check(roots.every(r=>dot(r,r)===2),'norme p=1/2');
const adjacency=roots.map((r,i)=>roots.map((s,j)=>i!==j&&dot(r,s)!==0));
check(adjacency.every(row=>row.filter(Boolean).length===20),'degré D7');
const visited=new Set([0]);const queue=[0];
while(queue.length){const p=queue.shift();adjacency[p].forEach((ok,q)=>{
  if(ok&&!visited.has(q)){visited.add(q);queue.push(q);}
});}
check(visited.size===42,'connexité D7');

// Cas caractéristique10 : les sept demi-coefficients blocs valent1.
// Un tournoi cyclique régulier donne C epsilon=-6*1, mais aucun T.
const residues=new Set([1,2,4]);const epsilon=[];const indegrees=Array(7).fill(0);
for(let i=0;i<7;i++)for(let j=i+1;j<7;j++){
  const receiver=residues.has((j-i+7)%7)?i:j;
  indegrees[receiver]++;
  epsilon.push(-1,receiver===i?-1:1);
}
const Ce=Array(7).fill(0);
roots.forEach((r,k)=>r.forEach((x,i)=>Ce[i]+=x*epsilon[k]));
check(indegrees.every(x=>x===3),'tournoi régulier');
check(Ce.every(x=>x===-6),'C epsilon');
check(7*4+dot(epsilon,epsilon)===70,'profil caractéristique10');

// D12^+=D12+Z*(1/2,...,1/2), a=(3/2,3/2,1/2^10).
// Toutes les fractions sont contrôlées en coordonnées doublées.
const a2=[3,3,...Array(10).fill(1)];
const c=[1,1,-1,...Array(9).fill(1)];
const k2=c.map((x,i)=>2*x-a2[i]);
check(dot(a2,a2)===28,'a^2=7');
check(dot(c,c)===12,'c^2=12');
check(dot(c,a2)===14,'c.a=7');
check(dot(k2,a2)===0,'k dans a-perp');
check(dot(k2,k2)===20,'k^2=5');
check(c.reduce((s,x)=>s+x,0)%2===0,'c dans D12');
check(c.every(x=>x%2!==0),'c caractéristique sur D12');
check((c.reduce((s,x)=>s+x,0)/2-3)%2===0,'c caractéristique sur spin');
const b=[1,1,...Array(10).fill(0)];
check(dot(b,b)===2&&dot(b,a2)===6,'b^2=2,b.a=3');
const dualNormNumerator=7*dot(b,b)-(dot(b,a2)/2)**2;
check(dualNormNumerator===5,'dual de K : norme5/7');

// Les trois profils d'une caractéristique8 dans le collage unimodulaire24.
const char8=[];
for(const b1 of [1,3])for(const b2 of [1,3])if(b1<=b2)
  for(let n3=0;n3<=1;n3++)for(let aSquare=0;aSquare<=3;aSquare++)
    if(b1*b1+b2*b2+8*n3+4*aSquare===14)
      char8.push({b_abs:[b1,b2],n3,block_half_square:aSquare});
check(char8.length===3,'trois profils caractère8');

const result={scope:'Contrôles finis arithmétiques; aucun graphe99 ni exclusion de genre',
  code_P:{size:classes.size,two_torsion:order2,invariant_factors:'4^6',
    root_classes:42,root_order:4,root_projection_norm:'1/2'},
  D7_nonorthogonality_graph:{vertices:42,degree:20,edges:420,connected:visited.size===42},
  characteristic10_tournament:{indegrees,C_epsilon:Ce,squared_coefficient_norm:70,
    limitations:'Condition des blocs seulement; T et appartenance au réseau non construits'},
  counterexample_K11_squared:{rank:22,determinant:49,minimum:2,
    characteristic_minimum:10,dual_vector_norm:'5/7',
    limitations:'Contre-témoin à la borne caractéristique seule; viole min N#>=8/7'},
  characteristic8_glue_profiles:char8};
const target=path.join(path.dirname(fileURLToPath(import.meta.url)),'verifier_sept_blocs_caracteristiques.json');
fs.writeFileSync(target,JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result));
