import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

def exchange():
    code = tcombobox.get()
    b_code = b_combobox.get()
    if code and b_code:
        try:
            response = requests.get(f"https://open.er-api.com/v6/latest/{b_code}")
            response.raise_for_status()
            data = response.json()
            if code in data ['rates']:
                exchange_rate = data['rates'][code]
                t_name = cur[code]
                b_name = cur[b_code]
                mb.showinfo("Курс обмена", f"Курс:{exchange_rate:.3f} {t_name} за 1 {b_name}")
            else:
                mb.showerror("Ошибка!", f"Валюта {code} не найдена.")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}")
    else:
        mb.showwarning("Внимание!", "Введите код валюты!")


def update_t_label(event):
    code = tcombobox.get()
    name = cur[code]
    t_label.config(text=name)


def update_b_label(event):
    code = b_combobox.get()
    name = cur[code]
    b_label.config( text=name )

cur = {
    'RUB': 'Российский рубль',
    'EUR': 'Евро',
    'GBP': 'Британский фунт стерлингов',
    'JPY': 'Японская йена',
    'CNY': 'Китайский юань',
    'KZT': 'Казахский тенге',
    'UZS': 'Узбекский сум',
    'CHF': 'Швейцарский франк',
    'AED': 'Дирхам ОаЭ',
    'CAD': 'Канадский доллар',
    'USD': 'Американский доллар'
}
window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x300")

Label(text="Базовая валюта").pack(padx=10, pady=10)
b_combobox = ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(padx=10, pady=10)
b_combobox.bind("<<ComboboxSelected>>", update_b_label)
b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

Label(text="Целевая валютa").pack(padx=10, pady=10)

tcombobox = ttk.Combobox(values=list(cur.keys()))
tcombobox.pack(padx=10, pady=10)
tcombobox.bind("<<ComboboxSelected>>", update_t_label)
t_label = ttk.Label()
t_label.pack(padx=10, pady=10)


# entry = Entry()
# entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()






# result = requests.get("https://open.er-api.com/v6/latest/USD")
# data = json.loads(result.text)
# p = pprint.PrettyPrinter(indent=4)
# p.pprint(data)

