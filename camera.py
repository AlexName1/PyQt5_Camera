# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QRegExpValidator, QRegExp


class Ui_MainWindow(object):
    # def __init__(self):
    #     self.onlyInt = QIntValidator()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 494)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(33, 242, 246, 16))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(33, 197, 253, 16))
        self.label_3.setObjectName("label_3")
        self.camera_simulator = QtWidgets.QLabel(self.centralwidget)
        self.camera_simulator.setGeometry(QtCore.QRect(30, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.camera_simulator.setFont(font)
        self.camera_simulator.setObjectName("camera_simulator")
        self.checkBox_mapir_survey_3_n = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_mapir_survey_3_n.setGeometry(QtCore.QRect(172, 104, 129, 17))
        self.checkBox_mapir_survey_3_n.setObjectName("checkBox_mapir_survey_3_n")
        self.button_result = QtWidgets.QPushButton(self.centralwidget)
        self.button_result.setGeometry(QtCore.QRect(290, 440, 101, 41))
        self.button_result.setObjectName("button_result")
        self.checkBox_PA = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_PA.setGeometry(QtCore.QRect(31, 81, 135, 17))
        self.checkBox_PA.setObjectName("checkBox_PA")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(33, 152, 306, 16))
        self.label_2.setObjectName("label_2")
        self.checkBox_MP = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_MP.setGeometry(QtCore.QRect(31, 104, 88, 17))
        self.checkBox_MP.setObjectName("checkBox_MP")

        self.checkBox_mapir_survey_3_w = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_mapir_survey_3_w.setGeometry(QtCore.QRect(172, 81, 132, 17))
        self.checkBox_mapir_survey_3_w.setObjectName("checkBox_mapir_survey_3_w")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(33, 332, 397, 16))
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(33, 287, 364, 16))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(33, 377, 381, 16))
        self.label_7.setObjectName("label_7")

        reg_ex = QRegExp("[0-9]+.?[0-9]{,2}")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(33, 171, 133, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setValidator(QRegExpValidator(reg_ex))

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(33, 216, 133, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setValidator(QRegExpValidator(reg_ex))

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(33, 261, 133, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setValidator(QRegExpValidator(reg_ex))

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(33, 306, 133, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setValidator(QRegExpValidator(reg_ex))

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(33, 351, 133, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setValidator(QRegExpValidator(reg_ex))

        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(33, 396, 133, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setValidator(QRegExpValidator(reg_ex))

        self.text_result = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_result.setGeometry(QtCore.QRect(445, 150, 280, 290))
        self.text_result.setObjectName("text_result")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.result()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Camera Simulator"))
        self.label_4.setText(_translate("MainWindow", "Введите проектное поперечное перекрытие, %"))
        self.label_3.setText(_translate("MainWindow", "Введите проектное продольнное перекрытие, %"))
        self.camera_simulator.setText(_translate("MainWindow", "Camera Simulator"))

        self.button_result.setText(_translate("MainWindow", "Рассчитать"))

        self.checkBox_PA.setText(_translate("MainWindow", "DJI Phantom Advanced"))
        self.checkBox_MP.setText(_translate("MainWindow", "DJI Mavic Pro"))

        self.checkBox_mapir_survey_3_w.setText(_translate("MainWindow", "Mapir Survey 3 W RGN"))
        self.checkBox_mapir_survey_3_n.setText(_translate("MainWindow", "Mapir Survey 3 N RGN"))

        self.label_2.setText(_translate("MainWindow", "Введите проектное пространственное разрешение, см/пикс"))

        self.label_6.setText(_translate("MainWindow", "Введите установленную скорость съемки в настройках внешней "
                                                      "камеры, сек"))
        self.label_5.setText(
            _translate("MainWindow", "Введите установленное в настройках внешней камеры ISO в единицах"))
        self.label_7.setText(
            _translate("MainWindow", "Введите предполагаемый интервал съемки в настройках внешней камеры"))

    def result(self):
        self.button_result.clicked.connect(lambda: self.write_text())

    def write_text(self):
        # self.text_result.clear()
        # if drone <= 1:
        if self.checkBox_PA.isChecked():
            carelemsizeforward = float(0.00261)
            carelemsizebroad = float(0.00261)
            carfocus = float(8.8)
            carmatrixsizefullpixforward = float(3648)
            carmatrixsizefullpixbroad = float(4864)

            if self.checkBox_mapir_survey_3_w.isChecked():
                mouelemsizeforward = float(0.00155)
                mouelemsizebroad = float(0.00155)
                moufocus = float(3.37)
                moumatrixsizefullpixforward = float(3000)
                moumatrixsizefullpixbroad = float(4000)

                # # TODO: проверка на наличие чисел
                if not self.lineEdit.text():
                    self.text_result.setText("Заполните значение: проектное пространственное разрешение, см/пикс")
                    return
                elif not self.lineEdit_2.text():
                    self.text_result.setText("Заполните значение: проектное продольнное перекрытие, %")
                    return
                elif not self.lineEdit_3.text():
                    self.text_result.setText("Заполните значение: проектное поперечное перекрытие, %")
                    return
                elif not self.lineEdit_4.text():
                    self.text_result.setText("Заполните значение: установленное в настройках внешней камеры ISO в "
                                             "единицах")
                    return
                elif not self.lineEdit_5.text():
                    self.text_result.setText("Заполните значение: установленная скорость съемки в "
                                             "настройках внешней камеры, сек")
                    return
                elif not self.lineEdit_6.text():
                    self.text_result.setText("Заполните значение: предполагаемый интервал съемки в настройках "
                                             "внешней камеры")
                    return

                gsdprj = float(self.lineEdit.text())
                prodprj = float(self.lineEdit_2.text())
                popprj = float(self.lineEdit_3.text())
                isoprj = float(self.lineEdit_4.text())
                shuprj = float(self.lineEdit_5.text())
                intprj = float(self.lineEdit_6.text())

                mourealsizeforward = float(mouelemsizeforward * (moumatrixsizefullpixforward))
                mourealsizebroad = float(mouelemsizebroad * (moumatrixsizefullpixbroad))
                Htrue = float(((gsdprj * float(10)) * moufocus) / mouelemsizeforward)
                mouprojectionrealforward = float((mourealsizeforward * Htrue) / moufocus)
                mouprojectionrealbroad = float((mourealsizebroad * Htrue) / moufocus)
                moubasisforward = float((mouprojectionrealforward / float(100)) * ((float(100) - prodprj)))
                moubasisbroad = float((mouprojectionrealbroad / float(100)) * ((float(100) - popprj)))
                carrealsizeforward = float(carelemsizeforward * carmatrixsizefullpixforward)
                carrealsizebroad = float(carelemsizebroad * carmatrixsizefullpixbroad)
                gsdcar = float((Htrue / carfocus) * carelemsizeforward)
                carprojectionrealforward = float((carrealsizeforward * Htrue) / carfocus)
                carprojectionrealbroad = float((carrealsizebroad * Htrue) / carfocus)
                prodolperekreal = float(
                    ((carprojectionrealforward - moubasisforward) / carprojectionrealforward) * float(100))
                popperekreal = float(((carprojectionrealbroad - moubasisbroad) / carprojectionrealbroad) * float(100))
                Hf = float(Htrue / 1000)
                H = round(Hf)
                Pdist = float(gsdprj * 0.8)
                PSpeed = float((Pdist / (1 / shuprj)) / 100)
                Speed = round(PSpeed)
                P05real = float(
                    ((mouprojectionrealforward / 1000) - (Speed) * intprj) / ((mouprojectionrealforward / 1000)) * 100)
                P05 = round(P05real)
                Prod = round(prodolperekreal)
                Pop = round(popperekreal)
                self.text_result.setText(f'Реальное продольное перекрытие съемочных материалов с внешней камеры с '
                                         f'заданным интервалом в процентах = {P05}\n\n'
                                         f'Высота полета БАС, устанавливаемая для камеры носителя, в метрах = {H}\n\n'
                                         f'Предельная скорость полета носителя в метрах = {Speed}\n\n'
                                         f'Продольное перекрытие, устанавливаемое для камеры носителя в '
                                         f'процессе формирования полетного задания в процентах, в процентах = '
                                         f'{Prod}\n\n'
                                         f'Поперечное перекрытие, устанавливаемое для камеры носителя в '
                                         f'процессе формирования полетного задания, в процентах = {Pop}\n\n')

            else:
                self.text_result.setText('Камеры нет в базе!')
        else:
            self.text_result.setText('БВС нет в базе!')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
