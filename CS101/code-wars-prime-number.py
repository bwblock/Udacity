def is_prime(num):
  num = abs(num)
  i = 2
  while i < num or i < 3:
    if num != 2 and num % i == 0 or num == 1:
      return False
    i += 1
  return True
  
  
print (is_prime(1))