#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#anagram
s1=input().lower().replace(" ", "")
s2=input().lower().replace(" ", "")
print(s1,s2)
s1_set=set(s1)
s2_set=set(s2)
isAnagram=True
if len(s1)==len(s2):
    for c in s1_set:
        if not(s1.count(c)==s2.count(c)):
            isAnagram=False
            break
else:
    isAnagram=False
if isAnagram:
    print("Yes")
else:
    print("not Anagram")


# In[ ]:


#bingo
import random
bingo = {}
for i in range(1,76):


# In[ ]:


#morse
def reverseLookup(data,value): 
    keys = []
    for key in data:
        if data[key] == value:
            keys.append(key)   
    return keys
morse ={
        'A': '.-', 
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.', 
        'G': '--.', 
        'H': '....',
        'I': '..', 
        'J': '.---', 
        'K': '-.-',
        'L': '.-..', 
        'M': '--', 
        'N': '-.',
        'O': '---', 
        'P': '.--.', 
        'Q': '--.-',
        'R': '.-.', 
        'S': '...', 
        'T': '-',
        'U': '..-', 
        'V': '...-', 
        'W': '.--',
        'X': '-..-', 
        'Y': '-.--', 
        'Z': '--..',
        '1': '.----', 
        '2': '..---', 
        '3': '...--',
        '4': '....-', 
        '5': '.....', 
        '6': '-....',
        '7': '--...', 
        '8': '---..', 
        '9': '----.',
        '0': '-----'
    }
a=input().split()
ans=''
for i in a:
    ans+=str(reverseLookup(morse, str(i)))
print(ans)


# In[ ]:


#pcodes
postalCodes={
    'A':"Newfoundland","B":"Nova Scotia","C":"Prince Edward Island","E":"New Brunswick","G":"Quebec","H":"Quebec","J":"Quebec",
    "K":"Ontario","L":"Ontario","M":"Ontario","N":"Ontario","P":"Ontario","R":"Manitoba","S":"Saskatchewan","T":"Alberta","V":"British Columbia",
    "X":"Nunavut or Northwest Territories","Y":"Yukon"
}
code=input().strip()
prov=code[0]
ans=''
ans+=str(postalCodes[prov])
if(code[1]==0):
    ans+=" and Rural"
else:
    ans+=" and Urban"
print(ans)


# In[ ]:


#reverse
def reverseLookup(data,value): 
    keys = []
    for key in data:
        if data[key] == value:
            keys.append(key)   
    return keys
myDic={
    "color":"blue",
    "price":"pricey",
    "brand":"bmw",
    "model":"555",
    "watch":"pricey"
}
print(reverseLookup(myDic, "blue"))
print(reverseLookup(myDic, "555"))
print(reverseLookup(myDic, "pricey"))


# In[ ]:


#score
scores = {
    "a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
            "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
            "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
            "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
            "x": 8, "z": 10
}
word = input().lower()

total = 0
for c in word:
    total += scores[c]
print(total)


# In[ ]:


#numtoeng
def toEnglish(num):
    d={
            0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",
            11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",
            30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",
            100:"one hundred",200:"two hundred",300:"three hundred",400:"four hundred",500:"five hundred",
            600:"six hundred",700:"seven hundred",800:"eight hundred",900:"nine hundred"
       }
    
    s=""
    c=0
    if(num==0):
        return "zero"
    while(num>0):
        r=num%10
        if(r!=0):
            s=d[r*(10**c)]+" "+s
        num=num//10
        c=c+1
    return s

a=int(input())
print(toEnglish(a))

