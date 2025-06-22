# สาโรจน์ พราหมณ์แก้ว 6709616913 เลขที่ 39

# Widgets : Listbox, messagebox, spinbox, labelFrame 
# Widgets (ธรรมดา) : Frame, Label, Button, Entry 
# Widgets (เพิ่มเติม) :
#   Combobox บรรทัดที่ 116, 126, 136, 146
#   PhotoImage บรรทัดที่ 69, 84, 87, 90, 93

# อธิบาย : โปรแกรมสำหรับสั่งซื้อสินค้าโดยมี widgets ต่าง ๆ ประกอบข้างต้น 
# เมื่อเลือกสินค้าก็ให้ระบุ ขนาดและจำนวน จากนั้นก็เพิ่มลงตะกร้า
# ตัวสินค้าจะอยู่ที่ "My Shopping Cart" แต่ก่อน "Buy" สามารถแก้ไขก่อนทำการสั่งซื้อได้
# โดยให้กรอกข้อมูลที่เป็นที่บ่งบอกถึงความเป็นเจ้าของและจะให้จัดส่งไปที่ใด  
# อย่างเช่น ชื่อ นามสกุล เบอร์โทร ที่อยู่ 
# แต่ถ้าไม่ได้ระบุของความเป็นบุคคลและไม่ได้มีรายการสั่งซื้อลงไป ก็ไม่สามารถสั่งซื้อสินค้าได้


from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# เข้าทำเมื่อกด "Buy" โดยแสดงว่ารายละเอียดของผู้สั่งและการสั่งซื้อสำเร็จแล้ว
def enter_data():
    fname = e1.get()
    lname = e2.get()
    tel = e3.get()
    addrs = e4.get()

    if len(fname) != 0 and len(lname) != 0 and len(tel) != 0 and len(addrs) != 0:
        info = "-----Your Order completed-----\nName: " + fname + " " + lname + " \nAddress: " + addrs
        
        msg = messagebox.showinfo("Order completed", info) #Messagebox: Notification that
        
    else:
        print("Please fill in completely infomation")

# เมื่อมีการกด "Add to Cart" ทำให้รายละเอียดที่ได้กรอกแล้วครบถ้วนอย่าง size และ จำนวนชิ้น จะส่งรายละเอียดมาที่
# "My Shopping Cart" เพื่อจะตัดสินใจการซื้อต่อไป
def addtocart(a, getcb, getsp):
    if getsp != "0" and getcb != "Select your size":
        if a == 1:
            list_box.insert(END,"T-shirt " + getcb + " " + getsp)
        elif a == 2:
            list_box.insert(END,"Trousers" + getcb + " " + getsp)
        elif a == 3:
            list_box.insert(END,"Hat" + getcb + " " + getsp)
        else:
            list_box.insert(END,"Bag" + getcb + " " + getsp)
    else:
        print("Please fill in completely infomation")

# เมื่อมีการเลือกรายการในส่วน "My Shopping Cart" และกด "Delete item" จะสามารถลบรายการนั้นได้
# มีการเช็ค Error คือเมื่อไม่มีรายการอะไร แต่กดปุ่ม "Delete item" ก็จะไม่มีอะไร Error แจ้งเตือนใด ๆ
def del_item():
    try:
        indx = list_box.curselection()
        list_box.delete(indx)
    except Exception:
        pass

#สร้าง main window
base = Tk()
base.title("KaiTom Shopping")

frm = Frame(base)
frm.pack()

inside_header = Frame(frm, height=30)
inside_header.grid()

image_path = PhotoImage(file="image/Headerbar.png",height=150, width=462) #PhotoImage: Display Header image 
label_img = Label(inside_header, image = image_path) # ใช้ Label ในการแสดง image จาก PhotoImage
label_img.pack()
        
inside_main = Frame(frm, height=30, width= 100)
inside_main.grid()

#inside left
ins_main_left = Frame(inside_main, height=30, width= 200)
pd1 = LabelFrame(ins_main_left, text = "T-Shirt") #LabelFrame: T-Shirt
pd2 = LabelFrame(ins_main_left, text = "Trousers") #LabelFrame: Trousers
pd3 = LabelFrame(ins_main_left, text = "Hat") #LabelFrame: Hat
pd4 = LabelFrame(ins_main_left, text = "Shoulder bag") #LabelFrame: Shoulder bag

img_pd1 = PhotoImage(file="image/tshirt.png") #PhotoImage: Display product 1
lb1_img = Label(pd1, image = img_pd1)

img_pd2 = PhotoImage(file="image/trousers.png") #PhotoImage: Display product 2
lb2_img = Label(pd2, image = img_pd2)

img_pd3 = PhotoImage(file="image/hat.png") #PhotoImage: Display product 3
lb3_img = Label(pd3, image = img_pd3)

img_pd4 = PhotoImage(file="image/bag.png") #PhotoImage: Display product 4
lb4_img = Label(pd4, image = img_pd4)

lb1_img.pack()
lb2_img.pack()
lb3_img.pack()
lb4_img.pack()

#inside right
ins_main_right = Frame(inside_main, width= 100, padx=10, pady=28)

#listbox
lst_frame = LabelFrame(ins_main_right, text="My Shopping Cart")
list_box = Listbox(lst_frame,width=24)
cfrm_btn = Button(ins_main_right, text="Buy",padx=71, borderwidth=3 , relief="raised",command = enter_data)
list_del_btn = Button(lst_frame, text="Delete item", command = del_item)
#listbox


#add info of Product
#pd1
lst_size = ["S","M","L","XL"]
lst_hat = ["54-55","56-57","58-59","60-61"]
lst_bag = ["20x25x12","25x30x12"]

cb1 = ttk.Combobox(pd1, value = lst_size, width = 15) #Dropdown: about size of T-Shirt
cb1.set("Select your size")
sp1 = Spinbox(pd1, from_= 0, to = 100, width = 16) 
t1_btn = Button(pd1, text="Add to Cart", command = lambda: addtocart(1, cb1.get(), sp1.get()))

cb1.pack(pady=(5,0))
sp1.pack(pady=(5,0))
t1_btn.pack(pady=(5,5))

#pd2
cb2 = ttk.Combobox(pd2, value = lst_size, width = 15) #Dropdown: about size of Trousers
cb2.set("Select your size")
sp2 = Spinbox(pd2, from_= 0, to = 100, width = 16)
t2_btn = Button(pd2, text="Add to Cart", command = lambda: addtocart(2, cb2.get(), sp2.get()))

cb2.pack(pady=(5,0))
sp2.pack(pady=(5,0))
t2_btn.pack(pady=(5,5))

#pd3
cb3 = ttk.Combobox(pd3, value = lst_hat, width = 15) #Dropdown: about size of Hat
cb3.set("Select your size")
sp3 = Spinbox(pd3, from_= 0, to = 100, width = 16)
t3_btn = Button(pd3, text="Add to Cart", command = lambda: addtocart(3, cb3.get(), sp3.get()))

cb3.pack(pady=(5,0))
sp3.pack(pady=(5,0))
t3_btn.pack(pady=(5,5))

#pd4
cb4 = ttk.Combobox(pd4, value = lst_bag, width = 15) #Dropdown: about size of Shoulder bag
cb4.set("Select your size")
sp4 = Spinbox(pd4, from_= 0, to = 100, width = 16)
t4_btn = Button(pd4, text="Add to Cart", command = lambda: addtocart(4, cb4.get(), sp4.get()))

cb4.pack(pady=(5,0))
sp4.pack(pady=(5,0))
t4_btn.pack(pady=(5,5))
#add info of Product

pd1.grid(row=0, column=0, padx=(6,3), pady=(6,3))
pd2.grid(row=0, column=1, padx=(3,6), pady=(6,3))
pd3.grid(row=1, column=0, padx=(6,3), pady=(3,6))
pd4.grid(row=1, column=1, padx=(3,6), pady=(3,6))

ins_main_left.grid(row=0, column=0)
#inside left

l1 = Label(ins_main_right, text="First Name")
l2 = Label(ins_main_right, text="Last Name")
l3 = Label(ins_main_right, text="Tel")
l4 = Label(ins_main_right, text="Address")

e1 = Entry(ins_main_right,width=16, border=3)
e2 = Entry(ins_main_right,width=16, border=3)
e3 = Entry(ins_main_right,width=16, border=3)
e4 = Entry(ins_main_right,width=27, border=3)

l1.grid(row=0 , column=0)
l2.grid(row=1 , column=0)
l3.grid(row=2 , column=0)
l4.grid(row=3 , column=0)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=4, column=0, columnspan=2)

lst_frame.grid(row=6, column=0, columnspan=2,pady=(30,0))
list_box.pack(padx=10, pady=10)

list_del_btn.pack(side=RIGHT, padx=(0,10), pady=(0,10))
cfrm_btn.grid(row=7, column=0, columnspan=2, pady=(10,0))

ins_main_right.grid(row=0, column=1)
#inside ridht

base.mainloop()