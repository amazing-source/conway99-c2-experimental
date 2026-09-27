import fs from 'node:fs';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
const here=fileURLToPath(import.meta.url);
const b=(x,y)=>{let z=0;for(let i=0;i<3;i++){const a=(x>>(2*i))&3,c=(y>>(2*i))&3;z^=((a&1)*((c>>1)&1))^(((a>>1)&1)*(c&1));}return z&1;};
const cost=x=>{let z=0;for(let i=0;i<3;i++){const a=(x>>(2*i))&3;z+=(a===3?1:a===0?0:2);}return z;};
const all=new Map();
for(let x=1;x<64;x++)for(let y=x+1;y<64;y++){
 if(b(x,y))continue;
 const two=[0,x,y,x^y];
 for(let z=y+1;z<64;z++){
  if(two.includes(z)||b(x,z)||b(y,z))continue;
  const h=[...two,...two.map(a=>a^z)].sort((a,c)=>a-c);
  all.set(h.join(','),h);
 }
}
assert.equal(all.size,135);
const counters={even:0,odd:0,min1:0,E8:0,D16:0,admissible:0};
const witnesses=[];
for(const h of all.values()){
 assert.equal(h.length,8);
 for(const x of h)for(const y of h)assert.equal(b(x,y),0);
 if(h.every(x=>cost(x)%2===0)){counters.even++;continue;}
 counters.odd++;
 if(h.some(x=>cost(x)===1)){counters.min1++;continue;}
 const singleton=x=>[0,1,2].filter(i=>((x>>(2*i))&3)!==0).length===1;
 if(h.some(x=>cost(x)===2&&singleton(x))){counters.E8++;continue;}
 if(h.some(x=>cost(x)===2&&!singleton(x))){counters.D16++;continue;}
 const shell=h.filter(x=>cost(x)===3);
 const integral_components=[0,1,2].filter(i=>shell.every(x=>[0,3].includes((x>>(2*i))&3)));
 assert(shell.length>0);assert(integral_components.length>0);
 counters.admissible++;
 witnesses.push({glue:h,minima:h.map(cost),norm3_classes:shell,integral_components});
}
assert.deepEqual(counters,{even:30,odd:105,min1:37,E8:24,D16:12,admissible:32});
const shape=witnesses.reduce((a,w)=>{const k=w.norm3_classes.length+':'+w.integral_components.length;a[k]=(a[k]||0)+1;return a;},{});
assert.deepEqual(shape,{'2:1':24,'1:3':8});
const result={exact:true,counters,shape,witnesses,scope:'All odd unimodular glues of D8^3 with min>=2 and no E8/D16 admit at least one full integral coordinate component on the complete norm3 shell; the dual gap then excludes the whole physical frame for g18 and g20.',source_sha256:crypto.createHash('sha256').update(fs.readFileSync(here)).digest('hex')};
fs.writeFileSync(here.replace(/\.mjs$/,'.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({exact:result.exact,counters,shape,witnesses:witnesses.length,source_sha256:result.source_sha256}));
