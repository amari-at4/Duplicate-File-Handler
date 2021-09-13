# use the function blackbox(lst) that is already defined
my_list = []
returned_list = blackbox(my_list)
if id(my_list) == id(returned_list):
    print("modifies")
else:
    print("new")
