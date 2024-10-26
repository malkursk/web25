# a,b=map(int,input().split())
# print(a+b)


# f = open('input.txt')
# s = f.readline()
# print(s)
# a,b=map(int,s.split())
# f.close()

# f = open('output.txt', 'w')
# f.write(str(a+b))
# f.close()


j=input()
jewels = set(list(j))

s=input()
stones = list(s)

count = 0
for stone in stones:
    if stone in jewels:
        count+=1

print(count)



