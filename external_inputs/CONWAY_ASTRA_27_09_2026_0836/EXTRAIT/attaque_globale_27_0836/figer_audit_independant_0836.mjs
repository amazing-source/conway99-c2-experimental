import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const digest=b=>crypto.createHash('sha256').update(b).digest('hex');
const pairs=[
 ['THEOREME_CARACTERISTIQUE8_THETA.md','verifier_theta_caracteristique8'],
 ['THEOREME_MOMENTS_CARACTERISTIQUES8.md','verifier_moments_caracteristique8'],
 ['EXCLUSION_FRAME_D8_TROIS.md','verifier_frame_D8_trois'],
 ['AUDIT_GENERATION42_ET_COQUE_ENTIERE.md','verifier_coque_D8_mod2'],
 ['AUDIT_D11_ET_LIMITE_COQUE.md','verifier_D11_et_coque_D6'],
 ['ROOTLESS_SHADOWFRAME_CODE24_ET_OCTADES.md','verifier_rootless_code24'],
 ['AUDIT_HEPTADE_RANG4_ET_D6_BLOCS.md','verifier_heptade_et_D6_bornes'],
 ['AUDIT_D6_SIX_FRACTIONNAIRES_MEME_PAIRE.md','verifier_D6_fA6_independant'],
 ['AUDIT_Q42_ET_CLASSIFICATION_D6.md','verifier_Q42_et_collage_D6_independant'],
 ['AUDIT_D6_MIXTE_CENTRES_REPETES.md','verifier_D6_mixte_centres_independant'],
 ['AUDIT_FAMILLE_COMPLETE_D8_TROIS.md','verifier_collages_D8_independant']
];
const resultChecks=[];
for(const [note,stem] of pairs){
 const source=fs.readFileSync(path.join(here,stem+'.mjs'));
 const result=JSON.parse(fs.readFileSync(path.join(here,stem+'.json'),'utf8'));
 assert.equal(result.exact,true,stem+' executed exact result');
 assert.equal(result.source_sha256,digest(source),stem+' source binding');
 assert(fs.readFileSync(path.join(here,note),'utf8').length>100);
 resultChecks.push({source:stem+'.mjs',result:stem+'.json',exact:true});
}
const files=pairs.flatMap(([note,stem])=>[note,stem+'.mjs',stem+'.json']);
files.push('BILAN_AUDIT_INDEPENDANT_0836.md','figer_audit_independant_0836.mjs');
const entries=files.map(file=>{const bytes=fs.readFileSync(path.join(here,file));return{file,bytes:bytes.length,sha256:digest(bytes)};});
assert.equal(entries.length,35);assert.equal(new Set(files).size,35);
const dependencies=[
 '../attaque_globale_27_0803/MANIFEST_AUDIT_INDEPENDANT_0803.json',
 '../attaque_globale_27_0803/AUDIT_COLLAGE_E8_ET_SEPT_BLOCS.md',
 '../attaque_globale_27_0803/G18_G20_D12_COLLAGE.md',
 '../attaque_globale_27_0803/UNIFICATION_G18_G20_RANG24.md',
 '../attaque_globale_27_0803/verifier_golay_enveloppe_indep.json',
 '../attaque_globale_27_0803/controles_positifs_cadre_global.json',
 '../dossier6_involution/NOTE_RESEAU_MINIMUM.md',
 'controle_selection42_golay.json'
].map(file=>{const bytes=fs.readFileSync(path.join(here,file));return{file,bytes:bytes.length,sha256:digest(bytes),access:'read_only'};});
assert.equal(dependencies[0].sha256,'0ca8af0714d5edcf74e6ee5295fabf8e508678008d1d455a2fcb4bc2a6858ef8');
const theta=JSON.parse(fs.readFileSync(path.join(here,'verifier_theta_caracteristique8.json'),'utf8'));
for(const binding of theta.input_bindings)assert.equal(digest(fs.readFileSync(path.join(here,binding.file))),binding.sha256);
const q42=JSON.parse(fs.readFileSync(path.join(here,'verifier_Q42_et_collage_D6_independant.json'),'utf8'));
assert.equal(q42.input_sha256,dependencies.at(-1).sha256);
const out={exact:true,status:'frozen_own_outputs_only',scope:'Uniform mathematical consequences and explicitly conditional families of the same physical frame; no full g18/g20 exclusion.',
 file_count:entries.length,executed_exact_sources:resultChecks.length,entries,result_checks:resultChecks,
 dependencies,old_outputs_modified:false,new_local_type_exclusions:0,
 rootless_shadowframe_uniform:true,D8_three_entire_ambient_family_excluded:true,
 D6_four_entire_ambient_family_excluded:false,D6_same_pair_fractional_six_excluded:true,
 D6_mixed_regime_excluded:false,D6_mixed_centres_necessary:'four distinct centres, two B and two D; only when h7 is integral in AC',
 limitations:['No full odd-unimodular rank-24 classification','No universal shell Gram rank-20 bound','No shadowframe without the rootless hypothesis','Positive H2/BvLS parameters remain 3/9 and their own norms','Fixed Q42 fixtures do not satisfy all physical graph axioms']};
const manifest=path.join(here,'MANIFEST_AUDIT_INDEPENDANT_0836.json');
fs.writeFileSync(manifest,JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({exact:true,own_files:entries.length,executed_sources:resultChecks.length,manifest_sha256:digest(fs.readFileSync(manifest))}));
