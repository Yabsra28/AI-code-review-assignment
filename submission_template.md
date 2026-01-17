# AI Code Review Assignment (Python)

## Candidate
- Name: Yabsra Fekadu
- Approximate time spent:

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- The function is using the wrong denominator. It divides by len(orders) instead of non cancelled orders.
- If all orders get cancelled it will endup dividing in zero.
- If all the inputs are empty , it will again end up dividing with zero.

### Edge cases & risks
- Empty input is not handled.
- Assumes order has "status" and "amount" keys.
- Fails silently or crashes if amount is missing or not the right type

### Code quality / design issues
- Logic doesnt match the stated business requirement.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Count only non-cancelled orders in the denominator.
- Safely handle empty input and all-cancelled scenarios.
- Use .get() to avoid KeyErrors and ensure robustness.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- I will consider on Empty list input,All orders cancelled, Mixed cancelled and non-cancelled orders, Orders missing amount or status,Large input size for numerical stability. Because the test will ensure the functino doesnt crash on missing data, validates the division by zero safeguard.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- Claims cancelled orders are excluded from the calculation, which is false due to the incorrect denominator.
- Does not mention failure cases such as empty input or all-cancelled orders.

### Rewritten explanation
- This function calculates the average order value using only non-cancelled orders.It sums the amounts of orders whose status is not "cancelled" and divides by the count of those orders.
If no valid orders exist, the function safely returns 0.0.

## 4) Final Judgment
- Decision: Request Changes 
- Justification: The original implementation produces incorrect results and can raise runtime errors.
- Confidence & unknowns: High confidence after correction

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- Uses "@" in email as the only validity check, which is insufficient.
- Non string inputs cause false positives or runtime errors.

### Edge cases & risks
- Accepts invalid emails such as "@", "test@", or "@test".
- Does not handle None or non-string values.

### Code quality / design issues
- Oversimplified validation logic.
- Explanation significantly overstates correctness.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Validate input type before processing.
- Use a simple regular expression to enforce a basic email structure.
- Safely ignore malformed entries.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

- I would test empty input as well as lists containing a mix of valid emails, clearly invalid strings, and non-string values to verify that only properly formatted emails are counted. I would also include edge cases like "@" or "test@" to ensure the validation logic is not overly permissive.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- The original code does not actually validate emails correctly. It only validate if it has "@"
- Safety and correctness are overstated.

### Rewritten explanation
- This function counts email addresses that conform to a basic validity pattern.
It ensures each entry is a string and matches a simple email format before counting it as valid.
Invalid and non-string entries are safely ignored.

## 4) Final Judgment
- Decision:  Request Changes 
- Justification: The original implementation does not meet its stated goal of counting valid emails.
- Confidence & unknowns: Moderate confidence

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- Divides by len(values) instead of the count of valid measurements.
- Division by zero occurs when all values are None.

### Edge cases & risks
- Crashes when encountering non-numeric values.
- Mixed input types are not safely handled.

### Code quality / design issues
- Lack of error handling contradicts the explanation’s claims.
- No validation of numeric conversion.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Track count of valid numeric measurements only.
- Use try/except to safely handle conversion to float.
- Return 0.0 when no valid measurements exist.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- I would test empty input and cases where all values are None to confirm the function behaves safely when no valid measurements are available. I would also test mixed numeric and non-numeric inputs, including numeric strings, to ensure invalid values are skipped and valid measurements are averaged correctly.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- Claims safe handling of mixed input types, which is false.
- Does not mention division by zero risk.

### Rewritten explanation
- This function computes the average of valid numeric measurements.
It ignores None values and skips entries that cannot be converted to floats.
If no valid measurements are found, it safely returns 0.0.

## 4) Final Judgment
- Decision: Request Changes 
- Justification: Mathematically incorrect and implemention is unsafe
- Confidence & unknowns: High confidence after fixes
