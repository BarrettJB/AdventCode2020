answer = 1
for slope in range(1,10,2):
  index = 0
  trees = 0
  skip = 0
  with open('input.txt','r') as file:
    for line in file:
      if(slope == 9 and skip == 1):
        skip = 0
        continue
      else:
        skip = 1
      if(index >= (len(line)-1)):
        index = index % (len(line)-1)
      if(line[index] == '#'):
        trees = trees + 1
      index = index + (slope%8)
  print(slope, ": ", trees)
  answer = answer * trees
print(answer)