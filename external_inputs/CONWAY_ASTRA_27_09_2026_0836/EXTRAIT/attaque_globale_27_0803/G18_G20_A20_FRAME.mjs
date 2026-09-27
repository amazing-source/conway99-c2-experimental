import fs from 'node:fs';
import assert from 'node:assert/strict';
const exactTrace=(n,d)=>{
  const denominator=n+1;
  const weights=Array.from({length:n},(_,i)=>i+1).filter(k=>k*(n+1-k)<=3*denominator);
  const maxNumerator=Math.max(...weights.map(k=>k*(n+1-k)));
  const lhs=7*(n-d)*denominator,rhs=42*maxNumerator+28*denominator;
  return {n,d,admissible_k:weights,max_projection_norm:{numerator:maxNumerator,denominator},
    lower_trace_numerator:lhs,upper_trace_numerator:rhs,strict_gap_numerator:lhs-rhs,excluded:lhs>rhs};
};
const sameRank=[20,21,22].map(n=>exactTrace(n,0));
const rank24=[22,23,24].map(n=>exactTrace(n,2));
for(const row of sameRank.concat(rank24)){
  assert.equal(row.max_projection_norm.numerator,3*(row.n-2));
  assert.deepEqual(row.admissible_k,[1,2,3,row.n-2,row.n-1,row.n]);
  assert(row.excluded);
}
const boundary=[exactTrace(19,0),exactTrace(21,2)];
assert(boundary.every(row=>!row.excluded));
const out={exact:true,same_rank_22:sameRank,integral_extension_dimension_at_most24:rank24,
  boundary_not_closed_by_this_inequality:boundary,
  scope:'Common N22 frame and acquired dual gap8/7; no type catalogue, P0, g>=21 or entire g18/g20 exclusion.'};
fs.writeFileSync(new URL('./G18_G20_A20_FRAME.json',import.meta.url),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify(out));
