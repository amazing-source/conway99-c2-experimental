// Independent bounded certificates for the two human decomposition arguments.
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';import assert from 'node:assert/strict';import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url)),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const roots=[];
for(let i=0;i<7;i++)for(let j=i+1;j<7;j++)for(const s of[1,-1]){
 const v=Array(7).fill(0);v[i]=1;v[j]=s;roots.push({support:[i,j],sign:s,v});
}
assert.equal(roots.length,42);
const adj=roots.map((p,i)=>roots.map((q,j)=>i!==j&&dot(p.v,q.v)!==0?j:-1).filter(j=>j>=0));
assert(adj.every(row=>row.length===20));const parent=Array(42).fill(-1),queue=[0];parent[0]=0;
for(let k=0;k<queue.length;k++)for(const q of adj[queue[k]])if(parent[q]<0){parent[q]=queue[k];queue.push(q);}
assert.equal(queue.length,42);const edges=adj.reduce((n,row)=>n+row.length,0)/2;assert.equal(edges,420);
const sisterPaths=[];
for(let p=0;p<42;p+=2){
 assert.equal(dot(roots[p].v,roots[p+1].v),0);
 const middle=adj[p].find(q=>adj[q].includes(p+1));assert(middle!==undefined);
 sisterPaths.push([p,middle,p+1]);
}
const pairChecks=[];
for(let i=0;i<7;i++)for(let j=i+1;j<7;j++){
 const ids=roots.map((r,k)=>r.support[0]===i&&r.support[1]===j?k:-1).filter(k=>k>=0);
 assert.equal(ids.length,2);const contributions=ids.map(k=>roots[k].v[i]*roots[k].v[j]);
 assert.deepEqual(contributions,[1,-1]);
 const subsetValues=[0,1,2,3].map(mask=>contributions.reduce((s,x,k)=>s+(((mask>>k)&1)?x:0),0));
 assert.deepEqual(subsetValues,[0,1,-1,0]);
 assert.deepEqual(subsetValues.filter(x=>x%3===0),[0,0]);pairChecks.push({blocks:[i,j],ids,subsetValues});
}
const diagonalCases=[];
for(let n=0;n<=12;n++)if(n%3===0){const G=n/3;diagonalCases.push({incidences:n,Gram_diagonal:G,idempotence:G*G===4*G});}
assert.deepEqual(diagonalCases.filter(r=>r.idempotence).map(r=>r.incidences),[0,12]);
const out={exact:true,D7_lines:42,nonorthogonality_edges:edges,degree:20,connected:true,parent,sisterPaths,pairChecks,diagonalCases,
 source_sha256:sha(fs.readFileSync(fileURLToPath(import.meta.url))),
 scope:'Discrete steps of two uniform human proofs. Norm3 generators must be pure in an integral minimum2 orthogonal decomposition. No local catalogue, lattice classification or graph99 search.'};
fs.writeFileSync(path.join(here,'verifier_indecomposabilite_courte.json'),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({exact:true,D7_lines:42,edges,connected:true,offdiagonal_checks:84,pure_block_incidence_counts:[0,12]}));
