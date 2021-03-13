# -*- coding: utf-8 -*-
"""Assignment1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qD9LSYJERaicRHm7YHZHfjUXbt4sQCC0
"""

import random as rd

sample_data = 500000

list_of_balls = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
red_count = white_count = green_count = 0 
# 1 corresponds to red marble
# 2 corresponds to white marble
# 3 corresponds to green marble
for i in range(sample_data):
  temp = rd.randint(0, 16)
  if(list_of_balls[temp] == 1):
    red_count += 1
  elif(list_of_balls[temp] == 2):
    white_count += 1
  else:
    green_count += 1
prob_red = red_count / sample_data
prob_white = white_count / sample_data
prob_green = green_count / sample_data
print("Following results are obtained from the simulation")
print("(i) Probability that the taken out marble will be red is: {}".format(prob_red))
print("(ii) Probability that the taken out marble will be white is: {}".format(prob_white))
print("(iii) Probability that the taken out marble will not be green is: {}".format(1 - prob_green))
print()
print("Following results are obtained theoretically")
print("(i) Probability that the taken out marble will be red is: 0.294117647")
print("(ii) Probability that the taken out marble will be white is: 0.4705882353")
print("(iii) Probability that the taken out marble will not be green is: 0.764705883")
print("Both sets of results are approximately the same")

