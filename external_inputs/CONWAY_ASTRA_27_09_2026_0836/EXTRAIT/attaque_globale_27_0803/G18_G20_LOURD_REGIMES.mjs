// Tiny independent capacity check on4 external vertices, not a completion search.
import fs from 'node:fs';
import assert from 'node:assert/strict';
const edges=[];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)edges.push([i,j]);
const graphs=Array.from({length:64},(_,mask)=>{
 const rows=Array(4).fill(0),degree=Array(4).fill(0);let n=0;
 for(let e=0;e<6;e++)if(mask&(1<<e)){const[i,j]=edges[e];rows[i]|=1<<j;rows[j]|=1<<i;degree[i]++;degree[j]++;n++;}
 return{mask,rows,degree,n};
});
const pop=x=>{let n=0;while(x){x&=x-1;n++;}return n;};
const regimes=[];
for(const difference of [4,5]){
 const survivors=[];let checked=0;
 for(const A of graphs)for(const B of graphs){
  checked++;if(B.n-A.n!==difference)continue;
  // Omit all unknown cross contributions: these are necessary lower bounds.
  if(edges.some(([i,j],e)=>(A.mask&(1<<e))&&pop(B.rows[i]&B.rows[j])>1))continue;
  if(B.degree.some((d,i)=>4-d+A.degree[i]>2))continue;
  if(difference===4)assert(A.n===0&&B.n===4&&B.degree.every(d=>d===2));
  else assert(A.n===0&&B.n===5);
  survivors.push({A:A.mask,B:B.mask,degree_B:B.degree});
 }
 assert.equal(survivors.length,difference===4?3:6);regimes.push({difference,checked,survivors});
}
let rowChecks=0,accepted=0;
for(let A=0;A<16;A++)for(let B=0;B<16;B++)if(pop(B)-pop(A)===1){
 for(let e=0;e<4;e++)if(A&(1<<e)){
  rowChecks++;if(pop(B&(15^(1<<e)))>1)continue;
  accepted++;assert.equal(pop(A),1);assert.equal(pop(B),2);assert(B&(1<<e));
 }
}
const pairs=[];for(let a=0;a<=3;a++)for(let b=0;b<=3;b++)if(12+2*(a-b)<=8)pairs.push([a,b]);
assert.deepEqual(pairs,[[0,2],[0,3],[1,3]]);
const out={exact:true,matching_edge_regimes:pairs,external:regimes,R3_row_checks:rowChecks,R3_accepted_rows:accepted,
 scope:'Necessary capacity regimes for the same norm14 heavy eigenvector. Not a graph/type completion or exclusion.'};
fs.writeFileSync(new URL('./G18_G20_LOURD_REGIMES.json',import.meta.url),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out));
