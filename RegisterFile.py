import registers
import Address


class Register:

    def __init__(self, addr):
        self.addr = Address.AddressN(addr, len(addr))
        self.data = registers.REGISTER_FILE[self.addr.intformat]

    def changedata(self, data):
        registers.REGISTER_FILE.update({self.addr.intformat, data})


class RegisterFile:
    def __init__(self):
        self.rs = 0
        self.rt = 0
        self.rd = 0
        self.data = 0
        self.r1 = 0
        self.r2 = 0

    def update(self, rs, rt, rd, data):
        self.rs = Register(rs)
        self.rt = Register(rt)
        self.rd = Register(rd)
        self.data = Register(data)
        self.r1 = 0
        self.r2 = 0
