# Decision 0001: Repository Structure

## Decision

Project AI Engineer will use a hybrid repository structure.

The repository will contain:

- `sandbox/` for notebooks, experiments, prototypes, and exploratory work.
- `enterprise_ai_platform/` for the production-quality flagship application.
- `shared/` for reusable utilities and libraries.
- `docs/` for roadmap notes, engineering notes, and architecture decisions.

## Reasoning

This structure supports two different engineering modes:

1. Exploration
2. Production development

Jupyter notebooks and quick experiments are useful for learning, testing ideas, and exploring data or AI libraries. However, production applications should live in regular Python packages with testing, linting, type checking, and clear structure.

The hybrid approach allows experimentation without letting exploratory code pollute the main application.

## Tradeoffs

### Advantages

- Supports both JupyterLab and VS Code workflows.
- Keeps experiments separate from production code.
- Allows the flagship application to evolve over time.
- Reflects how real AI engineering projects often work.

### Disadvantages

- Requires discipline to move useful experiments into production code.
- Slightly more structure than a simple tutorial repository.

## Status

Accepted.