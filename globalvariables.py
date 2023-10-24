x = "awesome"


def myfunc():
    x = "fantastic"
    print("python is " + x)


myfunc()
print("Python is " + x)


# global variables (use global keyword if you want to change a global variable inside a function)

def myfunc():
    global x
    x = "fantastic"
    print(f"python is {x}")


myfunc()
print("python is " + x)

x = "awesome"


def myfunc():
    global x
    x = "fantastic"
    print(f"python is {x}")


myfunc()
print("python is " + x)
