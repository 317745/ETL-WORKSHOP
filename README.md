# ETL Workshop - Data Engineer Challenge

## Faculty & Program
**Faculty:** Faculty of Engineering and Basic Sciences  
**Program:** Data Engineering and Artificial Intelligence  
**Course:** ETL (G01)  
**Workshop:** Workshop-1: Data Engineer  

## Introduction
This project simulates a real job interview challenge. The goal is to design and implement a full ETL pipeline: extract data from a CSV file, transform it according to business rules (HIRED = both scores ≥ 7), load it into a Data Warehouse (DW), and build KPIs and visualizations from the DW using Dash.

## Getting Started
You will receive a CSV file (`data/candidates.csv`) with 50,000 rows. ETL steps: design a Star Schema (Fact table: applications, Dimension tables: candidate, date, interview, diagram + justification in `DW/diagram`), extract CSV, apply HIRED rule, compute KPIs, load into DW (SQLite). KPIs & Visualizations: Hires by Technology (total hires grouped by technology), Hires by Year (total hires per year), Hires by Seniority (total hires grouped by seniority), Hires by Country over Years (focus on USA, Brazil, Colombia, Ecuador), Hires by Month for a Year (monthly hires for a given year), Total Applications vs Hires (comparison of all applications and hires).

## Technologies & Setup
Install dependencies: `pip install -r requirements.txt`. Key Libraries: dash, flask, pandas, numpy, plotly. Linux / distros: recommended to create a virtual environment: `python3 -m venv .venvEtl`, `source .venvEtl/bin/activate`, `pip install -r requirements.txt`.

## Project Structure
.
├── applications.db        # SQLite DW  
├── dashboard              # Dash app  
│   └── app.py  
├── data                   # Raw CSV  
│   └── candidates.csv  
├── extract                # Extraction module  
│   └── dataExtraction.py  
├── transform              # Transformation module  
│   └── dataTansformation.py  
├── load                   # Load module  
│   └── dataLoad.py  
├── main.py                # Runs ETL + Dashboard  
├── requirements.txt       # Python dependencies  
└── README.md

## How to Run
Activate virtual environment (Linux/macOS): `source .venvEtl/bin/activate`. Run ETL + Dashboard: `python3 main.py`. Open browser at [http://127.0.0.1:3333/](http://127.0.0.1:3333/). If you get an error, the port may be in use. Close other apps or change the port.

## Deliverables
- `main.py` (ETL + Dashboard runner)  
- `data/querys.py` (SQL queries in `kpis` class)  
- Star Schema diagram (`DW/diagram`)  
- Dash visualizations (`dashboard/app.py`)  
- README.md (this file)
