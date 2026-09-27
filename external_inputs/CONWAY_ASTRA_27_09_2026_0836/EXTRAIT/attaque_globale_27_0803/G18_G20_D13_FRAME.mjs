import fs from 'node:fs';import assert from 'node:assert/strict';
const rows=[];
for(let n=13;n<=24;n++){
 const lower=7*(n-2),upper=42+7*4;
 assert(n>4*3);assert(lower>upper);
 rows.push({Dn_rank:n,half_weight_norm:n+'/4',half_weight_exceeds_root_generator_norm3:true,
  common_space_dimension:22,extension_dimension_at_most:24,frame_trace_lower:lower,frame_trace_upper:upper,strict_gap:lower-upper});
}
const out={exact:true,rows,scope:'No D_n,n>=13, in any integral extension of dimension<=24 containing the common N22 frame and dual gap8/7. No entire g18/g20 exclusion.'};
fs.writeFileSync(new URL('./G18_G20_D13_FRAME.json',import.meta.url),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({exact:true,rows:rows.length,first:rows[0],last:rows.at(-1)}));
