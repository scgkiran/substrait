def test_read_substrait_extensions():
    from tests.coverage.extensions import Extension
    registry = Extension.read_substrait_extensions('../extensions')
    assert len(registry.function_registry) >= 143
    num_overloads = sum([len(f) for f in registry.function_registry.values()])
    assert num_overloads >= 425
    assert len(registry.dependencies) >= 13
    assert len(registry.scalar_functions) >= 162
    assert len(registry.aggregate_functions) >= 29
    assert len(registry.window_functions) >= 0
