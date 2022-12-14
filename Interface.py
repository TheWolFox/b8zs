#!/usr/bin/python3
import tkinter as tk

class selectorWindow:
    def getData(self):
        ip = self.ip_input.get()
        port = self.port_input.get();
        print('oi')
        print(ip, port)

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
        self.host = tk.Button(self.window, command=lambda: self.getData())
        self.host.configure(
            background="#b8c0ff",
            compound="none",
            cursor="based_arrow_down",
            overrelief="raised",
            text='host',
            width=7)
        self.host.pack(side="left")
        self.client = tk.Button(self.window)
        self.client.configure(background="#b8c0ff", text='client', width=7)
        self.client.pack(side="bottom")

        self.window.title("Configuracao")
        # Main widget
        self.mainwindow = self.window
        
    

    def run(self):
        self.mainwindow.mainloop()
