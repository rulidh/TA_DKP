from tkinter import *
from tkinter import ttk

class newWindow1:
    def __init__(self, master):
        self.master= master

        self.header= Label(self.master, text='Selamat Datang di UNDIP Healthcare').pack()
        self.description= Label(self.master, text='UNDIP Healthcare merupakan salah satu fasilitas\nyang terdapat dalam '
                                                  'Universitas Diponegoro dalam\nmembantu mahasiswa UNDIP memeriksa '
                                                  'kesehatan\nmelalui angka bmi yang nantinya bisa diteruskan\nkepada '
                                                  'pihak yang berwenang jika kesehatan \nmahasiswa terganggu', width=41)
        self.description.pack(pady=20)

        self.daftar_button= Button(self.master, text='Sign in',command=self.daftar_window).place(x=135, y= 170)
    def daftar_window(self):
        self.master.withdraw()
        daftar_window= Toplevel(self.master)
        daftar_window.geometry("320x240")
        daftar_window.resizable(width=0, height=0)
        newWindow2(daftar_window)
class newWindow2:
    def __init__(self, master):
        self.master= master

        self.header= Label(self.master, text='Pendaftaran UNDIP Healthcare').pack()
        self.labels()

        self.user_entry= Entry(self.master, width=22, textvariable=name)
        self.user_entry.place(x=120, y=34)
        self.nim_entry= Entry(self.master, width=22, textvariable=nim)
        self.nim_entry.place(x=120, y=64)
        self.email_entry = Entry(self.master, width=22, textvariable=email)
        self.email_entry.place(x=120, y=94)
        self.password_entry = Entry(self.master, width=22, show="*")
        self.password_entry.place(x=120, y=124)

        self.login_button= Button(self.master, text='Login', command=self.login_window).place(x=145, y=160)
        self.quit= Button(self.master, text='Quit Program', command=self.quit).place(x=240, y=215)
    def labels(self):
        self.labels= ['Nama', 'NIM', 'Email', 'Password']

        for i in range(len(self.labels)):
            self.label= 'label'+ str(i)
            self.label= ttk.Label(self.master, text=self.labels[i])
            self.label.place(x=60, y=32+(i*30))
    def login_window(self):
        if self.user_entry.get() and self.nim_entry.get() and "@students.undip.ac.id" in self.email_entry.get() and self.password_entry.get():
            self.master.withdraw()
            login_window = Toplevel(self.master)
            login_window.geometry("320x240")
            login_window.resizable(width=0, height=0)
            newWindow3(login_window)
        else:
            if "@" not in self.email_entry.get():
                self.label= Label(self.master, text='Format Email salah', width=40)
                self.label.place(x=25 ,y=195)
            else:
                self.label= Label(self.master, text='Silahkan pakai email UNDIP')
                self.label.place(x=90 ,y=195)
    def quit(self):
        main_window.destroy()
class newWindow3:
    def __init__(self, master):
        self.master= master

        self.header= Label(self.master, text='Pengecekan Kesehatan').pack()
        self.login_notif= Label(self.master, text='*Login Berhasil', font= ("Arial", 7)).place(x=0, y=1)

        self.canvas= Canvas(self.master, width=320, height=240)
        self.canvas.pack()
        self.canvas.create_rectangle(0, 50, 320, 240, outline= "black")

        self.user_label= Label(self.master, text="Nama : "+ name.get())
        self.user_label.place(x=40, y=24)
        self.nim_label= Label(self.master, text="NIM    : "+ nim.get())
        self.nim_label.place(x=40, y=44)
        self.berat_label= Label(self.master, text='Berat Badan (kg)').place(x=70, y=88)
        self.tinggi_label= Label(self.master, text='Tinggi Badan (m)').place(x=70, y=113)

        self.berat_entry= Entry(self.master, width=10, textvariable=berat_badan)
        self.berat_entry.place(x=170, y=90)
        self.tinggi_entry= Entry(self.master, width=10, textvariable=tinggi_badan)
        self.tinggi_entry.place(x=170, y=115)

        self.btn= Button(self.master, text='Cek BMI kamu', command=self.inputFormat)
        self.btn.place(x=120, y=150)
        self.quitbtn= Button(self.master, text='Quit', command=self.quit)
        self.quitbtn.place(x=288, y=215)
        self.printbtn= Button(self.master, text='Print', command=self.bmiPrint)
        self.printbtn.place(x=0, y= 215)

    def quit(self):
        main_window.destroy()

    def bmiValue(self):
        return float(self.berat_entry.get()) / (float(self.tinggi_entry.get()) * float(self.tinggi_entry.get()))

    def bmiInfo(self):
        if self.bmiValue()<= 18.5:
            self.label= Label(self.master, text='Kekurangan berat badan\nJangan lupa Makan', borderwidth=5)
            self.label.place(x=97, y=190)
        elif self.bmiValue()> 18.5 and self.bmiValue()<= 24.9:
            self.label= Label(self.master, text='Normal, Pertahankan', borderwidth=20)
            self.label.place(x=89, y=185)
        elif self.bmiValue()>=25.0 and self.bmiValue()<=29.9:
            self.label = Label(self.master, text='Kelebihan berat badan\nAtur Jadwal Makan', borderwidth=10)
            self.label.place(x=97, y=187)
        else:
            self.label = Label(self.master, text='Obesitas\nDisarankan pergi ke Dokter', borderwidth=5)
            self.label.place(x=90, y=200)

    def bmi(self):
        if float(self.tinggi_entry.get())!= 0.0:
            bmi= self.bmiValue()
            return bmi
        else:
            self.zero_error= Label(self.master, text='Tidak bisa dibagi dengan 0', borderwidth=20)
            self.zero_error.place(x=75, y=175)
            return self.zero_error

    def bmiPrint(self):
        if '.' not in self.berat_entry.get() or '.' not in self.tinggi_entry.get():
            print("Pakai Desimal")
        elif float(self.tinggi_entry.get()) == 0.0:
            print("Format salah, gagal print")
        else:
            print("==========UNDIP Healthcare==========")
            print("------------------------------------")
            print("==========Hasil Pengecekan==========")
            print("Nama:", name.get())
            print("NIM:", nim.get())
            print("Berat Badan  :", self.berat_entry.get(), "kg")
            print("Tinggi Badan :", self.tinggi_entry.get(), "m")
            print("Hasil BMI:", self.bmiValue())

    def inputFormat(self):
        if '.' not in self.berat_entry.get() or '.' not in self.tinggi_entry.get():
            self.error_label= Label(self.master, text='Use Decimal Format', borderwidth=20)
            self.error_label.place(x=90, y=175)
        elif float(self.tinggi_entry.get())== 0.0:
            self.bmi()
        else:
            self.bmiInfo()
            self.bmi_label = Label(self.master, text=self.bmiValue())
            self.bmi_label.place(x=115, y=175)

main_window= Tk()
main_window.title("UNDIP Healthcare")
main_window.geometry("320x240")
main_window.resizable(width=0, height=0)
login= newWindow1(main_window)

name= StringVar()
nim= StringVar()
email= StringVar()

tinggi_badan= DoubleVar()
berat_badan= DoubleVar()

main_window.mainloop()