// Controle exact fini d'une relaxation necessaire du MEME frame D6^4.
// Ni recherche de graphe, ni solveur, ni enumeration des normes7 signees.
import { writeFileSync } from 'node:fs';

function* compositions(total, length, prefix = []) {
  if (length === 1) { yield [...prefix, total]; return; }
  for (let n = 0; n <= total; n++) yield* compositions(total - n, length - 1, [...prefix, n]);
}
function subsets4(allowed) {
  const result = [];
  for (let a = 0; a < allowed.length; a++)
    for (let b = a + 1; b < allowed.length; b++)
      for (let c = b + 1; c < allowed.length; c++)
        for (let d = c + 1; d < allowed.length; d++) result.push([allowed[a], allowed[b], allowed[c], allowed[d]]);
  return result;
}
function rootPairNecessary(first, second) {
  if (first.unit_component !== second.unit_component) return true;
  return first.support.filter(x => second.support.includes(x)).length <= 2;
}

// h7 has four units at B2,B3,B4,B5. Orthogonality forces all centres
// at B0,B1 or in D. This fixes only harmless coordinate permutations.
let checked = 0, capacityPassed = 0, exactCapacityPassed = 0, withOneNormal = 0, survivingPairs = 0;
const oneNormalCases = [];
for (const multiplicities of compositions(6, 8)) {
  checked++;
  const mB = [multiplicities[0], multiplicities[1], 0, 0, 0, 0];
  const mD = multiplicities.slice(2);
  const tB = mB.map((m, j) => m + (j >= 2 ? 1 : 0));
  const maxB = Math.max(...tB), maxD = Math.max(...mD);
  if (maxB + maxD > 3) continue;
  capacityPassed++;
  if (tB.every(a => mD.every(b => a + b === 1 || a + b === 3))) exactCapacityPassed++;
  // A normal with four units in D has half-coordinates on B. For
  // every such D unit one characteristic has product +/-3. Therefore
  // maxB+mD[j] <= 1 is necessary, since k>=2 forces BOTH normals flat.
  const eligibleD = mD.flatMap((m, j) => maxB + m <= 1 ? [j] : []);
  const eligibleB = tB.flatMap((m, j) => m + maxD <= 1 ? [j] : []);
  const options = [
    ...subsets4(eligibleD).map(support => ({ unit_component: 'D', support })),
    ...subsets4(eligibleB).map(support => ({ unit_component: 'B', support })),
  ];
  if (options.length) {
    withOneNormal++;
    oneNormalCases.push({ mB, mD, normal_options: options });
  }
  // Repetition is allowed here: it is a SAFE SUPERSET of the actual
  // two signed orthogonal normals. Common >=3 unit axes already fail.
  for (const first of options) for (const second of options)
    if (rootPairNecessary(first, second)) survivingPairs++;
}

let signedPairs = 0;
for (let first = 0; first < 16; first++) for (let second = 0; second < 16; second++) {
  const a = Array.from({length: 4}, (_, j) => ((first >> j) & 1) ? -1 : 1);
  const b = Array.from({length: 4}, (_, j) => ((second >> j) & 1) ? -1 : 1);
  let witness = false;
  for (let i = 0; i < 4; i++) for (let j = i + 1; j < 4; j++) {
    const sign = a[i] * a[j];
    if (Math.abs(a[i] + sign * a[j]) === 2 && Math.abs(b[i] + sign * b[j]) === 2) witness = true;
  }
  if (!witness) throw new Error('Missing root witness for common four unit axes');
  signedPairs++;
}
if (checked !== 1716 || exactCapacityPassed !== 16 || survivingPairs !== 0) throw new Error('Coverage failed');
const result = {
  exact: true,
  scope: 'D6^4/C4, same physical frame49+two primitive normals; f_A=6 only',
  assumptions: ['fullframe=7I24','min(N*)>=8/7','J=7I2 primitive','seven h mutually orthogonal'],
  centre_distributions_checked: checked,
  characteristic_capacity_passed: capacityPassed,
  exact_characteristic_capacity_passed: exactCapacityPassed,
  distributions_with_one_relaxed_normal: withOneNormal,
  relaxed_two_normal_pairs: survivingPairs,
  common_four_axis_signed_pairs_checked: signedPairs,
  one_normal_cases: oneNormalCases,
  conclusion: 'f_A=6 impossible; symmetric f_B=6 impossible; no global g18/g20 exclusion',
};
writeFileSync(new URL('./G18_G20_D6_SIX_SPINORS.json', import.meta.url), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify({ exact: result.exact, checked, capacityPassed, exactCapacityPassed, withOneNormal, survivingPairs, signedPairs }));
