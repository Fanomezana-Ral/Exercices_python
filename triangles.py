#mampiditra valeur
# n = int(input("entrer la valeur de n: "))
n=5

print("triangle: ")
for i in range(1,n+1):
    print("*"*i)  
    
print("-----------")    
print("inverse: ")    
for i in range(n,0,-1):
    print("*"*i)

print("-----------")  
print("pyramide")
for i in range(1,n+1):
    espace = " "*(n-i)
    etoile = "*"*(2*i-1)
    print(espace+etoile)

print("-----------")  
print("pyramide inverse")
for i in range(n,0,-1):
    espace = " "*(n-i)
    etoile = "*"*(2*i-1)     
    print(espace+etoile)

print("-----------") 
print("fleche droite") 
for i in range(1,n+1):
    espace = " "*(n-1)
    etoile = "*"*(i)
    if (i==n-1):
        etoile="*"*(i*2)
        espace="*"*0
    elif(i==n):
        etoile="*"*((i*2)-1)
        espace="*"*0
    print (espace+etoile)
for i in range(n-1,0,-1):
    espace = " "*(n-1)
    etoile = "*"*(i)
    if (i==n-1):
        etoile="*"*(i*2)
        espace="*"*0
    elif(i==n):
        etoile="*"*((i*2))
        espace="*"*0  
    print (espace+etoile)

    
print("-----------") 
print("fleche gauche") 
for i in range(1,n+1):
    espace = " "*(n-i)
    etoile = "*"*i
    if (i== n-1):
        etoile ="*"*(i*2)
    elif(i==n):
        etoile ="*"*((i*2)-1)    
    print(espace+etoile)
for i in range(n-1,0,-1):
    espace = " "*(n-i)
    etoile = "*"*i
    if (i== n-1):
        etoile ="*"*(i*2)
    elif(i==n):
        etoile ="*"*((i*2)-1) 

    print(espace+etoile)

print("Sablier")
for i in range(n,0,-1):
    espace=" "*(n-i)
    etoile="*"*((i*2)-1)
    print(espace+etoile)  
for i in range(2,n+1):
    espace=" "*(n-i)
    etoile="*"*((i*2)-1)
    print(espace+etoile)    


for i in range(n,0,-1):
    etoile="*"*(n-i)
    espace=" "*((i*2)-1)
    print(etoile+espace+etoile)  
for i in range(2,n+1):
    etoile="*"*(n-i)
    espace=" "*((i*2)-1)
    print(etoile+espace+etoile)    