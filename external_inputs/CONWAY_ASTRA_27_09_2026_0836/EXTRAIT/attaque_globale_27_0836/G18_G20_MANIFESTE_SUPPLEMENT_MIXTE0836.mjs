// Raccord et freeze uniquement : aucun nouveau calcul de recherche.
import { readFileSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
function record(path) {
  const bytes = readFileSync(new URL(path, import.meta.url));
  return { path, bytes: bytes.length, sha256: createHash('sha256').update(bytes).digest('hex') };
}
const frozen = JSON.parse(readFileSync(new URL('./G18_G20_MANIFESTE_COMBINATOIRE0836.json', import.meta.url), 'utf8'));
for (const old of frozen.own) {
  const now = record(old.path);
  if (now.sha256 !== old.sha256 || now.bytes !== old.bytes) throw new Error(`Frozen file altered: ${old.path}`);
}
const ownNames = ['G18_G20_D6_MIXTE_CENTRES_REPETES.md','G18_G20_D6_MIXTE_CENTRES_REPETES.mjs',
  'G18_G20_D6_MIXTE_CENTRES_REPETES.json','G18_G20_MANIFESTE_SUPPLEMENT_MIXTE0836.mjs'];
const prerequisites = ['G18_G20_MANIFESTE_COMBINATOIRE0836.json',
  'G18_G20_D6_SIX_SPINORS.md','G18_G20_D6_QUATRE.md',
  'AUDIT_D6_MIXTE_CENTRES_REPETES.md',
  'verifier_D6_mixte_centres_independant.mjs','verifier_D6_mixte_centres_independant.json'];
const result = JSON.parse(readFileSync(new URL('./G18_G20_D6_MIXTE_CENTRES_REPETES.json', import.meta.url), 'utf8'));
if (result.exact !== true || result.pairs_passing_root_bound !== 0 || result.local_ratio_sign_cases_checked !== 64)
  throw new Error('Supplement control not complete');
const manifest = {
  kind: 'frozen_mathematical_supplement',
  same_frame: '42 u + 7 h + 2 primitive normals in D6^4 cycle glue',
  scope: 'f_A=4,f_B=2; h7 integer typeI in A/C, and symmetric version',
  conclusion: 'the four AC-spinor centres are distinct, exactly two in B and two in D',
  whole_mixed_regime_excluded: false,
  whole_D6_frame_excluded: false,
  new_complete_g18_g20_type_excluded: false,
  earlier_frozen_own_files_verified: frozen.own.length,
  own: ownNames.map(record), prerequisites: prerequisites.map(record),
};
const bytes = Buffer.from(JSON.stringify(manifest,null,2)+'\n');
writeFileSync(new URL('./G18_G20_MANIFESTE_SUPPLEMENT_MIXTE0836.json', import.meta.url), bytes);
console.log(JSON.stringify({exact: true, own: ownNames.length, prerequisites: prerequisites.length,
  frozen_files_intact: frozen.own.length, sha256: createHash('sha256').update(bytes).digest('hex')}));
