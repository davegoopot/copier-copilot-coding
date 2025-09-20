# copier-basic
Generic foundation for a coding project.

## Usage with uvx

You can use this copier template with [uvx](https://docs.astral.sh/uv/guides/tools/) to run copier in an isolated environment without installing it globally.

### Prerequisites

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/) which includes uvx

### Running the template

To create a new project using this template:


```bash
uvx copier copy gh:davegoopot/copier-copilot-coding your-new-project
```

## Alternative: Usage with pipx

If you can't install uv, you can use [pipx](https://pipx.pypa.io/) as an alternative to run copier in an isolated environment.

### Prerequisites

- Install [pipx](https://pipx.pypa.io/stable/installation/)

### Running the template

To create a new project using this template:

```bash
pipx run copier copy gh:davegoopot/copier-copilot-coding your-new-project
```

## Updating an Existing Project

If you've already created a project using this template and want to update it with the latest template changes, you can use Copier's update functionality.

### Updating with uvx

Navigate to your existing project directory and run:

```bash
uvx copier update
```

This will update your project with any new changes from the template while preserving your existing answers and customizations.

### Updating with pipx

Navigate to your existing project directory and run:

```bash
pipx run copier update
```

### Note on Updates

- Copier will remember your previous answers and only prompt you for new questions
- Your existing customizations will be preserved where possible
- If there are conflicts, Copier will ask you how to resolve them
- It's recommended to commit your current changes before running an update

