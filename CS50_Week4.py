import emoji
import pyfiglet
import inflect
p=inflect.engine()
import random

# def emoji1():
#         inp = input("string to emoji please input string ")
#         print(emoji.emojize(inp, language='alias', variant="emoji_type"))
        

# emoji1()

# unfinihsed as boring 
# def frank():
#     inp = input("please input string ")
#     result = pyfiglet.figlet_format(inp) 
#     print(result)

# frank()


# def adieu():
#       ad = []
      
#       while True:
#         inp = input("please input string ")
#         if inp == "DNC":
#             output = p.join(ad)
#             print("Audieu, audieu, to " + output)
            
        
#         else:
#             ad.append(inp)


# adieu()

# def game():
#         a = random.randint(0, 100)
#         while True:
#             inp = input("guess the int ")
#             if int(inp) < 0:
#                 game()
#             elif (int(inp) < a):
#                 print("too small!")
#             elif (int(inp) > a):
#                 print("too large!")
#             else:
#                 print("just right!")
            
# game()

# Problem Name is Little Professor - U are up to here. 
def main():
    ...


def get_level():
     while True:
        inp = input("guess the int ")
        if int(inp) != 1 or int(inp) != 2 or int(inp) != 3:
            get_level()
        else:
            level = int(inp)
            return level
            


def generate_integer(level):
    i = 0
    while i < 10:
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        x = a + b
        a = str(a)
        b = str(b)
    
        while True:
            inp = input("a" "+" "b")
            if (int(inp) != x):
            

            
if __name__ == "__main__":
    main()