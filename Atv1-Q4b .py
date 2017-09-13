
# coding: utf-8

# In[37]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[52]:


df = pd.read_csv('produtos-de-extensao.csv', sep=';', error_bad_lines=False)

dp = df[df['tproduto']=='ARTIGO']
count_artigo = len(dp)

dp2 = df[df['tproduto']=='REVISTA']
count_revista = len(dp2)

dp3 = df[df['tproduto']=='RELATÓRIO TÉCNICO']
count_RT = len(dp3)

dp4 = df[df['tproduto']=='LIVRO']
count_livro = len(dp4)

dp5 = df[df['tproduto']=='COMUNICAÇÃO']
count_Com = len(dp5)

dp6 = df[df['tproduto']=='CARTILHA']
count_cartilha = len(dp6)

dp7 = df[df['tproduto']=='MANUAL']
count_manual = len(dp7)

dp8 = df[df['tproduto']=='PRODUTO AUDIOVISUAL - VÍDEO']
count_PAv = len(dp8)

dp82 = df[df['tproduto']=='PRODUTO AUDIOVISUAL - FILME']
count_PAf = len(dp82)

dp83 = df[df['tproduto']=='PRODUTO AUDIOVISUAL - CD']
count_PAcd = len(dp83)

dp84 = df[df['tproduto']=='PRODUTO AUDIOVISUAL - DVD']
count_PAdvd = len(dp84)

dp9 = df[df['tproduto']=='PROGRAMA DE TV']
count_PTV = len(dp9)

dp10 = df[df['tproduto']=='PRODUTO ARTÍSTICO']
count_PArt = len(dp10)

dp11=df[df['tproduto']=='JORNAL']
count_j = len(dp11)

dp12 = dp11=df[df['tproduto']=='OUTROS']
count_outros = len(dp12)


# In[53]:


pop = {"ARTIGO": count_artigo , "REVISTA": count_revista, "RELATÓRIO TÉCNICO": count_RT, "LIVRO": count_livro
       , "COMUNICAÇÃO": count_Com, "CARTILHA" : count_cartilha , "MANUAL" : count_manual , "PROGRAMA AUDIOVISUAL - VÍDEO" : count_PAv,
        "PROGRAMA AUDIOVISUAL - FILME" : count_PAf,"PROGRAMA AUDIOVISUAL - DVD" : count_PAdvd,"PROGRAMA AUDIOVISUAL - CD" : count_PAcd ,"PROGRAMA DE TV" : count_PTV , "PRODUTO ARTÍSTICO":count_PArt , "JORNAL":count_j , "OUTROS":count_outros}

tp_produto = [i for i in pop.keys()]

qt_produto= [j for j in pop.values()]

popPos = np.arange(len(tp_produto))

azul = "green"


# In[54]:


plt.barh(popPos, qt_produto, align='center', color=azul)             
plt.yticks(popPos, tp_produto)   
plt.xlabel('quantidade de projetos concluídos')    
plt.title('Produtos de extensão da UFRN')
plt.show()


# In[ ]:




