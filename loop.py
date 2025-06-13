x = 0
# while x <= 5:
#     print(x)
#     x += 1

# for i in range(0,10,2):
#     print(i)

# for i in range(7,-7,-2):
#     print(i)

# while x <= 10:
#     if x == 7:
        
#         continue
#     x += 1
#     print(x)
#     x += 1

# 1 + (1+2) + (1+2+3) + ( 1+2+3+4)

sum = 0
x = 0
for i in range(1,5):
    for j in range(1,1+i):
        sum = sum + j
print(sum)