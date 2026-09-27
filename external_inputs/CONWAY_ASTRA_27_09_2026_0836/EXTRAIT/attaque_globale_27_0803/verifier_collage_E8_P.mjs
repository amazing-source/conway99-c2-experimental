// Bounded independent integer checks. This does not classify rank24 lattices.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const mod=(x,p=7)=>((x%p)+p)%p;
const norm=a=>dot(a,a);
const tr=A=>A[0].map((_,j)=>A.map(r=>r[j]));
const mm=(A,B)=>{const Bt=tr(B);return A.map(a=>Bt.map(b=>dot(a,b)));};
function detBareiss(input){
  const A=input.map(r=>r.map(BigInt));let sign=1n,last=1n;
  for(let k=0;k<A.length-1;k++){
    let p=k;while(p<A.length&&!A[p][k])p++;assert(p<A.length);
    if(p!==k){[A[p],A[k]]=[A[k],A[p]];sign=-sign;}
    const pivot=A[k][k];
    for(let i=k+1;i<A.length;i++)for(let j=k+1;j<A.length;j++){
      const numerator=pivot*A[i][j]-A[i][k]*A[k][j];
      assert.equal(numerator%last,0n);A[i][j]=numerator/last;
    }
    for(let i=k+1;i<A.length;i++)A[i][k]=0n;last=pivot;
  }
  return sign*A.at(-1).at(-1);
}
// All E8 roots and all candidates left by the D8 constraints, in doubled coordinates.
const roots2=[];
for(let i=0;i<8;i++)for(let j=i+1;j<8;j++)for(const a of[-2,2])for(const b of[-2,2]){
  const r=Array(8).fill(0);r[i]=a;r[j]=b;roots2.push(r);
}
for(let mask=0;mask<256;mask++){
  const r=Array.from({length:8},(_,i)=>(mask>>i)&1?-1:1);
  if(r.filter(x=>x<0).length%2===0)roots2.push(r);
}
assert.equal(roots2.length,240);assert(roots2.every(r=>norm(r)===8));
const candidates2=[Array(8).fill(0)];
for(let i=0;i<8;i++)for(const s of[-2,2]){const x=Array(8).fill(0);x[i]=s;candidates2.push(x);}
for(let mask=0;mask<256;mask++)candidates2.push(Array.from({length:8},(_,i)=>(mask>>i)&1?-1:1));
assert.equal(candidates2.length,273);
const survivors=candidates2.filter(x=>roots2.every(r=>dot(x,r)%4===0&&Math.abs(dot(x,r))<=4));
assert.deepEqual(survivors,[Array(8).fill(0)]);
// Gram matrix of the primitive seven-block closure: 2e_0,...,2e_5,ones.
const Pbasis=Array.from({length:6},(_,i)=>Array.from({length:7},(_,j)=>i===j?2:0));
Pbasis.push(Array(7).fill(1));const Pgram=mm(Pbasis,tr(Pbasis));
assert.equal(detBareiss(Pgram),4096n);
// P*/P represented by k mod4 with even sum, quotienting the translation 2*ones.
let classesBefore=0,torsion2Before=0;const quotient=new Set();
for(let code=0;code<4**7;code++){
  let n=code;const k=Array.from({length:7},()=>{const x=n%4;n=Math.floor(n/4);return x;});
  if(k.reduce((s,x)=>s+x,0)%2)continue;classesBefore++;
  const translate=k.map(x=>(x+2)%4);
  quotient.add([k.join(''),translate.join('')].sort()[0]);
  if(k.every(x=>x%2===0))torsion2Before++;
}
assert.equal(classesBefore,8192);assert.equal(quotient.size,4096);assert.equal(torsion2Before/2,64);
// P has exponent <=4 and exactly 64 elements annihilated by2, hence (Z/4)^6.
const U=[[2,-3],[3,2]];assert.deepEqual(mm(tr(U),U),[[13,0],[0,13]]);
const plane=Array.from({length:49},(_,i)=>[Math.floor(i/7),i%7]);
assert.equal(plane.filter(v=>mod(norm(v))===0).length,1);
let antiIsometryChecks=0;
for(const a of plane)for(const b of plane){
  const ua=U.map(r=>mod(dot(r,a))),ub=U.map(r=>mod(dot(r,b)));
  assert.equal(mod(dot(ua,ub)),mod(-dot(a,b)));antiIsometryChecks++;
}
// Potential mixed roots of the rank24 gluing: these are only necessary norm pairs.
const mixed=[];
for(let b1=-2;b1<=2;b1++)for(let b2=-2;b2<=2;b2++){
  const j=b1*b1+b2*b2;
  if(j&&j<=6&&14-j>=8)mixed.push({b:[b1,b2],seven_y_norm:j,seven_x_norm:14-j});
}
assert.deepEqual([...new Set(mixed.map(v=>v.seven_y_norm))].sort((a,b)=>a-b),[1,2,4,5]);
// Characteristic vectors of norm8 in the odd unimodular24 gluing.
const profiles=[];
for(const b1 of[1,3])for(const b2 of[1,3])if(b1<=b2)
for(let n3=0;n3<=1;n3++)for(let n5=0;n5<=1;n5++)for(let z=0;z<=3;z++)
  if(b1*b1+b2*b2+4*z+8*n3+24*n5===14)profiles.push({b_abs:[b1,b2],root_abs3:n3,root_abs5:n5,block_half_square_sum:z});
assert.deepEqual(profiles,[
  {b_abs:[1,1],root_abs3:0,root_abs5:0,block_half_square_sum:3},
  {b_abs:[1,1],root_abs3:1,root_abs5:0,block_half_square_sum:1},
  {b_abs:[1,3],root_abs3:0,root_abs5:0,block_half_square_sum:1}
]);
// In the middle profile, reflection in the unique norm3 generator must move the block.
let reflectionCases=0,blockSaturationCases=0;
for(let i=0;i<7;i++)for(let j=i+1;j<7;j++)for(const c of[-1,1])
for(let k=0;k<7;k++)for(const a of[-1,1])for(const s of[-1,1]){
  const C=Array(7).fill(0);C[i]=1;C[j]=c;
  const after=C.map((x,l)=>(l===k?a:0)+s*x);const allowed=norm(after)===1;
  assert.equal(allowed,C[k]!==0&&a*C[k]===-s);reflectionCases++;if(allowed)blockSaturationCases++;
}
let neighborSaturationCases=0;
for(const a of[-1,1])for(const h of[-1,1])for(const s of[-1,1]){
  assert.equal(Math.abs(a-2*s*h)===1,a===s*h);neighborSaturationCases++;
}
const priorFiles=[
 '../dossier6_involution/NOTE_RESEAU_MINIMUM.md',
 '../dossier6_involution/AUDIT_GENRE.md',
 '../reprise_27_0636/CONTROLES_MOMENTS_ENTIERS_REMOTE.json'
];
const prior=priorFiles.map(f=>({path:f,sha256:sha(fs.readFileSync(path.join(here,f)))}));
const out={exact:true,E8:{roots:240,candidates:273,survivors:1,only_zero:true},
 primitive_P:{basis:Pbasis,Gram:Pgram,determinant:4096,discriminant_order:4096,exponent:4,torsion2_order:64,structure:'(Z/4)^6'},
 discriminant_anti_isometry:{U,checks:antiIsometryChecks,F7_I2_anisotropic:true},
 rank24_mixed_root_necessary_norms:mixed,rank24_characteristic_norm8_profiles:profiles,
 norm8_middle_profile_reflection:{cases:reflectionCases,valid_block_moves:blockSaturationCases,neighbor_cases:neighborSaturationCases},
 prior,source_sha256:sha(fs.readFileSync(fileURLToPath(import.meta.url))),
 scope:'Finite checks of formulas and the E8 minuscule lemma. Gluing needs a rank22 integral lattice of determinant49 with the stated anisotropic discriminant. Mixed norm pairs are possibilities, not vectors. No norm2/characteristic8/global involution exclusion.'};
fs.writeFileSync(path.join(here,'verifier_collage_E8_P.json'),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({exact:true,E8_nonzero_survivors:0,P_det:4096,P_torsion2:64,anti_isometry_checks:antiIsometryChecks,characteristic8_profiles:3,reflection_cases:reflectionCases}));
