def array_left_rotation(a, n, k):
    temp=list(a[:k])
    ini=list(a[k:])
    final=ini+temp
    return final

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
