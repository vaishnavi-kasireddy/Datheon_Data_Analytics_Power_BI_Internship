# Task 2 — Superstore Sales Dashboard

This Power BI report helps a manager track sales performance and see which regions and product groups contribute to profit. It uses the Superstore retail sales dataset from 2015 to 2018.

## Report pages

- **Executive Overview** shows sales, profit, profit margin, and distinct orders. It also includes a monthly sales trend, a regional treemap, and an annual sales growth table.
- **Product Profitability** compares sales, profit, and margin by category and sub-category. The date and region slicers are synced across both pages.

## How I built it

I cleaned the source CSV in Power Query and built a star schema with `Fact Orders`, `Dim Customer`, `Dim Product`, and `Dim Date`. I used DAX to calculate the KPIs and checked the unfiltered totals against my Python analysis in Task 1.

## Key finding

Furniture generated **741,999.80 in sales** but had a profit margin of only **2.49%**. The profitability matrix shows why revenue alone can be misleading. The Tables sub-category generated **206,965.53 in sales** but recorded a **17,725.48 loss**.

## Open the report

- [Power BI report (.pbix)](./Superstore_Executive_Sales_Dashboard.pbix) — download and open in Power BI Desktop to use the filters.
- [Two-page PDF preview](./Datheon_Task_2_Superstore_Sales_Dashboard.pdf) — view without Power BI.