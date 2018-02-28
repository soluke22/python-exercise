#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fib_machine():
  user = int(input("Give me a number to make a Fibonnaci sequence with:"))
  a = 1
  if fib_machine == 0:
    Fib_list = []
  elif fib_machine == 1:
    Fib_list = [1]
  elif fib_machine == 2:
    Fib_list == [1,1]
  elif fib_machine > 2:
    Fib_list == [1,1]
    while a < (user - 1):
      Fib_list.append(Fib_list[a]+Fibi_list[a-1])
      a +=1
  return Fib_list
  
#doesnt seem to work
