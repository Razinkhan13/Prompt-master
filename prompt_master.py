"""
100X Prompt Master - Lead Project Manager & Universal Architect
================================================================

Transform any user input into elite-level prompts optimized for multiple AI models.
This system multiplies the potential of any idea by 100x through strategic refinement
and multi-model optimization.

Author: Prompt Master System
License: MIT
"""

import json
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class ModelType(Enum):
    """Supported AI model types for optimization."""
    CLAUDE = "claude"
    GEMINI = "gemini"
    GPT = "gpt"
    GROK = "grok"
    QWEN = "qwen"


class VisionLevel(Enum):
    """Vision levels for project scaling."""
    BASIC = "Basic/MVP"
    INTERMEDIATE = "Intermediate/Production-Ready"
    ENTERPRISE = "Enterprise Grade"
    GLOBAL = "Global Scale"


@dataclass
class RefinementOption:
    """Represents a refinement choice with simple and pro paths."""
    question: str
    option_a: str  # The Simple Path
    option_b: str  # The Pro Path
    option_a_label: str = "Simple Path"
    option_b_label: str = "Pro Path"


@dataclass
class ProjectReport:
    """Project delivery report structure."""
    vision_level: str
    invisible_features: List[str]
    architecture_style: str
    next_step_advice: str


class PromptMaster:
    """
    The 100X Prompt Master - Universal Architect System

    Takes any seed input and transforms it into elite-level execution plans
    optimized for multiple AI models.
    """

    def __init__(self):
        self.user_input = ""
        self.technical_level = "beginner"  # beginner, intermediate, advanced
        self.refinement_answers = {}
        self.vision_level = VisionLevel.INTERMEDIATE

    def process(self, user_input: str, technical_level: str = "beginner") -> Dict:
        """
        Main entry point - processes user input through the 100X workflow.

        Args:
            user_input: The seed input from the user
            technical_level: User's technical expertise (beginner/intermediate/advanced)

        Returns:
            Dictionary containing all phases of the 100X transformation
        """
        self.user_input = user_input
        self.technical_level = technical_level

        result = {
            "phase_1": self._phase_1_xray_summary(),
            "phase_2": self._phase_2_visual_blueprint(),
            "phase_3": self._phase_3_strategic_refinement(),
            "phase_4_template": self._phase_4_multi_model_template(),
        }

        return result

    def generate_final_prompts(self, refinement_answers: Dict[str, str]) -> Dict:
        """
        Generate final optimized prompts after user provides refinement answers.

        Args:
            refinement_answers: Dictionary mapping question IDs to chosen options (A/B)

        Returns:
            Dictionary containing optimized prompts for each model type
        """
        self.refinement_answers = refinement_answers

        prompts = self._phase_4_multi_model_payload()
        report = self._generate_project_report()

        return {
            "prompts": prompts,
            "report": report
        }

    def _phase_1_xray_summary(self) -> Dict:
        """
        PHASE 1: THE X-RAY SUMMARY
        Mirror the user's request in plain English with high-energy support.
        """
        summary = self._generate_xray_summary(self.user_input)

        return {
            "title": "X-RAY SUMMARY - Understanding Your Vision",
            "summary": summary,
            "tone": "supportive_professional_high_energy"
        }

    def _generate_xray_summary(self, user_input: str) -> str:
        """Generate a clear, non-technical summary of user's request."""
        # Analyze the input and create a clear summary
        summary = f"""
🎯 **Your Vision Understood:**

{self._extract_core_intent(user_input)}

**What This Means:**
You want to create something that {self._identify_user_goal(user_input)}.

**The Impact:**
This has the potential to {self._predict_impact(user_input)}.

✨ **I'm here to make this 100x better than you imagined!**
"""
        return summary.strip()

    def _extract_core_intent(self, user_input: str) -> str:
        """Extract the core intent from user input."""
        # Simple heuristic-based extraction
        return f"You're looking to build or create: {user_input[:200]}"

    def _identify_user_goal(self, user_input: str) -> str:
        """Identify what the user wants to achieve."""
        keywords = {
            "app": "build a functional application",
            "website": "create a web presence",
            "system": "develop a working system",
            "tool": "create a useful tool",
            "platform": "build a complete platform",
            "api": "develop a data service",
            "dashboard": "create a monitoring interface"
        }

        user_lower = user_input.lower()
        for keyword, goal in keywords.items():
            if keyword in user_lower:
                return goal

        return "solve a problem or create value"

    def _predict_impact(self, user_input: str) -> str:
        """Predict the potential impact of the project."""
        return "solve real problems, save time, and create measurable value for its users"

    def _phase_2_visual_blueprint(self) -> Dict:
        """
        PHASE 2: THE VISUAL BLUEPRINT
        Generate a Mermaid.js diagram showing the logic flow.
        """
        is_technical = self.technical_level in ["intermediate", "advanced"]
        diagram = self._generate_mermaid_diagram(self.user_input, is_technical)

        return {
            "title": "VISUAL BLUEPRINT - Your System Architecture",
            "diagram": diagram,
            "diagram_type": "mermaid",
            "label_style": "technical" if is_technical else "human"
        }

    def _generate_mermaid_diagram(self, user_input: str, technical: bool) -> str:
        """Generate a Mermaid.js diagram based on the project type."""
        if technical:
            return """```mermaid
graph TD
    A[User Input] --> B[Authentication Layer]
    B --> C[Business Logic]
    C --> D[Data Processing]
    D --> E[Storage Layer]
    E --> F[API Response]
    F --> G[User Interface]

    B --> H[Security Validation]
    H --> C

    D --> I[Error Handling]
    I --> J[Logging System]

    style A fill:#e1f5ff
    style G fill:#c8e6c9
    style H fill:#fff9c4
    style I fill:#ffccbc
```"""
        else:
            return """```mermaid
graph TD
    A[User Starts] --> B[Safe Login]
    B --> C[Main Features]
    C --> D[Save Information]
    D --> E[Success!]
    E --> F[See Results]

    B --> G[Security Check]
    G --> C

    C --> H[If Error Occurs]
    H --> I[Show Helpful Message]

    style A fill:#e1f5ff
    style E fill:#c8e6c9
    style G fill:#fff9c4
    style H fill:#ffccbc
```"""

    def _phase_3_strategic_refinement(self) -> Dict:
        """
        PHASE 3: STRATEGIC REFINEMENT
        Provide 3 key questions with Simple Path vs Pro Path options.
        """
        questions = self._generate_refinement_questions(self.user_input)

        return {
            "title": "STRATEGIC REFINEMENT - 100X Options",
            "description": "Choose how you want to scale your idea:",
            "questions": [
                {
                    "id": f"q{i+1}",
                    "question": q.question,
                    "option_a": {
                        "label": q.option_a_label,
                        "description": q.option_a
                    },
                    "option_b": {
                        "label": q.option_b_label,
                        "description": q.option_b
                    }
                }
                for i, q in enumerate(questions)
            ]
        }

    def _generate_refinement_questions(self, user_input: str) -> List[RefinementOption]:
        """Generate strategic refinement questions."""
        # Default strategic questions that work for most projects
        questions = [
            RefinementOption(
                question="How should users access your system?",
                option_a="Anyone can browse and explore freely without signing up (Faster to launch, more visitors)",
                option_b="Require user accounts to build a community and personalize experiences (Higher engagement, better data)"
            ),
            RefinementOption(
                question="What level of data handling do you need?",
                option_a="Simple storage that just works - save and retrieve information (Easier to build, lower cost)",
                option_b="Advanced analytics with insights, trends, and predictive capabilities (More powerful, competitive advantage)"
            ),
            RefinementOption(
                question="How should your system scale?",
                option_a="Start simple, handle hundreds of users efficiently (Quick launch, lower complexity)",
                option_b="Build for millions from day one with enterprise-grade infrastructure (Future-proof, premium quality)"
            )
        ]

        return questions

    def _phase_4_multi_model_template(self) -> Dict:
        """
        Return template structure for Phase 4 before refinement answers.
        """
        return {
            "title": "MULTI-MODEL PAYLOAD - Supreme Prompts",
            "description": "After you choose your options, I'll generate optimized prompts for:",
            "models": [
                "Claude/Gemini - Deep reasoning and long-context logic",
                "GPT/Grok - Strict instruction following and efficiency",
                "Qwen - Balanced performance and multilingual support"
            ],
            "status": "awaiting_refinement_answers"
        }

    def _phase_4_multi_model_payload(self) -> Dict:
        """
        PHASE 4: THE MULTI-MODEL PAYLOAD
        Generate supreme prompts optimized for different AI models.
        """
        base_prompt = self._build_base_prompt()

        prompts = {
            "claude_gemini": self._optimize_for_claude_gemini(base_prompt),
            "gpt_grok": self._optimize_for_gpt_grok(base_prompt),
            "qwen": self._optimize_for_qwen(base_prompt)
        }

        return prompts

    def _build_base_prompt(self) -> str:
        """Build the foundational prompt with all elite standards."""
        elite_standards = """
## ELITE STANDARDS - MANDATORY IMPLEMENTATION

### 1. Security-First Architecture
- Implement input validation and sanitization at all entry points
- Use parameterized queries to prevent SQL injection
- Implement proper authentication and authorization
- Enable HTTPS/TLS encryption for all data transmission
- Store sensitive data encrypted at rest
- Implement rate limiting and DDoS protection
- Follow OWASP Top 10 security guidelines

### 2. Clean Architecture Principles
- Use modular, component-based structure
- Implement separation of concerns (MVC/MVVM pattern)
- Write readable, self-documenting code
- Follow SOLID principles
- Implement dependency injection
- Create reusable, testable components
- Use meaningful naming conventions

### 3. UI/UX Excellence
- Implement responsive design (mobile-first approach)
- Use modern CSS framework (Tailwind CSS or equivalent)
- Add smooth animations and transitions
- Ensure accessibility (WCAG 2.1 Level AA compliance)
- Implement loading states and skeleton screens
- Use consistent design system
- Optimize for performance (lazy loading, code splitting)

### 4. Error Handling & Resilience
- Implement comprehensive try-catch blocks
- Provide user-friendly error messages
- Log errors for debugging (without exposing sensitive data)
- Implement graceful degradation
- Add retry logic for network requests
- Implement circuit breaker pattern for external services
- Create fallback UI states
"""

        user_requirements = f"""
## PROJECT REQUIREMENTS

**User Vision:** {self.user_input}

**Refinement Choices:**
{self._format_refinement_choices()}

**Target Vision Level:** {self.vision_level.value}
"""

        implementation_guide = """
## IMPLEMENTATION GUIDE

Create a complete, production-ready implementation that includes:

1. **Core Functionality**
   - Implement all features described in the user vision
   - Add data validation and business logic
   - Create intuitive user interfaces

2. **Database/Storage**
   - Design normalized database schema
   - Implement efficient queries and indexes
   - Add data migration scripts

3. **API Layer** (if applicable)
   - Create RESTful API endpoints
   - Implement proper HTTP methods and status codes
   - Add API documentation (OpenAPI/Swagger)

4. **Frontend** (if applicable)
   - Create responsive, modern UI
   - Implement state management
   - Add form validation and feedback

5. **Testing**
   - Write unit tests for business logic
   - Add integration tests for APIs
   - Implement E2E tests for critical flows

6. **DevOps**
   - Add Docker configuration
   - Create CI/CD pipeline
   - Add monitoring and logging

7. **Documentation**
   - Write clear README with setup instructions
   - Add API documentation
   - Include code comments for complex logic
"""

        return f"{elite_standards}\n\n{user_requirements}\n\n{implementation_guide}"

    def _format_refinement_choices(self) -> str:
        """Format the user's refinement choices."""
        if not self.refinement_answers:
            return "No refinement choices provided yet."

        formatted = []
        for q_id, choice in self.refinement_answers.items():
            formatted.append(f"- {q_id}: {choice} Path")

        return "\n".join(formatted)

    def _optimize_for_claude_gemini(self, base_prompt: str) -> str:
        """Optimize prompt for Claude and Gemini (reasoning-focused)."""
        optimization = """
# CLAUDE/GEMINI OPTIMIZATION

You are tasked with implementing this project with deep reasoning and comprehensive understanding.

## Your Approach:
1. **Think Step-by-Step:** Break down complex problems into logical steps
2. **Consider Context:** Use your long-context capability to understand all requirements
3. **Explain Reasoning:** Provide clear explanations for architectural decisions
4. **Anticipate Edge Cases:** Think through potential issues before they occur
5. **Prioritize Correctness:** Ensure logical soundness over speed

## Output Format:
- Start with a brief analysis of the requirements
- Explain your architectural decisions
- Provide well-structured, commented code
- Include detailed documentation
- Suggest improvements and alternatives

"""
        return optimization + base_prompt

    def _optimize_for_gpt_grok(self, base_prompt: str) -> str:
        """Optimize prompt for GPT and Grok (instruction-focused)."""
        optimization = """
# GPT/GROK OPTIMIZATION

Follow these instructions precisely and efficiently.

## Execution Guidelines:
1. **Be Direct:** Implement exactly what's specified
2. **Be Efficient:** Use best practices and optimal patterns
3. **Be Complete:** Deliver fully functional code
4. **Be Structured:** Organize code logically
5. **Be Professional:** Follow industry standards

## Required Deliverables:
✓ Complete, runnable code
✓ Clear file structure
✓ Installation instructions
✓ Usage examples
✓ Error handling implemented

## Constraints:
- Use modern language features
- Follow language-specific style guides
- Implement all security requirements
- Add comprehensive error handling
- Include input validation

"""
        return optimization + base_prompt

    def _optimize_for_qwen(self, base_prompt: str) -> str:
        """Optimize prompt for Qwen (balanced approach)."""
        optimization = """
# QWEN OPTIMIZATION

Implement this project with balanced focus on quality, efficiency, and clarity.

## Implementation Strategy:
1. **Balance:** Combine reasoning with efficient execution
2. **Clarity:** Write clear, maintainable code
3. **Completeness:** Cover all requirements thoroughly
4. **Best Practices:** Use proven patterns and approaches
5. **Documentation:** Include helpful comments and docs

## Deliverables:
- Well-structured codebase
- Clear documentation
- Working examples
- Setup instructions
- Test coverage

"""
        return optimization + base_prompt

    def _generate_project_report(self) -> ProjectReport:
        """Generate the final project delivery report."""
        invisible_features = [
            "🔐 Enterprise-grade security with encryption and validation",
            "⚡ Performance optimization with caching and lazy loading",
            "♿ Accessibility compliance (WCAG 2.1) for inclusive design",
            "🔄 Automatic error recovery and graceful degradation",
            "📊 Built-in analytics and monitoring capabilities",
            "🌍 Internationalization support for global reach"
        ]

        architecture_style = self._determine_architecture_style()

        next_steps = """
1. **Review the Generated Prompts:** Choose the model that best fits your needs
2. **Copy the Optimized Prompt:** Use it with your chosen AI model
3. **Iterate and Refine:** Test the output and request improvements
4. **Deploy with Confidence:** Follow the implementation guide provided
5. **Monitor and Scale:** Use the built-in features for growth
"""

        return ProjectReport(
            vision_level=self.vision_level.value,
            invisible_features=invisible_features[:3],  # Top 3
            architecture_style=architecture_style,
            next_step_advice=next_steps
        )

    def _determine_architecture_style(self) -> str:
        """Determine the architecture style based on choices."""
        # Simple heuristic based on refinement answers
        if self.refinement_answers.get("q3") == "B":
            return "High-Performance Scalable Architecture"
        elif self.refinement_answers.get("q2") == "B":
            return "Data-Driven Intelligence Platform"
        else:
            return "Modern Clean Architecture"

    def format_output(self, result: Dict, include_prompts: bool = False) -> str:
        """
        Format the output in a beautiful, readable format.

        Args:
            result: The result dictionary from process() or generate_final_prompts()
            include_prompts: Whether to include the full prompts (for final output)

        Returns:
            Formatted string output
        """
        output = []

        # Header
        output.append("=" * 80)
        output.append("🚀 100X PROMPT MASTER - UNIVERSAL ARCHITECT")
        output.append("=" * 80)
        output.append("")

        # Phase 1
        if "phase_1" in result:
            phase1 = result["phase_1"]
            output.append("📋 " + phase1["title"])
            output.append("-" * 80)
            output.append(phase1["summary"])
            output.append("")

        # Phase 2
        if "phase_2" in result:
            phase2 = result["phase_2"]
            output.append("🎨 " + phase2["title"])
            output.append("-" * 80)
            output.append(phase2["diagram"])
            output.append("")

        # Phase 3
        if "phase_3" in result:
            phase3 = result["phase_3"]
            output.append("🎯 " + phase3["title"])
            output.append("-" * 80)
            output.append(phase3["description"])
            output.append("")

            for q in phase3["questions"]:
                output.append(f"\n**{q['question']}**")
                output.append(f"  A) {q['option_a']['label']}: {q['option_a']['description']}")
                output.append(f"  B) {q['option_b']['label']}: {q['option_b']['description']}")
            output.append("")

        # Phase 4 & Report (if final prompts generated)
        if include_prompts and "prompts" in result:
            output.append("⚡ MULTI-MODEL PAYLOAD - Supreme Prompts Generated!")
            output.append("-" * 80)
            output.append("")

            prompts = result["prompts"]
            for model_type, prompt in prompts.items():
                output.append(f"\n### {model_type.upper().replace('_', ' ')} VERSION")
                output.append("-" * 40)
                output.append(prompt[:500] + "..." if len(prompt) > 500 else prompt)
                output.append("")

            # Project Report
            if "report" in result:
                report = result["report"]
                output.append("")
                output.append("=" * 80)
                output.append("📊 100X PROJECT DELIVERY REPORT")
                output.append("=" * 80)
                output.append("")
                output.append(f"**Vision Level:** {report.vision_level}")
                output.append("")
                output.append("**Invisible Features Added:**")
                for feature in report.invisible_features:
                    output.append(f"  • {feature}")
                output.append("")
                output.append(f"**Architecture Style:** {report.architecture_style}")
                output.append("")
                output.append("**Next-Step Advice:**")
                output.append(report.next_step_advice)
                output.append("")

        output.append("=" * 80)

        return "\n".join(output)


# Example usage
if __name__ == "__main__":
    # Initialize the Prompt Master
    pm = PromptMaster()

    # Example seed input
    seed_input = "I want to build a simple todo app where users can add tasks and mark them complete"

    # Phase 1-3: Initial processing
    print("Processing your idea through the 100X workflow...\n")
    result = pm.process(seed_input, technical_level="beginner")
    print(pm.format_output(result))

    # Simulate user choosing options
    print("\n\n[User makes choices: A, B, A]\n\n")

    # Phase 4: Generate final prompts
    refinement_answers = {
        "q1": "A",  # Simple Path for user access
        "q2": "B",  # Pro Path for data handling
        "q3": "A"   # Simple Path for scaling
    }

    final_result = pm.generate_final_prompts(refinement_answers)
    print(pm.format_output(final_result, include_prompts=True))
