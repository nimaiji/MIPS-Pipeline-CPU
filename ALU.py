class ALUContorl:

    def __init__(self):
        self.funct = 0
        self.aluop = 0
        self.output = 0

    def update(self, funct, aluop):
        self.funct = funct
        self.aluop = aluop
        self.output = 0
        if aluop == 00 or (aluop[0] == '1' and funct[2:6] == '0000'):  # add
            self.output = '010'
        elif aluop[1] == '1' or (aluop[0] == '1' and funct[2:6] == '0010'):
            self.output = '110'
        elif aluop[0] == '1' and funct[2:6] == '0100':  # and
            self.output = '000'
        elif aluop[0] == '1' and funct[2:6] == '0101':  # or
            self.output = '001'
        elif aluop[0] == '1' and funct[2:6] == '1010':  # slt
            self.output = '111'


class ALU:

    def __init__(self):
        self.input1 = 0
        self.input2 = 0
        self.output = 0
        self.zero = 0

    def update(self, in1, in2, aluc):
        self.input1 = in1
        self.input2 = in2
        self.output = 0
        self.zero = 0

        if aluc == '010':  # addi, lw, sw #add
            self.output = in1 + in2
        elif aluc == '110':  # beq, bne #sub
            self.output = in1 - in2
        elif aluc == '000':  # and
            self.output = in1 & in2
        elif aluc == '001':  # or
            self.output = in1 | in2
        elif aluc == '111':  # slt
            self.output = in1 - in2

        if self.output == 0:
            self.zero = 1

    def signextend(self, offset):
        if len(offset) < 32:
            base = '0' * (32 - len(offset)) + offset
        return base

    def adder(self, in1, in2):  # for better simulation
        return in1 + in2

    def shiftleft(self, data, amount):  # for better simulation
        return data << amount
