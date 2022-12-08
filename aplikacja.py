from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from algorytm_wegierski import metoda_wegierska

class  AlgorytmWegierski(App):
    
    def build(self):
        self.title = 'Algorytm Węgierski - minimalizacja kosztów'
        self.MainWindow = GridLayout()
        self.MainWindow.cols = 1
        self.MainWindow.size_hint = (1, 1)
        self.MainWindow.pos_hint = {"center_x": 0.5, "center_y":0.5}

        self.MainWindow.padding=(5,0)
        self.BoxN=BoxLayout(orientation='horizontal',height=50)
        self.BoxN.size_hint_max=(None,60)
        self.BoxN.padding=(0,5)

        self.pytanie = Label(
                        halign="center",
                        text= "Podaj rozmiar macierzy (2-10)",
                        font_size= 18,
                        color= '#E0E0E0',
                        size_hint= (1,1),
                        )
        self.BoxN.add_widget(self.pytanie)

        self.rozmiar = TextInput(
                    multiline= False,
                    padding_y= (5,5),
                    size_hint= (1,1),
                    halign="center",
                    input_filter='int',
                    height=50
                    )
        self.BoxN.add_widget(self.rozmiar)

        self.button_zatwierdz = Button(
                      text= "ZATWIERDŹ",
                      size_hint= (1,1),
                      bold= True,
                      background_color ='#00CCFF',
                      height=50
                      )
        self.button_zatwierdz.bind(on_press=self.podajN)
        self.BoxN.add_widget(self.button_zatwierdz)
        self.MainWindow.add_widget(self.BoxN)

        self.result = Label(
                        text= "Wynik",
                        text_size = (760,None),
                        font_size= 18,
                        bold= True,
                        color= '#FF8000',
                        size_hint= (0.6,0.6),
                        valign = 'middle'
                        )
        
        return self.MainWindow

    def oblicz(self, instance):
        self.result.text=""
        if self.rozmiar.text:
            if int(self.rozmiar.text)>0 and int(self.rozmiar.text)<11 :
                n=int(self.rozmiar.text)
            else:
                n=1
        else:
            n=1
        for i in range(n):
            for j in range(n):
                self.tab[i][j].background_color="#FFFFFF"
        self.macierz=[[0]*n for i in range(n)]
        for i in range(n):
            for j in range(n):
                if self.tab[i][j].text.isdigit():
                    if int(self.tab[i][j].text)>0:
                        self.macierz[i][j]=int(self.tab[i][j].text)
                    else:
                        self.macierz[i][j]=(-1)*int(self.tab[i][j].text)
        
        macierz_wynikowa,wynik=metoda_wegierska(self.macierz)
        for (w,k) in wynik:
            self.result.text +="Wykonwcy  "+ str(w+1) +"  przypisuje zadanie  "+ str(k+1) +"                     "
        if n==1:
            self.result.text="Wynik"
        for (w,k) in wynik:
            self.tab[w][k].background_color="#00CCFF"


    def podajN(self, instance):
        self.BoxN.remove_widget(self.button_zatwierdz)
        self.BoxN.remove_widget(self.rozmiar)
        self.N = Label(
                        text= "",
                        font_size= 18,
                        bold= True,
                        color= '#FF8000'
                        )

        if self.rozmiar.text:
            if int(self.rozmiar.text)>0 and int(self.rozmiar.text)<11:
                n=int(self.rozmiar.text)
            else:
                n=1
        else:
            n=1
        if 1<n<11:
            self.N.text+="N = "+str(n)
        else:
            self.N.text+="Nieprawidłowy rozmiar"
        self.BoxN.add_widget(self.N)

        self.Matrix = GridLayout()
        self.Matrix.padding=(0,5)
        self.Matrix.cols =n
        self.tab=[[0]*n for i in range(n)]
        for i in range(n):
            for j in range(n):
                self.tab[i][j] = TextInput(
                    halign="center",
                    size_hint=(1,1),
                    input_filter='int'
                    )
                self.Matrix.add_widget(self.tab[i][j])
        self.MainWindow.add_widget(self.Matrix)

        self.button_opt = Button(
                      text= "OPTYMALIZUJ",
                      height= 40,
                      bold= True,
                      background_color ='#00CCFF',
                      size_hint= (0.25,0.25)
                      )
        self.button_opt.bind(on_press=self.oblicz)
        self.MainWindow.add_widget(self.button_opt)
        self.MainWindow.add_widget(self.result)       
        
# uruchominie aplikacji
if __name__ == "__main__":
    AlgorytmWegierski().run()