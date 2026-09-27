// Known-edge carrier check, without a global graph search.
import fs from 'node:fs';import assert from 'node:assert/strict';
const pairs=[];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)pairs.push([i,j]);
const count=x=>{let n=0;while(x){x&=x-1;n++;}return n;},graphs=[];
for(let mask=0;mask<64;mask++){
 const row=Array(4).fill(0);for(let e=0;e<6;e++)if(mask&(1<<e)){const[i,j]=pairs[e];row[i]|=1<<j;row[j]|=1<<i;}
 if(count(mask)===5||(count(mask)===4&&row.every(r=>count(r)===2)))graphs.push({mask,row});
}
assert.equal(graphs.length,9);const proofs=[];let contexts=0;
for(const g of graphs)for(let labels=0;labels<16;labels++){
 contexts++;const s=Array.from({length:4},(_,j)=>labels&(1<<j)?1:-1);
 if(pairs.some(([i,j])=>count(g.row[i]&g.row[j])>=2&&s[i]===s[j]))continue;
 const adj=Array.from({length:10},()=>Array(10).fill(false));
 const edge=(a,b)=>{adj[a][b]=true;adj[b][a]=true;};
 for(let i=0;i<4;i++)for(let j=0;j<4;j++)if(g.row[i]&(1<<j))edge(i,4+j);
 edge(8,9);for(let i=0;i<4;i++){edge(i,s[i]===1?8:9);edge(4+i,s[i]===1?9:8);}
 let witness=null;
 for(let i=0;i<4;i++)for(let j=0;j<4;j++)for(let k=0;k<4;k++)for(let l=0;l<4;l++){
  if(new Set([i,j,k,l]).size!==4||s[i]!==1||s[l]!==1||s[j]!==-1||s[k]!==-1)continue;
  const triangles=[[i,4+j,8],[k,4+l,9]],bars=[[i,4+l],[4+j,k],[8,9]];
  const known=triangles.flatMap(t=>[[t[0],t[1]],[t[0],t[2]],[t[1],t[2]]]).concat(bars);
  if(!known.every(([a,b])=>adj[a][b]))continue;
  const six=triangles.flat();let n=0;for(let a=0;a<6;a++)for(let b=a+1;b<6;b++)if(adj[six[a]][six[b]])n++;
  assert.equal(n,9);witness={triangles,bars,known_edges:n};break;
 }
 assert(witness);proofs.push({B_mask:g.mask,labels,s,witness});
}
assert.equal(proofs.length,36);
const result={exact:true,graphs:9,label_contexts:contexts,budget_compatible_contexts:proofs.length,all_contain_induced_prism:true,proofs,
 scope:'P0 excludes heavy external carrier degree4 only. Remaining carriers and g18/g20 remain open.'};
fs.writeFileSync(new URL('./G18_G20_CARRIER_LOURD_P0.json',import.meta.url),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({exact:true,graphs:9,contexts,prisms:proofs.length,scope:result.scope}));
