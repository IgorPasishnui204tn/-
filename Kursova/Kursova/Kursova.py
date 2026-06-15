import tkinter as tk
from tkinter import messagebox


class BigBCDNumber:

    def __init__(self, number="0"):
        if not number.isdigit():
            raise ValueError("Число повинно містити тільки цифри")

        self.digits = [int(d) for d in reversed(number)]
        self.end_marker = 0xF

    def __del__(self):
        self.digits.clear()

    def copy(self):
        new_obj = BigBCDNumber("0")
        new_obj.digits = self.digits.copy()
        return new_obj

    def add_digit(self, digit):
        if 0 <= digit <= 9:
            self.digits.insert(0, digit)
        else:
            raise ValueError("Цифра повинна бути від 0 до 9")

    def remove_digit(self, index):
        if 0 <= index < len(self.digits):
            del self.digits[index]
        else:
            raise IndexError("Невірний індекс")

    def change_digit(self, index, value):
        if not (0 <= value <= 9):
            raise ValueError("Цифра повинна бути від 0 до 9")

        if 0 <= index < len(self.digits):
            self.digits[index] = value
        else:
            raise IndexError("Невірний індекс")

    def get_number(self):
        return ''.join(map(str, reversed(self.digits)))

    def get_bcd(self):

        bcd_list = []

        for digit in self.digits:
            bcd_list.append(format(digit, '04b'))

        bcd_list.append("1111")

        return " ".join(bcd_list)


number_obj = None


def create_number():
    global number_obj

    try:
        number_obj = BigBCDNumber(entry_number.get())

        result_text.delete(1.0, tk.END)
        result_text.insert(
            tk.END,
            f"Число: {number_obj.get_number()}\n"
            f"BCD: {number_obj.get_bcd()}"
        )

    except Exception as e:
        messagebox.showerror("Помилка", str(e))


def copy_number():

    global number_obj

    if number_obj is None:
        return

    copy_obj = number_obj.copy()

    result_text.insert(
        tk.END,
        f"\n\nКопія створена:\n{copy_obj.get_number()}"
    )


def add_digit():

    global number_obj

    try:

        digit = int(entry_digit.get())

        number_obj.add_digit(digit)

        update_output()

    except Exception as e:
        messagebox.showerror("Помилка", str(e))


def change_digit():

    global number_obj

    try:

        index = int(entry_index.get())
        digit = int(entry_digit.get())

        number_obj.change_digit(index, digit)

        update_output()

    except Exception as e:
        messagebox.showerror("Помилка", str(e))


def remove_digit():

    global number_obj

    try:

        index = int(entry_index.get())

        number_obj.remove_digit(index)

        update_output()

    except Exception as e:
        messagebox.showerror("Помилка", str(e))


def update_output():

    result_text.delete(1.0, tk.END)

    result_text.insert(
        tk.END,
        f"Число: {number_obj.get_number()}\n"
        f"BCD: {number_obj.get_bcd()}"
    )


root = tk.Tk()
root.title("Курсова Робота")
root.geometry("700x500")

tk.Label(root, text="Введіть число").pack()

entry_number = tk.Entry(root, width=40)
entry_number.pack()

tk.Button(
    root,
    text="Створити об'єкт",
    command=create_number
).pack(pady=5)

tk.Label(root, text="Індекс").pack()

entry_index = tk.Entry(root)
entry_index.pack()

tk.Label(root, text="Цифра").pack()

entry_digit = tk.Entry(root)
entry_digit.pack()

tk.Button(
    root,
    text="Створити копію",
    command=copy_number
).pack(pady=5)

tk.Button(
    root,
    text="Додати цифру",
    command=add_digit
).pack(pady=5)

tk.Button(
    root,
    text="Змінити цифру",
    command=change_digit
).pack(pady=5)

tk.Button(
    root,
    text="Видалити цифру",
    command=remove_digit
).pack(pady=5)

result_text = tk.Text(root, height=12, width=70)
result_text.pack(pady=10)

root.mainloop()