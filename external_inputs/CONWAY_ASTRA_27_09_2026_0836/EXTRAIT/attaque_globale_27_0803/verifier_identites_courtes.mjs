// Bounded exact checks of identities used in the human proofs. No graph99 search or solver.
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';import assert from 'node:assert/strict';import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url)),sha=b=>crypto.createHash('sha256').update(b).digest('hex'),read=n=>fs.readFileSync(path.join(here,n)),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),tr=A=>A[0].map((_,i)=>A.map(r=>r[i])),mm=(A,B)=>{const T=tr(B);return A.map(r=>T.map(c=>dot(r,c)));},choose2=n=>n*(n-1)/2;
let localPolynomialChecks=0;for(let t=1;t<=5;t++)for(let d=0;d<=48;d++){assert.equal(choose2(d)+choose2(d+t),d*d+(t-1)*d+t*(t-1)/2);localPolynomialChecks++;}
const d7=[];for(let i=0;i<7;i++)for(let j=i+1;j<7;j++)for(const s of[1,-1]){const r=Array(7).fill(0);r[i]=1;r[j]=s;d7.push(r);}const C=tr(d7);assert.deepEqual(mm(C,tr(C)),Array.from({length:7},(_,i)=>Array.from({length:7},(_,j)=>i===j?12:0)));
const n=C.map((r,i)=>[...Array.from({length:7},(_,j)=>i===j?3:0),...r]),w=C.map((r,i)=>[...Array.from({length:7},(_,j)=>i===j?-4:0),...r]);
assert.deepEqual(mm(n,tr(n)),Array.from({length:7},(_,i)=>Array.from({length:7},(_,j)=>i===j?21:0)));assert.deepEqual(mm(w,tr(w)),Array.from({length:7},(_,i)=>Array.from({length:7},(_,j)=>i===j?28:0)));
assert(n.every((r,i)=>r.every((x,j)=>(x-w[i][j])%7===0)));
const blockRows=C.map(r=>r.reduce((s,x)=>s+x,0)-1);assert.deepEqual(blockRows,[11,9,7,5,3,1,-1]);let parityChecks=0;
for(let M=0;M<=210;M++){const rootsRowSum=462-4*M,rowSquaresMod8=((7+2*rootsRowSum)%8+8)%8;assert.equal(rowSquaresMod8,3);const equalityPossible=((rowSquaresMod8+497-4*M-588)%8+8)%8===0;assert.equal(equalityPossible,M%2===0);parityChecks++;}
const heavyNorm14=[2,3].map(k=>({heavy:k,negative_vertices:14-3*k,min_negative_neighbors:8-k,min_common:2*(8-k)-(14-3*k)}));assert(heavyNorm14.every(r=>r.min_common>2));
const pairLoads=[];for(const x of[1,-1])for(const y of[1,-1]){const loads=[x+y,x-y];assert(!(Math.abs(loads[0])>=2&&Math.abs(loads[1])>=2));pairLoads.push({coefficients:[x,y],loads});}
const characteristic10Profiles=[];for(let n3=0;n3<=3;n3++)for(let n5=0;n5<=1;n5++)for(let b2=0;b2<=1;b2++)for(let b1=0;b1<=7;b1++)if(2*n3+6*n5+4*b2+b1===7&&b1+b2<=7)characteristic10Profiles.push({root_abs3:n3,root_abs5:n5,block_half_abs2:b2,block_half_abs1:b1});assert.equal(characteristic10Profiles.length,7);
assert.equal(characteristic10Profiles.filter(r=>r.root_abs3===0&&r.root_abs5===0).length,2);
// Actual Hamming H(2,3), characteristic-independent integer control: its lattice has a generator of norm1.
const coord=Array.from({length:9},(_,i)=>[Math.floor(i/3),i%3]),sigma=coord.map(([x,y])=>3*((3-x)%3)+(3-y)%3),adj=coord.map(a=>coord.map(b=>+(a.reduce((s,x,i)=>s+(x!==b[i]),0)===1))),reps=Array.from({length:9},(_,i)=>i).filter(i=>i<sigma[i]);
assert.equal(reps.length,4);const S=reps.map(a=>reps.map(b=>adj[a][b]-adj[a][sigma[b]])),H=S.map((r,i)=>r.map((x,j)=>+(i===j)-x));assert.deepEqual(mm(H,H),H.map(r=>r.map(x=>3*x)));
const o=H.findIndex((r,i)=>r[i]===1);assert(o>=0);const a=H.map(r=>r[o]);assert.equal(dot(a,a),3);assert.deepEqual(S.map(r=>dot(r,a)),a.map(x=>x?-2*x:0));assert(a.every(x=>[0,1,-1].includes(x)));
const P=[],Q=[];a.forEach((x,i)=>{if(!x)return;P.push(x>0?reps[i]:sigma[reps[i]]);Q.push(x>0?sigma[reps[i]]:reps[i]);});const A=P.map(v=>P.map(z=>adj[v][z])),B=P.map(v=>Q.map(z=>adj[v][z])),deg=A.map(r=>r.reduce((s,x)=>s+x,0)),m=P.length,e=deg.reduce((s,x)=>s+x,0)/2;
assert.deepEqual(B.map(r=>r.reduce((s,x)=>s+x,0)),deg.map(x=>x+2));const outside=Array.from({length:9},(_,i)=>i).filter(i=>!P.includes(i)&&!Q.includes(i)),D=outside.reduce((s,i)=>s+choose2(P.reduce((n,j)=>n+adj[i][j],0)),0);
assert.equal(D,m*(m-2)-3*e-dot(deg,deg));assert(D>0); // The m7/d7 forcing argument is NOT transplanted here.
const bvlsFile=path.join(here,'../reprise_27_0636/CONTROLES_MOMENTS_ENTIERS_REMOTE.json'),bvlsBytes=fs.readFileSync(bvlsFile);
const out={exact:true,localPolynomialChecks,global_M_parity_cases:parityChecks,seven_coefficient_relations_Gram:21,seven_image_columns_standard_Gram:28,mod7_coincidence:true,
 heavyNorm14,pairLoads,characteristic10Profiles,Hamming_H2_control:{graph_vertices:9,degree:4,r:1,d:3,S,H,norm1_generator:o,coefficient_vector:a,P,Q,external_common_pairs:D,norm1_NOT_rejected:true},
 frozen_BvLS_positive_control_sha256:sha(bvlsBytes),positive_scope:'H2 is rebuilt directly. BvLS integer/p3 control remains acquired and frozen, not rerun or assigned SRG99 constants.',
 source_sha256:sha(read('verifier_identites_courtes.mjs')),scope:'Checks polynomial/parity/coefficient identities and a true small positive graph. The norm1 impossibility for SRG99 is a human proof, not a finite catalogue sweep.'};
fs.writeFileSync(path.join(here,'verifier_identites_courtes.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({exact:true,polynomial_checks:localPolynomialChecks,parity_cases:parityChecks,H2_norm1_preserved:true,norm10_profiles:characteristic10Profiles.length}));
