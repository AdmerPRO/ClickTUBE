import tkinter as tk
from tkinter import messagebox
import random


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
editor_cost = 20
graphic_cost = 50
stały_widz_count = 0
stały_widz_multiplier = 1
stały_widz_unlocked = False
shop_window = None  # Dodaj zmienną shop_window jako globalną

# Funkcje do obsługi przycisków

def click():
    global sub_count
    sub_count += sub_per_click * stały_widz_multiplier + editor_count * 1 + graphic_count * 2
    if sub_count >= 1000 and not stały_widz_unlocked:
        unlock_stały_widz()
    update_display()

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
    tk.Label(shop_window, text=f"Ilość Przyjaciela: {editor_count}").pack()

    # Montażysta
    editor_button = tk.Button(shop_window, text=f"Kup Montażystę (Koszt: {editor_cost})", command=buy_editor)
    editor_button.pack()
    tk.Label(shop_window, text=f"Ilość Montażystów: {editor_count}").pack()

    # Grafik
    graphic_button = tk.Button(shop_window, text=f"Kup Grafika (Koszt: {graphic_cost})", command=buy_graphic)
    graphic_button.pack()
    tk.Label(shop_window, text=f"Ilość Grafików: {graphic_count}").pack()

    if stały_widz_unlocked:
        tk.Button(shop_window, text="Kup Stałego Widza (Koszt: 1000)", command=buy_stały_widz).pack()

    tk.Button(shop_window, text="Zamknij", command=close_shop).pack()

def confirm_exit():
    result = messagebox.askquestion("Wyjście", "Czy na pewno chcesz opuścić grę?")
    if result == "yes":
        root.destroy()

# Funkcje do zakupu przedmiotów w sklepie
def buy_friend():
    global sub_count, sub_per_click, friend_cost, editor_count
    cost = friend_cost
    if sub_count >= cost and editor_count < 100:
        sub_count -= cost
        sub_per_click += 1
        friend_cost += 10  # Zwiększ koszt przyjaciela
        editor_count += 1
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
    stały_widz_unlocked = True
    update_display()
    messagebox.showinfo("Brawo", "Odblokowałeś/aś Super Widza")

def buy_stały_widz():
    global sub_count, stały_widz_multiplier
    cost = 1000
    if sub_count >= cost:
        sub_count -= cost
        stały_widz_multiplier = random.randint(2, 10)
        update_display()
        close_shop()
    else:
        messagebox.showerror("Błąd", "Nie masz wystarczająco Subskrybcji")

# Funkcja do aktualizacji wyświetlania
def update_display():
    sub_label.config(text=f"Suby: {sub_count}")
    stały_widz_label.config(text=f"Stały Widz (x{stały_widz_multiplier})" if stały_widz_unlocked else "")

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

# Etykieta dla Subów
sub_label = tk.Label(root, text=f"Suby: {sub_count}", font=("Helvetica", 12))
sub_label.pack(side="top")

# Uruchomienie aplikacji
root.mainloop()
