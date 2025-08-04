"""Basic tests for {{cookiecutter.project_name}}"""

import pytest
from src.{{cookiecutter.project_slug}} import __version__


def test_version():
    """Test that version is defined."""
    assert __version__ == "{{cookiecutter.version}}"


def test_import():
    """Test that the package can be imported."""
    import src.{{cookiecutter.project_slug}}
    assert src.{{cookiecutter.project_slug}} is not None