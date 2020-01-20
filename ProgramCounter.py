import Address


class ProgramCounter:

    def __init__(self):
        # Todo: control signal from hazard detection handling
        self.addr = Address.Address32(0)

    def nextinstruction(self, PCWrite, offset):
        if PCWrite == 0:
            self.addr += offset

    def __str__(self):
        return str(self.addr)
