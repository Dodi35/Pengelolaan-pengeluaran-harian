expenses = []

def show_menu():
    print("\n=== MENU ===")
    print("1. Tambah Pengeluaran")
    print("2. Lihat Pengeluaran")
    print("3. Hitung Total")
    print("4. Keluar")


def add_expense():
    name = input("Nama pengeluaran: ")
    
    try:
        amount = int(input("Jumlah: "))
    except ValueError:
        print("Jumlah harus angka!")
        return
    
    expenses.append({
        "name": name,
        "amount": amount
    })
    print("Pengeluaran berhasil ditambahkan!")


def show_expenses():
    if not expenses:
        print("Belum ada data.")
        return
    
    print("\nDaftar Pengeluaran:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - Rp{expense['amount']}")


def calculate_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total pengeluaran: Rp{total}")


def main():
    while True:
        show_menu()
        choice = input("Pilih menu: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()