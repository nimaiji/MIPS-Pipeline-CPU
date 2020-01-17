import Address

class ProgramCounter:

    def __init__(self):
        self.addr = Address.Address32(0)

    def nextinstruction(self, offset):
        self.addr += offset

    def __str__(self):
        return str(self.addr)


