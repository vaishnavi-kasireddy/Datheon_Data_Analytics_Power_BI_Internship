# Superstore Sales Exploratory Data Analysis

**Datheon Internship — Task 1: Data Analytics & Power BI**

**Tools Used:** Python, Pandas, Matplotlib, Seaborn, Jupyter Notebook, VS Code

## Project Overview

This project is part of my Data Analytics & Power BI internship at Datheon.

The main goal was to explore retail sales data, identify sales patterns, understand profitability across different categories and regions, and examine how discounts relate to business performance.

I used Python for data cleaning, analysis and visualisation to find insights that could support business decisions.

## Dataset

**Source:** [Datheon Superstore Sales Dataset](https://www.datheon.in/datasets/superstore_sales.csv)

The original dataset contains 10,800 rows and 21 columns.

During data exploration, I noticed that the CSV also contained separate People and Returns records. After filtering these records, I identified:

- 9,994 valid sales line items
- 5,009 unique orders
- 793 unique customers
- 11 missing postal codes in the sales data
- 0 exact duplicate sales rows

The dataset covers sales from January 2015 to December 2018.

## Data Cleaning and Preparation

Before starting the analysis, I performed the following steps:

1. Checked the dataset structure, column names and data types.
2. Identified missing values and duplicate records.
3. Separated the sales records from the additional People and Returns data.
4. Retained records with missing postal codes because they were still useful for the analysis.
5. Converted Order Date and Ship Date into datetime format.
6. Created additional columns such as Year, Year-Month and Profit Margin.

These steps helped prepare the dataset for further analysis.

## Analysis Performed

I explored the following areas:

- Overall sales and profit performance
- Monthly sales trends and seasonality
- Sales and profit by product category
- Regional business performance
- Customer segment performance
- Customer purchase volume
- Discount levels and profitability
- Yearly sales growth and low-profit product sub-categories

## Key Findings

### 1. Overall Business Performance

Superstore generated approximately **2.30 million in sales** and **286,397 in profit**, with an overall profit margin of **12.47%**.

### 2. Product Category Performance

Technology generated the highest sales and profit.

Furniture also generated significant sales, but its profit margin was only **2.49%**. Further analysis showed that Tables and Bookcases were loss-making sub-categories.

### 3. Regional Performance

The West region performed the best in terms of total sales and profit.

The Central region had the lowest profit margin at **7.92%**, suggesting that its product mix, costs and discounts deserve further investigation.

### 4. Monthly Sales Trends

Sales generally increased over the four-year period, although monthly performance fluctuated.

November 2018 recorded the highest individual monthly sales, at approximately **118,448**. November also had the highest combined sales across the four calendar years.

### 5. Discount and Profitability Analysis

One of the most interesting findings was the relationship between discounts and profitability.

Sales without discounts achieved a **29.51% profit margin**, while discount bands above 20% showed negative aggregate margins.

This suggests that high discounts are associated with lower profitability, although other factors may also contribute.

## Visualisations

I created charts using Matplotlib and Seaborn to explore:

- Monthly sales trends
- Sales across calendar months
- Category and regional performance
- Customer segment profit margins
- Discount versus profit
- Profit margins across discount groups

The generated charts are available in the `reports/figures/` folder.

## Project Structure

```text
Datheon_Task1_VSCode_Project/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── task1_superstore_eda.ipynb
├── reports/
│   └── figures/
├── src/
│   └── check_dataset.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run the Project

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Make sure Python and the Python and Jupyter extensions are installed.
4. Open the VS Code terminal and run:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

5. Open `notebooks/task1_superstore_eda.ipynb`.
6. Select the `.venv` Python kernel.
7. Run the notebook cells in order to reproduce the analysis and charts.

## Limitations

- The analysis uses historical sales data from 2015 to 2018.
- Missing postal codes were retained because they did not affect the main analysis.
- People and Returns records were excluded from this project.
- The dataset records individual sales line items, so unique orders were counted separately.
- Discount analysis shows associations rather than proving that discounts directly caused losses.
- The CSV does not explicitly specify its currency.

## What I Learned

This project helped me practise Python and Pandas for real-world data cleaning and exploratory analysis.

I gained a better understanding of grouping data, calculating KPIs, working with dates and creating visualisations.

My biggest takeaway was that **high sales do not always mean high profit**. Comparing sales and profitability across different categories, regions and customers helped me see why both measures are important.

## Acknowledgement

Dataset and internship task provided by [Datheon](https://www.datheon.in/).

This project was completed as part of a project-based learning internship.