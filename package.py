import json
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import datetime
import sys

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
    def __init__(self, entrywindow, entries, itemswindow):

        QFrame.__init__(self)
        self.entrywindow = entrywindow
        self.entries = entries
        self.itemswindow = itemswindow

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
            self.showframe.activeEntryListItem.setStyleSheet("border-right: 1px solid #55f")
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
            itemFont = QFont("Regular")
            itemFont.setBold(False)
            itemFont.setPixelSize(17)
            itemFont.setWeight(1)
            itemName.setFont(itemFont)
            itemName.setForeground(QBrush(QColor(100, 100, 255)))
            itemName.setTextAlignment(Qt.AlignLeft)
            itemName.setFlags(Qt.ItemIsEnabled)
            itemQuantity = QTableWidgetItem(str(item[1]))
            itemQuantity.setTextAlignment(Qt.AlignCenter)
            self.showframe.itemsTable.setItem(index, 0, itemName)
            self.showframe.itemsTable.setItem(index, 1, itemQuantity)

class EntryShowFrame(QFrame):
    def __init__(self):
        QFrame.__init__(self, objectName='entryshowframe')
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.mainframe = QFrame()
        self.mainframe.setLayout(QGridLayout())
        self.mainframe.hide()

        self.infoframe = QFrame()
        self.infoframe.setLayout(QGridLayout())
        # self.infoframe.hide()

        self.vname_heading = QLabel("Vehicle", objectName='vname-heading')
        self.vnum_heading = QLabel("Number", objectName='vnum-heading')
        self.item_heading = QLabel("Items", objectName='items-heading')

        self.itemSearchBar = QLineEdit(objectName='item-search-bar')
        self.itemSearchBar.setMaximumWidth(500)
        self.itemAddButton = QPushButton(objectName='item-add-button')
        self.itemAddButton.clicked.connect(self.add_item)
        self.itemDeleteButton = QPushButton(objectName='item-delete-button')
        self.itemDeleteButton.clicked.connect(self.remove_item)
        self.itemSearchBar.setMinimumWidth(610)
        # itemsdata = DataMethods.get_data("./Records/items")
        # self.itemSearchBar.setCompleter(QCompleter(map(str, itemsdata.keys())))

        # self.itemsTableFrame = QFrame()
        # self.itemsTableFrame.setLayout(QGridLayout())
        # self.itemsTableFrame.layout().setContentsMargins(0, 0, 0, 0)
        self.itemsTable = QTableWidget(objectName='items-table')
        self.itemsTable.setMinimumWidth(715)
        self.itemsTable.setMinimumHeight(300)
        self.itemsTable.setColumnCount(3)
        self.itemsTable.setHorizontalHeaderLabels(['Item', 'Quantity', 'Amount'])
        self.itemsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.itemsTable.itemChanged.connect(self.on_entry_change)
        self.itemsTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.itemsTable.verticalScrollBar().setObjectName("items-table-vscrollbar")
        # self.itemsTable.setShowGrid(False)
        # self.itemsTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.entryCheckoutButton = QPushButton("Checkout", objectName='entry-checkout-button')

        # self.itemsTable.verticalHeader().set
        for i in range(3):
            self.itemsTable.setColumnWidth(i, 225)
        self.itemsTable.hide()

        self.activeEntryListItem = None

        self.layout.addWidget(self.mainframe, 0, 0, 1, 1)
        self.layout.addWidget(self.infoframe, 0, 0, 1, 1)

        self.mainframe.layout().addWidget(self.vname_heading, 0, 0, 1, 5, Qt.AlignCenter | Qt.AlignTop)
        self.mainframe.layout().addWidget(self.vnum_heading, 1, 0, 1, 5, Qt.AlignCenter)
        self.mainframe.layout().addWidget(self.item_heading, 2, 0, 1, 1)
        self.mainframe.layout().addWidget(self.itemSearchBar, 3, 0, 1, 1)
        self.mainframe.layout().addWidget(self.itemAddButton, 3, 1, 1, 1)
        self.mainframe.layout().addWidget(self.itemDeleteButton, 3, 2, 1, 1)
        self.mainframe.layout().addWidget(self.itemsTable, 4, 0, 1, 3, Qt.AlignTop)
        self.mainframe.layout().addWidget(self.entryCheckoutButton, 5, 0, 1, 3, Qt.AlignRight)
        
    def on_entry_change(self, item):
    
        print(item.text())
        entrydata = DataMethods.get_data("./Records/entries")
        entryid = self.activeEntryListItem.entryid
        current_entry = entrydata[entryid]
        if item.column() == 1:
            if not item.text().isnumeric():
                old = QTableWidgetItem(str(current_entry['items'][item.row()][1]))
                old.setTextAlignment(Qt.AlignCenter)
                self.itemsTable.setItem(item.row(), item.column(), old)
                return
            try:
                entrydata[entryid]['items'][item.row()][1] = int(item.text())
            except IndexError:
                return
        DataMethods.put_data(entrydata, "./Records/entries")

    def add_item(self, ):
        item = self.itemSearchBar.text()
        entrydata = DataMethods.get_data("./Records/entries")
        item_names = [item_name[0] for item_name in entrydata[self.activeEntryListItem.entryid]['items']]
        if item in item_names:
            itemindex = item_names.index(item)
            entrydata[self.activeEntryListItem.entryid]['items'][itemindex][1] += 1
            tableitem = QTableWidgetItem(str(entrydata[self.activeEntryListItem.entryid]['items'][itemindex][1]))
            tableitem.setTextAlignment(Qt.AlignCenter)
            self.itemsTable.setItem(itemindex,
                1, tableitem)
        else:
            self.itemsTable.setRowCount(self.itemsTable.rowCount() + 1)
            itemname = QTableWidgetItem(item)
            itemname.setFlags(Qt.ItemIsEnabled)
            itemfont = QFont("Regular", 13)
            itemfont.setWeight(1)
            itemname.setFont(itemfont)
            itemname.setForeground(QBrush(QColor(100, 100, 255)))
            itemqty = QTableWidgetItem("1")

            # itemqty.setStyleSheet("font-size: 20px")
            itemqty.setTextAlignment(Qt.AlignCenter)
            entrydata[self.activeEntryListItem.entryid]['items'].append((item, 1))
            # self.itemsTable.insertRow(self.itemsTable.rowCount())s
            self.itemsTable.setItem(self.itemsTable.rowCount() - 1, 0, itemname)
            self.itemsTable.setItem(self.itemsTable.rowCount() - 1, 1, itemqty)
        # self.itemsTable.setItem(0, 1, QTableWidgetItem("5"))
        DataMethods.put_data(entrydata, "./Records/entries")

    def remove_item(self):
        current_row = self.itemsTable.currentRow()
        if current_row == -1:
            return
        print("row: " + str(current_row))
        entrydata = DataMethods.get_data("./Records/entries")
        del entrydata[self.activeEntryListItem.entryid]['items'][current_row]        

        self.itemsTable.removeRow(current_row)

        DataMethods.put_data(entrydata, "./Records/entries")


class NewEntryWindow(QWidget):
    def __init__(self, entries):
        QWidget.__init__(self, objectName='new-entry-widget')

        self.setGeometry(450, 150, 500, 500)
        self.setWindowTitle("New Entry")

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(10, 0, 10, 10)
        self.layout.setAlignment(Qt.AlignTop)

        self.entries = entries

        self.heading = QLabel("New Entry", objectName="new-entry-heading")
        self.vname_label = QLabel("Vehicle Name: ", objectName='new-entry-vname-label')
        self.vname_edit = QLineEdit(objectName='new-entry-vname-edit')
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

        vname = self.vname_edit.text()
        vnum = self.vnum_edit.text()
        cinfo = self.cinfo_edit.toPlainText()
        date = self.date_edit.date()
        date = f"{date.day()}-{date.month()}-{date.year()}"
        print(date)

        if "" in [vname, vnum, cinfo]:
            messageBox = QMessageBox()
            messageBox.setGeometry(600, 300, 300, 300)
            messageBox.setText("Fill Empty Fields")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.setIcon(QMessageBox.Information)
            messageBox.setWindowTitle("Fill Empty Field")
            messageBox.exec_()
            return

        entryid = str(len(entrydata.keys()) + 1)
        entrydata[str(entryid)] = {
            "vname": vname,
            "vnum": vnum,
            "customerinfo": cinfo,
            "items": [],
            "totalamount": 0,
            "date": date
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
        new_entry_window.show()

    def delete_entry(self):
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
        self.hide()


class ItemsWindowLayout(QGridLayout):
    def __init__(self):
        QGridLayout.__init__(self)

        self.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        self.heading = QLabel("Manage Items", objectName='itemswindow-heading')
        self.searchbar = QLineEdit(objectName='itemswindow-searchbar')
        self.searchbar.setPlaceholderText("Search Items")
        self.itemAddButton = QPushButton("Add Item", objectName='itemswindow-item-add-button')
        self.itemAddButton.setIcon(QIcon("./icons/plus_1.png"))
        self.itemRemoveButton = QPushButton("Remove Item", objectName='itemswindow-item-remove-button')
        self.itemRemoveButton.setIcon(QIcon("./icons/minus_1.png"))
        self.itemsList = QListWidget(objectName='itemswindow-itemslist')

        self.itemAddButton.clicked.connect(self.pop_item_dialog)
        self.itemRemoveButton.clicked.connect(self.delete_item)
        self.searchbar.textChanged.connect(self.search_item)

        self.dialogOpen = False

        self.noiteminfo = QLabel("No Items")
        self.noiteminfo.hide()



        itemsdata = DataMethods.get_data("data")

        for item in itemsdata['items']:
            self.itemsList.addItem(item)
        if self.itemsList.count() < 1:
            self.itemsList.hide()
            self.noiteminfo.show()


        self.addWidget(self.heading, 0, 0, 1, 3, Qt.AlignCenter)
        self.addWidget(self.searchbar, 1, 0, 1, 1)
        self.addWidget(self.itemAddButton, 1, 1, 1, 1)
        self.addWidget(self.itemRemoveButton, 1, 2, 1, 1)
        self.addWidget(self.noiteminfo, 2, 0, 1, 1)
        self.addWidget(self.itemsList, 2, 0, 1, 3)


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

        self.addWidget(dialog, 2, 1, 1, 2, Qt.AlignTop | Qt.AlignLeft)
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

        
        data = DataMethods.get_data("data")
        if item in data['items']:
            messagebox = QMessageBox()
            messagebox.setText("'{}' Already Exists!".format(item))
            messagebox.setStandardButtons(QMessageBox.Ok)
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Item Exists")
            messagebox.exec_()
            namefield.setText("")
            return

        data['items'].append(item.strip())
        DataMethods.put_data(data, "data")
        self.itemsList.clear()
        for i in sorted(data['items']):
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
            data = DataMethods.get_data("data")
            data['items'].remove(self.itemsList.item(to_delete).text())
            DataMethods.put_data(data, "data")
            self.itemsList.takeItem(to_delete)


    def search_item(self):
        kword = self.searchbar.text().lower()
        data = DataMethods.get_data("data")
        if kword == "":
            self.itemsList.clear()
            for item in sorted(data['items']):
                self.itemsList.addItem(item)
            return
        self.itemsList.clear()
        for item in sorted(data['items']):
            i = item.lower()
            if True in [i.startswith(kword), kword in i, i.endswith(kword), i == kword]:
                self.itemsList.addItem(item)


class StockWindowLayout(QGridLayout):
    def __init__(self):
        QGridLayout.__init__(self)

        
