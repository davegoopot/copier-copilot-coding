# GitHub Copilot Instructions for {{cookiecutter.project_name}}

## Project Overview
{{cookiecutter.project_description}}

## Development Guidelines

### Code Style
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions small and focused on a single responsibility

### Testing
- Write unit tests for all new functionality
- Maintain test coverage above 80%
- Use descriptive test names that explain what is being tested

### Documentation
- Update README.md when adding new features
- Document API endpoints and function parameters
- Include examples in docstrings where helpful

### Git Practices
- Use meaningful commit messages
- Keep commits atomic (one logical change per commit)
- Branch from main for new features
- Use pull requests for code review

## Project Structure
```
{{cookiecutter.project_slug}}/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   └── {{cookiecutter.project_slug}}/
│       └── __init__.py
└── tests/
    └── __init__.py
```

## Common Tasks
- Use `pip install -r requirements.txt` to install dependencies
- Run tests with `python -m pytest`
- Format code with `black` and `isort`
- Check code quality with `flake8` or `pylint`

## AI Assistant Guidelines
When helping with this project:
1. Prioritize code readability and maintainability
2. Suggest appropriate error handling and logging
3. Recommend relevant Python libraries when applicable
4. Consider performance implications for data processing
5. Ensure security best practices are followed