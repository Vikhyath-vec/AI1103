# -*- coding: utf-8 -*-
"""Assignment7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A1siOtJNFkO6lVQlKH2cUHtACNO5fHQy
"""

import random as rd

sample_size = 100000
# lists containing results
x = []
y = []
z = []
u = []
for i in range(sample_size):
  dice_one = rd.randint(1,6)
  dice_two = rd.randint(1,6)
  sum = dice_one + dice_two
  x.append(dice_one)
  y.append(dice_two)
  z.append(sum)
  u.append(sum % 6)

# counting lists
prob_x = [0, 0, 0, 0, 0, 0]
prob_y = [0, 0, 0, 0, 0, 0]
prob_z = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
prob_u = [0, 0, 0, 0, 0, 0]
for i in range(sample_size):
  prob_x[(x[i]-1)] += 1
  prob_y[(y[i]-1)] += 1
  prob_z[(z[i]-1)] += 1
  prob_u[(u[i])] += 1

for i in range(6):
  prob_x[i] /= sample_size
  prob_y[i] /= sample_size
  prob_u[i] /= sample_size
for i in range(12):
  prob_z[i] /= sample_size

# print(prob_x)
# print(prob_y)
# print(prob_z)
# print(prob_u)


# checking option 1

flag = 0
for i in range(6):
  for j in range(12):
    count = 0
    for k in range(sample_size):
      if x[k] == i+1 and z[k] == j+1:
        count += 1
    if abs((count / sample_size) - (prob_x[i] * prob_z[j])) >= 0.005:
      flag = 1
      break
  if flag == 1:
    break
if flag == 1:
  print("X and Z are not independent")
else:
  print("X and Z are independent")

# checking option 2

flag = 0
for i in range(6):
  for j in range(6):
    count = 0
    for k in range(sample_size):
      if x[k] == i+1 and u[k] == j:
        count += 1
    if abs((count / sample_size) - (prob_x[i] * prob_u[j])) >= 0.005:
      flag = 1
      break
  if flag == 1:
    break
if flag == 1:
  print("X and U are not independent")
else:
  print("X and U are independent")

# checking option 3

flag = 0
for i in range(6):
  for j in range(12):
    count = 0
    for k in range(sample_size):
      if u[k] == i and z[k] == j+1:
        count += 1
    if abs((count / sample_size) - (prob_u[i] * prob_z[j])) >= 0.005:
      flag = 1
      break
  if flag == 1:
    break
if flag == 1:
  print("U and Z are not independent")
else:
  print("U and Z are independent")

# checking option 1

flag = 0
for i in range(6):
  for j in range(12):
    count = 0
    for k in range(sample_size):
      if y[k] == i+1 and z[k] == j+1:
        count += 1
    if abs((count / sample_size) - (prob_y[i] * prob_z[j])) >= 0.005:
      flag = 1
      break
  if flag == 1:
    break
if flag == 1:
  print("Y and Z are not independent")
else:
  print("Y and Z are independent")

print("Hence the correct options are (2) and (4)")
