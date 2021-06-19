# CAN View Pro

## 软件特性
- Done
 - 实现pcan view的功能
 - 实现发送报文的CRC和alivecounter位的填充
 - 实现加载dbc并解析，can变量的功能
- TODO
 - 界面能够记录并显示trace
 - 保存trace


## 软件更新记录
 - 2021/6/19 解决dbc文件中不同id中存在相同信号，导致软件阻塞的问题
 - 2021/6/19 self.update_Treeview_recv_msg() dictionary changed size during iteration