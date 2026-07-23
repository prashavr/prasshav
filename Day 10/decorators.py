









def into(a):
    print("Performing arithmetic Operations.")
    a()    #add()
    
    @into
    def add():
        print("Sum:", 5 + 10)