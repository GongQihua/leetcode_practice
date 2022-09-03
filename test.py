#（a,e,i,o,u)
# If you need to import additional packages or classes, please import here.

from re import A


def func(x):

 
    n = len(x)
    ans = []
    for i in range(n):
        if x[i] == ' ':
            t = x[i]
        if x[i] == 'A' or x[i] == 'E' or x[i] == 'I' or x[i] == 'O' or x[i] == 'U':
            t = x[i]
        if x[i] == 'a' or x[i] == 'e' or x[i] == 'i' or x[i] == 'o' or x[i] == 'o':
            t = x[i].upper()
        else:
            t = x[i].lower()
        ans.append(t)
    return ans
    
if __name__ == "__main__":
    #x = input()
    x = 'Who Love Solo'
    y = func(x)
    print("".join(y))
