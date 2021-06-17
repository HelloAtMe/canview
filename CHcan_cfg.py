# -*- coding: utf-8 -*-
"""
@ File         : CHcan_cfg.py
@ Project      : 
@ Author       : 
@ Contact      : 
@ Date         : 2021-06-17 13:19:16
@ Description  : 
"""

SCROLLBAR_WIDTH = 21
STATUSBAR_HEIGHT = 0
PERIODIC_TIME   = 20

# Self configuration
# ================ Code Here ================ #
from can_driver import *

p_connectShow = {
    True:['已连接', 'light green'],
    False:['未连接', 'red']
}
p_CHANNELS = {
    'PCAN_USBBUS1':PCAN_USBBUS1,
    'PCAN_USBBUS2':PCAN_USBBUS2,
    'PCAN_USBBUS3':PCAN_USBBUS3,
    'PCAN_USBBUS4':PCAN_USBBUS4,
    'PCAN_USBBUS5':PCAN_USBBUS5,
    'PCAN_USBBUS6':PCAN_USBBUS6,
    'PCAN_USBBUS7':PCAN_USBBUS7,
    'PCAN_USBBUS8':PCAN_USBBUS8
}
p_BAUDRATES = {
    '1 MBit/sec':PCAN_BAUD_1M,
    '500 kBit/sec':PCAN_BAUD_500K
}
# ================ Code Here ================ #
