import fs from 'node:fs';import assert from 'node:assert/strict';
const factorNorms=[];for(let t=0;t<=4;t++)if(7*t===t*t+3*t)factorNorms.push(t);
assert.deepEqual(factorNorms,[0,4]);
const offDiagonal=[];for(let g=-4;g<=4;g++)if([-1,0,1].includes(3*g))offDiagonal.push(g);
assert.deepEqual(offDiagonal,[0]);
const multiplicities={0:2,3:7,7:3};
assert.equal(2+7+3,12);assert.equal(3*7+7*3,42);
const incidenceValues=[];for(const eigen of [0,3,7]){
 const ph=eigen*(7-eigen)/12;assert(ph===0||ph===1);incidenceValues.push(4*ph);
}
assert(incidenceValues.every(x=>x!==2));
assert.equal(7*(12-2),42+7*4);assert.equal(4/2**2,1);
const out={exact:true,trace_equality:70,axis_multiplicities:multiplicities,possible_column_incidence_norms:incidenceValues,
 required_D7_column_incidence_norm:2,factor_projection_norms:factorNorms,factor_off_diagonal:offDiagonal,
 spinor_extension:{rank:12,index:2,determinant:1},
 scope:'No D12 root sub-system in any integral extension of dimension<=24 containing the common N22 frame and dual gap8/7. No entire g18/g20 exclusion.'};
fs.writeFileSync(new URL('./G18_G20_D12_COLLAGE.json',import.meta.url),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out));
