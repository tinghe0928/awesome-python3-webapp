#! /usr/bin/env python3

def perm(s,i):
     
    if i == len(s):
        print(s)
    else:
        for j in range(i,len(s)):
            s[i],s[j] = s[j],s[i]
            perm(s,i+1)
            s[i],s[j] = s[j],s[i]
           
s = "aac"
s = list(s)              
perm(s,0)
    
