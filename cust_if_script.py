#!/usr/bin/env python3

"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""

message = 'the firmware needs to be updated'

# wrap versiom in a float() to accept decimals as numbers
version = int(input("what is the current firmware running? "))

# if input valuw was higher or equal to 26
if version >= 26:
    message = message + 'firmware is latest'

elif version == 25:
    message = message + 'firmware needs one revision update'

elif version == 24:
    message = message + 'firmware needs two revisions update'

else:
    message = message + 'update firmware imediately'

print (message)
