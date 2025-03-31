from kivy.uix.gridlayout import GridLayout # Importowanie klasy GridLayout do tworzenia układu
from kivy.app import App # Importowanie klasy App, aby stworzyć główną aplikację
from kivy.uix.widget import Widget  # Importowanie Widget, podstawowego komponentu w Kivy
from kivy.uix.textinput import TextInput # Importowanie TextInput, komponentu umożliwiającego wprowadzanie tekstu
from kivy.uix.button import Button # Importowanie Button, komponentu przycisku
from kivy.uix.label import Label  # Importowanie Label, komponentu wyświetlającego tekst
from kivy.uix.image import Image # Importowanie Image, do obsługi obrazków
from kivy.graphics import Rectangle, Color # Importowanie ScrollView, do dodawania przewijania w aplikacji



class MyApka(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # Wywołanie konstruktora klasy GridLayout
        self.lista = []
        self.pictures = r"D:\pythonprg\zakupy.jpg" # Ścieżka do tła obrazu
        self.cols = 1
        self.spacing = 10
        self.padding = 20

        # Rysowanie tła w aplikacji
        with self.canvas.before:
            self.bg_color = Color(1, 1, 1,1) # Ustawienie koloru tła
            self.bg_rect = Rectangle(source = self.pictures, size = (800, 600), pos = (0,0))  #Dodanie obrazu jako tła

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
            

class MyApp(App):
    def build(self):
        return MyApka()

    
if __name__ == "__main__":
    MyApp().run()
        
        
        

        

        
        
        

    

                

    
           






    
        




    

        



