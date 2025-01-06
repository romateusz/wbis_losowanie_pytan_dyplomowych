import customtkinter as ctk
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

def losuj_pytania(kierunek):
    global wylosowane_pytania
    wylosowane_pytania = losowanie_I_st(f"./st_I/{kierunek}.txt")
    przejdz_do_ekranu_oczekiwania()

def losuj_pytania_II_st(kierunek, specjalizacja):
    global wylosowane_pytania
    pytanie_ogólne = losowanie_ogólne_II_st(f"./st_II/og/{kierunek}.txt")
    pytanie_specjalizacyjne = losowanie_specjalizacyjne_II_st(f"./st_II/spec/{kierunek}/{specjalizacja}.txt")
    wylosowane_pytania = [pytanie_ogólne] + [pytanie_specjalizacyjne]
    przejdz_do_ekranu_oczekiwania()

def przejdz_do_ekranu_stopnia(stopien):
    global current_stopien
    current_stopien = stopien
    hide_all_frames()
    if stopien == 1:
        ekran_I_stopnia.pack(fill="both", expand=True)
    elif stopien == 2:
        ekran_II_stopnia.pack(fill="both", expand=True)

def przejdz_do_wyboru_specjalizacji(kierunek):
    global current_kierunek
    current_kierunek = kierunek
    hide_all_frames()
    ekran_wyboru_specjalizacji.pack(fill="both", expand=True)
    title_label_spec.configure(text=f"Wybierz specjalizację ({kierunek}):")
    # Usuwanie poprzednich przycisków specjalizacji
    for widget in spec_buttons_frame.winfo_children():
        widget.destroy()
    # Tworzenie przycisków dla aktualnych specjalizacji
    for specjalizacja_text in specjalizacje[kierunek]:
        button = ctk.CTkButton(
            spec_buttons_frame,
            text=specjalizacja_text,
            font=("Helvetica", 13),
            corner_radius=20,
            fg_color="#006800",
            hover_color="#005700",
            text_color="white",
            command=lambda spec=specjalizacja_text: losuj_pytania_II_st(kierunek, spec),
            width=280
        )
        button.pack(pady=10)

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

# Tworzenie głównego okna
root = ctk.CTk()
root.title("Aplikacja do losowania pytań")
root.geometry("800x600")

# Listy kierunków i specjalizacji
kierunki_I_st = [
    ("Architektura krajobrazu", "Architektura_krajobrazu"),
    ("Budownictwo", "Budownictwo"),
    ("Inżynieria i gospodarka wodna", "Inzynieria_i_gospodarka_wodna"),
    ("Inżynieria środowiska", "Inzynieria_srodowiska"),
    ("Ochrona środowiska", "Ochrona_srodowiska"),
]

kierunki_II_st = [
    "Architektura krajobrazu",
    "Budownictwo",
    "Inzynieria i gospodarka wodna",
    "Inzynieria srodowiska",
    "Ochrona Srodowiska",
    "Restoration and management of environment",
    "Water Management and Water Use",
]

specjalizacje = {
    "Architektura krajobrazu": ["Projektowanie krajobrazu", "Sztuka ogrodu i krajobrazu", "Urządzanie i pielęgnowanie krajobrazu"],
    "Budownictwo": ["Geotechnika", "Konstrukcje budowlane", "Studia niestacjonarne"],
    "Inzynieria i gospodarka wodna": ["Gospodarka wodna", "Inżynieria wodna i melioracyjna"],
    "Inzynieria srodowiska": ["Ekoinzynieria", "Geoinzynieria srodowiskowa", "Inzynieria sanitarna", "Inzynieria wodna", "Studia niestacjonarne"],
    "Ochrona Srodowiska": ["Systemy ochrony srodowiska", "Technologie w ochronie srodowiska"],
    "Restoration and management of environment": ["Restoration and management of environment"],
    "Water Management and Water Use": ["Water Management and Water Use"],
}

# Ekran powitalny
welcome_frame = ctk.CTkFrame(root)
welcome_frame.pack(fill="both", expand=True)

title_label = ctk.CTkLabel(welcome_frame, text="Aplikacja do Losowania Pytań na Egzamin Dyplomowy", font=("Helvetica", 18, "bold"))
title_label.pack(pady=(110, 20))

desc_label = ctk.CTkLabel(welcome_frame, text="Wybierz stopień:", font=("Helvetica", 16))
desc_label.pack(pady=10)

button_I_stopnia = ctk.CTkButton(
    welcome_frame,
    text="I Stopień",
    corner_radius=20,
    fg_color="#006800",
    hover_color="#005700",
    text_color="white",
    command=lambda: przejdz_do_ekranu_stopnia(1),
    width=280
)
button_I_stopnia.pack(pady=5)

button_II_stopnia = ctk.CTkButton(
    welcome_frame,
    text="II Stopień",
    corner_radius=20,
    fg_color="#006800",
    hover_color="#005700",
    text_color="white",
    command=lambda: przejdz_do_ekranu_stopnia(2),
    width=280
)
button_II_stopnia.pack(pady=10)

# Ekran I stopnia
ekran_I_stopnia = ctk.CTkFrame(root)

back_button_I = ctk.CTkButton(
    ekran_I_stopnia,
    text="Powrót",
    font=("Helvetica", 13, "bold"),
    corner_radius=20,
    fg_color="#006800",
    hover_color="#005700",
    text_color="white",
    command=wróć_do_ekranu_głównego,
    width=100
)
back_button_I.pack(side="top", anchor="ne", padx=30, pady=30)

title_label_I = ctk.CTkLabel(ekran_I_stopnia, text="Wybierz kierunek studiów I Stopnia", font=("Helvetica", 18, "bold"))
title_label_I.pack(pady=20)

for kierunek_text, kierunek_file in kierunki_I_st:
    button = ctk.CTkButton(
        ekran_I_stopnia,
        text=kierunek_text,
        font=("Helvetica", 13),
        corner_radius=20,
        fg_color="#006800",
        hover_color="#005700",
        text_color="white",
        command=lambda file=kierunek_file: losuj_pytania(file),
        width=280
    )
    button.pack(pady=10)

# Ekran II stopnia
ekran_II_stopnia = ctk.CTkFrame(root)
back_button_II = ctk.CTkButton(
    ekran_II_stopnia,
    text="Powrót",
    font=("Helvetica", 13, "bold"),
    corner_radius=20,
    fg_color="#006800",
    hover_color="#005700",
    text_color="white",
    command=wróć_do_ekranu_głównego,
    width=100
)
back_button_II.pack(side="top", anchor="ne", padx=30, pady=30)

title_label_II = ctk.CTkLabel(ekran_II_stopnia, text="Wybierz kierunek studiów II Stopnia", font=("Helvetica", 18, "bold"))
title_label_II.pack(pady=20)

for kierunek_text in kierunki_II_st:
    button = ctk.CTkButton(
        ekran_II_stopnia,
        text=kierunek_text,
        font=("Helvetica", 13),
        corner_radius=20,
        fg_color="#006800",
        hover_color="#005700",
        text_color="white",
        command=lambda kierunek=kierunek_text: przejdz_do_wyboru_specjalizacji(kierunek),
        width=280
    )
    button.pack(pady=10)

# Ekran wyboru specjalizacji
ekran_wyboru_specjalizacji = ctk.CTkFrame(root)

back_button_spec = ctk.CTkButton(
    ekran_wyboru_specjalizacji,
    text="Powrót",
    font=("Helvetica", 13, "bold"),
    corner_radius=20,
    fg_color="#006800",
    hover_color="#005700",
    text_color="white",
    command=wróć_do_ekranu_II_stopnia,
    width=100
)
back_button_spec.pack(side="top", anchor="ne", padx=30, pady=30)

title_label_spec = ctk.CTkLabel(ekran_wyboru_specjalizacji, text="", font=("Helvetica", 18, "bold"))
title_label_spec.pack(pady=20)

spec_buttons_frame = ctk.CTkFrame(
    ekran_wyboru_specjalizacji,
    fg_color="transparent",
)
spec_buttons_frame.pack()

# Ekran oczekiwania
waiting_frame = ctk.CTkFrame(root)
waiting_label = ctk.CTkLabel(waiting_frame, text="Proszę czekać, trwa losowanie pytań.", font=("Helvetica", 16))
waiting_label.pack(expand=True)

# Ekran wyników
result_frame = ctk.CTkFrame(root)
back_button_result = ctk.CTkButton(
    result_frame,
    text="Powrót",
    font=("Helvetica", 13, "bold"),
    corner_radius=20,
    fg_color="#006800",
    hover_color="#005700",
    text_color="white",
    command=wróć_do_ekranu_głównego,
    width=100
)
back_button_result.pack(side="top", anchor="ne", padx=30, pady=30)

result_label = ctk.CTkLabel(result_frame, font=("Helvetica", 16), wraplength=500)
result_label.pack(pady=20)

# Lista wszystkich ekranów do ukrywania
all_frames = [welcome_frame, ekran_I_stopnia, ekran_II_stopnia, ekran_wyboru_specjalizacji, waiting_frame, result_frame]

footer_label = ctk.CTkLabel(
    root,
    text="Wydział Budownictwa i Inżynierii Środowiska SGGW - 2025\nStworzył: Mateusz Roman",
    font=("Helvetica", 12),
    text_color="white"
)
footer_label.pack(side="bottom", pady=10)

# Uruchomienie aplikacji
root.mainloop()