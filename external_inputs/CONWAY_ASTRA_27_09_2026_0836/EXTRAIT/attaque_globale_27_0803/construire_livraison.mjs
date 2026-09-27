async function buildGlobalDelivery(dir) {
const fs = await import('node:fs/promises'), path = await import('node:path'), crypto = await import('node:crypto'), zlib = await import('node:zlib');
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const excluded = new Set(['PREUVES_COMPLETES_ATTAQUE_GLOBALE.md','DOSSIER_COMPLET_SOURCES_ET_SORTIES.md','MANIFESTE_ATTAQUE_GLOBALE.json','ATTAQUE_GLOBALE_27_0803_PREUVES_CERTIFICATS.zip','AUDIT_LIVRAISON.json']);
const base = (await fs.readdir(dir)).filter(n => !excluded.has(n)).sort();
const notes = base.filter(n => n.endsWith('.md') && n !== 'BILAN_ATTAQUE_GLOBALE.md' && n !== 'ETAT_REPRISE.md');
const order = ['BILAN_ATTAQUE_GLOBALE.md','UNIFICATION_G18_G20_RANG24.md','INDECOMPOSABILITE_GLOBALE.md','RACINES_CORANG_UN_CANDIDAT.md','CONTRE_MODELE_ENVELOPPE_G20_GOLAY.md',...notes.filter(n => !['UNIFICATION_G18_G20_RANG24.md','INDECOMPOSABILITE_GLOBALE.md','RACINES_CORANG_UN_CANDIDAT.md','CONTRE_MODELE_ENVELOPPE_G20_GOLAY.md'].includes(n)),'ETAT_REPRISE.md'];
let proof = '# Preuves complètes — attaque globale du 27 septembre 2026\n\nCe dossier rassemble les preuves, les audits adverses et les limites de cette reprise. Il ne démontre pas l’inexistence de l’involution. Les deux valeurs g⁻=18 et g⁻=20 sont traitées par un cadre commun, sans balayage des types locaux.\n\n';
for (const n of order) proof += '\n\n---\n\nPièce originale : '+n+'\n\n'+await fs.readFile(path.join(dir,n),'utf8');
await fs.writeFile(path.join(dir,'PREUVES_COMPLETES_ATTAQUE_GLOBALE.md'),proof);
let complete = proof+'\n\n---\n\n# Programmes exacts et sorties intégrales\n\nLes programmes mathématiques sont des contrôles bornés ; les scripts de manifeste ne sont pas des preuves de non-existence. Les sorties complètes comprennent la base de 22 vecteurs et le Gram du contrôle positif.\n\n';
for (const n of base.filter(n => n.endsWith('.mjs') || n.endsWith('.json'))) complete += '\n\n## '+n+'\n\n````'+(n.endsWith('.json')?'json':'javascript')+'\n'+await fs.readFile(path.join(dir,n),'utf8')+'\n````\n';
await fs.writeFile(path.join(dir,'DOSSIER_COMPLET_SOURCES_ET_SORTIES.md'),complete);
const prefix = path.basename(dir);
const payload = [];
for (const n of [...base,'PREUVES_COMPLETES_ATTAQUE_GLOBALE.md','DOSSIER_COMPLET_SOURCES_ET_SORTIES.md'].sort()) {const data=await fs.readFile(path.join(dir,n));payload.push({name:prefix+'/'+n,data});}
const prerequisiteNames = ['dossier6_involution/NOTE_RESEAU_MINIMUM.md','dossier6_involution/AUDIT_GENRE.md','reprise_27_0636/CONTROLES_MOMENTS_ENTIERS_REMOTE.json'];
for(const n of prerequisiteNames){const data=await fs.readFile(path.join(path.dirname(dir),n));payload.push({name:n,data});}
const manifest={status:'Livraison de preuves partielles uniformes; aucune exclusion complète g18/g20',scope:'Reprise 27 septembre 2026 à 08:03 UTC; fichiers produits dans cette conversation uniquement',files:payload.map(e=>({path:e.name,bytes:e.data.length,sha256:sha(e.data)})),prerequisites_from_previous_campaign:prerequisiteNames,positive_controls:['H(2,3), r=1,d=3','BvLS, r=4,d=9','Réseau complémentaire de rang22/det49, construction explicite Golay']};
const manifestBytes=Buffer.from(JSON.stringify(manifest,null,2)+'\n');await fs.writeFile(path.join(dir,'MANIFESTE_ATTAQUE_GLOBALE.json'),manifestBytes);payload.push({name:prefix+'/MANIFESTE_ATTAQUE_GLOBALE.json',data:manifestBytes});
const table=Array.from({length:256},(_,i)=>{let c=i;for(let j=0;j<8;j++)c=(c&1)?0xedb88320^(c>>>1):c>>>1;return c>>>0;});const crc = b=>{let c=0xffffffff;for(const v of b)c=table[(c^v)&255]^(c>>>8);return(c^0xffffffff)>>>0;};
const locals=[],central=[];let offset=0;
for(const e of payload){const name=Buffer.from(e.name),compressed=zlib.deflateRawSync(e.data),c=crc(e.data);const h=Buffer.alloc(30);h.writeUInt32LE(0x04034b50);h.writeUInt16LE(20,4);h.writeUInt16LE(0x800,6);h.writeUInt16LE(8,8);h.writeUInt16LE(8<<11,10);h.writeUInt16LE(((2026-1980)<<9)|(9<<5)|27,12);h.writeUInt32LE(c,14);h.writeUInt32LE(compressed.length,18);h.writeUInt32LE(e.data.length,22);h.writeUInt16LE(name.length,26);locals.push(h,name,compressed);const ch=Buffer.alloc(46);ch.writeUInt32LE(0x02014b50);ch.writeUInt16LE(20,4);ch.writeUInt16LE(20,6);ch.writeUInt16LE(0x800,8);ch.writeUInt16LE(8,10);ch.writeUInt16LE(h.readUInt16LE(10),12);ch.writeUInt16LE(h.readUInt16LE(12),14);ch.writeUInt32LE(c,16);ch.writeUInt32LE(compressed.length,20);ch.writeUInt32LE(e.data.length,24);ch.writeUInt16LE(name.length,28);ch.writeUInt32LE(offset,42);central.push(ch,name);offset+=h.length+name.length+compressed.length;}
const centralBytes=Buffer.concat(central),end=Buffer.alloc(22);end.writeUInt32LE(0x06054b50);end.writeUInt16LE(payload.length,8);end.writeUInt16LE(payload.length,10);end.writeUInt32LE(centralBytes.length,12);end.writeUInt32LE(offset,16);const archive=Buffer.concat([...locals,centralBytes,end]);const zipName='ATTAQUE_GLOBALE_27_0803_PREUVES_CERTIFICATS.zip';await fs.writeFile(path.join(dir,zipName),archive);
return{zip:zipName,bytes:archive.length,entries:payload.length,sha256:sha(archive),proof_bytes:Buffer.byteLength(proof),full_bytes:Buffer.byteLength(complete),manifest_sha256:sha(manifestBytes)};
}
import {fileURLToPath} from 'node:url';
import path from 'node:path';
console.log(JSON.stringify(await buildGlobalDelivery(path.dirname(fileURLToPath(import.meta.url))),null,2));
