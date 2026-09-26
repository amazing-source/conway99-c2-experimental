import itertools,json

def penalty(t):return (t-1)*(t-2)//2 if t else 0
assert all(t<=2+penalty(t) for t in range(1001))
assert all(1-t+t*(t-1)//2==penalty(t) for t in range(1,1001))
PROFILES=[]
for n3 in range(3):
 counts=[2-n3,20+3*n3,10-3*n3,n3]
 assert sum(counts)==32 and sum(t*counts[t] for t in range(4))==40
 assert sum(t*(t-1)//2*counts[t] for t in range(4))==10
 possible=0;equal=0
 for s,t in itertools.product(range(4),repeat=2):
  left=counts[:];left[s]-=1;left[t]-=1
  if min(left)<0:continue
  possible+=1
  sums=set()
  for c0 in range(min(left[0],10)+1):
   for c2 in range(min(left[2],10-c0)+1):
    for c3 in range(min(left[3],10-c0-c2)+1):
     c1=10-c0-c2-c3
     if c1<=left[1]:sums.add(c1+2*c2+3*c3)
  equal+=int(s+t in sums)
 assert equal==0
 PROFILES.append({'n0_n1_n2_n3':counts,'unused_pair_choices':possible,'balanced_cut_choices':equal})
print('NORM10_CUT_INDEPENDENT',json.dumps(PROFILES),flush=True)
SIX=[]
for n0 in range(4):
 n3=3-n0;n2=11-3*n3;n1=32-n0-n2-n3
 if n0==0:
  assert n2+n3>4
 else:
  SIX.append([n0,n1,n2,n3])
  for c in [2]:
   assert 11-n3-(6-c+n3)>2*n0
print('NORM10_SIX_PROFILES',json.dumps({'profiles':SIX,'small_pair_selected_max':1}),flush=True)
# Control of the general global double-count on H(2,3), with an actual flat odd eigenfunction.
V=list(itertools.product(range(3),repeat=2));N={v:{w for w in V if sum(v[i]==w[i] for i in range(2))==1} for v in V}
P={(0,1),(1,0),(2,2)};Q={tuple((-a)%3 for a in p) for p in P}
f={v:int(v in P)-int(v in Q) for v in V}
assert all(sum(f[w] for w in N[v])==-2*f[v] for v in V)
assert all(not N[v]&P for v in P) and all(not N[v]&Q for v in Q)
ts=[len(N[v]&P) for v in V if not f[v]]
assert all(len(N[v]&P)==len(N[v]&Q) for v in V if not f[v])
assert sum(ts)==(4-2)*3 and sum(t*(t-1)//2 for t in ts)==3*(3-1)-3*1
print('H23_GLOBAL_CONTROL',json.dumps({'outside_t':ts,'sum':sum(ts),'pair_sum':sum(t*(t-1)//2 for t in ts),'root_only_hypothesis':False}),flush=True)

import json
from itertools import product,combinations
D5=[(1,0,0,0,0),(2,0,0,0,0),(0,1,0,0,0),(0,2,0,0,0),(0,0,1,0,0),(0,0,2,0,0),(0,0,0,1,0),(0,0,0,2,0),(0,0,0,0,1),(0,0,0,0,2),(1,0,2,1,2),(2,0,1,2,1),(2,1,1,1,2),(1,2,2,2,1),(2,2,2,0,2),(1,1,1,0,1),(2,2,0,1,1),(1,1,0,2,2),(1,2,1,1,0),(2,1,2,2,0),(0,1,2,1,1),(0,2,1,2,2)]
for dimension,directions in [(2,[(1,0),(2,0),(0,1),(0,2)]),(5,D5)]:
    V=list(product(range(3),repeat=dimension));DD=set(directions)
    add=lambda a,b:tuple((x+y)%3 for x,y in zip(a,b))
    neg=lambda a:tuple((-x)%3 for x in a)
    adj=lambda a,b:add(a,neg(b)) in DD
    zero=(0,)*dimension;c=directions[0];nc=neg(c)
    labels=[a for a in directions if a not in (c,nc)];n=len(labels)
    sigma=[labels.index(neg(a)) for a in labels]
    U=[add(c,a) for a in labels]
    mu=[];tau=[]
    for b in range(n):
        mm=[d for d in range(n) if adj(U[b],U[d])]
        tt=[d for d in range(n) if adj(U[b],neg(U[d]))]
        assert len(mm)==len(tt)==1
        mu.append(mm[0]);tau.append(tt[0])
    far=[a for a in V if a not in (zero,c,nc) and all(not adj(a,t) for t in (zero,c,nc))]
    F={add(labels[a],labels[b]):(a,b) for a,b in combinations(range(n),2) if b!=sigma[a]}
    assert set(F)==set(far) and len(F)==n*(n-2)//2
    Phi={z:tuple(b for b in range(n) if adj(z,U[b])) for z in far}
    assert all(len(e)==2 for e in Phi.values())
    target={e for e in combinations(range(n),2) if e[1]!=mu[e[0]]}
    assert len(set(Phi.values()))==len(Phi) and set(Phi.values())==target
    for a in range(n):
        for b in range(n):
            v=sum(a in F[z] and b in Phi[z] for z in far)
            rhs=2-(a==b)-(b==sigma[a])-(b==mu[a])-(b==tau[sigma[a]])
            assert v==rhs
    for b in range(n):
        for d in range(n):
            v=sum(b in Phi[z] and d in Phi[neg(z)] for z in far)
            rhs=2-(d==sigma[b])-(d==tau[mu[b]])-(d==mu[tau[b]])-(d==tau[b])
            assert v==rhs
    print('COMPACT_CONTROL',json.dumps({'m':len(directions)//2,'vertices':len(V),'labels':n,'far':len(far),'bijection':True,'K2':True,'K3':True,'free':all(mu[i]!=tau[i] for i in range(n))}),flush=True)
