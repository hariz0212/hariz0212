#!/usr/bin/env python
# coding: utf-8

# In[42]:


#Exercice1


# In[43]:


amis = ["Alice", "Bob", "Alice", "Dan", "Bob", "Carl","Bob","Dan","Carl","Bob","Dan","Alice","Dan","Bob"]

def cree_reseau(tab):
    dico={}
    i=0

    t=[]
    j=[]
    while i<len(tab):
        
        
        if tab[i] not in list(dico):
            dico[tab[i]]=[]
        if tab[i+1] not in list(dico):
            dico[tab[i+1]]=[]
            
        if tab[i]not in dico[tab[i+1]]:
            dico[tab[i+1]].append(tab[i])
        if tab[i+1] not in dico[tab[i]]:
            dico[tab[i]].append(tab[i+1])
        i+=2
        
        
    return dico
cree_reseau(amis)


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


reseau=cree_reseau(amis)
def liste_personne(reseau):
    return list(reseau)


# In[45]:


#Exercie 4


# In[ ]:





# In[46]:


def sont_amis(reseau, amis1, amis2):
    if amis2 not in reseau[amis1]:
        return False
    else:
        return True


# In[47]:


#Exercice 5


# In[48]:


def sont_amis_de(nom,tab,amis):
    reseau=cree_reseau(amis)
    tab_amis=reseau[nom]
    i=0
    while i<len(tab):
        if tab[i] not in tab_amis:

            return False
        i+=1
    return True
tab=['Bob']
sont_amis_de("Dan",tab,amis)
   


# In[ ]:


#Exercice 6


# In[ ]:


def est_commu(reseau, Groupe):
    i = 0
    while i < len(Groupe) :
        psg = i + 1
        while psg < len(Groupe):
            if Groupe[psg] not in reseau[Groupe[i]]:
                return False
            psg = psg + 1
        i = i + 1
    return True


# In[49]:


#Exercice 7


# In[50]:


def comu(a, amis):
    tabf = []
    reseau = cree_reseau(amis)
    j = 0
    while j < len(a):
        if j == 0:
            # Ajouter la première personne à tabf
            tabf.append(a[j])
            j += 1
        else:
            # Vérifie si la personne est amie avec tous ceux dans tabf
            if sont_amis_de(a[j], tabf, amis):
                 tabf.append(a[j])
            j+=1
    return tabf
a=['Alice', 'Bob', 'Carl','Dan']
comu(a,amis)
        


# In[51]:


#Exercice 8


# In[52]:


def tri_popu(b, amis):
    reseau = cree_reseau(amis)
    i = 1
    while i < len(b):
        cle = b[i]  # L'élément à insérer
        nb_amis_cle = len(reseau[cle])  # Nombre d'amis de la personne cle
        j = i
        # Décaler les éléments vers la droite pour faire de la place
        while j > 0 and nb_amis_cle > len(reseau[b[j-1]]):
            b[j] = b[j-1]
            j -= 1
        b[j] = cle  # Insérer l'élément à la bonne position
        i += 1
    return b
b=['Alice', 'Carl', 'Dan']
tri_popu(b,amis)


# In[53]:


#Exercice 9


# In[54]:


def comu_dans_reseau(c, amis):
    reseau = tri_popu(c, amis)
    return comu(reseau, amis)
comu_dans_reseau(b,amis)
    


# In[55]:


#Exercice10


# In[56]:


def comu_dans_amis(personne,amis):
    reseau=cree_reseau(amis)
    tab=reseau[personne]
    tabf=tri_popu(tab,amis)
    finale=comu(tabf,amis)
    finale.insert(0,personne)
    return finale

comu_dans_amis('Bob',amis)
    


# In[57]:


#Exercice 12


# In[60]:


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


# In[ ]:




