import opcodes
import Format
import Address


class DataMemory:

    def __init__(self, baseaddr):
        self.addr = 0
        self.wdata = 0
        self.baseaddr = Address.Address32(baseaddr)
        self.output = 0
        self.MEMORY = {}

    def update(self, addr, wdata, MemWrtie, MemRead):
        if MemWrtie == 1:
            self.write(addr, wdata)

        if MemRead == 1:
            self.read(addr)

    def write(self, addr, wdata):
        self.MEMORY[addr] = wdata

    def read(self, addr):
        self.output = self.MEMORY[addr]


class InstructionMemory:

    def __init__(self, path):
        self.path = path
        self.instructions_in_array = []
        self.parse()

    def parse(self):
        file = open(self.path, 'r')
        for line in file:
            line = line.rstrip('\n')
            if line[0:6] == '000000':
                self.instructions_in_array += [self.createRFormat(line)]
            elif line[0:6] == opcodes.BEQ or line[0:6] == opcodes.LW or line[0:6] == opcodes.SW:
                self.instructions_in_array += [self.createIFormat(line)]
            elif line[0:6] == opcodes.J:
                self.instructions_in_array += [self.createJFormat(line)]

    def update(self, addr):
        try:
            return self.instructions_in_array[addr.intformat]
        except:
            return Format.RFormat('0' * 6, '0' * 5, '0' * 5, '0' * 5, '0' * 5, '0' * 6)

    def createRFormat(self, instruction):
        i = Format.RFormat(instruction[0:6], instruction[6:11], instruction[11:16], instruction[16:21],
                           instruction[21:26], instruction[26:32])
        return i

    def createIFormat(self, instruction):
        i = Format.IFormat(instruction[0:6], instruction[6:11], instruction[11:16], instruction[16:32])
        return i

    def createJFormat(self, instruction):
        i = Format.JFormat(instruction[0:6], instruction[6:32])
        return i
