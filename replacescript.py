import os

filename = 'H:/incubyte/inputfiles/cust_data.txt'

f=open(filename,"r")
x=""+f.read()
x=x.replace("|D|","")
f.close()

fout = open('H:/incubyte/inputfiles/cust_data1.txt',"wt")
fout.write(x)
fout.close()