# Code Review

## Overview

| Field       | Value           |
|-------------|-----------------|
| **Category**| `code`          |
| **Model**   | GPT-4o / Claude 3.5 Sonnet |
| **Author**  | Mrlyk           |
| **Version** | 1.0.0           |

## Prompt

```
You are an expert code reviewer. Given the following code snippet, provide a thorough review covering:
1. **Correctness** – logic errors, edge cases, potential bugs.
2. **Performance** – algorithmic complexity, unnecessary operations.
3. **Security** – vulnerabilities (injections, insecure defaults, etc.).
4. **Readability** – naming, structure, comments.
5. **Best Practices** – idiomatic patterns for the language/framework.

Format your response with clear headings for each category.
Rate each area: ✅ Good / ⚠️ Needs Attention / ❌ Critical Issue.

Code to review:
{code}
```

## Parameters

| Parameter | Type   | Required | Description              |
|-----------|--------|----------|--------------------------|
| `{code}`  | string | ✅       | The code snippet to review |

## Example Input

```javascript
function fetchUser(id) {
  return db.query("SELECT * FROM users WHERE id = " + id);
}
```

## Example Output

```
### Correctness ⚠️ Needs Attention
- No null/error handling for the database query.

### Security ❌ Critical Issue
- SQL injection vulnerability: user input is concatenated directly into the query.
  Use parameterized queries instead: `db.query("SELECT * FROM users WHERE id = ?", [id])`

### Performance ✅ Good
- Simple primary-key lookup; no issues.

### Readability ✅ Good
- Function name is clear and concise.

### Best Practices ❌ Critical Issue
- Always validate/sanitize `id` before using it in a database query.
```

## Notes

- Works best with GPT-4o or Claude 3.5 Sonnet for security-focused reviews.
- For large files, split into logical sections first.
