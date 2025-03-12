def bubble_sort(lst, key):
    k = False
    while not k:
        k = True
        for i in range(0, len(lst)-1):
            if key(lst[i]) > key(lst[i+1]):
                t = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = t
                k = False
    return lst

def search(lst, key):
    k = []
    for i in lst:
        if key(i):
            k.append(i)
    return k

def combine(lst, k):

    t = len(lst)
    rez = []
    def backtrack(start, comb):
        if len(comb) == k:
            rez.append(comb.copy())
            return

        for i in range(start, t):
            comb.append(lst[i])
            backtrack(i+1, comb)
            comb.pop()
    backtrack(0, [])
    return rez





