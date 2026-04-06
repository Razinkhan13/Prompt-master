"""
Interactive CLI for Prompt Master
==================================

A user-friendly command-line interface for the 100X Prompt Master system.
"""

from prompt_master import PromptMaster


def print_header():
    """Print welcome header."""
    print("\n" + "=" * 80)
    print("🚀 PROMPT MASTER - 100X UNIVERSAL ARCHITECT")
    print("=" * 80)
    print("Transform any idea into elite-level AI prompts")
    print("=" * 80 + "\n")


def get_user_input():
    """Get seed input from user."""
    print("📝 STEP 1: Tell me your idea")
    print("-" * 80)
    print("What do you want to build? (Be as simple or detailed as you like)")
    print()
    seed_input = input("Your idea: ").strip()

    if not seed_input:
        print("❌ Please provide an idea to continue.")
        return None

    return seed_input


def get_technical_level():
    """Get user's technical level."""
    print("\n📊 STEP 2: What's your technical expertise?")
    print("-" * 80)
    print("1. Beginner - I'm new to coding")
    print("2. Intermediate - I have some experience")
    print("3. Advanced - I'm a professional developer")
    print()

    choice = input("Choose (1-3): ").strip()

    levels = {
        "1": "beginner",
        "2": "intermediate",
        "3": "advanced"
    }

    return levels.get(choice, "beginner")


def display_phases(pm, result):
    """Display the workflow phases."""
    print("\n" + "=" * 80)
    print("🔄 PROCESSING YOUR IDEA THROUGH THE 100X WORKFLOW")
    print("=" * 80)
    print(pm.format_output(result))


def get_refinement_answers(phase3_data):
    """Get user's choices for refinement questions."""
    print("\n" + "=" * 80)
    print("🎯 STEP 3: Make Your Strategic Choices")
    print("=" * 80)
    print("For each question, choose A (Simple Path) or B (Pro Path)")
    print()

    answers = {}
    questions = phase3_data["questions"]

    for q in questions:
        print(f"\n{q['question']}")
        print(f"  A) {q['option_a']['label']}: {q['option_a']['description']}")
        print(f"  B) {q['option_b']['label']}: {q['option_b']['description']}")
        print()

        while True:
            choice = input(f"Your choice for this question (A/B): ").strip().upper()
            if choice in ["A", "B"]:
                answers[q["id"]] = choice
                break
            else:
                print("❌ Please enter A or B")

    return answers


def choose_ai_model():
    """Let user choose which AI model prompt to see."""
    print("\n" + "=" * 80)
    print("🤖 STEP 4: Choose Your AI Model")
    print("=" * 80)
    print("Which AI model will you use?")
    print()
    print("1. Claude or Gemini (Best for: Deep reasoning, complex logic)")
    print("2. GPT or Grok (Best for: Fast execution, clear instructions)")
    print("3. Qwen (Best for: Balanced performance, multilingual)")
    print("4. Show all prompts")
    print()

    choice = input("Choose (1-4): ").strip()

    models = {
        "1": "claude_gemini",
        "2": "gpt_grok",
        "3": "qwen",
        "4": "all"
    }

    return models.get(choice, "all")


def display_final_output(pm, final_result, model_choice):
    """Display the final prompts and report."""
    print("\n" + "=" * 80)
    print("✨ YOUR 100X PROMPTS ARE READY!")
    print("=" * 80)

    prompts = final_result["prompts"]

    if model_choice == "all":
        # Show all prompts
        for model_name, prompt in prompts.items():
            print(f"\n{'=' * 80}")
            print(f"🤖 {model_name.upper().replace('_', ' ')} VERSION")
            print("=" * 80)
            print(prompt)
    else:
        # Show selected prompt
        prompt = prompts.get(model_choice)
        if prompt:
            print(f"\n{'=' * 80}")
            print(f"🤖 {model_choice.upper().replace('_', ' ')} VERSION")
            print("=" * 80)
            print(prompt)

    # Show report
    report = final_result["report"]
    print("\n" + "=" * 80)
    print("📊 100X PROJECT DELIVERY REPORT")
    print("=" * 80)
    print()
    print(f"**Vision Level:** {report.vision_level}")
    print()
    print("**Invisible Features Added:**")
    for feature in report.invisible_features:
        print(f"  • {feature}")
    print()
    print(f"**Architecture Style:** {report.architecture_style}")
    print()
    print("**Next-Step Advice:**")
    print(report.next_step_advice)
    print()


def save_to_file(content, filename="my_prompt.txt"):
    """Save prompt to a file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"\n✅ Saved to {filename}")
        return True
    except Exception as e:
        print(f"\n❌ Error saving file: {e}")
        return False


def main():
    """Main interactive CLI."""
    print_header()

    # Step 1: Get user input
    seed_input = get_user_input()
    if not seed_input:
        return

    # Step 2: Get technical level
    technical_level = get_technical_level()

    # Initialize Prompt Master
    pm = PromptMaster()

    # Process through workflow
    print("\n⏳ Processing your idea...")
    result = pm.process(seed_input, technical_level)

    # Display phases 1-3
    display_phases(pm, result)

    # Step 3: Get refinement choices
    refinement_answers = get_refinement_answers(result["phase_3"])

    # Generate final prompts
    print("\n⏳ Generating your 100X prompts...")
    final_result = pm.generate_final_prompts(refinement_answers)

    # Step 4: Choose model
    model_choice = choose_ai_model()

    # Display final output
    display_final_output(pm, final_result, model_choice)

    # Offer to save
    print("\n" + "=" * 80)
    save_choice = input("\n💾 Would you like to save this prompt to a file? (y/n): ").strip().lower()

    if save_choice == "y":
        filename = input("Filename (default: my_prompt.txt): ").strip() or "my_prompt.txt"

        # Prepare content
        content = []
        content.append("=" * 80)
        content.append("100X PROMPT MASTER OUTPUT")
        content.append("=" * 80)
        content.append(f"\nSeed Input: {seed_input}")
        content.append(f"Technical Level: {technical_level}")
        content.append(f"\nRefinement Choices: {refinement_answers}")
        content.append("\n" + "=" * 80)
        content.append("\nOPTIMIZED PROMPT:")
        content.append("=" * 80)

        if model_choice == "all":
            for model_name, prompt in final_result["prompts"].items():
                content.append(f"\n\n--- {model_name.upper()} ---\n")
                content.append(prompt)
        else:
            content.append(final_result["prompts"][model_choice])

        save_to_file("\n".join(content), filename)

    print("\n" + "=" * 80)
    print("✨ Thank you for using Prompt Master!")
    print("🚀 Go build something amazing!")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please try again or report this issue on GitHub.")
