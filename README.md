# Notepad Automation Bot

A simple Python bot that finds the Notepad icon on your Desktop, types blog posts, and saves them.

* **Computer Vision:** Finds the icon anywhere (Top-left, Center, Bottom-right).
* **Retry Logic:** Tries 3 times if it can't find the icon.
* **Offline Backup:** Uses a local file if the internet fails.

## 📂 Project Structure

```text
NotepadAutomation/
├── bot.py                  # Main automation script
├── pyproject.toml          # Dependency configuration (uv)
├── uv.lock                 # Lock file for reproducible installs
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
├── resources/              # Images for computer vision & backup data
│   ├── notepad_icon.png
│   ├── notepad_dark.png
│   ├── confirm_save.png
│   └── posts.json
└── screenshots/            # Proof of execution (Deliverables)
    ├── top_left.png
    ├── center.png
    └── bottom_right.png

## 🚀 How to Run

1.  **Install dependencies:**
    ```bash
    uv sync
    ```

2.  **Run the bot:**
    ```bash
    uv run python bot.py
    ```
    *(Make sure your Desktop is visible!)*
