import json
import os
import subprocess
import threading
import tkinter as tk
import webbrowser
import zipfile
from datetime import datetime
from pathlib import Path
from tkinter import *
from tkinter import filedialog, font, messagebox, ttk
from tkinter.filedialog import asksaveasfile
from tkinter.scrolledtext import ScrolledText

import multitasking
import sv_ttk
import shutil
import win32clipboard
from pygments import lex
from pygments.lexers import PythonLexer

from codeeditor import *
from codeeditor import TextLineNumbers, TextPad
from tkterm import Terminal

multitasking.set_max_threads(20)
theme_used = 'd_sv' #by Default
stheme = "dark"
null = 'nones'

def run():
        root.f = asksaveasfile(initialfile = 'Untitled.py',defaultextension=".py",mode="w",filetypes=[("Python Source File","*.py"),("Python Source File","*.py")])
        if root.f is None:
                return
        file_save = str(textPad.get(1.0,END))
        root.f.write(file_save)
        args = root.f.name
        print(root.f.name)
        fps = open(r'dir.ini', 'w') 
        path = root.f.name
        fps.write(root.f.name)
        fps.close()
        root.f.close()
        subprocess.call(['run_file.bat'])
def venv_create():
        folder = filedialog.askdirectory()
        if folder==None:
                return
        dir = folder
        subprocess.call(['create_venv.bat', dir])

def pip():
        pip = tk.Tk()
        theme_system()
        if null=='null':
                root.filename = filedialog.asksaveasfile(mode="w",defaultextension='.txt')
        pip.geometry('200x75')
        pip.minsize(200,75)
        pip.maxsize(200,75)
        pip.title('Package Installer')
        textp = Text(pip,width=25,height=3,relief=RIDGE,font=('Seoge UI Light',10,'bold'),borderwidth=2)
        textp.place(x=200,y=75)
        textp.pack()
        def pkg():
                pip.filename = str('tools/scripts/temp/requirements.txt')
                pkg_selected = str(textp.get(1.0,END))
                fp = open(r'python/python37-32/scripts/temp/requirements.txt', 'w')
                fp.write(pkg_selected)
                
                os.startfile("package.bat")
        package = ''
        install = ttk.Button(pip,text='Install',command=pkg)
        install.place(x=0,y=0)
        install.pack()


def compiler():
        os.startfile("python/python37-32/Scripts/apte.bat")
def pcp():
        os.startfile("python_cp.bat")
def extensions():
        exte = tk.Tk()
        theme_system()
        exte.title('Extension Manager')
        def install():
                root.filename = filedialog.askopenfilename(
                initialdir = '/',
                title="Select file",
                filetypes=(("Katana Extension Package","*.kep"),("Katana Support Addon","*.ksa"),("all files","*.*")))
                if root.filename==None:
                        return
                try:
                        with zipfile.ZipFile(root.filename, 'r') as zip_ref:
                                zip_ref.extractall('extensions/')
                                Label(exte, text="Installed")
                except:
                        Label(exte, text="Not Installed due to Unsupported Format")
        #def disable():
        #        root.filename = filedialog.askopenfilename(
        #        initialdir = '/',
        #        title="Select file",
        #        filetypes=(("Extension or Support Addon index file","*.esf"),("all files","*.*")))
        #        try:
        #                
        #                os.rename(root.filename, 'extensions/disable/disabled_addon.dis')
        #        except:
        #                try:
        #                        os.rename(root.filename, 'extensions/disable/da.dis')
        #                except:
        #                        os.rename(root.filename, 'extensions/disable/disabled_extension.dis')
        #        else:
        #                Label(exte, text='Save Error (Error Code: glowhole)')
        #def enable():
        #        root.filename = filedialog.askopenfilename(
        #        initialdir = '/',
        #        title="Select file",
        #        filetypes=(("Disabled Extension File","*.dis"),("all files","*.*")))
        # انشاالله اپدیت بعد
        def uninstall():
                
                root.filename = filedialog.askopenfilename(
                initialdir = '/',
                title="Select file",
                filetypes=(("Katana Extension Package Files List","*.ini"),("all files","*.*")))
                if root.filename==None:
                        return
                fp = open(r(root.filename), 'r')
                listen = fp.read()
                
                for p in Path(".").glob(listen):
                        p.unlink()
        ttk.Button(exte, text='Install Extension', command=install).pack()
        #Button(exte, text='Disable Extension', command=disable).pack()
        ttk.Button(exte, text='UnInstall Extension', command=uninstall).pack()
def explorer():
        os.chdir('tools/explorer/')
        os.startfile('external_explorer.exe')
        os.chdir("/")
def about():
        """
                This is Katana IDE About Window
        """
        root = tk.Tk()
        theme_system()
        root.title('Katana About')
        root.geometry('300x150')
        Label(root,text="").pack()
        Label(root,text="").pack()
        
        Label(root,text="Katana is an Open Source, PowerFull IDE For Python, C, C++", ).pack()
        Label(root,text="is Developed in Python, C, Tkinter by Seemon(tm)").pack()
        Label(root,text="Use's Lowest Hardware for Best Performance").pack()
def new():
        textPad.delete('1.0','end')
def theme_system():
        global theme_used
        if theme_used=='d_f':
                try:
                        root.tk.call('source', 'assets/theme/forest-light.tcl')
                        theme_used = 'd_f'
                except:
                        style.theme_use('forest-dark')
                style.theme_use('forest-dark')

        if theme_used=='l_f':
                try:
                        root.tk.call('source', 'assets/theme/forest-light.tcl')
                        theme_used = 'd_f'
                except:
                        style.theme_use('forest-light')
                style.theme_use('forest-light')

        if theme_used=='d_a':
                try:
                        root.tk.call("source", "assets/theme/azure.tcl")
                        theme_used = 'd_a'
                except:
                        root.tk.call("set_theme", "dark")
                root.tk.call("set_theme", "dark")

        if theme_used=='l_a':
                try:
                        root.tk.call("source", "assets/theme/azure.tcl")
                        theme_used = 'l_a'
                except:
                        root.tk.call("set_theme", "light")
                root.tk.call("set_theme", "light")

        if theme_used=='d_sv':
                sv_ttk.set_theme("dark")
                theme_used = 'd_sv'

        if theme_used=='l_sv':
                sv_ttk.set_theme("light")
                theme_used = 'l_sv'


def theme():
        global theme_used
        def toggle_theme():
                if sv_ttk.get_theme() == "dark":
                        sv_ttk.use_light_theme()
                elif sv_ttk.get_theme() == "light":
                        sv_ttk.use_dark_theme()
        def space():
                Label(root, text='').pack()
        def text(text):
                Label(root,text=text).pack()
        root = tk.Tk()
        theme_system()
        root.geometry('200x425')
        root.title('Personalization')
        text("Personalization")
        space()
        ttk.Button(root, text="Random Sun Valley", command=toggle_theme).pack()
        space()
        def d_sv():
                sv_ttk.set_theme("dark")
                theme_used = 'd_sv'
                d_svo()
        ttk.Button(root, text="Dark Sun Valley", command=d_sv).pack()
        space()
        def l_sv():
                sv_ttk.set_theme("light")
                theme_used = 'l_sv'
                l_svo()
        ttk.Button(root, text="Light Sun Valley (BETA)", command=l_sv).pack()
        space()
        style = ttk.Style(root)
        def import_theme():
                
                root.tk.call('source', 'assets/theme/forest-light.tcl')
                root.tk.call("source", "assets/theme/azure.tcl")
        def d_forest():
                try:
                        root.tk.call('source', 'assets/theme/forest-light.tcl')
                        theme_used = 'd_f'
                except:
                        style.theme_use('forest-dark')
                style.theme_use('forest-dark')
                d_foresto()
        ttk.Button(root, text="Dark Forest", command=d_forest).pack()
        
        space()
        def l_forest():
                try:
                        root.tk.call('source', 'assets/theme/forest-light.tcl')
                        theme_used = 'l_f'
                except:
                        style.theme_use('forest-light')
                style.theme_use('forest-light')
                l_foresto()
        ttk.Button(root, text="Light Forest", command=l_forest).pack()
        space()
        def d_azure():
                try:
                        root.tk.call("source", "assets/theme/azure.tcl")
                        theme_used = 'd_a'
                except:
                        root.tk.call("set_theme", "dark")
                root.tk.call("set_theme", "dark")
                d_azureo()
        ttk.Button(root, text="Dark Azure", command=d_azure).pack()
        space()
        def l_azure():
                try:
                        root.tk.call("source", "assets/theme/azure.tcl")
                        theme_used = 'l_a'
                except:
                        root.tk.call("set_theme", "light")
                root.tk.call("set_theme", "light")
                l_azureo()

        ttk.Button(root, text="Light Azure", command=l_azure).pack()
        space()


def d_svo():
        sv_ttk.set_theme("dark")
        
def l_svo():
        sv_ttk.set_theme("light")

def d_foresto():
        try:
                root.tk.call('source', 'assets/theme/forest-light.tcl')
        except:
                style.theme_use('forest-dark')
        style.theme_use('forest-dark')
def l_foresto():
        try:
                root.tk.call('source', 'assets/theme/forest-light.tcl')
        except:
                style.theme_use('forest-light')
        style.theme_use('forest-light')
def l_azureo():
        root.tk.call("set_theme", "light")
def d_azureo():
        root.tk.call("set_theme", "dark")

def new_cons():
        os.startfile("start_new_cons.bat")
def new_wind():
        os.startfile("run.bat")
def new_window():
        root = tk.Tk()
        root.geometry('500x500')
        root.title('Katana IDE')


        menubar = Menu(root)

        file = Menu(menubar,tearoff = 0)
        file.add_command(label="New",command=new)
        file.add_command(label="New window",command=new_window)
        file.add_command(label="Open",command=Open)
        file.add_command(label="Save",command=save)
        file.add_command(label="Save as", command=save_as)
        file.add_separator()
        file.add_command(label="Exit",command=exit)
        menubar.add_cascade(label="File",menu=file,font=('verdana',10,'bold'))



        edit = Menu(menubar,tearoff = 0)

        edit.add_separator()
        edit.add_command(label="Cut",command=cut)
        edit.add_command(label="Copy",command=copy)
        edit.add_command(label="Paste",command=paste)
        edit.add_command(label="Delete",command=delete)
        edit.add_command(label="Select All",accelerator="Ctrl+A",command=select_all)
        edit.add_command(label="Time/Date",accelerator="F5",command=time)
        menubar.add_cascade(label="Edit",menu=edit)


        Format = Menu(menubar, tearoff = 0)

        
        Format.add_command(label="Font...", command=fonts)

        menubar.add_cascade(label="Format",menu=Format)



        Help = Menu(menubar, tearoff = 0)

        Help.add_command(label="View Help",command=view_help)
        Help.add_command(label="Send FeedBack",command=send_feedback)
        Help.add_command(label="About Katana IDE")

        menubar.add_cascade(label="Help",menu=Help)


        root.config(menu=menubar)





        text = ScrolledText(root,width=1000,height=1000)
        text.place(x=0,y=0)



        root.mainloop()
def newp():
        root = tk.Tk()
        root.title('New Project')
        root.geometry("765x600")
        theme_system()
        text = Label(frame_bar, text="Enter Name").pack(fill=("480","300"))
        frame_bar = ttk.Frame(root)
        textp = Text(root,width=25,height=1,relief=RIDGE,font=('Seoge UI Light',10,'bold'),borderwidth=2).pack(fill=("476","300"))
        frame_bar.pack(fill=tk.BOTH, expand=True)
        def browsef():
                __yes_or_no__ = True
                root.filename = filedialog.asksaveasfile(mode="w",defaultextension='.json')
                if root.filename==None:
                        return
                #print(browse_func)
        browse = ttk.Button(frame_bar, text="Browse", command=browsef)
        x = ''
        browse.pack(side=LEFT, fill=("382","300"))
        def createp():
                global __yes_or_no__
                if __yes_or_no__==False:
                        messagebox.showwarning(title='Please Select a Folder First')

                        
                data = {
                'katana_project' : [
                        {
                                'name' : proj_name,
                                'dir' : proj_directory,
                                'katana_version' : 'v0.1_public_beta',
                                'stylment' : proj_style
                        }
                                ]
                }
                original = r'C:\\Users\\usr_data\\Projects\\katana.json' 
                new_project = proj_directory
                shutil.copyfile()
                parsed = json.dump(data, parse) 
                
                
        frame_bar = ttk.Frame(root)
        frame_bar.pack(fill=tk.BOTH, expand=True)
        create = ttk.Button(frame_bar, text="Create Project",command=createp)
        create.pack(side=RIGHT, fill=tk.BOTH)
        cancel = ttk.Button(frame_bar, text="Cancel",command=root.destroy)
        cancel.pack(side=RIGHT, fill=tk.BOTH)


def Open():
        global textPad
        root.filename = filedialog.askopenfilename(
                initialdir = '/',
                title="Select file",
                filetypes=(("python source file","*.py"),("all files","*.*")))
        file = open(root.filename)
        textPad.insert('end',file.read())
        while 1:
                theData = str(textPad.get(1.0,END))
                theTmp = open(r'C:\\Users\\tmp_data\\highlight\\usrCodes.txt', 'w')
                theTmp.write(theData)
                theTmp.close()
                theFile = open(r"C:\\Users\\tmp_data\\highlight\\usrCodes.txt", 'r')
                buffer = theFile.read(8192*1024)
                if not buffer: break
                linesInFile += buffer.count('\n')
                lines = linesInFile
                overlord = master.master.master
                textPad.highlightAll2(lines, overlord)
                textPad.update()
def save():
        pass
def save_as():
        root.filename = filedialog.asksaveasfile(mode="w",defaultextension='.py')
        if root.filename is None:
                return
        file_save =  str(textPad.get(1.0,END))
        root.filename.write(file_save)
        root.filename.close()

def exit():
        sv_ttk.set_theme("dark")
        message = messagebox.askquestion('Katana IDE',"Do you want to save changes")
        
        if message == "yes":{
                save_as()
        }
        if message == "no":{
                root.destroy()
        }
        else:{
                root.destroy()
        }
        

def cut():
        textPad.event_generate("<<Cut>>")
def redo():
        textPad.event_generate("<<Redo>>")
def undo():
        textPad.event_generate("<<Undo>>")


def copy():
        textPad.event_generate("<<Copy>>")


def paste():
        textPad.event_generate("<<Paste>>")


def delete():
        message = messagebox.askquestion('Katana IDE',"Do you want to Delete all")
        if message == "yes":
                textPad.delete('1.0','end')
        else:
               return "break"

       

def select_all():
        textPad.tag_add('sel','1.0','end')
        return 'break'
def run_nsav():
        subprocess.call(['run_file.bat'])
def clipboard():
        root = tk.Tk()
        theme_system()
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        show = Label(root, text=data).pack()
        def clear():
                win32clipboard.OpenClipboard()
                win32clipboard.EmptyClipboard()
                win32clipboard.CloseClipboard()
        def add_clip():
                win32clipboard.OpenClipboard()
                win32clipboard.EmptyClipboard()
                root = tk.Tk()

                textbox = ScrolledText(root).pack()
                impo = Button(root, text='Import Text', command=import_contacts(textbox)).pack()
        def import_contacts(event):
                textbox = event
                message =  str(textbox.get(1.0,END))
                win32clipboard.SetClipboardText(message)        
        clear = ttk.Button(root, text="Clear", command=clear).pack()
        add = ttk.Button(root, text='Add', command=add_clip).pack()


                
def time():     
        d = datetime.now()
        textPad.insert('end',d)
        
def openp():
        nothing = 'donothing'


def fonts():
        root = tk.Tk()
        theme_system()
        root.geometry('400x400')
        root.title('Font')
        sv_ttk.set_theme("dark")
        l1 = Label(root,text="Font:")
        l1.place(x=10,y=10)
        f = tk.StringVar() 
        fonts = ttk.Combobox(root, width = 15, textvariable = f, state='readonly',font=('verdana',10,'bold'),) 
        fonts['values'] = font.families()
        fonts.place(x=10,y=30)
        fonts.current(0) 


        l2 = Label(root,text="Font Style:")
        l2.place(x=180,y=10)
        st = tk.StringVar() 
        style = ttk.Combobox(root, width = 15, textvariable = st, state='readonly',font=('verdana',10,'bold'),) 
        style['values'] = ('bold','bold italic','italic')
        style.place(x=180,y=30)
        style.current(0) 

        l3 = Label(root,text="Size:")
        l3.place(x=350,y=10)
        sz = tk.StringVar() 
        size = ttk.Combobox(root, width = 2, textvariable = sz, state='readonly',font=('verdana',10,'bold'),) 
        
        size['values'] = (8,9,10,12,15,20,23,25,27,30,35,40,43,47,50,55,65,76,80,90,100,150,200,255,300)
        size.place(x=350,y=30)
        size.current(0) 
               
              
        sample = LabelFrame(root,text="Sample",height=100,width=200)
        sample['font'] = (fonts.get(),size.get(),style.get())
        sample.place(x=180,y=220)

        l4 = Label(sample,text="This is sample")
        l4.place(x=20,y=30)



        def OK():

               textPad['font'] = (fonts.get(),size.get(),style.get())
               selected_font = fonts.get()
               size = size.get()
               noe = style.get()
               root.destroy()
               

        ok = ttk.Button(root,text="OK",relief=RIDGE,borderwidth=2,padx=20,highlightcolor="blue",command=OK)
        ok.place(x=137,y=350)

        def Apl():
                l4['font'] = (fonts.get(),size.get(),style.get())
                selected_font = fonts.get()
                size = size.get()
                noe = style.get()
        Apply = ttk.Button(root,text="Apply",relief=RIDGE,borderwidth=2,padx=20,highlightcolor="blue",command=Apl)
        Apply.place(x=210,y=350)        

        def Cnl():
                root.destroy()

        cancel = ttk.Button(root,text="Cancel",relief=RIDGE,borderwidth=2,padx=20,command=Cnl)
        cancel.place(x=295,y=350)
        root.mainloop()



def view_help():
        webbrowser.open('seemon.ir')


def send_feedback():
        webbrowser.open('seemon.ir')


root = tk.Tk()
root.configure(bg="#000000")
root.geometry('600x400')
root.minsize(600,400)
root.title('Katana IDE')
photo = tk.PhotoImage(file = 'katana.png')
root.wm_iconphoto(False, photo)
selected_font = ""
size = '10'
noe = 'bold'

menubar = Menu(root)













frame1 = ttk.Frame(root)
frame1.pack(fill=tk.BOTH, expand=True)
        

textPad = TextPad(frame1, undo=True, maxundo=-1, autoseparators=True, width=89, height=23)
textPad.filename = None
textPad.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

textScrollY = ttk.Scrollbar(textPad)
textScrollY.config(cursor="double_arrow")
textPad.configure(yscrollcommand=textScrollY.set)
textScrollY.config(command=textPad.yview)
textScrollY.pack(side=tk.RIGHT, fill=tk.Y)
autocompleteEntry = tk.Label(root, bg='black', fg='green', text='Recom List', font=('Mono', 13))
autocompleteEntry.pack(side='bottom', fill=BOTH)
textPad.entry = autocompleteEntry
terminal = Terminal(root, bg="#282C34", bd=0, width=50, height=25)
terminal.pack()



def on_change(root):
        linenumber.redraw()
        
linenumber = TextLineNumbers(frame1, width=30)
linenumber.attach(textPad)
linenumber.pack(side="left", fill="y")

 
textPad.bind("<<Change>>", on_change)
textPad.bind("<Configure>", on_change)


        







file = Menu(menubar,tearoff = 0)
file.add_command(label="New Project",command=newp)
file.add_command(label="New Python File", command=new)
file.add_command(label="Open",command=Open)
file.add_command(label="Open Project",command=openp)
file.add_command(label="Open Console Window", command=new_cons)
file.add_command(label='Open New Window', command=new_wind)
file.add_command(label="Save",command=save)
file.add_command(label="Save as", command=save_as)
file.add_separator()
file.add_command(label="Exit",command=exit)
menubar.add_cascade(label="File",menu=file,font=(selected_font,size,noe))
editd = Menu(menubar,tearoff = 0)
editd.add_command(label="Compile",command=compiler)
editd.add_command(label="Install Package",command=pip)
editd.add_command(label="Create Virtual Enviroment",command=venv_create)
editd.add_command(label="Manage Extensions", command=extensions)
menubar.add_cascade(label="Develop Options", menu=editd,font=(selected_font,size,noe))
run_code = Menu(menubar,tearoff = 0)
run_code.add_command(label="Run",command=run)
run_code.add_command(label="Run Without Save", command=run_nsav)
menubar.add_cascade(label="Run Codes",menu=run_code,font=(selected_font,size,noe))

#Atention : DONT FUCK THIS CODES FOR ANY REASONS 'a note from q'

edit = Menu(menubar,tearoff = 0)
edit.add_command(label="Undo",accelerator="Ctrl+Z",command=undo)
edit.add_command(label="Redo",accelerator="Ctrl+Y",command=redo)
edit.add_separator()
edit.add_command(label="Cut",accelerator="Ctrl+X",command=cut)
edit.add_command(label="Copy",accelerator="Ctrl+C",command=copy)
edit.add_command(label="Paste",accelerator="Ctrl+V",command=paste)
edit.add_command(label="Delete",accelerator="Del",command=delete)
edit.add_command(label="Select All",accelerator="Ctrl+A",command=select_all)
edit.add_command(label="Time/Date",accelerator="F5",command=time)
menubar.add_cascade(label="Edit",menu=edit)


Format = Menu(menubar, tearoff = 0)
Format.add_command(label="Theme's", command=theme)
Format.add_command(label='Show Clipboard',command=clipboard)
Format.add_command(label="Python Command Prompt", command=pcp)
Format.add_command(label="Font...", command=fonts)

menubar.add_cascade(label="Format",menu=Format)



Help = Menu(menubar, tearoff = 0)

Help.add_command(label="View Help",command=view_help)
Help.add_command(label="Send FeedBack",command=send_feedback)
Help.add_command(label="About Katana",command=about)

menubar.add_cascade(label="Help",menu=Help)



m = Menu(root, tearoff = 0)
m.add_command(label ="Select All",accelerator="Ctrl+A",command=select_all) 
m.add_command(label ="Cut",accelerator="Ctrl+X",command=cut) 
m.add_command(label ="Copy",accelerator="Ctrl+C",command=copy) 
m.add_command(label ="Paste",accelerator="Ctrl+V",command=paste) 
m.add_command(label ="Delete",accelerator="Del",command=delete) 
m.add_separator() 
m.add_command(label ="Undo",accelerator="Ctrl+Z",command=TextPad.edit_undo)
m.add_command(label ="Redo",accelerator="Ctrl+Z",command=TextPad.edit_redo) 
m.add_command(label ="Run",accelerator="Ctrl+R",command=run)
def do_popup(event): 
    try: 
        m.tk_popup(event.x_root, event.y_root) 
    finally: 
        m.grab_release() 
  
root.bind("<Button-3>", do_popup) 
theme_system()
root.config(menu=menubar)
root.mainloop()

# a tip for you: DONT FUCK THIS CODES BY ANY REASON'S
