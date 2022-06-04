version=1.3
up_version=1.4
update_time='2022-06-02'

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random
import platform


白色='white'
浅浅灰色='#f4f4f4'
浅灰色='#ececec'
灰色='#cecece'
深灰色='#858585'
深深灰色='#4b4b4b'
黑色='black'
粉色='#ff7373'
浅粉色='#ff9c9c'
浅浅粉色='#f4cccc'

xlaw,xstart,xsetting,xgame,xabout=False,False,False,False,False

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
    menu_about=tk.Menu(menu_top,tearoff=False)
    style(menu_about,'检查更新(推荐)',粉色,update)
    style(menu_about,'意见反馈',深灰色,restart)
    menu_about.add_separator(background=白色)# 添加一条分割线
    style(menu_about,'关于Conjecture',浅粉色,about)
    menu_top.add_cascade(label="关于",activebackground=白色,background=白色,menu=menu_about)#顶层菜单绑定下拉菜单
    
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
#主窗体模板
class windows(tk.Tk):
    def win(self,label,color,x,y):
        self.title(label)#窗体标题
        width=x
        height=y
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        self.geometry('%dx%d+%d+%d'%(width, height, (screenwidth-width)/2, (screenheight-height)/2))
        self.resizable(width=False, height=False)#禁止更改宽和高
        self.config(bg=color)#设置窗体颜色
        self.iconbitmap('E:/Users/Administrator/Desktop/MobileFile/数.ico')#设置图标
    
    #窗体关闭关联事件
    def cut(self,function):
        self.protocol('WM_DELETE_WINDOW', function)

#画布：开始界面
def start():
    global list_frame,frame_start,xstart
    
    if xstart==False:
        #表面功能
        frame_start=tk.Frame(win,bg=白色)
        list_frame.append(frame_start)
        
        Lab_start=tk.Label(frame_start,pady=4,padx=31,text='Conjecture',bg=白色,fg=深深灰色,font=('等线',40,'bold'),height=1,width=0,anchor='sw')
        Lab_start.grid(sticky='n',ipadx=0,ipady=17,row=0,column=0)#放置标签
        But_start=tk.Button(frame_start,padx=0,text="开始",bg=白色,fg=灰色,activebackground=白色,highlightcolor=深深灰色,cursor='plus',font=('楷体',25,'bold'),bd=0,anchor='center',command=game)
        But_start.grid(sticky='w',padx=140,pady=115,row=0,column=0)#放置按钮
        
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
    global list_frame,frame_about,xabout,version,update_time
    
    if xabout==False:
        frame_about=tk.Frame(win,bg=白色)
        list_frame.append(frame_about)
        
        信息=str(platform.platform())+'-'+str(platform.architecture()[0])+'\n版本日期:'+update_time+'\nConjecture版本:v'+str(version)
        
        Lab_about=tk.Label(frame_about,pady=10,padx=54,text='Conjecture',bg=白色,fg=黑色,font=('等线',40,'bold'),height=0,width=0,anchor='n')
        Lab_about.grid(sticky='n',pady=0,ipadx=0,ipady=24,row=0,column=0)#放置标签
        Lab_about=tk.Label(frame_about,pady=0,padx=0,text=str(信息),bg=白色,fg=黑色,font=('等线',8,'bold'),height=0,width=0,anchor='center')
        Lab_about.grid(sticky='n',padx=54,pady=75,ipadx=0,ipady=0,row=0,column=0)#放置标签
        Lab_about=tk.Label(frame_about,pady=0,padx=0,text='By  绫袅  编写于2022-06-02',bg=白色,fg=粉色,font=('等线',12,'bold'),height=0,width=0,anchor='center')
        Lab_about.grid(sticky='n',padx=54,pady=120,ipadx=20,ipady=0,row=0,column=0)#放置标签
        But_about=tk.Button(frame_about,padx=22,text="确认",bg=白色,fg=黑色,activebackground=白色,activeforeground=粉色,cursor='heart',font=('楷体',14),bd=1,anchor='center',command=start)
        But_about.grid(sticky='w',padx=140,pady=150,row=0,column=0)#放置按钮
        
        change(frame_about)
        xstart=True
    else:
        change(frame_start)
    

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

#画布：检查更新
def update():
    global version,up_version
    if up_version>version:
        win_up=windows()
        win_up.win('提示信息',白色,180,70)
        win_up.lift(aboveThis=win)
        win_up.mainloop()
    else:
        
        showinfo(title='提示信息',message='当前已经是最新版！')


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
def 猜数字():       
    #主桌面
    global list_frame,win,list_win
    win=windows()
    win.win('Conjecture',白色,400,218)
    
    list_frame=[]
    list_win=[]
    start()#开始
    menu()#主菜单

    win.mainloop()#将窗体显示出来
    
猜数字()
