from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore    import *
from PyQt5 import QtCore
import random,time
import os



count = 0
wastheButton_1Pressed = False
wastheButton_2Pressed = False
wastheButton_3Pressed = False
wastheButton_4Pressed = False
wastheButton_5Pressed = False
wastheButton_6Pressed = False
wastheButton_7Pressed = False
wastheButton_8Pressed = False
wastheButton_9Pressed = False


class Play(QWidget):
        def __init__(self):
                super().__init__()
                self.x = QPushButton()
                self.setGeometry(600,200,540,540)
                self.setFixedHeight(630)
                self.setFixedWidth(555)
                self.setWindowTitle("Tic-Toc-Toi")
                self.create_Button()
                self.r_x = Restart_X()
                self.r_o = Restart_O()
                self.r_s = Restart_S()


        def create_Button(self):
                self.layout = QGridLayout()
                self.button_1 = QPushButton()
                self.button_2 = QPushButton()
                self.button_3 = QPushButton()
                self.button_4 = QPushButton()
                self.button_5 = QPushButton()
                self.button_6 = QPushButton()
                self.button_7 = QPushButton()
                self.button_8 = QPushButton()
                self.button_9 = QPushButton()
                self.button_1.setFixedSize(170, 200)
                self.button_2.setFixedSize(170, 200)
                self.button_3.setFixedSize(170, 200)
                self.button_4.setFixedSize(170, 200)
                self.button_5.setFixedSize(170, 200)
                self.button_6.setFixedSize(170, 200)
                self.button_7.setFixedSize(170, 200)
                self.button_8.setFixedSize(170, 200)
                self.button_9.setFixedSize(170, 200)

                self.layout.addWidget(self.button_1, 0, 0)
                self.layout.addWidget(self.button_2, 0, 1)
                self.layout.addWidget(self.button_3, 0, 2)
                self.layout.addWidget(self.button_4, 1, 0)
                self.layout.addWidget(self.button_5, 1, 1)
                self.layout.addWidget(self.button_6, 1, 2)
                self.layout.addWidget(self.button_7, 2, 0)
                self.layout.addWidget(self.button_8, 2, 1)
                self.layout.addWidget(self.button_9, 2, 2)

                self.button_1.setStyleSheet("background-color : black")
                self.button_2.setStyleSheet("background-color : black")
                self.button_3.setStyleSheet("background-color : black")
                self.button_4.setStyleSheet("background-color : black")
                self.button_5.setStyleSheet("background-color : black")
                self.button_6.setStyleSheet("background-color : black")
                self.button_7.setStyleSheet("background-color : black")
                self.button_8.setStyleSheet("background-color : black")
                self.button_9.setStyleSheet("background-color : black")


                self.setLayout(self.layout)
                self.setStyleSheet("background-color : red")


                self.button_list = ["button_1","button_2","button_3","button_4","button_5","button_6","button_7","button_8","button_9"]
                self.game_over = {"button_1" : "","button_2" : "","button_3" : "","button_4" : "","button_5" : "","button_6" : "","button_7" : "","button_8" : "","button_9" : ""}

                self.singlemod_play()

        def singlemod_play(self):
                self.button_1.clicked.connect(self.BUTTON_1)
                self.button_2.clicked.connect(self.BUTTON_2)
                self.button_3.clicked.connect(self.BUTTON_3)
                self.button_4.clicked.connect(self.BUTTON_4)
                self.button_5.clicked.connect(self.BUTTON_5)
                self.button_6.clicked.connect(self.BUTTON_6)
                self.button_7.clicked.connect(self.BUTTON_7)
                self.button_8.clicked.connect(self.BUTTON_8)
                self.button_9.clicked.connect(self.BUTTON_9)





        def BUTTON_1(self):
                global count
                global wastheButton_1Pressed
                for button in self.button_list:
                        if "button_1" == button and wastheButton_1Pressed == False:
                                self.button_1.setIcon(QIcon("X.png"))
                                self.button_1.setIconSize(QtCore.QSize(160, 190))
                                self.button_list.remove("button_1")
                                self.game_over.update({"button_1":"X"})
                                wastheButton_1Pressed = True
                                self.Game_Over()

                                count +=1
                                if count < 9:
                                        self.program()
                                else:
                                        self.scoreless()




        def BUTTON_2(self):
                global count
                global wastheButton_2Pressed
                for button in self.button_list:
                        if "button_2" == button and wastheButton_2Pressed == False:
                                self.button_2.setIcon(QIcon("X.png"))
                                self.button_2.setIconSize(QtCore.QSize(160, 190))
                                self.button_list.remove("button_2")
                                self.game_over.update({"button_2":"X"})
                                wastheButton_2Pressed = True
                                self.Game_Over()
                                count += 1
                                if count < 9:
                                        self.program()
                                else:
                                        self.scoreless()



        def BUTTON_3(self):
                global count
                global wastheButton_3Pressed
                for button in self.button_list:
                        if "button_3" == button and wastheButton_3Pressed == False:
                                self.button_3.setIcon(QIcon("X.png"))
                                self.button_3.setIconSize(QtCore.QSize(160, 190))
                                self.button_list.remove("button_3")
                                self.game_over.update({"button_3":"X"})
                                wastheButton_3Pressed = True
                                self.Game_Over()
                                count += 1
                                if count < 9:
                                        self.program()
                                else:
                                        self.scoreless()




        def BUTTON_4(self):
                global count
                global wastheButton_4Pressed
                for button in self.button_list:
                        if "button_4" == button and wastheButton_4Pressed == False:
                                self.button_4.setIcon(QIcon("X.png"))
                                self.button_4.setIconSize(QtCore.QSize(160, 190))
                                self.button_list.remove("button_4")
                                self.game_over.update({"button_4":"X"})
                                wastheButton_4Pressed = True
                                self.Game_Over()
                                count += 1
                                if count < 9:
                                        self.program()
                                else:
                                        self.scoreless()


        def BUTTON_5(self):
                global count
                global wastheButton_5Pressed
                for button in self.button_list:
                        if "button_5" == button and wastheButton_5Pressed == False:
                                self.button_5.setIcon(QIcon("X.png"))
                                self.button_5.setIconSize(QtCore.QSize(160, 190))
                                self.button_list.remove("button_5")
                                self.game_over.update({"button_5":"X"})
                                wastheButton_5Pressed = True
                                self.Game_Over()
                                count += 1
                                if count < 9:
                                        self.program()
                                else:
                                        self.scoreless()


        def BUTTON_6(self):
                global count
                global wastheButton_6Pressed
                for button in self.button_list:
                        if "button_6" == button and wastheButton_6Pressed == False:
                                self.button_6.setIcon(QIcon("X.png"))
                                self.button_6.setIconSize(QtCore.QSize(160, 190))
                                self.button_list.remove("button_6")
                                self.game_over.update({"button_6":"X"})
                                wastheButton_6Pressed = True
                                self.Game_Over()
                                count += 1
                                if count < 9:
                                        self.program()
                                else:
                                        self.scoreless()


        def BUTTON_7(self):
                global count
                global wastheButton_7Pressed
                for button in self.button_list:
                        if "button_7" == button and wastheButton_7Pressed == False:
                                self.button_7.setIcon(QIcon("X.png"))
                                self.button_7.setIconSize(QtCore.QSize(160, 190))
                                self.button_list.remove("button_7")
                                self.game_over.update({"button_7":"X"})
                                wastheButton_7Pressed = True
                                self.Game_Over()
                                count += 1
                                if count < 9:
                                        self.program()
                                else:
                                        self.scoreless()


        def BUTTON_8(self):
                global count
                global wastheButton_8Pressed
                for button in self.button_list:
                        if "button_8" == button and wastheButton_8Pressed == False:
                                self.button_8.setIcon(QIcon("X.png"))
                                self.button_8.setIconSize(QtCore.QSize(160, 190))
                                self.button_list.remove("button_8")
                                self.game_over.update({"button_8":"X"})
                                wastheButton_8Pressed = True
                                self.Game_Over()
                                count += 1
                                if count < 9:
                                        self.program()
                                else:
                                        self.scoreless()


        def BUTTON_9(self):
                global count
                global wastheButton_9Pressed
                for button in self.button_list:
                        if "button_9" == button and wastheButton_9Pressed == False:
                                self.button_9.setIcon(QIcon("X.png"))
                                self.button_9.setIconSize(QtCore.QSize(160,190))
                                self.button_list.remove("button_9")
                                self.game_over.update({"button_9":"X"})
                                wastheButton_9Pressed = True
                                self.Game_Over()
                                count += 1
                                if count < 9:
                                        self.program()
                                else:
                                        self.scoreless()


        def program(self):
                global count
                global wastheButton_1Pressed
                global wastheButton_2Pressed
                global wastheButton_3Pressed
                global wastheButton_4Pressed
                global wastheButton_5Pressed
                global wastheButton_6Pressed
                global wastheButton_7Pressed
                global wastheButton_8Pressed
                global wastheButton_9Pressed
                x = random.choice(self.button_list)
                if x == "button_1":
                        self.button_1.setIcon(QIcon("O.png"))
                        self.button_1.setIconSize(QtCore.QSize(145, 175))
                        wastheButton_1Pressed = True
                        self.button_list.remove("button_1")
                        self.game_over["button_1"] = "O"
                        count += 1
                        self.Game_Over()
                elif x == "button_2":
                        self.button_2.setIcon(QIcon("O.png"))
                        self.button_2.setIconSize(QtCore.QSize(145, 175))
                        wastheButton_2Pressed = True
                        self.button_list.remove("button_2")
                        self.game_over["button_2"] = "O"
                        count += 1
                        self.Game_Over()
                elif x == "button_3":
                        self.button_3.setIcon(QIcon("O.png"))
                        self.button_3.setIconSize(QtCore.QSize(145, 175))
                        wastheButton_3Pressed = True
                        self.button_list.remove("button_3")
                        self.game_over["button_3"] = "O"
                        count += 1
                        self.Game_Over()
                elif x == "button_4":
                        self.button_4.setIcon(QIcon("O.png"))
                        self.button_4.setIconSize(QtCore.QSize(145, 175))
                        wastheButton_4Pressed = True
                        self.button_list.remove("button_4")
                        self.game_over["button_4"] = "O"
                        count += 1
                        self.Game_Over()
                elif x == "button_5":
                        self.button_5.setIcon(QIcon("O.png"))
                        self.button_5.setIconSize(QtCore.QSize(145, 175))
                        wastheButton_5Pressed = True
                        self.button_list.remove("button_5")
                        self.game_over["button_5"] = "O"
                        count += 1
                        self.Game_Over()
                elif x == "button_6":
                        self.button_6.setIcon(QIcon("O.png"))
                        self.button_6.setIconSize(QtCore.QSize(145, 175))
                        wastheButton_6Pressed = True
                        self.button_list.remove("button_6")
                        self.game_over["button_6"] = "O"
                        count += 1
                        self.Game_Over()
                elif x == "button_7":
                        self.button_7.setIcon(QIcon("O.png"))
                        self.button_7.setIconSize(QtCore.QSize(145, 175))
                        wastheButton_7Pressed = True
                        self.button_list.remove("button_7")
                        self.game_over["button_7"] = "O"
                        count += 1
                        self.Game_Over()
                elif x == "button_8":
                        self.button_8.setIcon(QIcon("O.png"))
                        self.button_8.setIconSize(QtCore.QSize(145, 175))
                        wastheButton_8Pressed = True
                        self.button_list.remove("button_8")
                        self.game_over["button_8"] = "O"
                        count += 1
                        self.Game_Over()
                elif x == "button_9":
                        self.button_9.setIcon(QIcon("O.png"))
                        self.button_9.setIconSize(QtCore.QSize(145, 175))
                        wastheButton_9Pressed = True
                        self.button_list.remove("button_9")
                        self.game_over["button_9"] = "O"
                        count += 1
                        self.Game_Over()

        def Game_Over(self):


                button_1 = self.game_over["button_1"]
                button_2 = self.game_over["button_2"]
                button_3 = self.game_over["button_3"]
                button_4 = self.game_over["button_4"]
                button_5 = self.game_over["button_5"]
                button_6 = self.game_over["button_6"]
                button_7 = self.game_over["button_7"]
                button_8 = self.game_over["button_8"]
                button_9 = self.game_over["button_9"]



                if button_1 == "X" and button_2 == "X" and button_3 == "X":

                        self.play_Again_X()


                elif button_1 == "O" and button_2 == "O" and button_3 == "O":

                        self.play_Again_O()


                elif button_4 == "X" and button_5 == "X" and button_6 == "X":

                        self.play_Again_X()


                elif button_4 == "O" and button_5 == "O" and button_6 == "O":

                        self.play_Again_O()



                elif button_7 == "X" and button_8 == "X" and button_9 == "X":

                        self.play_Again_X()


                elif button_7 == "O" and button_8 == "O" and button_9 == "O":

                        self.play_Again_O()



                elif button_1 == "X" and button_4 == "X" and button_7 == "X":

                        self.play_Again_X()


                elif button_1 == "O" and button_4 == "O" and button_7 == "O":

                        self.play_Again_O()



                elif button_2 == "X" and button_5 == "X" and button_8 == "X":

                        self.play_Again_X()


                elif button_2 == "O" and button_5 == "O" and button_8 == "O":

                        self.play_Again_O()


                elif button_3 == "X" and button_6 == "X" and button_9 == "X":

                        self.play_Again_X()


                elif button_3 == "O" and button_6 == "O" and button_9 == "O":

                        self.play_Again_O()



                elif button_1 == "X" and button_5 == "X" and button_9 == "X":

                        self.play_Again_X()


                elif button_1 == "O" and button_5 == "O" and button_9 == "O":

                        self.play_Again_O()



                elif button_3 == "X" and button_5 == "X" and button_7 == "X":

                        self.play_Again_X()


                elif button_3 == "O" and button_5 == "O" and button_7 == "O":

                        self.play_Again_O()






        def play_Again_X(self):

                self.r_x.show()
                self.hide()

        def play_Again_O(self):

                self.r_o.show()
                self.hide()
        def scoreless(self):

                self.r_s.show()
                self.hide()


class Window(QWidget):
        def __init__(self):
                super().__init__()
                self.init_ui()
                self.setGeometry(600,200,540,570)
                self.setWindowTitle("Tic-Toc-Toi")
                self.giris.clicked.connect(self.new_window)
                self.p = Play()
                self.setStyleSheet("background-color : black")
                self.setFixedHeight(570)
                self.setFixedWidth(540)

        def init_ui(self):
                self.giris = QPushButton("Play")
                self.cikis = QPushButton()
                self.write = QLabel(" Welcome to Tic-Toc-Toi")
                self.write.setFont(QFont('Times',15))
                self.write.setStyleSheet("color : red")
                self.giris.setFont(QFont('Times',11))
                self.giris.setStyleSheet("color : black")
                v_box = QVBoxLayout()
                h_box = QHBoxLayout()

                v_box.addStretch()
                v_box.addWidget(self.write)
                v_box.addStretch()
                h_box.addStretch()
                v_box.addWidget(self.giris)
                v_box.addStretch()
                h_box.addLayout(v_box)
                h_box.addStretch()
                self.setLayout(h_box)
                self.giris.setStyleSheet("background-color : red")
                self.show()

        def new_window(self):
                self.p.show()
                self.hide()


class Restart_X(QWidget):
        def __init__(self):
                super().__init__()
                self.setGeometry(600, 200, 540, 570)
                self.setStyleSheet("background-color : black")
                self.setFixedHeight(570)
                self.setFixedWidth(540)
                self.setWindowTitle("Tic-Toc-Toi")
                self.init_ui()
                self.restard_button.clicked.connect(self.reset)

        def init_ui(self):


                self.label = QLabel("YOU WON")

                self.restard_button = QPushButton("Restart")

                self.v_box = QVBoxLayout()
                self.h_box = QHBoxLayout()

                self.v_box.addStretch()
                self.v_box.addWidget(self.label)
                self.v_box.addStretch()
                self.h_box.addStretch()
                self.v_box.addWidget(self.restard_button)
                self.v_box.addStretch()

                self.h_box.addLayout(self.v_box)
                self.h_box.addStretch()
                self.setLayout(self.h_box)

                self.label.setFont(QFont('Times',15))
                self.label.setStyleSheet("color : red")

                self.restard_button.setFont(QFont('Times', 11))
                self.restard_button.setStyleSheet("color : black")
                self.restard_button.setStyleSheet("background-color : red")



        def reset(self):

                os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

class Restart_O(QWidget):
        def __init__(self):
                super().__init__()
                self.setGeometry(600, 200, 540, 570)
                self.setStyleSheet("background-color : black")
                self.setFixedHeight(570)
                self.setFixedWidth(540)
                self.setWindowTitle("Tic-Toc-Toi")
                self.init_ui()
                self.restard_button.clicked.connect(self.reset)

        def init_ui(self):


                self.label = QLabel("YOU LOSE")

                self.restard_button = QPushButton("Restart")

                self.v_box = QVBoxLayout()
                self.h_box = QHBoxLayout()

                self.v_box.addStretch()
                self.v_box.addWidget(self.label)
                self.v_box.addStretch()
                self.h_box.addStretch()
                self.v_box.addWidget(self.restard_button)
                self.v_box.addStretch()

                self.h_box.addLayout(self.v_box)
                self.h_box.addStretch()
                self.setLayout(self.h_box)

                self.label.setFont(QFont('Times',15))
                self.label.setStyleSheet("color : red")

                self.restard_button.setFont(QFont('Times', 11))
                self.restard_button.setStyleSheet("color : black")
                self.restard_button.setStyleSheet("background-color : red")


        def reset(self):

                os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
class Restart_S(QWidget):
        def __init__(self):
                super().__init__()
                self.setGeometry(600, 200, 540, 570)
                self.setStyleSheet("background-color : black")
                self.setFixedHeight(570)
                self.setFixedWidth(540)
                self.setWindowTitle("Tic-Toc-Toi")
                self.init_ui()
                self.restard_button.clicked.connect(self.reset)

        def init_ui(self):


                self.label = QLabel("SCORELESS")

                self.restard_button = QPushButton("Restart")

                self.v_box = QVBoxLayout()
                self.h_box = QHBoxLayout()

                self.v_box.addStretch()
                self.v_box.addWidget(self.label)
                self.v_box.addStretch()
                self.h_box.addStretch()
                self.v_box.addWidget(self.restard_button)
                self.v_box.addStretch()

                self.h_box.addLayout(self.v_box)
                self.h_box.addStretch()
                self.setLayout(self.h_box)

                self.label.setFont(QFont('Times',15))
                self.label.setStyleSheet("color : red")

                self.restard_button.setFont(QFont('Times', 11))
                self.restard_button.setStyleSheet("color : black")
                self.restard_button.setStyleSheet("background-color : red")


        def reset(self):

                os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

if __name__ == "__main__":
        app = QApplication(sys.argv)
        pencere = Window()
        sys.exit(app.exec_())