// Controle exact du dernier argument de couverture unitaire, pas un solveur.
import { writeFileSync } from 'node:fs';
function* compositions(total, count, p = []) {
  if (count === 1) { yield [...p, total]; return; }
  for (let v = 0; v <= total; v++) yield* compositions(total - v, count - 1, [...p, v]);
}
const units = [];
for (let component = 0; component < 2; component++)
  for (let a = 0; a < 6; a++) for (let b = a + 1; b < 6; b++)
    for (let c = b + 1; c < 6; c++) for (let d = c + 1; d < 6; d++) {
      const support = [a,b,c,d].map(j => j + 6*component);
      units.push({ component, support, vector: Array.from({length: 12}, (_, j) => support.includes(j) ? 1 : 0) });
    }
let checked = 0, repeated = 0, diagonalContexts = 0, coveredPairs = 0, survivingPairs = 0;
const hist = {};
for (const centres of compositions(4, 12)) {
  checked++;
  if (Math.max(...centres) <= 1) continue;
  repeated++;
  for (let tB = 0; tB <= 2; tB++) {
    const tD = 2 - tB;
    const residual = centres.map((m, j) => (j < 6 ? tB : tD) - m);
    if (residual.some(x => x < 0 || x > 2)) continue;
    diagonalContexts++;
    const profile = centres.filter(x => x > 0).sort((a,b) => b-a).join('+');
    hist[profile] = (hist[profile] || 0) + 1;
    for (const first of units) for (const second of units) {
      if (!residual.every((v,j) => v === first.vector[j] + second.vector[j])) continue;
      coveredPairs++;
      const common = first.support.filter(j => second.support.includes(j)).length;
      // If >=3 unit axes are shared, two sign ratios agree. A root on
      // those axes has absolute pairing2 with BOTH normals: 8>6.
      if (first.component !== second.component || common <= 2) survivingPairs++;
    }
  }
}
if (checked !== 1365 || repeated !== 870 || diagonalContexts !== 150 || coveredPairs !== 270 || survivingPairs !== 0)
  throw new Error('Unexpected exact coverage');
let localSignCases = 0;
for (let mB = 0; mB <= 1; mB++) for (let mD = 0; mD <= 1; mD++)
  for (let bits = 0; bits < 16; bits++) {
    const [b1,b2,d1,d2] = Array.from({length: 4}, (_, j) => ((bits>>j)&1) ? -1 : 1);
    const first = b1*d1, second = b2*d2;
    const rPlus = (first === 1 ? 1 : 0) + (second === 1 ? 1 : 0);
    const kPlus = mB+mD+rPlus, kMinus = mB+mD+2-rPlus;
    const exactCapacity = [1,3].includes(kPlus) && [1,3].includes(kMinus);
    const ratioRelation = b1*b2*d1*d2 === -((-1)**(mB+mD));
    if (exactCapacity !== ratioRelation) throw new Error('Incorrect local ratio equivalence');
    localSignCases++;
  }
const splitProfiles = [];
for (let b = 0; b <= 4; b++) for (const epsilon of [-1,1]) {
  const d = 4-b;
  const ratiosB = Array.from({length: 6}, (_, j) => epsilon*((-1)**(j<b ? 1 : 0)));
  const ratiosD = Array.from({length: 6}, (_, j) => -epsilon*((-1)**(j<d ? 1 : 0)));
  const inner = (ratiosB.reduce((a,v)=>a+v,0)+ratiosD.reduce((a,v)=>a+v,0))/4;
  if (inner !== epsilon*(2-b)) throw new Error('Incorrect spinor inner product');
  splitProfiles.push({ centres_B: b, centres_D: d, epsilon, spinor_inner: inner, orthogonal: inner === 0 });
}
const result = {
  exact: true,
  scope: 'D6^4/C4, f_A=4,f_B=2, h7 integer typeI supported in A or C, common physical normals',
  assumptions: ['fullframe=7I24','min(N*)>=8/7','J=7I2 primitive','seven h mutually orthogonal'],
  all_four_centre_distributions: checked,
  repeated_centre_distributions: repeated,
  diagonal_compatible_repeated_contexts: diagonalContexts,
  profiles: hist,
  ordered_unit_support_pairs_covering_diagonal: coveredPairs,
  pairs_passing_root_bound: survivingPairs,
  local_ratio_sign_cases_checked: localSignCases,
  split_profiles: splitProfiles,
  conclusion: 'the four centres of the AC-spinor blocks must be distinct, two in B and two in D; whole mixed regime not excluded',
};
writeFileSync(new URL('./G18_G20_D6_MIXTE_CENTRES_REPETES.json', import.meta.url), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify(result));
