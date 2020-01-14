from Format import Format


class IFormat(Format):

    def __init__(self, opcode, rs, rt, const):
        super().__init__(opcode)
        self.rs = rs
        self.rt = rt
        self.const = const

    def __str__(self):
        return 'I' + self.opdcode