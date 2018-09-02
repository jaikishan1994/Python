# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 23:50:10 2018

@author: v-jaimo
"""
import random
import copy
def gen(ch, l):
    g = ""
    for i in range(0,l,1):
        if((i >= 0) & (ch[i] != ' ')):
            g = g + '*'            
        elif(ch[i] == ' '):
            g = g + ' '
    return g

def check(letter,ch,initial):
    l = len(ch)
    c = 0   #correct
    blanks = 0
    for i in range(0,l,1):
        if((ch[i]!=letter) & (initial[i] == '*')):
            initial[i] = '*'
            blanks += 1
            if(c == 0):
                c = 0
        elif((ch[i]!=letter) & (initial[i] != '*')):
            if(c == 0):
                c = 0
        elif((ch[i]==letter)):
            initial[i] = letter
            c = 1
        
    if(c==1):
        return initial,int(blanks)
    else:
        return int(0),int(blanks)
        
Movies = ["ALPHA","INCREDIBLES","DEAD POOL","AVATAR","TITANIC","JURASSIC PARK","GLADIATOR","TROY","DIE HARD","GOD FATHER","ANT MAN","SPIDER MAN"]

rand_movie = random.choice(Movies)
l = len(rand_movie)
initial = gen(rand_movie,l)
initial = list(initial)
blanks = copy.copy(l)
score = 0
c = 1 #Continue flag
temp = copy.copy(rand_movie) 

#while(c!=0):    #continue
print("Guess the movie Name!");
print(''.join(initial))
while(blanks > 0):
    guess = input("Can you guess the movie name?  ").upper()
    if(guess == rand_movie): 
        score = blanks
        print("Awsome!")
        break
    else:
        print("Incorrect!")
        letter = input("Guess any letter in the movie name?  ")[0].upper()
        chk,blanks = check(letter,rand_movie,initial)
        while(chk==0):
            letter = input("Sorry! '",letter,"' is not in the movie name. Try again")[0].upper()
            chk,blanks = check(letter,rand_movie,initial)
        print(''.join(chk))

print("Your score is ",score)    