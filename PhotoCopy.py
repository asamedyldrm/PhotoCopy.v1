import os
import shutil
from tkinter import *
from tkinter import filedialog

def copy_photos():
    # kaynak dosya yolu ve adı
    src_path = src_var.get()
    # kopya fotoğrafların kaydedileceği klasör yolu
    dst_path = dst_var.get()
    # isimleri içeren dosya yolu
    names_file = names_var.get()

    # isimleri oku
    with open(names_file) as f:
        names = f.read().splitlines()
    num_copies = len(names)
    # resmi kopyala
    for i in range(num_copies):
        # kopya fotoğrafın ismini oluştur
        dst_name = names[i] + ".jpg"
        # kopya fotoğrafın yolunu oluştur
        dst = os.path.join(dst_path, dst_name)
        # resmi kopyala
        shutil.copy(src_path, dst)

root = Tk()

root.title("PhotoCopy.v1 | Samet YILDIRIM")
root.geometry("500x275")
root.config(bg='#fff')

# kopyalanacak fotoğraf seçenekleri
src_var = StringVar()
src_button = Button(root, text="Kopyalanacak Fotoğrafı Seçin", bg='#7286D3', fg='#fff', command=lambda: src_var.set(filedialog.askopenfilename(title = "Kopyalanacak Fotoğrafı Seçin")))
src_button.pack(pady=10)

# kopyalanacak dosyaların kaydedileceği klasör seçenekleri
dst_var = StringVar()
dst_button = Button(root, text="Kopyalanacak Dosyaların Kaydedileceği Klasörü Seçin", bg='#7286D3', fg='#fff', command=lambda: dst_var.set(filedialog.askdirectory(title = "Kopyalanacak Dosyaların Kaydedileceği Klasörü Seçin")))
dst_button.pack(pady=10)

# isimleri içeren dosya seçenekleri
names_var = StringVar()
names_button = Button(root, text="İsimleri İçeren Dosyayı Seçin", bg='#7286D3', fg='#fff', command=lambda: names_var.set(filedialog.askopenfilename(title = "İsimleri İçeren Dosyayı Seçin")))
names_button.pack(pady=10)

copy_button = Button(root, text = "Fotoğrafları Kopyala", command = copy_photos, bg='#567189', fg='#fff')
copy_button.pack(pady=10)

lab = Label(root, text='Samet YILDIRIM | All rights reserved.', bg="#fff", fg="#000")
lab.pack(pady=40)

root.mainloop()

