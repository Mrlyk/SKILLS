# Data Summary

## Overview

| Field       | Value              |
|-------------|--------------------|
| **Category**| `data-analysis`    |
| **Model**   | GPT-4o             |
| **Author**  | Mrlyk              |
| **Version** | 1.0.0              |

## Prompt

```
You are a data analyst. Given the following dataset (in CSV or JSON format), provide:
1. **Summary Statistics** – row count, column types, missing values.
2. **Key Insights** – top 3–5 notable patterns or anomalies.
3. **Recommendations** – next steps for analysis or data cleaning.

Present the output in a structured, business-friendly format using Markdown tables where appropriate.

Dataset:
{data}
```

## Parameters

| Parameter | Type          | Required | Description                   |
|-----------|---------------|----------|-------------------------------|
| `{data}`  | string (CSV/JSON) | ✅  | Raw data to analyze           |

## Example Input

```csv
name,age,salary,department
Alice,30,90000,Engineering
Bob,25,60000,Marketing
Carol,,75000,Engineering
Dave,40,110000,
```

## Example Output

```
### Summary Statistics
| Column     | Type    | Missing |
|------------|---------|---------|
| name       | string  | 0       |
| age        | numeric | 1       |
| salary     | numeric | 0       |
| department | string  | 1       |

### Key Insights
- Engineering employees have higher average salaries ($82,500) vs Marketing ($60,000).
- 2 out of 4 records have at least one missing field.

### Recommendations
- Impute or investigate missing `age` for Carol.
- Fill or drop the missing `department` for Dave before segmentation analysis.
```

## Notes

- Best results with GPT-4o when dataset is under ~4,000 tokens.
- For larger datasets, summarize or sample first.
