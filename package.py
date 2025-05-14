import json
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import datetime
import sys
from threading import Thread
import time

app = QApplication(sys.argv)
screen_rect = app.desktop().screenGeometry()

class DataMethods:
    def get_data(file):
        with open(f"{file}.json", 'r') as datafile:
            data = json.load(datafile)
        return data

    def put_data(data, file):
        with open(f"{file}.json", 'w') as file:
            json.dump(data, file, indent=4)

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Mandapathil Automobiles")
        self.setGeometry(0, 0, 500, 500)
        self.setFixedSize(1300, 600)

class DashBoardSection(QFrame):
    def __init__(self, heading, objectName):
        QFrame.__init__(self, objectName=objectName)
        
        self.layout = QGridLayout()
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.setLayout(self.layout)
        self.heading = QLabel(f"{heading}")
        # self.heading.font().setUnderline(True)
        

        self.layout.addWidget(self.heading, 0, 0, 1, 2, Qt.AlignCenter)


class DashBoard(QFrame):
    def __init__(self, entrywindow, entries, itemswindow, stockwindow, entryhistorywindow):

        QFrame.__init__(self)
        self.entrywindow = entrywindow
        self.entries = entries
        self.itemswindow = itemswindow
        self.stockwindow = stockwindow
        self.entryhistorywindow = entryhistorywindow

        self.layout = QGridLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)

        self.datetimeFrame = QFrame(objectName='dtframe')
        self.dtLayout = QGridLayout()
        self.datetimeFrame.setLayout(self.dtLayout)

        self.timelabel = QLabel(objectName="time-text")
        self.time_p_label = QLabel(objectName='time-p-label')
        self.time_p_label.setFont(QFont("Sans Serif", 19))
        self.datelabel = QLabel(objectName='date-text')
        self.daylabel = QLabel(objectName='day-text')
        self.daylabel.setFont(QFont("Sans Serif", 17))
        # Thread(target=self.show_time, daemon=True).start()

        self.toolframe = QFrame(objectName='toolframe')
        self.toolframe.setStyleSheet("margin-top: 20px")
        self.toolframelayout = QGridLayout()
        self.toolframe.setLayout(self.toolframelayout)
        self.tool_1 = QPushButton("Notes", objectName='dashboard-tool1')
        self.tool_2 = QPushButton("Tool2", objectName='dashboard-tool2')
        self.tool_3 = QPushButton("tool3", objectName='dashboard-tool3')

        self.toolframelayout.addWidget(self.tool_1, 2, 0, 1, 1)
        self.toolframelayout.addWidget(self.tool_2, 2, 1, 1, 1)
        self.toolframelayout.addWidget(self.tool_3, 2, 2, 1, 1)

        self.dtLayout.addWidget(self.timelabel, 0, 0, 1, 1)
        self.dtLayout.addWidget(self.time_p_label, 0, 1, 1, 1)
        self.dtLayout.addWidget(self.datelabel, 1, 0, 1, 2)
        self.dtLayout.addWidget(self.daylabel, 2, 0, 1, 2)
        self.dtLayout.addWidget(self.toolframe, 3, 0, 1, 2)

        self.EntrySection = DashBoardSection("Entries", objectName='dashboard-entrysection')
        self.EntrySection.heading.setObjectName("entrysection-heading")
        self.ActiveEntry = QFrame(objectName='dashboard-entrysection-sub1')
        self.ActiveEntry.setLayout(QGridLayout())
        self.ActiveEntryIcon = QLabel()
        self.ActiveEntryIcon.setPixmap(QPixmap("icons/entry_1.png"))
        self.ActiveEntryLabel = QLabel("Active Entries", objectName='dashboard-entrysection-label-sub1')
        self.EntryHistory = QFrame(objectName='dashboard-entrysection-sub2')
        self.EntryHistory.setLayout(QGridLayout())
        self.EntryHistoryIcon = QLabel()
        self.EntryHistoryIcon.setPixmap(QPixmap("icons/entry_history.png"))
        self.EntryHistoryLabel = QLabel("History", objectName='dashboard-entrysection-label-sub2')

        self.ActiveEntry.layout().addWidget(self.ActiveEntryLabel, 1, 0, 1, 1, Qt.AlignCenter)
        self.ActiveEntry.layout().addWidget(self.ActiveEntryIcon, 0, 0, 1, 1, Qt.AlignCenter)
        self.EntryHistory.layout().addWidget(self.EntryHistoryLabel, 1, 0, 1, 1, Qt.AlignCenter)
        self.EntryHistory.layout().addWidget(self.EntryHistoryIcon, 0, 0, 1, 1, Qt.AlignCenter)

        # self.EntryHistoryButton = QPushButton(objectName='dashboard-entrysection-sub3')

        self.EntrySection.layout.addWidget(self.ActiveEntry, 1, 0, 1, 1, Qt.AlignCenter)
        self.EntrySection.layout.addWidget(self.EntryHistory, 1, 1, 1, 1, Qt.AlignCenter)
        # self.EntrySection.layout.addWidget(self.ActiveEntryLabel, 2, 0, 1, 1, Qt.AlignCenter)
        # self.EntrySection.layout.addWidget(self.EntryHistoryLabel, 2, 1, 1, 1, Qt.AlignCenter)

        self.OrderSection = DashBoardSection(heading="Orders", objectName='dashboard-ordersection')
        self.OrderSection.heading.setObjectName("ordersection-heading")
        self.Orders = QFrame(objectName='dashboard-ordersection-sub1')
        self.Orders.setLayout(QGridLayout())
        self.OrdersIcon = QLabel()
        self.OrdersIcon.setPixmap(QPixmap("icons/order_1.png"))
        self.OrdersLabel = QLabel("Orders", objectName="dashboard-ordersection-label-sub1")

        self.Orders.layout().addWidget(self.OrdersIcon, 0, 0, 1, 1, Qt.AlignCenter)
        self.Orders.layout().addWidget(self.OrdersLabel, 1, 0, 1, 1, Qt.AlignCenter)

        self.OrderSection.layout.addWidget(self.Orders, 1, 0, 1, 1)


        self.StatSection = DashBoardSection(heading="Stats", objectName='dashboard-statsection')
        self.StatSection.heading.setObjectName("statsection-heading")
        self.Stats = QFrame(objectName='dashboard-statsection-sub1')
        self.Stats.setLayout(QGridLayout())
        self.StatsIcon = QLabel()
        self.StatsIcon.setPixmap(QPixmap("icons/stats_1.png"))
        self.StatsLabel = QLabel("Stats", objectName="dashboard-statsection-label-sub1")

        self.Stats.layout().addWidget(self.StatsIcon, 0, 0, 1, 1)
        self.Stats.layout().addWidget(self.StatsLabel, 1, 0, 1, 1, Qt.AlignCenter)

        self.StatSection.layout.addWidget(self.Stats, 1, 0, 1, 1)


        self.StockSection = DashBoardSection(heading="Stock", objectName='dashboard-stocksection')
        self.StockSection.heading.setObjectName("stocksection-heading")
        self.Items = QFrame(objectName='dashboard-stocksection-sub1')
        self.Items.setLayout(QGridLayout())
        self.ItemsIcon = QLabel()
        self.ItemsIcon.setPixmap(QPixmap("icons/inventory_1.png"))
        self.ItemsLabel = QLabel("Manage Items", objectName='dashboard-stocksection-label-sub1')
        self.Stocks = QFrame(objectName='dashboard-stocksection-sub2')
        self.Stocks.setLayout(QGridLayout())
        self.StocksIcon = QLabel()
        self.StocksIcon.setPixmap(QPixmap("icons/storage_1.png"))
        self.StocksLabel = QLabel("Stock", objectName='dashboard-stocksection-label-sub2')

        self.Items.layout().addWidget(self.ItemsIcon, 0, 0, 1, 1, Qt.AlignCenter)
        self.Items.layout().addWidget(self.ItemsLabel, 1, 0, 1, 1, Qt.AlignCenter)
        self.Stocks.layout().addWidget(self.StocksIcon, 0, 0, 1, 1, Qt.AlignCenter)
        self.Stocks.layout().addWidget(self.StocksLabel, 1, 0, 1, 1, Qt.AlignCenter)

        self.StockSection.layout.addWidget(self.Items, 1, 0, 1, 1)
        self.StockSection.layout.addWidget(self.Stocks, 1, 1, 1, 1)

        self.layout.addWidget(self.datetimeFrame, 0, 1, 1, 1)
        self.layout.addWidget(self.EntrySection, 0, 0, 1, 1)
        self.layout.addWidget(self.OrderSection, 1, 0, 1, 1, Qt.AlignLeft)
        self.layout.addWidget(self.StatSection, 1, 0, 1, 1, Qt.AlignRight)
        self.layout.addWidget(self.StockSection, 1, 1, 1, 1)

        # self.ActiveEntry.mouseReleaseEvent = lambda event: self.on_release(event, self.ActiveEntry)
        # self.EntryHistory.mouseReleaseEvent = lambda event: self.on_release(event, self.EntryHistory)
        # self.Orders.mouseReleaseEvent = lambda event: self.on_release(event, self.Orders)
        # self.Stats.mouseReleaseEvent = lambda event: self.on_release(event, self.Stats)

        self.ActiveEntry.mousePressEvent = lambda event: self.on_click(event, self.ActiveEntry)
        self.EntryHistory.mousePressEvent = lambda event: self.on_click(event, self.EntryHistory)
        self.Orders.mousePressEvent = lambda event: self.on_click(event, self.Orders)
        self.Stats.mousePressEvent = lambda event: self.on_click(event, self.Stats)
        self.Items.mousePressEvent = lambda event: self.on_click(event, self.Items)
        self.Stocks.mousePressEvent = lambda event: self.on_click(event, self.Stocks)

    def show_time(self):
        try:
            while True:
                now = datetime.datetime.now()
                self.timelabel.setText(now.strftime("%I:%M"))
                self.time_p_label.setText(now.strftime("%p"))
                self.datelabel.setText(now.strftime("%d/%m/%Y"))
                self.daylabel.setText(now.strftime("%A"))
        except RuntimeError:
            return

    def on_click(self, event, from_):
        if from_ == self.ActiveEntry:
            self.entrywindow.show()
            self.entries.show()

        elif from_ == self.Items:
            self.itemswindow.show()
        elif from_ == self.Stocks:
            self.stockwindow.show()
        elif from_ == self.EntryHistory:
            self.entryhistorywindow.show()
        else:
            messagebox = QMessageBox()
            messagebox.setWindowTitle("OOPS :(")
            messagebox.setText("This Feature is Under Development")
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.exec_()

class EntryListItem(QFrame):
    def __init__(self, vname, vnum, vdate, entryid, showframe):
        QFrame.__init__(self, objectName='entrylistitem')
        self.setMinimumWidth(280)

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        # self.layout.setAlignment(Qt.AlignTop)
        self.layout.setVerticalSpacing(5)

        self.vname = QLabel(vname, objectName='entrylistitem-vname')
        self.vnum = QLabel(vnum, objectName='entrylistitem-vnum')
        self.vdate = QLabel(vdate, objectName='entrylistitem-vdate')
        self.entryid = entryid

        self.layout.addWidget(self.vname, 0, 0, 1, 1)
        self.layout.addWidget(self.vnum, 1, 0, 1, 1)
        self.layout.addWidget(self.vdate, 2, 0, 1, 1)

        self.showframe = showframe
        self.mousePressEvent = lambda event: self.on_click()

    def on_click(self):
        self.showframe.infoframe.hide()
        self.showframe.mainframe.show()
        self.showframe.itemsTable.show()
        if self.showframe.activeEntryListItem is not None:
            self.showframe.activeEntryListItem.setStyleSheet("border-right: 0px solid #55f")
        self.showframe.activeEntryListItem = self
        self.setStyleSheet("""
            border: 0px;
            background-color: #efefff;
        """)
        self.vname.setStyleSheet("border: none; border-radius: none")
        self.vnum.setStyleSheet("border: none; border-radius: none")
        self.vdate.setStyleSheet("border: none; border-radius: none")
        self.showframe.vname_heading.setText(f'{self.vname.text()}')
        self.showframe.vnum_heading.setText(self.vnum.text())

        data = DataMethods.get_data("data")
        entrydata = DataMethods.get_data("./Records/entries")
        entry = entrydata[self.entryid]
        self.showframe.itemsTable.setRowCount(len(entry['items']))


        for index, item in enumerate(entry['items'], 0):
            itemName = QTableWidgetItem(item[0])
            # itemFont = QFont("Regular")
            # itemFont.setBold(False)
            # itemFont.setPixelSize(17)
            # itemFont.setWeight(1)
            # itemName.setFont(itemFont)
            # itemName.setForeground(QBrush(QColor(50, 50, 255)))
            # itemName.setTextAlignment(Qt.AlignLeft)
            # itemName.setFlags(Qt.ItemIsEnabled)
            itemQuantity = QTableWidgetItem(str(item[1]))
            itemPrice = QTableWidgetItem(str(item[2]))
            # itemQuantity.setTextAlignment(Qt.AlignCenter)
            self.showframe.itemsTable.setItem(index, 0, itemName)
            self.showframe.itemsTable.setItem(index, 1, itemQuantity)
            self.showframe.itemsTable.setItem(index, 2, itemPrice)
        self.showframe.set_table_buttons()
        self.showframe.set_table_style()
        

class EntryShowFrame(QFrame):
    def __init__(self):
        QFrame.__init__(self, objectName='entryshowframe')
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.layout.setContentsMargins(0, 0, 0, 0)

        stock_data = DataMethods.get_data("./Records/stock")
        parts_data = DataMethods.get_data("./Records/data_items")

        self.mainframe = QFrame()
        self.mainframe.setLayout(QGridLayout())
        self.mainframe.hide()

        self.infoframe = QFrame()
        self.infoframe.setLayout(QGridLayout())
        # self.infoframe.hide()

        self.vname_heading = QLabel("Vehicle", objectName='vname-heading')
        self.vnum_heading = QLabel("Number", objectName='vnum-heading')
        self.item_heading = QLabel("Items", objectName='items-heading')


        self.partselectbox = QComboBox(objectName='part-select-box')
        self.partselectbox.setEditable(True)
        self.partselectbox.addItems(sorted([part for part in parts_data['Parts']]))
        self.partselectbox.setInsertPolicy(QComboBox.NoInsert)

        self.itemselectbox = QComboBox(objectName='item-select-box')
        self.itemselectbox.setMaximumWidth(500)
        self.itemselectbox.setMinimumWidth(501)

        self.itempricebox = QDoubleSpinBox(objectName='item-price-box')
        self.itempricebox.setRange(1, 99999)
        self.itempricebox.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.part_selected()
        self.partselectbox.currentIndexChanged.connect(self.part_selected)
        self.itemselectbox.currentIndexChanged.connect(self.item_changed)

        self.itemAddButton = QPushButton(objectName='item-add-button')
        self.itemAddButton.clicked.connect(self.add_item)
        self.itemDeleteButton = QPushButton(objectName='item-delete-button')
        self.itemDeleteButton.clicked.connect(self.remove_item)
        
        # itemsdata = DataMethods.get_data("./Records/items")
        # self.itemSearchBar.setCompleter(QCompleter(map(str, itemsdata.keys())))

        # self.itemsTableFrame = QFrame()
        # self.itemsTableFrame.setLayout(QGridLayout())
        # self.itemsTableFrame.layout().setContentsMargins(0, 0, 0, 0)
        self.itemsTable = QTableWidget(objectName='items-table')
        self.itemsTable.setMinimumWidth(715)
        self.itemsTable.setMinimumHeight(300)
        self.itemsTable.setColumnCount(6)
        self.itemsTable.setHorizontalHeaderLabels(['Item', 'Quantity', 'Amount', "", "", ""])
        self.itemsTable.itemChanged.connect(self.on_entry_change)
        self.itemsTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.itemsTable.verticalScrollBar().setObjectName("items-table-vscrollbar")
        self.tableIsSet = False
        # self.itemsTable.setShowGrid(False)
        # self.itemsTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.item_stat_frame = QFrame()
        self.item_stat_frame.setLayout(QGridLayout())

        self.total_price_label = QLabel("Total: ")

        self.item_stat_frame.layout().addWidget(self.total_price_label, 0, 0, 1, 1, Qt.AlignRight)


        self.entryCheckoutButton = QPushButton("Checkout", objectName='entry-checkout-button')
        self.entryCheckoutButton.clicked.connect(self.checkout)

        # self.itemsTable.verticalHeader().set
        self.itemsTable.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)
        self.itemsTable.horizontalHeader().setSectionResizeMode(4, QHeaderView.Fixed)
        self.itemsTable.setColumnWidth(0, 450)
        self.itemsTable.setColumnWidth(1, 100)
        self.itemsTable.setColumnWidth(2, 150)
        self.itemsTable.setColumnWidth(3, 50)
        self.itemsTable.setColumnWidth(4, 50)
        self.itemsTable.setColumnWidth(5, 60)
        self.itemsTable.hide()

        self.activeEntryListItem = None

        self.layout.addWidget(self.mainframe, 0, 0, 1, 1)
        self.layout.addWidget(self.infoframe, 0, 0, 1, 1)

        self.mainframe.layout().addWidget(self.vname_heading, 0, 0, 1, 5, Qt.AlignCenter | Qt.AlignTop)
        self.mainframe.layout().addWidget(self.vnum_heading, 1, 0, 1, 5, Qt.AlignCenter)
        self.mainframe.layout().addWidget(self.item_heading, 2, 0, 1, 1)
        self.mainframe.layout().addWidget(self.partselectbox, 3, 0, 1, 1)
        self.mainframe.layout().addWidget(self.itemselectbox, 3, 1, 1, 1)
        self.mainframe.layout().addWidget(self.itempricebox, 3, 2, 1, 1)
        self.mainframe.layout().addWidget(self.itemAddButton, 3, 3, 1, 1)
        self.mainframe.layout().addWidget(self.itemDeleteButton, 3, 4, 1, 1)
        self.mainframe.layout().addWidget(self.itemsTable, 4, 0, 1, 5, Qt.AlignTop)
        self.mainframe.layout().addWidget(self.item_stat_frame, 5, 0, 1, 5)
        self.mainframe.layout().addWidget(self.entryCheckoutButton, 6, 0, 1, 5, Qt.AlignRight)
    
    def set_table_buttons(self):
        for row in range(self.itemsTable.rowCount()):
            increment_button = QPushButton("+", objectName='entry-item-increment-button')
            decrement_button = QPushButton("-", objectName='entry-item-decrement-button')
            delete_button = QPushButton("X", objectName='entry-item-delete-button')
            increment_button.clicked.connect(lambda: self.change_quantity("increment"))
            decrement_button.clicked.connect(lambda: self.change_quantity("decrement"))
            delete_button.clicked.connect(self.remove_item)
            self.itemsTable.setCellWidget(row, 3, increment_button)
            self.itemsTable.setCellWidget(row, 4, decrement_button)
            self.itemsTable.setCellWidget(row, 5, delete_button)

    def set_table_style(self):
        for row in range(self.itemsTable.rowCount()):
            for col in range(self.itemsTable.columnCount() - 3):
                item = self.itemsTable.item(row, col)
                if col == 0:
                    font = QFont("Regular", 12)
                    font.setWeight(100)
                    item.setTextAlignment(Qt.AlignLeft)
                    item.setForeground(QBrush(QColor(50, 50, 255)))
                    item.setFlags(Qt.ItemIsEnabled)
                    item.setFont(font)
                else:
                    font = QFont("Regular", 12)
                    font.setWeight(75)
                    item.setTextAlignment(Qt.AlignCenter)
                    item.setForeground(QBrush(QColor(50, 50, 255)))
                    item.setFont(font)

    def change_quantity(self, type_):
        row = self.itemsTable.currentRow()
        item = self.itemsTable.item(row, 0).text()

        entrydata = DataMethods.get_data("./Records/entries")
        stock_data = DataMethods.get_data("./Records/stock")
        data = DataMethods.get_data("data")

        entryid = self.activeEntryListItem.entryid
        
        perprice = int(entrydata[entryid]['items'][row][2] / entrydata[entryid]['items'][row][1])

        if type_ == 'increment':
            # if fetch[0]['quantity'] - 1 < 1:
            #     data['active_removed_stocks'].append(fetch[0])
            #     del stock_data[fetch[2]][fetch[1]]
            #     DataMethods.put_data(stock_data, "./Records/stock")
            #     return
            # stock_data[part_name][index]['quantity'] -= 1

            if not self.fetch_stock_from_table(item, -1):
                return
            entrydata[entryid]['items'][row][1] += 1
            entrydata[entryid]['items'][row][2] += perprice
        else:
            if entrydata[entryid]['items'][row][1] - 1 == 0:
                self.remove_item()
                return
            
            if not self.fetch_stock_from_table(item, 1):
                return

            # stock_data[fetch[2]][fetch[1]]['quantity'] += 1
            # else:
            #     items = [(i['vehicle'], i['part_no']) for i in data['active_removed_stocks']]
            #     if (fetch[0]['vehicle'], fetch[0]['part_no']) in items:
            #         del data['active_removed_stocks'][items.index(fetch[0]['vehicle'], fetch[0]['part_no'])]

                DataMethods.put_data(stock_data, "./Records/stock")
            entrydata[entryid]['items'][row][1] -= 1
            entrydata[entryid]['items'][row][2] -= perprice
        item = QTableWidgetItem(str(entrydata[entryid]['items'][row][1]))
        itemprice = QTableWidgetItem(str(entrydata[entryid]['items'][row][2]))
        self.itemsTable.setItem(row, 1, item)
        self.itemsTable.setItem(row, 2, itemprice)
        DataMethods.put_data(entrydata, "./Records/entries")
        self.check_total()
        self.set_table_style()
        

    def on_entry_change(self, item):
        entrydata = DataMethods.get_data("./Records/entries")
        stock_data = DataMethods.get_data("./Records/stock")
        data = DataMethods.get_data("data")
        entryid = self.activeEntryListItem.entryid
        current_entry = entrydata[entryid]
        partitem = self.itemsTable.item(item.row(), 0).text()
        if item.column() == 1:

            if not item.text().isnumeric() or int(item.text()) < 1:
                old = QTableWidgetItem(str(current_entry['items'][item.row()][1]))
                self.itemsTable.setItem(item.row(), item.column(), old)
                self.set_table_style()
                return


            old = int(current_entry['items'][item.row()][1])
            new = int(item.text())
            if old-new == 0:
                return

            if not self.fetch_stock_from_table(partitem, int(-(new - old))):
                return

            DataMethods.put_data(stock_data, "./Records/stock")

            entrydata[entryid]['items'][item.row()][1] = int(item.text())
            self.check_total()

        elif item.column() == 2:
            try: 
                float(item.text())
                
            except: 
                old = QTableWidgetItem(str(current_entry['items'][item.row()][2]))
                self.itemsTable.setItem(item.row(), item.column(), old)
                self.set_table_style()
                return

            entrydata[entryid]['items'][item.row()][2] = float(item.text())
        DataMethods.put_data(entrydata, "./Records/entries")

        

        self.check_total()


    def part_selected(self):
        
        self.itemselectbox.clear()
        part = self.partselectbox.currentText()

        stock_data = DataMethods.get_data("./Records/stock")

        if part not in stock_data.keys():
            return
        for item in stock_data[part]:
            print(part)
            print(item)
            self.itemselectbox.addItem(f'{" | ".join([part, item["vehicle"], item["part_no"]])}')

    def item_changed(self):
        item = self.itemselectbox.currentText().split(" | ")
        if item[0] == "": return
        itemname = item[0]
        itemveh = item[1]
        item_no = "" if len(item) < 3 else item[2]
        part = self.partselectbox.currentText()


        stock_data = DataMethods.get_data("./Records/stock")
        for i in stock_data[itemname]:
            if i['vehicle'] == itemveh and i['part_no'] == item_no:
                self.itempricebox.setValue(i['mrp'])
                break
        else:
            self.itempricebox.setValue(1)


    def add_item(self):
        item = self.itemselectbox.currentText()
        price = self.itempricebox.value()
        entrydata = DataMethods.get_data("./Records/entries")
        stock_data = DataMethods.get_data("./Records/stock")


        item_names = [item_name[0] for item_name in entrydata[self.activeEntryListItem.entryid]['items']]
        # stock_check
        # if fetch[-1]:
        #     if fetch[0]["quantity"] -1 < 1:
        #         maindata['active_removed_stocks'].append(fetch[0])
        #         del stock_data[fetch[2]][fetch[1]]
        #     else:
        #         stock_data[fetch[2]][fetch[1]]["quantity"] -= 1

        if not self.fetch_stock_from_table(item, -1):
            return



        if item in item_names:
            itemindex = item_names.index(item)
            entrydata[self.activeEntryListItem.entryid]['items'][itemindex][1] += 1
            entrydata[self.activeEntryListItem.entryid]['items'][itemindex][2] += float(price)
            DataMethods.put_data(entrydata, "./Records/entries")
            tableitem = QTableWidgetItem(str(entrydata[self.activeEntryListItem.entryid]['items'][itemindex][1]))
            tableitem.setTextAlignment(Qt.AlignCenter)
            priceitem = QTableWidgetItem(str(entrydata[self.activeEntryListItem.entryid]['items'][itemindex][2]))
            self.itemsTable.setItem(itemindex, 1, tableitem)
            self.itemsTable.setItem(itemindex, 2, priceitem)

        else:
            self.itemsTable.setRowCount(self.itemsTable.rowCount() + 1)
            itemname = QTableWidgetItem(item)
            itemqty = QTableWidgetItem("1")
            itemprice = QTableWidgetItem(str(price))

            # itemqty.setStyleSheet("font-size: 20px")
            itemqty.setTextAlignment(Qt.AlignCenter)
            entrydata[self.activeEntryListItem.entryid]['items'].append((item, 1, price))
            DataMethods.put_data(entrydata, "./Records/entries")
            # self.itemsTable.insertRow(self.itemsTable.rowCount())s
            self.itemsTable.setItem(self.itemsTable.rowCount() - 1, 0, itemname)
            self.itemsTable.setItem(self.itemsTable.rowCount() - 1, 1, itemqty)
            self.itemsTable.setItem(self.itemsTable.rowCount() - 1, 2, itemprice)
        # self.itemsTable.setItem(0, 1, QTableWidgetItem("5"))
        

        self.set_table_buttons()
        self.set_table_style()
        self.check_total()

    def remove_item(self):


        messagebox = QMessageBox()
        messagebox.setWindowTitle("Delete Item?")
        messagebox.setText("Are you sure you want to delete this item?")
        messagebox.setIcon(QMessageBox.Warning)
        messagebox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)

        if messagebox.exec_() != QMessageBox.Yes:
            return

        stock_data = DataMethods.get_data("./Records/stock")
        data = DataMethods.get_data("data")
        current_row = self.itemsTable.currentRow()
        
        
        if current_row == -1:
            return

        item = self.itemsTable.item(current_row, 0).text()
        remain = int(self.itemsTable.item(current_row, 1).text())

        # if not fetch[-1]:
        #     if (fetch[0], fetch[1]) in [(i['vehicle'], i['part_no']) for i in data['active_removed_stocks']:
        #         ix = [(i['vehicle'], i['part_no']) for i in data['active_removed_stocks'].index((fetch[0], fetch[1]))
        #         stock_data[fetch['quantity'] += remain
        #         stock_data[fetch[2]].append(fetch[0])
        #     else:
        #         stock_data[fetch[2]][fetch[1]]['quantity'] += remain

        if not self.fetch_stock_from_table(item, remain):
            return
        entrydata = DataMethods.get_data("./Records/entries")

        del entrydata[self.activeEntryListItem.entryid]['items'][current_row]
        self.itemsTable.removeRow(current_row)

        DataMethods.put_data(entrydata, "./Records/entries")


        self.check_total()

    def check_total(self):
        entrydata = DataMethods.get_data("./Records/entries")
        entryid = self.activeEntryListItem.entryid

        total = 0
        for index in range(len(entrydata[entryid]['items'])):
            price = entrydata[entryid]['items'][index][2]
            total += price
        entrydata[entryid]['totalamount'] = total
        self.total_price_label.setText(str(total))

        DataMethods.put_data(entrydata, "./Records/entries")


    def checkout(self):

        confirmbox = QMessageBox()
        confirmbox.setText("Are you sure you want to save and checkout this entry?")
        confirmbox.setWindowTitle("Checkout")
        confirmbox.setGeometry(600, 300, 300, 300)
        confirmbox.setIcon(QMessageBox.Warning)
        confirmbox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)

        if confirmbox.exec_() != QMessageBox.Yes:
            return
        
        data = DataMethods.get_data("data")
        entrydata = DataMethods.get_data("./Records/entries")

        data['active_entries'].remove(self.activeEntryListItem.entryid)
        entrydata[self.activeEntryListItem.entryid]['state'] = 'closed'
        self.activeEntryListItem.deleteLater()
        self.activeEntryListItem = None

        dialog = QDialog(objectName='entry-checkout-result-window')
        dialog.setLayout(QGridLayout())
        dialog.layout().setAlignment(Qt.AlignCenter)
        dialog.setGeometry(600, 300, 300, 100)
        dialog.setWindowFlags(Qt.FramelessWindowHint)

        result = QLabel("Checkout Done!", objectName='entry-checkout-result-text')
        doneimg = QLabel()
        doneimg.setPixmap(QPixmap("./icons/green_tick.png"))
        doneimg.setMaximumWidth(50)
        doneimg.setMaximumHeight(50)

        dialog.layout().addWidget(result, 1, 0, 1, 1, Qt.AlignCenter)
        dialog.layout().addWidget(doneimg, 0, 0, 1, 1, Qt.AlignCenter)
        Thread(target=lambda: (time.sleep(2), dialog.close()), daemon=True).start() 
        dialog.exec_()


    def fetch_stock_from_table(self, itemstring, quantity):
        if itemstring == '': 
            messagebox = QMessageBox()
            messagebox.setWindowTitle("Choose an Item")
            messagebox.setText("Choose an Item To Add")
            messagebox.setIcon(QMessageBox.Information)
            messagebox.setStandardButtons(QMessageBox.Ok)
            messagebox.exec_()
            return

        item = itemstring.split(" | ")
        part = item[0]
        itemveh = item[1]
        item_no = "" if len(item) < 3 else item[2]

        stock_data = DataMethods.get_data("./Records/stock")
        data = DataMethods.get_data("data")
        res = ""

        for index, i in enumerate(stock_data[part], 0):
            if i['vehicle'] == itemveh and i['part_no'] == item_no:
                remain = i['quantity'] + quantity
                if remain == 0:
                    print("1")

                    data['active_removed_stocks'].append(i)
                    del stock_data[part][index]
                    res = True
                    break
                elif remain < 0:
                    res = False
                    break
                elif remain >= 1:
                    stock_data[part][index]['quantity'] += quantity
                    res = True
                    break
        else:
            for index, i in enumerate(data['active_removed_stocks'], 0):
                if i['vehicle'] == itemveh and i['part_no'] == item_no:
                    if quantity > 0:
                        stock_data[part].append(i)
                        data['active_removed_stocks'].remove(i)
                        res = True
                        break
                    else:
                        return False
        DataMethods.put_data(stock_data, "./Records/stock")
        DataMethods.put_data(data, "data")
        self.part_selected()
        return res

        #         return [i, index, part, True]
        # return return[itemveh, item_no, False]



class NewEntryWindow(QWidget):
    def __init__(self, entries):
        QWidget.__init__(self, objectName='new-entry-widget')

        self.setGeometry(450, 150, 500, 500)
        self.setWindowTitle("New Entry")

        data = DataMethods.get_data("./Records/data_items")

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(10, 0, 10, 10)
        self.layout.setAlignment(Qt.AlignTop)

        self.entries = entries
        self.entries.new_entry_window = self

        self.heading = QLabel("New Entry", objectName="new-entry-heading")
        self.vname_label = QLabel("Vehicle Name: ", objectName='new-entry-vname-label')
        self.vname_edit = QComboBox(objectName='new-entry-vname-edit')
        self.vnum_label = QLabel("Vehicle Number: ", objectName='new-entry-vnum-label')
        self.vnum_edit = QLineEdit(objectName='new-entry-vnum-edit')
        self.vnum_edit.textChanged.connect(self.on_num_type)
        self.cinfo_label = QLabel("Customer Info", objectName='new-entry-cinfo-label')
        self.cinfo_edit = QPlainTextEdit(objectName='new-entry-cinfo-edit')
        self.date_label = QLabel("Date: ", objectName='new-entry-date-label')
        self.date_edit = QDateEdit(objectName='new-entry-date-edit')
        self.date_edit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.create_button = QPushButton("Create", objectName='new-entry-create-button')
        self.create_button.clicked.connect(self.create_entry)

        self.vname_edit.addItems([item for item in data["Vehicles"]])
        self.vname_edit.setEditable(True)
        self.vname_edit.setInsertPolicy(QComboBox.NoInsert)

        now = datetime.datetime.now()
        day = int(now.strftime("%d"))
        month = int(now.strftime("%m"))
        year = int(now.strftime("%Y"))
        date = QDate(year, month, day)
        self.date_edit.setDate(date)
        

        self.layout.addWidget(self.heading, 0, 0, 1, 2, Qt.AlignCenter)
        self.layout.addWidget(self.vname_label, 1, 0, 1, 1)
        self.layout.addWidget(self.vname_edit, 1, 1, 1, 1)
        self.layout.addWidget(self.vnum_label, 2, 0, 1, 1)
        self.layout.addWidget(self.vnum_edit, 2, 1, 1, 1)
        self.layout.addWidget(self.cinfo_label, 3, 0, 1, 1)
        self.layout.addWidget(self.cinfo_edit, 3, 1, 1, 1)
        self.layout.addWidget(self.date_label, 4, 0, 1, 1)
        self.layout.addWidget(self.date_edit, 4, 1, 1, 1)
        self.layout.addWidget(self.create_button, 5, 1, 1, 1, Qt.AlignRight)

    def on_num_type(self):
        new = self.vnum_edit.text()
        if len(new) < 1:
            return
        elif new[-1] != " " and new[-1].islower():
            new = list(new)
            new[-1] = new[-1].upper()
            new = "".join(new)
            self.vnum_edit.setText(new)

    def create_entry(self):
        entrydata = DataMethods.get_data("./Records/entries")
        record_data = DataMethods.get_data("./Records/record")
        data = DataMethods.get_data("data")
        items_data = DataMethods.get_data("./Records/data_items")

        vname = self.vname_edit.currentText()
        vnum = self.vnum_edit.text()
        cinfo = self.cinfo_edit.toPlainText()
        date = self.date_edit.date()
        date = f"{date.day()}-{date.month()}-{date.year()}"
        

        messagebox = QMessageBox()
        messagebox.setGeometry(600, 300, 300, 300)
        messagebox.setStandardButtons(QMessageBox.Ok)
        messagebox.setIcon(QMessageBox.Information)
        

        if vname not in items_data["Vehicles"]:
            messagebox.setText(f"Unknown Vehicle '{vname}'")
            messagebox.setWindowTitle("Unknown Vehicle")
            messagebox.exec_()
            return

        if "" in [vnum, cinfo]:
            messagebox.setText("Fill Empty Fields")
            messagebox.setWindowTitle("Empty Fields Found")
            messagebox.exec_()
            return

        entryid = str(len(entrydata.keys()) + 1)
        entrydata[str(entryid)] = {
            "vname": vname,
            "vnum": vnum,
            "customerinfo": cinfo,
            "items": [],
            "totalamount": 0,
            "date": date,
            "state": "active"
        }

        if date in record_data.keys():
            record_data[date].append(entryid)
        else:
            record_data[date] = [entryid]

        data['active_entries'].append(entryid)

        DataMethods.put_data(entrydata, "./Records/entries")
        DataMethods.put_data(record_data, "./Records/record")
        DataMethods.put_data(data, "data")

        item = EntryListItem(vname, vnum, date, entryid, self.entries.entryshow)
        self.entries.entrylist.layout().addWidget(item)
        self.close()


class ActiveEntries(QFrame):
    def __init__(self):
        QFrame.__init__(self)

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setAlignment(Qt.AlignTop)
        self.layout.setContentsMargins(5, 0, 0, 10)
        self.layout.setVerticalSpacing(0)
        self.layout.setHorizontalSpacing(0)
        # self.setStyleSheet("background: white")


        self.entrylistarea = QScrollArea(objectName='entrylistarea')
        self.entrylistarea.setFrameStyle(0)
        self.entrylistarea.verticalScrollBar().setObjectName("entrylistarea-vscrollbar")
        self.entrylistarea.setWidgetResizable(True)
        self.entrylist = QFrame(objectName='entrylistframe')
        self.entrylist.setLayout(QGridLayout())
        self.entrylist.layout().setVerticalSpacing(0)
        self.entrylist.layout().setAlignment(Qt.AlignCenter | Qt.AlignTop)
        # self.entrylist.layout().setContentsMargins(0, 0, 0, 0)

        self.entryshow = EntryShowFrame()

        self.entrylist_search_frame = QFrame(objectName='entrylist-heading-frame')
        self.entrylist_search_frame.setLayout(QGridLayout())
        self.entrylist_searchbar = QLineEdit(objectName='entrylist-searchbar')
        self.entrylist_searchbar.setMaximumWidth(200)
        self.entry_add_button = QPushButton(objectName='entrylist-add-btn')
        self.entry_add_button.setMaximumWidth(32)
        self.entry_add_button.clicked.connect(self.create_new_entry)
        self.entry_remove_button = QPushButton(objectName='entrylist-remove-btn')
        self.entry_remove_button.setMaximumWidth(32)
        self.entry_remove_button.clicked.connect(self.delete_entry)

        self.entrylist_search_frame.layout().addWidget(self.entrylist_searchbar, 0, 0, 1, 1)
        self.entrylist_search_frame.layout().addWidget(self.entry_add_button, 0, 1, 1, 1)
        self.entrylist_search_frame.layout().addWidget(self.entry_remove_button, 0, 2, 1, 1)
        self.entrylist_search_frame.layout().setContentsMargins(10, 0, 10, 0)
        # self.entrylist.layout().addWidget(self.heading, 0, 0, 1, 1, Qt.AlignCenter)

        data = DataMethods.get_data("data")
        entries = DataMethods.get_data("./Records/entries")


        for i in data['active_entries']:
            entry = entries[i]
            item = EntryListItem(entry['vname'], entry['vnum'], entry['date'], i, self.entryshow)
            # item.mousePressEvent = lambda event: self.on_entry_selection(event, item)
            self.entrylist.layout().addWidget(item)
        
        self.entrylistarea.setWidget(self.entrylist)
        self.entrylistarea.setMaximumWidth(300)
        self.entrylistarea.setContentsMargins(0, 0, 0, 0)
        self.entrylist.layout().setContentsMargins(0, 0, 0, 0)
    
        self.layout.addWidget(self.entrylist_search_frame, 0, 0, 1, 1, Qt.AlignCenter)
        self.layout.addWidget(self.entrylistarea, 1, 0, 1, 1)
        self.layout.addWidget(self.entryshow, 0, 1, 2, 1)

    def on_entry_selection(self, event, frame):
        frame.setStyleSheet("border-right: 5px solid #5555ff")

    def create_new_entry(self):
        self.new_entry_window.show()

    def delete_entry(self):
        messagebox = QMessageBox()
        messagebox.setText("Are you sure want to delete this entry?")
        messagebox.setWindowTitle("Delete Entry?")
        messagebox.setIcon(QMessageBox.Warning)
        messagebox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)

        if messagebox.exec_() == QMessageBox.Yes:
            self.entryshow.activeEntryListItem.deleteLater()
            data = DataMethods.get_data("data")
            data['active_entries'].remove(self.entryshow.activeEntryListItem.entryid)
            DataMethods.put_data(data, "data")
            self.entryshow.activeEntryListItem = None


class SubWindow(QWidget):
    def __init__(self, title):
        QWidget.__init__(self)

        self.setGeometry(0, 0, screen_rect.width() - 10, screen_rect.height()-70)
        self.setWindowTitle(title)
        self.setFixedSize(screen_rect.width() - 10, screen_rect.height()-70)
        self.hide()


class ItemsWindowLayout(QGridLayout):
    def __init__(self):
        QGridLayout.__init__(self)

        self.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        self.heading = QLabel("Manage Items", objectName='itemswindow-heading')
        self.typebox = QComboBox(objectName='itemswindow-typebox')
        self.searchbar = QLineEdit(objectName='itemswindow-searchbar')
        self.searchbar.setPlaceholderText("Search Items")
        self.itemAddButton = QPushButton("Add Item", objectName='itemswindow-item-add-button')
        self.itemAddButton.setIcon(QIcon("./icons/plus_1.png"))
        self.itemRemoveButton = QPushButton("Remove Item", objectName='itemswindow-item-remove-button')
        self.itemRemoveButton.setIcon(QIcon("./icons/minus_1.png"))
        self.itemsList = QListWidget(objectName='itemswindow-itemslist')
        self.itemsList.setFocusPolicy(Qt.NoFocus)

        self.itemAddButton.clicked.connect(self.pop_item_dialog)
        self.itemRemoveButton.clicked.connect(self.delete_item)
        self.searchbar.textChanged.connect(self.search_item)
        self.typebox.currentIndexChanged[str].connect(lambda item: self.type_changed(item))

        self.currentType = "Parts"

        self.typebox.addItem("Parts")
        self.typebox.addItem("Vehicles")
        self.typebox.addItem("Brands")

        self.dialogOpen = False

        self.noiteminfo = QLabel("No Items")
        self.noiteminfo.hide()


        self.type_changed(self.currentType)
        # itemsdata = DataMethods.get_data("./Records/data_items")

        # for item in itemsdata['items']:
        #     self.itemsList.addItem(item)
        # if self.itemsList.count() < 1:
        #     self.itemsList.hide()
        #     self.noiteminfo.show()


        self.addWidget(self.heading, 0, 0, 1, 4, Qt.AlignCenter)
        self.addWidget(self.typebox, 1, 0, 1, 1)
        self.addWidget(self.searchbar, 1, 1, 1, 1)
        self.addWidget(self.itemAddButton, 1, 2, 1, 1)
        self.addWidget(self.itemRemoveButton, 1, 3, 1, 1)
        self.addWidget(self.noiteminfo, 2, 0, 1, 1)
        self.addWidget(self.itemsList, 2, 0, 1, 4)

    def type_changed(self, item):
        self.currentType = item
        self.itemsList.clear()
        data = DataMethods.get_data("./Records/data_items")

        for i in data[self.currentType]:
            self.itemsList.addItem(i)


    def pop_item_dialog(self, parent):

        if self.dialogOpen is True:
            return

        dialog = QFrame(objectName='pop-item-dialogframe')
        # dialog.setGeometry(500, 200, 200, 100)
        dialog.move(100, 100)

        dialog.setLayout(QGridLayout())
        dialog.layout().setAlignment(Qt.AlignCenter)


        namefield = QLineEdit(objectName='item-add-namefield')
        namefield.setPlaceholderText("Enter New Item Name")
        namefield.returnPressed.connect(lambda: self.add_item(namefield.text(), namefield))
        # button_frame = QFrame()
        # button_frame.setLayout(QGridLayout())
        # button_frame.layout().setAlignment(Qt.AlignRight)

        confirm_button = QPushButton("OK", objectName='item-add-confirm-btn')
        confirm_button.clicked.connect(lambda: self.add_item(namefield.text(), namefield))

        cancel_button = QPushButton("Cancel", objectName='item-add-cancel-btn')
        cancel_button.clicked.connect(lambda: self.close_dialog(dialog))

        # button_frame.layout().addWidget(confirm_button, 1, 1, 1, 1)
        # button_frame.layout().addWidget(cancel_button, 1, 0, 1, 1)


        dialog.layout().addWidget(namefield, 0, 0, 1, 2, Qt.AlignLeft)
        dialog.layout().addWidget(confirm_button, 1, 1, 1, 1)
        dialog.layout().addWidget(cancel_button, 1, 0, 1, 1)

        # dialog.layout().addWidget(button_frame, 1, 0, 1, 1)

        graphics = QGraphicsDropShadowEffect()
        graphics.setBlurRadius(20)
        graphics.setOffset(4, 2)
        dialog.setGraphicsEffect(graphics)

        self.addWidget(dialog, 2, 2, 1, 2, Qt.AlignTop | Qt.AlignLeft)
        self.dialogOpen = True
        # dialog.move(100, 100)

    def close_dialog(self, dialog):
        dialog.close()
        self.dialogOpen = False


    def add_item(self, item, namefield):

        if item == '':
            messagebox = QMessageBox()
            messagebox.setText("Item Name Cant Be Empty")
            messagebox.setStandardButtons(QMessageBox.Ok)
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Empty Item Name")
            messagebox.exec_()
            return

        
        data_items = DataMethods.get_data("./Records/data_items")
        stock_data = DataMethods.get_data("./Records/stock")

        if item in data_items[self.currentType]:
            messagebox = QMessageBox()
            messagebox.setText("'{}' Already Exists!".format(item))
            messagebox.setStandardButtons(QMessageBox.Ok)
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Item Exists")
            messagebox.exec_()
            namefield.setText("")
            return

        data_items[self.currentType].append(item.strip())
        stock_data[item] = []

        DataMethods.put_data(data_items, "./Records/data_items")
        DataMethods.put_data(stock_data, "./Records/stock")

        self.itemsList.clear()
        for i in sorted(data_items[self.currentType]):
            self.itemsList.addItem(i)
        namefield.setText("")

    def delete_item(self):
        to_delete = self.itemsList.currentRow()

        if self.itemsList.item(to_delete) is None:
            errobox = QMessageBox()
            errobox.setText("Choose An Item To Delete")
            errobox.setWindowTitle("Cant Remove Item")
            errobox.setStandardButtons(QMessageBox.Ok)
            errobox.setIcon(QMessageBox.Warning)
            errobox.exec_()
            return

        messagebox = QMessageBox()
        messagebox.setWindowTitle("Delete Item?")
        messagebox.setText("Are You Sure You Want To Delete '{}' ?".format(self.itemsList.item(to_delete).text()))
        messagebox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)

        if messagebox.exec_() == QMessageBox.Yes:
            data = DataMethods.get_data("./Records/data_items")
            stock_data = DataMethods.get_data("./Records/stock")

            data[self.currentType].remove(self.itemsList.item(to_delete).text())
            if self.currentType == "Parts": del stock_data[self.itemsList.item(to_delete).text()]

            DataMethods.put_data(data, "./Records/data_items")
            self.itemsList.takeItem(to_delete)


    def search_item(self):
        kword = self.searchbar.text().lower()
        data = DataMethods.get_data("./Records/data_items")

        if kword == "":
            self.itemsList.clear()
            for item in sorted(data[self.currentType]):
                self.itemsList.addItem(item)
            return
        self.itemsList.clear()
        for item in sorted(data[self.currentType]):
            i = item.lower()
            if True in [i.startswith(kword), kword in i, i.endswith(kword), i == kword]:
                self.itemsList.addItem(item)


class StockItem(QFrame):
    def __init__(self, stockshowframe):
        QFrame.__init__(self)

        self.setObjectName("stock-item")
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.setMinimumWidth(646)
        self.setMaximumWidth(646)
        self.setMinimumHeight(100)
        self.setMaximumHeight(100)

        self.stockshowframe = stockshowframe

        self.itemName = QLabel(objectName='stock-item-name')
        self.itemCount = QLabel(objectName='stock-item-count')

        self.layout.addWidget(self.itemName, 0, 0, 1, 1)
        self.layout.addWidget(self.itemCount, 1, 0, 1, 1)

        self.mousePressEvent = lambda event: self.on_click()

    def on_click(self):
        self.stockshowframe.itemStockTable.setRowCount(0)

        current_item = self.stockshowframe.currentStockItem
        self.stockshowframe.itemheading.setText(self.itemName.text())
        self.stockshowframe.currentStockItem = self.itemName.text()

        stock_data = DataMethods.get_data("./Records/stock")
        header = self.stockshowframe.itemStockTable.horizontalHeader()
        
        self.stockshowframe.itemStockTable.setColumnCount(9)
        header.setSectionResizeMode(7, QHeaderView.Fixed)
        self.stockshowframe.itemStockTable.setColumnWidth(0, 170)
        self.stockshowframe.itemStockTable.setColumnWidth(1, 120)
        self.stockshowframe.itemStockTable.setColumnWidth(2, 100)
        self.stockshowframe.itemStockTable.setColumnWidth(3, 80)
        self.stockshowframe.itemStockTable.setColumnWidth(6, 30)
        self.stockshowframe.itemStockTable.setColumnWidth(7, 30)
        self.stockshowframe.itemStockTable.setColumnWidth(8, 30)
        self.stockshowframe.itemStockTable.setHorizontalHeaderLabels(["Vehicle", "Part. No", "Brand", "Quantity", "Base Price", "MRP", "", "", ""])
        
        for index, item in enumerate(stock_data[self.itemName.text()], 0):
            self.stockshowframe.itemStockTable.insertRow(self.stockshowframe.itemStockTable.rowCount())
            for colindex, val in enumerate(item.values(), 0):
                self.stockshowframe.itemStockTable.setItem(index, colindex, QTableWidgetItem(str(val)))
                self.stockshowframe.setTableButtons()
                self.stockshowframe.disable_item_edit()

class StockListFrame(QFrame):
    def __init__(self, stockshowframe):
        QFrame.__init__(self)
        self.setObjectName("stock-list-frame")

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.stock_items = QFrame(objectName='stock-items-container')
        self.stock_items.setLayout(QGridLayout())
        self.stock_items.layout().setContentsMargins(5, 5, 5, 5)

        self.stockshowframe = stockshowframe

        self.searchbar = QLineEdit(objectName='stock-list-search')
        self.searchbar.setPlaceholderText("Search Parts")
        self.searchbar.textChanged.connect(self.search_item)

        self.stock_item_area = QScrollArea(objectName='stock-item-area')
        self.stock_item_area.verticalScrollBar().setObjectName("stock-itemarea-vscrollbar")
        self.stock_item_area.verticalScrollBar().setMaximumWidth(5)
        self.stock_item_area.setContentsMargins(0, 0, 0, 0)
        self.stock_item_area.setWidgetResizable(False)

        self.listItemCount = 0

        stock_data = DataMethods.get_data("./Records/stock")

        # i1 = StockItem(self.stockshowframe)
        # i2 = StockItem(self.stockshowframe)
        # i1.itemName.setText("hehe")
        # i2.itemName.setText("HUHU")
        # self.stock_items.layout().addWidget(i1, 0, 0)
        # self.stock_items.layout().addWidget(i2, 1, 0)

        # self.add_item("Item1")
        # self.add_item("Item2")

        for i in sorted(stock_data.keys()):
           self.add_item(self.stock_items, i)
        self.stock_item_area.setWidget(self.stock_items)
        

        self.default_length = len(stock_data.keys())
        self.default_list_height = self.stock_items.height()

        self.layout.addWidget(self.searchbar, 0, 0, 1, 1)
        self.layout.addWidget(self.stock_item_area, 1, 0, 1, 1)

    def search_item(self):

        stock_data = DataMethods.get_data("./Records/stock")

        text = self.searchbar.text().lower()

        if text == '':
            self.clearList(self.stock_items.layout())
            self.stock_items.setMinimumHeight(self.default_list_height)


            for i in stock_data.keys():
                self.add_item(self.stock_items, i)
        
        else:
            self.clearList(self.stock_items.layout())
            self.stock_items.setMinimumHeight(1)
            self.stock_items.setMaximumHeight(2)
            # self.clearList(self.search_result_frame.layout())
            items = [i for i in stock_data.keys()]
            for item in items:
                if True in [item.lower().startswith(text), text in item.lower(), item.lower().endswith(text)]:
                    self.add_item(self.stock_items, item)
                    self.stock_items.setMinimumHeight(self.stock_items.height() + 105)
                    self.stock_items.setMaximumHeight(self.stock_items.height() + 116)
                    

    def clearList(self, layout):
        
        for ix in reversed(range(layout.count())):
            item = layout.takeAt(ix)
            if item is not None:
                item.widget().deleteLater()
        # self.stock_items.setMinimumHeight(1)
        # self.stock_items.setMaximumHeight(2)

        self.listItemCount = 0

    def add_item(self, frame, name):
        stock_data = DataMethods.get_data("Records/stock")

        itemname = f'{name}'
        itemquantity = f'{len(stock_data[name])} Items'
        item = StockItem(self.stockshowframe)
        item.itemName.setText(itemname)
        item.itemCount.setText(str(itemquantity))
        row = self.listItemCount
        
        frame.layout().addWidget(item, row, 0, 1, 1, Qt.AlignTop)
        self.listItemCount += 1

class StockShowFrame(QFrame):
    def __init__(self):
        QFrame.__init__(self, objectName='stock-show-frame')

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.setFrameShape(QFrame.StyledPanel)

        self.currentStockItem = None

        self.infoFrame = QFrame()
        self.infoFrame.setLayout(QGridLayout())

        self.itemheading = QLabel(objectName='stock-item-heading')

        self.searchbar = QLineEdit(objectName='stock-item-search')
        self.searchbar.textChanged.connect(self.search_stock)
        self.add_stock_button = QPushButton(objectName='stock-item-add-button')
        self.add_stock_button.clicked.connect(lambda: self.item_add_dialog.show() if self.item_add_dialog.isHidden() else None)

        self.item_add_dialog = QFrame()
        self.item_add_dialog.setLayout(QGridLayout())

        stock_data = DataMethods.get_data("./Records/stock")
        data_items = DataMethods.get_data("./Records/data_items")

        vehicle_box = QComboBox(objectName='stock-add-vbox')
        id_box = QLineEdit(objectName='stock-add-idbox')
        quantity_box = QSpinBox(objectName='stock-add-quantitybox')
        brand_box = QComboBox(objectName='stock-add-brandbox')
        baseprice_box = QSpinBox(objectName='stock-add-basepricebox')
        mrp_box = QSpinBox(objectName='stock-add-mrpbox')
        add_button = QPushButton("Add", objectName='stock-add-addbutton')
        cancel_button = QPushButton("Cancel", objectName='stock-add-cancelbutton')

        vehicle_box.setMinimumWidth(130)
        id_box.setMaximumWidth(130)
        quantity_box.setMaximumWidth(60)
        baseprice_box.setMaximumWidth(80)
        mrp_box.setMaximumWidth(80)
        cancel_button.clicked.connect(lambda: self.cancel_add(self.item_add_dialog))
        add_button.clicked.connect(lambda: self.add_stock(vehicle_box.currentText(),
                                                         id_box.text(), 
                                                         brand_box.currentText(),
                                                         quantity_box.value(),
                                                         baseprice_box.value(),
                                                         mrp_box.value()))
        quantity_box.setRange(1, 100)
        baseprice_box.setRange(1, 100000)
        mrp_box.setRange(1, 100000)
        vehicle_box.setEditable(True)
        brand_box.setEditable(True)
        vehicle_box.setInsertPolicy(QComboBox.NoInsert)
        brand_box.setInsertPolicy(QComboBox.NoInsert)
        for veh in data_items['Vehicles']: vehicle_box.addItem(veh)
        for brand in data_items['Brands']: brand_box.addItem(brand)

        self.item_add_dialog.layout().addWidget(vehicle_box, 0, 0, 1, 1)
        self.item_add_dialog.layout().addWidget(id_box, 0, 1, 1, 1)
        self.item_add_dialog.layout().addWidget(brand_box, 0, 2, 1, 1)
        self.item_add_dialog.layout().addWidget(quantity_box, 0, 3, 1, 1)
        self.item_add_dialog.layout().addWidget(baseprice_box, 0, 4, 1, 1)
        self.item_add_dialog.layout().addWidget(mrp_box, 0, 5, 1, 1)
        self.item_add_dialog.layout().addWidget(add_button, 1, 4, 1, 1)
        self.item_add_dialog.layout().addWidget(cancel_button, 1, 5, 1, 1)

        self.item_add_dialog.hide()

        self.itemStockTable = QTableWidget(objectName='stock-item-table')
        self.itemStockTable.itemChanged.connect(self.on_entry_change)
        # self.itemStockTable.setFocusPolicy(Qt.NoFocus)

        self.layout.addWidget(self.itemheading, 0, 0, 1, 2)
        self.layout.addWidget(self.searchbar, 1, 0, 1 ,1)
        self.layout.addWidget(self.add_stock_button, 1, 1, 1, 1)
        self.layout.addWidget(self.item_add_dialog, 2, 0, 1, 2)
        self.layout.addWidget(self.itemStockTable, 3, 0, 1, 2)

    def search_stock(self):
        self.clear_table()
        text = self.searchbar.text().lower()
        stock_data = DataMethods.get_data("./Records/stock")

        if text == "":
            self.clear_table()
            for index, item in enumerate(stock_data[self.currentStockItem], 0):
                self.itemStockTable.insertRow(self.itemStockTable.rowCount())
                for colindex, val in enumerate(item.values(), 0):
                    self.itemStockTable.setItem(index, colindex, QTableWidgetItem(str(val)))
                    self.setTableButtons()
        else:
            # self.clear_table()
            names = [item["vehicle"].lower() for item in stock_data[self.currentStockItem]]

            for index, name in enumerate(names, 0):
                if True in [name.startswith(text), name.endswith(text), text in name]:
                    self.itemStockTable.insertRow(self.itemStockTable.rowCount())
                    item = stock_data[self.currentStockItem][index]
                    for colindex, val in enumerate(item.values(), 0):
                        
                        row = self.itemStockTable.rowCount() - 1
                        self.itemStockTable.setItem(row, colindex, QTableWidgetItem(str(val)))
            self.setTableButtons()

    def clear_table(self):
        for row in range(self.itemStockTable.rowCount()):
            self.itemStockTable.removeRow(0)

    def add_stock(self, vehicle, partid, brand, quantity, baseprice, mrp):
        stock_data = DataMethods.get_data("./Records/stock")
        added = False
        to_add = {
            "vehicle": vehicle,
            "part_no": str(partid),
            "brand": brand,
            "quantity": quantity,
            "baseprice": baseprice,
            "mrp": mrp
        }

        
        stockItem = stock_data[self.currentStockItem]
        vehs = [item['vehicle'] for item in stockItem]

        if vehicle not in vehs:
            stock_data[self.currentStockItem].append(to_add)
            self.itemStockTable.insertRow(self.itemStockTable.rowCount())
            
            for colindex, val in enumerate(to_add.values(), 0):
                self.itemStockTable.setItem(self.itemStockTable.rowCount() - 1, colindex, QTableWidgetItem(str(val)))
                

        else:
            for index, item in enumerate(stockItem, 0):
                if item['vehicle'] == vehicle and item['part_no'] == partid:
                    stock_data[self.currentStockItem][index]['quantity'] += quantity
                    self.itemStockTable.setItem(index, 3, QTableWidgetItem(str(stock_data[self.currentStockItem][index]['quantity'])))
                    break
            else:
                stock_data[self.currentStockItem].append(to_add)
                self.itemStockTable.insertRow(self.itemStockTable.rowCount())
                
                for colindex, val in enumerate(to_add.values(), 0):
                    self.itemStockTable.setItem(self.itemStockTable.rowCount()-1, colindex, QTableWidgetItem(str(val)))
        DataMethods.put_data(stock_data, "./Records/stock")
        self.setTableButtons()

    def setTableButtons(self):
        
        for row in range(self.itemStockTable.rowCount()):
            increment_button = QPushButton("+", objectName='stock-item-increment-button')
            increment_button.clicked.connect(lambda: self.change_quantity("increment"))
            decrement_button = QPushButton("-", objectName='stock-item-decrement-button')
            decrement_button.clicked.connect(lambda: self.change_quantity("decrement"))
            delete_button = QPushButton("X", objectName='stock-item-delete-button')
            delete_button.clicked.connect(self.delete_stock)
            self.itemStockTable.setCellWidget(row, 6, increment_button)
            self.itemStockTable.setCellWidget(row, 7, decrement_button)
            self.itemStockTable.setCellWidget(row, 8, delete_button)

    def on_entry_change(self, item):
        stock_data = DataMethods.get_data("./Records/stock")
        try:
            current_vehicle = self.itemStockTable.item(item.row(), 0).text()
            current_part_no = self.itemStockTable.item(item.row(), 1).text()
        except:
            return
        for index, i in enumerate(stock_data[self.currentStockItem], 0):
            if i['vehicle'] == current_vehicle and i['part_no'] == current_part_no:
                if item.column() in (3, 4, 5):
                    print(item.text())
                    key_index = list(i.keys())[item.column()]
                    if not item.text().isnumeric():
                        old = QTableWidgetItem(stock_data[self.currentStockItem][index][key_index])
                        self.itemStockTable.setItem(item.row(), item.column(), old)
                        return
                    if int(item.text()) <= 0 and item.column() == 3: return
                    stock_data[self.currentStockItem][index][key_index] = int(item.text())
                    DataMethods.put_data(stock_data, "./Records/stock")
                    break


    def change_quantity(self, type_):
        itemrow = self.itemStockTable.currentRow()
        
        veh = self.itemStockTable.item(itemrow, 0).text()
        part_no = self.itemStockTable.item(itemrow, 1).text()

        stock_data = DataMethods.get_data("./Records/stock")

        for index, item in enumerate(stock_data[self.currentStockItem], 0):

            if item['vehicle'] == veh and item['part_no'] == part_no:
                if type_ == "increment":
                    change = 1
                elif type_ == "decrement" and stock_data[self.currentStockItem][index]['quantity'] > 1:
                    change = -1
                else:
                    self.delete_stock()
                    return
                stock_data[self.currentStockItem][index]['quantity'] += change
                self.itemStockTable.setItem(itemrow, 3,
                                            QTableWidgetItem(str(stock_data[self.currentStockItem][index]['quantity'])))

        DataMethods.put_data(stock_data, "./Records/stock")

    def cancel_add(self, dialog):
        dialog.hide()

    def delete_stock(self):

        itemrow = self.itemStockTable.currentRow()
        veh = self.itemStockTable.item(itemrow, 0).text()
        part_no = self.itemStockTable.item(itemrow, 1).text()

        stock_data = DataMethods.get_data("./Records/stock")

        for index, item in enumerate(stock_data[self.currentStockItem], 0):
            if item['vehicle'] == veh and item['part_no'] == part_no:   
                messagebox = QMessageBox()
                messagebox.setWindowTitle("Delete Item?")
                messagebox.setText("Are You Sure You Want To Delete This Item?")
                messagebox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)

                if messagebox.exec_() == QMessageBox.Yes:
                    del stock_data[self.currentStockItem][index]
                else:
                    return
        self.itemStockTable.removeRow(itemrow)
        DataMethods.put_data(stock_data, "./Records/stock")

    def save_stock(self):
        row = self.itemStockTable.currentRow()

        vehicle = self.itemStockTable.cellWidget(row, 0)
        vehicle = vehicle.itemText(vehicle.currentIndex())
        ID = self.itemStockTable.item(row, 1).text()
        quantity = self.itemStockTable.cellWidget(row, 2).value()
        baseprice = self.itemStockTable.cellWidget(row, 3).value()
        mrp = self.itemStockTable.cellWidget(row, 4).value()

        stock_data = DataMethods.get_data("./Records/stock")

        # # if vehicle in stock_data[self.currentStockItem]:
        # #     stock_data[self.currentStockItem]['quantity'] += int(quantity)

        # #     # start here
    def disable_item_edit(self):
        try:
            for row in range(self.itemStockTable.rowCount()):
                item_0 = self.itemStockTable.item(row, 0).text()
                item_1 = self.itemStockTable.item(row, 1).text()
                item_2 = self.itemStockTable.item(row, 2).text()
                new_0 = QTableWidgetItem(item_0)
                new_0.setFlags(Qt.ItemIsEnabled)
                new_1 = QTableWidgetItem(item_1)
                new_1.setFlags(Qt.ItemIsEnabled)
                new_2 = QTableWidgetItem(item_2)
                new_2.setFlags(Qt.ItemIsEnabled)
                self.itemStockTable.setItem(row, 0, new_0)
                self.itemStockTable.setItem(row, 1, new_1)
                self.itemStockTable.setItem(row, 2, new_2)
        except AttributeError:
            return

class StockWindowLayout(QGridLayout):
    def __init__(self):
        QGridLayout.__init__(self)
        self.setContentsMargins(0, 0, 0, 0)

        
        self.stockshowframe = StockShowFrame()
        self.stocklistframe = StockListFrame(self.stockshowframe)

        self.stocklistframe.setMaximumWidth(500)
        
        self.addWidget(self.stocklistframe, 0, 0)
        self.addWidget(self.stockshowframe, 0, 1)



class EntryHistoryLayout(QGridLayout):
    def __init__(self):
        QGridLayout.__init__(self)
        self.setContentsMargins(0, 0, 0, 0)
        self.setHorizontalSpacing(0)

        
        self.showarea = QScrollArea()
        self.showarea.setMinimumWidth(900)
        self.showarea.setMaximumHeight(680)
        self.showframe = EntryHistoryShowFrame()
        self.showarea.setWidget(self.showframe)
        self.showarea.setWidgetResizable(True)

        self.listarea = EntryHistoryListFrame(self.showframe)

        self.addWidget(self.listarea, 0, 0, 1, 1)
        self.addWidget(self.showarea, 0, 1, 1, 1)


class EntryHistoryListItem(QFrame):
    def __init__(self, vname, vnum, cinfo, date, itemcount, totalamount, entryid, showframe):
        QFrame.__init__(self)
        
        self.setObjectName("entryhistorylistitem")
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        
        self.setMinimumWidth(400)

        self.vname = vname
        self.vnum = vnum
        self.cinfo = cinfo
        self.date = date
        self.itemcount = itemcount
        self.totalamount = totalamount
        self.showframe = showframe

        self.vname_lb = QLabel(vname, objectName='entryhistorylistitem-vname')
        self.vnum_lb = QLabel(vnum, objectName='entryhistorylistitem-vnum')
        self.date_lb = QLabel(date, objectName='entryhistorylistitem-date')
        self.itemcount_lb = QLabel(str(itemcount), objectName='entryhistorylistitem-itemcount')
        self.totalamount_lb = QLabel(str(totalamount), objectName='entryhistorylistitem-totalamount')

        self.entryid = entryid

        self.layout.addWidget(self.vname_lb, 0, 0, 1, 1)
        self.layout.addWidget(self.vnum_lb, 1, 0, 1, 1)
        self.layout.addWidget(self.date_lb, 2, 0, 1, 1)
        self.layout.addWidget(self.itemcount_lb, 0, 1, 1, 1)
        self.layout.addWidget(self.totalamount_lb, 1, 1, 1, 1)

        self.mousePressEvent = lambda event: self.on_click()
    def on_click(self, ):
        self.showframe.show()
        entrydata = DataMethods.get_data("./Records/entries")
        self.showframe.currentListItem = self
        self.showframe.vheading.setText(f"{self.vname} | {self.vnum}")
        self.showframe.vname_val.setText(self.vname)
        self.showframe.vnum_val.setText(self.vnum)
        self.showframe.cinfo_val.setText(self.cinfo)
        self.showframe.date_val.setText(self.date)
        self.showframe.itemcount_val.setText(str(self.itemcount))
        self.showframe.totalamount_val.setText(str(self.totalamount))

        for i in range(self.showframe.itemsTable.rowCount()): self.showframe.itemsTable.removeRow(0)
        self.showframe.itemsTable.setColumnCount(3)
        self.showframe.itemsTable.setHorizontalHeaderLabels(["Item", "Quantity", "Price"])
        for row, item in enumerate(entrydata[self.entryid]['items'], 0):
            self.showframe.itemsTable.setRowCount(len(entrydata[self.entryid]['items']))
            for col in range(3):
                widgetitem = QTableWidgetItem(f"{item[col]}")
                widgetitem.setFlags(Qt.ItemIsEnabled)
                self.showframe.itemsTable.setItem(row, col, widgetitem)
        self.showframe.itemsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        for col in range(self.showframe.itemsTable.columnCount()):
            wids = [400, 200, 245]
            self.showframe.itemsTable.setColumnWidth(col, wids[col])
        

class EntryHistoryListFrame(QFrame):
    def __init__(self, stockshowframe):
        QFrame.__init__(self, objectName='entryhistorylist')
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.stockshowframe = stockshowframe
        self.stockshowframe.hide()
        self.listarea = QScrollArea(objectName='entryhistorylist-area')

        self.areaframe = QFrame(objectName="entryhistorylist-areaframe")
        self.areaframe.setLayout(QGridLayout())

        entrydata = DataMethods.get_data("./Records/entries")

        for i in entrydata.keys():
            vname = entrydata[i]['vname']
            vnum = entrydata[i]['vnum']
            cinfo = entrydata[i]['customerinfo']
            date = entrydata[i]['date']
            itemcount = len(entrydata[i]['items'])
            totalamount = entrydata[i]['totalamount']
            self.areaframe.layout().addWidget(EntryHistoryListItem(vname, vnum, cinfo, date, itemcount, totalamount, i, self.stockshowframe))

        self.listarea.setWidget(self.areaframe)
        self.layout.addWidget(self.listarea)

class EntryHistoryShowFrame(QFrame):
    def __init__(self):
        QFrame.__init__(self, objectName='entryhistoryshow')

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        

        self.vheading = QLabel("", objectName='entryhistoryshow-heading')
        self.vname_key = QLabel("Vehicle: ", objectName='entryhistoryshow-vname_key')
        self.vnum_key = QLabel("Registration No.: ", objectName='entryhistoryshow-vnum_key')
        self.cinfo_key = QLabel("Customer Info: ", objectName='entryhistoryshow-cinfo_key')
        self.date_key = QLabel("Date: ", objectName='entryhistoryshow-date_key')
        self.time_key = QLabel("Time: ", objectName='entryhistoryshow-time_key')
        self.itemcount_key = QLabel("Item Count: ", objectName='entryhistoryshow-itemcount_key')
        self.totalamount_key = QLabel("Total Amount: ", objectName='entryhistoryshow-totalamount_key')
        self.items_heading = QLabel("Items", objectName='entryhistoryshow-itemsheading')

        self.vname_val = QLabel("a", objectName='entryhistoryshow-vname_val')
        self.vnum_val = QLabel("a", objectName='entryhistoryshow-vnum_val')
        self.cinfo_val = QLabel("a", objectName='entryhistoryshow-cinfo_val')
        self.date_val = QLabel("a", objectName='entryhistoryshow-date_val')
        self.time_val = QLabel("a", objectName='entryhistoryshow-time_val')
        self.itemcount_val = QLabel("a", objectName='entryhistoryshow-itemcount_val')
        self.totalamount_val = QLabel("a", objectName='entryhistoryshow-totalamount_val')


        self.currentListItem = None

        self.itemsTable = QTableWidget(objectName='entryhistoryshow-table')
        self.itemsTable.setMinimumHeight(500)
        self.itemsTable.setFocusPolicy(Qt.NoFocus)
        

        self.layout.addWidget(self.vheading, 0, 0, 1, 6, Qt.AlignCenter)
        self.layout.addWidget(self.vname_key, 1, 0, 1, 1)
        self.layout.addWidget(self.vnum_key, 2, 0, 1, 1)
        self.layout.addWidget(self.cinfo_key, 3, 0, 1, 1, Qt.AlignTop)
        self.layout.addWidget(self.date_key, 4, 0, 1, 1)
        self.layout.addWidget(self.time_key, 5, 0, 1, 1)
        self.layout.addWidget(self.items_heading, 6, 0, 1, 6, Qt.AlignCenter)
        self.layout.addWidget(self.itemsTable, 7, 0, 1, 6)


        self.layout.addWidget(self.vname_val, 1, 1, 1, 1)
        self.layout.addWidget(self.vnum_val, 2, 1, 1, 1)
        self.layout.addWidget(self.cinfo_val, 3, 1, 1, 1)
        self.layout.addWidget(self.date_val, 4, 1, 1, 1)
        self.layout.addWidget(self.time_val, 5, 1, 1, 1)