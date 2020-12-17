import random as rd

c = int(input("Enter No. of Chance To each player:"))

x1 = input("Enter 1st Player Name:")
x2 = input("Enter 2nd Player Name:")
print("------------------------------------------------")
print("Game Between {0} and {1}".format(x1,x2))
print("------------------------------------------------")
def num(x1,x2):
    chance = 0
    s1 = 0
    s2 = 0
    
    
    while chance<c :
        number = rd.randint(1,10)
        p1 = rd.randint(1,10)
        p2 = rd.randint(1,10)
        
        if number==p1 :
            print("P1 Guess Right..")
            s1 += 1
            chance += 1
            print(number)
               
        elif number==p2 :
            print("P2 Guess Right..")
            s2 += 1
            chance += 1
            print(number)
         
        elif number==p1 and number==p2 :
           print("Both right..")
           s1 += 1
           s2 += 1
           chance += 1
           print(number)
        
        else :
           print("Both Wrong..")
           chance += 1 
           print(number)
        
        if chance == c:
          print("Score Line is : {0} - {1}".format(s1,s2))
          print("Do you want to continue??")
          r = input()
          if r == 'y':
            chance = 0
         
    print("----------------------------------------")
    print("Score Line is : {0}-{1}".format(s1,s2))
    print("----------------------------------------")
    if s1==s2 :
           print("Game Draw.")
    elif s1 > s2 :
           print("{0} win the game.".format(x1))
    else :
           print("{0} win the game.".format(x2))
    
                                

num(x1,x2)

    

                   
        


    
    
        
    