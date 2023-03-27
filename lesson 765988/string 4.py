# put your python code here
def reversed1(variable):
    res=''
    for i in range(len(variable)-1,-1,-1):
        res+=variable[i]
    return res

def vsech(variable):
    res=''
    for i in range(len(variable)):
        if i%2 != 0:
            res+=variable[i]
    return res
def vsenech(variable):
    res=''
    for i in range(len(variable)):
        if i%2 == 0:
            res+=variable[i]
    return res

strin = input()

print(strin[1] * 4)
print(strin[-2:] + "!")
lenstr = len(strin) - 3
print(strin[0:lenstr])
print(strin+reversed1(strin))
print(vsech(strin))
print(vsenech(strin))