import uuid

def create():
    i = str(uuid.uuid1())
    return i

if __name__ == '__main__':
    create()