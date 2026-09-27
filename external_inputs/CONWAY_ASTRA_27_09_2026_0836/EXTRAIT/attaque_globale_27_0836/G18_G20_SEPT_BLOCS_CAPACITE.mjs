import crypto from 'node:crypto';
const mod=(x,p)=>(x%p+p)%p;
const weight=x=>{let n=0;for(;x;x&=x-1)n++;return n;};
const hash=x=>crypto.createHash('sha256').update(JSON.stringify(x)).digest('hex');
export function golayWords(){
  const g=[11,9,7,6,5,1,0].reduce((a,j)=>a|(1<<j),0),words=[];
  for(let m=0;m<4096;m++){
    let w=0;for(let j=0;j<12;j++)if(m>>j&1)w^=g<<j;
    if(weight(w)%2)w|=1<<23;words.push(w);
  }
  return words;
}
export function membership(z,code){
  if(z.length!==24||z.some(x=>!Number.isInteger(x)))throw Error('24 integral coordinates required');
  const parity=mod(z[0],2);let word=0;
  if(z.some(x=>mod(x,2)!==parity))return {member:false,reason:'mixed_parity'};
  for(let j=0;j<24;j++)if(mod(z[j]-parity,4)===2)word|=1<<j;
  const sum=z.reduce((a,b)=>a+b,0),inCode=code.has(word);
  return {member:inCode&&mod(sum,8)===0,word,in_code:inCode,sum,sum_mod8:mod(sum,8)};
}
const dot=(a,b)=>a.reduce((s,x,j)=>s+x*b[j],0);
export function prepareShell(B){
  if(B.length!==2||B.some(row=>row.length!==24||row.some(x=>Math.abs(x)!==1&&Math.abs(x)!==3)))
    throw Error('B must contain two 24-coordinate rows with entries +/-1 or +/-3');
  const words=golayWords(),code=new Set(words);
  if(B.some(row=>dot(row,row)!==56||!membership(row,code).member)||dot(B[0],B[1])!==0)
    throw Error('The two B charges must belong to U_Golay, have norm7 and be orthogonal');
  const lines=[];
  for(const word of words){
    const E=Array.from({length:24},(_,j)=>1-2*(word>>j&1));
    if(E[0]===1&&B.every(row=>dot(row,E)===0))lines.push(E);
  }
  return {B:B.map(row=>row.slice()),words,code,lines,
    code_sha256:hash(words),B_sha256:hash(B),shell_sha256:hash(lines),
    complete_shell_reconstructed:true,oriented_shell_size:2*lines.length,line_count:lines.length,
    scope:'Fixed explicit U_Golay and B; complete norm3 shell reconstructed from the code.'};
}
export function blockBins(row,lines){
  const bins={zero:0n,positive:0n,negative:0n};
  for(let i=0;i<lines.length;i++){
    const a=dot(row,lines[i]),bit=1n<<BigInt(i);
    if(a===0)bins.zero|=bit;else if(a===4)bins.positive|=bit;else if(a===-4)bins.negative|=bit;
  }
  return bins;
}
const popcount=x=>{let n=0;for(;x;x&=x-1n)n++;return n;};
export function pairCapacitiesFromBins(bins,lineCount){
  const profiles=[],all=(1n<<BigInt(lineCount))-1n;
  for(let c=0;c<bins.length;c++)for(let d=c+1;d<bins.length;d++){
    let far=all;for(let k=0;k<bins.length;k++)if(k!==c&&k!==d)far&=bins[k].zero;
    const plus=far&((bins[c].positive&bins[d].positive)|(bins[c].negative&bins[d].negative));
    const minus=far&((bins[c].positive&bins[d].negative)|(bins[c].negative&bins[d].positive));
    profiles.push({c,d,plus:plus.toString(16),minus:minus.toString(16),
      plus_count:popcount(plus),minus_count:popcount(minus)});
  }
  return profiles;
}
export function sevenCapacity(M,prepared){
  if(M.length!==7||M.some(row=>row.length!==24||row.some(x=>![0,1,-1].includes(x))))
    throw Error('M must have seven 24-coordinate rows with entries0,+1,-1');
  const context={M:M.map(row=>row.slice()),B:prepared.B,M_sha256:hash(M),
    B_sha256:prepared.B_sha256,code_sha256:prepared.code_sha256,shell_sha256:prepared.shell_sha256,
    complete_shell_reconstructed:prepared.complete_shell_reconstructed,
    assumptions:['Physical seven blocks in the fixed explicit U_Golay orthogonal to B',
      'Odd determinant of the physical N','All42 roots chosen from the complete norm3 shell']};
  const fail=(kind,witness)=>({refuted:true,kind,witness,context,
    scope:'Refutes this simultaneous seven-block selection only; not every envelope, genre or graph.'});
  for(let c=0;c<7;c++){
    if(dot(M[c],M[c])!==8)return fail('block_weight',{c,weight:dot(M[c],M[c])});
    const member=membership(M[c].map(x=>2*x),prepared.code);
    if(!member.member)return fail('block_not_in_lattice',{c,...member});
    if(dot(M[c],prepared.B[0])||dot(M[c],prepared.B[1]))return fail('block_not_orthogonal_B',{c});
    for(let d=0;d<c;d++)if(dot(M[c],M[d]))return fail('blocks_not_orthogonal',{c,d,inner:dot(M[c],M[d])});
  }
  const columnWeights=Array.from({length:24},(_,j)=>M.reduce((s,row)=>s+row[j]**2,0));
  if(columnWeights.filter(x=>x===1).length!==8||columnWeights.filter(x=>x===3).length!==16)
    return fail('column_weight_profile',{columnWeights});
  for(let j=0;j<24;j++)if(4*columnWeights[j]+prepared.B[0][j]**2+prepared.B[1][j]**2!==14)
    return fail('column_weight_B_mismatch',{j,column_weight:columnWeights[j],
      B_squared:prepared.B[0][j]**2+prepared.B[1][j]**2});
  const Z=Array.from({length:24},(_,j)=>M.reduce((s,row)=>s+row[j],0));
  const halfSum=membership(Z,prepared.code);
  if(!halfSum.member)return fail('half_sum_not_in_lattice',{Z,...halfSum});
  const bins=M.map(row=>blockBins(row,prepared.lines));
  const profiles=pairCapacitiesFromBins(bins,prepared.lines.length);
  const empty=profiles.find(p=>p.plus_count===0||p.minus_count===0);
  if(empty)return fail('empty_D7_class',{c:empty.c,d:empty.d,sign:empty.plus_count===0?'same':'opposite'});
  return {refuted:false,kind:'capacity_only',context,half_sum:halfSum,profiles,
    scope:'All42 classes nonempty; mutual Gram, frame, budgets and generation index still required.'};
}
