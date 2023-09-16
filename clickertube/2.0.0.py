import tkinter as tk
from tkinter import messagebox
import random
import json
import os


# Inicjalizacja okna
root = tk.Tk()
root.title("ClikerTube")
root.geometry("400x300")

# Początkowe wartości
sub_count = 0
sub_per_click = 1
editor_count = 0
graphic_count = 0
friend_cost = 10
friend_count = 0
editor_cost = 20
graphic_cost = 50
stały_widz_count = 0
stały_widz_multiplier = 1
stały_widz2_multiplier = 1
stały_widz_unlocked = False
stały_widz_unlocked2 = False
shop_window = None  # Dodaj zmienną shop_window jako globalną

def click():
    global sub_count
    sub_count += sub_per_click * stały_widz_multiplier * stały_widz2_multiplier + friend_count * 1 + editor_count * 2 + graphic_count * 3
    if sub_count >= 1000 and not stały_widz_unlocked:
        unlock_stały_widz()

    if sub_count >= 5000 and not stały_widz_unlocked2:
        unlock_stały_widz2()
    update_display()
def start_gry():
    messagebox.showinfo("ClickTube", "Witaj w ClickTUBE!")
start_gry()

#savedata

def savedata():
    global sub_count
    global sub_per_click
    global editor_count
    global editor_cost
    global graphic_count
    global graphic_cost
    global friend_count
    global friend_cost
    #Zapisywanie 1
    data1 = {
        "sc": sub_count,
        "spc": sub_per_click,
        "ec": editor_count,
        "eco": editor_cost,
        "gc": graphic_count,
        "gco": graphic_cost,
        "fc": friend_count,
        "fco": friend_cost
    }
    data1write = json.dumps(data1)
    with open('data1.json', 'w') as plik:
        plik.write(data1write)

    #Zapisywanie 2
    global stały_widz_count
    global stały_widz_multiplier
    global stały_widz_unlocked
    global stały_widz2_multiplier
    global stały_widz_unlocked2

    data2 = {
        "swc": stały_widz_count,
        "swu": stały_widz_unlocked,
        "swm": stały_widz_multiplier,
        "swm2": stały_widz2_multiplier,
        "swu2": stały_widz_unlocked2
    }
    data2write = json.dumps(data2)
    with open('data2.json', 'w') as plik:
        plik.write(data2write)

def loaddata():
    global sub_count
    global sub_per_click
    global editor_count
    global editor_cost
    global graphic_count
    global graphic_cost
    global friend_count
    global friend_cost
    #Wczytywanie
    with open('data1.json', 'r') as plik:
        data1 = json.load(plik)
    sub_count = data1["sc"]
    sub_per_click = data1["spc"]
    editor_count = data1["ec"]
    editor_cost = data1["eco"]
    graphic_count = data1["gc"]
    graphic_cost = data1["gco"]
    friend_count = data1["fc"]
    friend_cost = data1["fco"]
    #Wczytywanie 2
    global stały_widz_count
    global stały_widz_multiplier
    global stały_widz_unlocked
    global stały_widz2_multiplier
    global stały_widz_unlocked2
    with open('data2.json', 'r') as plik:
        data2 = json.load(plik)
    stały_widz_count = data2["swc"]
    stały_widz_unlocked = data2["swu"]
    stały_widz_multiplier = data2["swm"]
    stały_widz_unlocked2 = data2["swu2"]
    stały_widz2_multiplier = data2["swm2"]
# Funkcje do obsługi przycisków
loaddata()
def open_shop():
    global shop_window  # Zadeklaruj shop_window jako globalną
    shop_window = tk.Toplevel(root)
    shop_window.title("Sklep")

    # Etykiety i przyciski w sklepie
    tk.Label(shop_window, text="Sklep").pack()
    tk.Label(shop_window, text=f"Suby: {sub_count}").pack()

    # Przyjaciel
    friend_button = tk.Button(shop_window, text=f"Kup Przyjaciela (Koszt: {friend_cost})", command=buy_friend)
    friend_button.pack()
    tk.Label(shop_window, text=f"Ilość Przyjaciela: {friend_count}").pack()

    # Montażysta
    editor_button = tk.Button(shop_window, text=f"Kup Montażystę (Koszt: {editor_cost})", command=buy_editor)
    editor_button.pack()
    tk.Label(shop_window, text=f"Ilość Montażystów: {editor_count}").pack()

    # Grafik
    graphic_button = tk.Button(shop_window, text=f"Kup Grafika (Koszt: {graphic_cost})", command=buy_graphic)
    graphic_button.pack()
    tk.Label(shop_window, text=f"Ilość Grafików: {graphic_count}").pack()

    tk.Button(shop_window, text="Zamknij", command=close_shop).pack()

def confirm_exit():
    result = messagebox.askquestion("Wyjście", "Czy na pewno chcesz opuścić grę?")
    if result == "yes":
        root.destroy()
        savedata()

# Funkcje do zakupu przedmiotów w sklepie
def buy_friend():
    global sub_count, sub_per_click, friend_cost, friend_count
    cost = friend_cost
    if sub_count >= cost and friend_count < 100:
        sub_count -= cost
        sub_per_click += 1
        friend_cost += 10  # Zwiększ koszt przyjaciela
        friend_count += 1
        update_display()
        close_shop()
    else:
        messagebox.showerror("Błąd", "Nie masz wystarczająco Subskrybcji lub osiągnięto maksymalny poziom Przyjaciela")
        shop_window.destroy()

def buy_editor():
    global sub_count, editor_count, editor_cost
    cost = editor_cost
    if sub_count >= cost:
        sub_count -= cost
        editor_count += 1
        editor_cost += 10  # Zwiększ koszt montażysty
        update_display()
        close_shop()
    else:
        messagebox.showerror("Błąd", "Nie masz wystarczająco Subskrybcji")
        shop_window.destroy()

def buy_graphic():
    global sub_count, graphic_count, graphic_cost
    cost = graphic_cost
    if sub_count >= cost:
        sub_count -= cost
        graphic_count += 1
        graphic_cost += 20  # Zwiększ koszt grafika
        update_display()
        close_shop()
    else:
        messagebox.showerror("Błąd", "Nie masz wystarczająco Subskrybcji")
        shop_window.destroy()

def unlock_stały_widz():
    global stały_widz_unlocked
    global stały_widz_multiplier
    stały_widz_unlocked = True
    stały_widz_multiplier = random.randint(2, 10)
    update_display()
    messagebox.showinfo("Brawo", "Odblokowałeś/aś Stałego Widza")


def unlock_stały_widz2():
    global stały_widz_unlocked2
    global stały_widz2_multiplier
    stały_widz_unlocked2 = True
    stały_widz2_multiplier = random.randint(2, 10)
    update_display()
    messagebox.showinfo("Brawo", "Odblokowałeś/aś Stałego Widza")

# Funkcja do aktualizacji wyświetlania
def update_display():
    sub_label.config(text=f"Suby: {sub_count}")
    stały_widz_label.config(text=f"Stały Widz (x{stały_widz_multiplier})" if stały_widz_unlocked else "")
    stały_widz2_label.config(text=f"Stały Widz Dwa (x{stały_widz2_multiplier})" if stały_widz_unlocked2 else "")

def close_shop():
    shop_window.destroy()

# Przycisk SUB
sub_button = tk.Button(root, text="SUB", command=click, bg="red", width=10, height=2)
sub_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Przycisk Wyjdź
exit_button = tk.Button(root, text="Wyjdź", command=confirm_exit, bg="gray", width=10, height=2)
exit_button.pack(side="bottom")

# Przycisk Sklep
shop_button = tk.Button(root, text="Sklep", command=open_shop, bg="blue", width=10, height=2)
shop_button.pack(side="top")

# Etykieta dla Stałego Widza
stały_widz_label = tk.Label(root, text="", font=("Helvetica", 12))
stały_widz_label.pack(side="bottom")

stały_widz2_label = tk.Label(root, text="", font=("Helvetica", 12))
stały_widz2_label.pack(side="bottom")

# Etykieta dla Subów
sub_label = tk.Label(root, text=f"Suby: {sub_count}", font=("Helvetica", 12))
sub_label.pack(side="top")

# Uruchomienie aplikacji
root.mainloop()
