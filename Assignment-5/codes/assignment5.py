# -*- coding: utf-8 -*-
"""Assignment5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Z1BGqmNPBEmskSA3xvUkklG-mUZZJIp9
"""

import numpy as np
from scipy.stats import bernoulli as brn
import plotly.graph_objects as go
import matplotlib.pyplot as plt


def factorial(n):
  fact = 1
  for i in range(1, n+1):
    fact *= i
  return fact

def combination(n, r) -> float:
  comb = factorial(n)/(factorial(n-r) * factorial(r))
  return comb


prob_head = 1/2
prob_tail = 1 - prob_head
number_of_simulations = int(5e5)
count = 0
for i in range(number_of_simulations):
  person_one = brn.rvs(size = 4, p = prob_head)
  person_two = brn.rvs(size = 4, p = prob_head)
  no_of_heads_one = np.size(np.nonzero(person_one == 1))
  no_of_heads_two = np.size(np.nonzero(person_two == 1))
  if no_of_heads_one == no_of_heads_two:
    count += 1

prob_equal_heads = count / number_of_simulations
theoretical_prob_equal_heads = 0
for i in range(5):
  temp = combination(4, i) * ((prob_head)**4)
  theoretical_prob_equal_heads += (temp * temp)

print("The probability obtained from theoretical calculations (correct upto three decimal places) is: {0:.3f}.",format(theoretical_prob_equal_heads))
print("The probability obtained from simulations (correct upto three decimal places) is: {0:.3f}.",format(prob_equal_heads))
error = abs(theoretical_prob_equal_heads - prob_equal_heads)
print("The error in finding probability is: {0:.3f}.".format(error))
print("As the error is extremely small, we can conclude that both sets of results are approximately the same.")

cases = ['']
x = np.arange(len(cases))
plt.bar(x + 0.00, theoretical_prob_equal_heads, color = "skyblue", width = 0.2, label = 'Theoretical')
plt.bar(x + 0.2, prob_equal_heads, color = "black", width = 0.2, label = 'Simulated')
plt.xlabel('Theoretical v/s Simulated')
plt.ylabel('P(X=Y) = Probability of equal heads')
plt.xticks(x  + 0.2/2,[''])
plt.legend()
plt.show()