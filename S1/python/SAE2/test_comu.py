#!/usr/bin/env python
# coding: utf-8

# In[42]:


#Exercice1


# In[43]:


def create_reseau_test():
    assert cree_reseau(amis) == {"Alice" : ["Bob","Dan"],
                                "Bob" : ["Alice","Carl","Dan"],
                                "Carl" : ["Bob"],
                                "Dan" : ["Alice", "Bob"]}
                               
    print("Le test est ok")
    
    
create_reseau_test()


# In[ ]:


#Exercice 3


# In[44]:


def test_liste_personne():
    assert liste_personne(reseau) == ["Alice", "Bob", "Carl", "Dan"]
    print("Le test est : Ok")
test_liste_personne()


# In[45]:


#Exercie 4


# In[46]:


def teste_sont_amis():
    assert sont_amis(reseau, "Alice", "Dan") == True
    assert sont_amis(reseau, "Alice", "Carl") == False
    print("Le teste est : Ok")
teste_sont_amis()


# In[47]:


#Exercice 5


# In[48]:


def teste_sont_de():
    assert sont_amis_de("Dan", ["Bob","Dan"], amis) == True
    assert sont_amis_de("Alice",["Bob","Carl"],amis) == False
    print("Le teste est : Ok")
teste_sont_amis()
   


# In[ ]:


#Exercice 6


# In[ ]:


def teste_est_commu():
    assert est_commu(reseau, ["Bob","Dan","Alice"])==True
    assert est_commu(reseau, ["Bob","Carl","Alice"])==False
    print("Le teste est : Ok")
teste_est_commu()


# In[49]:


#Exercice 7


# In[50]:


def teste_commu():
    assert commu(reseau,['Alice', 'Bob', 'Carl','Dan'])== ['Alice', 'Bob', 'Dan']
    assert commu(reseau, ['Carl','Alice', 'Bob', 'Dan'])== ['Carl', 'Bob']
    assert commu(reseau, ['Carl','Alice', 'Dan'])== ['Carl']
    print("Le teste est : Ok")
teste_commu()


# In[51]:


#Exercice 8


# In[52]:


def teste_tri_popu():
    assert tri_popu(['Alice', 'Bob', 'Carl'], amis)==[ 'Bob','Alice', 'Carl']
    print("Le teste est : Ok")
teste_tri_popu():


# In[53]:


#Exercice 9


# In[54]:


def teste_comu_dans_reseau():
    assert comu_dans_reseau(['Alice', 'Bob', 'Carl','Dan'], amis)==[ 'Bob','Alice', 'Dan']
    print("Le teste est : Ok")
teste_comu_dans_reseau


# In[55]:


#Exercice10


# In[56]:


def teste_comu_dans_amis():
    assert comu_dans_amis('Alice', amis)==['Alice', 'Bob', 'Dan']
    assert comu_dans_amis('Carl', amis)==['Carl', 'Bob']
    print("Le teste est : Ok")
teste_comu_dans_amis()


# In[57]:


#Exercice 12


# In[1]:


def comu_max(amis):
    reseau=cree_reseau(amis)
    liste=liste_personne(reseau)
    i=0
    t=0
    while i< len(reseau):
        comu=comu_dans_amis(liste[i],amis)
        if len(comu)>t:
            t=len(comu)
            comu_max=comu
        i+=1
    return comu_max
comu_max(amis)

def teste_comu_max():
    assert comu_max(amis)== ['Alice', 'Bob', 'Dan']
    print("Le teste est : Ok")

