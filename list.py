##Take a list, say for example this one:
##	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
##and write a program that prints out all the elements of the list that are less than 5.

a = [1,2,3,1,2,3,4,5,65,22,22,234]

listwithout5 = []

for n in a:
  if n < 5:
    listwithout5.append(n)
print (listwithout5)
