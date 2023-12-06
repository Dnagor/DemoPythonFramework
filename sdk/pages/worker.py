class Worker:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_worker(self):
        print("name: {}, age: {}".format(self.name, self.age))
