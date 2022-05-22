from fractions import Fraction

def fuel():  
        try:
            inp = input("please input the fraction ")
            
            for char in inp:
                    if char.isdigit() == False:
                        index = inp.index(char)
            a = Fraction(int(inp[0:index]), int(inp[index+1:]))

            if float(a) <=0.01:
                print("E")
           
            elif float(a)>=.99:
                print("F")
                
            else:
                print(float(a))
         
        
        except:
            print("please recheck your input")

fuel()
