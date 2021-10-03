import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QGridLayout, QHBoxLayout
from PyQt5 import QtGui, QtCore, Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import *



app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Energy Calculator")
window.setWindowIcon(QtGui.QIcon("fishy.ico"))
window.setWindowFlag(Qt.WindowStaysOnTopHint)

window.setFixedWidth(300)
window.setFixedHeight(400)
window.move(1000, 200)
window.setStyleSheet("background: #161219;")

grid = QGridLayout()
hbox = QHBoxLayout
vertical = QVBoxLayout()

total_round = 1


def clicker(para, num, total):
    tot = int(total)
    eround1 = int(num)
    used = int(num)
    gained = int(num)
    destroyed = int(num)
    print(para)
    #row 1
    if para == plus_button1.text() + str(1):
        if tot >= 0 and tot != 0:
            tot -= 1
            used += 1
            energy_used.setText(str(used))
            energy.setText(str(tot))

    elif para == minus_button1.text() + str(1):
        if used != 0 and used > 0:
            used -= 1
            tot += 1
            energy_used.setText(str(used))
            energy.setText(str(tot))
        #row 2
    elif para == plus_button2.text() + str(2) and tot < 10:
        gained += 1
        tot += 1
        energy_gained.setText(str(gained))
        energy.setText(str(tot))
    elif para == minus_button2.text() + str(2) and tot > 0:
        if used != 0:
            gained -= 1
            tot -= 1
            energy_gained.setText(str(gained))
            energy.setText(str(tot))
        #row 3
    elif para == plus_button3.text() + str(3):
        if tot >= 0 and tot != 0:
            destroyed += 1
            tot -= 1
            energy_destroyed.setText(str(destroyed))
            energy.setText(str(tot))
    elif para == minus_button3.text() + str(3):
        if destroyed != 0 and used > 0:
            destroyed -= 1
            tot += 1
            energy_destroyed.setText(str(destroyed))
            energy.setText(str(tot))
    elif para == endturn.text() and tot <= 10:
        if tot == 9:
            tot += 1
            energy.setText(str(tot))
        if tot != 10:
            tot += 2
            energy.setText(str(tot))
        if eround1 >= 9:
            eround.setStyleSheet(
                "margin-top: 0px;" +
                "font-family: 'Fredoka One', cursive;" +
                "color: 'red';" +
                "font-size: 20px;"
            )
            eround.setText("Round " + str(eround1))
        eround1 += 1
        eround.setText("Round " + str(eround1))

        # reset
        used -= used
        gained -= gained
        destroyed -= destroyed
        energy_used.setText(str(used))
        energy_gained.setText(str(gained))
        energy_destroyed.setText(str(destroyed))

        #reset button
    elif para == reset_button.text() and tot <= 10:
        print("clicker")
        tot -= tot - 3
        eround1 -= eround1 - 1
        used -= used
        gained -= gained
        destroyed -= destroyed

        energy.setText(str(tot))
        eround.setText("Round " + str(eround1))
        energy_used.setText(str(used))
        energy_gained.setText(str(gained))
        energy_destroyed.setText(str(destroyed))



def label(text):
    energy_text = QLabel(text)
    energy_text.setAlignment(QtCore.Qt.AlignCenter)
    energy_text.setStyleSheet(
        "font-family: 'Fredoka One', cursive;" +
        "color: 'white';" +
        "font-size: 15px"
    )
    return energy_text


#Rounds
eround = QLabel("Round " + str(total_round))
eround.setAlignment(QtCore.Qt.AlignCenter)
eround.setStyleSheet(
    "margin-top: 0px;" +
    "font-family: 'Fredoka One', cursive;" +
    "color: 'white';" +
    "font-size: 20px;"
)



# energy tracker
energy = QLabel("3")
energy.setAlignment(QtCore.Qt.AlignCenter)
energy.setStyleSheet(
    "font-family: 'Fredoka One', cursive;" +
    "color: 'white';" +
    "font-size: 30px;"
)


#Row 1
minus_button1 = QPushButton("-")
minus_button1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
minus_button1.setStyleSheet(
    "*{color: 'white';" +
    "font-size: 15px;" +
    "padding: 5px 3px;" +
    "margin: 5px;" +
    "border: 4px solid '#8e6f6f';" +
    "border-radius: 10px;}" +
    "*:hover{background: '#923838';}"

)
minus_button1.clicked.connect(lambda x: clicker(minus_button1.text() + str(1), energy_used.text(), energy.text()))

#energy used
energy_used = QLabel("0")
energy_used.setAlignment(QtCore.Qt.AlignCenter)
energy_used.setStyleSheet(
    "font-family: 'Fredoka One', cursive;" +
    "color: 'white';" +
    "font-size: 15px"
)

plus_button1 = QPushButton("+")
plus_button1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
plus_button1.setStyleSheet(
    "*{color: 'white';" +
    "font-size: 15px;" +
    "padding: 5px 3px;" +
    "margin: 5px;" +
    "border: 4px solid '#8e6f6f';" +
    "border-radius: 10px;}" +
    "*:hover{background: '#008da2';}"

)
plus_button1.clicked.connect(lambda x: clicker(plus_button1.text() + str(1), energy_used.text(),energy.text()))

#Row 2
minus_button2 = QPushButton("-")
minus_button2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
minus_button2.setStyleSheet(
    "*{color: 'white';" +
    "font-size: 15px;" +
    "padding: 5px 3px;" +
    "margin: 5px;" +
    "border: 4px solid '#8e6f6f';" +
    "border-radius: 10px;}" +
    "*:hover{background: '#923838';}"

)
minus_button2.clicked.connect(lambda x: clicker(minus_button2.text() + str(2), energy_gained.text(),energy.text()))

#Energy gained
energy_gained = QLabel("0")
energy_gained.setAlignment(QtCore.Qt.AlignCenter)
energy_gained.setStyleSheet(
    "font-family: 'Fredoka One', cursive;" +
    "color: 'white';" +
    "font-size: 15px"
)

plus_button2 = QPushButton("+")
plus_button2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
plus_button2.setStyleSheet(
    "*{color: 'white';" +
    "font-size: 15px;" +
    "padding: 5px 3px;" +
    "margin: 5px;" +
    "border: 4px solid '#8e6f6f';" +
    "border-radius: 10px;}" +
    "*:hover{background: '#008da2';}"

)
plus_button2.clicked.connect(lambda x: clicker(plus_button2.text() + str(2), energy_gained.text(), energy.text()))

#Row 3
minus_button3 = QPushButton("-")
minus_button3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
minus_button3.setStyleSheet(
    "*{color: 'white';" +
    "font-size: 15px;" +
    "padding: 5px 3px;" +
    "margin: 5px;" +
    "border: 4px solid '#8e6f6f';" +
    "border-radius: 10px;}" +
    "*:hover{background: '#923838';}"

)
minus_button3.clicked.connect(lambda x: clicker(minus_button3.text() + str(3), energy_destroyed.text(), energy.text()))

#Energy destroyed
energy_destroyed = QLabel("0")
energy_destroyed.setAlignment(QtCore.Qt.AlignCenter)
energy_destroyed.setStyleSheet(
    "font-family: 'Fredoka One', cursive;" +
    "color: 'white';" +
    "font-size: 15px"
)

plus_button3 = QPushButton("+")
plus_button3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
plus_button3.setStyleSheet(
    "*{color: 'white';" +
    "font-size: 15px;" +
    "padding: 5px 3px;" +
    "margin: 5px;" +
    "border: 4px solid '#8e6f6f';" +
    "border-radius: 10px;}" +
    "*:hover{background: '#008da2';}"

)
plus_button3.clicked.connect(lambda x: clicker(plus_button3.text() + str(3), energy_destroyed.text(), energy.text()))

# endturn
endturn = QPushButton("End Turn")
endturn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
endturn.setStyleSheet(
    "*{color: 'white';" +
    "font-size: 15px;" +
    "padding: 5px 3px;" +
    "margin: 5px;" +
    "border: 4px solid '#8e6f6f';" +
    "border-radius: 10px}" +
    "*:hover{background: '#d2761e';}"

)
endturn.clicked.connect(lambda x: clicker(endturn.text(), eround.text().strip("Round "), energy.text()))

#reset Button

reset_button = QPushButton("Reset")
reset_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
reset_button.setStyleSheet(
    "*{color: 'white';" +
    "font-size: 15px;" +
    "padding: 5px 5px;" +
    "margin: 5px;" +
    "border: 4px solid '#8e6f6f';" +
    "border-radius: 10px;}" +
    "*:hover{background: '#008da2';}"

)
reset_button.clicked.connect(lambda x: clicker(reset_button.text(), energy_used.text(), energy.text()))


vertical.addWidget(eround)
grid.addWidget(energy, 1, 1)
grid.addWidget(label("Energy Used"), 2, 1)
#button layer 1
grid.addWidget(minus_button1, 3, 0)
grid.addWidget(energy_used, 3, 1)
grid.addWidget(plus_button1, 3, 3)

grid.addWidget(label("Energy Gained"), 4, 1)

#button Layer 2
grid.addWidget(minus_button2, 5, 0)
grid.addWidget(energy_gained, 5, 1)
grid.addWidget(plus_button2, 5, 3)

grid.addWidget(label("Energy Destroyed"), 6, 1)

#button layer 3
grid.addWidget(minus_button3, 7, 0)
grid.addWidget(energy_destroyed, 7, 1)
grid.addWidget(plus_button3, 7, 3)

#end turn Button
vertical.addWidget(endturn)

#reset Button
grid.addWidget(reset_button, 8, 1)

#footer
footer = "This App is coded by Clark "
foot = QLabel(footer)
foot.setAlignment(QtCore.Qt.AlignRight)
foot.setStyleSheet(
    "font-family: 'Lucida Handwriting', cursive;" +
    "color: 'white';" +
    "font-size: 5px;"

)
#version 1.5

grid.addWidget(foot, 8, 3)


vertical.addLayout(grid)
window.setLayout(vertical)
window.show()
sys.exit(app.exec())