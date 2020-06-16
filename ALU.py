class ALUContorl:

    def __init__(self):
        self.funct = 0
        self.aluop = 'xxx'
        self.aluc = 0

    def update(self, funct, aluop):
        self.funct = funct
        self.aluop = aluop
        self.aluc = 'xxx'
        if aluop == '00' or (aluop[0] == '1' and funct == '100000'):  # add
            self.aluc = '010'
        elif aluop[1] == '1' or (aluop[0] == '1' and funct == '100010'):
            self.aluc = '110'
        elif aluop[0] == '1' and funct == '100100':  # and
            self.aluc = '000'
        elif aluop[0] == '1' and funct == '100101':  # or
            self.aluc = '001'
        elif aluop[0] == '1' and funct == '101010':  # slt
            self.aluc = '111'


class ALU:

    def __init__(self):
        self.input1 = 0
        self.input2 = 0
        self.result = 0
        self.zero = 0

    def update(self, in1, in2, aluc):
        self.input1 = in1
        self.input2 = in2
        self.result = 0
        self.zero = 0

        if aluc == '010':  # addi, lw, sw #add
            self.result = in1 + in2
        elif aluc == '110':  # beq, bne #sub
            self.result = in1 - in2
        elif aluc == '000':  # and
            self.result = in1 & in2
        elif aluc == '001':  # or
            self.result = in1 | in2
        elif aluc == '111':  # slt
            self.result = in1 - in2

        if self.result == 0:
            self.zero = 1

        print(in1, in2, self.result, aluc)

    def signextend(self, offset):
        if len(offset) < 32:
            base = '0' * (32 - len(offset)) + offset
        return base

    def adder(self, in1, in2):  # for better simulation
        return in1 + in2

    def shiftleft(self, data, amount):  # for better simulation
        return data << amount

    def isequal(self, in1, in2):
        return in1 == in2
