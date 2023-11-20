from tkinter import *  # tkinter is used for making the GUI application
from tkinter import ttk # ttk used for making stylish interface
from PIL import Image,ImageTk  #install -- pip install pillow install from cmd
import random, os #it will used to generate random number for bill no
from tkinter import messagebox
import tempfile
from time import strftime



class  Bill_App:
    def __init__(self, root):  #defining constructor
        self.root = root  # initialising root, creating a window i.e. root
        self.root.geometry("1350x700+0+0") # defining the size of a window , 1530x800+0(x)+0(y)
        self.root.title("Billing Software") # giving our window a title

        # ==================Variables==================
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)  #randint is a function inside random package to generate random number in specified range
        self.bill_no.set(z) # this will set range of bill_no to generate randomly
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()


        # Product Categories
        self.Category=["Select Option","Clothing", "LifeStyle", "Mobile"]

        # SubCatClothing
        self.SubCatClothing=["Pant", "T-Shirt","Shirt"]
        self.pant=['Levis','Mufti','Spykar']
        self.price_levis=5000
        self.price_mufti=2000
        self.price_spykar=3000

        self.T_shirt=['Polo','Roadster','Jack&Jones']
        self.price_polo=1500
        self.price_Roadster=1800
        self.price_JackJones=1700

        self.Shirt=['Peter England', "Louis Phillipe","Park Avenue"]
        self.price_Peter=2100
        self.price_Louis=2700
        self.price_Park=1700

        # SubCatLifeStyle
        self.SubCatLifeStyle=['Bath Soap','Face Cream', 'Hair Oil']
        self.Bath_soap=['Dettol', "Savlon", "Lifebouy",'Dove']
        self.price_Dettol=40
        self.price_Savlon=55
        self.price_Life=30
        self.price_Dove=60

        self.Face_Cream=['Fair&lovely','Ponds','Olay','Garnier']
        self.price_fair=40
        self.price_ponds=55
        self.price_olay=70
        self.price_garnier=100

        self.Hair_OIl=['Parachute','Bajaj Almond','Navratan']
        self.price_para=60
        self.price_baja=75
        self.price_navratan=120

        # SubCatMobiles
        self.SubCatMobiles=['Iphone',"Samsung", "Xiaomi",'Realme','OnePlus']
        self.Iphone=['Iphone_X','Iphone_11','Iphone_12']
        self.price_ix=40000
        self.price_i11=50000
        self.price_i12=60000

        self.Samsung=['Samsung M16','Samsung M12','Samsung M21']
        self.price_sm16=16000
        self.price_sm12=12000
        self.price_sm21=20000

        self.Xiaomi=['Red11','Redme-12','RedmePro']
        self.price_r11=15000
        self.price_r12=17000
        self.price_rpro=21000        

        self.Realme=['RealMe 12','RealMe 13','RealMePro']
        self.price_rel12=25000
        self.price_rel13=22000
        self.price_relpro=26000
        
        self.OnePlus=['OnePlus1','OnePlus2','OnePlus3']
        self.price_one1=45000
        self.price_one2=55000
        self.price_one3=60000
        
        
         # Image1
        img=Image.open("image/1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=500, height=130)

         # Image2
        img_1=Image.open("image/2.jpg")
        img_1=img_1.resize((500,130),Image.ANTIALIAS) 
        self.photoimg_1=ImageTk.PhotoImage(img_1)  # creating variables using self becomes the class variable

        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=500,y=0,width=500, height=130)

        # Image3
        img_2=Image.open("image/1.jpg")
        img_2=img_2.resize((500,130),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl_img_2=Label(self.root,image=self.photoimg)
        lbl_img_2.place(x=1000,y=0,width=500, height=130)

        lbl_title=Label(self.root,text="BILLING SOFTWARE USING PYTHON", font=("times new roman", 25, "bold"), bg="white", fg="red")
        lbl_title.place(x=0, y=130, width=1400, height=40)


        def time():
            string= strftime('%H:%M:%S %p') # %p is for am and pm
            lbl.config(text = string)
            lbl.after(1000, time) # 1000 = 1 second

        lbl = Label(lbl_title, font= ('times new roman',16,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=120,height=50)
        time()

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=5,y=175,width=1360,height=530)

        # Customer Label Frame
        Cust_Frame=LabelFrame(Main_Frame, text="Customer",font=("times new roman", 12, "bold"), bg="white", fg="red")
        Cust_Frame.place(x=10,y=5,width=320,height=140)

        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("arial", 10, "bold"), bg="white")
        self.lbl_mob.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phone,font=("arial", 10, "bold"),width=24)
        self.entry_mob.grid(row=0, column=1)

        self.lblCustName=Label(Cust_Frame,font=('arial',10,'bold'),bg='white',text="Customer Name:", bd=4)
        self.lblCustName.grid(row=1, column=0, sticky=W, padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("arial", 10, "bold"),width=24)
        self.txtCustName.grid(row=1,column=1, sticky=W,padx=5,pady=2)

        self.lblEmail=Label(Cust_Frame,font=('arial', 10,'bold'), bg="white",text="Email:",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W, padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email, font=('arial',10,'bold'),width=24)
        self.txtEmail.grid(row=2, column=1, sticky=W,padx=5, pady=2)

        # Product Label Frame
        Product_Frame=LabelFrame(Main_Frame, text="Product",font=("times new roman", 12, "bold"), bg="white", fg="red")
        Product_Frame.place(x=340,y=5,width=600,height=140)

        # Category
        self.lblCategory=Label(Product_Frame,font=('arial', 10,'bold'), bg="white",text="Select Categories",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W, padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=('arial', 10,'bold'),width=24,state='readonly')
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>", self.Categories)


        # SubCategory
        self.lblSubCategory=Label(Product_Frame,font=('arial', 10,'bold'), bg="white",text="Subcategory",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W, padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame, value=[""],state='readonly',font=('arial', 10,'bold'),width=24)
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        # Product Name
        self.lblproduct=Label(Product_Frame,font=('arial',10,'bold'),bg="white", text="Product Name", bd=4)
        self.lblproduct.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,state="readonly",font=('arial',10,'bold'), width=24)
        self.ComboProduct.grid(row=2, column=1, sticky=W, padx=5, pady=2) 
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)       

        # Price
        self.lblPrice=Label(Product_Frame,font=('arial',10,'bold'),bg="white", text="Price", bd=4)
        self.lblPrice.grid(row=0, column=2, sticky=W, padx=5, pady=2)

        self.ComboPrice=ttk.Combobox(Product_Frame,state="readonly",textvariable=self.prices,font=('arial',10,'bold'), width=24)
        self.ComboPrice.grid(row=0, column=3, sticky=W, padx=5, pady=2) 

        # Qty
        self.lblQty=Label(Product_Frame,font=('arial',10,'bold'),bg="white", text="Qty", bd=4)
        self.lblQty.grid(row=1, column=2, sticky=W, padx=5, pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=('arial',10,'bold'), width=26) # state="readonly", add if needed, for time being removed
        self.ComboQty.grid(row=1, column=3, sticky=W, padx=5, pady=2)

        # Middle Frame
        MiddleFrame=Frame( Main_Frame,bd=10,bg="pink")
        MiddleFrame.place(x=10, y=150, width=930, height=340)

         # Image1
        img12=Image.open("image/4.jpeg")
        img12=img12.resize((460,210),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        lbl_img12=Label(MiddleFrame,image=self.photoimg12)
        lbl_img12.place(x=0,y=0,width=440, height=210)

         # Image2
        img_13=Image.open("image/1.jpg")
        img_13=img_13.resize((460,210),Image.ANTIALIAS) 
        self.photoimg_13=ImageTk.PhotoImage(img_13)  # creating variables using self becomes the class variable

        lbl_img_13=Label(MiddleFrame,image=self.photoimg_13)
        lbl_img_13.place(x=450,y=0,width=460, height=210)

        # Search
        Search_Frame=Frame(Main_Frame,bd=2, bg="white")
        Search_Frame.place(x=950, y=13, width=400, height=40)


        self.lblBill=Label(Search_Frame,font=('arial',10,'bold'),fg= "white",bg="red", text="Bill Number")
        self.lblBill.grid(row=0, column=0, sticky=W, padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=('arial',10,'bold'), width=26) # state="readonly", removed for the time being
        self.txt_Entry_Search.grid(row=0, column=1, sticky=W, padx=2)


        self.BtnSearch=Button(Search_Frame, command=self.find_bill,text="Search", font=('arial', 10, 'bold'), bg="orangered", fg="white",width=8,cursor="hand2")
        self.BtnSearch.grid(row=0, column=2)


        # RightFrame Bill Area 

        RightLabelFrame=LabelFrame(Main_Frame,text='Bill Area',font=("times new roman", 12, "bold"), bg="white", fg="red")
        RightLabelFrame.place(x=950, y=45,width=390, height=340)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame, yscrollcommand=scroll_y.set, bg="white", fg="blue",font=("times new roman", 12, "bold"))
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        # Bill Counter Label Frame

        Bottom_Frame=LabelFrame(Main_Frame, text="Bill Counter",font=("times new roman", 12, "bold"), bg="white", fg="red")
        Bottom_Frame.place(x=0,y=385,width=1350,height=125)

        self.lblSubTotal=Label(Bottom_Frame,font=('arial',10,'bold'),bg="white", text="Sub Total", bd=4)
        self.lblSubTotal.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.EntrySubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total, state="readonly",font=('arial',10,'bold'), width=26)
        self.EntrySubTotal.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.lbl_Tax=Label(Bottom_Frame,font=('arial',10,'bold'),bg="white", text="Govt Tax", bd=4)
        self.lbl_Tax.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.txt_Tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,state="readonly",font=('arial',10,'bold'), width=26)
        self.txt_Tax.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.lblAmountTotal=Label(Bottom_Frame,font=('arial',10,'bold'),bg="white", text="Total", bd=4)
        self.lblAmountTotal.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txtAmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,state="readonly",font=('arial',10,'bold'), width=26)
        self.txtAmountTotal.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # Button Frame

        Btn_Frame=Frame(Bottom_Frame,bd=2, bg="white")
        Btn_Frame.place(x=320, y=0)

        self.BtnAddtoCart=Button(Btn_Frame,height=2, command=self.AddItem,text="Add to Cart", font=('arial', 15, 'bold'), bg="orangered", fg="white",width=13,cursor="hand2")
        self.BtnAddtoCart.grid(row=0, column=0)

        self.Btngenerate_bill=Button(Btn_Frame,height=2,command=self.gen_bill ,text="Generate Bill", font=('arial', 15, 'bold'), bg="orangered", fg="white",width=13,cursor="hand2")
        self.Btngenerate_bill.grid(row=0, column=1)

        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2, text="Save Bill", font=('arial', 15, 'bold'), bg="orangered", fg="white",width=13,cursor="hand2")
        self.BtnSave.grid(row=0, column=2)

        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height=2, text="Print", font=('arial', 15, 'bold'), bg="orangered", fg="white",width=13,cursor="hand2")
        self.BtnPrint.grid(row=0, column=3)

        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2, text="Clear", font=('arial', 15, 'bold'), bg="orangered", fg="white",width=13,cursor="hand2")
        self.BtnClear.grid(row=0, column=4)

        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,height=2, text="Exit", font=('arial', 15, 'bold'), bg="orangered", fg="white",width=13,cursor="hand2")
        self.BtnExit.grid(row=0, column=5)
        self.welcome()

        self.l=[]
    # =========================== Function Declaration==========================================

    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\t Welcome Mini Mall")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")

        self.textarea.insert(END,"\n========================================")
        self.textarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
        self.textarea.insert(END,"\n========================================\n")

    
    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error", "Please select the Product Name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error", "Please Add to Cart product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n========================================")
            self.textarea.insert(END,f"\n Sub Amount: \t \t \t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount: \t \t \t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount: \t \t \t{self.total.get()}")
            self.textarea.insert(END,"\n========================================")
    
    def save_bill(self):
        op=messagebox.askyesno("Save Bill", "Do you want to save the Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved!", f"Bill No:{self.bill_no.get()} saved successfully")
            f1.close()

    def iprint(self):
        q=self.textarea.get(1.0, "end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found='no'
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0, END)
                for d in f1:
                    self.textarea.insert(END, d)
                f1.close()
                found="yes"
        if found=='no':
            messagebox.showerror("Error","Invalid Bill No")

    def clear(self):
        self.textarea.delete(1.0, END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()
    
    def Categories(self,event=""):
        if self.Combo_Category.get()=="Clothing":
            self.ComboSubCategory.config(value=self.SubCatClothing)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="LifeStyle":
            self.ComboSubCategory.config(value=self.SubCatLifeStyle)
            self.ComboSubCategory.current(0)


        if self.Combo_Category.get()=="Mobile":
            self.ComboSubCategory.config(value=self.SubCatMobiles)
            self.ComboSubCategory.current(0)

    
    def Product_add(self, event=""):
        if self.ComboSubCategory.get()=="Pant":
            self.ComboProduct.config(value=self.pant)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="T-Shirt":
            self.ComboProduct.config(value=self.T_shirt)
            self.ComboProduct.current(0)
        
        if self.ComboSubCategory.get()=="Shirt":
            self.ComboProduct.config(value=self.Shirt)
            self.ComboProduct.current(0)

        # Life Style
        if self.ComboSubCategory.get()=="Bath Soap":
            self.ComboProduct.config(value=self.Bath_soap)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Face Cream":
            self.ComboProduct.config(value=self.Face_Cream)
            self.ComboProduct.current(0)
        
        if self.ComboSubCategory.get()=="Hair Oil":
            self.ComboProduct.config(value=self.Hair_OIl)
            self.ComboProduct.current(0)

        # Mobile
        if self.ComboSubCategory.get()=="Iphone":
            self.ComboProduct.config(value=self.Iphone)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Samsung":
            self.ComboProduct.config(value=self.Samsung)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Xiaomi":
            self.ComboProduct.config(value=self.Xiaomi)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Realme":
            self.ComboProduct.config(value=self.Realme)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="OnePlus":
            self.ComboProduct.config(value=self.OnePlus)
            self.ComboProduct.current(0)

    def price(self, event=""):
        # Pant
        if self.ComboProduct.get()=="Levis":
            self.ComboPrice.config(value=self.price_levis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Mufti":
            self.ComboPrice.config(value=self.price_mufti)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Spykar":
            self.ComboPrice.config(value=self.price_spykar)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # T-shirt
        if self.ComboProduct.get()=="Polo":
            self.ComboPrice.config(value=self.price_polo)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Roadster":
            self.ComboPrice.config(value=self.price_Roadster)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Jack&Jones":
            self.ComboPrice.config(value=self.price_JackJones)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Shirt
        if self.ComboProduct.get()=="Peter England":
            self.ComboPrice.config(value=self.price_Peter)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Louis Phillipe":
            self.ComboPrice.config(value=self.price_Louis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Park Avenue":
            self.ComboPrice.config(value=self.price_Park)
            self.ComboPrice.current(0)
            self.qty.set(1)


        # Bath Soap
        if self.ComboProduct.get()=="Dettol":
            self.ComboPrice.config(value=self.price_Dettol)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Savlon":
            self.ComboPrice.config(value=self.price_Savlon)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Lifebouy":
            self.ComboPrice.config(value=self.price_Life)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Dove":
            self.ComboPrice.config(value=self.price_Dove)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Fari&Lovely":
            self.ComboPrice.config(value=self.price_fair)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Ponds":
            self.ComboPrice.config(value=self.price_ponds)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Olay":
            self.ComboPrice.config(value=self.price_olay)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Garnier":
            self.ComboPrice.config(value=self.price_garnier)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Parachute":
            self.ComboPrice.config(value=self.price_para)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Bajaj Almond":
            self.ComboPrice.config(value=self.price_baja)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Navratan":
            self.ComboPrice.config(value=self.price_navratan)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Iphone_X":
            self.ComboPrice.config(value=self.price_ix)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Iphone_11":
            self.ComboPrice.config(value=self.price_i11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Iphone_12":
            self.ComboPrice.config(value=self.price_i12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Samsung M16":
            self.ComboPrice.config(value=self.price_sm16)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Samsung M12":
            self.ComboPrice.config(value=self.price_sm12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Samsung M21":
            self.ComboPrice.config(value=self.price_sm21)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Red11":
            self.ComboPrice.config(value=self.price_r11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Redme-12":
            self.ComboPrice.config(value=self.price_r12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="RedmePro":
            self.ComboPrice.config(value=self.price_rpro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="RealMe 12":
            self.ComboPrice.config(value=self.price_rel12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="RealMe 13":
            self.ComboPrice.config(value=self.price_rel13)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="RealMePro":
            self.ComboPrice.config(value=self.price_relpro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="OnePlus1":
            self.ComboPrice.config(value=self.price_one1)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="OnePlus2":
            self.ComboPrice.config(value=self.price_one2)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="OnePlus3":
            self.ComboPrice.config(value=self.price_one3)
            self.ComboPrice.current(0)
            self.qty.set(1)





if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop() # mainloop it will remain active untill and unless it is closed (window)
