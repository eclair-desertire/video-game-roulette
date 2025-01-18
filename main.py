import customtkinter as ctk
import random

# Инициализация customtkinter
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class GameRouletteApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Настройки окна
        self.title("Game Roulette")
        self.geometry("600x400")

        # Заголовок
        self.label_title = ctk.CTkLabel(self, text="Game Roulette", font=("Arial", 24))
        self.label_title.pack(pady=10)

        # Фильтры
        self.genre_label = ctk.CTkLabel(self, text="Select Genre:")
        self.genre_label.pack(pady=5)
        self.genre_combobox = ctk.CTkComboBox(self, values=["Any", "RPG", "Shooter", "Strategy", "Adventure"])
        self.genre_combobox.set("Any")
        self.genre_combobox.pack(pady=5)

        self.platform_label = ctk.CTkLabel(self, text="Select Platform:")
        self.platform_label.pack(pady=5)
        self.platform_combobox = ctk.CTkComboBox(self, values=["Any", "PC", "Xbox", "PlayStation", "Nintendo"])
        self.platform_combobox.set("Any")
        self.platform_combobox.pack(pady=5)

        # Кнопка запуска рулетки
        self.spin_button = ctk.CTkButton(self, text="Spin the Roulette", command=self.spin_roulette)
        self.spin_button.pack(pady=20)

        # Поле для отображения выбранной игры
        self.result_label = ctk.CTkLabel(self, text="No game selected yet", font=("Arial", 16))
        self.result_label.pack(pady=10)

        # База игр (тестовые данные)
        self.games = [
            {"title": "The Witcher 3", "genre": "RPG", "platform": "PC"},
            {"title": "Halo Infinite", "genre": "Shooter", "platform": "Xbox"},
            {"title": "Super Mario Odyssey", "genre": "Adventure", "platform": "Nintendo"},
            {"title": "Civilization VI", "genre": "Strategy", "platform": "PC"},
        ]

    def spin_roulette(self):
        selected_genre = self.genre_combobox.get()
        selected_platform = self.platform_combobox.get()

        # Фильтрация игр по выбранным параметрам
        filtered_games = [
            game for game in self.games
            if (selected_genre == "Any" or game["genre"] == selected_genre) and
               (selected_platform == "Any" or game["platform"] == selected_platform)
        ]

        # Выбор случайной игры
        if filtered_games:
            selected_game = random.choice(filtered_games)
            self.result_label.configure(text=f"{selected_game['title']}\n{selected_game['genre']} - {selected_game['platform']}")
        else:
            self.result_label.configure(text="No games match the filters")

# Запуск приложения
if __name__ == "__main__":
    app = GameRouletteApp()
    app.mainloop()
