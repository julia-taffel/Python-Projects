def egzekutor(*args, **kwargs):
    for func in args:
        for x, y in kwargs.items():
            result = func(x, y)
            print(result)
            
egzekutor(lambda x,y:x+y, lambda x,y:y+x, a="b", b="c")