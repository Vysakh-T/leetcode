T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    P = {}
    O = ""
    for n in range(N):
        t1,t2 = map(int,input().split())
        temp = list(range(t1,t2+1))
        for i in temp:
            P[i] = 1
    M = list(map(int,input().split()))
    
    for m in range(len(M)):
        if P.get(M[m]) != None:
            O += str(M[m]) + " "
            P[M[m]] = None
        else:
            i = 1
            while(True):
                if P.get(M[m]-i) != None and M[m]-i not in M[m+1:]:
                    O += str(M[m]-i) + " "
                    P[M[m]-i] = None
                    break
                elif P.get(M[m]+i) != None and M[m]+i not in M[m+1:]:
                    O+= str(M[m]+i) + " "
                    P[M[m]+1] = None
                    break
                i+=1
    O = O[:len(O)-1]
    print("Case #{x}: {y}".format(x=t+1,y=O))
    
