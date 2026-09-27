// Fige uniquement les pieces propres de cette reprise ; aucun calcul de recherche.
import { readFileSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';

const ownNames = [
  'G18_G20_QUARANTE_DEUX_GENERATEURS.md',
  'G18_G20_DUAL_COORDONNEES.md',
  'G18_G20_D6_QUATRE.md','G18_G20_D6_QUATRE.mjs','G18_G20_D6_QUATRE.json',
  'G18_G20_D6_SIX_SPINORS.md','G18_G20_D6_SIX_SPINORS.mjs','G18_G20_D6_SIX_SPINORS.json',
  'G18_G20_SEPT_BLOCS_CAPACITE.md','G18_G20_SEPT_BLOCS_CAPACITE.mjs',
  'G18_G20_TEST_SEPT_BLOCS.mjs','G18_G20_TEST_SEPT_BLOCS.json',
  'G18_G20_STATUTS_COMBINATOIRES0836.md','G18_G20_MANIFESTE_COMBINATOIRE0836.mjs',
];
const prerequisitePaths = [
  '../attaque_globale_27_0803/UNIFICATION_G18_G20_RANG24.md',
  '../attaque_globale_27_0803/SEPT_BLOCS_CARACTERISTIQUES_ET_COLLAGE.md',
  '../attaque_globale_27_0803/AUDIT_COLLAGE_E8_ET_SEPT_BLOCS.md',
  '../attaque_globale_27_0803/G18_G20_D12_COLLAGE.md',
  '../attaque_globale_27_0803/G18_G20_MANIFESTE_COMBINATOIRE.json',
  'AUDIT_GENERATION42_ET_COQUE_ENTIERE.md',
  'AUDIT_D11_ET_LIMITE_COQUE.md',
  'verifier_D11_et_coque_D6.mjs','verifier_D11_et_coque_D6.json',
  'AUDIT_D6_SIX_FRACTIONNAIRES_MEME_PAIRE.md',
  'verifier_D6_fA6_independant.mjs','verifier_D6_fA6_independant.json',
];
function record(path) {
  const bytes = readFileSync(new URL(path, import.meta.url));
  return { path, bytes: bytes.length, sha256: createHash('sha256').update(bytes).digest('hex') };
}
const checks = ['G18_G20_D6_QUATRE.json','G18_G20_D6_SIX_SPINORS.json','G18_G20_TEST_SEPT_BLOCS.json'];
for (const name of checks) {
  if (JSON.parse(readFileSync(new URL(name, import.meta.url), 'utf8')).exact !== true) throw new Error(`Nonexact output: ${name}`);
}
const manifest = {
  kind: 'frozen_own_mathematical_sources_and_bounded_controls',
  scope: 'physical frame49, explicit envelopes; no new complete local type or g18/g20 exclusion',
  conclusions: {
    generation42: true,
    D11_in_U_dim24_excluded: true,
    D6_cycle_individual_h_classification_complete: true,
    D6_six_spinors_one_opposite_pair_excluded: true,
    D6_cycle_whole_frame_excluded: false,
    seven_Golay_selections_exhausted: false,
  },
  independent_f6_report: 'acquired; separate supplement, not substituted by producer control',
  own: ownNames.map(record),
  prerequisites: prerequisitePaths.map(record),
  checks: checks.map(name => ({ path: name, exact: true })),
};
const bytes = Buffer.from(JSON.stringify(manifest, null, 2) + '\n');
writeFileSync(new URL('./G18_G20_MANIFESTE_COMBINATOIRE0836.json', import.meta.url), bytes);
console.log(JSON.stringify({ exact: true, own: ownNames.length, prerequisites: prerequisitePaths.length,
  sha256: createHash('sha256').update(bytes).digest('hex') }));
