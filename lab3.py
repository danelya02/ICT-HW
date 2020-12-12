#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1
s=input()
ans=str()
s=s.lower()
for i in s:
    if( i!='a' and i!='o' and i!='y' and i!='e'and  i!='u' and i!='i'):
        ans+=i
if( len(s)!=0):
    ans_fin='.'+s[0]
for i in range(1, len(ans)):
    ans_fin+='.'+ans[i]
print(ans_fin)


# In[ ]:


#2
s=input().split("+")
s.sort()
print("+".join(s))


# In[ ]:


#3
s=input()
ans=str()
for i in range(0,len(s)):
    if(i==0):
        ans+=s[i].capitalize()
    else:
        ans+=s[i]
print(ans) 


# In[ ]:


#4
s = input()
one = s.split("0000000")
zero = s.split("1111111")
isDangerous = False
# for i in one:
#     if len(i)>=7:
#         isDangerous=True
#         break
# print(one,zero)
if(len(one)>1 or len(zero)>1):
    print("YES")
else:
    print("NO")


# In[ ]:


#5
s=input()
s_set=set()
for i in s:
    s_set.add(i)
# print(s_set)
if(len(s_set)%2):
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")


# In[ ]:


#6
s=input()
ans=str()
cntUpper=0
cntLower=0
for i in range(0,len(s)):
    if(ord(s[i])<=122 and ord(s[i])>=97):
        cntLower+=1
    if(ord(s[i])<=90 and ord(s[i])>=65):
        cntUpper+=1
if(cntLower>=cntUpper):
    for i in s:
        ans+=i.lower()
else:
    for i in s:
        ans+=i.upper()
print(ans)


# In[ ]:


#7
s=input()
s_set=set()
for i in s:
    if((ord(i)<=122 and ord(i)>=97) or (ord(i)<=90 and ord(i)>=65)):
        s_set.add(i.lower())
print(s_set)
if(len(s_set)==26):
    print("YES")
else:
    print("NO")


# In[ ]:


#8
s1=input()
s2=input()
if(s2[::-1]==s1):
    print("YES")
else:
    print("NO")


# In[ ]:


#9
s=input()
if(s.count('A')>s.count('D')):
    print("Anton")
elif(s.count('A')<s.count('D')):
    print("Danik")
else:
    print("Friendship")


# In[ ]:


#10
def isLower(c):
    if(ord(c)<=122 and ord(c)>=97):
        return True
def isUpper(c):
    if(ord(c)<=90 and ord(c)>=65):
        return True
s=input()
cntUpper=0
cntLower=0
ans=str()
for i in range(0,len(s)):
    if(ord(s[i])<=122 and ord(s[i])>=97):
        cntLower+=1
    if(ord(s[i])<=90 and ord(s[i])>=65):
        cntUpper+=1
if(isLower(s[0])):
    # print(cntLower, cntUpper)
    if(cntUpper+1==len(s)):
        for i in range(0,len(s)):
            if(i==0):
                ans+=s[i].upper()
            else:
                ans+=s[i].lower()
elif(len(s)==1 and cntLower==1):
    ans+=s[0].upper()
elif(len(s)==cntUpper):
    for i in range(0,len(s)):
        ans+=s[i].lower()

print(ans)


# In[ ]:


#11
s = input()
countZ = s.count('z')
countE = s.count('e')
countR = s.count('r')
countO = s.count('o')
countN = s.count('n')
countOne = 0
countZero = 0
ans=str()
while(countO != 0 and countN != 0 and countE != 0):
    if(countO > 0 and countN > 0 and countE > 0):
        countO -= 1
        countN -= 1
        countE -= 1
        countOne += 1
while(countZ != 0 and countE != 0 and countR != 0 and countO != 0):
    if(countZ > 0 and countE > 0 and countR > 0 and countO > 0):
        countZ -= 1
        countE -= 1
        countR -= 1
        countO -= 1
        countZero += 1

while(countOne):
    ans+='1 '
    countOne-=1
while(countZero):
    ans+='0 '
    countZero-=1
print(ans.strip())


# In[ ]:


#12
s=input()
cnt=0
ans=0
for i in s:
    if(i=="x"):
        cnt+=1
    else:
        maxXBiggerThan2=cnt-2
        ans+=max(0,maxXBiggerThan2)
        cnt=0
maxXBiggerThan2=cnt-2
ans=max(0,maxXBiggerThan2)
print(ans)

