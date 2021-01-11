"""
Kyoungjin Lim
"""



#alphabet string
alpha = "abcdefghijklmnopqrstuvwxyz"
#given chiValue table 
chi_table = [0.082, 0.015, 0.028, 0.043, 0.130, 0.022, 0.020, 0.061, 
                  0.070, 0.0015, 0.0077, 0.040, 0.024, 0.067, 0.075, 0.019, 
                  0.00095, 0.060, 0.063, 0.091, 0.028, 0.0098, 0.024, 0.0015,
                  0.020, 0.00074]

#ask for user input 
string = str(input("Enter the encrypted message: "))
#initialize results list that will stor 25 versions of message 
results_arr = [] 

#25 different translated messages based on different shift_by values 
#i representing shift_by value 
for i in range (25): 
    trans = str.maketrans(alpha, alpha[i:] + alpha[:i])
    results_arr.append(string.translate(trans))

#list of calculated chi values     
chi = []

#for each message stored in the results_arr
for string in results_arr: 
    chiVal = 0
    for i in range(25): 
        if alpha[i] in string: 
            j = 0; 
            occur = 0; 
            #occur representing frequency of char
            #get frequency of each char in the string 
            while (j < len(string)): 
                if string[j] == alpha[i]: 
                    occur += 1 
                j += 1 
            chiVal += ((occur - chi_table[i]*len(string))**2) / (chi_table[i]*len(string))
        else: 
            chiVal += chi_table[i]*len(string)
    #insert calculated chi value to the list 
    chi.append(chiVal)

#get the index of minimum chi value in the list 
idx = chi.index(min(chi))

#output the message with the minimum chi value 
print("The plaintext message is: ", results_arr[idx])
