def announce(f):
    def wrapper():
        print("the function is about to begin...")
        f()
        print("the function was performed")
    return wrapper  

@announce
def Hello():
    print("Hello, world!")

Hello()

