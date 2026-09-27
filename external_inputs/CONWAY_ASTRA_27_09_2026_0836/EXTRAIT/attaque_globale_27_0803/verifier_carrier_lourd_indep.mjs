// Independent dense known-edge test. No catalogue and no unknown-edge completion.
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';import assert from 'node:assert/strict';import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url)),sha=b=>crypto.createHash('sha256').update(b).digest('hex'),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const pairs=[];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)pairs.push([i,j]);
const graphs=[];
for(let code=0;code<64;code++){
 const B=Array.from({length:4},()=>Array(4).fill(0));let edges=0;
 pairs.forEach(([i,j],k)=>{if((code>>k)&1){B[i][j]=B[j][i]=1;edges++;}});
 if(edges===5||(edges===4&&B.every(r=>r.reduce((s,x)=>s+x,0)===2)))graphs.push({code,B});
}
assert.equal(graphs.length,9);
const subsets=[];
function combinations(start,a){if(a.length===6){subsets.push([...a]);return;}for(let v=start;v<10;v++){a.push(v);combinations(v+1,a);a.pop();}}
combinations(0,[]);assert.equal(subsets.length,210);
function prism(G,six){
 const H=six.map(i=>six.map(j=>G[i][j]));if(!H.every(r=>r.reduce((s,x)=>s+x,0)===3))return null;
 const triangles=[];for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)for(let k=j+1;k<6;k++)if(H[i][j]&&H[i][k]&&H[j][k])triangles.push([i,j,k]);
 if(triangles.length!==2||new Set(triangles.flat()).size!==6)return null;
 const t0=triangles[0],t1=triangles[1];
 if(!t0.every(i=>t1.reduce((s,j)=>s+H[i][j],0)===1)||!t1.every(j=>t0.reduce((s,i)=>s+H[i][j],0)===1))return null;
 return {six,triangles:triangles.map(t=>t.map(i=>six[i])),edge_count:9};
}
const records=[];let ruledByCommons=0;
for(const{code,B}of graphs)for(let labelCode=0;labelCode<16;labelCode++){
 const signs=Array.from({length:4},(_,i)=>((labelCode>>i)&1)?1:-1);
 const offending=pairs.find(([i,j])=>dot(B[i],B[j])>=2&&signs[i]===signs[j]);
 if(offending){ruledByCommons++;continue;}
 const G=Array.from({length:10},()=>Array(10).fill(0));const edge=(i,j)=>{G[i][j]=G[j][i]=1;};
 for(let i=0;i<4;i++)for(let j=0;j<4;j++)if(B[i][j])edge(i,4+j);
 edge(8,9);for(let i=0;i<4;i++){edge(i,signs[i]>0?8:9);edge(4+i,signs[i]>0?9:8);}
 let certificate=null;for(const six of subsets){certificate=prism(G,six);if(certificate)break;}
 assert(certificate);records.push({B_code:code,labelCode,certificate});
}
assert.equal(records.length,36);assert.equal(ruledByCommons,108);
// Independent scalar regime enumeration from matching capacities and the two eigen-sums.
const regimes=[];
for(let a=0;a<=3;a++)for(let b=0;b<=3;b++)for(let X=0;X<=8;X++)for(let Y=0;Y<=8;Y++){
 if(X-Y!==12+2*(a-b))continue;
 for(let eb=0;eb<=6;eb++)for(let ea=0;ea<=6;ea++)if(2*(eb-ea)+X-Y===16)regimes.push({a,b,X,Y,eb,ea});
}
assert(regimes.every(v=>(v.a===0&&v.b===2)||(v.a===1&&v.b===3)||(v.a===0&&v.b===3)));
const categories=[...new Set(regimes.map(v=>`${v.a},${v.b}`))].sort();assert.deepEqual(categories,['0,2','0,3','1,3']);
const inputFiles=['G18_G20_CARRIER_LOURD_P0.mjs','G18_G20_CARRIER_LOURD_P0.json','G18_G20_LOURD_REGIMES.md'];
const out={exact:true,graphs:9,contexts:144,commons_rejections:ruledByCommons,known_induced_prisms:records.length,certificates:records,scalar_regime_categories:categories,
 prior:inputFiles.map(f=>({path:f,sha256:sha(fs.readFileSync(path.join(here,f)))})),source_sha256:sha(fs.readFileSync(fileURLToPath(import.meta.url))),
 scope:'Dense independent check of all degree4 external carriers under P0 and of the scalar regime possibilities. It excludes only these carriers, not the remaining heavy case or an entire involution.'};
fs.writeFileSync(path.join(here,'verifier_carrier_lourd_indep.json'),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({exact:true,contexts:144,commons_rejections:ruledByCommons,known_prisms:records.length,regime_categories:categories}));
