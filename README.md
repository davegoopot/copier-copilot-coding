# copier-basic
Generic foundation for a coding project.

This is a [Copier](https://copier.readthedocs.io/) template for creating new projects. Copier is a library and command-line utility for rendering project templates.

## Usage with uvx

You can use this copier template with [uvx](https://docs.astral.sh/uv/guides/tools/) to run copier in an isolated environment without installing it globally.

### Prerequisites

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/) which includes uvx

### Running the template

To create a new project using this template:

<div style="position: relative; margin: 1em 0;">
<pre style="background-color: #f6f8fa; border-radius: 6px; padding: 16px; font-family: 'SFMono-Regular', 'Consolas', 'Liberation Mono', monospace; overflow: auto;"><code>uvx copier copy gh:davegoopot/copier-copilot-coding your-new-project</code></pre>
<button onclick="navigator.clipboard.writeText('uvx copier copy gh:davegoopot/copier-copilot-coding your-new-project').then(() => { this.textContent = '✓ Copied!'; setTimeout(() => this.textContent = '📋 Copy', 2000); })" style="position: absolute; top: 8px; right: 8px; background: #f6f8fa; border: 1px solid #d0d7de; border-radius: 4px; padding: 4px 8px; font-size: 12px; cursor: pointer; color: #656d76;">📋 Copy</button>
</div>

## Alternative: Usage with pipx

If you can't install uv, you can use [pipx](https://pipx.pypa.io/) as an alternative to run copier in an isolated environment.

### Prerequisites

- Install [pipx](https://pipx.pypa.io/stable/installation/)

### Running the template

To create a new project using this template:

<div style="position: relative; margin: 1em 0;">
<pre style="background-color: #f6f8fa; border-radius: 6px; padding: 16px; font-family: 'SFMono-Regular', 'Consolas', 'Liberation Mono', monospace; overflow: auto;"><code>pipx run copier copy gh:davegoopot/copier-copilot-coding your-new-project</code></pre>
<button onclick="navigator.clipboard.writeText('pipx run copier copy gh:davegoopot/copier-copilot-coding your-new-project').then(() => { this.textContent = '✓ Copied!'; setTimeout(() => this.textContent = '📋 Copy', 2000); })" style="position: absolute; top: 8px; right: 8px; background: #f6f8fa; border: 1px solid #d0d7de; border-radius: 4px; padding: 4px 8px; font-size: 12px; cursor: pointer; color: #656d76;">📋 Copy</button>
</div>

## Updating an Existing Project

If you've already created a project using this template and want to update it with the latest template changes, you can use Copier's update functionality.

### Updating with uvx

Navigate to your existing project directory and run:

<div style="position: relative; margin: 1em 0;">
<pre style="background-color: #f6f8fa; border-radius: 6px; padding: 16px; font-family: 'SFMono-Regular', 'Consolas', 'Liberation Mono', monospace; overflow: auto;"><code>uvx copier update</code></pre>
<button onclick="navigator.clipboard.writeText('uvx copier update').then(() => { this.textContent = '✓ Copied!'; setTimeout(() => this.textContent = '📋 Copy', 2000); })" style="position: absolute; top: 8px; right: 8px; background: #f6f8fa; border: 1px solid #d0d7de; border-radius: 4px; padding: 4px 8px; font-size: 12px; cursor: pointer; color: #656d76;">📋 Copy</button>
</div>

This will update your project with any new changes from the template while preserving your existing answers and customizations.

### Updating with pipx

Navigate to your existing project directory and run:

<div style="position: relative; margin: 1em 0;">
<pre style="background-color: #f6f8fa; border-radius: 6px; padding: 16px; font-family: 'SFMono-Regular', 'Consolas', 'Liberation Mono', monospace; overflow: auto;"><code>pipx run copier update</code></pre>
<button onclick="navigator.clipboard.writeText('pipx run copier update').then(() => { this.textContent = '✓ Copied!'; setTimeout(() => this.textContent = '📋 Copy', 2000); })" style="position: absolute; top: 8px; right: 8px; background: #f6f8fa; border: 1px solid #d0d7de; border-radius: 4px; padding: 4px 8px; font-size: 12px; cursor: pointer; color: #656d76;">📋 Copy</button>
</div>

### Note on Updates

- Copier will remember your previous answers and only prompt you for new questions
- Your existing customizations will be preserved where possible
- If there are conflicts, Copier will ask you how to resolve them
- It's recommended to commit your current changes before running an update

