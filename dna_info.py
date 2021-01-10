#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project: genomics 
@author: Kyoungjin Lim 
"""

import random 

def comp(string): 
    #helper function to convert binary into DNA code 
    result = ""
    
    if (string ==  "00"): 
        result = "A"
    elif (string == "01"): 
        result = "T"
    elif (string == "10"): 
        result = "C"
    elif (string == "11"): 
        result = "G"
        
    return result

def compback(string): 
    
    #helper function to convert DNA code into binary 
    result = ""
    
    if (string ==  "A"): 
        result = "00"
    elif (string == "T"): 
        result = "01"
    elif (string == "C"): 
        result = "10"
    elif (string == "G"): 
        result = "11"
        
    return result


def encode_sequence(string):
     
    #convert each char in string to ascii int 
    #convert that ascii int into binary form 
    #divide 8 bits binary by four parts, converting it to DNA base 
    
    result = ""
    
    for char in string: 
        num = ord(char)
        binary_string = '{0:08b}'.format(num)
        #split binary terms 
        
        result += comp(binary_string[0:2]) +  comp(binary_string[2:4]) + comp(binary_string[4:6]) + comp(binary_string[6:8]) 
    
    #return sequence of DNA bases that contain same info as string 
    return result 

def decode_sequence(stringdna): 
    
    
    #for each char in the given sequence of DNA 
    #turn into a binary format, add to string 
    #return that int into char, add them to return a string 
    
    binary = ""
    result = ""
    
    i = 0 
    
    while (i < len(stringdna)):
        binary = compback(stringdna[i]) + compback(stringdna[i+1]) + compback(stringdna[i + 2]) + compback(stringdna[i + 3])
        result += chr(int(binary, 2))
        i += 4 
    #return the string back - 
    return result 



def xor(x, y):
    
    #map for xor operation, symmetric 
    xormap = {('A', 'A'): 'A', ('A', 'T'): 'T', ('T', 'A'): 'T', ('A', 'C'): 'C', 
          ('C', 'A'): 'C', ('A', 'G'): 'G', ('G', 'A'): 'G', ('T', 'T'): 'A',
          ('C', 'T'): 'G', ('T', 'C'): 'G',  ('G', 'T'): 'C', ('T', 'G'): 'C', 
           ('C', 'C'): 'A', ('G', 'C'):'T', ('C', 'G'):'T', ('G','G'):'A'}
    
    return ''.join([xormap[a, b] for a, b in zip(x, y)])


def encrypt_decrypt(string, key = "CAT"): 
    
    #recursive design

    result = ""
    
    for char in string: 
        result += xor(char, key[0])

    if (len(key) == 1): 
        return result; 
     
    else:
        #input the result from above
        return encrypt_decrypt(result, key[1:])
     

def synthesizer(string):
    
    #string:: desired output 
    #return robot's output - reflecting the manufacturing process 
    
    #s_result is a return string 
    s_result = ""
    s = ""
    
    #dictionaries of probabilities, listed in sorted order 
    prob_T = {'G':0.02, 'C': 0.03, 'A': 0.05, 'T': 0.90 }
    prob_C = {'A': 0.01,  'G': 0.01,  'T': 0.01, 'C': 0.97}
    prob_G = {'A': 0.01, 'T': 0.02, 'C': 0.02, 'G': 0.95}
    
        
    for ch in string: 
        #A has 100 percent accuracy 
        if (ch == "A"): 
            s_result += "A"
            
        elif (ch == "T"): 
            curr = 0 
            rand = random.random()
            #loop through the probability dictionary 
