# -*- coding: utf-8 -*-
# author:BerryHN
from tkinter import *
class  WidgetsDemo:
    def __init__(self):
        window=Tk()
        window.title("第一个测试demo")
        frame1=Frame(window)
        frame1.pack()
        self.v1=IntVar()
        cbtBold=Checkbutton(frame1,text="加粗",variable=self.v1,command=self.processCheckbutton)
        self.v2=IntVar()
        rbRed=Radiobutton(frame1,text="红色",bg="red",variable=self.v2,value=1,command=self.processRadiobutton())
        rbYellow=Radiobutton(frame1,text="黄色",bg="yellow",variable=self.v2,value=2,command=self.processRadiobutton())
        cbtBold.grid(row=1,column=1)
        rbRed.grid(row=1,column=2)
        rbYellow.grid(row=1,column=3)
        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text="请输入名字")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable=self.name)
        btGetName = Button(frame2, text="获取名字", command=self.processButton)
        message = Message(frame2, text="组建demo")
        label.grid(row=1, column=1)
        entryName.grid(row=1, column=2)
        btGetName.grid(row=1, column=3)
        message.grid(row=1, column=4)
        # 添加一个tex
        text = Text(window)
        text.pack()
        text.insert(END, "Tip\n最好的学习TKinter方式是读\n")  # END表示插入到当前文本最后
        text.insert(END, "这是一些很好的学习例子使用他们\n")
        text.insert(END, "创建你自己的应用吧\n")
        window.mainloop()

    def processCheckbutton(self):
        print("复选按钮是"+("被选中" if self.v1.get()==1 else "未选中"))
    def processRadiobutton(self):
        print("红色是"+("被选中" if self.v2.get()==1 else "未选中"))
    def processButton(self):
        print("你的名字是"+self.name.get())



WidgetsDemo()