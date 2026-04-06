# Quick Start Guide

Get started with Prompt Master in 2 minutes!

## 🚀 Method 1: Interactive CLI (Recommended for Beginners)

```bash
# Clone and run
git clone https://github.com/Razinkhan13/Prompt-master.git
cd Prompt-master
python3 interactive_cli.py
```

The interactive CLI will guide you through:
1. Entering your idea
2. Selecting your technical level
3. Making strategic choices
4. Getting your optimized prompts

## 💻 Method 2: Python Script

```python
from prompt_master import PromptMaster

# Initialize
pm = PromptMaster()

# Your idea
idea = "Build a weather app"

# Process
result = pm.process(idea, technical_level="beginner")
print(pm.format_output(result))

# Choose options and generate prompts
answers = {"q1": "A", "q2": "B", "q3": "A"}
final = pm.generate_final_prompts(answers)
print(pm.format_output(final, include_prompts=True))
```

## 📚 Method 3: Run Examples

```bash
# See pre-built examples
python3 examples.py
```

## 🎯 What You'll Get

For ANY idea you input, you'll receive:

1. **X-Ray Summary** - Clear understanding of your vision
2. **Visual Blueprint** - Mermaid.js diagram of your system
3. **Strategic Questions** - 3 questions to scale your idea
4. **Optimized Prompts** - AI-model-specific prompts for:
   - Claude/Gemini (reasoning-focused)
   - GPT/Grok (instruction-focused)
   - Qwen (balanced)
5. **Project Report** - Summary of features and next steps

## 🛡️ Automatic Features Added

Every prompt includes:
- ✅ Security measures (encryption, validation)
- ✅ Clean architecture (modular, scalable)
- ✅ Beautiful UI/UX (responsive, accessible)
- ✅ Error handling (robust, user-friendly)

## 💡 Quick Tips

1. **Be Natural**: Just describe your idea normally
2. **Trust the Process**: Let the system add professional features
3. **Choose Wisely**: Think about your real needs in Phase 3
4. **Copy & Use**: Take your prompt to your favorite AI model

## 🆘 Need Help?

- Check [README.md](README.md) for detailed documentation
- See [EXAMPLES.md](EXAMPLES.md) for more examples
- Open an issue on GitHub

## 🚀 Next Steps

After getting your prompt:
1. Copy it to your AI model (Claude, GPT, etc.)
2. Let the AI generate the code
3. Test and iterate
4. Deploy your project!

---

**That's it! You're ready to 100x your ideas!** 🎉
