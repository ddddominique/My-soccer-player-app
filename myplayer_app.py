import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QCheckBox, QLineEdit

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class PlayerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.player_label = QLabel("Enter the player name: ", self)
        self.player_input = QLineEdit(self)
        self.get_player_button = QPushButton("Get the information", self)
        self.club_label = QLabel(self)
        self.player_height = QLabel(self)
        self.player_age = QLabel(self)
        self.country = QLabel(self)
        self.value = QLabel(self)
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Soccer Player App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.player_label)
        vbox.addWidget(self.player_input)
        vbox.addWidget(self.get_player_button)
        vbox.addWidget(self.club_label)
        vbox.addWidget(self.player_height)
        vbox.addWidget(self.player_age)
        vbox.addWidget(self.country)
        vbox.addWidget(self.value)

        self.setLayout(vbox)

        self.player_label.setAlignment(Qt.AlignCenter)
        self.player_input.setAlignment(Qt.AlignCenter)
        self.club_label.setAlignment(Qt.AlignCenter)
        self.player_height.setAlignment(Qt.AlignCenter)
        self.player_age.setAlignment(Qt.AlignCenter)
        self.country.setAlignment(Qt.AlignCenter)
        self.value.setAlignment(Qt.AlignCenter)

        self.player_label.setObjectName("player_label")
        self.player_input.setObjectName("player_input")
        self.get_player_button.setObjectName("get_player_button")
        self.club_label.setObjectName("club_label")
        self.player_height.setObjectName("player_height")
        self.player_age.setObjectName("player_age")
        self.country.setObjectName("country")
        self.value.setObjectName("value")

        self.setStyleSheet("""
            QLabel, QPushButton{
                    font-family: calibri;}
            QLabel#player_label{
                    font-size: 40px;       }
            QLineEdit#player_input{
                    font-size: 40px;       }
            QPushButton#get_player_button{
                    font-size: 30px;
                    font-weight: bold;}
            QLabel#club_label, #player_height, #player_age{
                    font-size: 30px;}
            QLabel#country, #value{
                    font-size: 30px;}
      
        """)

        self.get_player_button.clicked.connect(self.real_func)


    

    def real_func(self):
        name = self.player_input.text().strip()
        def get_player_info(name):
            url = "https://free-api-live-football-data.p.rapidapi.com/football-players-search"

            querystring = {"search":name}

            headers = {
                "x-rapidapi-key": "7dad5d88ecmshc2b935db82882dcp1e42a8jsn4f193e556e99",
                "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers, params=querystring)
            

            if response.status_code == 200:
                player_data = response.json()
                return player_data
            else:
                print(f"did not get it, we get {response.status_code}")

        def get_player_details(id):
            url = "https://free-api-live-football-data.p.rapidapi.com/football-get-player-detail"
            
            querystring = {"playerid":id}

            headers = {
            "x-rapidapi-key": "7dad5d88ecmshc2b935db82882dcp1e42a8jsn4f193e556e99",
            "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
            }

            response_details = requests.get(url, headers=headers, params=querystring)

            if response_details.status_code == 200:
                player_details = response_details.json()
                return player_details
            


        player_info = get_player_info(name)



        if player_info:
            first_player = player_info["response"]["suggestions"][0]
            player_id = first_player["id"]
            more_info = get_player_details(player_id)
            actual_details = more_info["response"]["detail"]
            self.club_label.setText(f"Club: {first_player["teamName"]}")
            self.player_height.setText(f"Height: {actual_details[0]["value"]["fallback"]}")
            self.player_age.setText(f"Age: {actual_details[2]["value"]["numberValue"]}")
            self.country.setText(f"Country: {actual_details[4]["value"]["fallback"]}")
            self.value.setText(f"Market Value: {actual_details[5]["value"]["fallback"]}")







    




        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    player_app = PlayerApp()
    player_app.show()
    sys.exit(app.exec_())