import random as r
import string as s
c=['@','#','(',')','_']
print("\nWelcome, \nI'm chitti, \nHow may i help you in generating password :) ")
l=int(input("\nHow many letter you want : "))
n=int(input("\nHow many number you want : "))
cc=int(input("\nHow many character you want : "))
pas=[]
password=""
for i in range(l):
    A=r.choice(s.ascii_letters)
    pas+=A
for j in range(n):
    B=r.choice(['0','1','2','3','4','5','6','7','8','9'])
    pas+=B
for k in range(cc):
    C=r.choice(c)
    pas+=C
r.shuffle(pas)
for p in pas:
    password+=p
print(password)
