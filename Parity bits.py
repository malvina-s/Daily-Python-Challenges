# Parity bits


#First input
bit = input('Enter 8bit: ')
lenb = len(bit)

while lenb == 8:
    #counting zeroes and ones of the string
    zeroes = bit.count('0')
    ones = bit.count('1')
    #testing if there are 8 characters on the string that are ones and zeroes
    if zeroes + ones != 8:
        print ('Wrong input')
    else:
        #checking if the number of ones is even or odd
        if ones%2 == 0:
            print ('The parity bit should be 0')
        else:
            print ('The parity bit should be 1')
    #next input
    bit = input('Enter 8bit: (blank to quit) : ')
    lenb = len(bit)

#case where the first number has the wrong format
if lenb != 8 and lenb != 0:
    print('Wrong input')        
