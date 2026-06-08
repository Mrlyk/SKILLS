---
name: clean-disk-space
description: Safe disk space analysis and cleanup workflow for local machines. Use when asked to analyze full disks, identify large cache/log/temp/build artifacts, produce a cleanup report, run or simulate dry-runs, wait for user approval, and then clean only confirmed redundant files without affecting software functionality, user data, databases, models, projects, or developer toolchains. Also use for creating reusable disk cleanup SOPs or post-cleanup reports.
---

# Clean Disk Space

## Overview

Use this skill to perform conservative disk cleanup. Treat deletion as a separate phase that happens only after read-only analysis, a clear report, dry-run-style confirmation, and explicit user approval.

## Core Rules

- Start with read-only analysis. Do not delete during discovery.
- If a scan is slow, noisy, or entering privacy-protected directories, stop or narrow the scope.
- Prefer allowlisted cleanup categories: caches, logs, temp files, package caches, and build caches.
- Treat large directories as evidence for review, not automatic deletion targets.
- Keep Docker, Podman, Colima, and other container runtimes as optional modules. Do not assume they exist.
- Require explicit approval before real cleanup. If the user asks for dry-run, provide a delete/keep list without deleting.
- Delete only paths or resources that appeared in the approved dry-run/report.
- Stop expanding scope after the target free-space goal is reached.

## Workflow

### 1. Establish Goal and Constraints

Clarify or infer:

- Target space to free, such as 50G.
- Whether real deletion is allowed now.
- Whether the user requires a report and approval before cleanup.
- Any keep rules, such as specific images, projects, models, databases, or apps.

If user intent includes "do not affect existing functionality", default to a conservative plan and exclude data/config/toolchain directories.

### 2. Read Current Disk State

Use platform-appropriate read-only commands. On macOS, check both root and data volume:

```bash
df -h /
df -h /System/Volumes/Data 2>/dev/null
```

Record free space before cleanup. Calculate the gap to the target.

### 3. Start With Narrow, Read-Only Scans

Avoid full home or full disk recursive scans at the beginning. Start with common safe candidates:

```bash
du -sh ~/Library/Caches ~/Library/Logs ~/.cache 2>/dev/null
du -sh ~/.npm ~/.pnpm-store ~/.yarn 2>/dev/null
du -sh ~/Downloads 2>/dev/null
```

For developer machines, inspect tool caches without deleting:

```bash
du -sh ~/Library/Developer ~/.gradle ~/.m2 ~/.cargo ~/.rustup 2>/dev/null
```

### 4. Narrow Scope When Scans Misbehave

If commands produce many permission errors, run for a long time, enter privacy-protected directories, or cause high CPU:

- Stop or abandon the broad scan.
- Switch to allowlisted paths.
- Do not deep-scan Mail, Messages, Photos, Safari, protected Containers, or user document libraries unless the user explicitly asks.
- Keep top-level size findings separate from cleanup candidates.

### 5. Classify Candidates

Low-risk default cleanup:

- Application caches under known cache directories.
- User logs.
- Package manager caches: npm, pnpm, yarn, pip, uv, Homebrew.
- Build caches and editor caches.
- Xcode DerivedData.

Needs explicit user confirmation:

- Downloads.
- Browser caches.
- Simulator devices and state.
- Unused container images.
- Large app-specific caches with unclear ownership.

Default keep list:

- Documents, Pictures, Movies, Mail, Messages, Photos.
- Source code and project workspaces.
- Databases and local data directories.
- Container volumes.
- Local AI model directories.
- IDE configuration in Application Support.
- Toolchains and dependency repositories such as `.nvm`, `.m2`, `.gradle`, `.rustup/toolchains`.

### 6. Prepare the Review Report

Before deletion, present:

- Current free space and target.
- Candidate paths/resources.
- Estimated reclaimable size for each item.
- Risk level and expected impact.
- Explicit keep list.
- Recommended cleanup scope.

Ask for explicit approval before running destructive commands.

### 7. Dry-Run or Dry-Run Equivalent

If the user asks for dry-run, do not delete. List what would be deleted and what will be kept.

Use real dry-run flags when tools support them. When they do not, simulate with read-only commands such as:

```bash
du -sh <candidate-paths> 2>/dev/null
find <candidate-path> -maxdepth 1 -type d 2>/dev/null
```

For tools without dry-run support, state that the command has no dry-run mode and use read-only size/listing commands instead.

### 8. Execute Approved Cleanup

Only after explicit approval:

- Clean in batches.
- Start with largest low-risk candidates.
- Avoid adding new paths that were not in the approved report.
- Recheck free space after major batches.
- Stop when the target is reached.

When deletion fails with permission errors:

- Do not automatically escalate to broad sudo deletion.
- Check the residual size.
- Skip small residuals.
- If residual size matters, isolate the path, explain why it is still safe, and request permission for a targeted retry.

### 9. Optional Container Runtime Module

Use this only if the user has Docker/Podman/Colima or asks about containers.

Read-only inspection examples for Docker:

```bash
docker system df
docker images
docker ps -a --size
docker builder du
```

Default rules:

- Build cache is usually low-risk.
- Unused images need user confirmation because they may need re-pull or rebuild.
- Volumes are data and must be kept by default.
- Respect any user-specified keep images.

### 10. Verify and Report

After cleanup, run read-only verification:

```bash
df -h /
df -h /System/Volumes/Data 2>/dev/null
```

If relevant, verify optional systems such as container images or build cache.

Final report should include:

- Before and after free space.
- Actual space gained.
- What was cleaned.
- What was kept.
- Residual items and why they were skipped.
- Whether the target was reached.
