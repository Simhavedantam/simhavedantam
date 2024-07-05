from abc import ABC, abstractmethod

PRINT_STATEMENT = "Hello! This is print statement"
SCAN_STATEMENT = "Enter The Value:"


# class PrintClass(ABC):
#
#     @abstractmethod
#     def print_data(self):
#         pass
#
#
# class ScanClass(ABC):
#
#     @abstractmethod
#     def scan_data(self):
#         pass
#
#
# class MyClass(PrintClass, ScanClass):
#     def __init__(self, data):
#         self.data = data
#
#     def print_data(self):
#         return self.data
#
#     def scan_data(self):
#         return str(input(self.data))
#
#
# printer = MyClass(PRINT_STATEMENT)
# scanner = MyClass(SCAN_STATEMENT)
#
# print(printer.print_data())
# print(scanner.scan_data())


class AbstractClass(ABC):

    @abstractmethod
    def abstract_method(self):
        pass


class PrinterClass(AbstractClass):
    def __init__(self, data):
        self.data = data

    def abstract_method(self):
        return self.data


class ScannerClass(AbstractClass):
    def __init__(self, data):
        self.data = data

    def abstract_method(self):
        return input(self.data)


printer = PrinterClass(PRINT_STATEMENT)
scanner = ScannerClass(SCAN_STATEMENT)

print(scanner.abstract_method())
