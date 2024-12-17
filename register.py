from tkinter import *
from tkinter import messagebox
import ast
import os

# Membuat folder 'data' jika belum ada
if not os.path.exists('data'):
    os.makedirs('data')

# Fungsi untuk memuat data user
def load_users():
    try:
        with open('data/datasheet.txt', 'r') as file:
            return ast.literal_eval(file.read())
    except FileNotFoundError:
        return {}

# Fungsi untuk menyimpan data user
def save_users(users):
    with open('data/datasheet.txt', 'w') as file:
        file.write(str(users))

# Fungsi untuk Sign In
def signin():
    username = user_entry.get()
    password = pass_entry.get()
    users = load_users()

    if username in users and users[username] == password:
        messagebox.showinfo("Sign In", f"Selamat datang, {username}!")
        window.destroy()  # Tutup window setelah berhasil login
    else:
        messagebox.showerror("Sign In", "Username atau password salah!")

# Fungsi untuk membuka jendela Sign Up
def open_signup_window():
    signup_window = Toplevel(window)
    signup_window.title("Sign Up")
    signup_window.geometry('400x400')
    signup_window.configure(bg='#fff')
    signup_window.resizable(False, False)

    def signup():
        username = new_user_entry.get()
        password = new_pass_entry.get()
        confirm_password = confirm_pass_entry.get()

        # Validasi input
        if not username or not password or not confirm_password:
            messagebox.showerror('Sign Up', 'Semua kolom harus diisi!')
            return

        if len(password) < 6:
            messagebox.showerror('Sign Up', 'Password minimal 6 karakter!')
            return

        if password != confirm_password:
            messagebox.showerror('Sign Up', 'Password tidak cocok!')
            return

        users = load_users()
        if username in users:
            messagebox.showerror('Sign Up', 'Username sudah ada!')
            return

        # Simpan user baru
        users[username] = password
        save_users(users)
        messagebox.showinfo('Sign Up', f'Akun "{username}" berhasil dibuat!')
        signup_window.destroy()

    # Layout Sign Up
    Label(signup_window, text="Sign Up", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 20, "bold")).pack(pady=20)

    Label(signup_window, text="Username", bg="white").pack()
    new_user_entry = Entry(signup_window, width=30)
    new_user_entry.pack(pady=5)

    Label(signup_window, text="Password", bg="white").pack()
    new_pass_entry = Entry(signup_window, width=30, show="*")
    new_pass_entry.pack(pady=5)

    Label(signup_window, text="Confirm Password", bg="white").pack()
    confirm_pass_entry = Entry(signup_window, width=30, show="*")
    confirm_pass_entry.pack(pady=5)

    Button(signup_window, text="Sign Up", bg="#57a1f8", fg="white", width=20, command=signup).pack(pady=20)

def toggle_password(entry, toggle_btn):
    if entry.cget('show') == '':
        entry.config(show='*')
        toggle_btn.config(text='Show')
    else:
        entry.config(show='')
        toggle_btn.config(text='Hide')
    
# Window Utama untuk Sign In
window = Tk()
window.title("Sign In")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False, False)

# Gambar
img = PhotoImage(file='assets/login.png')  # Pastikan file gambar ada di folder 'assets'
Label(window, image=img, border=0, bg='white').place(x=50, y=90)

# Frame utama
frame = Frame(window, width=350, height=390, bg='#fff')
frame.place(x=480, y=50)

heading = Label(frame, text='Sign In', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# Username Entry
Label(frame, text="Username", bg="white", font=("Microsoft Yahei UI Light", 11)).place(x=30, y=50)
user_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user_entry.place(x=30, y=80)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# Toggle Password Button
toggle_btn1 = Button(frame, text='Show', border=0, bg='white', cursor='hand2', command=lambda: toggle_password(pass_entry, toggle_btn1))
toggle_btn1.place(x=260, y=150)

# Password Entry
Label(frame, text="Password", bg="white", font=("Microsoft Yahei UI Light", 11)).place(x=30, y=120)
pass_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11), show="*")
pass_entry.place(x=30, y=150)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# Sign In Button
Button(frame, width=39, pady=7, text='Sign In', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=220)

# Sign Up Option
Label(frame, text="Belum punya akun?", bg="white", fg="black", font=("Microsoft Yahei UI Light", 9)).place(x=90, y=270)
Button(frame, width=6, text="Sign Up", border=0, bg='white', fg='#57a1f8', cursor='hand2', command=open_signup_window).place(x=200, y=270)

# Main Loop
window.mainloop()
