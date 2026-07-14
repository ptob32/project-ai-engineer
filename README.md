# Project AI Engineer

This repository is my AI engineering learning project focused on production-style Python, data engineering fundamentals, and AI system design.

## Current Focus

Sprint 2: Professional Python Project Structure

## Project Structure

- `src/enterprise_ai_platform/` - main Python package
- `tests/` - automated tests
- `data/` - raw, interim, and processed data
- `notebooks/` - project notebooks
- `sandbox/` - experiments and scratch work
- `docs/` - documentation and design decisions

## Setup

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -e .

## Configuration

Create a local configuration file by copying the template:

```bash
cp .env.example .env
```

On Windows, you can simply copy the file in File Explorer and rename it to `.env`.

Then edit `.env` and provide the appropriate values for your local environment. The `.env` file is intentionally excluded from Git because it may contain secrets such as API keys and passwords.