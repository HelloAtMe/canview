
# -*- coding: utf-8 -*-
"""
@ File         : CHcan_main.py
@ Project      : 
@ Author       : 
@ Contact      : 
@ Date         : 2021-06-17 13:19:16
@ Description  : 
"""
import queue
import threading
# from tkinter import messagebox, filedialog
# WING System Module Import
# Add bulit-in module, if necessary
# ================ Code Here ================ #
from tkinter import messagebox, filedialog
from tkinter import Entry, Button, IntVar
import os
import time
# ================ Code Here ================ #

from CHcan_ui import AppUI
from CHcan_cfg import PERIODIC_TIME
# WING User Module Import
# Add your-own module, if necessary
# ================ Code Here ================ #
from CHcan_cfg import p_connectShow, p_CHANNELS, p_BAUDRATES

from can_driver import *
from msg_handle import RMessage, SMessage
from dbc_handle import parsedbc
# ================ Code Here ================ #


class App(AppUI):
    def __init__(self):
        super().__init__()
        self.root_create()
        # WING Initialize Tk GUI and Variables
        # Write initial UI and varibales, here ...
        # ================ Code Here ================ #
        self.Treeview_send_msg.configure(columns=(1,2,3,4,5))
        self.Treeview_recv_msg.configure(columns=(1,2,3))
        self.Treeview_send_msg.column('#0', anchor='center', width=70)
        self.Treeview_send_msg.column(1, anchor='center', width=300)
        self.Treeview_send_msg.column(2, anchor='center', width=80)
        self.Treeview_send_msg.column(3, anchor='center', width=50)
        self.Treeview_send_msg.column(4, anchor='center', width=70)
        self.Treeview_send_msg.column(5, anchor='center', width=40)

        self.Treeview_send_msg.heading('#0', text='Message', anchor='center')
        self.Treeview_send_msg.heading(1, text='Data', anchor='center')
        self.Treeview_send_msg.heading(2, text='Cycle Time', anchor='center')
        self.Treeview_send_msg.heading(3, text='Count', anchor='center')
        self.Treeview_send_msg.heading(4, text='Alivecounter', anchor='center')
        self.Treeview_send_msg.heading(5, text='CRC', anchor='center')

        self.Treeview_recv_msg.column('#0', anchor='center', width=70)
        self.Treeview_recv_msg.column(1, anchor='center', width=400)
        self.Treeview_recv_msg.column(2, anchor='center', width=80)
        self.Treeview_recv_msg.column(3, anchor='center', width=40)

        self.Treeview_recv_msg.heading('#0', text='Message', anchor='center')
        self.Treeview_recv_msg.heading(1, text='Data', anchor='center')
        self.Treeview_recv_msg.heading(2, text='Cycle TIme', anchor='center')
        self.Treeview_recv_msg.heading(3, text='Count', anchor='center')


        try:
            self.m_objPCANBasic = PCANBasic()
        except:
            self.m_objPCANBasic = 0

        self.sendMsg = {}
        self.recvMsg = {}

        self.dbcFiles = []
        self.dbcFileSelect = ''
        # can parameter
        self.d_Baudrate = PCAN_BAUD_500K
        self.d_Channel = PCAN_USBBUS1
        self.d_FilterFromId = 0x000
        self.d_FilterToId = 0x7FF

        self.connect_status = False
        # threading management
        self.lock = threading.Lock()

        # invoke the can driver to send or receive the message
        self.sendCanMsg = TPCANMsg()
        self.recvCanMsg = TPCANMsg()
        self.recvCanTimestamp = TPCANTimestamp()

        # load dbc parameter
        self.varsAttributeFromDbc = {}

        # test parameter
        self.Button_connect_bt_cmd()
        self.Button_start_device_bt_cmd()
        self.update()
        # ================ Code Here ================ #
        self.after(PERIODIC_TIME, self.periodic_cmd)
        
    def periodic_cmd(self):
        # WING Periodic Command
        # Write things need to be handled periodically, here ...
        # ================ Code Here ================ #
        self.update_Treeview_send_msg()
        self.update_Treeview_recv_msg()
        # ================ Code Here ================ #
        self.after(PERIODIC_TIME, self.periodic_cmd)

    def run(self):
        self.root_show()
        self.mainloop()

    def root_resize_handler(self, event):
        self.root_width = event.width
        self.root_height = event.height
        self.root_show()

    def root_close_handler(self):
        # WING Tk Destroy
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        try:
            self.m_objPCANBasic.Uninitialize(self.d_Channel)
        finally:
            self.destroy()
        # ================ Code Here ================ #


    def Treeview_send_msg_evt0_cmd(self, event):
        # WING Event Treeview_send_msg : KeyPress-space
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        for item in self.Treeview_send_msg.selection():
            msg = self.sendMsg.get(item, None)
            if msg:
                self.lock.acquire()
                if msg.length == 8:
                    msg.updateAliveCount()
                    msg.updateCRC()

                self.sendCanMsg.ID = msg.id
                self.sendCanMsg.LEN = msg.length
                for i in range(msg.length):
                    self.sendCanMsg.DATA[i] = msg.data[i]
                msg.updateCount()
                self.lock.release()
                self.sendCanMsg.MSGTYPE = PCAN_MESSAGE_STANDARD
                self.m_objPCANBasic.Write(self.d_Channel,self.sendCanMsg)

        # ================ Code Here ================ #

    def Treeview_send_msg_evt1_cmd(self, event):
        # WING Event Treeview_send_msg : Double-ButtonPress-1
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        for item in self.Treeview_send_msg.selection():
            column= int(self.Treeview_send_msg.identify_column(event.x).replace('#', ''))   # Column
            try:
                _ = int(item, 16)
            except:
                if column > 0:
                    parent, value = TreeBox(event.widget, item, column).show(event.x, event.y)
                    sendMsg = self.sendMsg.get(parent, None)
                    if sendMsg:
                        self.lock.acquire()
                        self.sendMsg.get(parent).modify_data(item, value)
                        self.lock.release()
            else:
                if column != 0 and column != 1 and column != 3:
                    _, value = TreeBox(event.widget, item, column).show(event.x, event.y)
                    sendMsg = self.sendMsg.get(item, None)
                    if sendMsg:
                        self.lock.acquire()
                        if column == 2:
                            sendMsg.cycleTime = value
                        elif column == 4:
                            if value == 0:
                                sendMsg.aliveCount = False
                            else:
                                sendMsg.aliveCount = True
                        elif column == 5:
                            if value == 0:
                                sendMsg.crc = False
                            else:
                                sendMsg.crc = True
                        self.lock.release()
        # ================ Code Here ================ #

    def Button_connect_bt_cmd(self):
        # WING Button Button_connect
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        # check the valid channel
        channels = []
        self.occupied = False
        for n, c in p_CHANNELS.items():
            result = self.m_objPCANBasic.GetValue(c, PCAN_CHANNEL_CONDITION)
            if (result[0] == PCAN_ERROR_OK) and (result[1] == PCAN_CHANNEL_AVAILABLE):
                channels.append(n)
            elif (result[0] == PCAN_ERROR_OK) and (result[1] == PCAN_CHANNEL_OCCUPIED):
                channels.append(n)
                self.occupied = True

        # initial the gui
        self.Toplevel_connect_create()
        self.Combobox_device_name.configure(value=channels)
        if len(channels)>0:
            self.Combobox_device_name_text.set(channels[0])
        self.Combobox_baudrate.configure(value=list(p_BAUDRATES.keys()))
        self.Combobox_baudrate_text.set(list(p_BAUDRATES.keys())[1])
        self.Entry_idfrom_text.set(value='000')
        self.Entry_idto_text.set(value='7FF')
        self.Toplevel_connect_show()
        # ================ Code Here ================ #

    def Button_add_dbc_bt_cmd(self):
        # WING Button Button_add_dbc
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        dbcfile = filedialog.askopenfilename()
        if dbcfile:
            self.dbcFiles.append(dbcfile)

        self.Listbox_dbc_value.set([os.path.basename(f) for f in self.dbcFiles])
        # ================ Code Here ================ #

    def Button_add_msg_bt_cmd(self):
        # WING Button Button_add_msg
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        self.Toplevel_add_msg_create()
        self.Entry_d0_text.set(value='00')
        self.Entry_d1_text.set(value='00')
        self.Entry_d2_text.set(value='00')
        self.Entry_d3_text.set(value='00')
        self.Entry_d4_text.set(value='00')
        self.Entry_d5_text.set(value='00')
        self.Entry_d6_text.set(value='00')
        self.Entry_d7_text.set(value='00')
        self.Entry_id_text.set(value='000')
        self.Entry_length_text.set(value='8')
        self.Entry_period_time_text.set(value='0')
        self.Checkbutton_alivecounter_1_value.set(value=False)
        self.Checkbutton_crc_1_value.set(value=False)
        self.Toplevel_add_msg_show()
        # ================ Code Here ================ #

    def Button_reset_bt_cmd(self):
        # WING Button Button_reset
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        if self.connect_status:
            self.m_objPCANBasic.Reset(self.d_Channel)
        # ================ Code Here ================ #

    def Button_exit_device_bt_cmd(self):
        # WING Button Button_exit_device
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        if self.connect_status:
            self.m_objPCANBasic.Uninitialize(self.d_Channel)
            self.connect_status = False
            self.Label_connect_status_text.set(value=p_connectShow.get(self.connect_status)[0])
            self.Label_connect_status.configure(background=p_connectShow.get(self.connect_status)[1])
            messagebox.showinfo('信息', '设备已推出')

        # ================ Code Here ================ #

    def Button_del_msg_bt_cmd(self):
        # WING Button Button_del_msg
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        for i in self.Treeview_send_msg.selection():
            self.Treeview_send_msg.delete(i)
            self.lock.acquire()
            self.sendMsg.pop(i)
            self.lock.release()

        # ================ Code Here ================ #

    def Button_apply_dbc_bt_cmd(self):
        # WING Button Button_apply_dbc
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        for c in self.Listbox_dbc.curselection():
            for f in self.dbcFiles:
                if os.path.basename(f) == self.Listbox_dbc.get(c):
                    self.dbcFileSelect = f
                    break

        # parse the dbc
        if self.dbcFileSelect:
            self.varsAttributeFromDbc = parsedbc(self.dbcFileSelect)

            for id, msg in self.sendMsg.items():
                varAttribute = self.varsAttributeFromDbc.get(id, {})
                self.lock.acquire()
                msg.set_vars(varAttribute)
                self.lock.release()

            for id, msg in self.recvMsg.items():
                varAttribute = self.varsAttributeFromDbc.get(id, {})
                self.lock.acquire()
                msg.set_vars(varAttribute)
                self.lock.release()

        # ================ Code Here ================ #

    def Button_del_dbc_bt_cmd(self):
        # WING Button Button_del_dbc
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        dbcFilesToBeDeleted = []
        for c in self.Listbox_dbc.curselection():
            for f in self.dbcFiles:
                if os.path.basename(f) == self.Listbox_dbc.get(c):
                    if self.dbcFileSelect == f:
                        messagebox.showerror('错误', message='不能删除正在使用的DBC文件')
                        break
                    else:
                        dbcFilesToBeDeleted.append(f)

        for d in dbcFilesToBeDeleted:
            self.dbcFiles.remove(d)

        self.varsAttributeFromDbc = {}

        for _, msg in self.sendMsg.items():
            self.lock.acquire()
            msg.set_vars({})
            self.lock.release()
        for _, msg in self.sendMsg.items():
            self.lock.acquire()
            msg.set_vars({})
            self.lock.release()

        self.Listbox_dbc_value.set([os.path.basename(f) for f in self.dbcFiles])

        # ================ Code Here ================ #

    def Button_pause_start_bt_cmd(self):
        # WING Button Button_pause_start
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        for item in self.Treeview_send_msg.selection():
            msg = self.sendMsg.get(item, None)
            if msg:
                self.lock.acquire()
                msg.pause = not(msg.pause)
                self.lock.release()
        # ================ Code Here ================ #

    def Toplevel_connect_close_handler(self):
        # WING Toplevel Toplevel_connect Destroy
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        self.Toplevel_connect_root.destroy()
        # ================ Code Here ================ #

    def Toplevel_connect_resize_handler(self, event):
        self.Toplevel_connect_width = event.width
        self.Toplevel_connect_height = event.height
        self.Toplevel_connect_show()

    def Entry_idfrom_evt0_cmd(self, event):
        # WING Event Entry_idfrom : FocusOut
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        self.set_entry_text(self.Entry_idfrom_text, 3)
        # ================ Code Here ================ #

    def Entry_idto_evt0_cmd(self, event):
        # WING Event Entry_idto : FocusOut
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        self.set_entry_text(self.Entry_idto_text, 3)
        # ================ Code Here ================ #

    def Button_start_device_bt_cmd(self):
        # WING Button Button_start_device
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        self.d_Channel = p_CHANNELS.get(self.Combobox_device_name_text.get(), 0)
        self.d_Baudrate = p_BAUDRATES.get(self.Combobox_baudrate_text.get())
        FromID = int(self.Entry_idfrom_text.get(), 16)
        ToID = int(self.Entry_idto_text.get(), 16)
        Mode = PCAN_MODE_STANDARD

        if not self.occupied:
            if self.d_Channel in p_CHANNELS.values():
                self.m_objPCANBasic.Initialize(self.d_Channel, self.d_Baudrate)
                self.m_objPCANBasic.FilterMessages(self.d_Channel, FromID, ToID, Mode)

                self.connect_status = True
                self.Label_connect_status_text.set(value=p_connectShow.get(self.connect_status)[0])
                self.Label_connect_status.configure(background=p_connectShow.get(self.connect_status)[1])

                # start send message
                sendTask = threading.Thread(target=self.send_message, args=(self.lock, ))
                recvTask = threading.Thread(target=self.recv_message, args=(self.lock, ))
                sendTask.setDaemon(True)
                recvTask.setDaemon(True)
                sendTask.start()
                recvTask.start()

                messagebox.showinfo(title='成功', message='连接CAN设备成功')
                self.Toplevel_connect_root.destroy()
            else:
                messagebox.showerror(title='错误', message='未检测到CAN设备')
        else:
            messagebox.showerror(title='错误', message='CAN设备正在使用')
            self.Toplevel_connect_root.destroy()
        # ================ Code Here ================ #

    def Toplevel_add_msg_close_handler(self):
        # WING Toplevel Toplevel_add_msg Destroy
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        self.Toplevel_add_msg_root.grab_release()
        self.Toplevel_add_msg_root.destroy()
        # ================ Code Here ================ #

    def Toplevel_add_msg_resize_handler(self, event):
        self.Toplevel_add_msg_width = event.width
        self.Toplevel_add_msg_height = event.height
        self.Toplevel_add_msg_show()

    def Entry_d0_evt0_cmd(self, event):
        # WING Event Entry_d0 : FocusOut
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        self.set_entry_text(self.Entry_d0_text, 2)
        # ================ Code Here ================ #

    def Entry_d1_evt0_cmd(self, event):
        # WING Event Entry_d1 : FocusOut
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        self.set_entry_text(self.Entry_d1_text, 2)
        # ================ Code Here ================ #

    def Entry_d2_evt0_cmd(self, event):
        # WING Event Entry_d2 : FocusOut
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        self.set_entry_text(self.Entry_d2_text, 2)
        # ================ Code Here ================ #

    def Entry_d3_evt0_cmd(self, event):
        # WING Event Entry_d3 : FocusOut
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        self.set_entry_text(self.Entry_d3_text, 2)
        # ================ Code Here ================ #

    def Entry_d4_evt0_cmd(self, event):
        # WING Event Entry_d4 : FocusOut
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        self.set_entry_text(self.Entry_d4_text, 2)
        # ================ Code Here ================ #

    def Entry_d5_evt0_cmd(self, event):
        # WING Event Entry_d5 : FocusOut
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        self.set_entry_text(self.Entry_d5_text, 2)
        # ================ Code Here ================ #

    def Entry_d6_evt0_cmd(self, event):
        # WING Event Entry_d6 : FocusOut
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        self.set_entry_text(self.Entry_d6_text, 2)
        # ================ Code Here ================ #

    def Entry_d7_evt0_cmd(self, event):
        # WING Event Entry_d7 : FocusOut
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        self.set_entry_text(self.Entry_d7_text, 2)
        # ================ Code Here ================ #

    def Entry_id_evt0_cmd(self, event):
        # WING Event Entry_id : FocusOut
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        self.set_entry_text(self.Entry_id_text, 3)
        # ================ Code Here ================ #

    def Button_msg_ok_bt_cmd(self):
        # WING Button Button_msg_ok
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        if len(self.sendMsg) < 5:
            id_str = self.Entry_id_text.get()
            d0_str = self.Entry_d0_text.get()
            d1_str = self.Entry_d1_text.get()
            d2_str = self.Entry_d2_text.get()
            d3_str = self.Entry_d3_text.get()
            d4_str = self.Entry_d4_text.get()
            d5_str = self.Entry_d5_text.get()
            d6_str = self.Entry_d6_text.get()
            d7_str = self.Entry_d7_text.get()

            msg = SMessage()
            msg.id = int(id_str, 16)
            msg.set_data([int(d0_str, 16),
                        int(d1_str, 16),
                        int(d2_str, 16),
                        int(d3_str, 16),
                        int(d4_str, 16),
                        int(d5_str, 16),
                        int(d6_str, 16),
                        int(d7_str, 16)])
            msg.length = int(self.Entry_length_text.get())
            msg.cycleTime = int(self.Entry_period_time_text.get())
            msg.aliveCount = self.Checkbutton_alivecounter_1_value.get()
            msg.crc = self.Checkbutton_crc_1_value.get()
            msg.set_vars(self.varsAttributeFromDbc.get(id_str, {}))

            if self.Entry_id_text.get() in self.sendMsg.keys():
                messagebox.showerror('错误', 'Message已存在')
            else:
                self.lock.acquire()
                self.sendMsg.update({id_str:msg})
                self.lock.release()

                self.Toplevel_add_msg_root.destroy()
        else:
            messagebox.showerror('错误', 'Message数量达到极限')
        # ================ Code Here ================ #

    def Button_msg_cancel_bt_cmd(self):
        # WING Button Button_msg_cancel
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        self.Toplevel_add_msg_root.destroy()
        # ================ Code Here ================ #

    def Checkbutton_crc_1_bt_cmd(self):
        # WING Button Checkbutton_crc_1
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        pass
        # ================ Code Here ================ #

    def Checkbutton_alivecounter_1_bt_cmd(self):
        # WING Button Checkbutton_alivecounter_1
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        pass
        # ================ Code Here ================ #

    def Entry_length_evt0_cmd(self, event):
        # WING Event Entry_length : FocusOut
        # Write things need to be handled, here ...
        # ================ Code Here ================ #
        pass
        # ================ Code Here ================ #


    # WING Tk Class Main
    # Write things need to be handled, here ...
    # ================ Code Here ================ #
    def set_entry_text(self, ctrl, cnt):
        valid = True
        num = ctrl.get()
        if len(num) > cnt:
            valid = False
        try:
            num = int(num,16)
        except ValueError:
            valid = False
        finally:
            if valid:
                if cnt == 2:
                    text = '{:0>2X}'.format(num)
                elif cnt == 3:
                    text = '{:0>3X}'.format(num)
            else:
                text = '0'*cnt
                messagebox.showerror(title='错误', message='输入值无效，{}个应该16进制数字'.format(cnt))
            ctrl.set(value=text)

    def update_Treeview_send_msg(self):
        for i, msg in self.sendMsg.items():
            if i in self.Treeview_send_msg.get_children():
                self.Treeview_send_msg.item(i, values=(['{:0>2X}'.format(d) for d in msg.data],  msg.cycleTime, msg.count, msg.aliveCount, msg.crc))
            else:
                self.Treeview_send_msg.insert('', 'end', iid=i, text=i, values=(['{:0>2X}'.format(d) for d in msg.data], msg.cycleTime, msg.count, msg.aliveCount, msg.crc))
            for k, v in msg.varsValue.items():
                if k in self.Treeview_send_msg.get_children(i):
                    self.Treeview_send_msg.set(k, column=1, value=v)
                else:
                    self.Treeview_send_msg.insert(i, 'end', iid=k, text=k, values=(v, '', '', '', ''))

    def update_Treeview_recv_msg(self):
        for i, msg in self.recvMsg.items():
            if i in self.Treeview_recv_msg.get_children():
                self.Treeview_recv_msg.item(i, values=(['{:0>2X}'.format(d) for d in msg.data], msg.cycleTime, msg.count))
            else:
                self.Treeview_recv_msg.insert('', 'end', iid=i, text=i, values=(['{:0>2X}'.format(d) for d in msg.data], msg.cycleTime, msg.count))
            for k, v in msg.varsValue.items():
                if k in self.Treeview_recv_msg.get_children(i):
                    self.Treeview_recv_msg.set(k, column=1, value=v)
                else:
                    self.Treeview_recv_msg.insert(i, 'end', iid=k, text=k, values=(v, '', ''))


    def send_message(self, lock):
        _currentTime = 0
        _startTime = 0
        _intervalTime = 0

        while True:
            _currentTime = time.time_ns()
            _intervalTime = _currentTime - _startTime

            if _intervalTime > 100000:
                _startTime = _currentTime
                lock.acquire()
                for _, msg in self.sendMsg.items():
                    if msg.checkTimeout() and not(msg.pause):
                        if msg.length == 8:
                            msg.updateAliveCount()
                            msg.updateCRC()

                        self.sendCanMsg.ID = msg.id
                        self.sendCanMsg.LEN = msg.length
                        for i in range(msg.length):
                            self.sendCanMsg.DATA[i] = msg.data[i]
                        msg.updateCount()
                        msg.parse_data()

                        self.sendCanMsg.MSGTYPE = PCAN_MESSAGE_STANDARD
                        self.m_objPCANBasic.Write(self.d_Channel,self.sendCanMsg)
                lock.release()


    def recv_message(self, lock):
        _currentTime = 0
        _startTime = 0
        _intervalTime = 0

        while True:
            _currentTime = time.time_ns()
            _intervalTime = _currentTime - _startTime

            if _intervalTime > 100000:
                _startTime = _currentTime
                lock.acquire()

                result, self.recvCanMsg, self.recvCanTimestamp = self.m_objPCANBasic.Read(self.d_Channel)
                if result == PCAN_ERROR_OK:
                    recvMsg = self.recvMsg.get('{:0>3X}'.format(self.recvCanMsg.ID), None)
                    if not recvMsg:
                        recvMsg = RMessage()
                        recvMsg.set_vars(self.varsAttributeFromDbc.get('{:0>3X}'.format(self.recvCanMsg.ID), {}))
                        self.recvMsg.update({'{:0>3X}'.format(self.recvCanMsg.ID):recvMsg})
                    recvMsg.id = self.recvCanMsg.ID                    
                    recvMsg.length = self.recvCanMsg.LEN
                    for i in range(recvMsg.length):
                        recvMsg.data[i] = self.recvCanMsg.DATA[i]
                    timestamp = int(self.recvCanTimestamp.millis + (self.recvCanTimestamp.micros / 1000.0))
                    recvMsg.updateCycleTime(timestamp)
                    recvMsg.updateCount()
                    recvMsg.parse_data()

                lock.release()
    # ================ Code Here ================ #

# WING Tk App Main
# Write things need to be handled, here ...
# ================ Code Here ================ #
class TreeBox(Entry):
    def __init__(self, master, item, column):
        self.item = item
        self.column = column
        self.flag = IntVar(value=0)
        self.parent = ''
        self.value = 0
        super().__init__(master)
        self.cBtn = Button(self, text='确定', command=self.comfirm)
        self.grab_set()
        self.bind('<Enter>', self.bindevent)
        self.bind('<Leave>', self.unbindevent)
        
    
    def bindevent(self, event):
        self.bind('<Return>', lambda event : self.comfirm())
        self.bind('<KeyPress-Escape>', self.cancel)
    
    def unbindevent(self, event):
        self.unbind('<Return>')
        self.unbind('<KeyPress-Escape>')

    def cancel(self, event):
        self.flag.set(value=1)
        self.grab_release()
        self.cBtn.destroy()
        self.destroy()


    def comfirm(self):
        text = self.get()
        try:
            num = int(text)
        except:
            messagebox.showerror(title='错误', message='请输入数字')
        else:
            self.parent = self.master.parent(self.item)
            self.value = num
        finally:
            self.flag.set(value=1)
            self.grab_release()
            self.cBtn.destroy()
            self.destroy()

    def show(self, x, y):
        self.place(x=x, y=y, width=150, height=30, anchor='nw')
        self.cBtn.place(x=150, y=0, width=50, height=30, anchor='ne')
        self.wait_variable(self.flag)
        return self.parent, self.value

# ================ Code Here ================ #

if __name__ == '__main__':
    app = App()
    app.run()
