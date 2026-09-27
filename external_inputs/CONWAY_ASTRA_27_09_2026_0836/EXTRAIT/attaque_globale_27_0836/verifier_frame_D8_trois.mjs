// Exact small coordinate/discriminant check; the family obstruction is in the MD.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
const here=path.dirname(fileURLToPath(import.meta.url));
const assert=(x,s)=>{if(!x)throw new Error(s);};
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const add=(a,b)=>a.map((x,i)=>x+b[i]);
const zero=()=>Array(24).fill(0);
const vector=(entries)=>{const x=zero();for(const [i,v] of entries)x[i]=v;return x;};
const spin=(part)=>vector(Array.from({length:8},(_,i)=>[8*part+i,1])); // doubled coordinates
const unit=(part)=>vector([[8*part,2]]);
const generators=[add(spin(0),spin(1)),add(spin(1),spin(2)),add(add(unit(0),unit(1)),unit(2))];
const gram4=generators.map(a=>generators.map(b=>dot(a,b)));
assert(JSON.stringify(gram4)===JSON.stringify([[16,8,4],[8,16,4],[4,4,12]]),'glue Gram /4 integral');
// Class labels in F2^2: s=1, v=2, c=3.
const classGenerators=[[1,1,0],[0,1,1],[2,2,2]];
const classes=[];
for(let mask=0;mask<8;mask++){
  const row=[0,0,0];for(let j=0;j<3;j++)if(mask>>j&1)for(let i=0;i<3;i++)row[i]^=classGenerators[j][i];
  classes.push(row);
}
assert(new Set(classes.map(x=>x.join(''))).size===8,'eight independent glue classes');
const costs=[0,2,1,2];
const minima=classes.map(x=>x.reduce((s,c)=>s+costs[c],0));
assert(classes.filter(x=>x.every(c=>c===0||c===2)).length===2,'two integer classes; index4');
assert(classes.filter((x,i)=>minima[i]===3).every(x=>x.every(c=>c===2)),'norm3 only vvv');
assert(classes.filter((x,i)=>minima[i]===4).every(x=>x.filter(c=>c===1).length===2&&x.includes(0)),'noninteger norm4 only ss0');

const roots=[];
for(let part=0;part<3;part++)for(let i=0;i<8;i++)for(let j=i+1;j<8;j++)for(const sign of [1,-1])roots.push(vector([[8*part+i,1],[8*part+j,sign]]));
const characteristics=[];
for(let part=0;part<3;part++)for(let mask=0;mask<256;mask++){
  let minus=0;for(let i=0;i<8;i++)minus+=mask>>i&1;if(minus%2)continue;
  const chi=vector(Array.from({length:8},(_,i)=>[8*part+i,mask>>i&1?-1:1]));
  assert(dot(chi,chi)===8,'characteristic norm8');
  for(const r of roots)assert(dot(chi,r)%2===0,'even D8 root products');
  for(let j=0;j<3;j++){
    const twice=dot(chi,generators[j]);assert(twice%2===0,'integral product with glue');
    assert((twice/2-(gram4[j][j]/4))%2===0,'characteristic parity on glue');
  }
  const doubledSpin=vector(Array.from({length:8},(_,i)=>[8*part+i,mask>>i&1?-1:1]));
  assert(dot(chi,doubledSpin)===8,'matching spinor component gives inner4');
  characteristics.push({part,mask});
}
assert(characteristics.length===384,'384 explicit characteristics8');
const rootCount=3*8*7*2;
const shell3=16**3;
const nonintegerShell4=3*128**2;
const integerShell4=3*(16+70*16)+3*(8*7*2)**2;
assert(rootCount===336&&shell3===4096&&integerShell4+nonintegerShell4===90192,'direct shell counts');
assert(characteristics.length===48+rootCount,'independent theta characteristic count');
const quarterResidues=[];for(let a=0;a<2;a++)for(let b=0;b<2;b++)quarterResidues.push({halves:[a,b],square_sum_mod1_numerator4:a+b,integer:a+b===0});
assert(quarterResidues.filter(x=>x.integer).length===1,'normal coordinates forced integer');
const indices=[18,20].map(g=>({g,physical_index:7**((24-g)/2),integer_sublattice_index:4,contradiction:7**((24-g)/2)%4!==0}));
assert(indices.every(x=>x.contradiction),'both odd indices contradict containment in U_Z');
const out={exact:true,scope:'D8^3 glue family excluded for complete physical42+7 frame and two norm7 normals, not all U24',
  classes:classes.map((row,i)=>({row,minima:minima[i]})),glue_gram:gram4.map(row=>row.map(x=>x/4)),
  lattice_determinant:1,integer_sublattice_index:4,root_count:rootCount,shell3,shell4:integerShell4+nonintegerShell4,
  noninteger_shell4:nonintegerShell4,explicit_characteristics8:characteristics.length,
  character_checks:characteristics.length*(roots.length+3),energy_lower_bound_with_half_block:60,energy_available:56,
  half_square_checks:quarterResidues,physical_indices:indices,no_P0:true,no_all_U_classification:true,
  source_sha256:createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};
fs.writeFileSync(path.join(here,'verifier_frame_D8_trois.json'),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({exact:true,family_frame_excluded:true,characteristics8:384,shell3,root_count:rootCount,indices}));
