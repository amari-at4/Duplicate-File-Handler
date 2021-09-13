def check(first_object, second_object):
    if id(first_object) == id(second_object):
        print("True")
    else:
        print("False")
