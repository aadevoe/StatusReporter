import sys

from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtGui import QListWidgetItem

#######################################
import configmanager
import sqlitemanager
from weeklyreportwindow import ReportDialog

c = configmanager.loadconfig()
d = sqlitemanager

if c.create_table == "true":
    d.createTable(c.sqlitepath, c.query)
#######################################

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = uic.loadUi("mainwindow.ui")
        self.ui.setWindowTitle("StatusReporter v1.0")
        self.ui.move(300, 300)
        self.ui.pushButton.setDisabled(True)
        self.ui.calendarWidget.showToday()

        self.ui.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"),
                        lambda: d.insertStatus(c.sqlitepath, str(self.ui.textEdit.toPlainText())))

        self.ui.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), updateStatuses)

        self.ui.connect(self.ui.actionGenerate_Weekly_Report, QtCore.SIGNAL("triggered()"), onGenerateWeeklyReport)

        self.ui.connect(self.ui.textEdit, QtCore.SIGNAL("textChanged()"),
                        lambda: self.ui.pushButton.setDisabled(not self.ui.textEdit.toPlainText().trimmed()))

        self.ui.connect(self.ui.calendarWidget, QtCore.SIGNAL("selectionChanged()"), onDayChanged)
        for st in loadAndSortStatusesForCurrentDay():
            self.ui.listWidget.addItem(st)

        self.ui.show()

######################################

def loadAndSortStatusesForDay(day):
    win.ui.listWidget.clear()
    qstatuses = []
    map(lambda x: qstatuses.append(QListWidgetItem(x.status)),
        sorted(d.loadStatusesByDay(c.sqlitepath,day),
               key=lambda x: x.date, reverse=False))
    setStatuses(qstatuses)

def loadAndSortStatusesForCurrentDay():
    qstatuses = []
    map(lambda x: qstatuses.append(QListWidgetItem(x.status)),
        sorted(d.loadStatusesByCurrentDay(c.sqlitepath),
               key=lambda x: x.date, reverse=False))
    return qstatuses

def setStatuses(qstatuses):
    win.ui.listWidget.clear()
    for item in qstatuses:
        win.ui.listWidget.addItem(item)

def updateStatuses():
    win.ui.listWidget.clear()
    for item in loadAndSortStatusesForCurrentDay():
        win.ui.listWidget.addItem(item)


def onDayChanged():
    loadAndSortStatusesForDay(str(win.ui.calendarWidget.selectedDate().toPyDate()))

def onGenerateWeeklyReport():
    reportdialog.loadWeeklyStatuses()
    reportdialog.ui.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = MainWindow()
    reportdialog = ReportDialog()
    sys.exit(app.exec_())


