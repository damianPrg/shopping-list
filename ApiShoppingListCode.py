from kivy.uix.gridlayout import GridLayout # Importowanie klasy GridLayout do tworzenia układu
from kivy.app import App # Importowanie klasy App, aby stworzyć główną aplikację
from kivy.uix.widget import Widget  # Importowanie Widget, podstawowego komponentu w Kivy
from kivy.uix.textinput import TextInput # Importowanie TextInput, komponentu umożliwiającego wprowadzanie tekstu
from kivy.uix.button import Button # Importowanie Button, komponentu przycisku
from kivy.uix.label import Label  # Importowanie Label, komponentu wyświetlającego tekst
from kivy.uix.image import Image # Importowanie Image, do obsługi obrazków
from kivy.graphics import Rectangle, Color # Importowanie ScrollView, do dodawania przewijania w aplikacji
import requests # Import requests do pobierania danych z API
from kivy.core.window import Window # Import klasy do zarządzania oknem aplikacji
from googletrans import Translator # Import biblioteki Google Translator do tłumaczenia






class MyApka(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # Wywołanie konstruktora klasy GridLayout
        self.lista = []
        Window.size = (1024, 768)
        self.pictures = r"D:\pythonprg\zakupy.jpg" # Ścieżka do tła obrazu
        self.cols = 1
        self.spacing = 10
        self.padding = 20

        # Rysowanie tła w aplikacji
        with self.canvas.before:
            self.bg_color = Color(1, 1, 1,1) # Ustawienie koloru tła
            self.bg_rect = Rectangle(source = self.pictures, size = (1024, 768), pos = (0,0))  #Dodanie obrazu jako tła

        # Tworzenie pola do wpisania nazwy produktu
        self.text_input = TextInput(hint_text = "Podaj nazwę produktu ", font_size = 30, size_hint_y = None, height = 50)
        self.add_widget(self.text_input)

        # Tworzenie układu dla listy produktów
        self.list_layout = GridLayout(cols = 1, spacing = 5, size_hint_y = 0.1, height = 50)
        self.add_widget(self.list_layout)

        # Tworzenie pola do wpisania nazwy pliku, w którym zapiszemy listę
        self.name_input = TextInput(hint_text = "Podaj nazwę pliku", font_size = 30, size_hint_y = None, height = 50)
        self.add_widget(self.name_input)

        # Tworzenie przycisku do zapisywania pliku
        button1 = Button(text = "Zapisz plik", size_hint_y = None, height = 50)
        button1.bind(on_press = self.button_save_file)
        self.add_widget(button1)

        # Tworzenie przycisku do dodawania produktów do listy
        button = Button(text = "Dodaj do listy", size_hint_y = None, height = 50)
        button.bind(on_press = self.add_to_list)
        self.add_widget(button)

        # Pole do wpisania kodu kreskowego
        self.barcode_input = TextInput(hint_text = "Wpisz kod kreskowy", font_size = 30, size_hint_y = None, height = 50)
        search_button = Button(text = "Szukaj", size_hint_y = None, height = 50)
        search_button.bind(on_press = self.product_info)
        self.result_label = Label(text = "Tutaj pojawią sie wyniki", font_size = 20, bold = True, color = (1, 0, 0, 1), size_hint_y = None )

        # Dodanie elementów do interfejsu
        self.add_widget(search_button)
        self.add_widget(self.result_label)
        self.add_widget(self.barcode_input)

        

    # Funkcja dodająca produkt do listy i wyświetlająca go w aplikacji
    def add_to_list(self, instance):
        tekst = self.text_input.text
        if tekst:
            self.lista.append(tekst)
            self.list_layout.add_widget(Label(
                text = tekst,
                font_size = 30,
                size_hint_y = None,
                height = 25 ))
                
            self.text_input.text = ""

            self.save_to_file()

    # Funkcja zapisująca listę do pliku
    def save_to_file(self):
        tekst = self.name_input.text
        if not tekst.endswith(".txt"):
            tekst += ".txt"
        try:
            with open(tekst, "w", encoding= "utf-8") as file:
                for item in self.lista:
                    file.write(item + "\n")
                print("Lista została zapisana do pliku")
        except:
            print("Błąd zapisu pliku")

    # Funkcja zapisująca listę do pliku na podstawie wprowadzonej nazwy pliku
    def button_save_file(self, instance):
        tekst = self.name_input.text
        if not tekst.endswith(".txt"):
            tekst += ".txt"

        try:
            with open(tekst, "w", encoding="utf-8") as file:
                for item in self.lista:
                    file.write(item + "\n")
            print("Zapisano w pliku")
        except:
            print("Błąd zapisu pliku")

    # Tłumaczenie składników produktu
    def translate_ingredients(self, ingredients_text, target_language = 'pl', src_language = 'auto'):
        translator = Translator()
        translated = translator.translate(ingredients_text, src= src_language, dest = target_language )
        return translated.text

    # Pobieranie informacji o produkcie na podstawie kodu kreskowego
    def product_info(self, instance):
        barcode = self.barcode_input.text.strip()
        if not barcode:
            self.result_label.text = "Podaj kod kreskowy!"
            return

        url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if "product" in data:
                product = data["product"]
                name = product.get("product_name", "Brak nazwy")
                ingredients = product.get("ingredients_text", "Brak informacji o składnikach")

                translated_ingredients1 = self.translate_ingredients(name)
                translated_ingredients = self.translate_ingredients(ingredients)
                self.result_label.text = f"Nazwa: {translated_ingredients1}\nSkładniki: {translated_ingredients}"
            else:
                self.result_label.text = "Produkt nie znaleziony."
        else:
            self.result_label.text = "Błąd pobierania danych."
        
        
        
class MyApp(App):
    def build(self):
        return MyApka()

    
if __name__ == "__main__":
    MyApp().run()
            

            



        
        
        

        
        

        

    

        

        
        
        
            
