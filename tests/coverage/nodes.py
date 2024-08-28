from dataclasses import dataclass
from typing import List


@dataclass
class CaseGroup:
    name: str
    description: str


@dataclass
class CaseLiteral:
    value: str | int | float | list
    type: str


@dataclass
class TestCase:
    function: str
    base_uri: str
    group: CaseGroup
    options: dict
    args: List[CaseLiteral]
    result: CaseLiteral | str
    comment: str


@dataclass
class TestFile:
    version: str
    include: str
    testcases: List[TestCase]
