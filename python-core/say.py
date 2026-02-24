# packages can be helpful to get functions,etc.

import sys

from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])