#想定：丁寧に条件分岐すれば問題なくできそう
#実際；AC

# a, b, c, d = map(int, input().split())
# ans = "No"
# if c-a<0:
#     pass
# elif d-b>=0:
#     pass
# else:
#     ans = "Yes"
# print(ans)

#めっちゃきれいに書ける
A,B,C,D = map(int, input().split())

ans="No"
if C>=A and D<B:
  ans="Yes"

print(ans)
### from gokurakuさん

#次回：条件分の冗長さを無くす