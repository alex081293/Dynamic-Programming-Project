x = 0
sum = 0
for x in range(1000):
  if (x % 3 == 0):
    sum = sum+x
  elif (x % 5 == 0):
    sum = sum+x
print sum
