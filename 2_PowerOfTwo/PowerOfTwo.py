n = int(input())

b = True

for i in range(30):
    ans = pow(2,i)

    if(ans==n):
        b=True
        break
    else:
        b=False
        continue

print(b)