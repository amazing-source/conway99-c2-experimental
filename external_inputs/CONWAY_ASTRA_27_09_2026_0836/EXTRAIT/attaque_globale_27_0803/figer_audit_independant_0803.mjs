// Freeze only this audit agent's new0803 files. Never writes any old folder or producer file.
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';import assert from 'node:assert/strict';import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url)),sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const ownNotes=['AUDIT_NORME1_ET_METRIQUES.md','AUDIT_COLLAGE_E8_ET_SEPT_BLOCS.md','AUDIT_INDECOMPOSABILITE.md','AUDIT_COMPOSANTES_RACINES_ET_CARRIER.md','AUDIT_RACINES_CORANG_UN.md','AUDIT_GOLAY_ENVELOPPE.md'];
const runs=['verifier_identites_courtes','verifier_collage_E8_P','verifier_indecomposabilite_courte','verifier_carrier_lourd_indep','verifier_corang_un_indep','verifier_golay_enveloppe_indep'];
const own=ownNotes.concat(runs.flatMap(s=>[s+'.mjs',s+'.json']),['figer_audit_independant_0803.mjs']);
const entry=f=>{const bytes=fs.readFileSync(path.join(here,f));return{path:f,bytes:bytes.length,sha256:sha(bytes)};};
const runChecks=[];
for(const s of runs){const result=JSON.parse(fs.readFileSync(path.join(here,s+'.json'),'utf8'));assert.equal(result.exact,true);assert.equal(result.source_sha256,entry(s+'.mjs').sha256);runChecks.push({source:s+'.mjs',result:s+'.json',exact:true});}
const collage=JSON.parse(fs.readFileSync(path.join(here,'verifier_collage_E8_P.json')));
for(const e of collage.prior)assert.equal(entry(e.path).sha256,e.sha256);
const carrier=JSON.parse(fs.readFileSync(path.join(here,'verifier_carrier_lourd_indep.json')));
for(const e of carrier.prior)assert.equal(entry(e.path).sha256,e.sha256);
const corang=JSON.parse(fs.readFileSync(path.join(here,'verifier_corang_un_indep.json')));
assert.equal(entry('RACINES_CORANG_UN_CANDIDAT.md').sha256,corang.producer_note_sha256);
const golay=JSON.parse(fs.readFileSync(path.join(here,'verifier_golay_enveloppe_indep.json')));
assert.equal(entry('controle_enveloppe_g20_golay.json').sha256,golay.supplied_certificate_sha256);
assert.equal(entry('controle_enveloppe_g20_golay.mjs').sha256,golay.producer_source_sha256);
const inputFiles=[
 '../dossier6_involution/NOTE_RESEAU_MINIMUM.md','../dossier6_involution/AUDIT_GENRE.md','../reprise_27_0636/CONTROLES_MOMENTS_ENTIERS_REMOTE.json',
 'INDECOMPOSABILITE_GLOBALE.md','RACINES_CORANG_UN_CANDIDAT.md','SEPT_BLOCS_CARACTERISTIQUES_ET_COLLAGE.md','UNIFICATION_G18_G20_RANG24.md',
 'G18_G20_NORME14_LOURDS.md','G18_G20_LOURD_REGIMES.md','G18_G20_CARRIER_LOURD_P0.md','G18_G20_CARRIER_LOURD_P0.mjs','G18_G20_CARRIER_LOURD_P0.json',
 'G18_G20_E8_MINUSCULE.md','G18_G20_D13_FRAME.md','G18_G20_D11_D12_DANS_N.md','G18_G20_D12_COLLAGE.md','G18_G20_A20_FRAME.md',
 'CONTRE_MODELE_ENVELOPPE_G20_GOLAY.md','controle_enveloppe_g20_golay.mjs','controle_enveloppe_g20_golay.json',
 'TEMPLATE_CONDITIONNEL_SHADOW24.md','BILAN_ATTAQUE_GLOBALE.md','controles_positifs_cadre_global.mjs','controles_positifs_cadre_global.json'
 ];
const manifest={status:'AUDIT INDEPENDANT ACQUIS; own0803 pieces frozen',own_files:own.map(entry),inputs_read_snapshot:inputFiles.map(entry),runChecks,
 inputs_policy:'Snapshots of external sources read for audit. They are not modified or frozen by this script. Old files remain read-only.',
 acquired_human_proofs:[
  'Correct separation of standard21/28 coefficient Grams, real4 block Gram and beta on imH',
  'Known dual minimum8/7 with exact common-neighbor recount; no novelty claim',
  'Indecomposability of N and same-rank integral minimum2 overlattices via two uniform proofs',
  'Primitive P of seven blocks, det2^12, discr(Z/4)^6, complement rank15/classes5/2',
  'Rank22 and rank21 root strata impossible in det49 elementary2 lattice carrying the physical real22 frame',
  'E8 absent in integral extensions of rank<=24; D>=11 and A>=20 absent in rank22 frame lattice; D>=12 and A>=22 absent in extensions<=24',
  'Heavy norm2 branch has6 incident roots,4 external and three physical regimes; P0 carrier degree4 excluded',
  'Three norm8 characteristic profiles in conditional unimodular24 gluing; root3 saturation remains a constraint',
  'Positive Golay-envelope example independently replayed: rank22det49/min3/gen3/indecomposable/dual>=10/7/char>=10, no physical frame'
 ],
 scope_hypotheses:'SRG99 signed integer frame and old structural discriminant reduction for g18/g20 are assumed where named. Corank-one proof needs rank22/det49/elementary7 rank2/min2/full real frame. P0 is used only for the carrier cut. A shadowframe24 is conditional.',
 positive_controls:{small_H2_rebuilt_by_audit:true,H2_r:1,H2_d:3,H2_root_norm:1,BvLS_r:4,BvLS_d:9,BvLS_root_norm:4,new_parent_controls_reviewed_not_rerun_by_audit:true,SRG99_F7_P0_not_imposed:true},
 remaining_open:['Both g18 and g20 involution cases','Norm2 flat and residual heavy carriers','All three characteristic8 profiles','Existence of shadowframe24','Selection of exactly42 roots/7 blocks satisfying the common physical frame in the Golay-envelope or another genus lattice'],
 no_solver:true,no_Web:true,no_repository_access:true,no_local_Python:true,no_heavy_local_search:true,whole_type_exclusions_added:0,
 historical_local_ledger_unchanged:{g18_closed:278,g18_open:163},self_hash_omitted:true};
fs.writeFileSync(path.join(here,'MANIFEST_AUDIT_INDEPENDANT_0803.json'),JSON.stringify(manifest,null,2)+'\n');
console.log(JSON.stringify({own_files:own.length,input_snapshots:inputFiles.length,exact_runs:runChecks.length,source_bindings_current:true,whole_type_exclusions_added:0}));
