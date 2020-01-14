from Format import Format


class JFormat(Format):

    def __init__(self, opcode, address):
        super().__init__(opcode)
        self.address = address



    def __str__(self):
        return 'J' + self.opdcode
