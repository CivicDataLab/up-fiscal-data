# Budget Portal

Scoping the Uttar Pradesh fiscal data through the digital portal.

## Table of Contents

[Platform](https://github.com/CivicDataLab/up-fiscal-data/blob/master/01-data-scoping/budget-portal.md#platform)

[Contents](https://github.com/CivicDataLab/up-fiscal-data/blob/master/01-data-scoping/budget-portal.md#contents)

[Expenditure](https://github.com/CivicDataLab/up-fiscal-data/blob/master/01-data-scoping/budget-portal.md#expenditure)
- Research
- Observation
- Scope

[Reciepts](https://github.com/CivicDataLab/up-fiscal-data/blob/master/01-data-scoping/budget-portal.md#reciepts)
- Research
- Observation
- Scope

**Platfrom Name** : Koshvani web -- A Gateway to Finance Activities in the State of Uttar Pradesh  
**Platform URL** : http://koshvani.up.nic.in/  
**Data Formats** : Machine Readable - `.HTML`, `.XLS`

## Contents

The platform contains the following budgetary data information, amongst other things.

- Expenditure
    - Grant-wise expenditure
    - Grant-wise (Revenue/Capital) expenditure
    - Grant & Major Head-wise expenditure
    - Grant & Object Wise expenditure
    - Budgetary scheme expenditure
    - DDO-wise expenditure
    - Division-wise expenditure
    - Payment Budget Control Statement (Output-10)
    - Department wise Expenditure
    - PFMS Expenditure Detail

- Receipts
    - Receipt Budget Control Statement (Output-9)
    - Target-wise Receipt
    - Receipt upto Challan
    - Division-wise receipt
    - Commercial Tax Receipt

## Expenditure

### Research

- **Grant-wise expenditure** and **Grant-wise (Revenue/Capital) expenditure** capture similar information, with the latter containing revenue vs capital expediture breakup.
- **Grant & Major Head-wise expenditure** and **Budgetary scheme expenditure** capture the Major Heads and Schemes details under each grant on the platform, which is not always available under other sections in the same format.
- **Grant & Object Wise expenditure** creates a master list of various object level expenditre for each grant.
- **DDO-wise expenditure** shares information similar to **Grant-wise expenditure** but starting at the DDO level, instead of grant level.
- **Division-wise expenditure** shares expenditure information at a district and treasury level list.
- **Payment Budget Control Statement (Output-10)** shares the overall expenditure of for each Major Head.
- **Department wise Expenditure** shares the total spending under each grant with the shares from _Tribal Welfare_ and _Scheduled Castes Spending_.
- **PFMS Expenditue Detail** shares the Central Schemes wise spending for the state with Grant and Accounting Head information.

### Observations

- Grant # `081 - Social Welfare Department (Tribal Welfare)` & `083 - Social Welfare Department (Special Component Scheme for Scheduled Castes)` spending is spread across other grant heads, which can be observed under
- Various _Major Head_, _Scheme List_ and _Ditrict / Treasury_ information in available in seperate tables for data regularly and cimpletion.
- Scheme Codes in various sections will reuqires to be broken down by Budget Variables discovered in the document [analysis](https://github.com/CivicDataLab/up-fiscal-data/blob/master/01-data-scoping/budget-documents.md#structure).

### Scope

The following sections are required to be extraced based on the research.

The priorty scale goes from `Level 1` to `Level 4`. A [phased approach](https://github.com/CivicDataLab/up-fiscal-data/blob/master/00-docs/decisions/005-phases.md) is being taken to ensure a sustainable architecture. 

| Section | Rationale | Priority |
|---|---|---|
| DDO-wise expenditure | Extract all levels of accounting head of spending information. | `Level 1` |
| PFMS Expenditure Detail | Central Scheme code to State scheme code connection. | `Level 1` |
| Grant & Major Head-wise expenditure | Master list of Major Heads and Codes under each grant. | `Level 2` |
| Budgetary scheme expenditure | Master list of all schemes under various grants. | `Level 2` |
| Division-wise expenditure | Master list of all disticts and spending under each treasury. | `Level 3` |
| Grant-wise (Revenue/Capital) expenditure | Evaluate and verify expenditure breakup. | `Level 3` |
| Department wise Expenditure | Contributions of Tribal Welfare and Scheduled Castes spending for each grant. | `Level 4` |

## Receipts

Receipts data out of scope for the current exercise. Check out `[ADR -004](https://github.com/CivicDataLab/up-fiscal-data/blob/master/00-docs/decisions/004-receipts.md)` for more info.
