def main(t):
    N,K,V = map(int,input().split())
    A = list(map(int,input().split()))
    extra = ((N+K) * V) - sum(A)
    if extra>0 and extra%K==0:
        print(int(extra/K))
    else:
        print(-1)
    if t>1:
        main(t-1)
        
main(int(input()))