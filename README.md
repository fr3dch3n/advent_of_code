# Advent of Code

Solutions for [Advent of Code](https://adventofcode.com/) challenges.

## Requirements

- Python 3.14+
- [mise](https://mise.jdx.dev/) - for task running and Python version management
- [uv](https://github.com/astral-sh/uv) - for fast Python package management

## Setup

Install dependencies and set up pre-commit hooks:

```bash
mise run install
```

## Available Tasks

All tasks are managed through mise. Run them with `mise run <task>`:

- **install** - Create uv environment and install dependencies
- **run** - Run the main program
- **test** - Run tests with pytest
- **lint** - Run ruff linter and formatter checks
- **format** - Auto-format code with ruff
- **pre-commit** - Run pre-commit hooks on all files
- **pre-commit-install** - Install pre-commit hooks

## Development

Run tests:

```bash
mise run test
```

Format code:

```bash
mise run format
```

Check linting:

```bash
mise run lint
```

Run the program:

```bash
mise run run
```
