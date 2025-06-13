# age = 20
# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are a child")

# mark = int(input("Enter Your Mark:" ))

# if mark <= 100 and mark >= 90:
#     print("A+")
# elif mark <= 89 and mark >= 80:
#     print("A")
# elif mark <= 79 and mark >= 70:
#     print("A-")
# elif mark <= 69 and mark >= 60:
#     print("B+")
# elif mark <= 59 and mark >= 50:
#     print("B")
# elif mark <= 49 and mark >= 40:
#     print("C")
# elif mark <= 39 and mark >= 33:
#     print("D")
# else:
#     print("Fail")

# if age >= 18:
#     if has_permission == True:
#         print("You can enter the club")
#     else:
#         print("You need permission to enter the club")
# else:
#     print("You are not allowed to enter the club")


# age = int(input("Enter your age: "))
# has_permission = bool(input("Do you have permission:"))

# if age >= 18:
#     if has_permission == True:
#         print("You can enter the club")
#     else:
#         print("You need permission to enter the club")
# else:
#     print("You are not allowed to enter the club")


age = int(input("Enter your age: "))

if age >= 18:
    has_permission = bool(int(input("Do you have permission? (1 for Yes, 0 for No): ")))
    if has_permission:
        print("You can enter the club")
    else:
        print("You need permission to enter the club")
else:
    print("You are not allowed to enter the club")



