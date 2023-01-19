a = input('number 1 (?):')
b = input('number 2 (?):')
c = input('oporater (?):')

if a.isnumeric() == False :
    
    print("error not a number")

if b.isnumeric() == False :
    
    print("error not a number")
    

if c == '+' :
    h = int(a)+int(b)
    
    print(h)
