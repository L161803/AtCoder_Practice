tmp = input()

N = int(tmp)
array = [int(x) for x in tmp]

if N%sum(array)==0:
    print("Yes")
else:
    print("No")
