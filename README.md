# Prompt Master 🎯

> **Enhancing Prompts for LLMs** - A comprehensive guide to crafting effective prompts for Large Language Models

## Overview

Prompt Master is your go-to resource for learning and mastering the art of prompt engineering. Whether you're working with ChatGPT, Claude, GPT-4, or any other LLM, this repository provides techniques, examples, and best practices to help you get the most accurate and useful responses.

## Table of Contents

- [What is Prompt Engineering?](#what-is-prompt-engineering)
- [Core Principles](#core-principles)
- [Prompt Techniques](#prompt-techniques)
- [Best Practices](#best-practices)
- [Common Use Cases](#common-use-cases)
- [Examples](#examples)
- [Contributing](#contributing)

## What is Prompt Engineering?

Prompt engineering is the practice of designing and refining inputs (prompts) to get desired outputs from Large Language Models. It's a critical skill for maximizing the effectiveness of AI tools in various applications.

## Core Principles

### 1. **Be Clear and Specific**
- State exactly what you want
- Provide context when necessary
- Define the format of the expected output

### 2. **Provide Context**
- Include relevant background information
- Specify the role or perspective you want the AI to take
- Define any constraints or requirements

### 3. **Use Examples**
- Show examples of desired output (few-shot learning)
- Demonstrate the pattern you want followed
- Include both good and bad examples when helpful

### 4. **Iterate and Refine**
- Start with a basic prompt
- Analyze the results
- Adjust and improve based on output quality

## Prompt Techniques

### Zero-Shot Prompting
Ask the model to perform a task without providing examples.

```
Translate the following English text to French: "Hello, how are you?"
```

### Few-Shot Prompting
Provide examples to guide the model's response.

```
Translate English to French:
English: Hello
French: Bonjour

English: Goodbye
French: Au revoir

English: Thank you
French: Merci

English: How are you?
French:
```

### Chain-of-Thought (CoT)
Encourage the model to show its reasoning process.

```
Question: If a train travels 120 miles in 2 hours, what is its average speed?
Let's think step by step:
```

### Role-Based Prompting
Assign a specific role or expertise to the model.

```
You are an experienced software architect. Review the following code design and suggest improvements...
```

### Structured Output Prompting
Request specific formats like JSON, tables, or lists.

```
List the top 5 programming languages in 2024 in JSON format with fields: name, rank, and primary_use.
```

## Best Practices

✅ **Do:**
- Be explicit about what you want
- Break complex tasks into smaller steps
- Specify output format when needed
- Use delimiters to separate different parts of the prompt
- Test and iterate your prompts
- Consider edge cases

❌ **Don't:**
- Be vague or ambiguous
- Assume the model knows your specific context
- Overload a single prompt with too many tasks
- Forget to specify constraints
- Use unclear or confusing language

## Common Use Cases

### Content Creation
- Blog posts and articles
- Social media content
- Product descriptions
- Email templates

### Code Assistance
- Code generation
- Debugging help
- Code review
- Documentation writing

### Data Processing
- Text summarization
- Information extraction
- Data transformation
- Classification tasks

### Analysis and Research
- Comparative analysis
- Research summaries
- Critical evaluation
- Trend identification

### Education and Learning
- Explanations of complex topics
- Practice problems
- Study guides
- Tutoring assistance

## Examples

### Example 1: Code Generation
```
Create a Python function that takes a list of numbers and returns the median value.
Include proper error handling and docstring documentation.
```

### Example 2: Content Summarization
```
Summarize the following article in 3 bullet points, focusing on the main findings:
[Article text here]
```

### Example 3: Data Formatting
```
Convert the following unstructured data into a properly formatted CSV:
Name: John, Age: 30, City: NYC
Name: Jane, Age: 25, City: LA
```

### Example 4: Creative Writing
```
Write a short story (200 words) about a robot learning to paint.
The tone should be heartwarming and suitable for children.
```

## Advanced Techniques

### Temperature and Sampling
- Lower temperature (0.0-0.3): More focused and deterministic
- Higher temperature (0.7-1.0): More creative and diverse

### Prompt Chaining
Break complex tasks into sequential prompts where each builds on the previous output.

### Self-Consistency
Generate multiple responses and choose the most consistent answer for critical tasks.

### Negative Prompting
Specify what you don't want in the output.

```
Write a professional email about project delays.
Do not use casual language or emojis.
```

## Tips for Different LLMs

### GPT Models (OpenAI)
- Excellent at following instructions
- Strong with structured outputs
- Good at maintaining context in conversations

### Claude (Anthropic)
- Strong analytical capabilities
- Excellent at following complex instructions
- Good at ethical reasoning and balanced perspectives

### Open Source Models
- May require more explicit instructions
- Often benefit from few-shot examples
- Test thoroughly for your specific use case

## Contributing

We welcome contributions! Please feel free to:
- Add new prompt examples
- Share techniques you've discovered
- Improve documentation
- Report issues or suggest improvements

## Resources

- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Prompt Engineering Documentation](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [Learn Prompting](https://learnprompting.org/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Happy Prompting! 🚀**
