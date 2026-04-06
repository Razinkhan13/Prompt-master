# Code Generation Examples

Practical examples of prompts for various programming tasks.

## Python Examples

### Example 1: Data Processing Function

**Prompt:**
```
Create a Python function that processes a list of dictionaries containing user data.
The function should:
- Filter users by age (>=18)
- Sort by registration date (newest first)
- Return only username, email, and account_status fields

Input format:
[
  {"username": "john_doe", "age": 25, "email": "john@example.com",
   "account_status": "active", "registration_date": "2024-01-15"},
  ...
]

Include type hints and docstring.
```

**Expected Output:**
```python
from typing import List, Dict
from datetime import datetime

def filter_and_sort_users(users: List[Dict]) -> List[Dict]:
    """
    Filter adult users and sort by registration date.

    Args:
        users: List of user dictionaries with keys: username, age, email,
               account_status, registration_date

    Returns:
        List of filtered and sorted user dictionaries containing only
        username, email, and account_status fields
    """
    # Filter users aged 18 or older
    adult_users = [user for user in users if user.get('age', 0) >= 18]

    # Sort by registration date (newest first)
    sorted_users = sorted(
        adult_users,
        key=lambda x: datetime.strptime(x['registration_date'], '%Y-%m-%d'),
        reverse=True
    )

    # Return only specified fields
    return [
        {
            'username': user['username'],
            'email': user['email'],
            'account_status': user['account_status']
        }
        for user in sorted_users
    ]

# Example usage
users = [
    {"username": "john_doe", "age": 25, "email": "john@example.com",
     "account_status": "active", "registration_date": "2024-01-15"},
    {"username": "jane_smith", "age": 17, "email": "jane@example.com",
     "account_status": "active", "registration_date": "2024-02-01"},
    {"username": "bob_wilson", "age": 30, "email": "bob@example.com",
     "account_status": "inactive", "registration_date": "2023-12-10"}
]

result = filter_and_sort_users(users)
print(result)
```

### Example 2: API Request Handler

**Prompt:**
```
Create a Python class for making API requests with:
- Retry logic (max 3 attempts)
- Exponential backoff
- Timeout handling
- JSON response parsing
- Error logging

Use the requests library and include proper exception handling.
```

## JavaScript/TypeScript Examples

### Example 3: React Component

**Prompt:**
```
Create a React TypeScript component for a searchable dropdown with:
- Props: options (array of {label, value}), onSelect callback, placeholder
- Features: filter options as user types, keyboard navigation (arrow keys, enter)
- Styling: use Tailwind CSS classes
- Accessibility: proper ARIA labels

Include TypeScript interfaces for all props.
```

### Example 4: Data Validation

**Prompt:**
```
Write a JavaScript function to validate email addresses that:
- Checks basic email format (user@domain.com)
- Rejects common invalid patterns
- Handles edge cases (dots, plus signs, subdomain)
- Returns {valid: boolean, error?: string}

Include test cases covering valid and invalid scenarios.
```

## SQL Examples

### Example 5: Complex Query

**Prompt:**
```
Write a SQL query to:
- Find top 10 customers by total purchase amount in 2024
- Include: customer name, email, total spent, order count
- Join customers, orders, and order_items tables
- Exclude cancelled orders
- Format currency to 2 decimal places

Tables:
- customers (id, name, email)
- orders (id, customer_id, status, order_date)
- order_items (id, order_id, quantity, price)
```

**Expected Output:**
```sql
SELECT
    c.name AS customer_name,
    c.email,
    COUNT(DISTINCT o.id) AS order_count,
    ROUND(SUM(oi.quantity * oi.price), 2) AS total_spent
FROM
    customers c
    INNER JOIN orders o ON c.id = o.customer_id
    INNER JOIN order_items oi ON o.id = oi.order_id
WHERE
    o.status != 'cancelled'
    AND YEAR(o.order_date) = 2024
GROUP BY
    c.id, c.name, c.email
ORDER BY
    total_spent DESC
LIMIT 10;
```

## API Design Examples

### Example 6: REST API Endpoint

**Prompt:**
```
Design a REST API endpoint for user registration:
- Method: POST
- Path: /api/v1/users/register
- Request body: email, password, username
- Validation: email format, password strength (min 8 chars, 1 uppercase, 1 number)
- Response: user object (without password) and JWT token
- Error handling: 400 for validation errors, 409 for duplicate email

Provide:
1. OpenAPI/Swagger specification
2. Express.js implementation
3. Input validation with Joi
```

## Algorithm Examples

### Example 7: Optimization Problem

**Prompt:**
```
Implement a Python function to solve the knapsack problem:
- Given: items with weights and values, knapsack capacity
- Find: maximum value achievable without exceeding capacity
- Use dynamic programming approach
- Time complexity: O(n*W) where n=items, W=capacity

Include:
- Function with clear variable names
- Comments explaining the DP logic
- Test cases with different scenarios
```

## Testing Examples

### Example 8: Unit Tests

**Prompt:**
```
Write Jest unit tests for this function:

function calculateDiscount(price: number, discountPercent: number): number {
  if (price < 0 || discountPercent < 0 || discountPercent > 100) {
    throw new Error('Invalid input');
  }
  return price - (price * discountPercent / 100);
}

Test cases should cover:
- Normal scenarios (various prices and discounts)
- Edge cases (0%, 100% discount, 0 price)
- Error cases (negative values, >100% discount)
- Rounding precision

Use describe blocks and clear test names.
```

## Database Examples

### Example 9: Schema Design

**Prompt:**
```
Design a PostgreSQL database schema for a blog platform with:

Entities:
- Users (auth info, profile)
- Posts (title, content, status, timestamps)
- Comments (nested/threaded)
- Tags (many-to-many with posts)
- Categories (hierarchical)

Requirements:
- Proper indexes for common queries
- Foreign key constraints
- Soft delete capability
- Audit timestamps (created_at, updated_at)

Provide CREATE TABLE statements with comments.
```

## DevOps Examples

### Example 10: Dockerfile

**Prompt:**
```
Create a production-ready Dockerfile for a Node.js Express API:
- Base image: Node 18 Alpine
- Multi-stage build (dependencies, build, production)
- Non-root user
- Health check endpoint
- Environment variables for config
- Optimized layer caching

Include:
- .dockerignore file
- Comments explaining each step
- Security best practices
```

## Data Science Examples

### Example 11: Data Analysis

**Prompt:**
```
Write a Python script using pandas to analyze sales data:
- Load CSV with columns: date, product, category, quantity, revenue
- Calculate: monthly revenue trends, top 5 products by revenue, category performance
- Handle missing values
- Create summary statistics
- Export results to Excel with multiple sheets

Include visualization with matplotlib (line chart for trends, bar chart for top products).
```

## Integration Examples

### Example 12: Third-Party API Integration

**Prompt:**
```
Create a Python module to integrate with Stripe payment API:
- Create payment intent
- Handle webhooks (payment_succeeded, payment_failed)
- Verify webhook signatures
- Log all transactions
- Retry failed payments (max 3 times)

Include:
- Environment variable configuration
- Error handling and logging
- Type hints
- Example usage
```

## Tips for Code Generation Prompts

1. **Be Specific About Requirements:**
   - Language and version
   - Libraries/frameworks to use
   - Coding standards to follow

2. **Include Context:**
   - Purpose of the code
   - Where it fits in the system
   - Performance requirements

3. **Specify Output Format:**
   - Code structure
   - Documentation style
   - Test coverage

4. **Request Examples:**
   - Usage examples
   - Input/output samples
   - Edge cases

5. **Mention Constraints:**
   - Performance limits
   - Memory constraints
   - Compatibility requirements

## Common Patterns

### Pattern 1: CRUD Operations
```
Create a [language] class/module for CRUD operations on [entity]:
- Create: validate input, handle duplicates
- Read: single item and list with pagination
- Update: partial updates, optimistic locking
- Delete: soft delete with restoration
Include error handling and database transactions.
```

### Pattern 2: Data Transformation
```
Write a function to transform [input format] to [output format]:
Input structure: [describe]
Output structure: [describe]
Rules: [transformation logic]
Handle edge cases: [list cases]
```

### Pattern 3: Validation Logic
```
Implement validation for [data type] with rules:
- [rule 1]
- [rule 2]
- [rule 3]
Return detailed error messages for each failure.
Format: {valid: boolean, errors: string[]}
```

## Next Steps

- Practice with different programming languages
- Experiment with varying levels of detail in prompts
- Build a personal library of effective prompts
- Share successful patterns with the community
