# ETL Workshop - Data Engineer Challenge

## 📌 Faculty & Program
**Faculty:** Faculty of Engineering and Basic Sciences  
**Program:** Data Engineering and Artificial Intelligence  
**Course:** ETL (G01)  
**Workshop:** Workshop-1: Data Engineer  

---

## 📝 Introduction
This workshop simulates a real job interview code challenge. The goal is to design and implement an end-to-end ETL process to understand what companies expect in recruitment processes. The project includes:

- Extracting data from a CSV file.
- Transforming it into a Dimensional Data Model (Star Schema).
- Loading it into a Data Warehouse (DW).
- Building reports with KPIs and visualizations directly querying the DW (not the CSV).

---

## 🚀 Getting Started
You will receive a CSV file (`data/candidates.csv`) with 50,000 rows of candidate data. Your task:

1. **Design a Dimensional Data Model (DDM)**  
   - Fact Table  
   - Dimension Tables  
   - Provide a diagram and justification of your design.

2. **ETL Process**  
   - **Extract:** Load CSV using Python.  
   - **Transform:** Apply the “HIRED” rule (both scores ≥ 7).  
   - **Load:** Insert transformed data into the DW.  

3. **KPIs & Visualizations**  
   Reports must query the DW:
   - Hires by technology  
   - Hires by year  
   - Hires by seniority  
   - Hires by country over years (focus on USA, Brazil, Colombia, Ecuador)  
   - +2 additional KPIs of your choice  

   Visualizations must clearly show the data.

---

## 🛠 Technologies
- **Python 3**  
- **Pandas**  
- **SQLite** (DW)  
- **Dash** (Dashboard / Visualizations)  
- Libraries installed via `requirements.txt`  

**Note:** To run the project, simply execute:

```bash
python3 main.py
