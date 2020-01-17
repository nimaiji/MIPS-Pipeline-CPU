import numpy as np


class AddressN:
    def __init__(self, addr, n):
        tag = '{:0' + str(n) + 'b}'
        if type(addr) == int:
            self.intformat = addr
            self.bitformat = tag.format(np.uint32(addr))
        elif type(addr) == str:
            self.intformat = self.bitstoint(addr)
            self.bitformat = tag.format(np.uint32(self.intformat))

    def bitstoint(self, bits):
        eq = 0
        m = 1
        for bit in bits[::-1]:
            b = int(bit)
            eq += b * m
            m *= 2
        return eq

    def __add__(self, other):
        if type(other) == int:
            return AddressN(self.intformat + other)
        elif type(other) == AddressN:
            return AddressN(self.intformat + AddressN.intformat)

    def __str__(self):
        return str(self.intformat) + ':' + self.bitformat


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

    def __add__(self, other):
        if type(other) == int:
            return Address32(self.intformat + other)
        elif type(other) == Address32:
            return Address32(self.intformat + Address32.intformat)

    def __str__(self):
        return str(self.intformat) + ':' + self.bitformat
