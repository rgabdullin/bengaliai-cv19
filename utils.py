import os

def mkdir(x):
    if not os.path.exists(x):
        os.mkdir(x)
    return x

def rmdir(x):
    if os.path.exists(x):
        if os.path.isdir(x):
            for file in os.listdir(x):
                item = os.path.join(x, file)
                if os.path.isdir(item):
                    rmdir(item)
                else:
                    os.remove(item)
            os.rmdir(x)
        else:
            os.remove(x)
    return x
