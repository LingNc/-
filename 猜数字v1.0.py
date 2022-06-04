import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo
import random

#颜色列表
color='white'
白色=color
浅灰色='#ececec'
浅浅灰色='#f4f4f4'
灰色='#cecece'
深灰色='#858585'
黑色='black'
list_frame=[]#画布列表

class Func:
    #属性
    list_frame=[]
    #方法
    #隐藏除x外xlist中的控件
    def hide(self,x,xlist):
        for i in self.xlist:
            i.grid_forget()
        self.x.grid(padx=10,row=0)#布局
        win.update()#更新界面
    #画布创建
    def frame(self,win):
        #画布：开始界面
        frame_top=tkinter.Frame(win,bg=color)
        list_frame.append(frame_top)
        #画布：规则页面
        frame_law=tkinter.Frame(win,bg=color)
        list_frame.append(frame_law)
        #画布：选项页面
        frame_setting=tkinter.Frame(win,bg=color)
        list_frame.append(frame_setting)
              


#主窗体
win = tkinter.Tk()
win.title("Conjecture")#窗体标题
win.geometry("400x218+670+340")#设置窗体显示屏幕上的位置
win.resizable(width=False, height=False)#禁止更改宽和高
win.config(bg=color)#设置窗体颜色
win.iconbitmap('E:/Users/Administrator/Desktop/MobileFile/数.ico')#设置图标



global game_judge#判断游戏是否正在进行】
game_judge=False


def game():#创建游戏页面
    #声明全局变量
    global list_box,run_text,text_game,str_but_game,But_game,Lab_run,box_game,entry_game,frame_game
    global list_frame
    #画布：游戏页面
    frame_game=tkinter.Frame(win,bg=color)
    list_frame.append(frame_game)
    
    list_box=['历史记录']#游戏历史数据表
    run_text='游戏暂未开始...'
    text_game='开始'
    str_but_game=tkinter.StringVar()

    #界面控件
    But_game=tkinter.Button(frame_game,text=text_game,relief='flat',bd=0,bg=浅灰色,activebackground=灰色,justify='center')
    But_game.grid(padx=312,pady=158,ipadx=16,ipady=3,row=0,column=0,sticky='nw')
    Lab_run=tkinter.Label(frame_game,bd=1,bg=浅灰色,height=6,width=25,highlightthickness=1)
    Lab_run.grid(padx=193,pady=8,row=0,column=0,sticky='wn')
    box_game=tkinter.Listbox(frame_game,bd=0,width=25,bg=白色,highlightthickness=1,highlightbackground=灰色,highlightcolor=灰色,selectbackground='black',selectmode='single',takefocus=False,justify='center')#创建游戏历史列表
    box_game.grid(pady=8,padx=5,row=0,column=0,sticky='wn')
    entry_game=tkinter.Entry(frame_game,bg=浅灰色,bd=5,width=14,relief='flat',selectbackground='black',insertbackground=深灰色,highlightbackground='black',highlightcolor='black')
    entry_game.grid(padx=193,pady=159,ipady=1,row=0,column=0,sticky='wn')
    #显示历史信息
    for k in list_box:
        box_game.insert('end',k)
    
    #切换到游戏界面
    hide(frame_game,list_frame)
    global game_judge#判断游戏是否正在进行
    game_judge=True
    

#开始页面
Lab_start=tkinter.Label(frame_top,pady=4,padx=21,text='数 Conjecture',bg=color,font=('等线',40,'bold'),height=1,width=0,anchor='sw')
Lab_start.grid(sticky='n',ipadx=37,ipady=14,row=0,column=0)#放置标签
But_start=tkinter.Button(frame_top,padx=0,text="开始",bg=color,fg=深灰色,font=('楷体',25,'bold'),bd=0,anchor='center',command=game)
But_start.grid(sticky='w',padx=147,pady=110,row=0,column=0)#放置按钮
frame_top.grid(padx=10,column=0,row=0)#放置主界面

#box_game=tkinter.Listbox(frame_game,bd=0,bg=浅灰色,selectbackground=灰色,selectmode='single',yscrollcommand=True,takefocus=False)#创建游戏历史列表
#scro_game=tkinter.Scrollbar(box_game,width=12,troughcolor=color,bg=color,activebackground=灰色)
#box_game.config(yscrollcommand=scro_game.set)
#scro_game.config(command=box_game.yview)
#box_game.grid(pady=10,ipadx=60,ipady=64)#创建列表框
#scro_game.pack(side='right',fill='y')#创建滚动条



#画布:规则界面
def law():#规则函数
    global frame_law,list_frame
    frame_law=tkinter.Frame(win,bg=color)
    list_frame.append(frame_law)
    title="数 Conjecture"#规则描述
    little='游戏规则：'
    text_1='''1.以游戏难度5为例，系统随机产出一个5位数字且每个位上的数字各不相同。 2.首先你需要猜出一个长度相同的数字，系统会将你所给的这一串数字与系统随机产生的数进行对比，返回相同数字的个数与猜对的数字的所在位置的个数。 3.你需要进行推理，尽量在更少的试错次数下，找出正确答案，获得更低的分数。'''
    Lab_law_title=tkinter.Label(frame_law,text=title,pady=10,justify='left',font=('等线',25),bg=color).grid(sticky='w')
    Lab_law_little=tkinter.Label(frame_law,text=little,font=('等线',16),justify='left',anchor='n',bg=color).grid(sticky='w')
    Lab_law_Text_1=tkinter.Label(frame_law,text=text_1,font=('等线',10),bg=color,justify='left',wraplength=380,anchor='w').grid(sticky='w')
    hide(frame_law,list_frame)#放置规则界面
    
def top_map():#回到主页
    hide(frame_top,list_frame)#放置主界面
        

#画布：游戏选项页面
def setting():#游戏选项页面显示
    global frame_setting,list_frame
    frame_setting=tkinter.Frame(win,bg=color)
    list_frame.append(frame_setting)
    hide(frame_setting,list_frame)
    comb_hard=tkinter.ttk.Combobox(frame_setting)#创建难度列表
    comb_hard['value']=(0,1,2,3,4,5,6,7,8,9)
    comb_hard.current(5)
    def hard():#绑定游戏难度
        pass
        
    Lab_setting=tkinter.Button(frame_setting,text='选定难度',bd=1,command=hard)#游戏难度选择


    
#顶层菜单
menu_1=tkinter.Menu(win,activebackground=深灰色,bg=灰色,selectcolor='black',bd=0,relief='flat')#主菜单

def back_game():#回到游戏函数
    global game_judge
    if game_judge==True:
        hide(frame_game,list_frame)
    else:
        showinfo(title='提示信息',message='游戏暂未开始！')

def restart():#重新开始
    global game_judge,list_frame
    if game_judge==True:
        global frame_game
        frame_game.destroy()#删除游戏界面
        list_frame.remove(frame_game)#移除列表信息
        top_map()#回到主页
        game_judge=False
    else:
        showinfo(title='提示信息',message='游戏暂未开始！')
        
def win_exit():#关闭根窗口
    win.destroy()
    
menu_set=tkinter.Menu(menu_1,tearoff=False)#新增"文件"菜单的菜单项，并使用 accelerator 设置菜单项的快捷键
menu_set.add_command(label="保存",activebackground=黑色,background=白色,command=top_map, accelerator="Ctrl+S")
menu_set.add_command(label="重新开始",activebackground=黑色,background=白色,command=restart, accelerator="Ctrl+B")
menu_set.add_command(label="回到游戏",activebackground=深灰色,background=白色,command=back_game, accelerator="Ctrl+B")
menu_set.add_command(label="游戏规则",activebackground=深灰色,background=白色,command=law, accelerator="Ctrl+A")
menu_set.add_command(label="高级设置",activebackground=深灰色,background=白色,command=setting, accelerator="Ctrl+C")
menu_set.add_separator(background=白色)# 添加一条分割线
menu_set.add_command(label="退出",activebackground=黑色,background=白色,command=win_exit)

#在主目录菜单上新增"文件"选项，并通过menu参数与下拉菜单绑定
menu_1.add_cascade(label="选项",activebackground=白色,background=白色,menu=menu_set)
menu_1.add_command(label="关于")
win.config(menu=menu_1)#显示菜单

#右键菜单-开始和规则
list_mouse=list_frame
for j in list_mouse:
    menu_mouse=tkinter.Menu(j, tearoff=False)
menu_mouse.add_command(label='主页面',activebackground=黑色,background=白色,command=top_map)
menu_mouse.add_separator(background=白色)# 添加一条分割线
menu_mouse.add_command(label='回到游戏',activebackground=深灰色,background=白色,command=back_game)
menu_mouse.add_command(label='游戏规则',activebackground=深灰色,background=白色,command=law)
menu_mouse.add_command (label="高级设置",activebackground=深灰色,background=白色,command=setting)
menu_mouse.add_command(label='重新开始',activebackground=黑色,background=白色,command=restart)

def command(event):# 定义事件函数
    menu_mouse.post(event.x_root, event.y_root)# 使用 post()在指定的位置显示弹出菜单
win.bind("<Button-3>",command)# 绑定鼠标右键，这是鼠标绑定事件

win.mainloop()#将窗体显示出来
