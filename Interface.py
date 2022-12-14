#!/usr/bin/python3
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class selectorWindow:
    def createSender(self):
        ip = self.ip_input.get()
        port = self.port_input.get();
        print('oi')
        print(ip, port)
        self.window.destroy()
        sender = messageWindow('client')
        sender.run()
    
    def createHost(self):
        ip = self.ip_input.get()
        port = self.port_input.get();
        self.window.destroy()
        host = messageWindow('host')
        host.run()

    def __init__(self, master=None):
        # build ui
        self.window = tk.Tk() if master is None else tk.Toplevel(master)
        self.window.configure(
            background="#e7c6ff",
            height=200,
            padx=30,
            pady=30,
            width=200)
        self.ip = tk.Label(self.window)
        self.ip.configure(
            background="#e7c6ff",
            font="{poppins} 10 {}",
            text='IP address:')
        self.ip.pack(side="top")
        self.ip_input = tk.Entry(self.window)
        self.ip_input.pack(side="top")
        self.port = tk.Label(self.window)
        self.port.configure(
            background="#e7c6ff",
            compound="center",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Port:')
        self.port.pack(side="top")
        self.port_input = tk.Entry(self.window)
        self.port_input.pack(side="top")
        self.host = tk.Button(self.window, command=lambda: self.createHost())
        self.host.configure(
            background="#b8c0ff",
            compound="none",
            cursor="based_arrow_down",
            overrelief="raised",
            text='host',
            width=7)
        self.host.pack(side="left")
        self.client = tk.Button(self.window, command=lambda: self.createSender())
        self.client.configure(background="#b8c0ff", text='client', width=7)
        self.client.pack(side="bottom")

        self.window.title("Config")
        # Main widget
        self.mainwindow = self.window

    def run(self):
        self.mainwindow.mainloop()

class messageWindow:

    def recieveMessage(self):
        self.message_data.insert(tk.END, "HEHEHEHHE")

    def __init__(self, fun, master=None, ):
        # build ui
        self.messageWindow = tk.Tk() if master is None else tk.Toplevel(master)
        self.messageWindow.configure(
            background="#e7c6ff", height=200, width=200)
        self.title = tk.Label(self.messageWindow)
        self.title.configure(background="#e7c6ff", text='Message Data')
        self.title.pack(side="top")
        self.message_data = tk.Text(self.messageWindow)
        self.message_data.configure(height=10, width=50)
        self.message_data.pack(side="top")
        self.m_title = tk.Label(self.messageWindow)
        self.m_title.configure(background="#e7c6ff", text='Message')
        self.m_title.pack(side="top")
        self.message_input = tk.Entry(self.messageWindow)
        self.message_input.configure(width=50)
        self.message_input.pack(side="top")

        self.button = tk.Button(self.messageWindow)
        if fun == 'host':      
            self.button.configure(background="#b8c0ff", text='Recieve', command=lambda: self.recieveMessage())
        else:
            self.button.configure(background="#b8c0ff", text='Send')
        
        self.button.pack(side="top")

        self.messageWindow.title(fun)
        # Main widget
        self.mainwindow = self.messageWindow

    def run(self):
        self.mainwindow.mainloop()