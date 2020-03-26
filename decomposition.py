import sympy #Library Input

def calculate_power(number1,divisor): #Funtion for power calculation
  if number1 == 0:
    return number1
  if number1 % divisor == 0:
    return 1 + calculate_power(number1 / divisor, divisor)
  else:
    return 0

def calculate_factorization(number1): #Funtion for geting factor
  dictionary = {}
  for prime in sympy.primerange(2, number1): 
    if number1 % prime == 0:
      check_power = calculate_power(number1, prime)
      dictionary[prime] = check_power
      number1 /= pow(prime, check_power)
      if number1 == 1 :
        return dictionary

def factor_fun(number1):
  output_dictionary = calculate_factorization(number1)
  print (' '.join('({},{})'.format(i,j) for i,j in output_dictionary.items()))
  

factorization = int(input("Enter The Number = "))
factor_fun(factorization)
