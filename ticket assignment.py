

n=int(input("how many ticket do you want to book"))
c=0
i=1
for i in range(1,n+i):
    a=input("enter the age or IF YOU ARE DONE ENTER quit ")
    a=a.lower()
    if a=="quit":
        c=c+0
    
        break
    else:
        a=int (a)
        if a<3 :
            c=c+0
            print("cost of ticket is free")
        else:
            if a >=3  and a<=12:
                c=c+10
                print("cost of  a ticket is $10")
            
            else:
                    if a>12:
                        c=c+15
                        print("cost of a ticket is$15")

print("your total cost of ",i ,"ticket is:$" ,c)
