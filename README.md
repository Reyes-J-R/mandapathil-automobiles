🛠️ Two-Wheeler Spare Parts Management System (PyQt5)

A desktop-based GUI software solution built using PyQt5 for managing a two-wheeler spare parts shop.
Designed to simplify inventory tracking, billing, and customer entry management in a clean and interactive interface.

---

✨ Features

📊 Dashboard

- Clean UI with sections:
  - Entries
  - Orders (WIP)
  - Stats (WIP)
  - Stock Management
- Quick navigation between modules
- Interactive clickable UI components

---

🧾 Entry Management

- Create and manage customer entries
- Track:
  - Vehicle Name
  - Vehicle Number
  - Items added
- Dynamic item table with:
  - Quantity control (+ / -)
  - Delete item
  - Price calculation

---

📦 Inventory Management

- Manage spare parts categorized by type
- Add/remove stock items
- Track quantities in real-time
- Integrated with billing system

---

🧮 Billing System

- Add items to entries
- Auto price calculation
- Total amount tracking
- Checkout system

---

🧠 Smart UI Features

- Dynamic dropdowns (Parts → Items)
- Auto item price updates
- Table-based editing
- Styled UI with PyQt widgets

---

📁 Data Management

- JSON-based storage:
  - "data.json"
  - "Records/entries.json"
  - "Records/stock.json"
  - "Records/data_items.json"
- Simple and lightweight (no DB required)

---

🧩 Tech Stack

- Python
- PyQt5
- JSON (local storage)

---

⚙️ Setup

1. Clone the repository

git clone https://github.com/your-username/spare-parts-gui.git
cd spare-parts-gui

2. Install dependencies

pip install PyQt5

3. Run the application

python main.py

---

📂 Project Structure

.
├── main.py
├── data.json
├── Records/
│   ├── entries.json
│   ├── stock.json
│   ├── data_items.json
├── icons/
├── styles/
└── README.md

---

🧠 Core Components

🪟 Window

- Main application window
- Fixed size layout
- Entry point of UI

---

📊 Dashboard

- Navigation hub of the app
- Connects all modules:
  - Entry window
  - Stock window
  - Items window
  - Entry history

---

📋 Entry System

- "EntryListItem": Represents each entry
- "EntryShowFrame": Handles:
  - Item addition
  - Table rendering
  - Checkout logic

---

💾 DataMethods

Utility class for:

get_data(file)
put_data(data, file)

Handles all JSON read/write operations.

---

🔄 Workflow

1. Create or select an entry
2. Add items (via part → item selection)
3. Adjust quantity
4. View total
5. Checkout

---

🚧 Limitations

- Uses JSON (not scalable for large shops)
- No authentication system
- No cloud sync
- Some features under development:
  - Orders
  - Stats
- Threading for time display is incomplete

---

🔮 Future Improvements

- Move to SQLite / PostgreSQL
- Add billing invoice generation (PDF)
- Add user authentication
- Add search & filters
- Improve UI/UX (animations, themes)
- Multi-user support

---

🤝 Contributing

Contributions are welcome.
Feel free to fork the repo and submit a pull request.

---

📜 License

MIT License

---

💡 Use Case

Perfect for:

- Small automobile shops
- Local spare parts dealers
- Offline inventory systems

---

🚀 Author Note

Built as a practical solution to digitize a traditional spare parts shop workflow using Python and PyQt.

---
