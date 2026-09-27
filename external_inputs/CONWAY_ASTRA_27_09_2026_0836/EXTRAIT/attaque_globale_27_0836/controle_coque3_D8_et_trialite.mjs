import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

// Petits calculs exacts independants : aucune coque quadratique 4096 x 4096.
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const assert=(p,m)=>{if(!p)throw new Error(m);};
const pop=n=>{let k=0;while(n){n&=n-1;k++;}return k;};
function rank2(rows,ncols){
  const a=rows.slice();let r=0;
  for(let j=0;j<ncols;j++){
    const p=a.findIndex((x,i)=>i>=r&&((x>>>j)&1));
    if(p<0)continue;
    [a[r],a[p]]=[a[p],a[r]];
    for(let i=0;i<a.length;i++)if(i!==r&&((a[i]>>>j)&1))a[i]^=a[r];
    r++;
  }
  return r;
}
const blockMasks=[255,255<<8,255<<16];
const basis=[];
for(let b=0;b<3;b++)for(let j=1;j<8;j++)basis.push((1<<(8*b))|(1<<(8*b+j)));
basis.push((1<<0)|(1<<8)|(1<<16));
const gramMasks=basis.map(x=>basis.reduce((m,y,j)=>m|((pop(x&y)&1)<<j),0));
const unsignedTriples=[];
for(let i=0;i<8;i++)for(let j=0;j<8;j++)for(let k=0;k<8;k++)
  unsignedTriples.push((1<<i)|(1<<(8+j))|(1<<(16+k)));
assert(rank2(basis,24)===22,'dimension W');
assert(rank2(unsignedTriples,24)===22,'span des 512 triplets');
assert(rank2(gramMasks,22)===20,'rang Gram modulo deux');
const radical=[blockMasks[0]^blockMasks[1],blockMasks[1]^blockMasks[2]];
for(const z of radical)for(const x of basis)assert((pop(z&x)&1)===0,'radical orthogonal');
for(const x of unsignedTriples){
  const par=blockMasks.map(b=>pop(x&b)&1);assert(par.every(p=>p===1),'parites trois blocs');
}

// Classes (x,y) avec v=(1,0), s=(0,1), c=(1,1).
const classMin=[0,1,2,2];
const glueBasis=[[2,2,0],[0,2,2],[1,1,1]];
const glue=[];
for(let m=0;m<8;m++){
  const cl=[0,0,0];
  for(let i=0;i<3;i++)if((m>>i)&1)for(let j=0;j<3;j++)cl[j]^=glueBasis[i][j];
  glue.push({mask:m,classes:cl,min:cl.reduce((s,c)=>s+classMin[c],0),
    integral:cl.every(c=>(c&2)===0)});
}
assert(new Set(glue.map(x=>x.classes.join(','))).size===8,'indice huit');
assert(glue.filter(x=>x.integral).length===2,'indice entier quatre');
assert(glue.filter(x=>x.min===3).length===1,'unique classe de norme trois');
assert(glue.find(x=>x.min===3).classes.every(c=>c===1),'classe vvv');
const rootDet=64,glueIndex=8,unimodDet=rootDet/(glueIndex*glueIndex);
assert(unimodDet===1,'determinant U');

// Trialite D4 : A=Hadamard/2. Les vecteurs testes ont coordonnees doublees.
const had=[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]];
for(let i=0;i<4;i++)for(let j=0;j<4;j++)assert(dot(had[i],had[j])===(i===j?4:0),'orthogonalite A');
const roots4=[];
for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)for(const a of [-1,1])for(const b of [-1,1]){
  const x=[0,0,0,0];x[i]=2*a;x[j]=2*b;roots4.push(x);
}
const transform=(x,flip=false)=>had.map(row=>dot(row,x.map((z,i)=>flip&&i===0?-z:z))/2);
for(const x of roots4)for(const flip of [false,true]){
  const y=transform(x,flip);
  assert(y.every(z=>Number.isInteger(z)&&z%2===0),'racine D4 entiere');
  assert((y.reduce((s,z)=>s+z,0)/2)%2===0,'racine D4 somme paire');
  assert(dot(y,y)===8,'norme deux preservee');
}
const spinEven=[],spinOdd=[];
for(let m=0;m<16;m++){
  const x=Array.from({length:4},(_,i)=>((m>>i)&1)?-1:1);
  (pop(m)%2?spinOdd:spinEven).push(x);
}
function isDoubledUnit(x){return dot(x,x)===4&&x.filter(z=>z!==0).length===1&&x.every(z=>z===0||Math.abs(z)===2);}
for(const x of spinEven)assert(isDoubledUnit(transform(x)),'s vers v');
for(const x of spinOdd)assert(isDoubledUnit(transform(x,true)),'c vers v');
const result={exact:true,
  scope:'Coque D8^3 complete et trialite D4 ; aucune enumeration de reperes physiques.',
  glue,root_determinant:rootDet,index:glueIndex,determinant:unimodDet,
  integer_sublattice_index:4,norm3_shell_count:16**3,
  unsigned_triple_masks:unsignedTriples.length,span_mod2:22,
  gram_mod2_rank:20,radical_dimension:2,radical_ambient_masks:radical,
  basis_mod2:basis,gram_rows_mod2:gramMasks,
  triality:{D4_roots_tested:roots4.length,even_spinors:spinEven.length,
    odd_spinors:spinOdd.length,hadamard:had,all_images_verified:true},
  physical_root_Gram_mod2_required_rank:22,
  consequence:'Aucun repere physique 42+7 dans cette enveloppe D8^3. Une composante D4 uniforme en classe est impossible pour les memes 42 u.'};
const outfile=path.join(path.dirname(fileURLToPath(import.meta.url)),'controle_coque3_D8_et_trialite.json');
fs.writeFileSync(outfile,JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({exact:true,determinant:unimodDet,shell:16**3,Gram_mod2:20,
  required:22,triality_verified:true}));
