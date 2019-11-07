import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import uic
import threading
import python.Sync as Sync

form_class = uic.loadUiType("./qtDesigner/servergui.ui")[0]


class MyWindow(QMainWindow, form_class, threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.start()
        super().__init__()
        self.setupUi(self)

        self.DBdata = Sync.SyncCursor()
        self.referenceImg = QPixmap()

        # Tab1 메뉴
        self.menuTable.clear()
        self.make_table_tab1(self.DBdata.menu_list)
        self.menuTable.clicked.connect(self.menuClicked)

        # Tab2 분석
        self.AllBtn.clicked.connect(lambda : self.showReivewGraph(4))
        self.PosBtn.clicked.connect(lambda : self.showReivewGraph(0))
        self.NegBtn.clicked.connect(lambda : self.showReivewGraph(1))
        self.NorBtn.clicked.connect(lambda : self.showReivewGraph(2))
        self.ComBtn.clicked.connect(lambda : self.showReivewGraph(3))
        # self.reviewData = Sync.SyncCursor()
        self.ReviewTable.clear()
        self.ReviewTable.clicked.connect(self.cellClicked)
        self.reviewLabel.setWordWrap(True)


    def _initTable(self, _sTable: QTableWidget, _list=None, col=1, _Header=['first','second']):
        _sTable.clear()
        _sTable.setColumnCount(col)
        _sTable.setRowCount(len(_list))
        _sTable.setHorizontalHeaderLabels(_Header)
        header = _sTable.horizontalHeader()
        header.setSectionResizeMode(col-1, QHeaderView.Stretch)
        _sTable.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)

    def _setImage(self, _sLabel : QLabel, _width=200, _height=200, _src=None):
        if type(_src) == bytes:
            pixmap = QPixmap()
            pixmap.loadFromData(_src)
        else:
            pixmap = QPixmap(_src)
        resizePixmap = pixmap.scaled(_width, _height)
        self.referenceImg = resizePixmap.copy()
        _sLabel.setPixmap(self.referenceImg)
        del resizePixmap
        del pixmap

    #================================================================================================
    #                           Tab 1 -- 메뉴
    #================================================================================================



    def make_table_tab1(self, _list):
        self._initTable(_sTable=self.menuTable, _list=_list, col=4, _Header=["menuID", "국가", "메뉴", "가격"])
        n = 0
        t = 0
        while n < len(_list):
            if _list[n][2] == '한식' or _list[n][2] == '중식' or _list[n][2] == '일식' or \
                    _list[n][4] == None  or _list[n][3] == '아이콘':
                n += 1
                continue
            self.menuTable.setItem(t, 0, QTableWidgetItem(str(_list[n][0])))

            if str(_list[n][1]) == '한국':
                self.menuTable.setItem(t, 1, QTableWidgetItem('한국'))
            elif str(_list[n][1]) == '중국':
                self.menuTable.setItem(t, 1, QTableWidgetItem('중국'))
            elif str(_list[n][1]) == '일본':
                self.menuTable.setItem(t, 1, QTableWidgetItem('일본'))

            self.menuTable.setItem(t, 2, QTableWidgetItem(str(_list[n][2])))
            self.menuTable.setItem(t, 3, QTableWidgetItem(str(_list[n][4])))
            n += 1
            t += 1
        self.menuTable.setRowCount(t)
        self.menuTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def set_infoTable(self, _menuid = 0):
        #sales_list
        # self.menuTable.setItem(t, 0, QTableWidgetItem(str(_list[n][0])))
        # temp = [i for i in Sync.sales_list if i[2] == 1001]


        temp = [i for i in self.DBdata.sales_list if i[2] == _menuid]
        totalNum = len(temp)
        if totalNum == 0:
            sumN = 0
            Percent = str(0) + '%'
        else:
            sumN = len(temp) * int(temp[0][-1])
            sumAll = 0
            for i in self.DBdata.sales_list:
                sumAll += float(i[-1])
            Percent =format(sumN / sumAll * 100, '.2f') + '%'

        self.menuInfoTable.setItem(0,0, QTableWidgetItem(str(totalNum) + "개"))
        self.menuInfoTable.setItem(1, 0, QTableWidgetItem(str(sumN) + "원"))
        self.menuInfoTable.setItem(2, 0, QTableWidgetItem(Percent))

    def find_img(self, key=1001):
        for i in self.DBdata.menu_list:
            if key in i:
                return i[-1]

    def menuClicked(self, signal):
        row = signal.row()
        menuID = int(self.menuTable.item(row, 0).text())
        Bimg = self.find_img(menuID)

        self._setImage(_sLabel=self.menuImageLabel, _width=441, _height=461, _src=Bimg)
        self.set_infoTable(_menuid=menuID)


    # ================================================================================================
    #                           Tab 2 -- 분석
    # ================================================================================================

    def cellClicked(self, signal):
        row = signal.row()
        column = signal.column()
        self.reviewLabel.setText(self.ReviewTable.item(row, column).text())

    def showReivewGraph(self, op=4):
        if op == 4:
            self.DBdata.showAllGraph()
            self.calcReview(self.DBdata.table_list)
        else:
            self.DBdata.showSepGraph(op)
            if op == 0:
                self.calcReview(self.DBdata.Positive)
            elif op == 1:
                self.calcReview(self.DBdata.Negative)
            elif op == 2:
                self.calcReview(self.DBdata.Normal)
            elif op == 3:
                self.calcReview(self.DBdata.Complexive)

        self._setImage(_src='./foo.png', _width=571, _height=421, _sLabel=self.GraphLabel)

    def make_table_tab2(self, _list):
        self._initTable(_sTable=self.ReviewTable, _list=_list, col=1, _Header=["Review"])

        for i in range(0, len(_list)):
            self.ReviewTable.setItem(i, 0, QTableWidgetItem(str(_list[i][1])))

        self.ReviewTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def calcReview(self, _list):
        self.totalLabel.setText("Total Num : " + str(len(_list)))
        aveN = 0.0
        maxN = 0
        minN = 100

        self.make_table_tab2(_list)

        for i in _list:
            if float(i[-1][:-1]) > maxN:
                maxN = float(i[-1][:-1])
            elif float(i[-1][:-1]) < minN:
                minN = float(i[-1][:-1])
            aveN = aveN + float(i[-1][:-1])

        if len(_list) == len(self.DBdata.table_list):
            aveN = len(self.DBdata.Positive) / len(self.DBdata.table_list) * 100
            self.aveLabel.setText("Positive Per : " + format(aveN, '.1f') + "%")
            pass
        else:
            aveN = aveN / len(_list)
            self.aveLabel.setText("Avarage : " + format(aveN, '.1f') + "%")
        self.bestLabel.setText("Max Percent : " + format(maxN,'.1f') + "%")
        self.worstLabel.setText("Min Percent : " + format(minN,'.1f') + "%")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywind = MyWindow()
    mywind.show()
    sys.exit(app.exec_())
