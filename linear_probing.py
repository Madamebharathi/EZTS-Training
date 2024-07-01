k=[22,10,47,42,56,100,50,92,99,79]
res=[False]*len(k)
for i in k:
    #h_k=i%10
    j=0
    j_key=i%len(k)
    while res[j_key]!=False and j<len(k):
        j_key=((i%10)+j)%len(k)
        j+=1
    res[j_key]=i

print(res)    