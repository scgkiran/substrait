# SPDX-License-Identifier: Apache-2.0
from tests.coverage.extensions import build_type_to_short_type


def test_read_substrait_extensions():
    from tests.coverage.extensions import Extension

    registry = Extension.read_substrait_extensions("../extensions")
    assert len(registry.registry) >= 161
    num_overloads = sum([len(f) for f in registry.registry.values()])
    assert num_overloads >= 510
    assert len(registry.dependencies) >= 13
    assert len(registry.scalar_functions) >= 162
    assert len(registry.aggregate_functions) >= 29
    assert len(registry.window_functions) >= 0


def test_build_type_to_short_type():
    long_to_short = build_type_to_short_type()
    assert long_to_short["i64"] == "i64"
    assert long_to_short["fp64"] == "fp64"
    assert long_to_short["timestamp"] == "ts"
    assert long_to_short["timestamp_tz"] == "tstz"
    assert long_to_short["precision_timestamp"] == "pts"
    assert long_to_short["precision_timestamp_tz"] == "ptstz"
    assert long_to_short["interval_year"] == "iyear"
    assert long_to_short["interval_day"] == "iday"
    assert long_to_short["decimal"] == "dec"
    assert long_to_short["boolean"] == "bool"
    assert long_to_short["string"] == "str"
    assert long_to_short["binary"] == "vbin"
    assert long_to_short["fixedbinary"] == "fbin"
    assert long_to_short["fixedchar"] == "fchar"
    assert long_to_short["varchar"] == "vchar"
    assert long_to_short["list"] == "list"
    assert long_to_short["map"] == "map"
    assert long_to_short["struct"] == "struct"

