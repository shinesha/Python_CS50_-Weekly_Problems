# from fractions import Fraction

# # partial solution but the rest is easy and no time to finish now
# def fuel():  
#         try:
#             inp = input("please input the fraction ")
#             # for i in range(len(inp)):
#             #     if inp[1].isdigit and inp[2].isdigit and inp[3].isdigit:
                

#             for char in inp:
#                     if char.isdigit() == False:
#                         # makes the / symbol the index
#                         index = inp.index(char)
#                         # Fraction must convert to decimal 
#             a = Fraction(int(inp[0:index]), int(inp[index+1:]))

#             if float(a) <=0.01:
#                 print("E")
           
#             elif float(a)>=.99:
#                 print("F")
                
#             else:
#                 print(float(a))
         
        
#         except ValueError:
#             print("please recheck your input")

# fuel()

# The except on works in VS cloud, not on downloaded IDE 

# def Taqueria():
#     menu = {
#     "Baja Taco": 4.00,
#     "Burrito": 7.50,
#     "Bowl": 8.50,
#     "Nachos": 11.00,
#     "Quesadilla": 8.50,
#     "Super Burrito": 8.50,
#     "Super Quesadilla": 9.50,
#     "Taco": 3.00,
#     "Tortilla Salad": 8.00
# }

#     cost = 0
#     # inp = "AA"
#     # while inp != "A1":
#     while True:
#         try: 
#             inp = input("what items do you want to order ")
#             inp = inp[0:1].upper() + inp[1:].lower()
    
#             if inp in menu:
#                 cost += menu.get(inp)
#                 print("$", cost)
                
#         except EOFError:
#             break

# Taqueria()

#A again EOF with input from terminal does not work but code does work if i do
#it a different way. 
# def GroceryList():
#      groceryL =[]
#      while True:
#         try: 
#             inp = input("what items do you want to order ")
#             inp = inp[0:].upper()
#             groceryL.append(inp)
#             groceryL.sort()
#             print(groceryL)
#         except EOFError:
#             # groceryL.sort()
#             # print(groceryL)
#             break

# GroceryList()

# last one, didn't do it as too easy. 
