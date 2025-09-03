# cookiecutter-basic
Generic foundation for a coding project.

## Usage with uvx

You can use this cookiecutter template with [uvx](https://docs.astral.sh/uv/guides/tools/) to run cookiecutter in an isolated environment without installing it globally.

### Prerequisites

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/) which includes uvx

### Running the template

To create a new project using this template:


```bash
uvx cookiecutter gh:davegoopot/cookiecutter-basic
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

## Running on an Existing Folder

If you already have a project folder and want to apply this cookiecutter template to it, you can do so by generating the template in a temporary location and then copying the files you want to your existing project.

### With uvx

```bash
# Generate the template in a temporary directory
uvx cookiecutter --output-dir /tmp gh:davegoopot/cookiecutter-basic

# Copy template files to your existing project (choose one approach):

# Option 1: Copy all files, overwriting existing ones
cp -r /tmp/my_project/* /path/to/your/existing/project/
cp -r /tmp/my_project/.* /path/to/your/existing/project/ 2>/dev/null || true

# Option 2: Copy only specific files you want (e.g., just .github folder)
cp -r /tmp/my_project/.github /path/to/your/existing/project/

# Clean up
rm -rf /tmp/my_project
```

### With pipx

```bash
# Generate the template in a temporary directory
pipx run cookiecutter --output-dir /tmp gh:davegoopot/cookiecutter-basic

# Copy template files to your existing project (choose one approach):

# Option 1: Copy all files, overwriting existing ones
cp -r /tmp/my_project/* /path/to/your/existing/project/
cp -r /tmp/my_project/.* /path/to/your/existing/project/ 2>/dev/null || true

# Option 2: Copy only specific files you want (e.g., just .github folder)
cp -r /tmp/my_project/.github /path/to/your/existing/project/

# Clean up
rm -rf /tmp/my_project
```

**Note:** The template will generate a folder named based on your project name (default: `my_project`). You can customize this by providing different answers when prompted during the cookiecutter execution, or use `--no-input` to accept defaults.

