#
# Haydin Davis
# 10/31
# Magic 8 Ball Programming Project
# COSC 2409 DNT
#
import random

infile=open('8_ball_responses.txt','r')
awnsers=infile.readlines()

question=input("Ask me anything: ")
print(random.choice(awnsers))
