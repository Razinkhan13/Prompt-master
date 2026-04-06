# Examples Directory

This directory contains example usage of the Prompt Master system.

## Available Examples

### 1. Todo Application (`examples.py::example_todo_app()`)
A simple todo application for beginners.
- **Technical Level**: Beginner
- **Choices**: Simple access, Pro analytics, Simple scaling
- **Perfect for**: Learning the basics

### 2. E-commerce Platform (`examples.py::example_ecommerce()`)
A complete online store with payment processing.
- **Technical Level**: Intermediate
- **Choices**: Pro paths for all options
- **Perfect for**: Real-world business applications

### 3. Analytics Dashboard (`examples.py::example_dashboard()`)
A real-time data visualization dashboard.
- **Technical Level**: Advanced
- **Choices**: Mixed - Pro for features, Simple for scale
- **Perfect for**: Data-driven applications

### 4. API Service (`examples.py::example_api_only()`)
Backend API for customer data management.
- **Technical Level**: Advanced
- **Choices**: Workflow demonstration only
- **Perfect for**: Understanding the process

## Running Examples

```bash
# Run the main example
python examples.py

# Or import and run specific examples
python -c "from examples import example_ecommerce; example_ecommerce()"
```

## Creating Your Own

```python
from prompt_master import PromptMaster

pm = PromptMaster()

# Your seed input
seed = "Your idea here"

# Process
result = pm.process(seed, technical_level="beginner")
print(pm.format_output(result))

# Generate final prompts
answers = {"q1": "A", "q2": "B", "q3": "A"}
final = pm.generate_final_prompts(answers)
print(pm.format_output(final, include_prompts=True))
```
