# for y in range(7):
#     for i in range(5):
#         if((i==0 or i==4)and y!=0) or (y==0 or y == 3) and (i > 0 and i<4):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()



# for i in range(1 , 101) :
#     if i%3==0 and i%5==0 :
#         continue
#     print(i)
# print("bye")
# for i in range(1 , 101) :
#     if i%3==0 or i%5==0 :
#         print(i)
# print("bye")
# for y in range(4):
#     for i in range(4):
#         print("*" ,end="")
#     print()



# for i in range(4):
#     for j in range(4 - i):
#         print("*" ,end="")
#     print()
# for i in range(4):
#     for j in range(4 - i):
#         print(j+1 ,end="")
#     print()

# a = ["shayan" , "Taha" , "12.5"]
# print(len(a[1 : -1]))

# a = "shayanabchabhcbauasuakjsa"
# for i in a:
#     print(i,a.index(i))

# for i in range(4):
#     for j in range(i + 1):
#         print("*",end="")
#     print()
#
# for i in range(1,5):
#     for j in range(i):
#         print("*" , end="")
#     print()

# for i in range(5):
#     for j in range(i + 1):
#         print("*", end="")
#     print()

# a = "asdfghjklmnbvcxz"
# for i in range(len(a)):
#     print(i+1 , a[i])

# for i in range(5 + 1):
#     for j in range(5-i):
#         print("*" , end="")
#     print()

# msg = 5
# for i in range(msg ,0,-1):
#     for j in range(i):
#         print("*", end="")
#     print()

# msg = 5
# for i in range(msg):
#     for j in range(1,i):
#         print("*", end="")
#     print()

# for i in range(1,6) :
#     for j in range(i):
#         print(j+1 , end="")
#     print()

# for i in range(6) :
#     for j in range(i,1):
#         print(j , end="")
#     print()

# for i in range(5):
#     for j in range(i ,-1,-1):
#         print(j+1 ,end="")
#     print()

# for i in range(1,6):
#     for j in range(i):
#         print(i,end="")
#     print()

# for i in range(5):
#     for j in range(i+1):
#         print(5-j,end="")
#     print()

# for i in range(4):
#     for j in range(4-i-1):
#         print(" " , end=" ")
#     for j in range(i+1):
#         print("*" , end=" ")
#     print()

# size = 5
# for i in range(size):
#     for j in range(1, size - i):
#         print(" ", end="")
#     for k in range(2*i-1):
#         print("*", end="")
#     print()
# for i in range(3 ,0 ,-1):
#     for j in range(1, size - i):
#         print(" ", end="")
#     for k in range(2*i-1):
#         print("*", end="")
#     print()

# hill program
# size = 5
# for i in range(1,size):
#     for k in range(size - i - 1):
#         print(" " ,end="")
#     for j in range(i):
#         print("*" , end="")
#     print()

# size = 5
# for i in range(1,size):
#     for k in range(size - i - 1):
#         print(" ",end="")
#     for j in range(i):
#         print("*" , end=" ")
#     print()


# for i in range(3, 0, -1):
#     for j in range(i,0 ,-1):
#         print(j, end="")
#     print()



# Diamond Program
# size = 6
# for i in range(1,size):
#     for k in range(size - i - 1):
#         print(" ",end="")
#     for j in range(i):
#         print("*" , end=" ")
#     print()
# for i in range(4, 0, -1):
#     for m in range(1,size-i):
#         print(" " ,end="")
#     for j in range(i):
#         print("*", end=" ")
#     print()
size  = 6
for i in range(5,0,-1):
    for j in range(1,size-i):
        print(" " ,end="")
    for k in range(i):
        print("*",end="")
    print()










