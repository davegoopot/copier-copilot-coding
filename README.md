# cookiecutter-basic

A basic cookiecutter template for Python projects that includes a `.github/copilot-instructions.md` file and other essential project structure.

## Features

- 📁 Standard Python project structure with `src/` layout
- 🤖 `.github/copilot-instructions.md` file for AI assistance
- 📝 Pre-configured README.md template
- 🧪 Basic test structure with pytest
- 📦 requirements.txt with development dependencies
- 🚫 Comprehensive .gitignore for Python projects
- ⚖️ License templates (MIT, Apache-2.0, GPL-3.0, BSD-3-Clause, AGPL-3.0)
- 🐍 Python version selection (3.8-3.12)

## Usage

### Prerequisites

Install cookiecutter if you haven't already:

```bash
pip install cookiecutter
```

### Generate a new project

```bash
cookiecutter https://github.com/davegoopot/cookiecutter-basic
```

You'll be prompted to enter values for the following:

- **project_name**: The name of your project (e.g., "My Awesome Project")
- **project_slug**: Python package name (auto-generated from project_name)
- **project_description**: Brief description of your project
- **author_name**: Your name
- **author_email**: Your email address
- **version**: Initial version (default: 0.1.0)
- **license**: Choose from MIT, Apache-2.0, GPL-3.0, BSD-3-Clause, or AGPL-3.0
- **python_version**: Target Python version (3.8-3.12)

### What gets created

```
your_project/
├── .github/
│   └── copilot-instructions.md    # AI assistant guidelines
├── src/
│   └── your_project/
│       └── __init__.py            # Package initialization
├── tests/
│   ├── __init__.py
│   └── test_basic.py              # Basic tests
├── .gitignore                     # Python gitignore
├── LICENSE                        # Selected license
├── README.md                      # Project documentation
└── requirements.txt               # Dependencies
```

## The copilot-instructions.md file

The generated project includes a `.github/copilot-instructions.md` file that provides:

- Project overview and description
- Development guidelines (code style, testing, documentation)
- Git practices and workflow
- Project structure documentation
- Common tasks and commands
- AI assistant guidelines for the project

This file helps AI assistants like GitHub Copilot understand your project context and provide better suggestions.

## Contributing

1. Fork this repository
2. Create a feature branch
3. Make your changes
4. Test the template by generating a new project
5. Submit a pull request
