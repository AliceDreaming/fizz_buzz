import sys

print " The name of this script is {}".format(sys.argv[0])
print " User supplied {} argument at run time".format(len(sys.argv))

for arg in sys.argv[1:]:
          print arg
