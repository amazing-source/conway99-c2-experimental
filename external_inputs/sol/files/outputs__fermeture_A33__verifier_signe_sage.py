import json
from sage.all import matrix,GF
sig=[a^1 for a in range(12)];tau=[5,2,1,4,3,0,11,8,7,10,9,6]
C=matrix(GF(7),7,12,lambda c,a:1 if c==0 else (1 if a==2*(c-1) else -1 if a==2*(c-1)+1 else 0))
P=matrix(GF(7),19,19,lambda a,b:0)
for c in range(7):P[c,c]=4
for c in range(7):
 for a in range(12):P[c,7+a]=-C[c,a];P[7+a,c]=-C[c,a]
for a in range(12):
 for b in range(12):P[7+a,7+b]=3*int(a==b)-int(b==sig[a])+int(b==tau[a])
I=list(P.pivots());r=P.rank();D=int(P.matrix_from_rows_and_columns(I,I).det())
print('A33_BALL_SIGN',json.dumps({'rank':r,'pivots':I,'det':D,'square':D in (1,2,4),'required_for_hyperbolic_rank20':False}),flush=True)
