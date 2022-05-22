

#doesn't work
# def camel():
#       inp = input("please input variable name in camerl case ")
#       for i in inp:
#           if i.isupper():
            
#               index = inp.find(i)
#               A = inp[:index] + "_" + inp[index-1+1:]
#               A = A.lower()
#               print(A)
#               break;



# def camel():
#     inp = input("please input variable name in camerl case ")
#     inp = [char for char in inp]
   
#     print(inp)
#     A = []
#     for i in inp:
#             if i.isupper():
#              A.append('_')
#              A.append(i.lower())
#             else:
#               A.append(i)        
              
#     print(''.join(A))
           

# camel()


# def coke2():
#     amount = 0 
#     while amount < 50:
#       inp = input("insert ")
#       print(inp)
#       if inp == "5" or inp == "10" or inp == "25":
#         amount +=  int(inp)
#         print("amount", amount)
#       if amount>=50:
#           change = amount-50
#           print("you are owed " + str(change) + " cents change")

# coke2()


# does't work 
# def vowels():
#     inp = input("please input the text ").upper()
#     inp = [char for char in inp]
   
#     print(inp)
#     A = []
#     B= ["A", "E", "I", "O", "U"]

   
#     for i in inp:
#         for j in B:

#           if i != j:
#               print(i)
#               A.append(i)
   
              
#     print(''.join(A))

# #vowels()

# def vowels1():
#      c = input("please input the text ").upper()
#      vowels= ["A", "E", "I", "O", "U"]
#      print(''.join([l for l in c if l not in vowels]));

# vowels1()




# cheated on this one, anwer on you tube 
# def is_Plate_Valid():
#     c = input("please input your number plate request ").upper()
#     if 2 <= len(c) and  6>= len(c) and c[0].isalpha() and c[1].isalpha and c.isalnum():
#         for char in c:
#             if char.isdigit():
#                 index = c.index(char)
#                 if c[index:].isdigit() and char != 0:
#                     print("Valid")
#                 else:
#                     print("inalid")
#     else: 
#         print("invalid")



# is_Plate_Valid()


def nutrition():
    mydict = {"apples": 130, "Avocado California": 50, "Banana": 110, "Cantaloupe" : 50, "Grapefruit" : 60 }
    c = input("please input your number plate request ").casefold()
    for k, v in mydict.items():
        if c == k.casefold():
            print(v)


nutrition()