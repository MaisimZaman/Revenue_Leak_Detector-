# 🕵️ Revenue Leak Detector Dashboard

A full-featured business intelligence dashboard built with **Streamlit** to detect and analyze revenue loss in e-commerce pipelines.

▶️ **Live Demo**: [revanue-leak-detector.streamlit.app](https://revanue-leak-detector.streamlit.app)
🔗 **GitHub Repo**: [Revenue Leak Detector](https://github.com/MaisimZaman/Revenue_Leak_Detector-)

---

## 📋 What the Project Does (Expanded)

The **Revenue Leak Detector Dashboard** is a data-driven decision-support tool designed for e-commerce businesses. It analyzes transactional data to uncover where revenue is being lost across the customer journey — from failed payments and high refund rates to abusive discount behavior. 

It provides clear visual insights, actionable metrics, and a revenue recovery simulator to model the impact of operational improvements. This allows stakeholders and analysts to not just observe the data but act on it with confidence.

## 📊 Features

- 🔻 **Funnel Breakdown** — Track drop-offs from checkout to delivery
- 🚨 **Refund & Discount Abuse Analyzer** — Identify refund-heavy users and exploited promos
- ❌ **Failed Payment Drilldown** — Spot failed transactions by region and payment method
- 📈 **Revenue Recovery Simulator** — Simulate potential revenue gains from operational improvements
- 📤 **Export Tool** — Download filtered data as CSV
- 📁 **Custom Upload Support** — Upload your own transaction dataset

---

## 📷 Screenshots

> ⚠️ Add these image files into the `images/` directory of your repo and replace placeholder text accordingly.

### 1. Overview and Filtering Panel
🖼️ `images/overview_filters.png`
📍 Show sidebar filters with dropdowns and the transaction table preview

### 2. Funnel Breakdown
🖼️ `images/funnel_breakdown.png`
📍 Funnel chart showing drop-offs and revenue lost metric

### 3. Refund & Discount Analysis
🖼️ `images/refund_abuse.png`
📍 Bar chart of discounts in refunded orders, top refunders table

### 4. Failed Payment Insights
🖼️ `images/payment_failures.png`
📍 Failed payments by region and payment method + revenue lost

### 5. Revenue Recovery Simulator
🖼️ `images/recovery_simulator.png`
📍 Slider inputs on sidebar + recovered revenue KPIs

### 6. Export Tool
🖼️ `images/export_tool.png`
📍 CSV download section with button visible

---

## 🧱 Folder Structure
```
revenue_leak_app/
├── app.py
├── data/
│   ├── revenue_leak_data.csv
│   └── alt_revenue_data.csv
├── export/
│   └── export_tools.py
├── modules/
│   ├── funnel.py
│   ├── payment_analysis.py
│   └── refund_analysis.py
├── simulators/
│   └── recovery_simulator.py
├── images/
│   └── [your screenshots here]
├── requirements.txt
└── README.md
```

---

## 🚀 Running Locally

```bash
git clone https://github.com/MaisimZaman/Revenue_Leak_Detector-.git
cd Revenue_Leak_Detector-
pip install -r requirements.txt
streamlit run app.py
```

---

## 📄 Input Dataset Details

The application expects a dataset of transactional e-commerce data in CSV format. You can either:
- Use the included sample files (`revenue_leak_data.csv`, `alt_revenue_data.csv`), or
- Upload your own file with the same structure.

### Required Columns
The input file must include the following fields:
- `TransactionID` – Unique identifier for each transaction
- `CustomerID` – Unique identifier for each customer
- `Category` – Product category of the item purchased
- `Region` – Geographic region of the order
- `PaymentMethod` – Method used to pay (e.g. Credit Card, PayPal)
- `Status` – Order result: `Completed`, `Refunded`, `Failed Payment`, or `Returned`
- `OriginalPrice` – Price before discounts
- `DiscountType` – Type of discount applied (e.g. BOGO, 10OFF)
- `DiscountAmount` – Dollar amount reduced from original price
- `FinalPrice` – Net price after discount
- `TransactionDate` – Date of transaction (for time filtering)

### What This Accomplishes
Once this data is uploaded or loaded by default, the dashboard enables users to:
- Detect which funnel stages lose the most customers or revenue
- Identify refund-heavy users or promotions being abused
- View geographic and method-based trends in failed payments
- Simulate the financial impact of improving operations (e.g. reducing refund rate by 20%)
- Export any filtered view for offline use or executive reporting
- `TransactionID`
- `CustomerID`
- `Category`
- `Region`
- `PaymentMethod`
- `Status` *(Completed, Refunded, Failed Payment, Returned)*
- `OriginalPrice`
- `DiscountType`
- `DiscountAmount`
- `FinalPrice`
- `TransactionDate`

---

## 💼 Resume Bullet Sample
> Developed a modular **Revenue Leak Detection dashboard** using Python and Streamlit, analyzing 5,000+ e-commerce transactions to identify failed payments, refund abuse, and drop-offs — enabling **revenue recovery simulations** and downloadable reports, modeled for exec insights.

---

## 🔧 Future Improvements
- PDF export with styled report
- ML-based churn prediction
- Column-mapping for custom uploads

---

## 🧠 Credits
Built by **Maisim Zaman**.

> *Lead. Analyze. Recover.*
