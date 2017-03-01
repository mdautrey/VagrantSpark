# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 18:09:26 2016

@author: Karine
"""


import numpy as np
from numpy.linalg import *
from pylab import *
from time import time
from matplotlib import pyplot as mp
import matplotlib.pylab as plt
import math
import random
from random import gauss
import scipy.stats as sps   


random.seed(1)
#########################################################
#création des n va suivant une densité
########################################################
def normal(n):
# Dimension
    d = 2
#mu
    m = np.zeros(d)
#covariance
    cov = np.array([[0.95, 0.5], [0.5, 0.95]])
    X = np.random.multivariate_normal(m, cov, size=n)
    #plt.figure()
    #plt.scatter(X[:, 0], X[:, 1],marker='o');
    return X
   
def expo(n,lambd):
    X=np.zeros(n)
    for i in range(1,n):
        X[i] = np.random.exponential(lambd);
    #plt.figure()
    Y=np.zeros(n);
    #plt.scatter(X,Y,marker='o');
    X=X.reshape(1,n);
    return X
    
def mixte(n):
    X=np.zeros(n)  
#tirage aléatoire
    for i in range(1,n):
        d=np.random.rand(1)
        if (d<=0.5):
            X[i]=np.random.normal(1,1/3);
        else:
            X[i]=np.random.normal(-1,1/3);
            
    Y=0.1*np.ones(n);
    #affiche les barres en position x et de hauteur Y
    #plt.stem(X,Y);
    X=X.reshape(1,n);
    return X       

def traceNormal(x,m,sd):
    y=(np.exp(-pow(x-m,2)/sd))/(sd*np.sqrt(2*np.pi))
    return y
    
###########################################################    
####différentes largeur de fenêtre    
##########################################################

#calcul de l'écart type corrigé de données en colonnes
def sigma(X):
    #nombre de données
    n=X.shape[1]
    s=0;

    #calcul de la moyenne
    m=np.sum(X,axis=1)/n;
    print(m)
    #calcul de l'écart
    for i in range(1,n):
          s= s+pow(np.linalg.norm(X[:,i]-m),2)
    s=np.sqrt(s/(n-1));
    return s
   
#calcul de l'interquartile    
def IQR(dist):
    return np.percentile(dist, 75) - np.percentile(dist, 25)
    
#les va X sont données en colonnes 
def amiseNorm(X):
    ##nombre de variables
    n=X.shape[1];
    h=1.06*sigma(X)*pow(n,-1/5);
    return h

#les va X sont données en colonnes 
def amiseNorm2(X):
    ##nombre de variables
    n=X.shape[1];
    h=0.79*IQR(X)*pow(n,-1/5);
    return h

#les va X sont données en colonnes 
def srot(X):
    ##nombre de variables
    n=X.shape[1];
    A=min(sigma(X),IQR(X)/1.34);
    h=0.9*A*pow(n,-1/5);
    return h    

def os(X):
    ##nombre de variables
    n=X.shape[1];
    h=1.144*sigma(X)*pow(n,-1/5);
    return h    
 
#X=mixte(10);    
#print(amiseNorm(X));    
#print(amiseNorm2(X));   
#print(os(X));
#print(srot(X));
#print(1.144/1.06);


###########################################################
#############calcul du noyau de densité gaussienne       
#les va X sont données en colonnes  
#h est la largeur de la fenêtre  
def kernelDens(Xd,h):
    ##nombre de variables
    n=Xd.shape[1]
    x=np.linspace(min(Xd[0,:]),max(Xd[0,:]),1000);
    y=np.zeros(len(x));

    hauteur=np.zeros(n);
    #hauteur=hauteur.reshape(1,n)
    
    for i in range(1,len(y)):
        #print(i)
        somme=0;
        for j in range(1,n):
           somme=somme+(np.exp(-pow((x[i]-Xd[0,j]),2)/h))/np.sqrt(2*np.pi)
           ##représentattion des gausiennes centrées sur chaque valeur
           #plt.plot(x,traceNormal(x,Xd[0,j],h)/n);
           #calcul de la hauteur de la loi normale
           #hauteur[j]=max(traceNormal(x,Xd[0,j],h)/n);
        y[i]=somme/(n*h)
    #plt.stem(Xd[0,:],hauteur,marker='o');
    plt.plot(x,y)  
    return n
#print(mixte(10)[0])
#nombre de réalisations souhaitée
n=500
## m et sd : moyenne et écart type de la normale
m=0
sd=1
X=np.random.normal(m,sd,n)
X=X.reshape(1,n)

xtheo=linspace(min(X[0,:]),max(X[0,:]),100)
ytheo=traceNormal(xtheo,m,sd)
#plt.plot(xtheo,ytheo)

#kernelDens(X,0.059)   

# Simulation des marchés suivant une loi normale multidimensionnelle
# de moyenne mu et de matrice de variance covariance

def market(mu,cov):
    #n est le nombre de marchés donc la longueur du vecteur moyenne mu
    n=len(mu)
    res= np.zeros(n);
    res = np.random.multivariate_normal(mu, cov, size=1);
    #res.reshape(1,len(mu))
    return res;

#tests sur nombre de marchés=n
n=5   
m=np.random.rand(5);

# vérification que la matrice de covariance est semi-définie positive
def is_pos(x):
    return np.all(np.linalg.eigvals(x) >= 0)   

def is_pos_def(x):
    return np.all(np.linalg.eigvals(x) > 0)
   
#n : taille i.e. nombres de données
##Création d'une matrice de covariance
def covTest(n):
    #initialisation avecun ematrice non positive
    res= -1*np.ones(n**2);
    res=res.reshape(n,n);
    #print(np.linalg.eigvals(res))
    #jusqu'à obtenir une matrice positive
    while (not(is_pos(res))):
        #print(res);
        for i in range(0,n):
           for j in range(i,n):
               res[i,j]=np.random.rand(1);
               res[j,i]=res[i,j];
    return res;

def muTest(n):
    res=np.random.rand(n);
    return(res)

# Création des données suivant le nombre de données temporelles ntemps
def marketTest(mu,cov,nTemps):
    #n: nombre de marchés qui va devenir le nombre de colonnes
    n=len(mu) 
    #nTemps ets le nombre de lignes
    res=np.zeros(n*nTemps).reshape(nTemps,n); 
    for i in range(0,nTemps):
        #print("A l'instant", i)
        res[i,:]=market(mu,cov);
        #print(res[i,:])
    return res;
 
####################################################################    
##################              Tests            ################### 
####################################################################
   
##nombre de marchés    
n=2
##nombre d'instants où sont relevés les marchés
nTemps=5
    
#a=covTest(n) 
#print(a) 
#print(np.linalg.eigvals(a))
#print(is_pos_def(a))   
#print(is_pos(a)) 
#print("vecteur moyenne")
#print(muTest(n))
#print("matrice de covariance")
#print(covTest(n))
#
#market1=marketTest(muTest(n),covTest(n),5)       
#print("réalisations des marchés")
#print(market1)
#

####################test sur un porte-feuille de 1000 réparti en nb actions 
nb=3
f=1000/nb*np.ones(nb)

# f valeur du porte-feuille : 1 ligne et n colonnes
def returnFact(f):
    n=len(f);
    f=f.reshape(n,1)
    res=np.zeros(n);
    res=res.reshape(1,n);
    print('taille')
    print(f)
    #matrice des coefficients , la divion par 100 est pour avoir des retours
    # de l'ordre du 1% max
    W=np.random.random(n**2)/100;
    W=W.reshape(n,n)
    print('coeff');
    print(W);
    #vecteur de l'intercept
    c=np.random.random(n);
    c=c.reshape(n,1);
    print('intercept');
    print(c);

    res=np.dot(W,f)+c;
    #print('res')
    #print(res)
    #res=res.reshape(1,n)
    return (res)

print(returnFact(f))


##définition du porte-feuille ayant 10 actions
# f :vecteur contenant les valeurs des actions
def portfolio(x):
    #nombre des actions
    n=len(x);
    
    










#def portefeuille(x,w):
    

#    g=np.sum(data, axis=0)/n;
#    return(g)
# 
#            xpoint = np.array([data[i,0],data[j,0]]);
#            ypoint = np.array([data[i,1],data[j,1]]);
