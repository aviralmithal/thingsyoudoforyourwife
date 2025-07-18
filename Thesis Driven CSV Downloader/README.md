
# 🏙️ ThesisDriven Data Downloader

A Python script that automates logging into [ThesisDriven](https://database.thesisdriven.com), 
loading all real estate market banners, 
extracting their links, and downloading available CSV files for multi-family core theme.

---

## 🚀 Features

- Automates login using Playwright
- Clicks "View More" to load all banner items
- Extracts all unique banner links
- Visits each banner link and downloads CSVs (if available)

---

## 🛠️ Requirements

- Python 3.7+
- [Playwright for Python](https://playwright.dev/python/)

### 📦 Install Dependencies

```bash
pip install playwright
playwright install
```

---

## 🔐 Setup Credentials

Before running the script, open the Python file and update the `login_to_site()` function with your email and password:

```python
page.fill(..., 'YOUR_EMAIL_HERE')
page.fill(..., 'YOUR_PASSWORD_HERE')
```

> ⚠️ Do not hardcode credentials in public repositories. For better security, use environment variables or a `.env` file with `python-dotenv`.

---

## ▶️ How to Use

1. Save the script as `thesisdriven_scraper.py`
2. Run it using:

```bash
python thesisdriven_scraper.py
```

The script will:
- Open a browser
- Log into your ThesisDriven account
- Load all city market banners using the "View More" button
- Extract unique city market links
- Visit each link and attempt to download CSVs
- Save CSV files locally with safe filenames

---

## 📁 Output

Downloaded files will look like:

```
boston-ma.csv
austin-tx.csv
chicago-il.csv
```

They'll be saved in the same directory as the script.

---

## ⚠️ Notes

- The browser is launched in **non-headless mode** so you can watch it work. Change to `headless=True` in `p.chromium.launch()` to run silently.
- The script includes timeouts and exception handling to gracefully skip banners without CSVs.
- If nothing is downloaded, check the UI for changes on ThesisDriven that may require selector updates.

---

## 🔒 Optional Improvements

- Store credentials securely using a `.env` file
- Add a logger to capture errors
- Automatically organize downloads by city or date

---

## 👨‍💻 Author

Script by **Aviral Mithal**  
Crafted with ❤️ to automate real estate market data collection.

---

## 🧪 Disclaimer

This script is for educational and personal use only.
Make sure your use complies with the terms and conditions of [ThesisDriven](https://database.thesisdriven.com).
