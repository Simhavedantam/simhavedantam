HELLO_WORLD = "Hello World"


# class PrintObject:
#     def __init__(self, statement):
#         self.statement = statement
#
#     def print_object(self):
#         print(self.statement)


class PrintObject:
    def __init__(self, statement):
        self.statement = statement

    def print_object(self):
        return self.statement


hello_world = PrintObject(HELLO_WORLD)

print(hello_world.print_object())
