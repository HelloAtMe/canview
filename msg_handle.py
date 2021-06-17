# -*- coding: utf-8 -*-
'''
@ File         : msg_handle.py
@ Project      : 
@ Author       : Wcy
@ Contact      : 
@ Date         : 2021-06-11 12:18:44
@ Description  : 
'''

from CRC import CalcCRC_8B

'''
data type
varsAttribute => 
{
    key:{
        'start' : 0,
        'length' : 0,
        'factor' : 0,
        'offset' : 0,
        'max' : 0,
        'min' : 0
    }
}

varsValue =>
{
    key:value
}
'''
class Message(object):
    def __init__(self):
        self.id = 0
        self.data = [0]*8
        self.length = 0
        self.cycleTime = 0
        self.count = 0
        self.varsAttribute = {}
        self.varsValue = {}
    

    def updateCount(self):
        self.count += 1


    def set_data(self, data):
        for i, d in enumerate(data):
            self.data[i] = d
    

    def set_vars(self, varsAttribute):
        for k, v in varsAttribute.items():
            self.varsAttribute.update({k:v})
        self.parse_data()


    def modify_data(self, varName, varValue):
        ''' varsValue -> data '''
        dataSetStr = '0' * self.length * 8
        self.varsValue.update({varName:varValue})

        for k, v in self.varsAttribute.items():
            if k == varName:
                rData = 0
                vData = self.varsValue.get(k)
                start = v.get('start')
                length = v.get('length')
                factor = v.get('factor')
                offset = v.get('offset')
                min = v.get('min')
                max = v.get('max')
                if vData > max:
                    vData = max
                elif vData < min:
                    vData = min
                rData = vData * factor + offset
                dataSetStr = self.bit2data(dataSetStr, rData, start, length)
                break
            
        for i in range(self.length):
            self.data[i] = int(dataSetStr[(i*8):(i*8+8)], 2)


    def parse_data(self):
        ''' data -> varsValue '''
        dataSetStr = ''
        for i in range(self.length):
            dataSetStr += '{:0>8b}'.format(self.data[i])
        for k, v in self.varsAttribute.items():
            start = v.get('start')
            length = v.get('length')
            factor = v.get('factor')
            offset = v.get('offset')
            min = v.get('min')
            max = v.get('max')
            rData = (self.data2bit(dataSetStr, start, length) - offset) / factor
            if rData > max:
                rData = max
            elif rData < min:
                rData = min
            self.varsValue.update({k:rData})


    def bit2data(self, dataSetStr, rData, start, length):
        rdataCtrl = '{{:0>{0}b}}'.format(length)
        rdataStr = rdataCtrl.format(rData)
        _t = start / 8
        _m = start % 8
        _start = _t*8+(8-_m)

        for i in range(length):
            dataSetStr[_start-i] = rdataStr[length-i]
        
        return dataSetStr


    def data2bit(self, dataSetStr, start, length):
        rdataCtrl = '{{:0>{0}b}}'.format(length)
        rdataStr = rdataCtrl.format(0)
        _t = start / 8
        _m = start % 8
        _start = _t*8+(8-_m)

        for i in range(length):
            rdataStr[length-i] = dataSetStr[_start-i]

        return int(rdataStr,2)


class SMessage(Message):
    def __init__(self):
        self.aCount = 0
        self.tCount = 0
        self.pause = False
        self.aliveCount = False
        self.crc = False
        super().__init__()


    def updateAliveCount(self):
        if self.aliveCount:
            if self.aCount > 14:
                self.aCount = 0
            self.data[6] = (self.data[6] & 0xF0) + self.aCount
            self.aCount += 1
    

    def updateCRC(self):
        if self.crc:
            self.data[7] = CalcCRC_8B(self.data[:7])


    def checkTimeout(self):
        if self.cycleTime > 0:
            self.tCount += 1
            if self.tCount > self.cycleTime:
                self.tCount = 0
                return True
            else:
                return False
        else:
            return False

    # removed, add it to the main function.

    # def send(self, lock):
    #     lock.acquire()
    #     if self.length == 8:
    #         if self.aliveCount:
    #             if self.aCount > 14:
    #                 self.aCount = 0
    #             d6 = self.data[6]
    #             self.data[6] = (d6 & 0xF0) + self.aCount
    #             self.aCount += 1
    #         if self.crc:
    #             self.data[7] = CalcCRC_8B(self.data[:7])
    #     self.canMsg.ID = self.id
    #     self.canMsg.LEN = self.length
    #     self.canMsg.MSGTYPE = PCAN_MESSAGE_STANDARD
    #     for i in range(self.length):
    #         self.canMsg.DATA[i] = self.data[i]
    #     self.count += 1
    #     lock.release()
    #     self.m_objPCANBasic.Write(self.m_Channel,self.canMsg)
    #     if self.cycleTime > 0:
    #         send_task = threading.Timer(self.cycleTime*0.001, self.send, args=(lock, ))
    #         send_task.setDaemon(True)
    #         send_task.start()
        

class RMessage(Message):
    def __init__(self):
        self.timestamp = 0
        super().__init__()

    def updateCycleTime(self, newTimestamp):
        self.cycleTime = newTimestamp - self.timestamp
        self.timestamp = newTimestamp