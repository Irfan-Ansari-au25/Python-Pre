



l=['scha', 'a', 'ba' ,'xyyx' ,'xsalxy' ,'uioiu']
N=len(l)
counter=0
for i in l:
    if len(i) >= 3 and len(i) <= 20 and i.endswith(i[:1]): # i.endswith(i[:1]) or i[0] == i[-1]
        counter+=1 
print(counter)