import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const cur=path.dirname(fileURLToPath(import.meta.url));
const prev=path.join(cur,'../attaque_globale_27_0803');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const title='# Preuves complètes — attaque directe du repère 42+7\n\n';
const allCurrent=(await fs.readdir(cur)).sort();
const exclude=new Set(['PREUVES_COMPLETES_REPERE42_7.md','DOSSIER_SOURCES_SORTIES_REPERE42_7.md','LIRE_D_ABORD.md']);
let proof=title+await fs.readFile(path.join(cur,'BILAN_ATTAQUE_DIRECTE_REPERE42_7.md'),'utf8');
proof+='\n\n---\n\n# Dépendances intégrales : campagne immédiatement précédente, 0803\n\n';
proof+=await fs.readFile(path.join(prev,'PREUVES_COMPLETES_ATTAQUE_GLOBALE.md'),'utf8');
for(const name of allCurrent.filter(n=>n.endsWith('.md')&&!exclude.has(n)&&n!=='BILAN_ATTAQUE_DIRECTE_REPERE42_7.md')){
 const data=await fs.readFile(path.join(cur,name));
 proof+='\n\n---\n\n# Pièce : '+name+'\n\nSHA256 : '+sha(data)+'\n\n'+data.toString('utf8');
}
await fs.writeFile(path.join(cur,'PREUVES_COMPLETES_REPERE42_7.md'),proof,'utf8');
let source='# Sources et sorties exactes — repère 42+7\n\nLes fichiers intégraux sont tous dans l’archive ; le domaine de 2,7 Mo reste dans son JSON original, sans troncature. Aucun graphe99 ni repère physique complet n’est produit.\n\n';
source+='## Campagne 0803, sources et sorties intégrales\n\n'+await fs.readFile(path.join(prev,'DOSSIER_COMPLET_SOURCES_ET_SORTIES.md'),'utf8');
const bt=String.fromCharCode(96).repeat(3);
for(const name of allCurrent.filter(n=>/\.(mjs|json|ps1)$/.test(n)&&n!=='MANIFESTE_REPERE42_7.json')){
 const data=await fs.readFile(path.join(cur,name));
 source+='\n\n## '+name+'\n\n'+data.length+' octets ; SHA256 '+sha(data)+'\n\n';
 if(data.length>300000){source+='Fichier volumineux fourni intégralement et séparément dans l’archive. Sa source génératrice figure dans ce document.\n';continue;}
 source+=bt+(name.endsWith('.mjs')?'javascript':name.endsWith('.ps1')?'powershell':'json')+'\n'+data.toString('utf8')+'\n'+bt+'\n';
}
await fs.writeFile(path.join(cur,'DOSSIER_SOURCES_SORTIES_REPERE42_7.md'),source,'utf8');
const entries=[];
for(const [folder,dir] of [['attaque_globale_27_0836',cur],['attaque_globale_27_0803',prev]]){
 for(const item of (await fs.readdir(dir,{withFileTypes:true})).sort((a,b)=>a.name.localeCompare(b.name))){
  if(!item.isFile()||item.name.endsWith('.zip')||(folder==='attaque_globale_27_0836'&&item.name==='MANIFESTE_REPERE42_7.json'))continue;
  const data=await fs.readFile(path.join(dir,item.name));
  entries.push({path:folder+'/'+item.name,bytes:data.length,sha256:sha(data)});
 }
}
const manifest={campaign:'2026-09-27 0836 UTC',scope:'full physical 42+7+2 frame, g18 and g20, no P=0',whole_goals_closed:false,former_snapshot_unchanged:true,archive:'../ATTAQUE_DIRECTE_27_0836_PREUVES_CERTIFICATS.zip',files:entries};
await fs.writeFile(path.join(cur,'MANIFESTE_REPERE42_7.json'),JSON.stringify(manifest,null,2)+'\n','utf8');
console.log(JSON.stringify({proof_bytes:Buffer.byteLength(proof),sources_bytes:Buffer.byteLength(source),manifest_files:entries.length,manifest_sha256:sha(await fs.readFile(path.join(cur,'MANIFESTE_REPERE42_7.json')))}));
