# Not too many method into a interface 
# This Machine interface is too large and might not be useful and
# versatile
class Machine:
    def print(self, document):
        raise NotImplementedError
    def fax(self, document):
        raise NotImplementedError
    def scan(self, document):
        raise NotImplementedError

class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass
    def fax(self, document):
        pass
    def scan(self, document):
        pass

class OldFashionedPrinter(Machine):
    def print(self, document):
        # This print method is fine but it doesnt make sense for 
        # an old printer to fax and scan
        pass
    def fax(self, document):
        pass # This is noop 
    def scan(self, document):
        # Example of one of the solution but not ideal for a large 
        # application
        raise NotImplementedError("Printer cannot scan!")

# Ideal solution 
class Printer:
    @abstractmethod
    def print(self, document):
        pass 

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass 

class MyPrinter(Printer):
    def print(self, document):
        print(document)

class Photocopier(Printer, Scanner):
    def print(self, document):
        pass 
    def scan(self, document):
        pass
# example of interface that contain big abstract
class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class MultiFunctionMachine(MultiFunctionDevice):
    # A decorator to combine both printer and scanner
    def __init__(self, printer, scanner) -> None:
        self.scanner = scanner
        self.printter = printer

    def print(self, document):
        self.printter.print(document)

    def scan(self, document):
        self.scanner.scanner(document)