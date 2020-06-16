import Address


class ProgramCounter:

    def __init__(self):
        self.addr = Address.Address32(0)

    def nextinstruction(self, PCWrite, PCSrc,new_pc,EPC):
        if PCWrite == 0 and PCSrc == '00':
            self.addr += 1
        elif PCSrc == '10':
            self.addr = new_pc

    def __str__(self):
        return str(self.addr)
