class Format:

    def __init__(self, opcode):
        self.opcode = opcode



class RFormat(Format):

    def __init__(self,opcode, rs, rt, rd, shamt, funct):
        super().__init__(opcode)
        self.rs = rs
        self.rt = rt
        self.rd = rd
        self.shamt = shamt
        self.funct = funct
        self.bits = self.opcode + self.rs + self.rt + self.rd + self.shamt + self.funct


    def __str__(self):
        return 'R' + self.opcode + ':' + self.funct

class IFormat(Format):

    def __init__(self, opcode, rs, rt, const):
        super().__init__(opcode)
        self.rs = rs
        self.rt = rt
        self.const = const
        self.bits = self.opcode + self.rs + self.rt + self.const

    def __str__(self):
        return 'I' + self.opcode

class JFormat(Format):

    def __init__(self, opcode, address):
        super().__init__(opcode)
        self.address = address
        self.bits = self.opcode + self.address


    def __str__(self):
        return 'J' + self.opcode
