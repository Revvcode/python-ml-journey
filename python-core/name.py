# sys has system functionalities
# this is useful for command line arguements - sys.argv stores name of the program in 0th index
# sys.exit helps ecit programs and also supports printing an exit string
# list slicing is possible by [starting index: Ending index] -  Ending index can be empty

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguements")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)