def histogram(list):
    i = 0
    l = ''
    while i < len(list):
        l += '*' * list[i] + '\n'
        i += 1
    print(l)
histogram([1, 2, 3, 7])