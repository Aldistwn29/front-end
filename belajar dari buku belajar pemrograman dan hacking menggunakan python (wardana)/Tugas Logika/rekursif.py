def faktorial(a):
    if a == 1:
        return 1
    else:
        return a * faktorial(a-1)

bil = int(input("Masukan Bilangan : "))
print("%d! = %d" % (bil, faktorial(bil)))

def faktorial(a):
     if a == 1: 
        return (a) 
    else: 
            return (a*faktorial(a-1)) 

bil = int(input("Masukan Bilangan : "))
print("%d! = %d" % (bil, faktorial(bil)))
