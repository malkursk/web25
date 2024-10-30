jewels="pgs"
stone=input("какие камни вы нашли? ")
count=0
for s in stone:
    if s in jewels:
        count+=1
if count>4:
    print("молодец! ты нашел ", count, "камней")
elif count>0:
    print("неплохо, ты нашел ", count, "камней, в следующий раз найдёшь больше")
else:
    print("ты не нашел камней, в следующий раз повезёт")