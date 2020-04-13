#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1) Assigning elements to different lists

L1=[];
L2=[];
n1=int(input("enter number of elements in list 1:"));
n2=int(input("enter number of elements in list 2:"));
for i in range(n1):
    x=int(input("enter element in list 1:"));
    L1.append(x);
for j in range(n2):
    y=int(input("enter element in list 2:"));
    L2.append(y);
print(L1)
print(L2)


# In[3]:


# 2) Accessing elements from a tuple

T=(3,5,6,7);
print(T);
x=int(input("enter the poition to access in tuple(startin position is 0)"));
print("you have accessed",x,"position and it holds the value:");
T[x]


# In[4]:


# 3) Deleting different dictionary elements.
D={"C":1,"python":2,"c++":3,"java":4};
print(D);
print("deleting C++ from dictionary");
del D["c++"];
print(D)


# In[ ]:




