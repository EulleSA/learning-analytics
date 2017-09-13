
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[10]:


#preparation of data
df = pd.read_csv('pesquisadores.csv', sep=';', error_bad_lines=False)

dp = df[df['centro']=='CENTRO DE TECNOLOGIA']
count_CT = len(dp)

dp2 = df[df['centro']=='UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE']
count_UFRN = len(dp2)

dp3 = df[df['centro']=='CENTRO DE CIÊNCIAS SOCIAIS APLICADAS']
count_CCSA = len(dp3)

dp4 = df[df['centro']=='CENTRO DE EDUCAÇÃO']
count_CE = len(dp4)

dp5 = df[df['centro']=='CENTRO DE CIÊNCIAS DA SAÚDE']
count_CCS = len(dp5)

dp6 = df[df['centro']=='CENTRO DE BIOCIÊNCIAS']
count_CB = len(dp6)

dp7 = df[df['centro']=='CENTRO DE CIÊNCIAS HUMANAS, LETRAS E ARTES']
count_CCHLA = len(dp7)

dp8 = df[df['centro']=='CENTRO DE  ENSINO SUPERIOR DO SERIDÓ']
count_CESS = len(dp8)

dp9 = df[df['centro']=='SUPERINTENDÊNCIA DO HUOL - EBSERH']
count_SH = len(dp9)


pop = {"CENTRO DE TECNOLOGIA": count_CT , "UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE* ": count_UFRN, "CENTRO DE CIÊNCIAS SOCIAIS APLICADAS": count_CCSA, "CENTRO DE EDUCAÇÃO": count_CE
       , "CENTRO DE CIÊNCIAS DA SAÚDE": count_CCS, "CENTRO DE BIOCIÊNCIAS" : count_CB , "CENTRO DE CIÊNCIAS HUMANAS, LETRAS E ARTES" : count_CCHLA , "CENTRO DE  ENSINO SUPERIOR DO SERIDÓ" : count_CESS
        , "SUPERINTENDÊNCIA DO HUOL - EBSERH" : count_SH}

tp_centro = [i for i in pop.keys()]

qt_pesquisadores = [j for j in pop.values()]

popPos = np.arange(len(tp_centro))

azul = "blue"


# In[11]:


#visualize results
plt.barh(popPos, qt_pesquisadores, align='center', color=azul)             
plt.yticks(popPos, tp_centro)   
plt.xlabel('Quantidade de pesquisadores')    
plt.title('População de pesquisadores da UFRN')
plt.show()



# In[ ]:




