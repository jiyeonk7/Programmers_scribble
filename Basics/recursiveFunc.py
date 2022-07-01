def recursive_function(i):
    if i == 100:
        return
    print(i, "to", i+1)
    recursive_function(i+1)
    print("end", i)

recursive_function(1)