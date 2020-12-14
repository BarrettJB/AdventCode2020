index = 0
trees = 0
with open('input.txt','r') as file:
  for line in file:
    print(line)
    if(index >= (len(line)-1)):
      index = index % (len(line)-1)
    print(index)
    if(line[index] == '#'):
      trees = trees + 1
    index = index + 3
 
print(trees)