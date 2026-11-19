def outer ():
    mode = "enclosing mode"
    def inner():
        mode = "local mode"
        print("inner function:", mode)
        inner()
        print("outer function:",mode)
        outer()
        