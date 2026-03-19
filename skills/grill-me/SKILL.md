---
name: grill-me
description: Interactively grill the user about their plan or design through relentless, structured questioning until every branch of the decision tree is resolved. Use when user explicitly asks to be grilled, stress-tested, or challenged on a plan. Trigger phrases include "grill me", "挑挑毛病", "帮我过一下方案", "盘一下".
---

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one.

Rules:
- If a question can be answered by exploring the codebase, explore the codebase instead of asking me.
- Ask 1-2 focused questions per turn. Do not dump all questions at once.
- For each question, state your recommended answer and reasoning, then ask if I agree or have a different take.
- When a branch is resolved, explicitly mark it done and move to the next.
- Keep going until all branches are resolved. Do not stop early or summarize prematurely.