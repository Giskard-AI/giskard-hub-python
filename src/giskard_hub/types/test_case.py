"""Deprecated test case aliases of the scenario types."""

from typing import Optional, TypeAlias, TypedDict
from typing_extensions import Required

from .._types import SequenceNotStr
from .scenario import (
    Scenario,
    ScenarioStatus,
    ScenarioComment,
    ScenarioReference,
    ScenarioCreateParams,
    ScenarioUpdateParams,
    ScenarioBulkUpdateParams,
    ScenarioCommentAddParams,
    ScenarioSchemaValidation,
    ScenarioCommentEditParams,
)

__all__ = [
    "TestCase",
    "TestCaseReference",
    "TestCaseComment",
    "TestCaseSchemaValidation",
    "TestCaseStatus",
    "BulkMoveTestCasesParams",
    "TestCaseCreateParams",
    "TestCaseUpdateParams",
    "TestCaseBulkDeleteParams",
    "TestCaseBulkUpdateParams",
    "CommentAddParams",
    "CommentEditParams",
]

TestCaseStatus: TypeAlias = ScenarioStatus


TestCaseComment = ScenarioComment


TestCaseReference = ScenarioReference


TestCaseSchemaValidation = ScenarioSchemaValidation


TestCase = Scenario


TestCaseCreateParams = ScenarioCreateParams
TestCaseUpdateParams = ScenarioUpdateParams
TestCaseBulkUpdateParams = ScenarioBulkUpdateParams


class TestCaseBulkDeleteParams(TypedDict, total=False):
    test_case_ids: Required[SequenceNotStr[str]]


class BulkMoveTestCasesParams(TypedDict, total=False):
    test_case_ids: Required[SequenceNotStr[str]]
    dataset_id: Required[str]
    duplicate: Optional[bool]


CommentAddParams = ScenarioCommentAddParams
CommentEditParams = ScenarioCommentEditParams
