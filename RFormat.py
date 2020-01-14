from Format import Format


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