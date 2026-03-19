# README Generator

## Overview

| Field       | Value              |
|-------------|--------------------|
| **Category**| `writing`          |
| **Model**   | GPT-4o / Claude 3.5 Sonnet |
| **Author**  | Mrlyk              |
| **Version** | 1.0.0              |

## Prompt

```
You are a technical writer who specializes in open-source documentation.
Generate a professional GitHub README.md for the following project.

Project name: {project_name}
Description: {description}
Tech stack: {tech_stack}
Key features: {features}

The README must include:
- Badges (build status, license, version)
- A clear introduction
- Installation instructions
- Usage examples with code blocks
- Configuration options (if applicable)
- Contributing guidelines
- License section

Use clean Markdown formatting. Write in English.
```

## Parameters

| Parameter        | Type   | Required | Description                        |
|------------------|--------|----------|------------------------------------|
| `{project_name}` | string | ✅       | Name of the project                |
| `{description}`  | string | ✅       | One-sentence project description   |
| `{tech_stack}`   | string | ✅       | Languages/frameworks used          |
| `{features}`     | string | ✅       | Comma-separated list of features   |

## Example Input

```
project_name: TaskFlow
description: A lightweight CLI task manager built with Node.js
tech_stack: Node.js, TypeScript, SQLite
features: Add/complete/delete tasks, due-date reminders, tag filtering
```

## Example Output

A fully formatted README.md with badges, installation steps, CLI usage examples, and contributing section.

## Notes

- Add `language: Chinese` at the end of the prompt for a Chinese README.
- Tested on GPT-4o and Claude 3.5 Sonnet.
