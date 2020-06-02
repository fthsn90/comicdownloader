#fthsn90# #02.06.2020#
from tkinter import *
from PIL import Image, ImageTk
import tkinter
from tkinter import messagebox
import webbrowser
from selenium import webdriver
import requests
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os
import patoolib

class mypro():

    def __init__(self):

        self.root = Tk()
        self.root.title("Comic Downloader")
        self.root.iconphoto(False, ImageTk.PhotoImage(Image.open("pics/comic.png")))
        self.root.geometry("410x510")
        self.root.resizable(width=FALSE, height=FALSE)
        self.ust = ImageTk.PhotoImage(Image.open('pics/ust.png'))
        self.downloadpic = ImageTk.PhotoImage(Image.open("pics/download.png").resize((86, 30), Image.ANTIALIAS))
        self.convertpic = ImageTk.PhotoImage(Image.open("pics/convert.png").resize((86, 30), Image.ANTIALIAS))
        self.download = True
        self.sayi = 1
        self.minute = 20
        self.what = """\n\n\n\n\t****Comic Downloader v.1.0****\n \t\n\tYou can download comic images from \n\t\n\thttp://www.readcomiconline.to/\n\t \n \t Also can convert these to Cbr!"""
        ####################
        self.topframe()
        self.urlframe()
        self.middleframe()
        self.bottom()
        self.statusbar()
        ####################
        self.root.mainloop()

    def topframe(self):
        self.topframe = Frame(self.root)
        self.lbl = Button(self.topframe,image=self.ust,command=self.git)
        self.lbl.grid()
        self.topframe.pack()
    
    def urlframe(self):
        self.urlframe = Frame(self.root)
        self.lbl = Label(self.urlframe,text="URL:")
        self.lbl.grid(row=0,column=0)
        self.v = StringVar()
        self.v.set("https://readcomiconline.to/Comic/Rick-and-Morty")
        self.entri = Entry(self.urlframe,bd=2,width=55,textvariable=self.v)
        self.entri.grid(row=0,column=1,pady=5)
        self.urlframe.pack()
    
    def middleframe(self):
        self.middleframe = Frame(self.root)
        self.lbl12 = Label(self.middleframe,text="Issue Number:")
        self.lbl12.grid(row=0,column=0,sticky="ew")
        self.entri2 = Entry(self.middleframe,width=5,bd=2)
        self.entri2.grid(row=0,column=1,sticky="w",pady=3)
        self.lbl2 = Label(self.middleframe,text="Quality:")
        self.lbl2.grid(row=1,column=0)
        self.clicked = StringVar()
        self.clicked.set("LOW")
        self.drop = OptionMenu(self.middleframe,self.clicked,"HQ","LOW")
        self.drop.grid(row=1,column=1)
        self.btn = Button(self.middleframe,text="Download",image=self.downloadpic,command=self.start)
        self.btn.grid(row=2,column=0,columnspan=1)
        self.btn2 = Button(self.middleframe,image=self.convertpic,command=self.convert)
        self.btn2.grid(row=2,column=1)
        self.middleframe.pack()
    
    def bottom(self):
        self.bottom = Frame(self.root)
        self.txt = Text(self.bottom,width=48,height=15)
        self.txt.insert(END,self.what)
        self.txt.grid(row=2,pady=3)
        self.bottom.pack()

    def statusbar(self):
        self.statusbar = Label(self.root,text="#rick and more coffee! \t\t\t\t\t#fthsn90 ",bd=1,relief=SUNKEN,anchor=W)
        self.statusbar.pack(side=BOTTOM,fill=X)

    def git(self):
        webbrowser.open("https://readcomiconline.to/")
    
    def indir(self,sayi):
        neredeyim = os.getcwd()
        self.nereye = os.path.join(f"{neredeyim}",f"{self.name}")
        try:
            s = WebDriverWait(self.browser, self.minute).until(EC.presence_of_element_located((By.XPATH, f"//*[@id='divImage']/p[{self.sayi}]/img")))
            link = s.get_attribute('src')
            r = requests.get(link)
            with open(f"{self.nereye}/{self.sayi}.jpg","wb") as f:
                f.write(r.content)
        except:
            self.download = False
        
    def start(self):
        if not self.entri.get():
            self.statusbar["text"] = "Please Enter An Url!"
        self.download = True
        self.options = Options()
        self.url = self.entri.get()
        self.comic = self.url.split("/")[4].replace("-"," ")
        self.issue = self.entri2.get()
        self.name = self.comic +"-"+ self.issue
        self.klasor = os.mkdir(self.name)
        self.options.headless = True

        self.browser = webdriver.Firefox(options=self.options)
        self.browser.get(self.url)
        # CHANGE WİTH YOUR "uBlock0@raymondhill.net.xpi" PATH <<<<<<---------------------!!!!
        try:
        	self.browser.install_addon(r"C:\Users\fthsn\AppData\Roaming\Mozilla\Firefox\Profiles\bp5xt9qj.default-release\extensions\uBlock0@raymondhill.net.xpi")
        except:
        	messagebox.showwarning("Warning","Look at 119. where is uBlock0@raymondhill.net.xpi? ")

        #get issue number
        self.s = WebDriverWait(self.browser, self.minute).until(EC.presence_of_element_located((By.LINK_TEXT, f"{self.comic} Issue #{self.issue}")))
        self.s.click()

        #All pages select
        self.reading_type = Select(WebDriverWait(self.browser, self.minute).until(EC.presence_of_element_located((By.XPATH, r'//*[@id="selectReadType"]'))))
        self.reading_type.select_by_value("1")

        #Quality thing
        if self.clicked.get()=="HQ":
            quality = Select(WebDriverWait(self.browser, self.minute).until(EC.presence_of_element_located((By.ID, "selectQuality"))))
            quality.select_by_value("hq")
        
        #Comic Loop
        while self.download:
            self.indir(self.sayi)
            self.sayi +=1
        self.statusbar["text"] = "Download Success Completed!"
        self.browser.close()

    def convert(self):
        try:

            files = []
            for r, d, f in os.walk(self.nereye):
                for file in f:
                    if ".jpg" in file:
                        files.append(os.path.join(r,file))
            
            images = tuple(files)
            patoolib.create_archive(f"{self.nereye}/#{self.name}.cbr", images, verbosity=-1)
            for f in files:
                os.remove(f)
            self.clear()
            messagebox.showinfo("Info","Convert Succeed!")
        except:
            self.statusbar["text"] = "There is a problem!"
        
    def clear(self):
        self.entri.delete("0","end")
        self.entri2.delete("0","end")
        self.statusbar["text"] = "Ready!"

mypro()