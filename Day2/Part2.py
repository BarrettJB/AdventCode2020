validCount = 0

with open('input.txt','r') as inputFile:
  for line in inputFile:
    pieces = line.split(' ')
    rnge = pieces[0].split('-')
    charTarget = pieces[1][0]
    pswd = pieces[2]
    if(
        (pswd[int(rnge[0])-1] == charTarget or pswd[int(rnge[1])-1] == charTarget) and
        pswd[int(rnge[0])-1] != pswd[int(rnge[1])-1]
      ):
      validCount = validCount + 1;
      #print(line)
      #input()

print((validCount))