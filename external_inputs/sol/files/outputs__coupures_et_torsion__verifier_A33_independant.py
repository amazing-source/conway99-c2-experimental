import json
with open("certificats_A33.json",encoding="utf-8") as fp:
    DATA=json.load(fp)
PHI=DATA["phi_reps"]
CASES=DATA["cases"]
from itertools import combinations,permutations,product
import json
L=range(12);sig=[i^1 for i in L];tau=[5,2,1,4,3,0,11,8,7,10,9,6]
E=list(combinations(L,2));E=[e for e in E if sig[e[0]]!=e[1]]
idx={e:j for j,e in enumerate(E)}
flip=lambda e:tuple(sorted(sig[a] for a in e))
Z=[e for e in E if e<flip(e)]
k2=[[2-int(a==b)-2*int(b==sig[a])-int(b==tau[sig[a]]) for b in L] for a in L]
k3=[[2-int(b==sig[a])-int(b==tau[a])-int(b==tau[sig[a]])-int(b==sig[tau[a]]) for b in L] for a in L]
def norm(p):
 t=pow(next(a for a in p if a),-1,7)
 return tuple((t*a)%7 for a in p)
small=[p for p in permutations(range(6)) if all(p[sig[a]]==sig[p[a]] and p[tau[a]]==tau[p[a]] for a in range(6))]
assert len(small)==6
G=[]
for p,q,swap in product(small,small,range(2)):
 G.append(tuple([p[a]+6*swap for a in range(6)]+[q[a]+6*(1-swap) for a in range(6)]))
assert len(set(G))==72
allpoints=set()
for a,b,c,d in product(range(7),repeat=4):
 if not(a or b or c or d):continue
 allpoints.add(norm((a,b,(-a-b)%7,a,b,(-a-b)%7,c,d,(-c-d)%7,c,d,(-c-d)%7)))
assert len(allpoints)==400
covered=set();osizes=[]
for p in PHI:
 orb={norm(tuple(p[g[i]] for i in L)) for g in G}
 assert not covered&orb
 covered|=orb;osizes.append(len(orb))
assert covered==allpoints
print('A33_INDEPENDENT_COVERAGE',json.dumps({'group':len(G),'projective_points':len(allpoints),'orbit_sizes':osizes}),flush=True)

def quad(A,x,y):return sum(x[a]*A[a][b]*y[b] for a in L for b in L)
CHECKS=[]
for case in CASES:
 p0=[(case.get('multiplier',1)*a)%7 for a in PHI[case['index']]];p=[]
 for j in (0,6):
  a=p0[j] if p0[j]<=3 else p0[j]-7;b=p0[j+1] if p0[j+1]<=3 else p0[j+1]-7
  p.extend((a,b,-a-b,a,b,-a-b))
 energy=3*sum(a*a for a in p)//2
 outGram=[[9*int(a==b)+1-int(b==sig[a]) for b in L] for a in L]
 inGram=outGram
 crossGram=[[1-int(a==b)+9*int(b==sig[a]) for b in L] for a in L]
 pd=[p[a]-p[sig[a]] for a in L]
 cross=quad(k2,pd,p)
 total=quad(outGram,p,p)-quad(k3,p,p)+4*(quad(inGram,p,p)-quad(crossGram,p,p))+4*cross
 assert total==49*energy
 cert=case['certificate'];prices=cert['price'];alpha=cert['dual_left'];beta=cert['dual_right'];scale=case['scale']
 assert all(isinstance(v,int) for v in prices+alpha+beta)
 assert len(set(alpha[12:]))==1
 bound=sum(prices[:60])+sum(prices[60+12*a+b]*k2[a][b]+prices[204+12*a+b]*k3[a][b] for a in L for b in L)+sum(alpha)+sum(beta)
 assert bound==cert['bound'] and bound>scale*energy
 checked=0
 for k,z in enumerate(Z):
  sz=flip(z);dz=sum(p[a] for a in z)-sum(p[a] for a in sz)
  for e in E:
   if any(k2[a][b]==0 for a in z for b in e):continue
   for f in E:
    if e==f or any(k2[a][b]==0 for a in sz for b in f):continue
    if any(k3[a][b]==0 for a in e for b in f):continue
    common=[a for a in e if a in f]
    if common and k3[common[0]][common[0]]<2:continue
    charge=sum(p[a] for a in e)-sum(p[a] for a in f)+2*dz
    if charge%7:continue
    val=prices[idx[e]]+prices[idx[f]]
    val+=sum(prices[60+12*a+b] for a in z for b in e)+sum(prices[60+12*a+b] for a in sz for b in f)
    val+=sum(prices[204+12*a+b] for a in e for b in f)+sum(prices[204+12*a+b] for a in f for b in e)
    val+=alpha[common[0]] if common else alpha[12]
    val+=beta[k]
    assert scale*(charge//7)**2>=val,(case['index'],k,z,e,f)
    checked+=1
 ans={'index':case['index'],'energy':energy,'bound_scaled':bound,'scale':scale,'columns_checked':checked,'valid':True}
 CHECKS.append(ans);print('A33_INDEPENDENT_CERT',json.dumps(ans),flush=True)

last=PHI[16]
survive={norm(tuple(last[g[i]] for i in L)) for g in G}
lines=set()
for p,q in combinations(sorted(survive),2):
 line=frozenset(norm(tuple((a*p[i]+b*q[i])%7 for i in L)) for a,b in product(range(7),repeat=2) if a or b)
 assert len(line)==8
 lines.add(line)
full=[line for line in lines if line<=survive]
print('A33_SURVIVOR_LINES',json.dumps({'points':len(survive),'projective_lines_through_pairs':len(lines),'lines_contained':len(full),'maximum_intersection':max(len(line&survive) for line in lines)}),flush=True)
phi=[1,1,-2,1,1,-2]*2
weights={sum(phi[a] for a in e)%7 for e in E}
differences={(a-b)%7 for a,b in product(weights,repeat=2)}
z=(2,5);sz=flip(z);need=(-2*(sum(phi[a] for a in z)-sum(phi[a] for a in sz)))%7
assert need not in differences
print('A33_HUMAN9',json.dumps({'edge_weights_mod7':sorted(weights),'differences_mod7':sorted(differences),'required_difference':need,'impossible':True}),flush=True)
