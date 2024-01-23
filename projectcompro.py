from asyncore import write
import csv
from tkinter import *
from tkinter import ttk



station = ('N24 คูคต','N23 แยก คปอ.','N22 พิพิธภัณฑ์กองทัพอากาศ','N21 โรงพยาบาลภูมิพลอดุลยเดช','N20 สะพานใหม่','N19 สายหยุด','N18 พหลโยธิน 59',
'N17 วัดพระศรีมหาธาตุ','N16 กรมทหารราบที่ 11','N15 บางบัว','N14 กรมป่าไม้',
'N13 มหาวิทยาลัยเกษตรศาสตร์','N12 เสนานิคม','N11 รัชโยธิน','N10 พหลโยธิน 24',
'N9 ห้าแยกลาดพร้าว','N8 หมอชิต','N7 สะพานควาย','N6 เสนาร่วม','N5 อารีย์','N4 สนามเป้า','N3 อนุสาวรีย์ชัยสมรภูมิ','N2 พญาไท','N1 ราชเทวี',
'CEN สยาม','E1 ชิดลม','E2 เพลินจิต','E3 นานา','E4 อโศก','E5 พร้อมพงษ์','E6 ทองหล่อ','E7 เอกมัย','E8 พระโขนง'
,'E9 อ่อนนุช','E10 บางจาก','E11 ปุณณวิถี','E12 อุดมสุข','E13 บางนา','E14 แบริ่ง','E15 สำโรง','E16 ปู่เจ้า','E17 ช้างเอราวัณ','E18 โรงเรียนนายเรือ'
,'E19 ปากน้ำ','E20 ศรีนครินทร์','E21 แพรกษา','E22 สายลวด','E23 เคหะฯ'
,'W1 สนามกีฬาแห่งชาติ','S1 ราชดำริ','S2 ศาลาแดง','S3 ช่องนนทรี','S4 เซนต์หลุยส์','S5 สุรศักดิ์','S6 สะพานตากสิน','S7 กรุงธนบุรี','S8 วงเวียนใหญ่',
'S9 โพธิ์นิมิตร','S10 ตลาดพลู','S11 วุฒากาศ','S12 บางหว้า',
'G1 กรุงธนบุรี','G2 เจริญนคร (ไอคอนสยาม)','G3 คลองสาน')


#หน้าจอ2
def calinterface2():
    interface2 = Tk()
    interface2.title('BTS train ticket booking')
    btout = Button(interface2,text='X',font=70,command=interface2.destroy,padx=5,fg='red',bg='black').pack(anchor=E)

    labeld = Label(interface2,text= showdate()[0] + ' '  + showdate()[1] + ' ' + showdate()[2],font=20).pack()
    
    label = Label(interface2,text="สถานีต้นทาง",font=200).pack(pady=5)
    label2 = Label(interface2,text = (get_values1()[1]),font=200).pack(pady=10)
   

    label3 = Label(interface2,text="สถานีปลายทาง",font=200).pack(pady=10)
    label4 = Label(interface2,text = (get_values2()[1]),font=200).pack(pady=10)

    count_station = abs(int((get_values2()[0])) - int((get_values1()[0])))
    
    label = Label(interface2,text = f"จำนวนสถานี : {count_station}",font=200).pack(pady=10)
    pay = (count_station * 2) + 17
    if pay <= 45 :
        label = Label(interface2,text = f"เงินที่ต้องชำระ :{pay} บาท",font=200).pack(pady=10)
    elif pay > 45:
        pay = 45 
        label = Label(interface2,text = f"เงินที่ต้องชำระ : {pay} บาท",font=200).pack(pady=10)
    

    btsubmit = Button(interface2,text = 'ชำระเงิน',font = 200,command= calinterface3).pack(pady=10)
    interface2.minsize(700,400)
    interface2.mainloop()


#หน้าชำระเงินเช็คว่าจ่ายเงินจริง หน้าจอ 3
def calinterface3():
    global interface3
    
    global entry
    
    interface3 = Tk()
    interface3.title('BTS train ticket booking')
    interface3.minsize(200,150)
    btout = Button(interface3,text='X',font=70,command=interface3.destroy,padx=5,fg='red',bg='black').pack(anchor=E)
    
    count_station = abs(int((get_values2()[0])) - int((get_values1()[0])))
    
    pay = (count_station * 2) + 17
    
    if pay <= 45 :
        label = Label(interface3,text = f"เงินที่ต้องชำระ :{pay} บาท",font=200).pack(pady=10)
    elif pay > 45:
        pay = 45 
        label = Label(interface3,text = f"เงินที่ต้องชำระ : {pay} บาท",font=200).pack(pady=10)
    labelh = Label(interface3,text='ใส่เงิน').pack()
    num = IntVar()
    entry = Entry(interface3,textvariable=num)
    entry.pack()
    
    btsubmit = Button(interface3,text = 'ยืนยัน',font = 200,command=calcheck).pack(pady=10)
    interface3.resizable(False,False)
    interface3.mainloop()



#ฟังก์ชันเช็คว่าจ่ายตามจำนวน

def calcheck():
    global totaln
    count_station = abs(int((get_values2()[0])) - int((get_values1()[0])))
    pay = (count_station * 2) + 17
    if pay <= 45:
        pay=pay
        
    elif pay > 45:
        pay = 45 
    
    totaln = int(entry.get())
    
    while True:
        if totaln == pay:
            calinterface4()
            break
        else:
            labelf = Label(interface3,text='โปรดใส่เงินให้ครบตามจำนวน').pack()
            break
        
#หน้าจอ4
def calinterface4():
    interface4 = Tk()
    interface4.title('BTS train ticket booking')
    interface4.minsize(700,400)

    btout = Button(interface4,text='X',font=70,command=interface4.destroy,padx=5,fg='red',bg='black').pack(anchor=E)

    labeld = Label(interface4,text= showdate()[0] + ' '  + showdate()[1] + ' ' + showdate()[2],font=20).pack()
    label = Label(interface4,text="สถานีต้นทาง",font=200).pack(pady=5)

    label2 = Label(interface4,text = (get_values1()[1]),font=200).pack(pady=10)
   
    label3 = Label(interface4,text="สถานีปลายทาง",font=200).pack(pady=10)
    label4 = Label(interface4,text = (get_values2()[1]),font=200).pack(pady=10)


    count_station = abs(int((get_values2()[0])) - int((get_values1()[0])))
    pay = (count_station * 2) + 17
    if pay <= 45:
        pay=pay
        
    elif pay > 45:
        pay = 45 

    label5 = Label(interface4,text = f"จำนวนสถานี : {count_station}",font=200).pack(pady=10)

    label = Label(interface4,text = f"ชำระแล้ว :{totaln} บาท",font=200).pack(pady=10)
    
    
    fliegetall = 'getall.csv'
    filealltxt = 'getall.txt'
    getall = [[str((showdate()[0]))+' '+str((showdate()[1]))+' '+str((showdate()[2]))],[str(get_values1()[1])],[str(get_values2()[1])],[str(count_station)] , [str(pay)]]
    
    with open(fliegetall,'a',encoding='utf-8')as outgetall:
        writefile = csv.writer(outgetall)
        writefile.writerow(getall)

        print(getall)
    interface4.mainloop()

    
    

    
    
#สถานีต้นทาง   
def get_values1(*arg):
    
    val_station1 = str(station1.current()),str(var1.get())
    return val_station1

#สถานีปลายทาง
def get_values2(*arg):
    
    val_station2 = str(station2.current()),str(var2.get())
    return val_station2

#แสดงวันที่เลือก
def showdate(*arg):
    sm = dayget.get(),monthget.get(),yearget.get()
    return sm


monthlist = [['January'],['February'],['March'],['April'],['May'],
['June'],['July'],['August'],['September'],['October'],['November'],['December']]
           




#หน้าจอแรก
interface = Tk()
interface.title('BTS train ticket booking')

interface.option_add('*Font','DubaiMedium 15')

btout = Button(interface,text='X',font=70,command=interface.destroy,padx=5,fg='red',bg='black',bd=5).grid(row=0,column=6)
label1 = Label(interface,text="BTS train ticket booking",font=200).grid(row=1,column=5)

label = Label(interface,text="สถานีต้นทาง",font=300).grid(row=2,column=5)

var1 = StringVar()
station1 = ttk.Combobox(interface,textvariable=var1,font=200,state='readonly')
station1['values'] = station
station1.grid(row=3,column=5)

label = Label(interface,text="สถานีปลายทาง",font=200).grid(row=4,column=5)

var2 = StringVar()
station2 = ttk.Combobox(interface,textvariable=var2,font=200,state='readonly')
station2['values'] = station
station2.grid(row=5,column=5)

dayget = StringVar()
day = ttk.Combobox(interface,textvariable=dayget,width=2,state='readonly')
day['values'] = list(range(1,32))
day.current(0)
day.grid(row=8,column=4)


        
monthget = StringVar()
month = ttk.Combobox(interface,textvariable=monthget,width=10,state='readonly')
month['values'] = monthlist
month.current(0)
month.grid(row=8,column=5)

yearget =StringVar()
year= ttk.Combobox(interface,textvariable=yearget,width=4,state='readonly')
year['values'] = list(range(2022,2031))
year.current(0)
year.grid(row=8,column=6)

btok = Button(interface,text='OK',command=calinterface2,font=200,bd=5).grid(row=9,column=5)

interface.resizable(False,False)

interface.mainloop()








