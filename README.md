# South African Inflation Analysis (2008-2026)
A Python-based analysis of South African monthly inflation (January 2008 - April 2026), using official CPI (COICOP) statistics published by Statistics South Africa. All price indices are linked to the base index of 100 in December 2024.
The aim was to explore inflation trends across different categories and identify which experienced the greatest long-term and short-term price changes.

## Data Source:
Data sourced from Statistics South Africa CPI (COICOP) dataset (Jan 2008 – Apr 2026)

## Questions Investigated:
1) How has the South African Cost Price Index (CPI) changed over time?
2) Which categories of items had the highest mean index?
3) How did the index of different categories change over time?
4) What was the relationship between transport and food indices over time?
5) Which specific products had the most volatile prices?
6) Which products experienced the greatest growth in their index from 2008 to 2026?
7) Which divisions experienced the greatest growth in their index from 2008 to 2026?
8) Which specific products experienced the largest monthly and yearly change in their price index?
9) Which specific categories experienced the largest monthly and yearly change in their price index?

## Technologies Used:
1) Python
2) Pandas
3) matplotlib
4) VS Code
5) ChatGPT (used extensively in composing code to analyse data, as programmer has never attempted data analysis before)

## Requirements
- pandas
- matplotlib
- openyxl

## How to Run:
1) Clone repository
2) Install required libraries:
pip install -r requirements.txt
3) Place CPI dataset in project folder
4) Run:
python analysis.py

## Example Visualisations:
![alt text](CostPriceIndexOverTime.png)
![alt text](CostTrendsByDivision.png)

## Key Findings:
1) The average inflation (calculated by finding the average index of all products per year, finding the yearly change between these values, and finding the average decimal yearly change) is 3.2069%.
2) The Information and Communication Division featured the highest mean index, due to its exceptionally high index in 2008 (approximately 370) which decreased drastically, in comparison to all other divisions (indices below 100 in 2008).
3) Transport experienced far less index increase (from an index of approximately 70 to 100) than Food and non-alcoholic beverages (from an index of approximately 37 to 105) from 2008 to 2026.
