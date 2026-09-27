import fs from 'node:fs';
import assert from 'node:assert/strict';
const bit=(m,j)=>m>>j&1;
const classes=[];
for(let m=0;m<16;m++){
  const local=Array.from({length:4},(_,i)=>bit(m,(i+3)%4)+2*bit(m,i));
  const twiceNorm=local.reduce((s,a)=>s+(a===0?0:a===3?2:3),0);
  classes.push({mask:m,classes:local,minimum_twice_norm:twiceNorm});
}
const hist={};for(const row of classes)hist[row.minimum_twice_norm/2]=(hist[row.minimum_twice_norm/2]||0)+1;
assert.deepEqual(hist,{0:1,3:4,4:5,5:4,6:2});
const baseline=i=>{
  const a=Array(24).fill(0);for(let j=0;j<6;j++){a[6*i+j]=j===0?-1:1;a[6*((i+1)%4)+j]=1;}return a;
};
const shell=Array.from({length:4},(_,i)=>baseline(i));
for(let c=0;c<4;c++)for(let a=0;a<6;a++)for(let b=a+1;b<6;b++){
  const v=baseline((c+3)%4);v[6*c+a]*=-1;v[6*c+b]*=-1;shell.push(v);
}
assert.equal(shell.length,64);
const dot=(a,b)=>a.reduce((s,x,j)=>s+x*b[j],0);
for(const row of shell)assert.equal(dot(row,row),12);
const G=shell.map(a=>shell.map(b=>{const n=dot(a,b);assert.equal(n%4,0);return n/4;}));
const rows=G.map(row=>row.reduce((s,a,j)=>s|(BigInt((a%2+2)%2)<<BigInt(j)),0n));
const echelon=[];
for(const original of rows){let row=original;for(const [pivot,r] of echelon)if(row>>BigInt(pivot)&1n)row^=r;
  if(row){let pivot=0;while(!(row>>BigInt(pivot)&1n))pivot++;echelon.push([pivot,row]);}}
assert.equal(echelon.length,24);
const choose=(n,k)=>{let a=1;for(let j=1;j<=k;j++)a=a*(n-j+1)/j;return a;};
const allowed={single_component_four_units:4*choose(6,4)*16,
  adjacent_two_plus_two_units:4*choose(6,2)**2*16,
  opposite_spinors_plus_intermediate_unit:4*32**2*12};
assert.deepEqual(allowed,{single_component_four_units:960,adjacent_two_plus_two_units:14400,
  opposite_spinors_plus_intermediate_unit:49152});
const out={exact:true,glue_classes:classes,coset_minimum_histogram:hist,
  determinant:256/16**2,root_system:'D6^4',norm3_shell_size:4*32**2,
  norm3_sample64_twice_coordinates:shell,sample_Gram_F2_rank:echelon.length,
  characteristic8_count:2*6**2*4,allowed_individual_norm4:allowed,
  allowed_individual_norm4_total:Object.values(allowed).reduce((a,b)=>a+b,0),
  scope:'Integral rootful envelope and individual h classification; no simultaneous physical49-frame or graph certified.'};
fs.writeFileSync(new URL('./G18_G20_D6_QUATRE.json',import.meta.url),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({exact:true,classes:hist,sample_Gram_F2_rank:24,
  norm3_shell:4096,characteristic8:288,allowed_norm4_total:64512,no_physical_frame_claim:true}));
