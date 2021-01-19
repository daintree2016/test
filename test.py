import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
from tkinter import simpledialog
import threading
import multiprocessing
from selenium import webdriver
import os
import time
from tkinter import messagebox
#FILENAME = 'C:\\Users\\rajra\\Downloads\\pic2.jpg'
FILENAME = 'all pics/ni.jpg'
root = tk.Tk()
#root.state('zoomed')
import os.path
from os import path
#root.geometry("500X300+20+20")
#root2=tk.Tk()
#root2.geometry(50,50)
#root.attributes('-fullscreen', True)
root.title("WELCOME TO MY GUI")
canvas = tk.Canvas(root, width=3000, height=1000)
canvas.pack()
tk_img = ImageTk.PhotoImage(file = FILENAME)
canvas.create_image(500,500, image=tk_img)
'''quit_button = tk.Button(root, text = "Quit", command = root.quit, anchor = 'w',
                    width = 10, activebackground = "#33B5E5")'''
#quit_button_window = canvas.create_window(10, 10, anchor='nw', window=quit_button)
#photo = PhotoImage(file = "C:\\Users\\rajra\\Pictures\\icon.ico")
#root.iconbitmap("C:\\Users\\rajra\\Pictures\\icon.ico")

def runapp():
    response=messagebox.askyesno("pop up message","Are you sure want to create this file")
    if response == 1:
        #os.startfile("C:\\Users\\Public\\raj44.xlsx")
        st=str(en.get())
        print(st)
        en.destroy()
        wen.destroy()
        runn.destroy()
        dele.destroy()
        try:
            opt.destroy()
            de.destroy()
            Browse = tk.Button(root,text="Browse",command=brow,border=0,bg='#E7E2E9',image=photo2,compound=CENTER)
            Browse.pack()
            canvas.create_window(700, 150, anchor='nw', window=Browse)
        except Exception:
            pass
        else:
            pass

        
        from openpyxl import Workbook
        wb = Workbook()
        #st=str(input())
        ws =  wb.active
        ws.title = "New File"
        if path.isfile('C:\\Users\\Public\\'+st+'.xlsx'):
            messagebox.showwarning("Warning message","The file name already exists in path \n Choose a unique file name")
        
        elif st=='':
            messagebox.showerror("Error message","please enter a file name")
        else:
            wb.save(filename = 'C:\\Users\\Public\\'+st+'.xlsx')
            messagebox.showinfo("Information","A new xl file created")
    else:
        en.destroy()
        wen.destroy()
        runn.destroy()
        dele.destroy()



w = tk.Label(root, text="Enter a keyword",border=0,font=('Helvetica',15,'bold'),bg='#E8DEE6',fg='brown')
w.pack()
canvas.create_window(440, 106, anchor='nw', window=w)



e = tk.Entry(root, width=20, font=('Helvetica',15))
e.pack(pady=10)
canvas.create_window(610, 104, anchor='nw', window=e)

pathh = "all pics/final3.png"
photo = ImageTk.PhotoImage(file = pathh)
path2 = "all pics/button.png"
photo2 = ImageTk.PhotoImage(file = path2)



def chrome():
    os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe ")

chrome=tk.Button(root,text="Chrome",command=chrome,image=photo)
chrome.config(bg='#D5DBE9',bd=0)
chrome.pack()
ash=canvas.create_window(1200, 30, anchor='nw', window=chrome)

def delet():
    try:
        en.destroy()
        wen.destroy()
        runn.destroy()
        dele.destroy()
        try:
            de.destroy()
        except Exception:
            pass
        else:
            pass
    except Exception:
        pass
    else:
        pass
    try:
        opt.destroy()
        de.destroy()
        
    except Exception:
        pass
    else:
        pass
    
    
    Browse = tk.Button(root,text="Browse",command=brow,border=0,bg='#E7E2E9',image=photo2,compound=CENTER)
    Browse.pack()
    canvas.create_window(700, 150, anchor='nw', window=Browse)




def brow():
    brow.has_been_called=True
    try:
        en.destroy()
        wen.destroy()
        runn.destroy()
        dele.destroy()
    except Exception:
        pass
    else:
        pass
    Browse.destroy()
    
    global opt
    global de
    arr=os.listdir(r"C:\Users\Public")
    
    listt=[]
    for a in arr:
        if a.endswith(".xlsx"):
            listt.append(a)
    print()
    global var
    var = StringVar()
    var.set("select")
    def print_it(event):
        print(var.get())
        runobj["state"]=NORMAL
        
        

    opt=tk.OptionMenu(root, var, *listt,command=print_it)
    opt.pack()
    canvas.create_window(700, 150, anchor='nw', window=opt)
    
    de= tk.Button(root, text="X",border=0,font=('Helvetica',9,'bold'),bg='grey',fg='red',command=delet)
    de.pack()
    canvas.create_window(775,155, anchor='nw', window=de)



def createe():
    global en
    en= Entry(root, width=10, font=('Helvetica',10))
    en.pack()
    
    canvas.create_window(570, 185, anchor='nw', window=en)
    global wen 
    wen= tk.Label(root, text="create a new file",border=0,font=('Helvetica',10,'bold'),bg='#E7E2E9',fg='blue')
    wen.pack()
    canvas.create_window(450, 186, anchor='nw', window=wen)
    global dele
    dele= tk.Button(root, text="X",border=0,font=('Helvetica',9,'bold'),bg='cyan',fg='red',command=delet)
    dele.pack()
    canvas.create_window(678, 184.5, anchor='nw', window=dele)
    global runn
    runn = tk.Button(root,text="OK",command=runapp,bg='pink',border=0)
    runn.pack()
    canvas.create_window(650, 185, anchor='nw', window=runn)
    #global st
    

    #print(st)
    #st=simpledialog.askstring("create a sheet","enter a new name")
    #e.destroy()
    #st.lift()
    #st.geometry(10,20)
    '''import os
    from openpyxl import Workbook
    wb = Workbook()
    #st=str(input())
    ws =  wb.active
    ws.title = "Changed Sheet"
    wb.save(filename = 'C:\\Users\\Public\\'+st+'.xlsx')
    messagebox.askyesno("pop up message","A new file created")'''

global Browse
Browse = tk.Button(root,text="Browse",command=brow,border=0,bg='#E7E2E9',image=photo2,compound=CENTER)
Browse.pack()
canvas.create_window(700, 150, anchor='nw', window=Browse)


#os.startfile('C:\\Users\\Public\\rajj.xlsx')

Create=tk.Button(root,text="Create",font=('Helvetica',10,'bold'),command=createe,image=photo2,compound=CENTER)
Create.config(bg='#E7E2E9',bd=0,fg='green')
Create.pack()
canvas.create_window(550, 150, anchor='nw', window=Create)



def RUNN():
    #thread = threading.Thread(target=RUNN)
    #thread.start()
    #thread.join()

    runobj["state"]=DISABLED
    
    try:    
        if brow.has_been_called==True:
            print("ok tested")
        
            threading.Thread(target=func).start()
    except Exception:
        messagebox.showinfo("Select file","please select an existing file \n        or \ncreate a new xl file")
    else:
        pass
        #runobj["state"]=DISABLED
    
    #runobj["state"]=DISABLED



def func():
    col=e.get()
    from selenium import webdriver
    from selenium.webdriver.common.action_chains import ActionChains
    options = webdriver.ChromeOptions() 

    #options.add_argument("user-data-dir=C:\\Users\\rajra\\AppData\\Local\\Google\\Chrome\\new user data")
    #options.add_argument("user-data-dir=C:\\Users\\rajra\\AppData\\Local\\Google\\Chrome\\User Data")
    driver= webdriver.Chrome(executable_path="chromedriver.exe", options=options)
    rix=0


    #driver.minimize_window()
    driver.get("https://www.amazon.com/")
    time.sleep(1)
    #driver.maximize_window()
    driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']").send_keys(col)
    time.sleep(1)
    try:
        driver.find_element_by_xpath("//*[@id='nav-search']/form/div[2]/div/input").click()
    except Exception:
        try:
            driver.find_element_by_xpath("//*[@id='nav-search-submit-text']/input").click()
        except Exception as s:
            print(s)
        else:
            pass
#//*[@id="nav-search-submit-text"]/input
    else:
        pass
    time.sleep(2)

    l=[]

    try:
        for o in range(1,8):
            try:
                for i in range(2,50):
                    try:
                #print(driver.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div["+str(i)+"]/div/span/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div/span[1]/span[1]/i").get_attribute("aria-label"))
                        kit=driver.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div["+str(i)+"]").get_attribute("data-asin")
                        l.append(kit)
                    except Exception as es:
                        print(es)
                        kll=driver.find_element_by_xpath("//*[@id='search']/div[1]/div/div[1]/div/span[3]/div[2]/div["+str(i)+"]").get_attribute("data-asin")
                        l.append(kll)
                    else:
                        pass
                print()
                if(len(l)>103):
                    driver.quit()
                    break
                else:
                    break
                urll=driver.current_url
                try:
                    time.sleep(1)
                    driver.find_element_by_partial_link_text("→").click()
                    time.sleep(1)
                except Exception as es:
                    print(es)
                    driver.get(urll)
                    time.sleep(1)
                    driver.find_element_by_partial_link_text("Next").click()
                else:
                    pass
                
            except Exception:
                try:
                    time.sleep(1)
                    driver.find_element_by_partial_link_text("→").click()
                    time.sleep(1)
                except Exception as es:
                    print(es)
                    driver.get(urll)
                    time.sleep(1)
                    driver.find_element_by_partial_link_text("Next").click()
                else:
                    pass
                
            else:
                pass
            #print(l)
            
        print()
        
    except Exception as es:
        print(es)
        pass
    else:
    
#print(l)

        import xlwings as xw 
        wb=xw.Book("C:\\Users\\Public\\"+str(var.get()))

        sht1=wb.sheets['New File']
        l = ' '.join(l).split()
        print(l)
        sht1['A1'].value = "ASINS"
        sht1['B1'].value = col

        sht1['C1'].value = "LINKS"
        for hi in range(2,102):
            print(hi)
            sht1['A'+str(hi)].value = l[rix]
            sht1['C'+str(hi)].value= '=HYPERLINK("https://www.amazon.com/s?k="&A'+str(hi)+'&"&ref=nb_sb_noss", "product link")'
            rix=rix+1
            #time.sleep(1)
        print()






runobj=tk.Button(root,text="RUN",font=('Helvetica',10,'bold'),command=RUNN,image=photo2,compound=CENTER)

runobj.config(bg='#E7E2E9',bd=0,fg='green')
runobj.pack()
canvas.create_window(850, 150, anchor='nw', window=runobj)

def nulll():
    pass

we= tk.Label(root, text="Chrome",border=0,font=('Helvetica',10,'bold'),bg='#DBDDEA',fg='blue')
we.pack()
canvas.create_window(1200, 82, anchor='nw', window=we)

photo3 = ImageTk.PhotoImage(file = 'all pics/inst3.png')
runobj=tk.Button(root,font=('Helvetica',10,'bold'),image=photo3,compound=CENTER,command=nulll)
runobj.config(bg='#E7E2E9',bd=0,fg='green')
runobj.pack()
canvas.create_window(1300, 36, anchor='nw', window=runobj)

we= tk.Label(root, text="Notes",border=0,font=('Helvetica',10,'bold'),bg='#DBDDEA',fg='blue')
we.pack()
canvas.create_window(1315, 82, anchor='nw', window=we)



def hello():
    pass

photo4 = ImageTk.PhotoImage(file = 'all pics/report2.png')
runobj=tk.Button(root,font=('Helvetica',10,'bold'),command=hello,image=photo4,compound=CENTER)
runobj.config(bg='#E7E2E9',bd=0,fg='green')
runobj.pack()
canvas.create_window(1400, 36, anchor='nw', window=runobj)

we= tk.Label(root, text="Report",border=0,font=('Helvetica',10,'bold'),bg='#DBDDEA',fg='blue')
we.pack()
canvas.create_window(1404, 82, anchor='nw', window=we)


we= tk.Label(root, text="ASINS",border=0,font=('Helvetica',25,'bold'),bg='yellow',fg='blue')
we.pack()
canvas.create_window(620, 20, anchor='nw', window=we)


we= tk.Label(root, text="ASIN DETAILS",border=0,font=('Helvetica',25,'bold'),bg='yellow',fg='blue')
we.pack()
canvas.create_window(610, 380, anchor='nw', window=we)


def null4():
    null4.has_been_called=True
    global opt
    global de
    arr=os.listdir(r"C:\Users\Public")
    
    listt=[]
    for a in arr:
        if a.endswith(".xlsx"):
            listt.append(a)
    print()
    global varr
    varr = StringVar()
    varr.set("select a file")
    def print_it(event):
        print(varr.get())
        
        
        
    global opt1
    global de1
    opt1=tk.OptionMenu(root, varr, *listt,command=print_it)
    opt1.pack()
    canvas.create_window(690, 456, anchor='nw', window=opt1)
    
    de1= tk.Button(root, text="X",border=0,font=('Helvetica',11,'bold'),bg='grey',fg='red',command=delet5)
    de1.pack()
    canvas.create_window(790,456, anchor='nw', window=de1) 

def delet5():
    
    opt1.destroy()
    de1.destroy()


def null5():
    pass


photo5 = ImageTk.PhotoImage(file = 'all pics/upload2.png')
runobjjj=tk.Button(root,font=('Helvetica',10,'bold'),command=null4,image=photo5)
runobjjj.config(bg="#9FACCC",border=0)
runobjjj.pack()
canvas.create_window(610, 456, anchor='nw', window=runobjjj)



we= tk.Label(root, text="upload\na file",border=0,font=('Helvetica',9,'bold'),bg='#9FACCC',fg='blue')
we.pack()
canvas.create_window(610, 500, anchor='nw', window=we)

def null5():
    #thread = threading.Thread(target=RUNN)
    #thread.start()
    #thread.join()

    runobj["state"]=DISABLED
    
    try:    
        if null4.has_been_called==True:
            print("ok tested")
        
            threading.Thread(target=rundet).start()
    except Exception:
        messagebox.showinfo("Select file","please select an existing file \n        or \ncreate a new xl file")
    else:
        pass

def rundet():
    
    from selenium import webdriver
    from selenium.webdriver.common.action_chains import ActionChains

    import xlwings as xw 
    wb=xw.Book("C:\\Users\\Public\\"+varr.get())
    sht1=wb.sheets['New File']
                        
    sht1['A1'].value = "ASINS"
                        
    w='error'
    x='error'
    s='error'
    y="unavailable"
    kin=[]
    n=1
    nil=2
    glis=[]
    glist=[]
    lis=[]
    import time
    options = webdriver.ChromeOptions() 
    #options.add_argument("user-data-dir=C:\\Users\\rajra\\AppData\\Local\\Google\\Chrome\\new user data")

    options.add_argument("user-data-dir=C:\\Users\\rajra\\ch.browse - Copy\\new user data1")
    
    driver= webdriver.Chrome(executable_path="driver/chromedriver.exe", chrome_options=options)

    #sheet=gc.open("new inventory").worksheet('Sheet10')
    #sheets=gc.open("new inventory").worksheet('Sheet3')

    try:
        for j in range(2,10):
            
            col=sht1['A'+str(j)].value
            try:
                driver.get("https://www.amazon.com/s?k="+str(col)+"&ref=nb_sb_noss")

                driver.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div[1]/span/div/div/div[1]").text
            except Exception:

                
                driver.get("https://www.amazon.com/dp/"+str(col)+"/")
                time.sleep(3)



                #action = ActionChains(driver)
                #firstLevelMenu = driver.find_element_by_id("acrPopover")
                #action.move_to_element(firstLevelMenu).perform()
                #time.sleep(5)


                glis.append(driver.current_url)
                try:
                    a=driver.find_element_by_xpath("//*[@id='productTitle']").text
                except Exception:
                    print(y)
                    glis.append(y)
                else:
                    print(a)
                    glis.append(a)



                try:
                    b=driver.find_element_by_xpath("//*[@id='bylineInfo']").text
                except Exception:
                    print(y)
                    glis.append(y)
                else:
                    print(b)
                    glis.append(b)



                try:
                    c=driver.find_element_by_xpath("//*[@id='priceblock_ourprice']").text

                except Exception:
                    try:
                        z=driver.find_element_by_xpath("//*[@id='priceblock_businessprice']").text
                        
                    except Exception:
                        try:
                            q=driver.find_element_by_xpath("//*[@id='priceblock_saleprice']").text
                        except Exception:
                            try:
                                p=driver.find_element_by_xpath("//*[@id='priceblock_dealprice']").text 
                            except Exception:
                                print("none")
                                glis.append("none")
                            else:
                                print(p)
                                glis.append(p)
                        else:
                            print(q)
                            glis.append(q)
                    else:
                        glis.append(z)
                else:
                    print(c)
                    glis.append(c)

                #glis.append('')
                #glis.append('')
                try:
                    u=driver.find_element_by_id('acrPopover').get_attribute('title')
                except Exception:
                    print(y)
                    glis.append(y)
                else:
                    print(u)
                    glis.append(u)



                try:
                    d=driver.find_element_by_xpath("//*[@id='merchant-info']").text
                    d.replace("\\n","")
                    
                except Exception:
                    print("not available")
                    glis.append("not available")
                else:
                    if(len(d)==0):
                        print("not available")
                        glis.append("not available")
                    else:
                        glis.append(d)
                        print(d)


                try:
                    e=driver.find_element_by_xpath("//*[@id='availability']/span").text
                    e.replace("\n","")
                except Exception:
                    print(y)
                    glis.append(y)
                else:
                    print(e)
                    glis.append(e)



                try:
                    k=driver.find_elements_by_tag_name("tbody")
                    for i in k:
                        l=i.text
                        if 'Weight' in l:
                            b=l.split('\n')
                            for i in b:
                                if "Item Weight" in i:
                                    w=i.replace("Item Weight","")

                    

                    for i in k:
                        l=i.text
                        if 'Product Dimensions' in l:
                            b=l.split('\n')
                            for i in b:
                                if "Product Dimensions" in i:
                                    x=i.replace("Product Dimensions","")




                    for i in k:
                        l=i.text
                        if 'Date First Available' in l:
                            b=l.split('\n')
                            for i in b:
                                if "Date First Available" in i:
                                    s=i.replace("Date First Available","")

                                    
                except Exception:
                    print(y)
                    glis.append(y)
                    glis.append(y)
                    glis.append(y)

                        
                else:
                    print(w)
                    print(x)
                    print(s)
                    glis.append(w)
                    glis.append(x)
                    glis.append(s)
                

                if glis[9]=="error":
                    l=driver.find_element_by_id("descriptionAndDetails").text
                    b=l.split("\n")
                    for i in b:
                        if "Product Dimensions" in i:
                            x=i.replace("Product Dimensions:","")
                        else:
                            pass
                    print()


                    for i in b:
                        if "Date First Available" in i:
                            s=i.replace("Date First Available:","")
                        else:
                            pass
                    print()


                    for i in b:
                        if "Weight" in i:
                            w=i.replace("Item Weight:","")
                        else:
                            pass
                    print()
                    
                    print(w)
                    print(x)
                    print(s)
                    glis[7]=w
                    glis.append(x)
                    glis.append(s)

                else:
                    print(y)
                    glis.append(w)
                    glis.append(x)
                    glis.append(s)
                    
                
                print(glis[6])
                p=glis[8]
                print(p)

                try:
                    if 'ounces' in str(p):
                        h=0.5
                        glis.append(h)
                    else:
                    
                        if 'pound' in str(p):
                            res = re.findall("[-+]?\d*\.\d+|\d+", glis[8])
                            print(res[0])
                            r=float(res[0])
                            glis.append(r)
                        else:
                            glis.append(y)
                except Exception:
                    glis.append(y)
                else:
                    pass


                


                #sheet.insert_row(glis,2)
                #print(glis)
                driver.quit
                #glis=[]
                #prime stock
                if (glis[7]!="In S"):
                    driver.get("https://www.amazon.com/gp/offer-listing/"+str(col)+"/ref=olp_f_new?ie=UTF8&f_primeEligible=true&f_new=true")
                    try:
                        k=driver.find_element_by_xpath("//*[@id='raw-platform-refinement-div']/fieldset[1]/ul/span[1]/div/label/span/span/i").get_attribute("aria-label")
                        driver.find_element_by_xpath("//*[@id='raw-platform-refinement-div']/fieldset[2]/ul/span/div/label/span/span").text
                        time.sleep(2)

                        try:
                            for i in range(2,7):
                                
                                d=driver.find_element_by_xpath("//*[@id='olpOfferList']/div/div/div["+str(i)+"]").text
                                din=d.split('\n')
                            
                                #res = re.findall("[-+]?\d*\.\d+|\d+", d)
                                for i in din:
                                    if '$' in i:
                                        print(i)
                                        kin.append(i) 
                            print()         
                        except Exception:
                            pass
                        else:
                            pass

                        

                    except Exception:

                        glis.append("NO")
                        glis.append("none")
                        print("NO")
                        print("none")
                    else:

                        glis.append("YES")
                        sel=','.join(kin)
                        glis.append(sel)
                        print(sel)
                        kin=[]
                else:
                    print("YES")
                    glis.append("YES")
                    print("not required")
                    glis.append("not required")


                if(glis[13]==''):
                    glis[12]='NO'
                    
                else:
                    pass
                #sheet.insert_row(glis,2)
                print(glis)
                m=1
                for l in range(68,82):
                    
                    sht1[chr(l)+str(nil)].value=glis[m-1]
                    m=m+1
                    
                print()
                nil=nil+1
                #driver.quit
                glis=[]
            else:
                m=1
                urr=driver.current_url
                glis.extend([urr,y,y,y,y,y,y,y,y,y,y,y,y])
                #sheet.insert_row(glis,2)
                for l in range(68,82):
                    
                    sht1[chr(l)+str(nil)].value=glis[m-1]
                    m=m+1
                    
                print()
                
                print(glis)
                #driver.quit
                glis=[]
            #nil=nil+1
        print()


    except Exception as h:
        print(h)
    else:
        pass

#print(driver.find_element_by_xpath("//*[@id='a-popover-content-11']/div/div/div/div[1]/span").text)

#ash.config(bg='systemTransparent')
#messagebox.showinfo("pop up message","are you sure to quit!!!!!")
ru=tk.Button(root,text="RUN",font=('Helvetica',10,'bold'),command=null5,image=photo2,compound=CENTER)

ru.config(bg='#6E8AB1',bd=0,fg='red')
ru.pack()
canvas.create_window(850, 450, anchor='nw', window=ru)

  
root.mainloop()


#//*[@id="nav-search-submit-text"]/input
