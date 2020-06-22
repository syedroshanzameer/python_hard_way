def print_two(*args):
    arg1,arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_2(arg1,arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_none():
    print("I got nothing")


print_two("Roshan", "Syed")
print_2("roshan","Syed")
print_none()


