#!/usr/bin/env python
# coding: utf-8

# In[2]:


#10
n = int(input())
i = 1
while i ** 2 <= n:
    print(i ** 2)
    i= i+1
    


# In[7]:


#11
n=int(input())
if (n >= 2):
    for i in range (2, i+1):
        if (n % i==0):
            print (i)
            break


# In[9]:


#12
n= int(input())
i=0
while 2**i<= n:
    print(2**i)
    i=i+1


# In[10]:


sum = 0 
while True: 
    n = int(input()) 
    if n == 0: #
        break 
    sum += n 
print(sum)


# In[13]:


maximum = 0
num_maximal = 0
element = -1
while element != 0:
    element = int(input())
    if element > maximum:
        maximum, num_maximal = element, 1
    elif element == maximum:
        num_maximal += 1       
print(num_maximal)


# In[14]:


n = int(input())    
phi_previous = 0
phi= 1
for i in range(n - 1): 
    phi, phi_previous = phi + phi_previous, phi
print(phi if n > 0 else 0) 


# In[16]:


max = 0
element = -1
while element != 0:
    element = int(input())
    if element > max:
        max = element
print(max)


# In[20]:


a = [int(i) for i in input().split()]
num_distinct = 1
for i in range(0, len(a) - 1):
    if a[i] != a[i + 1]:
        num_distinct += 1
print(num_distinct)


# In[21]:


a = [int(i) for i in input().split()]
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))


# In[23]:


a = [int(s) for s in input().split()]
counter = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            counter += 1
print(counter)


# In[24]:


n, k = [int(s) for s in input().split()]
bahn = ['I'] * n
for i in range(k):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        bahn[j] = '.'
print(''.join(bahn))


# In[ ]:




