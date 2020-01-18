class Format:

    def __init__(self, opcode):
        self.opdcode = opcode



class RFormat(Format):

    def __init__(self,opcode, rs, rt, rd, shamt, funct):
        super().__init__(opcode)
        self.rs = rs
        self.rt = rt
        self.rd = rd
        self.shamt = shamt
        self.funct = funct


    def __str__(self):
        return 'R' + self.opdcode + ':' + self.funct


class IFormat(Format):

    def __init__(self, opcode, rs, rt, const):
        super().__init__(opcode)
        self.rs = rs
        self.rt = rt
        self.const = const

    def __str__(self):
        return 'I' + self.opdcode

class JFormat(Format):

    def __init__(self, opcode, address):
        super().__init__(opcode)
        self.address = address



    def __str__(self):
        return 'J' + self.opdcode
