import numpy as np

#load data from file
items = np.loadtxt('input.txt', dtype=np.int32)

if(len(items) == 0):
  print("failed to read file... exiting...")
  exit()

for i in items:
  for j in items:
    for k in items:
      if ((i+j+k) == 2020):
        print(i*j*k)
        print(i,j,k)