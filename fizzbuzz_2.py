import sys

arg_len = len(sys.argv)

n=0
if arg_len > 1:
          n=int(sys.argv[1])
          if n <= 0:
                    print "Upper line {} is not valid for Fizz Buzz game, please run again with a valid value".format(n)
                    quit()
else:
          valid_input = False
          while not valid_input:
                    try:
                              n = int(raw_input("Please enter the upper line for the Fizz Buzz game: "))
                    except:
                              print "Input error! Please input a positive integer"
                    if n <= 0:
                              print "Input value {} is not valid for Fizz Buzz Upper line, please use a valid value"
                    else:
                              valid_input = True
                                                      
          
print("the upper line is {}".format(n))

for i in range(1, n+1):
          print("Fizz buzz counting up to {0}".format(i)) 
          if i%3 == 0 and i%5 == 0:
                    print("Fizz Buzz")
          elif i%3 == 0:
                    print("Fizz")
          elif i%5 == 0:
                    print("Buze")
          else:
                    print(i)