import sqlite3
import tkinter as tk  # ธีมสำหรับ tk
from tkinter import messagebox

# สร้าง GUI
GUI = tk.Tk()
GUI.title('บันทึกข้อมูลลง SQLite3') #ชื่อโปรแกรม
GUI.geometry('500x500') #ขนาดหน้าต่างโปรแกรม

# เชื่อมต่อกับฐานข้อมูล
conn = sqlite3.connect('data.db')

# สร้าง cursor object เพื่อส่งคำสั่ง SQL
c = conn.cursor()

# สร้างตารางในฐานข้อมูล (ถ้ายังไม่มี)
c.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, name TEXT)')

def insert_data():
    data = data_entry.get()
    sql = 'INSERT INTO data (name) VALUES (?)'
    c.execute(sql, (data,))
    conn.commit()
    print(c.rowcount, 'record inserted.')
    view_data()
    data_entry.set('')

def view_data():
    c.execute('SELECT * FROM data')
    rows = c.fetchall()
    data_list.delete(0, tk.END)
    for row in rows:
        data_list.insert(tk.END, row)

def update_data():
    selected_item = data_list.curselection()
    if selected_item:
        id = data_list.get(selected_item)[0]
        new_data = data_entry.get()
        sql = 'UPDATE data SET name = ? WHERE id = ?'
        c.execute(sql, (new_data, id))
        conn.commit()
        print(c.rowcount, 'record updated.')
        view_data()

def delete_data():
    selected_item = data_list.curselection()
    if selected_item:
        id = data_list.get(selected_item)[0]
        sql = 'DELETE FROM data WHERE id = ?'
        c.execute(sql, (id,))
        conn.commit()
        print(c.rowcount, 'record deleted.')
        view_data()

# สร้าง GUI components
data_label = tk.Label(GUI, text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='Green')
data_label.pack()
data_entry = tk.Entry(GUI)
data_entry.pack()

insert_button = tk.Button(GUI, text='บันทึก', command=insert_data)
insert_button.pack()

view_button = tk.Button(GUI, text='ดูข้อมูล', command=view_data)
view_button.pack()

update_button = tk.Button(GUI, text='แก้ไขข้อมูล', command=update_data)
update_button.pack()

delete_button = tk.Button(GUI, text='ลบข้อมูล', command=delete_data)
delete_button.pack()

data_list = tk.Listbox(GUI)
data_list.pack()

view_data()

GUI.mainloop()
