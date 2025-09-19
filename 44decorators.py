# def hello():
#     print("Hello world")


def greet(fx):
    def mfx(*args,**kwargs):
        print("Good morning")
        fx(*args,**kwargs)
        print("thanks for using this function")
    return mfx
        
@greet
def hello():
    print("Hello world ")

@greet      
def add(a,b):
    print(a+b) 

# @greet(hello)()
hello()

# @greet add(12,43)
add(12,43)