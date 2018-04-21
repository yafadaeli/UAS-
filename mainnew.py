from yafa.nilaim import nilai_mahasiswa
from yafa.pembauas import pembayaran
from yafa.kalku import kalku

def menu():
    print("===================================================")
    print("\n\t---pilihan---")
    print("\t1. penilaian mahasiswa")
    print("\t2. pembayaran mahasiswa")
    print("\t3. kalkulator")
   
    pilih = input("\n\tsilakan pilih : ")
    if pilih == 1:
        print(nilai_mahasiswa())
    elif pilih == 2:
        print(pembayaran())
    elif pilih == 3:
        print(kalku())
        
    else:
        exit
    tanya()

def tanya():
    tanya =raw_input("\nKembali ke menu (y/t)? ")
    if tanya == "y":
        menu()
    elif tanya == "t":
        exit
    else:
        print ("\n\tSalah input...........!!!")
        tanya()



def user():
    
    username = raw_input("\nUsername : ")
    password = raw_input("\npassword : ")
    print("================================================")

    if username == "Yafa" and password == "311710379":
        menu()
    
    else:
        print ("maaf passwor atau username mu salah.........!!!")
        user()
user()

