def octal(n):
    lst=[]
    while(n>=1):
        lst.append(str(int(n%8)))
        n/=8
    return listToString(lst[::-1])
    #print(lst[::-1])

def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele  
    return str1 
        
def print_formatted(number):
    for i in range(1,number+1):
        print(str(i).ljust(4),octal(i).ljust(4),hex(i).lstrip("0x").ljust(4),bin(i).lstrip("0b").ljust(4))

    
    
n = int(input())
print_formatted(n)
