I built a Power BI report to understand which groups of telecom customers were most likely to have left in the dataset. Of the **7,043 customers**, **1,869** were marked as having left, giving an overall observed churn rate of **26.54%**.

## Key findings

- **Tenure and contract type.** Among month-to-month customers with 0–12 months of tenure, **1,024 out of 1,994 customers churned (51.35%)**. This group accounted for about 55% of all observed churn.
- **Payment method.** Electronic-check users had the highest overall churn rate at **45.29%**. They also had the highest rate within the month-to-month group at **53.73%**, so contract type alone doesn’t explain the difference.
- **Monthly charges.** The **70 to under 100** charge band had the highest overall churn rate at **37.91%**, but the pattern changed by contract type. Among one-year customers, the **100 and above** band had higher churn than the 70 to under 100 band.
- **Internet service and tech support.** Among fiber-optic customers, churn was **49.37% without tech support** and **22.63% with tech support**. The gap also appeared within the month-to-month group.

## What I’d recommend

I’d start by testing a proactive onboarding check-in for new month-to-month customers, especially fiber customers without tech support. The check-in could help them set up their service, understand their first bill, and find support if something goes wrong. I’d compare 90-day churn with a similar group that receives the usual onboarding.

I’d also review the electronic-check payment process for issues such as failed payments or unclear reminders before recommending any change to payment options.

## Limitations

The dataset is a customer snapshot. The heatmap compares **observed churn across tenure groups**. It doesn’t follow the same signup cohorts month by month or show what caused an individual customer to leave.