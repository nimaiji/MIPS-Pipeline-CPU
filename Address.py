import numpy as np


class Address32:

    def __init__(self, addr):
        if type(addr) == int:
            self.intformat = addr
            self.bitformat = '{:032b}'.format(np.uint32(addr))
        # elif len(addr) != 32:
        #     raise Exception('Your address should be 32 bits', addr)
        elif type(addr) == str:
            self.intformat = self.bitstoint(addr)
            self.bitformat = '{:032b}'.format(np.uint32(self.intformat))

    def bitstoint(self, bits):
        eq = 0
        m = 1
        for bit in bits[::-1]:
            b = int(bit)
            eq += b * m
            m *= 2
        return eq

    def __str__(self):
        return str(self.intformat) + ':' + self.bitformat
