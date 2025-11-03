#ABC081B-Shift only

#NumPy
import numpy as np
N = int(input())
s = np.array(list(map(int,input().split())), dtype=np.int64)
ans=0
while np.all(s%2==0):
    ans+=1
    s = s/2
print(ans) 

#Natural Python version is available on ABC081B_2.py