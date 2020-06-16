import Format
import Address


class IFID:

    def __init__(self):
        self.pc = '0' * 32
        self.instruction = 0
        self.IFFlush = 0
        self.IFWrite = 0

    def update(self, pc, instruction, IFFlush, IFWrtie):
        self.pc = pc
        self.instruction = instruction
        self.IFFlush = IFFlush
        self.IFWrite = IFWrtie
        if IFFlush == 1 and IFWrtie == 1:
            self.flush()

    def flush(self):
        self.pc = Address.Address32(0)
        self.instruction = Format.RFormat('0' * 6, '0' * 5, '0' * 5, '0' * 5, '0' * 5, '0' * 6)
        self.IFFlush = 0


class IDEX:

    def __init__(self):
        self.pc = 0
        self.r1 = 0
        self.r2 = 0
        self.rs = 0
        self.rt = 0
        self.rd = 0
        self.signextended = '0' * 32
        # EX control signals
        self.aluop = 'x0x'
        self.RegDst = 0
        # Mem control signals
        self.MemWrite = 0
        self.MemRead = 0
        # WB control signals
        self.MemtoReg = 0
        self.RegWrite = 0

    def update(self, pc, ifidrs, ifidrt, ifidrd, r1, r2, signextended, aluop, RegDst, MemWrite, MemRead, MemtoReg,
               RegWrite):
        self.pc = pc
        self.rs = ifidrs
        self.rt = ifidrt
        self.rd = ifidrd
        self.r1 = r1
        self.r2 = r2
        self.signextended = signextended
        self.aluop = aluop
        self.RegDst = RegDst
        self.MemWrite = MemWrite
        self.MemRead = MemRead
        self.MemtoReg = MemtoReg
        self.RegWrite = RegWrite

    def zerocontrol(self):
        # EX control signals
        self.aluop = 'x0x'
        self.RegDst = 0
        # Mem control signals
        self.MemWrite = 0
        self.MemRead = 0
        # WB control signals
        self.MemtoReg = 0
        self.RegWrite = 0


class EXMEM:

    def __init__(self):
        self.result = 0
        self.wdata = 0
        self.rd = 0
        # WB control signals
        self.MemtoReg = 0
        self.RegWrite = 0
        # Mem control signals
        self.MemWrite = 0
        self.MemRead = 0

    def update(self, result, wdata, exmemrd, MemtoReg, RegWrite, MemWrite):
        self.result = result
        self.wdata = wdata
        self.rd = exmemrd
        self.MemtoReg = MemtoReg
        self.RegWrite = RegWrite
        self.MemWrite = MemWrite

    def zerocontrol(self):
        # WB control signals
        self.MemtoReg = 0
        self.RegWrite = 0
        # Mem control signals
        self.MemWrite = 0
        self.MemRead = 0


class MEMWB:

    def __init__(self):
        self.rdata = 0
        self.result = 0
        self.rd = 0
        # WB control signals
        self.MemtoReg = 0
        self.RegWrite = 0

    def update(self, rdata, result, memwbrd, MemtoReg, RegWrite):
        self.rdata = rdata
        self.result = result
        self.rd = memwbrd
        self.MemtoReg = MemtoReg
        self.RegWrite = RegWrite

    def zerocontrol(self):
        # WB control signals
        self.MemtoReg = 0
        self.RegWrite = 0
