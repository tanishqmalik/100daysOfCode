n = 121
replica = n
revNum = 0

while replica > 0:
    d = replica%10
    revNum = revNum*10 + d
    replica=replica//10

if(revNum==n):
    print("Yes, Issa palindrome")
else:
    print("Not a palindrome")

# 2nd method
n=1331
if(n<0):
    print("false")
n = str(n)
if(n==n[::-1]):
    print("true")
else:
    print("false")