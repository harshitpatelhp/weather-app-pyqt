from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt
import sys
import requests

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather app")
        self.setGeometry(70, 70, 350, 400)
        self.InitUI()

    def InitUI(self):
        central_widget= QWidget()
        self.setCentralWidget(central_widget)
        self.city_label= QLabel("Enter City Name:", self)
        self.city_field= QLineEdit(self)
        self.submit= QPushButton("Get Weather", self)
        self.temperature= QLabel("", self)
        self.weather_label= QLabel("", self)

        self.city_label.setStyleSheet("font-size: 30px;"
                                      "font-family: Helvetica;")
        self.city_field.setStyleSheet("padding: 5px;"
                                      "border-radius: 3px;"
                                      "font-size: 35px;"
                                      "border: 2px solid gray")
        self.submit.setStyleSheet("border-radius: 2px;"
                                  "font-family: Helvetica;"
                                  "font-weight: bold;"
                                  "font-size: 25px;"
                                  "border: 1px solid gray;")
        self.temperature.setStyleSheet("font-family: Helvetica;"
                                       "font-size: 40px;")
        self.weather_label.setStyleSheet("font-family: Helvetica;"
                                         "font-size: 40px;")
        vbox= QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_field)
        vbox.addWidget(self.submit)
        vbox.addWidget(self.temperature)
        vbox.addWidget(self.weather_label)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_field.setAlignment(Qt.AlignCenter)
        self.temperature.setAlignment(Qt.AlignCenter)
        self.weather_label.setAlignment(Qt.AlignCenter)

        central_widget.setLayout(vbox)

        self.submit.clicked.connect(self.display_weather)

    def display_weather(self):
        api_key= "YOUR_API_KEY_HERE"
        city= self.city_field.text()
        url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            response= requests.get(url)
            data= response.json()
            self.temperature.setStyleSheet("font-size: 40px;")
            self.temperature.setText(f'{data["main"]["temp"]- 273.15:.2f} ℃')
            self.weather_label.setText(data["weather"][0]["description"])

        except:
            self.temperature.setStyleSheet("font-size: 30px;")
            self.temperature.setText("Something Wrong Occured")
            self.weather_label.setText("")

def main():
    app= QApplication(sys.argv)
    window= MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
