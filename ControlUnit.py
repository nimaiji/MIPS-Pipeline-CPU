import opcodes

class MainControl:

    def __init__(self):
        self.RegDst = 0
        self.ALUSrc = 0
        self.MemtoReg = 0
        self.RegWrite = 0
        self.MemRead = 0
        self.MemWrtie = 0
        self.Branch = 0
        self.Jump = 0
        self.aluop = ''

    def update(self, opcode):

        if opcode == opcodes.RFORMAT:
            self.RegDst = 1
            self.ALUSrc = 0
            self.MemtoReg = 0
            self.RegWrite = 1
            self.MemRead = 0
            self.MemWrtie = 0
            self.Branch = 0
            self.Jump = 0
            self.aluop = '1x'
        elif opcode == opcodes.LW:
            self.RegDst = 0
            self.ALUSrc = 1
            self.MemtoReg = 1
            self.RegWrite = 1
            self.MemRead = 1
            self.MemWrtie = 0
            self.Branch = 0
            self.Jump = 0
            self.aluop = '00'
        elif opcode == opcodes.SW:
            self.ALUSrc = 1
            self.RegWrite = 0
            self.MemRead = 0
            self.MemWrtie = 1
            self.Branch = 0
            self.Jump = 0
            self.aluop = '00'
        elif opcode == opcodes.BEQ:
            self.ALUSrc = 0
            self.RegWrite = 0
            self.MemRead = 0
            self.MemWrtie = 0
            self.Branch = 1
            self.Jump = 0
            self.aluop = '01'
        elif opcode == opcodes.J:
            self.RegWrite = 0
            self.MemRead = 0
            self.MemWrtie = 0
            self.Branch = 0
            self.Jump = 1
