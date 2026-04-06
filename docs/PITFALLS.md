# Common Pitfalls and Solutions

Learn from common mistakes in prompt engineering and how to avoid them.

## Table of Contents
- [Clarity Issues](#clarity-issues)
- [Context Problems](#context-problems)
- [Format and Structure](#format-and-structure)
- [Scope Management](#scope-management)
- [Model Limitations](#model-limitations)

## Clarity Issues

### Pitfall 1: Vague Instructions

❌ **Poor Prompt:**
```
Write something about AI.
```

**Problems:**
- Too broad and undefined
- No clear objective
- No format specified
- No target audience

✅ **Better Prompt:**
```
Write a 500-word introduction to artificial intelligence for high school students.
Focus on real-world applications and avoid technical jargon.
Include three practical examples from daily life.
```

### Pitfall 2: Ambiguous Requirements

❌ **Poor Prompt:**
```
Make this better.
[text]
```

**Problems:**
- "Better" is subjective
- No criteria specified
- No direction given

✅ **Better Prompt:**
```
Improve this text by:
1. Making it more concise (reduce by 30%)
2. Using active voice instead of passive
3. Adding specific examples
4. Improving readability for a general audience

Original text:
[text]
```

### Pitfall 3: Multiple Unclear Tasks

❌ **Poor Prompt:**
```
Analyze this data and give me insights and also create a summary and recommendations.
```

**Problems:**
- Too many tasks at once
- No priority indicated
- Unclear deliverables

✅ **Better Approach:**
Break into separate prompts:
```
Prompt 1: Analyze this data and identify the top 3 trends:
[data]

Prompt 2: Based on these trends [results from Prompt 1], provide 3 actionable recommendations.
```

## Context Problems

### Pitfall 4: Missing Context

❌ **Poor Prompt:**
```
Review this code:
[code snippet]
```

**Problems:**
- No language specified
- No purpose explained
- No context about the project

✅ **Better Prompt:**
```
Review this Python function that processes user authentication data.
Focus on:
- Security vulnerabilities
- Error handling
- Code efficiency

Context: This is part of a web application handling 10,000+ daily users.

Code:
[code snippet]
```

### Pitfall 5: Assuming Model Knowledge

❌ **Poor Prompt:**
```
How do we fix the problem with our deployment pipeline?
```

**Problems:**
- Assumes model knows your specific system
- No details about the problem
- No context provided

✅ **Better Prompt:**
```
We use GitHub Actions for CI/CD deploying a Node.js app to AWS.
Current issue: Deployment fails at the Docker build step with error "EACCES: permission denied".

Our setup:
- Ubuntu runner
- Node 18
- Docker 20.10

What could be causing this and how can we fix it?
```

### Pitfall 6: Insufficient Examples

❌ **Poor Prompt:**
```
Format names properly.

Input: john smith
```

**Problems:**
- "Properly" is undefined
- Only one example
- Pattern unclear

✅ **Better Prompt:**
```
Convert names to proper case format:

john smith → John Smith
MARY JOHNSON → Mary Johnson
bob o'brien → Bob O'Brien
jean-paul sartre → Jean-Paul Sartre

Now format: sarah mcdonald
```

## Format and Structure

### Pitfall 7: No Output Format Specified

❌ **Poor Prompt:**
```
Give me information about these products.
```

**Problems:**
- No format specified
- Unclear what information
- No structure

✅ **Better Prompt:**
```
Compare these products in a table with columns:
- Product Name
- Price
- Key Features (3 max)
- Best For (use case)
- Rating

Products: [list]
```

### Pitfall 8: Inconsistent Delimiters

❌ **Poor Prompt:**
```
Translate this: Hello, how are you? And also this text: What's your name?
```

**Problems:**
- Unclear boundaries
- Confusing structure
- Hard to distinguish inputs

✅ **Better Prompt:**
```
Translate the following texts from English to Spanish:

Text 1:
"""
Hello, how are you?
"""

Text 2:
"""
What's your name?
"""

Format: Text 1: [translation]
        Text 2: [translation]
```

### Pitfall 9: Overlooking Length Constraints

❌ **Poor Prompt:**
```
Summarize this 10-page document.
[lengthy document]
```

**Problems:**
- No target length
- No focus areas
- May exceed token limits

✅ **Better Prompt:**
```
Summarize this document in exactly 5 bullet points.
Focus on: key findings, methodology, and conclusions.
Maximum 150 words total.

Document:
[text]
```

## Scope Management

### Pitfall 10: Overloading Single Prompt

❌ **Poor Prompt:**
```
Analyze this code, fix all bugs, optimize it, add tests, document it, and suggest refactoring.
```

**Problems:**
- Too many simultaneous tasks
- Quality suffers from complexity
- Hard to verify results

✅ **Better Approach:**
```
Step 1: Identify and list all bugs in this code
Step 2: Fix the critical bugs (from list)
Step 3: Add unit tests for fixed functionality
Step 4: Optimize performance bottlenecks
Step 5: Add documentation
```

### Pitfall 11: Unrealistic Expectations

❌ **Poor Prompt:**
```
Build a complete e-commerce platform with all features.
```

**Problems:**
- Too broad
- Undefined requirements
- Exceeds practical limits

✅ **Better Prompt:**
```
Create a basic product catalog page component in React with:
- Product card displaying image, title, price
- Grid layout (3 columns)
- Hover effects
- "Add to Cart" button

Provide component code with TypeScript types.
```

### Pitfall 12: Ignoring Iteration

❌ **Approach:**
Try to get perfect result in one prompt.

**Problems:**
- Unrealistic
- Misses refinement opportunities
- Wastes time on detailed first attempts

✅ **Better Approach:**
```
First prompt: Create basic outline
Review output → Identify gaps
Second prompt: Expand section X with more detail
Review output → Check accuracy
Third prompt: Refine tone and add examples
```

## Model Limitations

### Pitfall 13: Expecting Real-Time Data

❌ **Poor Prompt:**
```
What's the current stock price of Apple?
```

**Problems:**
- Models have knowledge cutoff dates
- No real-time data access
- May provide outdated information

✅ **Better Approach:**
```
Explain how to interpret stock price movements using technical indicators
like moving averages and RSI.
```

Or if you need current data:
```
Write a Python script to fetch current stock prices using the Alpha Vantage API.
```

### Pitfall 14: Requesting Calculations Without Verification

❌ **Poor Prompt:**
```
Calculate: 123,456 × 789,012 + 456,789 ÷ 123
```

**Problems:**
- Models may make arithmetic errors
- No verification mechanism
- Critical calculations need tools

✅ **Better Approach:**
```
Write a Python script to calculate: 123,456 × 789,012 + 456,789 ÷ 123
Then execute the script to get the accurate result.
```

Or:
```
Show me the steps to calculate this, then verify using a calculator.
```

### Pitfall 15: Ignoring Token Limits

❌ **Poor Prompt:**
```
[Paste entire 50-page document]
Analyze everything in detail.
```

**Problems:**
- May exceed context window
- Information lost or truncated
- Poor quality results

✅ **Better Approach:**
```
I have a 50-page document about [topic].
I'll share it in sections. First, here's the executive summary:
[section 1]

Analyze this section focusing on [specific aspects].
```

### Pitfall 16: Not Leveraging Model Strengths

❌ **Poor Use:**
Using AI for simple arithmetic or basic lookups

✅ **Better Use:**
- Pattern recognition
- Text generation and transformation
- Explanation and teaching
- Creative ideation
- Code generation
- Analysis and synthesis

## Language and Tone Issues

### Pitfall 17: Using Overly Complex Language

❌ **Poor Prompt:**
```
Utilize sophisticated methodologies to ameliorate the aforementioned computational inefficiencies.
```

**Problems:**
- Unnecessarily complex
- May confuse intent
- Reduces clarity

✅ **Better Prompt:**
```
Suggest ways to improve the performance issues mentioned above.
```

### Pitfall 18: Implicit Instructions

❌ **Poor Prompt:**
```
[Code snippet]
Thoughts?
```

**Problems:**
- Unclear what kind of feedback wanted
- No specific focus
- Vague expectations

✅ **Better Prompt:**
```
Review this code and provide specific feedback on:
1. Code readability
2. Potential bugs
3. Performance concerns

[code snippet]
```

## Testing and Validation

### Pitfall 19: Not Testing Edge Cases

❌ **Poor Approach:**
Only test prompts with ideal inputs

✅ **Better Approach:**
```
Test your prompt with:
- Typical inputs
- Edge cases (empty, very large, special characters)
- Invalid inputs
- Boundary conditions
```

### Pitfall 20: Single Attempt Evaluation

❌ **Poor Approach:**
Use prompt once and assume it works

✅ **Better Approach:**
1. Test prompt multiple times
2. Try with different inputs
3. Compare outputs
4. Refine based on patterns
5. Document what works

## Quick Reference: Before You Prompt

✅ **Checklist:**
- [ ] Is my objective clear?
- [ ] Have I provided necessary context?
- [ ] Did I specify the output format?
- [ ] Are there any ambiguous terms?
- [ ] Is the scope reasonable?
- [ ] Have I included relevant examples?
- [ ] Did I specify constraints or requirements?
- [ ] Is the prompt tested with edge cases?
- [ ] Can this be broken into smaller prompts?
- [ ] Have I considered the model's limitations?

## Learning from Failures

When a prompt doesn't work:

1. **Analyze Why:**
   - Was it unclear?
   - Missing context?
   - Wrong approach?

2. **Iterate:**
   - Make one change at a time
   - Test again
   - Document what improved

3. **Build a Library:**
   - Save successful prompts
   - Note what works for different tasks
   - Create templates

## Additional Resources

- Example prompt rewrites
- Community discussions on common issues
- Model-specific considerations
- Advanced debugging techniques
