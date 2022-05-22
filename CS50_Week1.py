# PROBLEM SET 1

# def Deep_Thought(): 
#     x = input("Great Question of Life, the Universe and Everything ")
#     if (x == "42" or x== "forty-two" or x== "forty two" or x== "forty-two".upper() or x== "forty two".upper()):
#         print("Yes")
#     else: print("No")

# Deep_Thought()

# def HomeSavings():
#       x = input("Great Question of Life, the Universe and Everything ")
#       x= x.casefold()
#       if x.startswith("hello"):
#           print("£0")
#       elif x.startswith("h"):
#           print("$20")
#       else: print("$100")

# HomeSavings()

# def FileSavings():
#         x = input("what file extension ")
#         x = x.casefold()
#         if x == ".gif" or x == ".jpg" or x == ".jpeg" or x == ".png" or x == ".pdf" or x==".txt" or x == ".zip":
#             x= x.replace(".", "")
#             print("image/" + x)
#         else: print("application/octet-stream")

# FileSavings()



# only works for single digits
# def Interpreter():
#         inp = input("what file extension ")
## get rid of spaces so you slice 
#         inp.replace(" ", "")
#         x = inp[:1]
#         y = inp[1:2]
#         z = inp[2:]
#         x = int(x)
#         z = int(z)

#         if y == '+':
#             print(x + z)
#         elif y == '-':
#             print(x - z)
   
# Interpreter()

# # works for multiple digits
# def Interpreter1():
#         inp = input("what file extension ")
# # take out the spcaes
#         inp.replace(" ", "")
# # loop to check for operator
#         for i in inp:
#             if i == "+":
#                 A = inp.find('+') 
#                 x = inp[:A]
#                 z = inp[A+1:]
#                 x = int(x)
#                 z = int(z)
#                 print(x + z)

# Interpreter1()

# def convert(time):
# strip out the semi colon in the time
#     time = time.replace(":", "")
#     time = int(time)
#     if time >=700 and time <= 800:
#         print("breaky")
#     elif time >=1200 and time <=1300:
#         print("lunch")
#     elif time >= 1800 and time <= 1900:
#         print("dinner")

# convert("19:00")

            
