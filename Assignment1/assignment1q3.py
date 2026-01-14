def safe_function(value, mylist=None):
    if mylist is None:
        mylist = []
    mylist.append(value)
    return mylist

# Test calls
print(safe_function(1))
print(safe_function(2))
