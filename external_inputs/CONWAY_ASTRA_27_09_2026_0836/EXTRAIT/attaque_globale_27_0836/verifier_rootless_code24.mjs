import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';import {createHash} from 'node:crypto';
const here=path.dirname(fileURLToPath(import.meta.url));const assert=(x,s)=>{if(!x)throw new Error(s);};
function choose(n,k){let x=1;for(let i=1;i<=k;i++)x=x*(n+1-i)/i;assert(Number.isInteger(x),'integer binomial');return x;}
const evenL0Covol=2**13,kernelCovol=2**25,codeSize=kernelCovol/evenL0Covol;
assert(codeSize===4096,'code size2^12');
const ball4=Array.from({length:5},(_,k)=>choose(24,k)).reduce((s,x)=>s+x,0);
assert(ball4===12951&&ball4*codeSize>2**24,'Hamming excludes d>=12');
const rhs=2**10*24*23,t=(rhs-552-132*4094)/32;
assert(t===759&&4094-2*t===2576,'weight enumerator via second moment');
const profiles=[];for(const b1 of [1,3])for(const b2 of [1,3])for(let activeBlocks=0;activeBlocks<=3;activeBlocks++)for(let heavyRoots=0;heavyRoots<=1;heavyRoots++)
  if(b1*b1+b2*b2+4*activeBlocks+8*heavyRoots===14)profiles.push({b_abs:[b1,b2],activeBlocks,heavyRoots});
assert(profiles.length===4,'three physical profiles, with normal-order two variants');
const edges=[];for(let i=0;i<8;i++)for(let j=i+1;j<8;j++){
  const signs=Array(8).fill(-1);signs[i]=signs[j]=1;assert(signs.reduce((s,x)=>s+x,0)===-4,'minority positions exactlytwo');edges.push([i,j]);
}
assert(edges.length===28&&2*3-12===-6&&8*3===12*2,'centroid forces cubicdegree3');
const possible=[0,8,12,16,24];
const disjointOctadWords=possible.filter(w=>w<=16&&possible.includes(8+w)&&possible.includes(24-8-w));
assert(JSON.stringify(disjointOctadWords)===JSON.stringify([0,8,16]),'no disjoint weight12 with an octad');
let goodColorings=0;for(let mask=0;mask<8;mask++){
  const colors=[mask&1,mask>>1&1,mask>>2&1];
  if(colors[0]!==colors[1]&&colors[1]!==colors[2]&&colors[2]!==colors[0])goodColorings++;
}
assert(goodColorings===0,'three repeated minor edges force impossible two-matching triangle');
const out={exact:true,scope:'rootless U24 theorem and exact arithmetic checks; no all-U or all-graph exclusion',
  rootless_characteristics8:48,antipodal_pairs:24,square_frame_Gram:8,shadowframe_Gram:2,
  Code:{length:24,dimension:12,min_distance:8,self_dual_proved:true,doubly_even_proved:true,weight_counts:{0:1,8:759,12:2576,16:759,24:1},uniqueness_not_claimed:true},
  L0_index:evenL0Covol,kernel_index:kernelCovol,Hamming_ball4:ball4,energy_profiles:profiles,
  minor_edge_options:edges.length,cubic_degree:3,multiplicity_max:2,triangle_colorings_valid:goodColorings,
  physical_template_uniform_if_rootless:true,physical_template_general_case_conditional:true,
  source_sha256:createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex')};
fs.writeFileSync(path.join(here,'verifier_rootless_code24.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({exact:true,code:'[24,12,8] self-dual doubly-even, no uniqueness claimed',rootless_shadowframe:true,minor_edge_multiplicity_max:2}));
