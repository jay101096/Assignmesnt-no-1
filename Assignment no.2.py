#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q.1
n = int(input())
for i in range (n):
    for j in range (i + 1):
        print("*", end = "")
    print("")
for ii in range (n , 0, -1):
    for jj in range (ii - 1, 0, -1):
        print("*", end = "")
    print("")


# In[2]:


#Q.2
s = input("enter any string: ")
print(s[::-1])


# In[ ]:




