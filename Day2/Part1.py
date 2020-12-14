validCount = 0

with open('input.txt','r') as input:
  for line in input:
    pieces = line.split(' ')
    rnge = pieces[0].split('-')
    charTarget = pieces[1][0]
    pswd = pieces[2]
    count = pswd.count(charTarget)
    if(count >= int(rnge[0]) and count <= int(rnge[1])):
      validCount = validCount + 1;

print(validCount)