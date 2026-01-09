"""Test generator plugin for Scope."""

from scope.core.plugins import hookimpl

from .pipeline import TestGeneratorPipeline


@hookimpl
def register_pipelines(register):
    """Register the test generator pipeline."""
    register(TestGeneratorPipeline)


__all__ = ["TestGeneratorPipeline"]
