import json,itertools,time

def rank_mod(A,p):
 A=[[int(x)%p for x in row] for row in A];r=0
 if not A:return 0
 for c in range(len(A[0])):
  piv=next((i for i in range(r,len(A)) if A[i][c]),None)
  if piv is None:continue
  A[r],A[piv]=A[piv],A[r];iv=pow(A[r][c],-1,p);A[r]=[(x*iv)%p for x in A[r]]
  for i in range(r+1,len(A)):
   if A[i][c]:
    q=A[i][c];A[i]=[(a-q*b)%p for a,b in zip(A[i],A[r])]
  r+=1
  if r==len(A):break
 return r

def sym_disc(A,p):
 A=[[int(x)%p for x in row] for row in A];r=0;disc=1;pivots=[]
 while A:
  n=len(A);i=next((i for i in range(n) if A[i][i]),None)
  if i is not None:
   order=[i]+[j for j in range(n) if j!=i];B=[[A[a][b] for b in order] for a in order];v=B[0][0];iv=pow(v,-1,p)
   disc=disc*v%p;r+=1;pivots.append([v]);A=[[(B[a][b]-B[a][0]*B[0][b]*iv)%p for b in range(1,n)] for a in range(1,n)]
  else:
   pair=next(((a,b) for a in range(n) for b in range(a+1,n) if A[a][b]),None)
   if pair is None:break
   a,b=pair;order=[a,b]+[j for j in range(n) if j not in pair];B=[[A[x][y] for y in order] for x in order];v=B[0][1];iv=pow(v,-1,p)
   disc=disc*(-v*v)%p;r+=2;pivots.append([0,v,0]);A=[[(B[x][y]-(B[x][0]*B[1][y]+B[x][1]*B[0][y])*iv)%p for y in range(2,n)] for x in range(2,n)]
 return r,disc,pivots

def bareiss(A):
 A=[row[:] for row in A];sign=1;prev=1;n=len(A)
 for k in range(n-1):
  if A[k][k]==0:
   i=next((i for i in range(k+1,n) if A[i][k]),None)
   if i is None:return 0
   A[k],A[i]=A[i],A[k];sign=-sign
  v=A[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    num=A[i][j]*v-A[i][k]*A[k][j];assert num%prev==0;A[i][j]=num//prev
  for i in range(k+1,n):A[i][k]=0
  prev=v
 return sign*A[-1][-1]

sig=[i^1 for i in range(12)];tau=[5,2,1,4,3,0,11,8,7,10,9,6]
C=[[1 if c==0 else 1 if a==2*(c-1) else -1 if a==2*(c-1)+1 else 0 for a in range(12)] for c in range(7)]
H=[[0]*19 for _ in range(19)]
for c in range(7):
 H[c][c]=4
 for a in range(12):H[c][7+a]=H[7+a][c]=-C[c][a]
for a in range(12):
 for b in range(12):H[7+a][7+b]=3*int(a==b)-int(b==sig[a])+int(b==tau[a])
r,disc,piv=sym_disc(H,7);assert r==14 and disc in (1,2,4)
J=[0,1,2,3,6,7,8];Q=[[int(a==b)+int(b==sig[a])+int(b==tau[a])-2 for b in J] for a in J];qd=bareiss(Q)
I=list(range(7))+[7+a for a in J];hd=bareiss([[H[a][b] for b in I] for a in I])
assert hd%7==1 and qd%7==2 and hd%7==(4**7*qd)%7
print('A33_SIGN_INDEPENDENT',json.dumps({'rank':r,'reduced_discriminant':disc,'pivots':piv,'minor_H_integer':hd,'minor_Q_integer':qd,'minor_H_mod7':hd%7,'minor_Q_mod7':qd%7}),flush=True)
assert (disc*(-1)**3)%7 not in (1,2,4)
print('A33_WITT_CONFLICT',json.dumps({'ball_rank':14,'cross_radical_rank':3,'residual_rank':0,'full_rank':20,'predicted_full_discriminant_character':-1,'required_hyperbolic_character':1,'contradiction':True}),flush=True)

def relative_witt(A,k,p):
 A=[[int(x)%p for x in row] for row in A];r=0;db=1;h=0
 def take(A,pair):
  n=len(A);order=list(pair)+[i for i in range(n) if i not in pair]
  return [[A[i][j] for j in order] for i in order]
 while True:
  i=next((i for i in range(k) if A[i][i]),None)
  if i is not None:
   B=take(A,(i,));v=B[0][0];iv=pow(v,-1,p);db=db*v%p;r+=1;k-=1
   A=[[(B[i][j]-B[i][0]*B[0][j]*iv)%p for j in range(1,len(B))] for i in range(1,len(B))];continue
  pair=next(((i,j) for i in range(k) for j in range(i+1,k) if A[i][j]),None)
  if pair is None:break
  B=take(A,pair);v=B[0][1];iv=pow(v,-1,p);db=db*(-v*v)%p;r+=2;k-=2
  A=[[(B[i][j]-(B[i][0]*B[1][j]+B[i][1]*B[0][j])*iv)%p for j in range(2,len(B))] for i in range(2,len(B))]
 while True:
  pair=next(((i,j) for i in range(k) for j in range(k,len(A)) if A[i][j]),None)
  if pair is None:break
  B=take(A,pair);v=B[0][1];d=B[1][1];iv=pow(v,-1,p);ivv=iv*iv%p;h+=1;k-=1
  A=[[(B[i][j]+d*ivv*B[i][0]*B[0][j]-iv*(B[i][0]*B[1][j]+B[i][1]*B[0][j]))%p for j in range(2,len(B))] for i in range(2,len(B))]
 assert all(A[i][j]==0 for i in range(k) for j in range(len(A)))
 F=[row[k:] for row in A[k:]];rf,df,_=sym_disc(F,p)
 return r,db,h,rf,df

D5=[(1,0,0,0,0),(2,0,0,0,0),(0,1,0,0,0),(0,2,0,0,0),(0,0,1,0,0),(0,0,2,0,0),(0,0,0,1,0),(0,0,0,2,0),(0,0,0,0,1),(0,0,0,0,2),(1,0,2,1,2),(2,0,1,2,1),(2,1,1,1,2),(1,2,2,2,1),(2,2,2,0,2),(1,1,1,0,1),(2,2,0,1,1),(1,1,0,2,2),(1,2,1,1,0),(2,1,2,2,0),(0,1,2,1,1),(0,2,1,2,2)]
for dimension,D,theta in [(2,[(1,0),(2,0),(0,1),(0,2)],1),(5,D5,4)]:
 DD=set(D);neg=lambda a:tuple((-x)%3 for x in a);add=lambda a,b:tuple((x+y)%3 for x,y in zip(a,b));adj=lambda a,b:add(a,neg(b)) in DD
 V=list(itertools.product(range(3),repeat=dimension));zero=(0,)*dimension;c=D[0];nc=neg(c);labels=[a for a in D if a not in (c,nc)];star=[add(c,a) for a in labels]
 blocks=[]
 for a in D:
  if a not in blocks and neg(a) not in blocks:blocks.append(a)
 reps=blocks+star
 assert len(set(reps))==len(reps) and not any(neg(a) in reps for a in reps)
 seen=set(reps)|{neg(a) for a in reps}|{zero}
 for a in V:
  if a not in seen:reps.append(a);seen.update((a,neg(a)))
 S=[[int(adj(a,b))-int(adj(a,neg(b))) for b in reps] for a in reps]
 N=[[S[i][j]-theta*int(i==j) for j in range(len(reps))] for i in range(len(reps))]
 p=3;count=len(blocks)+len(star);idx=list(range(count));A=[[N[i][j] for j in idx] for i in idx]
 g,dg,_=sym_disc(N,p);r,db,_=sym_disc(A,p);d=rank_mod([[row[j] for j in idx] for row in N],p);h=d-r;rho=g-r-2*h
 assert rho>=0 and g==rank_mod(N,p) and r==rank_mod(A,p)
 if rho==0:assert pow(dg*pow(db,-1,p)*pow(-1,h,p)%p,(p-1)//2,p)==1
 rr,ddb,hh,rf,df=relative_witt(N,count,p)
 assert (rr,hh,rf)==(r,h,rho)
 assert pow(dg*pow((ddb*pow(-1,h,p)*df)%p,-1,p)%p,(p-1)//2,p)==1
 ans={'residual_disc':df,'witt_relation_verified':True,'m':len(D)//2,'vertices':len(V),'odd_coordinates':len(reps),'p':p,'ball_rank':r,'full_rank':g,'image_ball_dimension':d,'cross_rank':h,'residual_rank':rho,'disc_ball':db,'disc_full':dg,'no_false_exclusion':True}
 print('WITT_POSITIVE_CONTROL',json.dumps(ans),flush=True)

PHI_BASIS=[[1,0,-1,1,0,-1]+[0]*6,[0,1,-1,0,1,-1]+[0]*6,[0]*6+[1,0,-1,1,0,-1],[0]*6+[0,1,-1,0,1,-1]]
UNIVERSAL=[3]+[0]*6+[1]*12
KERNEL=[UNIVERSAL]
for phi in PHI_BASIS:
 u=[2*sum(C[c][a]*phi[a] for a in range(12)) for c in range(7)]
 f=u+phi;KERNEL.append(f)
 assert all(sum(H[i][j]*f[j] for j in range(19))%7==0 for i in range(19))
assert all(sum(H[i][j]*UNIVERSAL[j] for j in range(19))==0 for i in range(19))
assert rank_mod(KERNEL,7)==5
E=[e for e in itertools.combinations(range(12),2) if sig[e[0]]!=e[1]]
flip=lambda e:tuple(sorted(sig[a] for a in e));Z=[e for e in E if e<flip(e)]
checks=0
for k,z in enumerate(Z):
 sz=flip(z);ds=[0]*7
 for a in z:ds[1+a//2]+=1 if a%2==0 else -1
 e=E[(7*k)%60];f=E[(13*k+5)%60]
 row=[-d for d in ds]+[-int(a in e)+int(a in f) for a in range(12)]
 assert sum(a*b for a,b in zip(row,UNIVERSAL))==0
 for phi,ker in zip(PHI_BASIS,KERNEL[1:]):
  lhs=sum(a*b for a,b in zip(row,ker))
  rhs=-(sum(phi[a] for a in e)-sum(phi[a] for a in f)+2*(sum(phi[a] for a in z)-sum(phi[a] for a in sz)))
  assert lhs==rhs;checks+=1
print('A33_KERNEL_BRIDGE',json.dumps({'local_kernel_dimension':5,'universal_kernel':True,'torsion_basis':4,'boundary_checks':checks,'balanced_dimension_formula':'dim U = 18-r0'}),flush=True)
