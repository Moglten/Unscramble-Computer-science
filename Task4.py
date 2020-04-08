"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

telemarketersNumbers = []

#iterate over all Number And take what is TeleMarket Of it

for i in range(len(calls)):

    #Convert Number to String To make use Indexing

    number = str(calls[i][0])

    if ( number[0] == "1" ) and ( number[1]=="4" ) and ( number[2] == "0" ):

        telemarketersNumbers.append(number)

#Convert To Set to earse Duplicates

telemarketersNumbers = sorted(list(set(telemarketersNumbers)))


#Printing

print("These numbers could be telemarketers: ")
for i in range(len(telemarketersNumbers)):
    print(telemarketersNumbers[i] )

