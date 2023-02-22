#WIFI PASS

from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('500x600+600+100')
GUI.title('โปรแกรมเก็บข้อมูล Wifi')
GUI.iconbitmap('ICON/icon.ico')
# กำหนด font และ ขนาด
style = ttk.Style()
style.theme_use('default')
style.configure('my.TButton',
	 font=('Arial', 16 ,'bold'),
	 foreground='blue',
	 background='green')

FONT1 = ('Cordia New',20,'bold')
FONT2 = ('Cordia New',26)
import sqlite3
############DATABASE###############
conn = sqlite3.connect('ssid.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS ssid (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
		ssid text,
		pas text,
		ipadd int)""")


def insert_ssid(ssid,pas,ipadd):
    ID = None
    #score = 0
    with conn:
        c.execute("""INSERT INTO ssid VALUES (?,?,?,?)""",
                  (ID,ssid,pas,ipadd))
    conn.commit()
    print('Data was inserted')


def view_ssid():
    with conn:
        c.execute("SELECT * FROM ssid")
        allssid = c.fetchall()
        print(allssid)

    return allssid
#######SSID#########
L1 = ttk.Label(GUI, text='ชื่อ WiFi',font=FONT1)
L1.pack(pady=15)

v_ssid = StringVar()
E1 =ttk.Entry(GUI,textvariable=v_ssid,font=FONT1,width=20)
E1.pack()

#######password#########
L2 = ttk.Label(GUI, text='PassWord WiFi',font=FONT1)
L2.pack(pady=15)

v_pass = StringVar()
E2 = ttk.Entry(GUI,textvariable=v_pass,font=FONT1,width=20)
E2.pack()

#######IP ADDRESS#########
L3 = ttk.Label(GUI, text='Ip Address',font=FONT1)
L3.pack(pady=15)

v_ipaddress = StringVar()
E3 =ttk.Entry(GUI,textvariable=v_ipaddress,font=FONT1,width=20)
E3.pack()

########BUTTON#############
def Save(event=None):
	ssid = v_ssid.get()
	pas = v_pass.get()
	ipadd = v_ipaddress.get()
	print('SSID: {} Pass: {}'.format(ssid,pas))
	##เคลียค่าในช่องหลังจากบันทึก
	v_ssid.set('')
	v_pass.set('')
	v_ipaddress.set('')
	E1.focus()
	print('_________')


B1 = ttk.Button(GUI,text='บันทึก',style='my.TButton',command=Save)
B1.pack(ipadx=10,ipady=5,pady=15)

E3.bind('<Return>',Save)


GUI.mainloop()