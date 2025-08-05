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

## Alternative: Usage with pipx

If you can't install uv, you can use [pipx](https://pipx.pypa.io/) as an alternative to run cookiecutter in an isolated environment.

### Prerequisites

- Install [pipx](https://pipx.pypa.io/stable/installation/)

### Running the template

To create a new project using this template:

```bash
pipx run cookiecutter gh:davegoopot/cookiecutter-basic
```

