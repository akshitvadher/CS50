for i in range(0, n, 1):
    for j in range(0, n+i+3, 1):
        if (j ==  n or j  == n+1 or i+j < n-1):
            print(" " ,end="")
        else:
            print("#" ,end="")