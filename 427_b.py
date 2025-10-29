N = int(input())
l = [1]
for i in range(N-1):
    a = l[i]//1000; l[i]-=a*1000
    b = l[i]//100; l[i]-=b*100
    c = l[i]//10; l[i]-=c*10
    d = l[i]%10; 
    l.append(l[i]+a+b+c+d)
    
print(l[i])