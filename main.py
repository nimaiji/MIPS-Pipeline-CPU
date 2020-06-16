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
import CPU
import opcodes
# pc = ProgramCounter.ProgramCounter()
# hd = Hazards.HazardDetection()
# im = Memory.InstructionMemory('instruction.txt')
# dm = Memory.DataMemory(0)
# ifid = Pipe.IFID()
# idex = Pipe.IDEX()
# exmem = Pipe.EXMEM()
# memwb = Pipe.MEMWB()
# cu = ControlUnit.MainControl()
# rf = RegisterFile.RegisterFile()
# alu = ALU.ALU()
# alu_control = ALU.ALUContorl()
# fu = Hazards.ForwardingUnit()
#
#
# def update():
#     new_instruction = im.update(pc.addr)
#     if pc.addr.intformat == Address.Address32(0).intformat:
#         ifidins = new_instruction
#     else:
#         ifidins = ifid.instruction
#
#     print(ifidins)
#     cu.update(ifidins.opcode)
#     mux = CPU.MUX()
#     wdata = mux.update([memwb.rdata, memwb.result], memwb.RegWrite)
#     print(wdata)
#     print(memwb.result)
#     dm.update(exmem.result, exmem.wdata, exmem.MemWrite, exmem.MemRead)
#     if type(ifidins) == Format.RFormat:
#         rf.update(ifidins.rs, ifidins.rt, memwb.rd, wdata)
#     elif type(ifidins) == Format.IFormat:
#         rf.update(ifidins.rs, ifidins.rt, 0, 0)
#
#     fu.update(idex.rs, idex.rt, exmem.rd, memwb.rd, exmem.RegWrite, memwb.RegWrite)
#     alu_control.update(idex.signextended[-6::], idex.aluop)
#     print('#', idex.signextended[-6::], idex.aluop)
#     alu_in1 = mux.update([idex.r1, wdata, exmem.result], fu.fa)
#     alu_in2 = mux.update([idex.r2, wdata, exmem.result], fu.fb)
#
#     alu.update(alu_in1, alu_in2, alu_control.aluc)
#     rtorrd = mux.update([idex.rt, idex.rd], idex.RegDst)
#     memwb.update(dm.output, exmem.result, exmem.rd, exmem.MemtoReg, exmem.RegWrite)
#     if cu.EXFlush:
#         exmem.zerocontrol()
#     else:
#         exmem.update(alu.result, wdata, rtorrd, idex.MemtoReg, idex.RegWrite, idex.MemWrite)
#     signextended = alu.signextend(ifidins.bits[-15::])
#
#     se = '0' * 32
#     if alu.isequal(rf.r1, rf.r2) and ifidins.opcode == opcodes.BEQ:
#         se = Address.Address32(signextended)
#         # se = Address.Address32(se.intformat * 4)
#         new_pc = se + Address.Address32(ifid.pc)
#     if hd.cmuxselect or cu.IDFlush:
#         idex.zerocontrol()
#     else:
#         idex.update(ifid.pc, ifidins.rs, ifidins.rt, ifidins.rd, rf.r1, rf.r2, signextended, cu.aluop, cu.RegDst,
#                     cu.MemWrtie, cu.MemRead, cu.MemtoReg, cu.RegWrite)
#     ifid.update(pc.addr, new_instruction, cu.IFFlush, hd.IFIDWrtie)
#     print(rf.rs.addr)
#     print(rf.rt.addr)
#     print(rf.rd.addr)
#     pc.nextinstruction(hd.PCWrite, cu.PCSrc, new_pc, 0)
#     print(registers.REGISTER_FILE)
#
#
# timer = multitimer.MultiTimer(1, update)
# timer.start()
#



mips = CPU.MIPS('instruction.txt')

# c = Clock.Clock(1)