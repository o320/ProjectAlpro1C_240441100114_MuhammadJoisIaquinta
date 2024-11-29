def input_bilangan(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)  
        else:
            print("Input tidak valid! Harap masukkan bilangan bulat.")

def tambah_pemasukan(saldo, transaksi, jumlah, keterangan):
    saldo += jumlah
    transaksi.append({"jenis": "Pemasukan", "jumlah": jumlah, "keterangan": keterangan, "terkait_pengeluaran": False})
    print(f"Pemasukan sebesar {jumlah} berhasil ditambahkan dengan keterangan: {keterangan}")
    return saldo, transaksi

def tambah_pengeluaran(saldo, transaksi, jumlah, keterangan):
    if jumlah > saldo:
        print("Saldo tidak cukup untuk pengeluaran ini. Pengeluaran dibatalkan.")
        return saldo, transaksi
    else:
        saldo -= jumlah
        transaksi.append({"jenis": "Pengeluaran", "jumlah": jumlah, "keterangan": keterangan, "terkait_pengeluaran": True})
        print(f"Pengeluaran sebesar {jumlah} berhasil dilakukan dengan keterangan: {keterangan}")
        return saldo, transaksi

def hapus_transaksi(saldo, transaksi, id):
    while id < 0 or id >= len(transaksi): 
        print("Indeks transaksi tidak valid. Masukkan indeks yang benar.")
        id = input_bilangan("Masukkan indeks transaksi yang ingin dihapus: ")

    transaksi_terhapus = transaksi[id]

    if transaksi_terhapus["jenis"] == "Pemasukan":
        total_pengeluaran_terkait = saldo
        for t in transaksi:
            if t["jenis"] == "Pengeluaran" and t["keterangan"] == transaksi_terhapus["keterangan"]:
                total_pengeluaran_terkait += t["jumlah"]

        if total_pengeluaran_terkait >= transaksi_terhapus["jumlah"]:
            print(f"Pemasukan sebesar {transaksi_terhapus['jumlah']} tidak dapat dihapus karena pengeluaran terkait lebih besar atau sama dengan pemasukan.")
        else:
            saldo -= transaksi_terhapus["jumlah"]
            print(f"Pemasukan sebesar {transaksi_terhapus['jumlah']} dengan keterangan \"{transaksi_terhapus['keterangan']}\" berhasil dihapus.")
            transaksi.pop(id)
    else:
        saldo += transaksi_terhapus["jumlah"]
        print(f"Pengeluaran sebesar {transaksi_terhapus['jumlah']} dengan keterangan \"{transaksi_terhapus['keterangan']}\" berhasil dihapus.")
        transaksi.pop(id)

    return saldo, transaksi

def update_transaksi(saldo, transaksi, id, jumlah_baru, keterangan_baru):
    while id < 0 or id >= len(transaksi):  
        print("Indeks transaksi tidak valid. Masukkan indeks yang benar.")
        id = input_bilangan("Masukkan indeks transaksi yang ingin diperbarui: ")

    transaksi_yang_diperbarui = transaksi[id]
    jumlah_lama = transaksi_yang_diperbarui["jumlah"]
    jenis = transaksi_yang_diperbarui["jenis"]

    if jenis == "Pemasukan":
        saldo = saldo - jumlah_lama + jumlah_baru
    else:
        saldo = saldo + jumlah_lama - jumlah_baru

    transaksi_yang_diperbarui["jumlah"] = jumlah_baru
    transaksi_yang_diperbarui["keterangan"] = keterangan_baru
    print(f"Transaksi {jenis} berhasil diperbarui ke jumlah {jumlah_baru} dengan keterangan \"{keterangan_baru}\".")
    return saldo, transaksi

def lihat_saldo(saldo):
    print(f"Saldo saat ini: {saldo}")

def lihat_transaksi(transaksi):
    if len(transaksi) == 0:
        print("Tidak ada transaksi.")
    else:
        print("Daftar Transaksi:")
        for i, t in enumerate(transaksi):
            print(f"{i}. {t['jenis']}: {t['jumlah']} ({t['keterangan']})")

def main():
    saldo = 0
    transaksi = []

    while True:
        print("\nMenu Keuangan:")
        print("1. Tambah Pemasukan")
        print("2. Tambah Pengeluaran")
        print("3. Lihat Saldo")
        print("4. Lihat Transaksi")
        print("5. Hapus Transaksi")
        print("6. Update Transaksi")
        print("7. Keluar")

        pilihan = input("Pilih menu (1-7): ")
        if pilihan == '1':
            jumlah = input_bilangan("Masukkan jumlah pemasukan: ")
            keterangan = input("Masukkan keterangan pemasukan: ")
            saldo, transaksi = tambah_pemasukan(saldo, transaksi, jumlah, keterangan)

        elif pilihan == '2':
            jumlah = input_bilangan("Masukkan jumlah pengeluaran: ")
            if jumlah > saldo:
                print("Saldo tidak cukup untuk pengeluaran ini. Pengeluaran dibatalkan.")
                continue
            keterangan = input("Masukkan keterangan pengeluaran: ")
            saldo, transaksi = tambah_pengeluaran(saldo, transaksi, jumlah, keterangan)

        elif pilihan == '3':
            lihat_saldo(saldo)

        elif pilihan == '4':
            lihat_transaksi(transaksi)

        elif pilihan == '5':
            lihat_transaksi(transaksi)
            if len(transaksi) == 0:
                continue
            indeks = input_bilangan("Masukkan indeks transaksi yang ingin dihapus: ")
            saldo, transaksi = hapus_transaksi(saldo, transaksi, indeks)

        elif pilihan == '6':
            lihat_transaksi(transaksi)
            if len(transaksi) == 0:
                continue  
            indeks = input_bilangan("Masukkan indeks transaksi yang ingin diperbarui: ")
            while indeks < 0 or indeks >= len(transaksi):
                print("Indeks transaksi tidak valid. Masukkan indeks yang benar.")
                indeks = input_bilangan("Masukkan indeks transaksi yang ingin diperbarui: ")
                
            jumlah_baru = input_bilangan("Masukkan jumlah baru: ")
            keterangan_baru = input("Masukkan keterangan baru: ")
            saldo, transaksi = update_transaksi(saldo, transaksi, indeks, jumlah_baru, keterangan_baru)

        elif pilihan == '7':
            print("Terima kasih telah menggunakan aplikasi manajemen keuangan!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

main()
