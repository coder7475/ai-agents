# Introduction

Artificial intelligence has come a long way — from chatbots that respond only to one stimulus, to systems that can act independently, plan, execute, and carry out multi-step processes on their own.  
This is what we call **agentic AI (or autonomous agents)**. It represents a major shift in what we can delegate to AI systems — and in the nature of the risks we must manage.

Before exploring agentic AI, let’s establish a foundation by understanding **Large Language Models (LLMs)** — the core technology powering many of today’s intelligent systems.

---

## Large Language Models (LLMs)

Large language models lie at the heart of most current AI systems. They are trained on vast collections of text and code, enabling them to produce human-like responses, summaries, and even generate programs or stories.

However, LLMs have built-in **limitations** that restrict their capabilities:

- **Text-only operation:** They can’t act outside their text box.
- **Fixed training data:** Their knowledge is frozen in time — they may miss recent events.
- **Hallucination risk:** They may invent information or make factual errors.

### Core Traits of LLMs

- **Text generation:** Predicts the next word step by step to form complete responses.
- **Stored knowledge:** Retains a wide range of information from its training data.
- **Instruction following:** Tuned to follow prompts in ways aligned with user intent.

### Security Risks

Because LLMs operate on text patterns, they can be **tricked or influenced**. Common risks include:

- **Prompt injection:** Malicious prompts that override intended instructions.
- **Jailbreaking:** Attempts to bypass safety restrictions.
- **Data poisoning:** Corrupting training or fine-tuning data to produce unsafe outputs.

Such vulnerabilities motivated the evolution toward **agentic AI**, where models can plan, act, and adapt autonomously while accessing external environments.

---

## Agentic AI

**Agentic AI** refers to AI systems with _agency_ — the capability to act toward a goal with minimal human guidance.  
Rather than being limited to static prompts, these systems operate dynamically.

### Capabilities of Agentic AI

- **Plan:** Formulate multi-step strategies to accomplish goals.
- **Act:** Execute operations such as calling APIs or running tools.
- **Watch & Adapt:** Adjust strategies when failures occur or new information arises.

---

## ReAct Prompting & Context-Awareness

Many of these capabilities stem from advances in **reasoning methods**, notably **Chain-of-Thought (CoT)** and **ReAct (Reason + Act)** prompting.

### Chain-of-Thought (CoT) Reasoning

CoT reasoning improves an LLM’s ability to perform complex, multi-step tasks by explicitly generating **intermediate reasoning steps**.  
This allows models to solve problems requiring logic, arithmetic, or common-sense reasoning.

However, CoT has limitations:

- It lacks **external knowledge** access.
- It’s prone to **hallucination** and **error propagation** due to isolated reasoning.

### ReAct: Unifying Reasoning and Action

**ReAct** improves upon CoT by integrating both reasoning and acting:

A ReAct-enabled LLM alternates between:

1. **Verbal reasoning traces:** Explaining its current thought process.
2. **Actions:** Interacting with external systems (e.g., APIs, search engines, or code execution).

#### Benefits of ReAct

- **Dynamic adaptation:** Updates plans as new information is gathered.
- **Grounded reasoning:** Fetches real-world data to reduce hallucinations.
- **Reason-action loop:** Mirrors human-like decision-making — think, act, observe, revise.

---

## Tool Use and User Space

Modern LLMs increasingly support **function calling**, enabling them to interact with external tools or APIs.

### Example: Tool Schema Registration

Developers define tools using JSON schemas, such as:

## Ref

- [TryHackME_ROOM](https://tryhackme.com/room/promptinjection-aoc2025-sxUMnCkvLO)
