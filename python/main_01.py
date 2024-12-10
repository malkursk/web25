def F(n):
    if n>1:
        print(n)
        F(n-3)
        F(n-2)
F(13)


















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


# j=input()
# jewels = set(list(j))

# s=input()
# stones = list(s)

# count = 0
# for stone in stones:
#     if stone in jewels:
#         count+=1

# print(count)


# def main():
#     nums = [1,2,3,4,5,6,7]
#     k = 3
    
#     r=[]
#     for i in range(len(nums)):
#         r.append(nums[(i-k)%len(nums)])
    
#     for i in range(len(nums)):
#         nums[i]=r[i]
    
#     return r



# print(main())