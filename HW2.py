#!/usr/bin/env python
# coding: utf-8

# In[10]:


#1
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')


# In[11]:


#2
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print('YES')
else:
    print('NO')


# In[12]:


#3
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2):
    print('YES')
else:
    print('NO')


# In[13]:


#4
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')


# In[15]:


#5
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (abs(x1-x2)==1 and abs(y1-y2)==2) or (abs(x1-x2)==2 and abs(y1-y2)==1):
    print("YES")
else:
    print("NO")
    


# In[16]:


#6
n = int(input())
m = int(input())
k = int(input())
if (k< m*n) and (k % m==0) or (k % n==0):
    print("YES")
else:
    print("NO")


# In[17]:


#7
n = int(input())
m = int(input())
x = int(input())
y = int(input())
# n, m = min(n, m), max(n, m)
if n > m:
    n, m = m, n
if x >= n / 2:
    x = n - x
if y >= m / 2:
    y = m - y
# print(min(x, y))
if x < y:
    print(x)
else:
    print(y)
    


# In[18]:


#8
a = int(input())
b = int(input())
c = int(input())
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a, b, c)


# In[6]:


a1, b1, c1, a2, b2, c2 = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
if a1*b1*c1 == a2*b2*c2:
    print('Boxes are equal')
elif a1*b1*c1 < a2*b2*c2 and ((b1 <= a2 and b1 <= b2 and b1 <= c2) or (a1 <= a2 and a1 <= b2 and b1 <= c2) or
                              (c1 <= a2 and c1 <= b2 and c1 <= c2)):
    print('The first box is smaller than the second one')
elif a1*b1*c1 > a2*b2*c2 and ((b1 >= a2 and b1 >= b2 and b1 >= c2) or (a1 >= a2 and a1 >= b2 and b1 >= c2) or
                              (c1 >= a2 and c1 >= b2 and c1 >= c2)):
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')

