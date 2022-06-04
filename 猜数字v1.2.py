import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random

白色='white'
浅浅灰色='#f4f4f4'
浅灰色='#ececec'
灰色='#cecece'
深灰色='#858585'
黑色='black'

#主桌面
win = tk.Tk()
win.title("Conjecture")#窗体标题
win.geometry("400x218+670+340")#设置窗体显示屏幕上的位置
win.resizable(width=False, height=False)#禁止更改宽和高
win.config(bg=白色)#设置窗体颜色
win.iconbitmap('E:/Users/Administrator/Desktop/MobileFile/数.ico')#设置图标





#菜单表
def menu():
    #添加特定样式菜单选项
    def style(menu,label,color,command):
        menu.add_command(label=label,activebackground=color,command=command,background=白色)
    
    #顶层菜单创建
    menu_top=tk.Menu(win,activebackground=深灰色,bg=灰色,selectcolor='black',bd=0,relief='flat')
    
    #menu_set选项菜单
    menu_set=tk.Menu(menu_top,tearoff=False)
    style(menu_set,'保存',黑色,start)
    style(menu_set,'重新开始',黑色,restart)
    style(menu_set,'回到游戏',深灰色,back)
    style(menu_set,'游戏规则',深灰色,law)
    style(menu_set,'高级设置',深灰色,setting)
    menu_set.add_separator(background=白色)# 添加一条分割线
    style(menu_set,'退出',黑色,win.destroy)
    menu_top.add_cascade(label="选项",activebackground=白色,background=白色,menu=menu_set)#顶层菜单绑定下拉菜单
    
    #menu_about关于菜单
    menu_top.add_command(label="关于")
    
    #显示菜单
    win.config(menu=menu_top)
    
    #右键菜单创建
    global list_frame
    for i in list_frame:
        menu_mouse=tk.Menu(i,tearoff=False)
        
    #添加快捷键
    style(menu_mouse,'开始界面',深灰色,start)
    style(menu_mouse,'回到游戏',深灰色,back)
    style(menu_mouse,'高级设置',深灰色,setting)
    style(menu_mouse,'游戏规则',深灰色,law)
    menu_mouse.add_separator(background=白色)# 添加一条分割线
    style(menu_mouse,'重新开始',黑色,restart)
    
    #右键菜单绑定事件
    def command(event):# 定义事件函数
        menu_mouse.post(event.x_root, event.y_root)# 使用 post()在指定的位置显示弹出菜单
    win.bind("<Button-3>",command)# 绑定鼠标右键，这是鼠标绑定事件




#画布表
xlaw,xstart,xsetting,xgame=False,False,False,False
#画布：开始界面
def start():
    global list_frame,frame_start,xstart
    
    if xstart==False:
        frame_start=tk.Frame(win,bg=白色)
        list_frame.append(frame_start)
        
        Lab_start=tk.Label(frame_start,pady=4,padx=21,text='数 Conjecture',bg=白色,font=('等线',40,'bold'),height=1,width=0,anchor='sw')
        Lab_start.grid(sticky='n',ipadx=37,ipady=24,row=0,column=0)#放置标签
        But_start=tk.Button(frame_start,padx=0,text="开始",bg=白色,fg=深灰色,font=('楷体',25,'bold'),bd=0,anchor='center',command=game)
        But_start.grid(sticky='w',padx=147,pady=110,row=0,column=0)#放置按钮
        frame_start.grid(padx=10,column=0,row=0)
        xstart=True
    else:
        change(frame_start)
    
#画布：选项页面
def setting():
    global list_frame,frame_setting,xsetting
    
    if xsetting==False:
        frame_setting=tk.Frame(win,bg=白色)
        list_frame.append(frame_setting)

        comb_hard=tk.ttk.Combobox(frame_setting)#创建难度列表
        comb_hard['value']=(0,1,2,3,4,5,6,7,8,9)
        comb_hard.current(5)
        
        def hard():#绑定游戏难度
            pass
            
        Lab_setting=tk.Button(frame_setting,text='选定难度',bd=1,command=hard)#游戏难度选择
        
        change(frame_setting)
        xsetting=True
    else:
        change(frame_setting)
        
#画布:规则界面
def law():#规则函数
    global list_frame,frame_law,xlaw
    
    if xlaw==False:
        frame_law=tk.Frame(win,bg=白色)
        list_frame.append(frame_law)
        
        title="数 Conjecture"#规则描述
        little='游戏规则：'
        text_1='''1.以游戏难度5为例，系统随机产出一个5位数字且每个位上的数字各不相同。 2.首先你需要猜出一个长度相同的数字，系统会将你所给的这一串数字与系统随机产生的数进行对比，返回相同数字的个数与猜对的数字的所在位置的个数。 3.你需要进行推理，尽量在更少的试错次数下，找出正确答案，获得更低的分数。'''
        Lab_law_title=tk.Label(frame_law,text=title,pady=10,justify='left',font=('等线',25),bg=白色).grid(sticky='w')
        Lab_law_little=tk.Label(frame_law,text=little,font=('等线',16),justify='left',anchor='n',bg=白色).grid(sticky='w')
        Lab_law_Text_1=tk.Label(frame_law,text=text_1,font=('等线',10),bg=白色,justify='left',wraplength=380,anchor='w').grid(sticky='w')
        change(frame_law)
        xlaw=True
    else:
        change(frame_law)
        win.update()

#画布：关于界面
def about():
    pass

#画布：反馈界面
def feedback():
    pass

#画布：排行界面
def rank():
    pass

#画布：游戏界面
def game():
    global frame_game,list_frame,xgame,list_box
    
    if xgame==False:
        frame_game=tk.Frame(win,bg=白色)
        list_frame.append(frame_game)
        frame_game.grid(padx=10,column=0,row=0)
        xgame=True
        
        run_text='游戏暂未开始...'
        text_game='开始'
        list_box=['历史记录']#游戏历史数据表
        str_but_game=tk.StringVar()

        #界面控件
        But_game=tk.Button(frame_game,text=text_game,relief='flat',bd=0,bg=浅灰色,activebackground=灰色,justify='center')
        But_game.grid(padx=312,pady=158,ipadx=16,ipady=3,row=0,column=0,sticky='nw')
        Lab_run=tk.Label(frame_game,bd=1,bg=浅灰色,height=6,width=25,highlightthickness=1)
        Lab_run.grid(padx=193,pady=8,row=0,column=0,sticky='wn')
        box_game=tk.Listbox(frame_game,bd=0,width=25,bg=白色,highlightthickness=1,highlightbackground=灰色,highlightcolor=灰色,selectbackground='black',selectmode='single',takefocus=False,justify='center')#创建游戏历史列表
        box_game.grid(pady=8,padx=5,row=0,column=0,sticky='wn')
        entry_game=tk.Entry(frame_game,bg=浅灰色,bd=5,width=14,relief='flat',selectbackground='black',insertbackground=深灰色,highlightbackground='black',highlightcolor='black')
        entry_game.grid(padx=193,pady=159,ipady=1,row=0,column=0,sticky='wn')

        
        #游戏主程序
        
        
        #显示历史信息
        for k in list_box:
            box_game.insert('end',k)
    else:
        change(frame_game)
        


#函数表

#切换到frame界面
def change(frame):
    global list_frame
    for i in list_frame:
        i.grid_forget()
    frame.grid(padx=10,column=0,row=0)
    
#关闭某控件/窗口
def destroy(item):
    item.destroy()
    
#回到游戏
def back():
    global xgame
    if xgame==True:
        game()
    else:
        showinfo(title='提示信息',message='游戏未进行！')
    
#重新开始
def restart():
    global xgame,list_frame
    if xgame==True:
        frame_game.destroy()
        list_frame.remove(frame_game)
        change(frame_start)
        xgame=False
    else:
        showinfo(title='提示信息',message='游戏未开始！')
        


#主进程
list_frame=[]
start()#开始
menu()#主菜单


    
    
win.mainloop()#将窗体显示出来