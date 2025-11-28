#各桁の値の和
def digit_sum(x):
    sum_ = 0
    while(x):
        sum_+=x%10
        x//10

    return sum_