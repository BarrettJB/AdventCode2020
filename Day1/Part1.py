import numpy as np

#load data from file
items = np.loadtxt('input.txt', dtype=np.int32)

if(len(items) == 0):
  print("failed to read file... exiting...")
  exit()

for i in items:
  for j in items:
    if ((i+j) == 2020):
      print(i*j)
      print(i,j)