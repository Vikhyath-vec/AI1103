# -*- coding: utf-8 -*-
"""Assignment4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19iNiCBDe5GSNQeMwxDepHbnFrUVm_0zD
"""

import random as rd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import bernoulli as brn

def factorial(n):
  fact = 1
  for i in range(1, n+1):
    fact *= i
  return fact

def combination(n, r) -> float:
  comb = factorial(n)/(factorial(n-r) * factorial(r))
  return comb
theo_mean = 1/4
theo_var = 0
print("The theoretical expectation value is: {}".format(theo_mean))
print("The theoretical variance is: {}".format(theo_var))
prob_yn_special = []
number = [10, 50, 100, 500, 1000, 5000]

sample = 50000
for n in number:
  prob_one = 1/4
  prob_zero = 1 - prob_one
  data = []
  for i in range(n):
    temp = brn.rvs(size = sample, p = prob_one)
    data.append(temp)
 
  yn = []
  for j in range(sample):
    sum = 0
    for i in range(n):
      sum += data[i][j]
    temp = sum / n
    yn.append(temp)

  
  prob_yn = []
  for i in range(n+1):
    prob_yn.append(0)

  for i in range(sample):
    temp = int(yn[i] * n)
    prob_yn[temp] += 1

  for i in range(n+1):
    prob_yn[i] /= sample
  if n==10:
    prob_yn_special = prob_yn.copy()
  
  mean = 0
  for i in range(n+1):
    temp = i * prob_yn[i] / n
    mean += temp
  print("-----------------------------------------------------------------")
  print("Value of n = {}".format(n))
  print("The expectation value (mean) is: {}".format(mean))
  print("The error in expectation value is: {}".format(abs(mean - theo_mean)))

  variance = 0
  for i in range(n+1):
    temp = ((i/n - mean)**2 ) * prob_yn[i]
    variance += temp
  print()
  print("The variance is: {}".format(variance))
  print("The error in variance is: {}".format(abs(variance - theo_var)))

print("-----------------------------------------------------------------")
print("From the above results, it is visible that as n is increasing (tending to infinity), the mean value reaches {} while the variance reaches {}.".format(theo_mean, theo_var))
print("Thus, Yn converges, in probability, to {}.".format(theo_mean))
print("The following is the PMF graph of Yn for the case n = 10")
n = 10
x_axis = []
for i in range(n+1):
  x_axis.append(i/n)

prob_yn_theory = []
for i in range(n+1):
  temp = combination(n, i) * ((1/4) ** i) * ((3/4) ** (n-i))
  prob_yn_theory.append(temp)



#Plotting
plt.stem(x_axis,prob_yn_special, markerfmt='o', use_line_collection=True, label='Simulation')
plt.stem(x_axis,prob_yn_theory, markerfmt='o',use_line_collection=True, label='Analysis')
plt.xlabel('$n$')
plt.ylabel('$p_{Y}(n)$')
plt.xticks( x_axis)
plt.legend()
plt.grid()
plt.show()
print("The following is the CDF graph of Yn for the case n = 10")
for i in range(n+1):
  if i != 0:
    prob_yn_special[i] += prob_yn_special[i-1]
    prob_yn_theory[i] += prob_yn_theory[i-1]

plt.stem(x_axis,prob_yn_special, markerfmt='o', use_line_collection=True, label='Simulation')
plt.stem(x_axis,prob_yn_theory, markerfmt='o',use_line_collection=True, label='Analysis')
plt.xlabel('$n$')
plt.ylabel('$F_{Y}(n)$')
plt.xticks( x_axis)
plt.legend()
plt.grid()
plt.show()