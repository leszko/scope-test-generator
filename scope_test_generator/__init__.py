"""Test generator plugin for Scope."""

import scope_worker.plugins

from .pipeline import TestGeneratorPipeline


@scope_worker.plugins.hookimpl
def register_pipelines(register):
    """Register the test generator pipeline."""
    register(TestGeneratorPipeline)


__all__ = ["TestGeneratorPipeline"]
