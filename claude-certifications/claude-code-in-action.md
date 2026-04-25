# My Learning from Course Claude Code in Action

AI Coding Assistants are language model + set of tools that gathers contexts, formulate a plan, take a action in iterative way to solve problem that meets the expectation.

Language Model can only take text and return test. The tools use system to bring AI and codebase together to create agentic loop where the model repeatedly calls tools and process results.

So first key takeaways is :

1. AI coding assistants use language models combined with tool execution to complete real-world programming tasks.

2. The "tool use" architecture lets models read files, run commands, and write code despite being fundamentally text-in, text-out systems.

3. Claude models are optimized for tool use, which makes Claude Code more capable, extensible, and secure than alternatives.

4. Understanding this architecture helps you give better instructions and get significantly better results.

---

## Module 1: What is Claude Code?

### Lesson 1: What is an AI Coding Assistant?

This lesson explains that AI coding assistants like Claude Code transcend simple autocomplete by merging large language models with practical tool execution. The system operates through an "agentic loop" where the model gathers context, formulates plans, and takes action by reading files, executing commands, and modifying code—tasks impossible for language models working in isolation.

The architecture relies on "tool use," a mechanism that enables text-based models to interact with external systems. When you request a file read, Claude wraps the request with tool definitions, generates a structured call, the system executes it, and the model receives the results to analyze. This bridges the gap between pure text processing and real-world development work.

Claude models demonstrate particular prowess with tool use, enabling them to chain multiple tools for complex problems and adapt to new tools instantly. This capability gives Claude Code advantages in handling demanding tasks, extensibility through MCP servers, and security through local-only processing. Understanding this foundation helps users provide clearer instructions and achieve substantially better outcomes from the assistant.

### Lesson 2: Claude Code Tools in Action

This lesson demonstrates how Claude Code leverages built-in tools to autonomously solve complex development tasks. The platform provides access to file reading, code writing, command execution, directory searching, and multi-file coordination capabilities. Rather than simply suggesting code snippets, Claude Code "reasons about your entire project, makes architectural decisions, and executes multi-step plans" by intelligently orchestrating these tools in sequence without requiring manual intervention between steps.

The lesson illustrates this through a practical example: when asked to add input validation to a registration form, Claude Code independently searches the codebase, examines existing patterns, writes matching code, runs tests, and reports changes. This represents a fundamental departure from traditional code-completion tools, making Claude Code particularly valuable for substantial refactoring efforts, end-to-end feature development, debugging intricate problems, and creating comprehensive test suites.

The key insight emphasized is that developers benefit most by allowing Claude Code to explore unfamiliar codebases first, enabling it to build contextual understanding that improves subsequent task execution. This exploratory phase proves critical for generating higher-quality code changes aligned with project conventions.

---

## Module 2: Getting Hands On

### Lesson 3: Setting Up Claude Code

This lesson provides a comprehensive guide for getting Claude Code up and running across multiple operating systems. The installation process is straightforward, with platform-specific commands for macOS (via Homebrew or a shell script), Linux, WSL, and Windows. After installation, users simply run the "claude" command in their terminal, which triggers an authentication flow on first launch. The setup emphasizes ease of access—getting from zero to productive typically takes just minutes.

The lesson stresses that Claude Code performs optimally when launched from within an existing project directory. Rather than operating in isolation, the tool automatically analyzes your codebase structure and builds contextual understanding before making changes. Users can work with any type of project—whether React applications, Python scripts, Go services, or static websites. For enterprise users, the guide notes that optional configuration for AWS Bedrock or Google Cloud Vertex AI may be necessary depending on organizational infrastructure.

**Key takeaways include:** single-command installation across all platforms, immediate terminal access via "claude," optional enterprise cloud provider setup, and launching from within your project directory for optimal results.

### Lesson 4: Adding Context with CLAUDE.md

This lesson teaches how to effectively manage context in Claude Code to optimize AI assistance for coding projects. The core approach involves running `/init` when starting a new project, which scans your codebase and generates a CLAUDE.md file containing architecture notes and conventions. The lesson emphasizes that "context is everything," but providing too much irrelevant information actually reduces performance quality.

The instructional content covers three CLAUDE.md file types serving different scopes: project-level files shared with teams, personal local files for individual preferences, and global files applying across all projects. Two key features enhance context management—the `#` memory shortcut allows updating instructions without manual editing, and `@` file mentions enable Claude to focus on specific files directly. The final guidance stresses starting every project with `/init` and referencing critical foundational files like database schemas in CLAUDE.md to ensure they're always available for consultation.

### Lesson 5: Making Changes with Planning and Thinking Modes

This lesson teaches three essential techniques for implementing code changes in Claude Code. Visual communication through screenshots (using Ctrl+V) provides clarity when modifying UI elements. Planning Mode, activated via Shift+Tab, enables thorough codebase research before implementation, allowing you to review the approach before any changes occur. The lesson emphasizes that "Planning Mode (breadth)" works best for "multi-step implementations that touch many files," while thinking modes serve different purposes.

Thinking modes provide escalating levels of reasoning—from basic "Think" to maximum "Ultrathink" capability—designed for complex algorithmic problems and architectural decisions. The core guidance distinguishes between these tools: use Planning Mode when you need broad codebase understanding across multiple files, and employ thinking modes for deep logical reasoning on difficult problems. The most powerful approach combines both features, allowing Claude Code to conduct comprehensive analysis for particularly challenging tasks, though this strategy consumes additional tokens.

### Lesson 6: Controlling Conversation Context

This lesson teaches developers how to manage conversation flow during extended coding sessions with Claude Code. The primary focus is preventing accumulated, irrelevant context from degrading Claude's performance. Four main techniques are presented: interrupting with Escape when Claude pursues wrong directions, combining Escape with memory shortcuts to eliminate recurring errors, using Double Escape to rewind and access earlier conversation points, and leveraging two commands for context management.

The `/compact` and `/clear` commands serve distinct purposes in controlling context. As the lesson explains, "use /compact when transitioning between related tasks — it keeps Claude's project knowledge. Use /clear when the next task is entirely unrelated — stale context can mislead Claude." The `/compact` command preserves valuable learning while condensing history, whereas `/clear` provides a complete reset for unrelated work. Together with the interrupt and rewind techniques, these tools enable developers to maintain focus and productivity throughout complex development projects.

### Lesson 7: Building Custom Commands

This lesson teaches developers how to create reusable slash commands that automate repetitive workflows in Claude Code. The process is straightforward: place markdown files in the `.claude/commands/` directory, where the filename becomes the command name. For instance, creating `audit.md` automatically generates a `/audit` command. "Custom commands let you automate repetitive workflows — running security audits, writing tests to your team's conventions, generating boilerplate" with minimal effort.

The real power emerges when you incorporate the `$ARGUMENTS` placeholder, enabling commands to accept dynamic input during invocation. This approach allows a single command template to handle multiple scenarios—whether testing specific functions, auditing particular packages, or following team conventions. By enforcing consistent processes across all team members, custom commands transform Claude Code from a general assistant into a project-specific productivity tool tailored to your development standards and workflows.

### Lesson 8: Extending Claude Code with MCP Servers

This lesson introduces the Model Context Protocol (MCP) as a way to dramatically expand Claude Code's capabilities beyond its built-in tools. MCP servers are lightweight processes that expose new functionality through a standardized protocol, enabling features like "browser automation, database queries, API monitoring, cloud service integration." The Playwright MCP server is highlighted as a popular example that allows Claude to control web browsers, navigate pages, and capture screenshots—transforming visual testing from a manual process into an automated, AI-driven workflow.

The practical guidance covers installation via the `claude mcp add` command and permission management through the `.claude/settings.local.json` configuration file. A key innovation is Claude's ability to analyze actual visual output rather than just code, enabling more informed decisions about UI improvements. The lesson emphasizes that the MCP ecosystem is rapidly expanding beyond Playwright to include database interactions, API testing, cloud provider integrations, and specialized development tools, positioning developers to build highly customized workflows tailored to their specific needs.

### Lesson 9: GitHub Integration for Automated Workflows

This lesson demonstrates how Claude Code transforms into an automated team collaborator through GitHub integration. By running the `/install-github-app` command, developers can activate two default workflows: automatic pull request reviews and "@claude" mentions in issues and pull requests. The setup wizard handles installation, API key configuration, and generates the necessary GitHub Actions files, enabling Claude to analyze code changes and respond to requests directly within version control.

The lesson emphasizes customization possibilities for teams with specific needs. Users can modify workflow files by adding "project setup steps and custom instructions" to tailor Claude's behavior. Importantly, when deploying MCP servers in GitHub Actions, "every tool from every MCP server must be individually listed in the allowed_tools configuration," creating a security-focused approach to automated environments that differs from local development flexibility.

The key takeaway is that this integration significantly reduces manual code review burden while maintaining team control through explicit tool permissions and customizable workflows—developers should begin with default settings and gradually enhance configurations as team requirements become clearer.

---

## Module 3: Hooks and the SDK

### Lesson 10: Introduction to Claude Code Hooks

This lesson introduces Claude Code hooks, which are automated event listeners that execute custom code at specific points in Claude's tool execution workflow. The core concept centers on two hook types: "PreToolUse hooks — run before a tool is executed, with the power to block the operation entirely" and "PostToolUse hooks — run after a tool has completed, with the ability to provide feedback or trigger follow-up actions." Hooks can be configured at three scopes—global, project, or personal—allowing flexibility in how broadly automation applies across your development environment.

PreToolUse hooks function as gatekeepers by intercepting tool calls before execution, enabling you to enforce security policies or validate operations. In contrast, PostToolUse hooks operate after execution has completed, making them ideal for triggering follow-up actions like code formatting or test runs. Practical applications span security enforcement (blocking access to sensitive files), code quality management (running linters and formatters), testing automation, and audit logging.

### Lesson 11: Defining and Configuring Hooks

This lesson teaches the foundational architecture for building Claude Code hooks through a structured four-step methodology. Developers learn to select between PreToolUse and PostToolUse hook types, configure tool matchers using pipe syntax to target specific operations, parse incoming JSON data via standard input, and control execution flow through exit codes. The framework emphasizes that "Exit code 0 allows the operation; exit code 2 blocks it (PreToolUse only)."

The practical foundation centers on understanding data flow between Claude and hook scripts. When triggered, hooks receive detailed JSON payloads containing session identifiers, transcript paths, tool names, and tool-specific input parameters. Developers can monitor built-in tools like Read, Write, Edit, Bash, and Grep, plus any custom MCP server tools. The lesson stresses that "Write clear stderr messages when blocking — Claude uses this feedback to adjust" its behavior and approach alternatives.

### Lesson 12: Implementing a Security Hook

This lesson demonstrates how to build a practical security mechanism that prevents Claude Code from accessing sensitive files like .env configurations. The core approach involves creating a "PreToolUse" hook that intercepts both Read and Grep tool operations, checking whether they target protected files and blocking access when necessary. Developers configure the hook in their `.claude/settings.local.json` file and implement a Node.js script that validates file paths against a blocklist.

The implementation follows a straightforward three-step process: configuring the hook to trigger on specific tool types, writing a script that examines stdin input and exits with code 2 to deny operations, and then testing the protection. Beyond .env files, this pattern extends to securing private keys, credentials, internal documentation, and other sensitive resources. A critical security best practice emphasized throughout is using absolute paths rather than relative ones for hook scripts to prevent path interception attacks, though this creates challenges when sharing configuration files across development teams.

### Lesson 13: Useful Hook Patterns for Real Projects

This lesson demonstrates two powerful hook patterns that address common challenges in AI-assisted development. The first pattern uses a PostToolUse hook to run TypeScript type checking after every file modification, catching missed call-site updates when Claude alters function signatures. The second pattern leverages a separate Claude Code instance to review changes and identify code duplication, particularly useful in larger projects where existing implementations might be overlooked.

Beyond these core patterns, the lesson introduces additional hook event types available in Claude Code, including Notification, Stop, SubagentStop, PreCompact, UserPromptSubmit, SessionStart, and SessionEnd. The instructor emphasizes practical debugging techniques, such as using jq to log hook input payloads for inspection. A key consideration is balancing automation benefits against performance costs by "monitor only high-value directories" where consistency matters most.

### Lesson 14: The Claude Code SDK

This lesson teaches developers how to leverage the Claude Code SDK to integrate AI-powered coding capabilities into their own applications and automation workflows. The SDK maintains feature parity with the interactive Claude Code tool while being available for TypeScript, Python, and CLI environments. A key security feature is its read-only default setting, requiring developers to explicitly grant write permissions through specific tool allowances.

The practical applications span across the entire development lifecycle. Developers can implement automated code review through git hooks, integrate AI analysis into CI/CD pipelines, generate documentation, identify technical debt, and build custom development tools. The lesson emphasizes that permissions should be "be explicit about permissions" to maintain security when running Claude programmatically in automated scenarios.

The five core takeaways highlight that the SDK operates programmatically across multiple languages, provides identical capabilities to interactive Claude Code, implements conservative security defaults, and enables end-to-end AI-augmented development workflows when combined with hooks and MCP servers.

---

## Module 4: Test Your Knowledge

### Lesson 15: Claude Code Knowledge Quiz

This final module tests your understanding of all the concepts covered in the course through a comprehensive quiz.

---

## Summary

The Claude Code in Action course provides a comprehensive guide to mastering AI-powered development with Claude Code. The key themes include:

1. **Tool Use Architecture**: Claude Code uses an agentic loop that combines language models with tool execution to solve real-world programming tasks.

2. **Context Management**: CLAUDE.md files, memory shortcuts (#), and file mentions (@) help provide relevant context while avoiding information overload.

3. **Planning and Thinking**: Use Planning Mode for broad codebase research across multiple files, and thinking modes (Think, Think Hard, UltraThink) for deep logical reasoning.

4. **Customization**: Custom commands, MCP servers, and hooks extend Claude Code to fit team-specific workflows and security requirements.

5. **Automation**: GitHub integration enables automated PR reviews and issue handling directly within version control.

6. **SDK Integration**: The Claude Code SDK allows programmatic access for CI/CD pipelines and custom development tools.

## Resources

- [Claude Code in Action](https://claudecertifications.com/courses/claude-code-in-action)
- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)