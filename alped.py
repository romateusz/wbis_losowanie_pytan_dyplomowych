import customtkinter as ctk
from PIL import Image
import random


def losowanie_I_st(file_name):
    with open(file_name, "r") as f:
        questions = [line.strip() for line in f.readlines()]
    draw = sorted(random.sample(range(len(questions)), 2))
    return [(index, questions[index]) for index in draw]

def losowanie_ogólne_II_st(file_name):
    with open(file_name, "r") as f:
        questions = [line.strip() for line in f.readlines()]
    draw = random.sample(range(len(questions)), 1)[0]
    return (draw, questions[draw])

def losowanie_specjalizacyjne_II_st(file_name):
    with open(file_name, "r") as f:
        questions = [line.strip() for line in f.readlines()]
    draw = random.sample(range(len(questions)), 1)[0]
    return (draw, questions[draw])

def przejdz_do_ekranu_oczekiwania():
    hide_all_frames()
    waiting_frame.pack(fill="both", expand=True)
    root.after(1500, przejdz_do_ekranu_wyniku)

def przejdz_do_ekranu_wyniku():
    hide_all_frames()
    result_frame.pack(fill="both", expand=True)
    result_label.configure(
        text="\n\n".join([f"{index+1}. {question}" for index, question in wylosowane_pytania])
    )

def losuj_pytania_I_st(kierunek):
    global wylosowane_pytania
    wylosowane_pytania = losowanie_I_st(f"./st_I/{kierunek}.txt")
    przejdz_do_ekranu_oczekiwania()

def losuj_pytania_II_st(kierunek, specjalizacja):
    global wylosowane_pytania
    pytanie_ogólne = losowanie_ogólne_II_st(f"./st_II/og/{kierunek}.txt")
    pytanie_specjalizacyjne = losowanie_specjalizacyjne_II_st(f"./st_II/spec/{kierunek}/{specjalizacja}.txt")
    wylosowane_pytania = [pytanie_ogólne] + [pytanie_specjalizacyjne]
    # uwzględnienie dodatkowego przypadku (ten kierunek nie ma pytań specjalizacyjnych, trzeb sprawdzić, czy nie wylosowało się to samo pytanie)
    if kierunek == "Restoration and management of environment":
        print(wylosowane_pytania[0][0], wylosowane_pytania[1][0])
        if wylosowane_pytania[0][0] == wylosowane_pytania[1][0]:
            losuj_pytania_II_st(kierunek, kierunek)
        else:
            # posortuj pytania po indeksie
            wylosowane_pytania = sorted(wylosowane_pytania, key=lambda x: x[0])
    przejdz_do_ekranu_oczekiwania()

def przejdz_do_ekranu_stopnia(stopien):
    global current_stopien
    current_stopien = stopien
    hide_all_frames()
    if stopien == 1:
        ekran_I_stopnia.pack(fill="both", expand=True)
    elif stopien == 2:
        ekran_II_stopnia.pack(fill="both", expand=True)

def przejdz_do_wyboru_specjalizacji(kierunek, kierunek_file):
    global current_kierunek
    current_kierunek = kierunek
    hide_all_frames()
    ekran_wyboru_specjalizacji.pack(fill="both", expand=True)
    title_label_spec.configure(text=f"Wybierz specjalizację dla kierunku:\n„{current_kierunek}”", font=("Helvetica", 34, "bold"), text_color="black", wraplength=900)
    title_label_spec.pack(pady=(100, 25))
    # Usuwanie poprzednich przycisków specjalizacji
    for widget in spec_buttons_frame.winfo_children():
        widget.destroy()
    # Tworzenie przycisków dla aktualnych specjalizacji
    for specjalizacja_text in specjalizacje[kierunek_file]:
        button = ctk.CTkButton(
            spec_buttons_frame,
            text=specjalizacja_text,
            font=("Helvetica", 28, "bold"),
            corner_radius=20,
            fg_color="#006800",
            hover_color="#005700",
            text_color="white",
            command=lambda spec=specjalizacja_text: losuj_pytania_II_st(kierunek_file, spec),
            width=600,
            height=58
        )
        button.pack(pady=7)

def wróć_do_ekranu_głównego():
    hide_all_frames()
    welcome_frame.pack(fill="both", expand=True)

def wróć_do_ekranu_II_stopnia():
    hide_all_frames()
    ekran_II_stopnia.pack(fill="both", expand=True)

def hide_all_frames():
    """Funkcja ukrywająca wszystkie ekrany."""
    for frame in all_frames:
        frame.pack_forget()

def rysuj_logo(okno):
    orzelek_image = ctk.CTkImage(Image.open("./images/logo.png"), size=(110, 110))
    orzelek_label = ctk.CTkLabel(okno, image=orzelek_image, text="")
    orzelek_label.place(x=30, y=40)

    logo_image = ctk.CTkImage(Image.open("./images/wbis.png"), size=(300, 130))
    logo_label = ctk.CTkLabel(okno, image=logo_image, text="")
    logo_label.place(x=150, y=30)

# Tworzenie głównego okna
root = ctk.CTk()
root.title("Aplikacja do losowania pytań")
root.geometry("1200x1000")

# Listy kierunków i specjalizacji
kierunki_I_st = [
    ("Architektura krajobrazu", "Architektura_krajobrazu"),
    ("Budownictwo", "Budownictwo"),
    ("Inżynieria i gospodarka wodna", "Inzynieria_i_gospodarka_wodna"),
    ("Inżynieria środowiska", "Inzynieria_srodowiska"),
    ("Ochrona srodowiska", "Ochrona_srodowiska"),
]

kierunki_II_st = [
    ("Architektura krajobrazu", "Architektura krajobrazu"),
    ("Budownictwo", "Budownictwo"),
    ("Inżynieria i gospodarka wodna", "Inzynieria i gospodarka wodna"),
    ("Inżynieria środowiska", "Inzynieria srodowiska"),
    ("Ochrona środowiska", "Ochrona srodowiska"),
    ("Restoration and management of environment", "Restoration and management of environment"),
    ("Water Management and Water Use", "Water Management and Water Use"),
]

specjalizacje = {
    "Architektura krajobrazu": ["Projektowanie krajobrazu", "Sztuka ogrodu i krajobrazu", "Urządzanie i pielęgnowanie krajobrazu"],
    "Budownictwo": ["Geotechnika", "Konstrukcje budowlane", "Studia niestacjonarne"],
    "Inzynieria i gospodarka wodna": ["Gospodarka wodna", "Inżynieria wodna i melioracyjna"],
    "Inzynieria srodowiska": ["Ekoinzynieria", "Geoinzynieria srodowiskowa", "Inzynieria sanitarna", "Inzynieria wodna", "Studia niestacjonarne"],
    "Ochrona srodowiska": ["Systemy ochrony srodowiska", "Technologie w ochronie srodowiska"],
    "Restoration and management of environment": ["Restoration and management of environment"],
    "Water Management and Water Use": ["Water Management and Water Use"],
}

# Ekran powitalny
welcome_frame = ctk.CTkFrame(root, fg_color="white")
welcome_frame.pack(fill="both", expand=True)

rysuj_logo(root)

title_label = ctk.CTkLabel(welcome_frame, text="Aplikacja Losująca Pytania na Egzamin Dyplomowy", font=("Helvetica", 34, "bold"), text_color="black")
title_label.pack(pady=(200, 40))

button_I_stopnia = ctk.CTkButton(
    welcome_frame,
    text="I Stopień",
    corner_radius=20,
    font=("Helvetica", 28, "bold"),
    fg_color="#006800",
    hover_color="#005700",
    text_color="white",
    command=lambda: przejdz_do_ekranu_stopnia(1),
    width=400,
    height=75
)
button_I_stopnia.pack(pady=10)

button_II_stopnia = ctk.CTkButton(
    welcome_frame,
    text="II Stopień",
    corner_radius=20,
    font=("Helvetica", 28, "bold"),
    fg_color="#006800",
    hover_color="#005700",
    text_color="white",
    command=lambda: przejdz_do_ekranu_stopnia(2),
    width=400,
    height=75
)
button_II_stopnia.pack(pady=10)

# Ekran I stopnia
ekran_I_stopnia = ctk.CTkFrame(root, fg_color="white")

rysuj_logo(ekran_I_stopnia)

back_button_I = ctk.CTkButton(
    ekran_I_stopnia,
    text="Powrót",
    font=("Helvetica", 24, "bold"),
    corner_radius=20,
    fg_color="#006800",
    hover_color="#005700",
    text_color="white",
    command=wróć_do_ekranu_głównego,
    width=140,
    height=40
)
back_button_I.pack(side="top", anchor="ne", padx=30, pady=30)

title_label_I = ctk.CTkLabel(ekran_I_stopnia, text="Wybierz kierunek studiów I stopnia", font=("Helvetica", 34, "bold"), text_color="black")
title_label_I.pack(pady=(100, 30))

for kierunek_text, kierunek_file in kierunki_I_st:
    button = ctk.CTkButton(
        ekran_I_stopnia,
        text=kierunek_text,
        font=("Helvetica", 26, "bold"),
        corner_radius=20,
        fg_color="#006800",
        hover_color="#005700",
        text_color="white",
        command=lambda file=kierunek_file: losuj_pytania_I_st(file),
        width=500,
        height=60
    )
    button.pack(pady=7)

# Ekran II stopnia
ekran_II_stopnia = ctk.CTkFrame(root, fg_color="white")

rysuj_logo(ekran_II_stopnia)

back_button_II = ctk.CTkButton(
    ekran_II_stopnia,
    text="Powrót",
    font=("Helvetica", 26, "bold"),
    corner_radius=20,
    fg_color="#006800",
    hover_color="#005700",
    text_color="white",
    command=wróć_do_ekranu_głównego,
    width=140,
    height=40
)
back_button_II.pack(side="top", anchor="ne", padx=30, pady=30)

title_label_II = ctk.CTkLabel(ekran_II_stopnia, text="Wybierz kierunek studiów II stopnia", font=("Helvetica", 34, "bold"), text_color="black")
title_label_II.pack(pady=(100,30))

for kierunek_text, kierunek_file in kierunki_II_st:
    button = ctk.CTkButton(
        ekran_II_stopnia,
        text=kierunek_text,
        font=("Helvetica", 22, "bold"),
        corner_radius=20,
        fg_color="#006800",
        hover_color="#005700",
        text_color="white",
        command=lambda kierunek=kierunek_text, path=kierunek_file: przejdz_do_wyboru_specjalizacji(kierunek, path),
        width=530,
        height=43
    )
    button.pack(pady=6)

# Ekran wyboru specjalizacji
ekran_wyboru_specjalizacji = ctk.CTkFrame(root, fg_color="white")

rysuj_logo(root)

back_button_spec = ctk.CTkButton(
    ekran_wyboru_specjalizacji,
    text="Powrót",
    font=("Helvetica", 26, "bold"),
    corner_radius=20,
    fg_color="#006800",
    hover_color="#005700",
    text_color="white",
    command=wróć_do_ekranu_II_stopnia,
    width=140,
    height=40
)
back_button_spec.pack(side="top", anchor="ne", padx=30, pady=30)

title_label_spec = ctk.CTkLabel(ekran_wyboru_specjalizacji, text="", font=("Helvetica", 25, "bold"))
title_label_spec.pack(pady=20)

spec_buttons_frame = ctk.CTkFrame(
    ekran_wyboru_specjalizacji,
    fg_color="transparent",
)
spec_buttons_frame.pack()

# Ekran oczekiwania
waiting_frame = ctk.CTkFrame(root, fg_color="white")
waiting_label = ctk.CTkLabel(waiting_frame, text="Proszę czekać, trwa losowanie pytań...", font=("Helvetica", 30, "bold"), text_color="black")
waiting_label.pack(expand=True)

# Ekran wyników
result_frame = ctk.CTkFrame(root, fg_color="white")
rysuj_logo(root)
back_button_result = ctk.CTkButton(
    result_frame,
    text="Powrót",
    font=("Helvetica", 26, "bold"),
    corner_radius=20,
    fg_color="#006800",
    hover_color="#005700",
    text_color="white",
    command=wróć_do_ekranu_głównego,
    width=140,
    height=40
)
back_button_result.pack(side="top", anchor="ne", padx=30, pady=30)

result_label = ctk.CTkLabel(
    result_frame,
    font=("Helvetica", 26),
    text_color="black",
    justify="left",
    wraplength=1000,
)
result_label.pack(padx=100, pady=100, anchor="w")

# Lista wszystkich ekranów do ukrywania
all_frames = [welcome_frame, ekran_I_stopnia, ekran_II_stopnia, ekran_wyboru_specjalizacji, waiting_frame, result_frame]

footer_frame = ctk.CTkFrame(
    root,
    fg_color="#1E3859",  # Kolor tła stopki
    height=50  # Wysokość stopki
)
footer_frame.pack(side="bottom", fill="x")

# Etykieta w stopce
footer_label = ctk.CTkLabel(
    footer_frame,
    text="Wydział Budownictwa i Inżynierii Środowiska SGGW - 2025\nStworzył: Mateusz Roman",   
    font=("Helvetica", 14),
    text_color="white"
)
footer_label.pack(pady=10)

# Uruchomienie aplikacji
root.mainloop()