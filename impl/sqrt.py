
# coding: utf-8

# In[ ]:

#1
from __future__ import print_function
from pynq import Overlay
from pynq import MMIO
import numpy as np
import struct
import binascii
import cmath
import random
import matplotlib.pyplot as plt
import sys

sys.path.append('/home/xilinx')


#if __name__ == "__main__":
#2
print("Entry:", sys.argv[0])
print("System argument(s):", len(sys.argv))

print("Start of \"" + sys.argv[0] + "\"")

ol = Overlay("/home/xilinx/IPBitFile/Yu_Chi/sqrt.bit")
#3
regIP = ol.top_process_magnitude_0
#4
#r=r[2:]
error_mag=np.zeros(3)

#5
print("============================")

    #Converting input to bytes to be sent to FPGA
#x=(struct.unpack('<I', struct.pack('<f', 4))[0])
#y=(struct.unpack('<I', struct.pack('<f', 1))[0])
regIP.write(0x400, 4)
regIP.write(0x800, 3)
c = regIP.read(0xc00)
    

print(c)

    
print("Exit process")

