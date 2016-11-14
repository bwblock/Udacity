def is_prime(num):
  i = 2
  while i < num or i < 3:
    if num % i == 0 and num != 0:
      return True
    i += 1
  return False
  
  
print (is_prime(2))