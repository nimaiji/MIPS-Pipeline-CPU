class ProgramCounter:

    def __init__(self):
        #should be 32 bit address
        self.index = 0

    def nextinstruction(self):
        self.index +=4


