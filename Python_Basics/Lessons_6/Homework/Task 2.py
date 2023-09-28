k=0
ocenki=[5,3,2,4,4,2]
for i in ocenki:
    if i==5 or i==4 or i==3:
        k+=1
print(ocenki,(k/len(ocenki))*100)