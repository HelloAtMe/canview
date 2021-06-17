# -*- coding: utf-8 -*-
"""
@ File         : dbc_handle.py
@ Author       : Wcy
@ Contact      : 
@ Date         : 2021-06-16 17:41:46
@ Description  : 
"""

import re


def parsedbc(dbcfile):
    # SG_ SignalName : StartBit|SignalSize@ByteOrder ValueType (Factor,Offset) [Min|Max] Unit Receiver

    patternMessage = re.compile(r'BO_\s*(\d+)\s*\w+\s*:\s*\d{1}\s*.*')
    patternSignal = re.compile(r'SG_\s*\w+\s*:\s*(\d+)\|(\d+)@[0|1][+|-]\s*\(([\d\.]+),([\d\.]+)\)\s*\[([\d\.]+)\|([\d\.]+)\]\s*“.*”\s*.*')

    MsgsAttributeDict = {}

    with open(dbcfile, 'r', encoding='utf-8') as f:
        dbclines = f.readlines()
        dbclines = [l.strip() for l in dbclines]

        MsgId = ''
        for line in dbclines:
            SignalsAttributeDict = {}

            MsgIdStrLst = patternMessage.findall(line)
            if MsgIdStrLst:
                if SignalsAttributeDict:
                    MsgsAttributeDict.update({MsgId:SignalsAttributeDict})
                MsgId = '{:0>3X}'.format(int(MsgIdStrLst[0]))
                SignalsAttributeDict = {}
            else:
                SignalAttributeStrLst = patternSignal.findall(line)
                if SignalAttributeStrLst:
                    if MsgId:
                        varName = SignalAttributeStrLst[0]
                        start = int(SignalAttributeStrLst[1])
                        length = int(SignalAttributeStrLst[2])
                        factor = formatString2Number(SignalAttributeStrLst[3])
                        offset = formatString2Number(SignalAttributeStrLst[4])
                        min = formatString2Number(SignalAttributeStrLst[5])
                        max = formatString2Number(SignalAttributeStrLst[6])

                        SignalsAttributeDict.update(
                            {
                                varName : {
                                    'start' : start,
                                    'length' : length,
                                    'factor' : factor,
                                    'offset' : offset,
                                    'min' : min,
                                    'max' : max
                                }
                            }
                        )
                        
        MsgsAttributeDict.update({MsgId:SignalsAttributeDict})


def formatString2Number(numStr):
    if '.' in numStr:
        return float(numStr)
    else:
        return int(numStr)


if __name__ == '__main__':
    patternMessage = re.compile(r'BO_\s*(\d+)\s*\w+\s*:\s*\d{1}\s*.*')
    patternSignal = re.compile(r'SG_\s*(\w+)\s*:\s*(\d+)\|(\d+)@[0|1][+|-]\s*\(([\d\.]+),([\d\.]+)\)\s*\[([\d\.]+)\|([\d\.]+)\]\s*“.*”\s*.*')

    p1 = 'BO_ 996 HUD_1_B: 8 HUD'
    p2 = 'SG_ HUD_BrightnessLv : 15|4@0+ (0.1,12.1) [0|15] “lv” ACU,AVNT'

    print(re.findall(patternMessage, p1))
    print(re.findall(patternSignal, p2))
    print(patternMessage.findall(p1))
    print(patternSignal.findall(p2))
