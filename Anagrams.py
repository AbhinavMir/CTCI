def common(m,n):
    h=set(list(m))-set(list(b))
    str = ''.join(list(h))
    return str
    
def number_needed(a, b):
    g=len(common(a,b))
    k=len(a)+len(b)-g
    return k

a = input().strip()
b = input().strip()

print(number_needed(a, b))
