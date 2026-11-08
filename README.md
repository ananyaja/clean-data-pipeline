# Clean Data Pipeline & Automated Ingestion Utility

> **Commercial Value Proposition:** Eliminates manual spreadsheet cleanup by automating the ingestion, validation, deduplication, and transformation of messy client data into audit-ready datasets.

---

## 🔍 The Business Problem
Businesses lose hundreds of hours annually dealing with messy CSV exports, inconsistent date formats, rogue whitespace, duplicate entries, and unhandled `NaN` values pulled from legacy CRM or e-commerce platforms. 

## 🛠️ The Solution
This lightweight Python pipeline uses **Pandas** and **NumPy** to execute a fully automated, reproducible data-cleansing sequence in seconds:
1. **Deduplication & Hygiene:** Strips trailing whitespaces and eliminates exact duplicate rows.
2. **Missing Value Intelligence:** Drops unrecoverable anchor records while intelligently imputing numerical medians and categorical defaults.
3. **Type Normalization:** Standardizes multi-format date strings into ISO timestamps and cleans currency symbols from numeric fields.
4. **Audit Trail Generation:** Logs row counts, dropped duplicates, and imputation metrics.

---

## 💻 Tech Stack
- **Language:** Python 3.x
- **Libraries:** Pandas, NumPy
- **Environment:** Google Colab, Jupyter Notebook, Local CLI

---

## 🚀 How to Run
```bash
git clone [https://github.com/ananyaja/clean-data-pipeline.git](https://github.com/ananyaja/clean-data-pipeline.git)
cd clean-data-pipeline
pip install -r requirements.txt
python cleaner.py
