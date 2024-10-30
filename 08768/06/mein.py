f=open("input.txt","r")
s=f.readline()
f.close()
a,b,c = map(int,s.split())
f=open("autput.txt","w")
f.write(str(a+b+c))
f.close