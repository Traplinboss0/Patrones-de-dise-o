
def singlenton(cls):

    instances = dict()

    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)

        return instances[cls]


    return wrap


@singlenton
class User(object):
    def __init__(self, username):
        self.username = username


if __name__ == '__main__':

    user1 = User('Sol')
    user2 = User('Luna')

    print(user1 is user2)




