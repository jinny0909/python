#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project 3, fractions.py
@author: Kyoungjin Lim
"""

class Frac: 
    
    def __init__(self, num, den): 
        
        """
        Parameters 
        -------
        
        num : TYPE, int 
            DESCRIPTION. numerator of fraction
        den: TYPE, int 
            DESCRIPTION. denominator of fraction 

        Returns
        -------
        Creates an instance of fraction 

        """
        self.num = num 
        self.den = den
        
        self.simplify()
                
        return 
    
    
    @staticmethod
    def _gcd(a, b):  
        """
        Return greatest common divisor Euclid algorithm.
        Parameters
        a : int
        b : int

        Returns
        a : int
        greatest common divisor of a,b
        """

        # Greatest common divisor Euclid algo
        while b:
            a, b = b, a % b
        return a
    


    def __str__(self): 
        return str(self.num) + "/" + str(self.den)
    
    def simplify(self):
        """Reduce fraction to its simplest form."""
        g = self._gcd(self.num, self.den)
        self.num = self.num//g
        self.den = self.den//g
        
        
    
   
    def _lcm(self, a,b): 
        """
        Return least common multiple Euclid algorithm.
        Parameters
        a : int
        b : int

        Returns
        a : int
        least common multiple of a,b
        
        """
        
        return a * b // self._gcd(a,b)
   
        
    def __add__(self, other):
        
        """
        Parameters 
        -------
        
        other : fraction 
            fraction addition 
        
        Returns
        -------
        Creates an instance of fraction 
            
        TYPE fraction 
            Result of + operation

        """
        
        if self.num == 0: 
            numer = other.num
            denom = other.den
           
        elif other.num == 0: 
            numer = self.num 
            denom = self.den
        
        elif self.den == other.den: 
            
            numer = self.num + other.num
            denom = self.den
        
        else: 
            denom = self._lcm(self.den, other.den)

            numer = int((denom / self.den) * self.num) +  int((denom / other.den) * other.num)
            
        return Frac(numer, denom)
    
    
    def __sub__(self, other):
        
        """
        Parameters 
        -------
        
        other : fraction 
            fraction subtraction
        
        Returns
        -------         
        TYPE fraction 
            Result of - operation

        """
        if self.den == other.den: 
        
            numer = self.num - other.num
            denom = self.den
        
        else: 
            denom = self._lcm(self.den, other.den)
            numer = int((denom / self.den) * self.num) -  int((denom / other.den) * other.num)

            
        return Frac(numer, denom)
        
    
    def __mul__(self, other):
        
        """
        Parameters 
        -------
        
        other : fraction 
            fraction multiplication
        
        Returns
        -------         
        TYPE fraction 
            Result of * operation
