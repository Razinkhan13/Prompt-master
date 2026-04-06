"""
Example Usage: Building a Todo Application
===========================================

This example demonstrates how to use Prompt Master to transform
a simple idea into an elite-level prompt.
"""

from prompt_master import PromptMaster


def example_todo_app():
    """Example: Building a todo application."""
    print("=" * 80)
    print("EXAMPLE 1: Todo Application")
    print("=" * 80)
    print()

    # Initialize Prompt Master
    pm = PromptMaster()

    # Simple seed input
    seed_input = "I want to build a simple todo app where users can add tasks and mark them complete"

    print(f"Seed Input: {seed_input}")
    print()

    # Process through the 100X workflow (Phases 1-3)
    print("Processing through 100X workflow...")
    print()
    result = pm.process(seed_input, technical_level="beginner")

    # Display phases 1-3
    print(pm.format_output(result))

    # Simulate user choosing options
    print("\n" + "=" * 80)
    print("USER MAKES CHOICES:")
    print("Q1: How should users access your system? -> A (Anyone can browse freely)")
    print("Q2: What level of data handling? -> B (Advanced analytics)")
    print("Q3: How should your system scale? -> A (Handle hundreds efficiently)")
    print("=" * 80)
    print()

    # Generate final prompts
    refinement_answers = {
        "q1": "A",  # Simple Path for user access
        "q2": "B",  # Pro Path for data handling
        "q3": "A"   # Simple Path for scaling
    }

    final_result = pm.generate_final_prompts(refinement_answers)

    # Display final output with prompts
    print(pm.format_output(final_result, include_prompts=True))


def example_ecommerce():
    """Example: Building an e-commerce platform."""
    print("\n\n")
    print("=" * 80)
    print("EXAMPLE 2: E-commerce Platform")
    print("=" * 80)
    print()

    pm = PromptMaster()

    seed_input = "I need an online store to sell handmade crafts with payment processing"

    print(f"Seed Input: {seed_input}")
    print()

    # Process as intermediate user
    result = pm.process(seed_input, technical_level="intermediate")
    print(pm.format_output(result))

    # Choose pro paths for e-commerce
    refinement_answers = {
        "q1": "B",  # Pro Path - require accounts
        "q2": "B",  # Pro Path - advanced analytics
        "q3": "B"   # Pro Path - scale for millions
    }

    final_result = pm.generate_final_prompts(refinement_answers)
    print(pm.format_output(final_result, include_prompts=True))


def example_dashboard():
    """Example: Building a data dashboard."""
    print("\n\n")
    print("=" * 80)
    print("EXAMPLE 3: Analytics Dashboard")
    print("=" * 80)
    print()

    pm = PromptMaster()

    seed_input = "Create a dashboard to visualize sales metrics with real-time updates"

    print(f"Seed Input: {seed_input}")
    print()

    # Process as advanced user
    result = pm.process(seed_input, technical_level="advanced")
    print(pm.format_output(result))

    # Mixed choices
    refinement_answers = {
        "q1": "B",  # Pro Path - user accounts for personalization
        "q2": "B",  # Pro Path - advanced analytics (essential for dashboard)
        "q3": "A"   # Simple Path - start with hundreds of users
    }

    final_result = pm.generate_final_prompts(refinement_answers)
    print(pm.format_output(final_result, include_prompts=True))


def example_api_only():
    """Example: Just viewing the workflow without generating prompts."""
    print("\n\n")
    print("=" * 80)
    print("EXAMPLE 4: Workflow Only (No Final Prompts)")
    print("=" * 80)
    print()

    pm = PromptMaster()

    seed_input = "Build an API for managing customer data"

    result = pm.process(seed_input, technical_level="advanced")
    print(pm.format_output(result))

    print("\n[User would now choose options and call generate_final_prompts()]")


if __name__ == "__main__":
    # Run all examples
    example_todo_app()

    # Uncomment to run other examples:
    # example_ecommerce()
    # example_dashboard()
    # example_api_only()
