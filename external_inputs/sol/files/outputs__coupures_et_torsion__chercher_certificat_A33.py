import json,time
from itertools import combinations
from collections import Counter
MU=[i^1 for i in range(12)]
TAU=[5,2,1,4,3,0,11,8,7,10,9,6]
PHI=[[0,0,0,0,0,0,0,1,6,0,1,6],[0,0,0,0,0,0,1,1,5,1,1,5],[0,0,0,0,0,0,1,2,4,1,2,4],[0,1,6,0,1,6,0,1,6,0,1,6],[0,1,6,0,1,6,0,2,5,0,2,5],[0,1,6,0,1,6,1,1,5,1,1,5],[0,1,6,0,1,6,1,2,4,1,2,4],[0,1,6,0,1,6,1,3,3,1,3,3],[0,1,6,0,1,6,2,2,3,2,2,3],[1,1,5,1,1,5,1,1,5,1,1,5],[1,1,5,1,1,5,1,2,4,1,2,4],[1,1,5,1,1,5,1,3,3,1,3,3],[1,1,5,1,1,5,2,2,3,2,2,3],[1,1,5,1,1,5,2,6,6,2,6,6],[1,1,5,1,1,5,3,5,6,3,5,6],[1,2,4,1,2,4,1,2,4,1,2,4],[1,2,4,1,2,4,3,5,6,3,5,6]]
L=list(range(12))
EDGES=[e for e in combinations(L,2) if e[0]//2!=e[1]//2]
EIDX={e:i for i,e in enumerate(EDGES)}
SIGE=lambda e:tuple(sorted(i^1 for i in e))
REPS=[e for e in EDGES if e<SIGE(e)]
K2=[[2-(a==b)-(b==(a^1))-(b==MU[a])-(b==TAU[a^1]) for b in L] for a in L]
K3=[[2-(d==(b^1))-(d==TAU[MU[b]])-(d==MU[TAU[b]])-(d==TAU[b]) for d in L] for b in L]
BASE=[]
for z in REPS:
    zz=SIGE(z)
    left=[e for e in EDGES if all(K2[a][b]>0 for a in z for b in e)]
    right=[e for e in EDGES if all(K2[a][b]>0 for a in zz for b in e)]
    v=[]
    for e in left:
        for f in right:
            if e==f:continue
            count=Counter((b,d) for b in e for d in f)
            count.update((b,d) for b in f for d in e)
            if any(n>K3[b][d] for (b,d),n in count.items()):continue
            common=set(e)&set(f)
            assert len(common)<=1
            v.append((e,f,next(iter(common)) if common else -1))
    BASE.append(v)
print('A33_BASE',json.dumps({'domain_min':min(map(len,BASE)),'domain_max':max(map(len,BASE))}),flush=True)

def has_matching(doms):
    match={}
    def augment(u,seen):
        for v in doms[u]:
            if v in seen:continue
            seen.add(v)
            if v not in match or augment(match[v],seen):match[v]=u;return True
        return False
    return sum(augment(u,set()) for u in range(len(doms)))

def assignment_cost(cost):
    n=len(cost);u=[0]*(n+1);v=[0]*(n+1);p=[0]*(n+1);way=[0]*(n+1)
    for i in range(1,n+1):
        p[0]=i;j0=0;mn=[10**9]*(n+1);used=[False]*(n+1)
        while True:
            used[j0]=True;i0=p[j0];delta=10**9;j1=0
            for j in range(1,n+1):
                if used[j]:continue
                cur=cost[i0-1][j-1]-u[i0]-v[j]
                if cur<mn[j]:mn[j]=cur;way[j]=j0
                if mn[j]<delta:delta=mn[j];j1=j
            for j in range(n+1):
                if used[j]:u[p[j]]+=delta;v[j]-=delta
                else:mn[j]-=delta
            j0=j1
            if p[j0]==0:break
        while True:
            j1=way[j0];p[j0]=p[j1];j0=j1
            if j0==0:break
    match=[-1]*n
    for j in range(1,n+1):match[p[j]-1]=j-1
    val=sum(cost[i][match[i]] for i in range(n))
    assert val==sum(u[1:])+sum(v[1:])
    assert all(u[i+1]+v[j+1]<=cost[i][j] for i in range(n) for j in range(n))
    return val,match,u[1:],v[1:]

import numpy as np
SCALE=1000
LAG_RESULTS=[]
import sys
CASE_SPECS=json.loads(sys.argv[1]) if len(sys.argv)>1 else [[6,2]]
for index,multiplier in CASE_SPECS:
    phi0=[(multiplier*a)%7 for a in PHI[index]];phi=[]
    for j in (0,6):
        a=phi0[j] if phi0[j]<=3 else phi0[j]-7
        b=phi0[j+1] if phi0[j+1]<=3 else phi0[j+1]-7
        phi.extend([a,b,-a-b,a,b,-a-b])
    energy=3*sum(x*x for x in phi)//2
    cols=[];weights=[];by=[{} for k in REPS]
    for k,z in enumerate(REPS):
        zz=SIGE(z);dz=sum(phi[a] for a in z)-sum(phi[a] for a in zz)
        for e,f,b in BASE[k]:
            charge=sum(phi[a] for a in e)-sum(phi[a] for a in f)+2*dz
            if charge%7:continue
            row=[0]*348;row[EIDX[e]]=1;row[EIDX[f]]=1
            for a in z:
                for d in e:row[60+12*a+d]+=1
            for a in zz:
                for d in f:row[60+12*a+d]+=1
            for a in e:
                for d in f:row[204+12*a+d]+=1
            for a in f:
                for d in e:row[204+12*a+d]+=1
            by[k].setdefault(b,[]).append(len(cols));cols.append(row);weights.append(SCALE*(charge//7)**2)
    C=np.array(cols,dtype=np.int64);W=np.array(weights,dtype=np.int64)
    target=np.array([1]*60+[K2[a][b] for a in L for b in L]+[K3[a][b] for a in L for b in L],dtype=np.int64)
    price=np.zeros(348,dtype=np.int64);best=-10**20;cert=None;start=time.time()
    for it in range(800):
        vals=W-C@price
        dc=[[10**8]*30 for _ in range(30)];arg={}
        for k,dct in enumerate(by):
            for b,idxs in dct.items():
                j=min(idxs,key=lambda j:int(vals[j]));cost=int(vals[j])
                rows=[b] if b>=0 else range(12,30)
                for row in rows:dc[row][k]=cost;arg[row,k]=j
        val,matching,du,dv=assignment_cost(dc)
        bound=val+int(target@price)
        if bound>best:
            best=bound;cert={'price':[int(x) for x in price],'dual_left':du,'dual_right':dv,'bound':int(bound),'iteration':it}
        if bound>SCALE*energy:break
        chosen=[arg[r,k] for r,k in enumerate(matching)]
        usage=C[chosen].sum(axis=0);grad=target-usage
        norm=int(grad@grad)
        if not norm:break
        step=max(1,int((SCALE*energy-bound)//max(1,norm)))
        price+=step*grad
        if it%10==0 and time.time()-start>28:break
    p=np.array(cert['price'],dtype=np.int64);v=W-C@p
    for k,dct in enumerate(by):
        for b,idxs in dct.items():
            rows=[b] if b>=0 else range(12,30)
            for r in rows:
                assert all(int(v[j])>=cert['dual_left'][r]+cert['dual_right'][k] for j in idxs)
    assert cert['bound']==int(target@p)+sum(cert['dual_left'])+sum(cert['dual_right'])
    ans={'index':index,'multiplier':multiplier,'energy':energy,'bound_scaled':int(best),'scale':SCALE,'excluded':best>SCALE*energy,'iterations':it+1,'seconds':time.time()-start,'certificate':cert}
    LAG_RESULTS.append(ans)
    print('A33_LAG',json.dumps(ans),flush=True)
