# Python code to find frustrated coders


input()
num_list = input()
num_list = list(map(int,num_list.split(' ')))

num_list.sort()

i = 0



for num in num_list:

    if num > num_list[i] :
        i += 1

num_list = num_list[i:]




print(sum(num_list))

# N=int(input())
# coders = list(map(int, input().split()))
# coders.sort()
# maxdata=max(coders)
# indexdata = []
# j = 0
# i=0
# while len(coders) > 0:
#     if coders[j] != coders[i] and i not in indexdata:
#         coders.pop(j)
#         p = i-1
#         indexdata.append(p)
#         j = 0
#         i-=1
#     else:
#         i+=1
#     if coders[i] == maxdata:
#         coders.pop(j)
#         break
# print(sum(coders))


N = int(input())
coders = list(map(int, input().split()))
coders.sort()
indexdata = []
l = [int(x) for x in coders]

for i in range(0, N - 1):
    for j in range(i, N):
        if coders[i] != coders[j] and (j) not in indexdata:
            l[i] = 0
            indexdata.append(j)
            break
print(sum(l))
