# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:58:07 2023
@author: Aditya Sarwade
"""
print("Welcome to the QUIZ!")

playing = input("Do you wish to play? ").lower()

if playing  != "yes":
    quit()

print("Okay Lets Play : ) ")

score = 0

answer = input(" What does CPU stand for  ")
if answer.lower() == "central processing unit":
    print('Correct !!')
    score +=1
else:
    print('Incorrect ')

answer = input(" What does  GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print('Correct !!')
    score +=1
else:
    print('Incorrect ')

answer = input(" Who developed python? ")
if answer.lower() == "guido van rossum":
    print('Correct !!')
    score +=1
else:
    print('Incorrect ')

answer = input(" What does psu stands for? ")
if answer.lower() == "power supply unit":
    print('Correct !!')
    score +=1
else:
    print('Incorrect ')

print("The score is "+ str(score)+ "  correct questions ! " )
print("The score is "+ str((score /4)* 100) + "%")
