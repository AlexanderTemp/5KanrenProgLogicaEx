# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 21:57:19 2021

@author: Alexander Humberto Nina Pacajes
"""
from kanren import Relation, facts, run, conde,var
papa=Relation()
mama=Relation()
mujer=Relation()
hombre=Relation()
facts(papa,('Humberto', 'Alexander'),
          ('Humberto', 'Yamileth'),
          ('Santiago','Humberto'),
          ('Santiago','Rosario'),
          ('Santiago','Rene'),
          ('German','Edwin'),
          ('German','Beatriz'),
          ('Edwin','Roberto'),
          ('Edwin', 'Michelle'))
facts(mama,('Beatriz','Alexander'),
           ('Beatriz','Yamileth'),
           ('Maria','Michelle'),
           ('Maria','Roberto'),
           ('Rosa','Edwin'),
           ('Rosa','Beatriz'),
           ('Julia','Humberto'),
           ('Julia','Rosario'),
           ('Julia','Rene'))
facts(mujer,('Rosa'),('Maria'),('Beatriz'),('Michelle'),('Julia'),('Rosario'),('Yamileth'))
facts(hombre,('German'),('Santiago'),('Edwin'),('Roberto'),('Humberto'),('Rene'),('Alexander'))
q=var()
def padres(p, hijos):
    return conde([papa(p,hijos)], [mama(p, hijos)])
def hijos(p,h):
    return conde([padres(h,p)])
def abuelos(a,n):
    y=var()
    return conde((padres(a,y), padres(y,n)))
def nietos(a,n):
    return conde([abuelos(n,a)])
def tios(t,x):
    y=var()
    z=var()
    return conde((padres(y,x),padres(z,y),hijos(t,z)))
def primos(p,x):
    z=var()
    y=var()
    w=var()
    return conde((padres(z,p),padres(y,x),padres(w,y),padres(w,z)))
print('- Quienes son los padres de Alexander?')
print((run(0,q,padres(q,'Alexander'))))
print('- Quienes son los hijos de Humberto')
print((run(0,q,hijos(q,'Humberto'))))
print('- Quienes son los abuelos de Alexander?')
print((run(0,q,abuelos(q,'Alexander'))))
print('- Quienes son los nietos de Santiago')
print((run(0,q,nietos(q,'Santiago'))))
print('- Quienes son los tios de Alexander?')
print((run(0,q,tios(q,'Alexander'))))
print('- Quienes son los primos de Alexander?')
print((run(0,q,primos(q,'Alexander'))))
