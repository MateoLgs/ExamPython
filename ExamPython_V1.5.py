from colorama import init
init()
from colorama import Fore, Back, Style
import os
import random


lettresDansMot=0
victoire= False

listeMots = ["acteur","cigare","banane","bateau","mignon","assaut","billet","utopie","oiseau","souris"]
randomMots= random.randint(0,4)
mot = listeMots[randomMots]
nbEssais=8

z=0


# a = 0;b = 0;c = 0;d = 0;e = 0;f = 0;g = 0;h = 0;i = 0;j = 0;k = 0;l = 0;m = 0;n = 0;o = 0;p = 0;q = 0;r = 0;s = 0;t = 0;u = 0;v = 0;w = 0;x = 0;y = 0;z = 0
  
# for i in mot: 
    # if i == 'a': 
        # a = a + 1  
# for i in mot: 
    # if i == 'b': 
        # b = b + 1 
# for i in mot: 
    # if i == 'c': 
        # c = c + 1 
# for i in mot: 
    # if i == 'd': 
        # d = d + 1 
# for i in mot: 
    # if i == 'e': 
        # e = e + 1 
# for i in mot: 
    # if i == 'f': 
        # f = f + 1 
# for i in mot: 
    # if i == 'g': 
        # g = g + 1 
# for i in mot: 
    # if i == 'h': 
        # h = h + 1 
# for i in mot: 
    # if i == 'i': 
        # i = i + 1 
# for i in mot: 
    # if i == 'j': 
        # j = j + 1 
# for i in mot: 
    # if i == 'k': 
        # k = k + 1 
# for i in mot: 
    # if i == 'l': 
        # l = l + 1 
# for i in mot: 
    # if i == 'm': 
        # m = m + 1
# for i in mot: 
    # if i == 'n': 
        # n = n + 1 
# for i in mot: 
    # if i == 'o': 
        # o = o + 1 
# for i in mot: 
    # if i == 'p': 
        # p = p + 1 
# for i in mot: 
    # if i == 'q': 
        # q = q + 1 
# for i in mot: 
    # if i == 'r': 
        # r = r + 1 
# for i in mot: 
    # if i == 's': 
        # s = s + 1 
# for i in mot: 
    # if i == 't': 
        # t = t + 1 
# for i in mot: 
    # if i == 'u': 
        # u = u + 1 
# for i in mot: 
    # if i == 'v': 
        # v = v + 1 
# for i in mot: 
    # if i == 'w': 
        # w = w + 1 
# for i in mot: 
    # if i == 'x': 
        # x = x + 1 
# for i in mot: 
    # if i == 'y': 
        # y = y + 1 

        
        
# print("A:", a ) 
# print("B:", b )
# print("C:", c )
# print("D:", d )
# print("E:", e )
# print("F:", f )
# print("G:", g )
# print("H:", h )
# print("I:", i )
# print("J:", j )
# print("K:", k )
# print("L:", l )
# print("M:", m )
# print("N:", n )
# print("O:", o )
# print("P:", p )
# print("Q:", q )
# print("R:", r )
# print("S:", s )
# print("T:", t )
# print("U:", u )
# print("V:", v )
# print("W:", w )
# print("X:", x )
# print("Y:", y )
# print("Z:", z )




print("Les lettres deviendront: \n- Rouges si elles sont bien placées,\n- Jaunes si elles sont mal placées,\n- Bleu si elles sont mauvaises.\n\n\n")




while(nbEssais>0 and victoire==False):
    lettresDansMot=0    
    print("Encore", nbEssais,"chances")
    proposition = input("Proposition : ")
   
    if(len(proposition)==6):
        for i in range(len(proposition)):

            
            if(proposition[i] == mot[i]):
                print(Back.RED + proposition[i], end="")
                lettresDansMot=lettresDansMot+1              
                if(lettresDansMot==6):
                    victoire=True 
                                     
            if proposition[i] in mot:
                if(proposition[i] != mot[i]):
                    sauvegarde = proposition[i]

                    print(Back.YELLOW + proposition[i], end="")
                    # if(proposition[i]==proposition[i-5] or proposition[i]==proposition[i-4] or proposition[i]==proposition[i-3] or proposition[i]==proposition[i-2] or proposition[i]==proposition[i-1] or proposition[i]==proposition[i+1] or proposition[i]==proposition[i+2] or proposition[i]==proposition[i+3] or proposition[i]==proposition[i+4] or proposition[i]==proposition[i+5]){
                        # print("test")
                    # } 
                    # for i in mot: 
                        # if i == proposition[i]: 
                            # z = z + 1 
                    
            else:
                print(Back.BLUE + proposition[i], end="")  
                        
            # nbLettre=mot.count(proposition[i])
            # print(z)
        print(Style.RESET_ALL)
       
        
        nbEssais-=1
    
    else : 
        print("---------------------------------------------------------------------------")
        print("\nUn mot a 6 lettre svp\n")   
    
    
   
if(nbEssais==0):
    os.system('cls')
    print("You Lose")
if(victoire==True):
    os.system('cls')
    print("You Win")

  
input()
