#各桁の値の和
def degit_sum(x):
    sum_ = 0
    while(x):
        sum_+=x%10
        x//10

    return sum_