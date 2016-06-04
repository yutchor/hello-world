#!/usr/bin/env python2.7 

########################
# Coin Tossing Program #
########################

import random
count = 0
point = 0
choice = input("How many choices? ")
while count < choice:
     
 count += 1    

 Q_answer = random.randrange(4)
 U_answer = random.randrange(1)

 if Q_answer == U_answer:
           print ('Correct!')
           point += 1
 if Q_answer != U_answer:
           print ('Wrong!')
           
percentage = point * 100 / choice
print ("Choices =",choice)
print ("Points =",point)
print ("Percentage =",percentage)


