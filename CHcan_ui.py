
# -*- coding: utf-8 -*-
"""
@ File         : CHcan_ui.py
@ Project      : 
@ Author       : 
@ Contact      : 
@ Date         : 2021-06-17 13:19:16
@ Description  : 
"""

import sys
from tkinter import Tk, Toplevel, PhotoImage
from tkinter import BooleanVar, IntVar, StringVar
from tkinter import Label, Frame, Text, Listbox, Entry, Checkbutton, Radiobutton, Canvas, LabelFrame, Menu
from tkinter import ttk

from CHcan_cfg import STATUSBAR_HEIGHT, SCROLLBAR_WIDTH


class AppUI(Tk):
    def __init__(self):
        super().__init__()
        self.title('CAN View')
        self.root_window_size()
        self.geometry('{}x{}+{}+{}'.format(self.root_width, self.root_height, self.root_x, self.root_y))
        self.resizable(True, True)
        self.style = ttk.Style()

    def root_window_size(self):
        self.root_width   = int(880)
        self.root_height  = int(641)+STATUSBAR_HEIGHT
        self.root_x       = int((self.winfo_screenwidth() - self.root_width)*0.5)
        self.root_y       = int((self.winfo_screenheight() - self.root_height)*0.3)

    def root_image_load(self):
        # ================ Auto Code ================ #
        self.Button_connect_pic_0 = '' 
        self.Button_add_dbc_pic_0 = '' 
        self.Button_add_msg_pic_0 = '' 
        self.Button_reset_pic_0 = '' 
        self.Button_exit_device_pic_0 = '' 
        self.Label_connect_status_pic_0 = '' 
        self.Label_11_pic_0 = '' 
        self.Label_3210_pic_0 = '' 
        self.Button_del_msg_pic_0 = '' 
        self.Button_apply_dbc_pic_0 = '' 
        self.Label_5678_pic_0 = '' 
        self.Button_del_dbc_pic_0 = '' 
        self.Label_4563_pic_0 = '' 
        self.Label_1456_pic_0 = '' 
        self.Button_pause_start_pic_0 = '' 
        # ================ Auto Code ================ #
        
    def root_bind(self):
        self.protocol('WM_DELETE_WINDOW', self.root_close_handler)
        self.Tk_0.bind('<Configure>', self.root_resize_handler)
        # ================ Auto Code ================ #
        self.Treeview_send_msg.bind('<KeyPress-space>', self.Treeview_send_msg_evt0_cmd)
        self.Treeview_send_msg.bind('<Double-ButtonPress-1>', self.Treeview_send_msg_evt1_cmd)
        # ================ Auto Code ================ #

    def root_create(self):
        self.root_image_load()
        self.Tk_0 = Frame(self, background='#ececec')
        self.Tk_0.place(relx=0, rely=0, relwidth=1, relheight=1, anchor='nw')
        # Widgets
        # ================ Auto Code ================ #
        self.style.configure('Treeview_recv_msg.Treeview',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'flat')
        self.Treeview_recv_msg = ttk.Treeview(self.Tk_0,
                                    show            = 'tree headings',
                                    selectmode      = 'browse',
                                    cursor          = 'arrow',
                                    takefocus       = False,
                                    style           = 'Treeview_recv_msg.Treeview')
        self.Treeview_recv_msg_scrollbar_vertical = ttk.Scrollbar(self.Tk_0, orient='vertical', command=self.Treeview_recv_msg.yview)
        self.Treeview_recv_msg.configure(yscrollcommand=self.Treeview_recv_msg_scrollbar_vertical.set)
        self.Treeview_recv_msg.bind('<MouseWheel>', lambda event:self.Treeview_recv_msg.yview_scroll(int(-0.01*event.delta), 'units'))
        self.style.configure('Treeview_send_msg.Treeview',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'flat')
        self.Treeview_send_msg = ttk.Treeview(self.Tk_0,
                                    show            = 'tree headings',
                                    selectmode      = 'browse',
                                    cursor          = 'arrow',
                                    takefocus       = False,
                                    style           = 'Treeview_send_msg.Treeview')
        self.Treeview_send_msg_scrollbar_vertical = ttk.Scrollbar(self.Tk_0, orient='vertical', command=self.Treeview_send_msg.yview)
        self.Treeview_send_msg.configure(yscrollcommand=self.Treeview_send_msg_scrollbar_vertical.set)
        self.Treeview_send_msg.bind('<MouseWheel>', lambda event:self.Treeview_send_msg.yview_scroll(int(-0.01*event.delta), 'units'))
        self.Button_connect_text = StringVar(value='连接设备')
        self.style.configure('Button_connect.TButton',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'flat')
        self.Button_connect = ttk.Button( self.Tk_0,
                                    textvariable    = self.Button_connect_text,
                                    image           = self.Button_connect_pic_0,
                                    compound        = 'center',
                                    cursor          = 'hand2',
                                    takefocus       = False,
                                    command         = self.Button_connect_bt_cmd,
                                    style           = 'Button_connect.TButton')
        self.Listbox_dbc_value = StringVar(value=())
        self.Listbox_dbc = Listbox(self.Tk_0,
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    listvariable    = self.Listbox_dbc_value,
                                    relief          = 'flat',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    justify         = 'center',
                                    selectmode      = 'single',
                                    cursor          = 'arrow',
                                    takefocus       = False)
        self.Listbox_dbc_scrollbar_vertical = ttk.Scrollbar(self.Tk_0, orient='vertical', command=self.Listbox_dbc.yview)
        self.Listbox_dbc.configure(yscrollcommand=self.Listbox_dbc_scrollbar_vertical.set)
        self.Listbox_dbc.bind('<MouseWheel>', lambda event:self.Listbox_dbc.yview_scroll(int(-0.01*event.delta), 'units'))
        self.Button_add_dbc_text = StringVar(value='添加DBC')
        self.style.configure('Button_add_dbc.TButton',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'flat')
        self.Button_add_dbc = ttk.Button( self.Tk_0,
                                    textvariable    = self.Button_add_dbc_text,
                                    image           = self.Button_add_dbc_pic_0,
                                    compound        = 'center',
                                    cursor          = 'hand2',
                                    takefocus       = False,
                                    command         = self.Button_add_dbc_bt_cmd,
                                    style           = 'Button_add_dbc.TButton')
        self.Button_add_msg_text = StringVar(value='添加信号')
        self.style.configure('Button_add_msg.TButton',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'flat')
        self.Button_add_msg = ttk.Button( self.Tk_0,
                                    textvariable    = self.Button_add_msg_text,
                                    image           = self.Button_add_msg_pic_0,
                                    compound        = 'center',
                                    cursor          = 'hand2',
                                    takefocus       = False,
                                    command         = self.Button_add_msg_bt_cmd,
                                    style           = 'Button_add_msg.TButton')
        self.Button_reset_text = StringVar(value='重置设备')
        self.style.configure('Button_reset.TButton',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'flat')
        self.Button_reset = ttk.Button( self.Tk_0,
                                    textvariable    = self.Button_reset_text,
                                    image           = self.Button_reset_pic_0,
                                    compound        = 'center',
                                    cursor          = 'hand2',
                                    takefocus       = False,
                                    command         = self.Button_reset_bt_cmd,
                                    style           = 'Button_reset.TButton')
        self.Button_exit_device_text = StringVar(value='退出设备')
        self.style.configure('Button_exit_device.TButton',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'flat')
        self.Button_exit_device = ttk.Button( self.Tk_0,
                                    textvariable    = self.Button_exit_device_text,
                                    image           = self.Button_exit_device_pic_0,
                                    compound        = 'center',
                                    cursor          = 'hand2',
                                    takefocus       = False,
                                    command         = self.Button_exit_device_bt_cmd,
                                    style           = 'Button_exit_device.TButton')
        self.Label_connect_status_text = StringVar(value='未连接')
        self.style.configure('Label_connect_status.TLabel',
                                    foreground      = '#000000',
                                    background      = '#ff0000',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'flat')
        self.Label_connect_status = ttk.Label(self.Tk_0,
                                    textvariable    = self.Label_connect_status_text,
                                    image           = self.Label_connect_status_pic_0,
                                    compound        = 'center',
                                    cursor          = 'arrow',
                                    takefocus       = False,
                                    wraplength      = 150,
                                    style           = 'Label_connect_status.TLabel')
        self.Label_11_text = StringVar(value='接\n\n收\n\n信\n\n号')
        self.style.configure('Label_11.TLabel',
                                    foreground      = '#000000',
                                    background      = '#ececec',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'raised')
        self.Label_11 = ttk.Label(self.Tk_0,
                                    textvariable    = self.Label_11_text,
                                    image           = self.Label_11_pic_0,
                                    compound        = 'center',
                                    cursor          = 'arrow',
                                    takefocus       = False,
                                    wraplength      = 29,
                                    style           = 'Label_11.TLabel')
        self.Label_3210_text = StringVar(value='发\n\n送\n\n信\n\n号')
        self.style.configure('Label_3210.TLabel',
                                    foreground      = '#000000',
                                    background      = '#ececec',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'raised')
        self.Label_3210 = ttk.Label(self.Tk_0,
                                    textvariable    = self.Label_3210_text,
                                    image           = self.Label_3210_pic_0,
                                    compound        = 'center',
                                    cursor          = 'arrow',
                                    takefocus       = False,
                                    wraplength      = 29,
                                    style           = 'Label_3210.TLabel')
        self.Button_del_msg_text = StringVar(value='删除信号')
        self.style.configure('Button_del_msg.TButton',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'flat')
        self.Button_del_msg = ttk.Button( self.Tk_0,
                                    textvariable    = self.Button_del_msg_text,
                                    image           = self.Button_del_msg_pic_0,
                                    compound        = 'center',
                                    cursor          = 'hand2',
                                    takefocus       = False,
                                    command         = self.Button_del_msg_bt_cmd,
                                    style           = 'Button_del_msg.TButton')
        self.Button_apply_dbc_text = StringVar(value='应用DBC')
        self.style.configure('Button_apply_dbc.TButton',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'flat')
        self.Button_apply_dbc = ttk.Button( self.Tk_0,
                                    textvariable    = self.Button_apply_dbc_text,
                                    image           = self.Button_apply_dbc_pic_0,
                                    compound        = 'center',
                                    cursor          = 'hand2',
                                    takefocus       = False,
                                    command         = self.Button_apply_dbc_bt_cmd,
                                    style           = 'Button_apply_dbc.TButton')
        self.Label_5678_text = StringVar(value='DBC操作')
        self.style.configure('Label_5678.TLabel',
                                    foreground      = '#000000',
                                    background      = '#ececec',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'groove')
        self.Label_5678 = ttk.Label(self.Tk_0,
                                    textvariable    = self.Label_5678_text,
                                    image           = self.Label_5678_pic_0,
                                    compound        = 'center',
                                    cursor          = 'arrow',
                                    takefocus       = False,
                                    wraplength      = 148,
                                    style           = 'Label_5678.TLabel')
        self.Button_del_dbc_text = StringVar(value='删除DBC')
        self.style.configure('Button_del_dbc.TButton',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'flat')
        self.Button_del_dbc = ttk.Button( self.Tk_0,
                                    textvariable    = self.Button_del_dbc_text,
                                    image           = self.Button_del_dbc_pic_0,
                                    compound        = 'center',
                                    cursor          = 'hand2',
                                    takefocus       = False,
                                    command         = self.Button_del_dbc_bt_cmd,
                                    style           = 'Button_del_dbc.TButton')
        self.Label_4563_text = StringVar(value='信号操作')
        self.style.configure('Label_4563.TLabel',
                                    foreground      = '#000000',
                                    background      = '#ececec',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'groove')
        self.Label_4563 = ttk.Label(self.Tk_0,
                                    textvariable    = self.Label_4563_text,
                                    image           = self.Label_4563_pic_0,
                                    compound        = 'center',
                                    cursor          = 'arrow',
                                    takefocus       = False,
                                    wraplength      = 148,
                                    style           = 'Label_4563.TLabel')
        self.Label_1456_text = StringVar(value='设备操作')
        self.style.configure('Label_1456.TLabel',
                                    foreground      = '#000000',
                                    background      = '#ececec',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'groove')
        self.Label_1456 = ttk.Label(self.Tk_0,
                                    textvariable    = self.Label_1456_text,
                                    image           = self.Label_1456_pic_0,
                                    compound        = 'center',
                                    cursor          = 'arrow',
                                    takefocus       = False,
                                    wraplength      = 148,
                                    style           = 'Label_1456.TLabel')
        self.Button_pause_start_text = StringVar(value='开始/暂停')
        self.style.configure('Button_pause_start.TButton',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ('Airal', 8, 'normal', 'roman'),
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'flat')
        self.Button_pause_start = ttk.Button( self.Tk_0,
                                    textvariable    = self.Button_pause_start_text,
                                    image           = self.Button_pause_start_pic_0,
                                    compound        = 'center',
                                    cursor          = 'hand2',
                                    takefocus       = False,
                                    command         = self.Button_pause_start_bt_cmd,
                                    style           = 'Button_pause_start.TButton')
        # ================ Auto Code ================ #
        # Menu
        # ================ Auto Code ================ #
        # ================ Auto Code ================ #
        self.root_bind()

    def root_widget_size(self):
        # ================ Auto Code ================ #
        # For place the widget : Treeview_recv_msg
        zone1_x = 0
        zone1_y = 20
        zone1_w = self.root_width - 150
        zone1_h = self.root_height // 2 - 20

        zone2_x = 0
        zone2_y = zone1_y + zone1_h + 20
        zone2_w = zone1_w
        zone2_h = zone1_h

        zone3_x = zone1_w
        zone3_y = zone1_y
        zone3_w = 150
        zone3_h = zone1_h

        zone4_x = zone2_w
        zone4_y = zone2_y
        zone4_w = 150
        zone4_h = zone2_h

        self.Treeview_recv_msg_bx = 30
        self.Treeview_recv_msg_by = zone1_y
        self.Treeview_recv_msg_bw = zone1_w - 30
        self.Treeview_recv_msg_bh = zone1_h
        self.Treeview_recv_msg_x = self.Treeview_recv_msg_bx
        self.Treeview_recv_msg_y = self.Treeview_recv_msg_by
        self.Treeview_recv_msg_w = self.Treeview_recv_msg_bw - SCROLLBAR_WIDTH
        self.Treeview_recv_msg_h = self.Treeview_recv_msg_bh
        self.Treeview_recv_msg_scrollbar_vertical_x = self.Treeview_recv_msg_x + self.Treeview_recv_msg_w
        self.Treeview_recv_msg_scrollbar_vertical_y = self.Treeview_recv_msg_y
        self.Treeview_recv_msg_scrollbar_vertical_w = SCROLLBAR_WIDTH
        self.Treeview_recv_msg_scrollbar_vertical_h = self.Treeview_recv_msg_h
        # For place the widget : Treeview_send_msg
        self.Treeview_send_msg_bx = 30
        self.Treeview_send_msg_by = zone2_y
        self.Treeview_send_msg_bw = zone2_w - 30
        self.Treeview_send_msg_bh = zone2_h
        self.Treeview_send_msg_x = self.Treeview_send_msg_bx
        self.Treeview_send_msg_y = self.Treeview_send_msg_by
        self.Treeview_send_msg_w = self.Treeview_send_msg_bw - SCROLLBAR_WIDTH
        self.Treeview_send_msg_h = self.Treeview_send_msg_bh
        self.Treeview_send_msg_scrollbar_vertical_x = self.Treeview_send_msg_x + self.Treeview_send_msg_w
        self.Treeview_send_msg_scrollbar_vertical_y = self.Treeview_send_msg_y
        self.Treeview_send_msg_scrollbar_vertical_w = SCROLLBAR_WIDTH
        self.Treeview_send_msg_scrollbar_vertical_h = self.Treeview_send_msg_h
        # For place the widget : Button_connect
        self.Button_connect_x = zone3_x + 3
        self.Button_connect_y = zone3_y + 32
        self.Button_connect_w = 70
        self.Button_connect_h = 30
        # For place the widget : Listbox_dbc
        self.Listbox_dbc_bx = zone3_x
        self.Listbox_dbc_by = zone3_y + 127
        self.Listbox_dbc_bw = 150
        self.Listbox_dbc_bh = 100
        self.Listbox_dbc_x = self.Listbox_dbc_bx
        self.Listbox_dbc_y = self.Listbox_dbc_by
        self.Listbox_dbc_w = self.Listbox_dbc_bw - SCROLLBAR_WIDTH
        self.Listbox_dbc_h = self.Listbox_dbc_bh
        self.Listbox_dbc_scrollbar_vertical_x = self.Listbox_dbc_x + self.Listbox_dbc_w
        self.Listbox_dbc_scrollbar_vertical_y = self.Listbox_dbc_y
        self.Listbox_dbc_scrollbar_vertical_w = SCROLLBAR_WIDTH
        self.Listbox_dbc_scrollbar_vertical_h = self.Listbox_dbc_h
        # For place the widget : Button_add_dbc
        self.Button_add_dbc_x = zone3_x + 3
        self.Button_add_dbc_y = zone3_y + 229
        self.Button_add_dbc_w = 70
        self.Button_add_dbc_h = 30
        # For place the widget : Button_add_msg
        self.Button_add_msg_x = zone4_x + 3
        self.Button_add_msg_y = zone4_y + 32
        self.Button_add_msg_w = 70
        self.Button_add_msg_h = 30
        # For place the widget : Button_reset
        self.Button_reset_x = zone3_x + 3
        self.Button_reset_y = zone3_y + 62
        self.Button_reset_w = 70
        self.Button_reset_h = 30
        # For place the widget : Button_exit_device
        self.Button_exit_device_x = zone3_x + 79
        self.Button_exit_device_y = zone3_y + 32
        self.Button_exit_device_w = 70
        self.Button_exit_device_h = 30
        # For place the widget : Label_connect_status
        self.Label_connect_status_x = zone4_x
        self.Label_connect_status_y = zone4_y + zone4_h - 30
        self.Label_connect_status_w = 150
        self.Label_connect_status_h = 30
        # For place the widget : Label_11
        self.Label_11_x = zone1_x
        self.Label_11_y = zone1_y
        self.Label_11_w = 29
        self.Label_11_h = zone1_h
        # For place the widget : Label_3210
        self.Label_3210_x = zone2_x
        self.Label_3210_y = zone2_y
        self.Label_3210_w = 29
        self.Label_3210_h = zone2_h
        # For place the widget : Button_del_msg
        self.Button_del_msg_x = zone4_x + 79
        self.Button_del_msg_y = zone4_y + 32
        self.Button_del_msg_w = 70
        self.Button_del_msg_h = 30
        # For place the widget : Button_apply_dbc
        self.Button_apply_dbc_x = zone3_x + 79
        self.Button_apply_dbc_y = zone3_y + 229
        self.Button_apply_dbc_w = 70
        self.Button_apply_dbc_h = 30
        # For place the widget : Label_5678
        self.Label_5678_x = zone3_x
        self.Label_5678_y = zone3_y+97
        self.Label_5678_w = 150
        self.Label_5678_h = 30
        # For place the widget : Button_del_dbc
        self.Button_del_dbc_x = zone3_x + 3
        self.Button_del_dbc_y = zone3_y + 259
        self.Button_del_dbc_w = 70
        self.Button_del_dbc_h = 30
        # For place the widget : Label_4563
        self.Label_4563_x = zone4_x
        self.Label_4563_y = zone4_y
        self.Label_4563_w = 150
        self.Label_4563_h = 30
        # For place the widget : Label_1456
        self.Label_1456_x = zone3_x
        self.Label_1456_y = zone3_y
        self.Label_1456_w = 150
        self.Label_1456_h = 30
        # For place the widget : Button_pause_start
        self.Button_pause_start_x = zone4_x + 3
        self.Button_pause_start_y = zone4_y + 62
        self.Button_pause_start_w = 70
        self.Button_pause_start_h = 30
        # ================ Auto Code ================ #

    def root_show(self):
        self.root_widget_size()
        # ================ Auto Code ================ #
        self.Treeview_recv_msg.place(x=self.Treeview_recv_msg_x, y=self.Treeview_recv_msg_y, width=self.Treeview_recv_msg_w, height=self.Treeview_recv_msg_h, anchor='nw')
        self.Treeview_recv_msg_scrollbar_vertical.place(x=self.Treeview_recv_msg_scrollbar_vertical_x, y=self.Treeview_recv_msg_scrollbar_vertical_y, width=self.Treeview_recv_msg_scrollbar_vertical_w, height=self.Treeview_recv_msg_scrollbar_vertical_h, anchor='nw')
        self.Treeview_send_msg.place(x=self.Treeview_send_msg_x, y=self.Treeview_send_msg_y, width=self.Treeview_send_msg_w, height=self.Treeview_send_msg_h, anchor='nw')
        self.Treeview_send_msg_scrollbar_vertical.place(x=self.Treeview_send_msg_scrollbar_vertical_x, y=self.Treeview_send_msg_scrollbar_vertical_y, width=self.Treeview_send_msg_scrollbar_vertical_w, height=self.Treeview_send_msg_scrollbar_vertical_h, anchor='nw')
        self.Button_connect.place(x=self.Button_connect_x, y=self.Button_connect_y, width=self.Button_connect_w, height=self.Button_connect_h, anchor='nw')
        self.Listbox_dbc.place(x=self.Listbox_dbc_x, y=self.Listbox_dbc_y, width=self.Listbox_dbc_w, height=self.Listbox_dbc_h, anchor='nw')
        self.Listbox_dbc_scrollbar_vertical.place(x=self.Listbox_dbc_scrollbar_vertical_x, y=self.Listbox_dbc_scrollbar_vertical_y, width=self.Listbox_dbc_scrollbar_vertical_w, height=self.Listbox_dbc_scrollbar_vertical_h, anchor='nw')
        self.Button_add_dbc.place(x=self.Button_add_dbc_x, y=self.Button_add_dbc_y, width=self.Button_add_dbc_w, height=self.Button_add_dbc_h, anchor='nw')
        self.Button_add_msg.place(x=self.Button_add_msg_x, y=self.Button_add_msg_y, width=self.Button_add_msg_w, height=self.Button_add_msg_h, anchor='nw')
        self.Button_reset.place(x=self.Button_reset_x, y=self.Button_reset_y, width=self.Button_reset_w, height=self.Button_reset_h, anchor='nw')
        self.Button_exit_device.place(x=self.Button_exit_device_x, y=self.Button_exit_device_y, width=self.Button_exit_device_w, height=self.Button_exit_device_h, anchor='nw')
        self.Label_connect_status.place(x=self.Label_connect_status_x, y=self.Label_connect_status_y, width=self.Label_connect_status_w, height=self.Label_connect_status_h, anchor='nw')
        self.Label_11.place(x=self.Label_11_x, y=self.Label_11_y, width=self.Label_11_w, height=self.Label_11_h, anchor='nw')
        self.Label_3210.place(x=self.Label_3210_x, y=self.Label_3210_y, width=self.Label_3210_w, height=self.Label_3210_h, anchor='nw')
        self.Button_del_msg.place(x=self.Button_del_msg_x, y=self.Button_del_msg_y, width=self.Button_del_msg_w, height=self.Button_del_msg_h, anchor='nw')
        self.Button_apply_dbc.place(x=self.Button_apply_dbc_x, y=self.Button_apply_dbc_y, width=self.Button_apply_dbc_w, height=self.Button_apply_dbc_h, anchor='nw')
        self.Label_5678.place(x=self.Label_5678_x, y=self.Label_5678_y, width=self.Label_5678_w, height=self.Label_5678_h, anchor='nw')
        self.Button_del_dbc.place(x=self.Button_del_dbc_x, y=self.Button_del_dbc_y, width=self.Button_del_dbc_w, height=self.Button_del_dbc_h, anchor='nw')
        self.Label_4563.place(x=self.Label_4563_x, y=self.Label_4563_y, width=self.Label_4563_w, height=self.Label_4563_h, anchor='nw')
        self.Label_1456.place(x=self.Label_1456_x, y=self.Label_1456_y, width=self.Label_1456_w, height=self.Label_1456_h, anchor='nw')
        self.Button_pause_start.place(x=self.Button_pause_start_x, y=self.Button_pause_start_y, width=self.Button_pause_start_w, height=self.Button_pause_start_h, anchor='nw')
        # ================ Auto Code ================ #

# =========================== defined for Toplevel_connect =========================== #
    def Toplevel_connect_image_load(self):
        # ================ Auto Code ================ #
        self.Label_2_pic_0 = '' 
        self.Label_4_pic_0 = '' 
        self.Label_5_pic_0 = '' 
        self.Label_3_pic_0 = '' 
        self.Button_start_device_pic_0 = '' 
        # ================ Auto Code ================ #

    def Toplevel_connect_window_size(self):
        self.Toplevel_connect_width = int(345)
        self.Toplevel_connect_height = int(276)
        self.Toplevel_connect_x = int(self.winfo_x() + ((self.winfo_width() - self.Toplevel_connect_width)*0.5))
        self.Toplevel_connect_y = int(self.winfo_y() + ((self.winfo_height() - self.Toplevel_connect_height)*0.4))
        if self.Toplevel_connect_x < 0 or self.Toplevel_connect_y < 0:
            self.Toplevel_connect_x       = int((self.winfo_screenwidth() - self.Toplevel_connect_width)*0.5)
            self.Toplevel_connect_y       = int((self.winfo_screenheight() - self.Toplevel_connect_height)*0.4)
    def Toplevel_connect_bind(self):
        self.Toplevel_connect_root.protocol('WM_DELETE_WINDOW', self.Toplevel_connect_close_handler)
        self.Toplevel_connect.bind('<Configure>', self.Toplevel_connect_resize_handler)
        # ================ Auto Code ================ #
        self.Entry_idfrom.bind('<FocusOut>', self.Entry_idfrom_evt0_cmd)
        self.Entry_idto.bind('<FocusOut>', self.Entry_idto_evt0_cmd)
        # ================ Auto Code ================ #

    def Toplevel_connect_create(self):
        self.Toplevel_connect_image_load()
        self.Toplevel_connect_root = Toplevel(self)
        self.Toplevel_connect_root.title('连接设备')
        self.Toplevel_connect_window_size()
        self.Toplevel_connect_root.geometry('{}x{}+{}+{}'.format(self.Toplevel_connect_width, self.Toplevel_connect_height, self.Toplevel_connect_x, self.Toplevel_connect_y))
        self.Toplevel_connect_root.resizable(False, False)
        self.Toplevel_connect = Frame(self.Toplevel_connect_root, background='#ececec')
        self.Toplevel_connect.place(relx=0, rely=0, relwidth=1, relheight=1, anchor='nw')
        # Widgets
        # ================ Auto Code ================ #
        self.Label_2_text = StringVar(value='波特率')
        self.style.configure('Label_2.TLabel',
                                    foreground      = '#000000',
                                    background      = '#ececec',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'groove')
        self.Label_2 = ttk.Label(self.Toplevel_connect,
                                    textvariable    = self.Label_2_text,
                                    image           = self.Label_2_pic_0,
                                    compound        = 'center',
                                    cursor          = 'arrow',
                                    takefocus       = False,
                                    wraplength      = 100,
                                    style           = 'Label_2.TLabel')
        self.Label_4_text = StringVar(value='FROM:')
        self.style.configure('Label_4.TLabel',
                                    foreground      = '#000000',
                                    background      = '#ececec',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'groove')
        self.Label_4 = ttk.Label(self.Toplevel_connect,
                                    textvariable    = self.Label_4_text,
                                    image           = self.Label_4_pic_0,
                                    compound        = 'center',
                                    cursor          = 'arrow',
                                    takefocus       = False,
                                    wraplength      = 100,
                                    style           = 'Label_4.TLabel')
        self.Label_5_text = StringVar(value='TO:')
        self.style.configure('Label_5.TLabel',
                                    foreground      = '#000000',
                                    background      = '#ececec',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'groove')
        self.Label_5 = ttk.Label(self.Toplevel_connect,
                                    textvariable    = self.Label_5_text,
                                    image           = self.Label_5_pic_0,
                                    compound        = 'center',
                                    cursor          = 'arrow',
                                    takefocus       = False,
                                    wraplength      = 100,
                                    style           = 'Label_5.TLabel')
        self.Label_3_text = StringVar(value='设备')
        self.style.configure('Label_3.TLabel',
                                    foreground      = '#000000',
                                    background      = '#ececec',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'groove')
        self.Label_3 = ttk.Label(self.Toplevel_connect,
                                    textvariable    = self.Label_3_text,
                                    image           = self.Label_3_pic_0,
                                    compound        = 'center',
                                    cursor          = 'arrow',
                                    takefocus       = False,
                                    wraplength      = 100,
                                    style           = 'Label_3.TLabel')
        self.Combobox_device_name_text = StringVar(value='')
        self.style.configure('Combobox_device_name.TCombobox',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    relief          = 'flat')
        self.Combobox_device_name = ttk.Combobox(self.Toplevel_connect,
                                    value           = [],
                                    textvariable    = self.Combobox_device_name_text,
                                    justify         = 'center',
                                    exportselection = True,
                                    cursor          = 'ibeam',
                                    takefocus       = True,
                                    style           = 'Combobox_device_name.TCombobox')
        self.Combobox_baudrate_text = StringVar(value='')
        self.style.configure('Combobox_baudrate.TCombobox',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    relief          = 'flat')
        self.Combobox_baudrate = ttk.Combobox(self.Toplevel_connect,
                                    value           = [],
                                    textvariable    = self.Combobox_baudrate_text,
                                    justify         = 'center',
                                    exportselection = True,
                                    cursor          = 'ibeam',
                                    takefocus       = True,
                                    style           = 'Combobox_baudrate.TCombobox')
        self.Entry_idfrom_text = StringVar(value='')
        self.style.configure('Entry_idfrom.TEntry',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    relief          = 'flat',)
        self.Entry_idfrom = ttk.Entry(self.Toplevel_connect,
                                    textvariable    = self.Entry_idfrom_text,
                                    justify         = 'center',
                                    show            = '',
                                    exportselection = True,
                                    cursor          = '',
                                    takefocus       = True,
                                    style           = 'Entry_idfrom.TEntry')
        self.Entry_idto_text = StringVar(value='')
        self.style.configure('Entry_idto.TEntry',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    relief          = 'flat',)
        self.Entry_idto = ttk.Entry(self.Toplevel_connect,
                                    textvariable    = self.Entry_idto_text,
                                    justify         = 'center',
                                    show            = '',
                                    exportselection = True,
                                    cursor          = '',
                                    takefocus       = True,
                                    style           = 'Entry_idto.TEntry')
        self.Button_start_device_text = StringVar(value='开始连接')
        self.style.configure('Button_start_device.TButton',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'flat')
        self.Button_start_device = ttk.Button( self.Toplevel_connect,
                                    textvariable    = self.Button_start_device_text,
                                    image           = self.Button_start_device_pic_0,
                                    compound        = 'center',
                                    cursor          = 'hand2',
                                    takefocus       = False,
                                    command         = self.Button_start_device_bt_cmd,
                                    style           = 'Button_start_device.TButton')
        # ================ Auto Code ================ #
        # Menu
        # ================ Auto Code ================ #
        # ================ Auto Code ================ #
        self.Toplevel_connect_bind()

    def Toplevel_connect_widget_size(self):
        # ================ Auto Code ================ #
        # For place the widget : Label_2
        self.Label_2_x = 15
        self.Label_2_y = 75
        self.Label_2_w = 100
        self.Label_2_h = 30
        # For place the widget : Label_4
        self.Label_4_x = 15
        self.Label_4_y = 124
        self.Label_4_w = 100
        self.Label_4_h = 30
        # For place the widget : Label_5
        self.Label_5_x = 15
        self.Label_5_y = 174
        self.Label_5_w = 100
        self.Label_5_h = 30
        # For place the widget : Label_3
        self.Label_3_x = 15
        self.Label_3_y = 26
        self.Label_3_w = 100
        self.Label_3_h = 30
        # For place the widget : Combobox_device_name
        self.Combobox_device_name_x = 130
        self.Combobox_device_name_y = 28
        self.Combobox_device_name_w = 200
        self.Combobox_device_name_h = 30
        # For place the widget : Combobox_baudrate
        self.Combobox_baudrate_x = 130
        self.Combobox_baudrate_y = 75
        self.Combobox_baudrate_w = 200
        self.Combobox_baudrate_h = 30
        # For place the widget : Entry_idfrom
        self.Entry_idfrom_x = 130
        self.Entry_idfrom_y = 124
        self.Entry_idfrom_w = 200
        self.Entry_idfrom_h = 30
        # For place the widget : Entry_idto
        self.Entry_idto_x = 130
        self.Entry_idto_y = 174
        self.Entry_idto_w = 200
        self.Entry_idto_h = 30
        # For place the widget : Button_start_device
        self.Button_start_device_x = 109
        self.Button_start_device_y = 227
        self.Button_start_device_w = 100
        self.Button_start_device_h = 30
        # ================ Auto Code ================ #

    def Toplevel_connect_show(self):
        self.Toplevel_connect_widget_size()
        # ================ Auto Code ================ #
        self.Label_2.place(x=self.Label_2_x, y=self.Label_2_y, width=self.Label_2_w, height=self.Label_2_h, anchor='nw')
        self.Label_4.place(x=self.Label_4_x, y=self.Label_4_y, width=self.Label_4_w, height=self.Label_4_h, anchor='nw')
        self.Label_5.place(x=self.Label_5_x, y=self.Label_5_y, width=self.Label_5_w, height=self.Label_5_h, anchor='nw')
        self.Label_3.place(x=self.Label_3_x, y=self.Label_3_y, width=self.Label_3_w, height=self.Label_3_h, anchor='nw')
        self.Combobox_device_name.place(x=self.Combobox_device_name_x, y=self.Combobox_device_name_y, width=self.Combobox_device_name_w, height=self.Combobox_device_name_h, anchor='nw')
        self.Combobox_baudrate.place(x=self.Combobox_baudrate_x, y=self.Combobox_baudrate_y, width=self.Combobox_baudrate_w, height=self.Combobox_baudrate_h, anchor='nw')
        self.Entry_idfrom.place(x=self.Entry_idfrom_x, y=self.Entry_idfrom_y, width=self.Entry_idfrom_w, height=self.Entry_idfrom_h, anchor='nw')
        self.Entry_idto.place(x=self.Entry_idto_x, y=self.Entry_idto_y, width=self.Entry_idto_w, height=self.Entry_idto_h, anchor='nw')
        self.Button_start_device.place(x=self.Button_start_device_x, y=self.Button_start_device_y, width=self.Button_start_device_w, height=self.Button_start_device_h, anchor='nw')
        # ================ Auto Code ================ #

# =========================== defined for Toplevel_add_msg =========================== #
    def Toplevel_add_msg_image_load(self):
        # ================ Auto Code ================ #
        self.Label_8_pic_0 = '' 
        self.Label_9_pic_0 = '' 
        self.Label_10_pic_0 = '' 
        self.Label_1234_pic_0 = '' 
        self.Button_msg_ok_pic_0 = '' 
        self.Button_msg_cancel_pic_0 = '' 
        self.Checkbutton_crc_1_pic_0 = '' 
        self.Checkbutton_alivecounter_1_pic_0 = '' 
        self.Label_9_1_pic_0 = '' 
        # ================ Auto Code ================ #

    def Toplevel_add_msg_window_size(self):
        self.Toplevel_add_msg_width = int(690)
        self.Toplevel_add_msg_height = int(234)
        self.Toplevel_add_msg_x = int(self.winfo_x() + ((self.winfo_width() - self.Toplevel_add_msg_width)*0.5))
        self.Toplevel_add_msg_y = int(self.winfo_y() + ((self.winfo_height() - self.Toplevel_add_msg_height)*0.4))
        if self.Toplevel_add_msg_x < 0 or self.Toplevel_add_msg_y < 0:
            self.Toplevel_add_msg_x       = int((self.winfo_screenwidth() - self.Toplevel_add_msg_width)*0.5)
            self.Toplevel_add_msg_y       = int((self.winfo_screenheight() - self.Toplevel_add_msg_height)*0.4)
    def Toplevel_add_msg_bind(self):
        self.Toplevel_add_msg_root.protocol('WM_DELETE_WINDOW', self.Toplevel_add_msg_close_handler)
        self.Toplevel_add_msg.bind('<Configure>', self.Toplevel_add_msg_resize_handler)
        # ================ Auto Code ================ #
        self.Entry_d0.bind('<FocusOut>', self.Entry_d0_evt0_cmd)
        self.Entry_d1.bind('<FocusOut>', self.Entry_d1_evt0_cmd)
        self.Entry_d2.bind('<FocusOut>', self.Entry_d2_evt0_cmd)
        self.Entry_d3.bind('<FocusOut>', self.Entry_d3_evt0_cmd)
        self.Entry_d4.bind('<FocusOut>', self.Entry_d4_evt0_cmd)
        self.Entry_d5.bind('<FocusOut>', self.Entry_d5_evt0_cmd)
        self.Entry_d6.bind('<FocusOut>', self.Entry_d6_evt0_cmd)
        self.Entry_d7.bind('<FocusOut>', self.Entry_d7_evt0_cmd)
        self.Entry_id.bind('<FocusOut>', self.Entry_id_evt0_cmd)
        self.Entry_length.bind('<FocusOut>', self.Entry_length_evt0_cmd)
        # ================ Auto Code ================ #

    def Toplevel_add_msg_create(self):
        self.Toplevel_add_msg_image_load()
        self.Toplevel_add_msg_root = Toplevel(self)
        self.Toplevel_add_msg_root.title('Application')
        self.Toplevel_add_msg_window_size()
        self.Toplevel_add_msg_root.geometry('{}x{}+{}+{}'.format(self.Toplevel_add_msg_width, self.Toplevel_add_msg_height, self.Toplevel_add_msg_x, self.Toplevel_add_msg_y))
        self.Toplevel_add_msg_root.resizable(False, False)
        self.Toplevel_add_msg = Frame(self.Toplevel_add_msg_root, background='#ececec')
        self.Toplevel_add_msg.place(relx=0, rely=0, relwidth=1, relheight=1, anchor='nw')
        # Widgets
        # ================ Auto Code ================ #
        self.Entry_d0_text = StringVar(value='')
        self.style.configure('Entry_d0.TEntry',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    relief          = 'flat',)
        self.Entry_d0 = ttk.Entry(self.Toplevel_add_msg,
                                    textvariable    = self.Entry_d0_text,
                                    justify         = 'center',
                                    show            = '',
                                    exportselection = True,
                                    cursor          = '',
                                    takefocus       = True,
                                    style           = 'Entry_d0.TEntry')
        self.Entry_d1_text = StringVar(value='')
        self.style.configure('Entry_d1.TEntry',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    relief          = 'flat',)
        self.Entry_d1 = ttk.Entry(self.Toplevel_add_msg,
                                    textvariable    = self.Entry_d1_text,
                                    justify         = 'center',
                                    show            = '',
                                    exportselection = True,
                                    cursor          = '',
                                    takefocus       = True,
                                    style           = 'Entry_d1.TEntry')
        self.Entry_d2_text = StringVar(value='')
        self.style.configure('Entry_d2.TEntry',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    relief          = 'flat',)
        self.Entry_d2 = ttk.Entry(self.Toplevel_add_msg,
                                    textvariable    = self.Entry_d2_text,
                                    justify         = 'center',
                                    show            = '',
                                    exportselection = True,
                                    cursor          = '',
                                    takefocus       = True,
                                    style           = 'Entry_d2.TEntry')
        self.Entry_d3_text = StringVar(value='')
        self.style.configure('Entry_d3.TEntry',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    relief          = 'flat',)
        self.Entry_d3 = ttk.Entry(self.Toplevel_add_msg,
                                    textvariable    = self.Entry_d3_text,
                                    justify         = 'center',
                                    show            = '',
                                    exportselection = True,
                                    cursor          = '',
                                    takefocus       = True,
                                    style           = 'Entry_d3.TEntry')
        self.Entry_d4_text = StringVar(value='')
        self.style.configure('Entry_d4.TEntry',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    relief          = 'flat',)
        self.Entry_d4 = ttk.Entry(self.Toplevel_add_msg,
                                    textvariable    = self.Entry_d4_text,
                                    justify         = 'center',
                                    show            = '',
                                    exportselection = True,
                                    cursor          = '',
                                    takefocus       = True,
                                    style           = 'Entry_d4.TEntry')
        self.Entry_d5_text = StringVar(value='')
        self.style.configure('Entry_d5.TEntry',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    relief          = 'flat',)
        self.Entry_d5 = ttk.Entry(self.Toplevel_add_msg,
                                    textvariable    = self.Entry_d5_text,
                                    justify         = 'center',
                                    show            = '',
                                    exportselection = True,
                                    cursor          = '',
                                    takefocus       = True,
                                    style           = 'Entry_d5.TEntry')
        self.Entry_d6_text = StringVar(value='')
        self.style.configure('Entry_d6.TEntry',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    relief          = 'flat',)
        self.Entry_d6 = ttk.Entry(self.Toplevel_add_msg,
                                    textvariable    = self.Entry_d6_text,
                                    justify         = 'center',
                                    show            = '',
                                    exportselection = True,
                                    cursor          = '',
                                    takefocus       = True,
                                    style           = 'Entry_d6.TEntry')
        self.Entry_d7_text = StringVar(value='')
        self.style.configure('Entry_d7.TEntry',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    relief          = 'flat',)
        self.Entry_d7 = ttk.Entry(self.Toplevel_add_msg,
                                    textvariable    = self.Entry_d7_text,
                                    justify         = 'center',
                                    show            = '',
                                    exportselection = True,
                                    cursor          = '',
                                    takefocus       = True,
                                    style           = 'Entry_d7.TEntry')
        self.Entry_id_text = StringVar(value='')
        self.style.configure('Entry_id.TEntry',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    relief          = 'flat',)
        self.Entry_id = ttk.Entry(self.Toplevel_add_msg,
                                    textvariable    = self.Entry_id_text,
                                    justify         = 'center',
                                    show            = '',
                                    exportselection = True,
                                    cursor          = '',
                                    takefocus       = True,
                                    style           = 'Entry_id.TEntry')
        self.Entry_period_time_text = StringVar(value='')
        self.style.configure('Entry_period_time.TEntry',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    relief          = 'flat',)
        self.Entry_period_time = ttk.Entry(self.Toplevel_add_msg,
                                    textvariable    = self.Entry_period_time_text,
                                    justify         = 'center',
                                    show            = '',
                                    exportselection = True,
                                    cursor          = '',
                                    takefocus       = True,
                                    style           = 'Entry_period_time.TEntry')
        self.Label_8_text = StringVar(value='信号:')
        self.style.configure('Label_8.TLabel',
                                    foreground      = '#000000',
                                    background      = '#ececec',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'flat')
        self.Label_8 = ttk.Label(self.Toplevel_add_msg,
                                    textvariable    = self.Label_8_text,
                                    image           = self.Label_8_pic_0,
                                    compound        = 'center',
                                    cursor          = 'arrow',
                                    takefocus       = False,
                                    wraplength      = 100,
                                    style           = 'Label_8.TLabel')
        self.Label_9_text = StringVar(value='ID:')
        self.style.configure('Label_9.TLabel',
                                    foreground      = '#000000',
                                    background      = '#ececec',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'flat')
        self.Label_9 = ttk.Label(self.Toplevel_add_msg,
                                    textvariable    = self.Label_9_text,
                                    image           = self.Label_9_pic_0,
                                    compound        = 'center',
                                    cursor          = 'arrow',
                                    takefocus       = False,
                                    wraplength      = 100,
                                    style           = 'Label_9.TLabel')
        self.Label_10_text = StringVar(value='周期:')
        self.style.configure('Label_10.TLabel',
                                    foreground      = '#000000',
                                    background      = '#ececec',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'flat')
        self.Label_10 = ttk.Label(self.Toplevel_add_msg,
                                    textvariable    = self.Label_10_text,
                                    image           = self.Label_10_pic_0,
                                    compound        = 'center',
                                    cursor          = 'arrow',
                                    takefocus       = False,
                                    wraplength      = 100,
                                    style           = 'Label_10.TLabel')
        self.Label_1234_text = StringVar(value='ms')
        self.style.configure('Label_1234.TLabel',
                                    foreground      = '#000000',
                                    background      = '#ececec',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'flat')
        self.Label_1234 = ttk.Label(self.Toplevel_add_msg,
                                    textvariable    = self.Label_1234_text,
                                    image           = self.Label_1234_pic_0,
                                    compound        = 'center',
                                    cursor          = 'arrow',
                                    takefocus       = False,
                                    wraplength      = 32,
                                    style           = 'Label_1234.TLabel')
        self.Button_msg_ok_text = StringVar(value='确  定')
        self.style.configure('Button_msg_ok.TButton',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'flat')
        self.Button_msg_ok = ttk.Button( self.Toplevel_add_msg,
                                    textvariable    = self.Button_msg_ok_text,
                                    image           = self.Button_msg_ok_pic_0,
                                    compound        = 'center',
                                    cursor          = 'hand2',
                                    takefocus       = False,
                                    command         = self.Button_msg_ok_bt_cmd,
                                    style           = 'Button_msg_ok.TButton')
        self.Button_msg_cancel_text = StringVar(value='取  消')
        self.style.configure('Button_msg_cancel.TButton',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'flat')
        self.Button_msg_cancel = ttk.Button( self.Toplevel_add_msg,
                                    textvariable    = self.Button_msg_cancel_text,
                                    image           = self.Button_msg_cancel_pic_0,
                                    compound        = 'center',
                                    cursor          = 'hand2',
                                    takefocus       = False,
                                    command         = self.Button_msg_cancel_bt_cmd,
                                    style           = 'Button_msg_cancel.TButton')
        self.LabelFrame_1 = LabelFrame(self.Toplevel_add_msg,
                                    foreground      = '#000000',
                                    background      = '#ececec',
                                    text            = '特殊格式',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    labelanchor     = 'nw',
                                    relief          = 'groove',
                                    cursor          = 'arrow',
                                    takefocus       = False)
        self.Checkbutton_crc_1_text = StringVar(value='CRC')
        self.Checkbutton_crc_1_value = BooleanVar(value=False)
        self.style.configure('Checkbutton_crc_1.TCheckbutton',
                                    foreground      = '#000000',
                                    background      = '#ececec',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'flat')
        self.Checkbutton_crc_1 = ttk.Checkbutton( self.LabelFrame_1,
                                    textvariable    = self.Checkbutton_crc_1_text,
                                    variable        = self.Checkbutton_crc_1_value,
                                    offvalue        = False,
                                    onvalue         = True,
                                    image           = self.Checkbutton_crc_1_pic_0,
                                    compound        = 'center',
                                    cursor          = 'hand2',
                                    takefocus       = True,
                                    style           = 'Checkbutton_crc_1.TCheckbutton',
                                    command         = self.Checkbutton_crc_1_bt_cmd)
        self.Checkbutton_alivecounter_1_text = StringVar(value='Alivecounter')
        self.Checkbutton_alivecounter_1_value = BooleanVar(value=False)
        self.style.configure('Checkbutton_alivecounter_1.TCheckbutton',
                                    foreground      = '#000000',
                                    background      = '#ececec',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'flat')
        self.Checkbutton_alivecounter_1 = ttk.Checkbutton( self.LabelFrame_1,
                                    textvariable    = self.Checkbutton_alivecounter_1_text,
                                    variable        = self.Checkbutton_alivecounter_1_value,
                                    offvalue        = False,
                                    onvalue         = True,
                                    image           = self.Checkbutton_alivecounter_1_pic_0,
                                    compound        = 'center',
                                    cursor          = 'hand2',
                                    takefocus       = True,
                                    style           = 'Checkbutton_alivecounter_1.TCheckbutton',
                                    command         = self.Checkbutton_alivecounter_1_bt_cmd)
        self.Entry_length_text = StringVar(value='')
        self.style.configure('Entry_length.TEntry',
                                    foreground      = '#000000',
                                    background      = '#FFFFFF',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    relief          = 'flat',)
        self.Entry_length = ttk.Entry(self.Toplevel_add_msg,
                                    textvariable    = self.Entry_length_text,
                                    justify         = 'center',
                                    show            = '',
                                    exportselection = True,
                                    cursor          = '',
                                    takefocus       = True,
                                    style           = 'Entry_length.TEntry')
        self.Label_9_1_text = StringVar(value='长度:')
        self.style.configure('Label_9_1.TLabel',
                                    foreground      = '#000000',
                                    background      = '#ececec',
                                    font            = ['Airal', 9, 'normal', 'roman'],
                                    anchor          = 'center',
                                    justify         = 'center',
                                    relief          = 'flat')
        self.Label_9_1 = ttk.Label(self.Toplevel_add_msg,
                                    textvariable    = self.Label_9_1_text,
                                    image           = self.Label_9_1_pic_0,
                                    compound        = 'center',
                                    cursor          = 'arrow',
                                    takefocus       = False,
                                    wraplength      = 100,
                                    style           = 'Label_9_1.TLabel')
        # ================ Auto Code ================ #
        # Menu
        # ================ Auto Code ================ #
        # ================ Auto Code ================ #
        self.Toplevel_add_msg_bind()

    def Toplevel_add_msg_widget_size(self):
        # ================ Auto Code ================ #
        # For place the widget : Entry_d0
        self.Entry_d0_x = 156
        self.Entry_d0_y = 33
        self.Entry_d0_w = 50
        self.Entry_d0_h = 30
        # For place the widget : Entry_d1
        self.Entry_d1_x = 216
        self.Entry_d1_y = 33
        self.Entry_d1_w = 50
        self.Entry_d1_h = 30
        # For place the widget : Entry_d2
        self.Entry_d2_x = 277
        self.Entry_d2_y = 33
        self.Entry_d2_w = 50
        self.Entry_d2_h = 30
        # For place the widget : Entry_d3
        self.Entry_d3_x = 338
        self.Entry_d3_y = 33
        self.Entry_d3_w = 50
        self.Entry_d3_h = 30
        # For place the widget : Entry_d4
        self.Entry_d4_x = 399
        self.Entry_d4_y = 33
        self.Entry_d4_w = 50
        self.Entry_d4_h = 30
        # For place the widget : Entry_d5
        self.Entry_d5_x = 460
        self.Entry_d5_y = 33
        self.Entry_d5_w = 50
        self.Entry_d5_h = 30
        # For place the widget : Entry_d6
        self.Entry_d6_x = 521
        self.Entry_d6_y = 33
        self.Entry_d6_w = 50
        self.Entry_d6_h = 30
        # For place the widget : Entry_d7
        self.Entry_d7_x = 585
        self.Entry_d7_y = 33
        self.Entry_d7_w = 50
        self.Entry_d7_h = 30
        # For place the widget : Entry_id
        self.Entry_id_x = 156
        self.Entry_id_y = 65
        self.Entry_id_w = 50
        self.Entry_id_h = 30
        # For place the widget : Entry_period_time
        self.Entry_period_time_x = 156
        self.Entry_period_time_y = 130
        self.Entry_period_time_w = 50
        self.Entry_period_time_h = 30
        # For place the widget : Label_8
        self.Label_8_x = 42
        self.Label_8_y = 33
        self.Label_8_w = 100
        self.Label_8_h = 30
        # For place the widget : Label_9
        self.Label_9_x = 42
        self.Label_9_y = 65
        self.Label_9_w = 100
        self.Label_9_h = 30
        # For place the widget : Label_10
        self.Label_10_x = 42
        self.Label_10_y = 130
        self.Label_10_w = 100
        self.Label_10_h = 30
        # For place the widget : Label_1234
        self.Label_1234_x = 214
        self.Label_1234_y = 130
        self.Label_1234_w = 32
        self.Label_1234_h = 30
        # For place the widget : Button_msg_ok
        self.Button_msg_ok_x = 198
        self.Button_msg_ok_y = 181
        self.Button_msg_ok_w = 100
        self.Button_msg_ok_h = 30
        # For place the widget : Button_msg_cancel
        self.Button_msg_cancel_x = 385
        self.Button_msg_cancel_y = 181
        self.Button_msg_cancel_w = 100
        self.Button_msg_cancel_h = 30
        # For place the widget : LabelFrame_1
        self.LabelFrame_1_x = 432
        self.LabelFrame_1_y = 73
        self.LabelFrame_1_w = 200
        self.LabelFrame_1_h = 85
        # For place the widget : Checkbutton_crc_1
        self.Checkbutton_crc_1_x = 32
        self.Checkbutton_crc_1_y = 31
        self.Checkbutton_crc_1_w = 130
        self.Checkbutton_crc_1_h = 30
        # For place the widget : Checkbutton_alivecounter_1
        self.Checkbutton_alivecounter_1_x = 32
        self.Checkbutton_alivecounter_1_y = 3
        self.Checkbutton_alivecounter_1_w = 130
        self.Checkbutton_alivecounter_1_h = 30
        # For place the widget : Entry_length
        self.Entry_length_x = 156
        self.Entry_length_y = 97
        self.Entry_length_w = 50
        self.Entry_length_h = 30
        # For place the widget : Label_9_1
        self.Label_9_1_x = 42
        self.Label_9_1_y = 97
        self.Label_9_1_w = 100
        self.Label_9_1_h = 30
        # ================ Auto Code ================ #

    def Toplevel_add_msg_show(self):
        self.Toplevel_add_msg_widget_size()
        # ================ Auto Code ================ #
        self.Entry_d0.place(x=self.Entry_d0_x, y=self.Entry_d0_y, width=self.Entry_d0_w, height=self.Entry_d0_h, anchor='nw')
        self.Entry_d1.place(x=self.Entry_d1_x, y=self.Entry_d1_y, width=self.Entry_d1_w, height=self.Entry_d1_h, anchor='nw')
        self.Entry_d2.place(x=self.Entry_d2_x, y=self.Entry_d2_y, width=self.Entry_d2_w, height=self.Entry_d2_h, anchor='nw')
        self.Entry_d3.place(x=self.Entry_d3_x, y=self.Entry_d3_y, width=self.Entry_d3_w, height=self.Entry_d3_h, anchor='nw')
        self.Entry_d4.place(x=self.Entry_d4_x, y=self.Entry_d4_y, width=self.Entry_d4_w, height=self.Entry_d4_h, anchor='nw')
        self.Entry_d5.place(x=self.Entry_d5_x, y=self.Entry_d5_y, width=self.Entry_d5_w, height=self.Entry_d5_h, anchor='nw')
        self.Entry_d6.place(x=self.Entry_d6_x, y=self.Entry_d6_y, width=self.Entry_d6_w, height=self.Entry_d6_h, anchor='nw')
        self.Entry_d7.place(x=self.Entry_d7_x, y=self.Entry_d7_y, width=self.Entry_d7_w, height=self.Entry_d7_h, anchor='nw')
        self.Entry_id.place(x=self.Entry_id_x, y=self.Entry_id_y, width=self.Entry_id_w, height=self.Entry_id_h, anchor='nw')
        self.Entry_period_time.place(x=self.Entry_period_time_x, y=self.Entry_period_time_y, width=self.Entry_period_time_w, height=self.Entry_period_time_h, anchor='nw')
        self.Label_8.place(x=self.Label_8_x, y=self.Label_8_y, width=self.Label_8_w, height=self.Label_8_h, anchor='nw')
        self.Label_9.place(x=self.Label_9_x, y=self.Label_9_y, width=self.Label_9_w, height=self.Label_9_h, anchor='nw')
        self.Label_10.place(x=self.Label_10_x, y=self.Label_10_y, width=self.Label_10_w, height=self.Label_10_h, anchor='nw')
        self.Label_1234.place(x=self.Label_1234_x, y=self.Label_1234_y, width=self.Label_1234_w, height=self.Label_1234_h, anchor='nw')
        self.Button_msg_ok.place(x=self.Button_msg_ok_x, y=self.Button_msg_ok_y, width=self.Button_msg_ok_w, height=self.Button_msg_ok_h, anchor='nw')
        self.Button_msg_cancel.place(x=self.Button_msg_cancel_x, y=self.Button_msg_cancel_y, width=self.Button_msg_cancel_w, height=self.Button_msg_cancel_h, anchor='nw')
        self.LabelFrame_1.place(x=self.LabelFrame_1_x, y=self.LabelFrame_1_y, width=self.LabelFrame_1_w, height=self.LabelFrame_1_h, anchor='nw')
        self.Checkbutton_crc_1.place(x=self.Checkbutton_crc_1_x, y=self.Checkbutton_crc_1_y, width=self.Checkbutton_crc_1_w, height=self.Checkbutton_crc_1_h, anchor='nw')
        self.Checkbutton_alivecounter_1.place(x=self.Checkbutton_alivecounter_1_x, y=self.Checkbutton_alivecounter_1_y, width=self.Checkbutton_alivecounter_1_w, height=self.Checkbutton_alivecounter_1_h, anchor='nw')
        self.Entry_length.place(x=self.Entry_length_x, y=self.Entry_length_y, width=self.Entry_length_w, height=self.Entry_length_h, anchor='nw')
        self.Label_9_1.place(x=self.Label_9_1_x, y=self.Label_9_1_y, width=self.Label_9_1_w, height=self.Label_9_1_h, anchor='nw')
        # ================ Auto Code ================ #
