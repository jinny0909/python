"""
Kyoungjin Lim 

Decipher a message that is encrypted with this scheme: 'a' to 'z', 'b' to 'y' 
which is each alphabet mapping to its opponent in reversed order alphabet. 
Assume that input is always in lower.case.
"""



#string of alphabet 
alpha = "abcdefghijklmnopqrstuvwxyz"

#ask user input, convert input into a string 
string = str(input("Enter the encrypted message: "))

#define the reverse translation 
trans = str.maketrans(alpha[0:], alpha[25::-1])

#output the result based on the above translation
print("The plaintext message is: ", string.translate(trans))
