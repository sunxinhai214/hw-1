#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 19:48:09 2019

@author: stevensun
"""

class Vector:
    
    def __init__(self,d):
        if d is int:
            self.coords＝[0]*d
        elif d is list:
            self.coords=d
    
    def __sub__(self,other):
        newlst=[]
        if len(self.coords) == len(other):
            for i in range(len(self.coords)):
                newlst.append(self.coords[i]-other[i])
                
        return newlst
        
        
        
    def __neg__(self):
        newlst=[]
        for ele in self.coords:
            newlst.append(-ele)
        return newlst
            
        
    def __mul__(self,other):
        newlst=[]
        if other is list and len(other) == len(self.coords):
            for i in len(other):
                newlst.append(other[i]*self.coords[i])
        elif other is int:
            for ele in self.coords:
                newlst.append(int(other)*ele)
        return newlst
    
            
        
    def __rmul__ (self,other):
        newlst=[]
        if other is list and len(other) == len(self.coords):
            for i in len(other):
                newlst.append(other[i]*self.coords[i])
        elif other is int:
            for ele in self.coords:
                newlst.append(int(other)*ele)
        return newlst
    
    
        
        
    def 

        
        
        
            