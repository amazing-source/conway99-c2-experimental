import itertools,time,json
from sage.all import *
L=list(range(12))
pi=[a^1 for a in L]
tau=[5,2,1,4,3,0,11,8,7,10,9,6]
mu=pi[:]
values=[1,2,4,1,2,4,3,5,6,3,5,6]
eps=[(a%2)^int(values[a] not in (1,2,4)) for a in L]
li={(values[a],eps[a]):a for a in L}
H=[[li[(lam*values[a]%7,eps[a])] for a in L] for lam in range(1,7)]
assert all(h[pi[a]]==pi[h[a]] and h[tau[a]]==tau[h[a]] for h in H for a in L)
def act(p,e):return tuple(sorted(p[a] for a in e))
E=[e for e in itertools.combinations(L,2) if mu[e[0]]!=e[1]]
K2=[[2-int(a==b)-int(pi[a]==b)-int(mu[a]==b)-int(tau[pi[a]]==b) for b in L] for a in L]
K3=[[2-int(pi[a]==b)-int(tau[a]==b)-int(tau[mu[a]]==b)-int(mu[tau[a]]==b) for b in L] for a in L]
O=[];seen=set()
for e in E:
 if e in seen:continue
 orb=sorted(set(act(h,e) for h in H));seen.update(orb);O.append(orb)
oi={e:i for i,orb in enumerate(O) for e in orb}
seen=set();Groups=[]
for i,orb in enumerate(O):
 if i in seen:continue
 j=oi[act(pi,orb[0])]; seen|={i,j}; Groups.append(sorted({i,j}))
Maps=[]
for orb in O:
 cand=[];z=orb[0]
 for k,out in enumerate(O):
  if len(orb)!=len(out):continue
  for e in out:
   m={};ok=True
   for h in H:
    zz,ee=act(h,z),act(h,e)
    if zz in m and m[zz]!=ee:ok=False;break
    m[zz]=ee
   if ok and len(set(m.values()))==len(orb):cand.append((k,m))
 Maps.append(cand)
dom=[]
for grp in Groups:
 dc=[]
 combos=itertools.product(*(Maps[i] for i in grp))
 for cm in combos:
  outs=tuple(k for k,m in cm)
  if len(set(outs))<len(outs):continue
  mp={z:e for k,m in cm for z,e in m.items()}; c2={};c3={}
  for z,e in mp.items():
   for a in z:
    for b in e:c2[a,b]=c2.get((a,b),0)+1
   f=mp[act(pi,z)]
   for a in e:
    for b in f:c3[a,b]=c3.get((a,b),0)+1
  if any(v>K2[a][b] for (a,b),v in c2.items()) or any(v>K3[a][b] for (a,b),v in c3.items()):continue
  if any((sum(values[a] for a in mp[z])-sum(values[a] for a in mp[act(pi,z)])+2*(sum(values[a] for a in z)-sum(values[a] for a in act(pi,z))))%7 for z in mp):continue
  dc.append((sum(1<<k for k in outs),c2,c3,mp))
 dom.append(dc)
print('RHO_F7_SETUP',json.dumps({'orbit_sizes':[len(o) for o in O],'groups':Groups,'domains':[len(d) for d in dom]}),flush=True)
nodes=0;start=time.time();sol=None;stopped=False
cur2=[[0]*12 for _ in L];cur3=[[0]*12 for _ in L]
def fits(c,used):
 mask,d2,d3,mp=c
 return not mask&used and all(cur2[a][b]+v<=K2[a][b] for (a,b),v in d2.items()) and all(cur3[a][b]+v<=K3[a][b] for (a,b),v in d3.items())
def dfs(rem,used,chosen):
 global nodes,sol,stopped
 nodes+=1
 if time.time()-start>8:stopped=True;return False
 if not rem:sol=chosen[:];return True
 ds=[]
 for i in rem:
  cs=[c for c in dom[i] if fits(c,used)]
  if not cs:return False
  ds.append((len(cs),i,cs))
 _,i,cs=min(ds,key=lambda t:t[0]);rr=[j for j in rem if j!=i]
 for c in cs:
  mask,d2,d3,mp=c
  for (a,b),v in d2.items():cur2[a][b]+=v
  for (a,b),v in d3.items():cur3[a][b]+=v
  if dfs(rr,used|mask,chosen+[c]):return True
  for (a,b),v in d2.items():cur2[a][b]-=v
  for (a,b),v in d3.items():cur3[a][b]-=v
  if stopped:return False
 return False
dfs(list(range(len(Groups))),0,[])
ans={'nodes':nodes,'seconds':time.time()-start,'status':'found' if sol else 'timeout' if stopped else 'exhausted'}
if sol:ans['phi']=[[list(z),list(e)] for c in sol for z,e in c[3].items()]
print('RHO_F7_RESULT',json.dumps(ans),flush=True)
