def exceptionFunction(a,b):
    try:
        print(a/b);
    except Exception:
        print("Exception")
    finally:
        print("execute no matter what")


exceptionFunction(3,0)
exceptionFunction(3,2)