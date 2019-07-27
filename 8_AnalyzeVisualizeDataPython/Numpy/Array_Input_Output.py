#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


arr = np.arange(5)


# In[3]:


arr


# In[4]:


np.save('myarray', arr)


# In[5]:


arr = np.array(20)
arr


# In[6]:


np.load('myarray.npy')


# In[7]:


arr1 = np.load('myarray.npy')


# In[8]:


arr1


# In[9]:


np.savez('ziparray.npz',x=arr, y=arr1)


# In[10]:


archive_array=np.load('ziparray.npz')


# In[11]:


archive_array['y']


# In[12]:


archive_array['x']


# In[13]:


arr = np.array([[1,2,3],[4,5,6]])


# In[14]:


np.savetxt('mytextarray', arr, delimiter=',')


arr = np.loadtxt('mytextarray', delimiter=',')
arr


# In[ ]:





# In[ ]:




