# from fractions import Fraction

# def fuel():  
#         try:
#             inp = input("please input the fraction ")
            
#             for char in inp:
#                     if char.isdigit() == False:
#                         index = inp.index(char)
#             a = Fraction(int(inp[0:index]), int(inp[index+1:]))

#             if float(a) <=0.01:
#                 print("E")
           
#             elif float(a)>=.99:
#                 print("F")
                
#             else:
#                 print(float(a))
         
#         except:
#             print("please recheck your input")

# fuel()


# def taqueria():
#     mydict ={
#     "Baja Taco": 4.00,
#     "Burrito": 7.50,
#     "Bowl": 8.50,
#     "Nachos": 11.00,
#     "Quesadilla": 8.50,
#     "Super Burrito": 8.50,
#     "Super Quesadilla": 9.50,
#     "Taco": 3.00,
#     "Tortilla Salad": 8.00
#     }
#     inp = "A"
#     Total_Cost = 0
#     while inp != "D":
#         inp = input("input food item or press control D to end ").casefold()
#         for k, v in mydict.items():
#             if inp == k.casefold():
#                 Total_Cost += v
#                 print("$", Total_Cost)
        

# taqueria()
            
# def Grocery():
#     shopping_list=[]
#     inp = "A"
#     while inp != "D":
#         inp = input("input food item or press control D to end ")
#         if inp == "D":
#             break;
#         else:
#             shopping_list.append(inp.upper())
    
#     shopping_list.sort
#     res ={}
#     for i in shopping_list:
#         res[i] = shopping_list.count(i)

#     for key, value in sorted(res.items()):
#         print("{} : {}".format(value, key))
    

# Grocery()


# def Outdated();
# moved on to harder problem 




