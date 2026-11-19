def outer():
    status = "pending"
    
    def inner():
        nonlocal status
        status ="completed"
        inner()
        print("final status:", status)
        outer()
        