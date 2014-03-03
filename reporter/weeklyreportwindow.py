from PyQt4 import QtGui, QtCore, uic
import configmanager
import sqlitemanager
#############################################


c = configmanager.loadconfig()
d = sqlitemanager
#############################################
class ReportDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = uic.loadUi("weeklyreportwindow.ui")
        self.ui.setWindowTitle("Generated weekly report ")
        self.ui.move(500, 500)

    def loadWeeklyStatuses(self):
        self.ui.textBrowser.clear()
        content = ""
        statuses = d.loadCurrentWeekStatuses(c.sqlitepath)
        sorted_keys = sorted(statuses)
        for st in sorted_keys:
            content+='\n'
            content+=st
            content+='\n'
            if len (statuses[st]) > 0:
                for stsi in statuses[st]:
                    content += stsi.status
                    content += '\n'
                # content+=statuses[st][0].status
        self.ui.textBrowser.insertPlainText(content)
