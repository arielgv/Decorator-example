#Example of a decorator execution in Python

def firstline(firstparameter):
    def secondline():
        firstparameter()
        print("Second line here")
    return secondline

@firstline
def firsttext():
    print("First line here")

firsttext()
