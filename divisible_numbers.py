##Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

user_num = input("Pick a number:")
divisible_num_list = []
x = range(1, (int(user_num)+1))
for n in x:
  if int(user_num)%n == 0:
    divisible_num_list.append(n)
print(divisible_num_list)
    
