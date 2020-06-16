import threading
import numpy as np
import registers
import Address
import RegisterFile
import ALU
import Clock
import Hazards
import ProgramCounter
import Memory
import Pipe
import multitimer
import ControlUnit
import Format
import opcodes
import matplotlib.pyplot as plt


class MUX:

    def __init__(self):
        self.inputs = []
        self.select = 0

    def update(self, inputs, select):
        self.inputs = inputs
        self.select = select
        if type(select) == str:
            select = self.bitstoint(select)
        return inputs[select]

    def bitstoint(self, bits):
        eq = 0
        m = 1
        for bit in bits[::-1]:
            b = int(bit)
            eq += b * m
            m *= 2
        return eq


class MIPS:

    def __init__(self, path):
        self.pc = ProgramCounter.ProgramCounter()
        self.hd = Hazards.HazardDetection()
        self.im = Memory.InstructionMemory(path)
        self.dm = Memory.DataMemory(0)
        self.ifid = Pipe.IFID()
        self.idex = Pipe.IDEX()
        self.exmem = Pipe.EXMEM()
        self.memwb = Pipe.MEMWB()
        self.cu = ControlUnit.MainControl()
        self.rf = RegisterFile.RegisterFile()
        self.alu = ALU.ALU()
        self.alu_control = ALU.ALUContorl()
        self.fu = Hazards.ForwardingUnit()
        self.cycle = 0
        self.ALUSrcH = []
        timer = multitimer.MultiTimer(1, self.update)
        timer.start()
        if self.cycle == len(self.im.instructions_in_array):
            timer.stop()
            self.ui()

    def update(self):
        new_instruction = self.im.update(self.pc.addr)
        if self.pc.addr.intformat == Address.Address32(0).intformat:
            ifidins = new_instruction
        else:
            ifidins = self.ifid.instruction

        print(new_instruction)
        self.cu.update(ifidins.opcode)
        mux = MUX()
        wdata = mux.update([self.memwb.rdata, self.memwb.result], self.memwb.RegWrite)
        # print(wdata)
        # print(self.memwb.result)
        self.dm.update(self.exmem.result, self.exmem.wdata, self.exmem.MemWrite, self.exmem.MemRead)
        if type(ifidins) == Format.RFormat:
            self.rf.update(ifidins.rs, ifidins.rt, self.memwb.rd, wdata)
        elif type(ifidins) == Format.IFormat:
            self.rf.update(ifidins.rs, ifidins.rt, 0, 0)

        self.fu.update(self.idex.rs, self.idex.rt, self.exmem.rd, self.memwb.rd, self.exmem.RegWrite,
                       self.memwb.RegWrite)
        self.alu_control.update(self.idex.signextended[-6::], self.idex.aluop)
        # print('#', self.idex.signextended[-6::], self.idex.aluop)
        alu_in1 = mux.update([self.idex.r1, wdata, self.exmem.result], self.fu.fa)
        alu_in2 = mux.update([self.idex.r2, wdata, self.exmem.result], self.fu.fb)

        self.alu.update(alu_in1, alu_in2, self.alu_control.aluc)
        rtorrd = mux.update([self.idex.rt, self.idex.rd], self.idex.RegDst)
        self.memwb.update(self.dm.output, self.exmem.result, self.exmem.rd, self.exmem.MemtoReg, self.exmem.RegWrite)
        if self.cu.EXFlush:
            self.exmem.zerocontrol()
        else:
            self.exmem.update(self.alu.result, wdata, rtorrd, self.idex.MemtoReg, self.idex.RegWrite,
                              self.idex.MemWrite)
        signextended = self.alu.signextend(ifidins.bits[-15::])

        se = '0' * 32
        new_pc = 0
        if self.alu.isequal(self.rf.r1, self.rf.r2) and ifidins.opcode == opcodes.BEQ:
            se = Address.Address32(signextended)
            # se = Address.Address32(se.intformat * 4)
            new_pc = se + self.ifid.pc
            self.cu.IDFlush = 1
            self.cu.IFFlush = 1

        if self.hd.cmuxselect or self.cu.IDFlush:
            self.idex.zerocontrol()
        else:
            self.idex.update(self.ifid.pc, ifidins.rs, ifidins.rt, ifidins.rd, self.rf.r1, self.rf.r2, signextended,
                             self.cu.aluop, self.cu.RegDst,
                             self.cu.MemWrite, self.cu.MemRead, self.cu.MemtoReg, self.cu.RegWrite)

        if self.cu.IFFlush == 1 or self.hd.IFIDWrtie == 1:
            self.ifid.flush()
        else:
            self.ifid.update(self.pc.addr, new_instruction, self.cu.IFFlush, self.hd.IFIDWrtie)
        self.pc.nextinstruction(self.hd.PCWrite, self.cu.PCSrc, new_pc, 0)
        print(registers.REGISTER_FILE)
        self.cycle += 1
        self.ALUSrcH.append(self.cu.ALUSrc)


    def ui(self):
        plt.figure(figsize=(9, 4))
        x = np.arange(5)
        plt.step(x, np.heaviside(self.ALUSrcH,0), label='pre (default)')
        plt.plot(x, np.heaviside(self.ALUSrcH,0), 'C0o', alpha=1)
        plt.legend(title='Parameter where:')
        plt.show()