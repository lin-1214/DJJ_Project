#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import numpy as np
import csv


dataset = []
pred_set = []

with open('./dataset.csv', newline='') as csvfile:
  rows = csv.reader(csvfile)
  for row in rows:
    dataset.append(float(row[1]))
    
for i in range(1,len(dataset)) :
    pred_set.append(dataset[i])

pred_set.append(0)

dataset=np.array(dataset)
pred_set=np.array(pred_set)
    
err = np.subtract(dataset, pred_set)
err = np.delete(err, len(err)-1)
RMSE = np.sqrt(np.mean(np.square(err)))
    
print(f"RMSE for July : {RMSE}")


# In[ ]:





# In[ ]:





# In[ ]:




