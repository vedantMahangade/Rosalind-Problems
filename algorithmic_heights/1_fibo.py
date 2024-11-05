def fibonaci(n):
    fiboarray = [1, 1]

    for i in range(2, n):
        fiboarray.append(0)
        ith_val = fiboarray[i-1]+fiboarray[i-2]
        fiboarray[i] = ith_val
    print(fiboarray[n-1])  


fibonaci(21)