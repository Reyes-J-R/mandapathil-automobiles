from PyQt5.QtWidgets import *
# from PyQt5 import Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os
import datetime
import json
import random
from threading import Thread

from package import DataMethods, Window, DashBoard, EntryListItem, EntryShowFrame, NewEntryWindow, ActiveEntries, SubWindow, ItemsWindowLayout, StockWindowLayout

# from win32api import GetSystemMetrics


stylesheet = open("style.css").read()

app = QApplication(sys.argv)

QFontDatabase.addApplicationFont("Fonts/Oswald-VariableFont_wght.ttf")
QFontDatabase.addApplicationFont("Fonts/Righteous-Regular.ttf")
QFontDatabase.addApplicationFont("Fonts/Barlow-Regular.ttf")

app.setStyleSheet(stylesheet)
screen = Window()
screen.closeEvent = lambda event: event.accept()
screen.show()
screen_rect = app.desktop().screenGeometry()
screen.setFixedSize(screen_rect.width() - 10, screen_rect.height()-70)
# screen.setWindowFlags()
layout = QGridLayout()
layout.setContentsMargins(0, 0, 0, 0)
screen.setLayout(layout)

active_entrywindow = SubWindow("Active Entries")
active_entries = ActiveEntries()
active_entrywindow.setLayout(QGridLayout())
active_entrywindow.layout().addWidget(active_entries)

new_entry_window = NewEntryWindow(active_entries)
new_entry_window.hide()

itemswindow = SubWindow("Items")
items_window_layout = ItemsWindowLayout()
itemswindow.setLayout(items_window_layout)
itemswindow.setGeometry(430, 150, 600, 500)


# stockwindow = SubWindow("Stock")
# stock_window_layout = StockWindowLayout
# stockwindow.setLayout(stock_window_layout)
# stockwindow.setFixedSize(screen_rect.width() - 10, screen_rect.height()-70)

dashboard = DashBoard(active_entrywindow, active_entries, itemswindow)
layout.addWidget(dashboard)

sys.exit(app.exec_())