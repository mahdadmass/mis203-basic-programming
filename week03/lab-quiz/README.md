# Lab 03 - Order Approval Policy

## Boundary Cases Test Table

| Case | Unit Price (TRY) | Quantity | Stock | Member? | Expected Subtotal | Expected Result & Final Price |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Just Below 500 TRY** | 99.00 | 5 | 10 | Yes | 495.00 TRY | APPROVED, no discount applied (Final: **495.00 TRY**) |
| **2. Exactly 500 TRY** | 100.00 | 5 | 10 | Yes | 500.00 TRY | APPROVED, 10% discount applied (Final: **450.00 TRY**) |
| **3. Above 500 TRY** | 100.00 | 6 | 10 | Yes | 600.00 TRY | APPROVED, 10% discount applied (Final: **540.00 TRY**) |

---

## Testing & Iteration Notes

* **Test Run Performed:** Tested Case 2 (Unit Price: 100 TRY, Quantity: 5, Member: Yes). Subtotal evaluated to exactly 500 TRY.
* **What I Changed After Testing:** Initially, the code used strict float comparisons (`subtotal == 500.0`) which can occasionally lead to precision issues. I changed the condition to `>= 500` to correctly capture orders meeting or exceeding the 500 TRY threshold regardless of minor floating-point representation nuances.
