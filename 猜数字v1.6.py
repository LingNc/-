
version=1.3
up_version=1.3
update_time='2022-06-02'

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random
import platform
from math import log, exp, sqrt
from collections import defaultdict
import time


白色='white'
浅浅灰色='#f4f4f4'
浅灰色='#ececec'
灰色='#cecece'
深灰色='#858585'
深深灰色='#4b4b4b'
黑色='black'
红色='red'
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
    style(menu_set,'保存',黑色,none)
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
    style(menu_about,'意见反馈',深灰色,none)
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
class windows(tk.Tk,tk.Label,tk.Button):
    #创建窗口
    def win(self,label,color,x,y):
        self.title(label)#窗体标题
        self.width=x
        self.height=y
        self.screenwidth = self.winfo_screenwidth()
        self.screenheight = self.winfo_screenheight()
        self.geometry('%dx%d+%d+%d'%(self.width, self.height, (self.screenwidth-self.width)/2, (self.screenheight-self.height)/2))
        self.resizable(width=False, height=False)#禁止更改宽和高
        self.config(bg=color)#设置窗体颜色
        self.iconbitmap('E:/Users/Administrator/Desktop/MobileFile/数.ico')#设置图标
    
    #窗体关闭关联事件
    def cut(self,which,function):
        which.protocol('WM_DELETE_WINDOW', function)
        
    #提示文字
    def text(self,label,x,y,fg):
        self=tk.Label(self,pady=y,padx=x,text=label,bg=白色,fg=fg,font=('等线',13,'bold'),height=1,width=0,anchor='s')
        self.grid(sticky='s',ipadx=0,ipady=0,row=0,column=0)#放置标签
    
    #按钮
    def enter(self,label,x,y,fg,活跃色,function):
        self=tk.Button(self,padx=2,pady=0,text=label,bg=白色,fg=fg,activebackground=白色,highlightcolor=活跃色,font=('等线',13),bd=1,anchor='center',command=function)
        self.grid(padx=x,pady=y,row=1,column=0)#放置按钮
        
        
            
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
            global level
            level=5
        
            
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

#画布：检查更新
def update():
    global version,up_version
    if up_version>version:
        win_up=windows()
        win_up.win('检查更新',白色,180,100)
        win_up.lift(aboveThis=win)
        win_up.text('发现有新版本!',34,17,红色)
        win.cut(win_up,win_up.destroy)
        win_up.enter('立即更新',0,0,黑色,红色,rank)
        win_up.mainloop()
    else:
        win_err=windows()
        win_err.win('检查更新',白色,180,70)
        win_err.lift(aboveThis=win)
        win_err.text('当前已是最新版!',24,24,黑色)
        win.cut(win_err,win_err.destroy)
        win_err.mainloop()
    
#画布：反馈界面
def feedback():
    none()

#画布：排行界面
def rank():
    none()

#画布：游戏界面
def game():
    #引入全局变量
    global frame_game,run_button,run_detail_list,list_frame,xgame,list_box,run_text,run_history,run_detail,run_entry,num_inside,num_input,level    
    level = 5
    #定义动态字符串
    run_text=tk.StringVar()
    run_history=tk.StringVar()
    run_detail=tk.StringVar()
    run_entry=tk.StringVar()
    run_button=tk.StringVar()
    
    run_detail_list=[]#初始化列表框
    
    #历史表单
    class history():
        def __init__(self):
            self.date=[]
        def detail(self,number,input_number,return_number):
            self.date.append([[number,input_number,return_number]])
        def option(self,number,right_rate,time):
            self.date[number].append([right_rate,time])
        def intime(self,number,intime):
            self.date[number].insert(0,intime)
            
    #比较个数,和正确率
    def compare(x,y):
        global in_put,same,diff,right,out_num
        same=len(set(x)&set(y))
        diff=len([x[i] for i in range(level) if x[i]==y[i]])
        out_num=str(same)+' '+str(diff)
        if level > 10:
            num=level-10
        else:
            num=0
        c=100*((C(10+num,same)/C(10+num,level))*((A(diff,diff)/A(same,same))))
        right=round(c,2)
        #转化为数字
        in_put=int(''.join(x))
        in_side=int(''.join(y))
        if in_put == in_side:
            return '恭喜你，答对了！答案为'+str(in_side)+'，正确率为'+str(right)+'%'
        else:
            return "有"+str(same)+"个数字相同，有"+str(diff)+"个位置相同\n正确率为"+str(right)+'%'
    
    #控制run_detail数量并自动删除
    def func_detail(string):
        global run_detail_list,run_detail,level
        
        #清除无用信息
        laji=['输入有误,请重新输入','输入重复,请换个数字','请输入一个'+str(level)+'位的数字']
        keep=run_detail.get().split('\n')
        for i in keep:
            for j in laji:
                if i == j:
                    keep.remove(i)
                else:
                    pass
            
        keep1='\n'.join(keep)
        run_detail.set(keep1)
        
        strings=string+'\n'
        run_detail.set(run_detail.get()+strings)
        run_detail_list=run_detail.get().split('\n')
        del run_detail_list[len(run_detail_list)-1]
        if len(run_detail_list) > 6:
            num=len(run_detail_list)-6
            del run_detail_list[0:num]
            lista='\n'.join(run_detail_list)+'\n'
            run_detail.set(lista)
        else:
            pass
        #清除之前的错误
        
    #查重
    def check(local,string):
        global list_history
        check_box=0#查重参数
        for i in range(local-1):
            if string==str(list_history.date[i][1][1]):
                check_box += 1
            else:
                pass
        if check_box==0:
            return True
        else:
            return False
            
    #输入校验,插入历史列表
    def run_step():
        global num_inside,num_input,level,run_history,list_history,run_button,run_entry
        run_button.set('继续')#更改按钮名称
        num_input=list(str(entry_game.get()))
        if (''.join(num_input).isdigit() and len(num_input)==level) == True:
            num=box_game.size()#本次参数历史位置
            if check(num,str(entry_game.get())):
                func_detail(compare(num_input,num_inside))
                #刷新历史列表
                list_history.detail(num,in_put,out_num)
                if num-1==0:
                    out_time=0
                    list_history.intime(num-1,time.time())
                else:
                    lastime=list_history.date[num-2][0]
                    nowtime=time.time()
                    list_history.intime(num-1,nowtime)
                    out_time=nowtime-lastime
                list_history.option(num-1,right,out_time)
                index_lab=str(list_history.date[num-1][1][0])+' '+str(list_history.date[num-1][1][1])+' '+str(list_history.date[num-1][1][2])
                box_game.insert('end',index_lab)
                box_game.itemconfig(box_game.size()-1,background=灰色)
                box_game.itemconfig(box_game.size()-2,background=白色)
                box_game.itemconfig(0,background=浅灰色)
                box_game.see(num)
            else:
                func_detail('输入重复,请换个数字')
        else:
            func_detail('输入有误,请重新输入')
        run_entry.set('')#清空输入框
            
    #页面构建与运行           
    if xgame==False:
        
        #界面初始化
        frame_game=tk.Frame(win,bg=白色)
        list_frame.append(frame_game)
        frame_game.grid(padx=10,column=0,row=0)
        xgame=True
        
        run_text='游戏暂未开始...'
        text_game='开始'
        run_button.set(text_game)

        #开始按钮
        But_game=tk.Button(frame_game,text=text_game,relief='flat',bd=0,bg=浅灰色,activebackground=灰色,justify='center',command=run_step)
        But_game.grid(padx=312,pady=158,ipadx=16,ipady=3,row=0,column=0,sticky='nw')
        But_game.config(textvariable=run_button)#绑定动态字符串
        #动态细节表
        Lab_run=tk.Label(frame_game,bd=1,bg=浅灰色,height=6,width=25,highlightthickness=1,wraplength=185,anchor='nw',justify='left')
        Lab_run.grid(padx=193,pady=8,row=0,column=0,sticky='wn')
        Lab_run.config(textvariable=run_detail,anchor='nw')#绑定动态字符串
        #历史列表
        box_game=tk.Listbox(frame_game,bd=0,width=25,bg=白色,highlightthickness=1,highlightbackground=浅灰色,highlightcolor=灰色,selectbackground=浅灰色,selectforeground=黑色,selectmode='single',takefocus=False,justify='center')#创建游戏历史列表
        box_game.grid(pady=8,padx=5,row=0,column=0,sticky='wn')
        box_game.config(listvariable=run_history)#绑定动态字符串
        #输入框
        entry_game=tk.Entry(frame_game,bg=浅灰色,bd=5,width=14,relief='flat',selectbackground='black',insertbackground=深灰色,highlightbackground='black',highlightcolor='black')
        entry_game.grid(padx=193,pady=159,ipady=1,row=0,column=0,sticky='wn')
        entry_game.config(textvariable=run_entry)#绑定动态字符串

        #游戏初始化
        #生成一个随机数
        num_range='0123456789'
        random.seed(a=None, version=2)
        num_inside=random.sample(num_range,level)    #随机生成level位数
        #信息栏初始化
        func_detail('请输入一个'+str(level)+'位的数字')
        #初始化历史数据表
        run_history.set('历史记录')
        box_game.itemconfig(0,background=浅灰色)
         #创建历史表单
        global list_history
        list_history=history()
        #绑定回车开始按钮
        def bang(self):
            run_step()
        entry_game.bind('<Return>',bang)#绑定回车

    else:
        change(frame_game)



#函数表
#组合数公式
def C(n,m):
    primes = set()
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.add(i)

    n_factors = defaultdict(int)
    m_factors = defaultdict(int)
    m = min(m, n - m)

    for i in range(1, m + 1):
        k = i
        while k not in primes and k > 1:
            for p in primes:
                if k % p == 0:
                    k = k // p
                    m_factors[p] += 1
                    break
        if k > 1:
            m_factors[k] += 1

        l = n - m + i
        while l not in primes and l > 1:
            for p in primes:
                if l % p == 0:
                    l = l // p
                    n_factors[p] += 1
                    break
        if l > 1:
            n_factors[l] += 1

    res = 1
    for k, v in n_factors.items():
        res *= k ** (v - m_factors[k])
    return int(res)

#排列数公式
def A(n,m):
    a,b=1,1
    for i in range(1,n+1):
        a *= i
    for j in range(1,n-m+1):
        b *= j
    if a != b:
        return a/b
    else:
        return a
    
#功能暂未开放
def none():
        win_none=windows()
        win_none.win('抱歉',白色,180,70)
        win_none.lift(aboveThis=win)
        win_none.text('功能暂未开放',35,23,黑色)
        win.cut(win_none,win_none.destroy)
        win_none.mainloop()

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
        win_back=windows()
        win_back.win('提示信息',白色,180,100)
        win_back.lift(aboveThis=win)
        win_back.text('游戏未运行',46,17,黑色)
        win.cut(win_back,win_back.destroy)
        win_back.enter('确认',0,0,黑色,红色,win_back.destroy)
        win_back.mainloop()

    
#重新开始
def restart():
    global xgame,list_frame
    if xgame==True:
        frame_game.destroy()
        list_frame.remove(frame_game)
        change(frame_start)
        xgame=False
    else:
        win_back=windows()
        win_back.win('提示信息',白色,180,100)
        win_back.lift(aboveThis=win)
        win_back.text('游戏未运行',46,17,黑色)
        win.cut(win_back,win_back.destroy)
        win_back.enter('确认',0,0,黑色,红色,win_back.destroy)
        win_back.mainloop()
        

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
