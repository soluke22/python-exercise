#Ask the user for a number and determine whether the number is prime or not.
def get_numb(numb_text):
    return int(input(numb_text))
prime_numb = get_numb("Pick any number:")
n = list(range(2,int(prime_numb)+1))
for a in n:
  if prime_numb == 2:
    print("That number is prime.")
    break
  elif prime_numb == 1:
    print("That number is not prime.")
    break
  elif prime_numb%a == 0:
    print("That number is not prime.")
    break
  else:
    print("That is a prime number!")
    break
