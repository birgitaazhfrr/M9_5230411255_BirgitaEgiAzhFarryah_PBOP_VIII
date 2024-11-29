import tkinter as tk
from tkinter import ttk, messagebox

class ReservasiHotel:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Reservasi Hotel Jiro")
        self.root.geometry("900x700")
        
        
        self.harga_kamar = {
            "single": 1000000,
            "double": 1700000,
            "suite": 3000000,
            "deluxe": 4000000
        }
        
        self.nomor_kamar_counter = {
            "single": 101,
            "double": 201,
            "suite": 301,
            "deluxe": 401
        }

        # Membuat widget
        self.buat_widget()

    def buat_widget(self):
        # Frame untuk judul
        frame_judul = tk.Frame(self.root, bg="#A9A9A9")  # Abu-abu gelap
        frame_judul.pack(pady=10)
        label_judul = tk.Label(
            frame_judul, text="Aplikasi Reservasi Hotel Jiro", 
            font=("Arial", 18, "bold"), fg="#FFFFFF", bg="#A9A9A9"  # Putih text on dark gray
        )
        label_judul.pack()

        # Frame untuk input
        frame_input = tk.Frame(self.root, bd=2, relief="solid", bg="#D3D3D3")  # Abu-abu terang
        frame_input.pack(pady=10, padx=20, fill="x")

        # Nama pelanggan
        tk.Label(frame_input, text="Nama Lengkap:", anchor="w", bg="#D3D3D3", fg="#000000").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.nama_entry = tk.Entry(frame_input, width=30, bg="#FFFFFF", fg="#000000")
        self.nama_entry.grid(row=0, column=1, padx=10, pady=5)

        # Email pelanggan
        tk.Label(frame_input, text="Email:", anchor="w", bg="#D3D3D3", fg="#000000").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.email_entry = tk.Entry(frame_input, width=30, bg="#FFFFFF", fg="#000000")
        self.email_entry.grid(row=1, column=1, padx=10, pady=5)

        # Nomor HP pelanggan
        tk.Label(frame_input, text="Nomor HP:", anchor="w", bg="#D3D3D3", fg="#000000").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.phone_entry = tk.Entry(frame_input, width=30, bg="#FFFFFF", fg="#000000")
        self.phone_entry.grid(row=2, column=1, padx=10, pady=5)

        # Pilihan tipe kamar
        tk.Label(frame_input, text="Pilih Tipe Kamar:", anchor="w", bg="#D3D3D3", fg="#000000").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.room_var = tk.StringVar(value="")
        room_options = list(self.harga_kamar.keys())
        self.room_menu = ttk.Combobox(frame_input, values=room_options, textvariable=self.room_var, state="readonly", width=27)
        self.room_menu.grid(row=3, column=1, padx=10, pady=5)

        # Tanggal check-in
        tk.Label(frame_input, text="Check-in (YYYY-MM-DD):", anchor="w", bg="#D3D3D3", fg="#000000").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.check_in_entry = tk.Entry(frame_input, width=30, bg="#FFFFFF", fg="#000000")
        self.check_in_entry.grid(row=4, column=1, padx=10, pady=5)

        # Tanggal check-out
        tk.Label(frame_input, text="Check-out (YYYY-MM-DD):", anchor="w", bg="#D3D3D3", fg="#000000").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.check_out_entry = tk.Entry(frame_input, width=30, bg="#FFFFFF", fg="#000000")
        self.check_out_entry.grid(row=5, column=1, padx=10, pady=5)

        # Pilihan metode pembayaran
        tk.Label(frame_input, text="Metode Pembayaran:", anchor="w", bg="#D3D3D3", fg="#000000").grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.payment_var = tk.StringVar(value="")
        payment_options = ["Cash", "Credit Card", "E-Wallet", "Bank Transfer"]
        self.payment_menu = ttk.Combobox(frame_input, values=payment_options, textvariable=self.payment_var, state="readonly", width=27)
        self.payment_menu.grid(row=6, column=1, padx=10, pady=5)

        # Tombol tambah pesanan
        tk.Button(self.root, text="Tambah Reservasi", command=self.tambah_reservasi, bg="#A9A9A9", fg="#000000", font=("Arial", 12)).pack(pady=10)

        # Frame untuk tabel daftar reservasi
        frame_tabel = tk.Frame(self.root, bg="#D3D3D3")  # Abu-abu terang untuk tabel
        frame_tabel.pack(padx=20, pady=10, fill="both", expand=True)

        # Scrollbar untuk tabel
        scrollbar_y = ttk.Scrollbar(frame_tabel, orient="vertical")
        scrollbar_x = ttk.Scrollbar(frame_tabel, orient="horizontal")

        # Tabel daftar reservasi
        self.tabel_pesanan = ttk.Treeview(
            frame_tabel,
            columns=("Nama", "Email", "Phone", "Tipe Kamar", "Nomor Kamar", "Harga", "Check-in", "Check-out", "Payment"),
            show="headings",
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )
        scrollbar_y.config(command=self.tabel_pesanan.yview)
        scrollbar_x.config(command=self.tabel_pesanan.xview)
        scrollbar_y.pack(side="right", fill="y")
        scrollbar_x.pack(side="bottom", fill="x")
        self.tabel_pesanan.pack(fill="both", expand=True)

        for col in self.tabel_pesanan["columns"]:
            self.tabel_pesanan.heading(col, text=col)
            self.tabel_pesanan.column(col, anchor="center", width=120)

        # Tombol clear table
        tk.Button(self.root, text="Hapus Tabel", command=self.hapus_tabel, bg="#A9A9A9", fg="#000000", font=("Arial", 12)).pack(pady=10)

    def tambah_reservasi(self):
        nama = self.nama_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        room_type = self.room_var.get().strip()
        check_in = self.check_in_entry.get().strip()
        check_out = self.check_out_entry.get().strip()
        payment_method = self.payment_var.get().strip()

        if not all([nama, email, phone, room_type, check_in, check_out, payment_method]):
            messagebox.showwarning("Peringatan", "Harap isi semua data!")
            return

        harga = self.harga_kamar.get(room_type, 0)
        room_number = self.nomor_kamar_counter[room_type]
        self.nomor_kamar_counter[room_type] += 1

        self.tabel_pesanan.insert("", "end", values=(nama, email, phone, room_type, room_number, f"Rp {harga:,}", check_in, check_out, payment_method))
        messagebox.showinfo("Sukses", f"Reservasi atas nama {nama} berhasil ditambahkan!\nNomor Kamar: {room_number}")

        # Clear the form fields after adding a reservation
        self.clear_form()

    def hapus_tabel(self):
        for item in self.tabel_pesanan.get_children():
            self.tabel_pesanan.delete(item)

    def clear_form(self):
        self.nama_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.room_menu.set("")
        self.check_in_entry.delete(0, tk.END)
        self.check_out_entry.delete(0, tk.END)
        self.payment_menu.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = ReservasiHotel(root)
    root.mainloop()
