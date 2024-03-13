nric = input('Enter an NRIC number: ')
nric = nric.upper()
if not nric.startswith('S') and nric.startswith('T') and nric.startswith('F') and nric.startswith('G'):
  print('NRIC is invalid.')
elif not nric[1:-2].isdecimal():
  print('NRIC is invalid.')
elif not nric[-1].isalpha():
  print('NRIC is invalid.')
elif len(nric) != 9:
  print('NRIC is invalid.')
else:
  num = int(nric[1])*2 + int(nric[2])*7 + int(nric[3])*6  + int(nric[4])*5 + int(nric[5])*4 + int(nric[6])*3 + int(nric[7])*2
  if nric[0] == ('T' or 'G'):
    num = int(num) + 4
  else: 
    num = int(num)
  quotient, remainder = divmod(num, 11)
  if nric[0].startswith('S') or nric[0].startswith('T'):
    string = ('J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A')
  else: 
    string = ('X', 'W', 'U', 'T', 'R', 'Q', 'P', 'N', 'M', 'L', 'K')
  if string[remainder] == nric [-1]:
    print('NRIC is valid.')
  else:
    print('NRIC is invalid.')