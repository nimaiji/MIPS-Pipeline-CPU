import registers
import Address


class Register:

    def __init__(self, addr):
        self.addr = Address.Address32(addr)
        self.data = registers.REGISTER_FILE[self.addr.intformat]

    def changedata(self, data):
        registers.REGISTER_FILE.update({self.addr.intformat: data})


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
        self.data = data
        self.r1 = self.rs.data
        self.r2 = self.rt.data
        self.rd.changedata(data)
