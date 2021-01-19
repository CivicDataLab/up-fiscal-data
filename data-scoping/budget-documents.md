# Budget Documents

Understanding the structure of Uttar Pradesh budget documents.

## Table of Contents

[Platform](https://github.com/CivicDataLab/up-fiscal-data/blob/main/data-scoping/budget-documents.md#platform)

[Contents](https://github.com/CivicDataLab/up-fiscal-data/blob/main/data-scoping/budget-documents.md#contents)

[Research](https://github.com/CivicDataLab/up-fiscal-data/blob/main/data-scoping/budget-documents.md#research)

[Structure](https://github.com/CivicDataLab/up-fiscal-data/blob/main/data-scoping/budget-documents.md#structure)

## Platform

**Platfrom Name** : Budget - Government of Uttar Pradesh  
**Platform URL** : http://budget.up.nic.in/  
**Data Formats** : Portable Document - `.PDF`

## Contents

The platform contains the following budget documents for the state of Uttar Pradesh.
- Budget Speech
- Grant Wise Budget Estimates
- Annual Financial Statement
- Memorandum On Grant Wise Demand
- Schedule of New Demand
- Receipt Detail
- Supplementary Budget

## Research

The budget document **_[2020-2021 Khand-2(part1)-Annual Financial Statement](http://budget.up.nic.in/khand2part1/khand2part1_2020_2021.pdf)_** discloses the budget structure, providing with the detailed list of accounting heads and related metrics.

The following was verified through the **_[2020-2021 Khand-2(part2)-Memorandum On Grant Wise Demand](http://budget.up.nic.in/khand2part2/khand2part2_2020_2021.pdf)_** and **_[Grant Wise Budget Estimates](http://budget.up.nic.in/GrantWisepdf.html)_**.

## Structure

### Variables

| Accounting Head (Code Length) | Accounting Head (English) | Accounting Head (Hindi) |
|:---:|---|---|
| `000` | Grant | अनुदान |
| `0000` | Major Head | मुख्य शीर्ष |
| `00` | Sub Major Head | उप मुख्य शीर्ष |
| `000` | Minor Head | लघु शीर्ष |
| `00` | Sub Head | उप शीर्ष |
| `0000` | Detailed Head | विस्तृत शीर्ष |
| `00` | Primary Unit of Investment (Standard Item) | विनियोग की प्राथमिक इकाई (मानक मद) |

### Metrics

| Metric (English) | Metric (Hindi) |
|---|---|
| Budget Estimates | आय-व्ययक अनुमान |
| Revised Estimates | पुनरीक्षित अनुमान |
| Actuals | वास्तविक आंकड़े |
