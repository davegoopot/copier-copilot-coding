# cookiecutter-basic
Generic foundation for a coding project.

## Usage with uvx

You can use this cookiecutter template with [uvx](https://docs.astral.sh/uv/guides/tools/) to run cookiecutter in an isolated environment without installing it globally.

### Prerequisites

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/) which includes uvx

### Running the template

To create a new project using this template:

```bash
uvx cookiecutter https://github.com/davegoopot/cookiecutter-basic
```

Or if you have this repository cloned locally:

```bash
uvx cookiecutter /path/to/cookiecutter-basic
```

### Why use uvx?

- **Isolated environment**: Runs cookiecutter in an isolated environment without affecting your global Python installation
- **No installation required**: You don't need to install cookiecutter globally
- **Always up-to-date**: uvx automatically uses the latest version of cookiecutter
- **Clean**: No leftover packages cluttering your system
