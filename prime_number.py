n = int(input('Enter a number: '))

j = True

for i in range (2, int(n**0.5)+1):      #Every composite number has a proper factor less than or equal to its square root.
  if n%i == 0:
    print (n, 'is not a prime number')
    j = False
    break
  if j == True:
    print (n, 'is a prime number')
