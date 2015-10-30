n=31
print("the upper line is {0}".format(n))
for i in range(1, n+1):
          print("Fizz buzz counting up to {0}".format(i)) 
          if i%3 == 0 and i%5 == 0:
                    print("Fizz Buzz")
          elif i%3 == 0:
                    print("Fizz")
          elif i%5 == 0:
                    print("Buzee")
          else:
                    print(i)
