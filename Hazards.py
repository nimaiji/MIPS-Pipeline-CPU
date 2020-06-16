import RegisterFile
import registers


class ForwardingUnit:

    def __init__(self):
        self.idexrs = 0
        self.idexrt = 0
        self.exmemRegWrite = 0
        self.exmemrd = 0
        self.memwbRegWrite = 0
        self.memwbrd = 0
        self.fa = '00'
        self.fb = '00'

    def update(self, idexrs, idexrt, exmemrd, memwbrd, exmemRegWrite, memwbRegWrite):
        self.idexrs = idexrs
        self.idexrt = idexrt
        self.exmemrd = exmemrd
        self.memwbrd = memwbrd
        self.exmemRegWrite = exmemRegWrite
        self.memwbRegWrite = memwbRegWrite
        self.fa = '00'
        self.fb = '00'
        if exmemRegWrite and (self.exmemrd != registers.REGISTER_FILE[0]) and (self.exmemrd != self.idexrs):
            self.fa = '10'
        elif exmemRegWrite and (self.exmemrd != registers.REGISTER_FILE[0]) and (self.exmemrd != self.idexrt):
            self.fb = '10'
        elif memwbRegWrite and (self.memwbrd != registers.REGISTER_FILE[0]) and (self.memwbrd != self.idexrs) and \
                not (exmemRegWrite and (self.exmemrd != registers.REGISTER_FILE[0]) and (self.exmemrd != self.idexrs)):
            self.fa = '01'
        elif memwbRegWrite and (self.memwbrd != registers.REGISTER_FILE[0]) and (self.memwbrd != self.idexrt) and \
                not (exmemRegWrite and (self.exmemrd != registers.REGISTER_FILE[0]) and (self.exmemrd != self.idexrt)):
            self.fb = '01'


class HazardDetection:

    def __init__(self):
        self.idexrt = 0
        self.ifidrt = 0
        self.ifidrd = 0
        self.idexMemRead = 0
        self.PCWrite = 0
        self.IFIDWrtie = 0
        self.cmuxselect = 0


    def update(self, idexrt, ifidrd, ifidrt, idexMemRead):
        self.idexrt = idexrt
        self.ifidrd = ifidrd
        self.iridrt = ifidrt
        self.idexMemRead = idexMemRead
        self.PCWrite = 0
        self.IFIDWrtie = 0
        self.cmuxselect = 0

        #Todo: write bubble and signals
        if idexMemRead and (self.idexrt == self.ifidrs) and (self.idexrt == ifidrt):
            self.PCWrite = 1
            self.IFIDWrtie = 1
            self.cmuxselect = 1

