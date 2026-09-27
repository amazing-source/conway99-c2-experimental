import fs from 'node:fs';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
const folder=new URL('./',import.meta.url);
const stems=['G18_G20_NORME14_LOURDS','G18_G20_LOURD_REGIMES','G18_G20_CARRIER_LOURD_P0',
  'G18_G20_E8_MINUSCULE','G18_G20_D13_FRAME','G18_G20_D12_COLLAGE','G18_G20_A20_FRAME'];
const own=stems.flatMap(stem=>['md','mjs','json'].map(ext=>`${stem}.${ext}`)).concat([
  'G18_G20_D11_D12_DANS_N.md','G18_G20_STATUTS_ET_PARAMETRES.md','G18_G20_MANIFESTE_COMBINATOIRE.mjs']);
const prerequisites=['AUDIT_NORME1_ET_METRIQUES.md','AUDIT_INDECOMPOSABILITE.md',
  'INDECOMPOSABILITE_GLOBALE.md','AUDIT_RACINES_CORANG_UN.md','RACINES_CORANG_UN_CANDIDAT.md',
  'controles_positifs_cadre_global.mjs','controles_positifs_cadre_global.json',
  'verifier_carrier_lourd_indep.mjs','verifier_carrier_lourd_indep.json'];
const record=name=>{const bytes=fs.readFileSync(new URL(name,folder));return {
  name,bytes:bytes.length,sha256:crypto.createHash('sha256').update(bytes).digest('hex')};};
const tests=stems.map(stem=>{
  const name=`${stem}.json`,data=JSON.parse(fs.readFileSync(new URL(name,folder),'utf8'));
  assert.equal(data.exact,true,`${name}: exact`);
  return {name,exact:true,scope:data.scope??'Finite step checks only; see the associated proof.'};
});
const positive=JSON.parse(fs.readFileSync(new URL('controles_positifs_cadre_global.json',folder),'utf8'));
assert.equal(positive.exact,true);
assert.deepEqual(positive.results.map(row=>[row.vertices,row.m,row.r,row.d]),[[9,2,1,3],[243,11,4,9]]);
const sourceBytes=fs.readFileSync(new URL('controles_positifs_cadre_global.mjs',folder));
assert.equal(crypto.createHash('sha256').update(sourceBytes).digest('hex'),positive.source_sha256);
const out={frozen_own_pieces:true,own_count:own.length,own:own.map(record),
  bound_prerequisites:prerequisites.map(record),existing_finite_tests:tests,
  positive_controls:{exact:true,source_hash_matches:true,own_parameters_preserved:true,new_execution:false},
  claims:{same_rank22:{E8_excluded:true,D_n_excluded_from:11,A_n_excluded_from:20},
    integral_extension_dimension_at_most24:{E8_excluded:true,D_n_excluded_from:12,A_n_excluded_from:22},
    root_rank20_requires_Nmax_det49_and_elementary_discriminant_dimension2:true,
    P0_only_for_carrier_appendix:true},
  limitations:['No g>=21 conclusion.','No uniform g18/g20 exclusion.',
    'The flat norm2 branch and remaining heavy regimes are open.',
    'D11 and A20/A21 in rank24 are not closed here.','No graph is certified.'],
  scope:'Read-only hash binding and documentary closure, not a new graph search or a proof of the full genre exclusion.'};
fs.writeFileSync(new URL('G18_G20_MANIFESTE_COMBINATOIRE.json',folder),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({frozen_own_pieces:true,own_count:out.own_count,prerequisites:prerequisites.length,
  existing_tests_exact:tests.length,positive_parameters_bound:true,no_full_g18_g20_exclusion:true}));
