import opcodes

class MainControl:

    def __init__(self):
        self.PCSrc = '00'
        self.RegDst = 0
        self.ALUSrc = 0
        self.MemtoReg = 0
        self.RegWrite = 0
        self.MemRead = 0
        self.MemWrite = 0
        self.Branch = 0
        self.Jump = 0
        self.IFFlush = 0
        self.IDFlush = 0
        self.EXFlush = 0
        self.aluop = ''


    def update(self, opcode):
        self.PCSrc = '00'
        if opcode == opcodes.RFORMAT:
            self.PCSrc = '00'
            self.RegDst = 1
            self.ALUSrc = 0
            self.MemtoReg = 0
            self.RegWrite = 1
            self.MemRead = 0
            self.MemWrite = 0
            self.Jump = 0
            self.aluop = '1x'


        elif opcode == opcodes.LW:
            self.PCSrc = '00'
            self.RegDst = 0
            self.ALUSrc = 1
            self.MemtoReg = 1
            self.RegWrite = 1
            self.MemRead = 1
            self.MemWrite = 0
            self.Branch = 0
            self.Jump = 0
            self.aluop = '00'

        elif opcode == opcodes.SW:
            self.PCSrc = '00'
            self.ALUSrc = 1
            self.RegWrite = 0
            self.MemRead = 0
            self.MemWrite = 1
            self.Jump = 0
            self.aluop = '00'

        elif opcode == opcodes.BEQ:
            self.PCSrc = '10'
            self.ALUSrc = 0
            self.RegWrite = 0
            self.MemRead = 0
            self.MemWrite = 0
            self.IFFlush = 1
            self.Jump = 0
            self.aluop = 'x1'

        elif opcode == opcodes.SLT:
            self.PCSrc = '00'
            self.RegDst = 1
            self.ALUSrc = 0
            self.MemtoReg = 0
            self.RegWrite = 1
            self.MemRead = 0
            self.MemWrite = 0
            self.Jump = 0
            self.aluop = '1x'

        elif opcode == opcodes.J:
            self.PCSrc = '10'
            self.RegWrite = 0
            self.MemRead = 0
            self.MemWrite = 0
            self.Branch = 0
            self.Jump = 1

