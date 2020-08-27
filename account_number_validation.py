import fileinput

# def hex_to_deci(A):
#     ch="0123456789ABCDEF"
#     i=0
#     deci=0
#     for j in range(len(A)-1,-1,-1):
#         deci=deci+ ch.index(A[j])*(16**i)
#         i=i+1
#     return(deci)
# def deci_to_hex(N):
#     N=int(N)
#     A=hex(N)
#     return(A[2:])

def process(line: str) -> str:
    #print(line)
    try:
        num=int(line,16)

    except:
        return("INVALID")
    if(len(line)!=8):
        return("INVALID")
    num=int(line[2:8],16)
    summ=0
    while(num!=0):
        summ=summ + (num%10)
        num=num//10
    compare=(str(hex(summ))[2:]).upper()
    #print(int(line[0:2],16))
    if(int(line[0:2],16)==int(compare,16)):
        return("VALID")
    return("INVALID")
    # # Return 'VALID' or 'INVALID'
    # if(len(line)!=8):
    #     return("INVALID")
    # deci=hex_to_deci(line[2:])
    # #print(deci)
    # sum_of_digits=0
    # for digit in str(deci):
    #     sum_of_digits +=int(digit)
    # #print(sum_of_digits)
    # hexa=deci_to_hex(sum_of_digits)
    # #print(str(hexa.upper))
    # #print(line[0:2])
    # if(hexa.upper()==line[0:2]):
    #     return("VALID")
    # else:
    #     return("INVALID")
    

for line in fileinput.input():