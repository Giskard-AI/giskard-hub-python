"""Type definitions for the Giskard Hub API.

This module provides all type definitions used throughout the SDK, organized by category:
- Common types: Generic response wrappers and shared types
- Core models: Main domain objects (Agent, Dataset, Project, etc.)
- API resources: API-specific resource representations
- Parameters: Input parameters for API operations (Create, Update, List, etc.)
- Responses: Response types for specific operations
- Enums: Enumerated types and literals
"""

from __future__ import annotations

from .user import User as User

# ==============================================================================
# Core Models - Main domain objects
# ==============================================================================
from .agent import Agent as Agent, AgentOutput as AgentOutput

# ==============================================================================
# Scan Probe Types (from scans/ subdirectory)
# ==============================================================================
from .scans import (
    Severity as Severity,
    ReviewStatus as ReviewStatus,
    ScanProbeResult as ScanProbeResult,
    ScanProbeAttempt as ScanProbeAttempt,
    AttemptUpdateParams as AttemptUpdateParams,
)

# ==============================================================================
# Common Types - Generic response wrappers and shared utilities
# ==============================================================================
from .common import (
    APIResponse as APIResponse,
    APIPaginatedMetadata as APIPaginatedMetadata,
    APIPaginatedResponse as APIPaginatedResponse,
    APIResponseWithIncluded as APIResponseWithIncluded,
)

# Headers
from .header import Header as Header
from .metric import Metric as Metric
from .dataset import Dataset as Dataset
from .test_case import TestCase as TestCase, TestCaseComment as TestCaseComment

# ==============================================================================
# Test Case Comment Types (from test_cases/ subdirectory)
# ==============================================================================
from .test_cases import (
    CommentAddParams as CommentAddParams,
    CommentEditParams as CommentEditParams,
)

# ==============================================================================
# Enums and Literals
# ==============================================================================
from .action_type import ActionType as ActionType

# ==============================================================================
# Evaluation Results Types (from evaluations/ subdirectory)
# ==============================================================================
from .evaluations import (
    TaskState as TaskState,
    FailureCategory as FailureCategory,
    ResultListParams as ResultListParams,
    ResultSearchParams as ResultSearchParams,
    ResultUpdateParams as ResultUpdateParams,
    FailureCategoryParam as FailureCategoryParam,
    ResultRetrieveParams as ResultRetrieveParams,
    ResultUpdateVisibilityParams as ResultUpdateVisibilityParams,
    ResultSubmitLocalOutputParams as ResultSubmitLocalOutputParams,
    TestCaseEvaluationAPIResource as TestCaseEvaluationAPIResource,
)

# Scan types and responses
from .scan_result import ScanResult as ScanResult, ScanCategory as ScanCategory
from .task_status import TaskStatus as TaskStatus

# ==============================================================================
# Shared Component Types - Used across multiple resources
# ==============================================================================
# Chat and messaging
from .chat_message import ChatMessage as ChatMessage
from .header_param import HeaderParam as HeaderParam
from .model_output import ModelOutput as ModelOutput

# Models and outputs
from .minimal_model import MinimalModel as MinimalModel
from .task_priority import TaskPriority as TaskPriority

# Task progress
from .task_progress import TaskProgress as TaskProgress
from .dataset_subset import DatasetSubset as DatasetSubset
from .knowledge_base import KnowledgeBase as KnowledgeBase
from .audit_diff_item import AuditDiffItem as AuditDiffItem

# Audit types and responses
from .audit_diff_kind import AuditDiffKind as AuditDiffKind

# Execution status and errors
from .execution_error import ExecutionError as ExecutionError

# Metadata and annotations
from .metadata_params import MetadataParams as MetadataParams
from .frequency_option import FrequencyOption as FrequencyOption
from .scan_list_params import ScanListParams as ScanListParams
from .task_list_params import TaskListParams as TaskListParams
from .agent_list_params import AgentListParams as AgentListParams

# ==============================================================================
# Generic API Response Wrappers
# ==============================================================================
from .check_list_params import CheckListParams as CheckListParams

# ==============================================================================
# Check/Evaluation Configuration Types
# ==============================================================================
from .conformity_params import ConformityParams as ConformityParams
from .output_annotation import OutputAnnotation as OutputAnnotation

# Reference types
from .task_api_resource import TaskAPIResource as TaskAPIResource

# ==============================================================================
# API Resources - API-specific resource representations
# ==============================================================================
from .audit_api_resource import AuditAPIResource as AuditAPIResource
from .chat_message_param import ChatMessageParam as ChatMessageParam
from .check_api_resource import CheckAPIResource as CheckAPIResource
from .correctness_params import CorrectnessParams as CorrectnessParams
from .model_output_param import ModelOutputParam as ModelOutputParam
from .paginated_metadata import PaginatedMetadata as PaginatedMetadata

# Project responses
# (Project responses now use generic APIResponse[ProjectAPIResource] and APIResponse[List[ProjectAPIResource])
# ==============================================================================
# Scan Types
# ==============================================================================
# Scan parameters
from .scan_create_params import ScanCreateParams as ScanCreateParams

# ==============================================================================
# Task Types
# ==============================================================================
# Task parameters
from .task_create_params import TaskCreateParams as TaskCreateParams
from .task_update_params import TaskUpdateParams as TaskUpdateParams

# ==============================================================================
# Agent Types
# ==============================================================================
# Agent parameters
from .agent_api_reference import AgentAPIReference as AgentAPIReference
from .agent_create_params import AgentCreateParams as AgentCreateParams
from .agent_update_params import AgentUpdateParams as AgentUpdateParams
from .audit_search_params import AuditSearchParams as AuditSearchParams

# ==============================================================================
# Check Types
# ==============================================================================
# Check parameters
from .check_create_params import CheckCreateParams as CheckCreateParams
from .check_update_params import CheckUpdateParams as CheckUpdateParams
from .dataset_list_params import DatasetListParams as DatasetListParams
from .groundedness_params import GroundednessParams as GroundednessParams
from .minimal_model_param import MinimalModelParam as MinimalModelParam
from .string_match_params import StringMatchParams as StringMatchParams
from .task_progress_param import TaskProgressParam as TaskProgressParam
from .test_case_reference import TestCaseReferencence as TestCaseReferencence
from .dataset_subset_param import DatasetSubsetParam as DatasetSubsetParam
from .project_api_resource import ProjectAPIResource as ProjectAPIResource
from .scan_retrieve_params import ScanRetrieveParams as ScanRetrieveParams
from .scheduled_evaluation import ScheduledEvaluation as ScheduledEvaluation

# ==============================================================================
# Dataset Types
# ==============================================================================
# Dataset parameters
from .dataset_create_params import DatasetCreateParams as DatasetCreateParams
from .dataset_update_params import DatasetUpdateParams as DatasetUpdateParams
from .execution_error_param import ExecutionErrorParam as ExecutionErrorParam
from .metadata_params_param import MetadataParamsParam as MetadataParamsParam

# ==============================================================================
# Project Types
# ==============================================================================
# Project parameters
from .project_create_params import ProjectCreateParams as ProjectCreateParams
from .project_update_params import ProjectUpdateParams as ProjectUpdateParams
from .scenario_api_resource import ScenarioAPIResource as ScenarioAPIResource
from .error_execution_status import ErrorExecutionStatus as ErrorExecutionStatus
from .evaluation_list_params import EvaluationListParams as EvaluationListParams

# Test case responses
# (Test case responses now use generic APIResponse[TestCase] and APIResponse[List[TestCase])
# ==============================================================================
# Scenario Types
# ==============================================================================
# Scenario parameters
from .scenario_create_params import ScenarioCreateParams as ScenarioCreateParams
from .scenario_update_params import ScenarioUpdateParams as ScenarioUpdateParams
from .test_case_check_config import TestCaseCheckConfig as TestCaseCheckConfig
from .conformity_params_param import ConformityParamsParam as ConformityParamsParam
from .evaluation_api_resource import EvaluationAPIResource as EvaluationAPIResource
from .probe_attempt_reference import ProbeAttemptReference as ProbeAttemptReference
from .scan_bulk_delete_params import ScanBulkDeleteParams as ScanBulkDeleteParams
from .scenario_preview_params import ScenarioPreviewParams as ScenarioPreviewParams
from .task_bulk_delete_params import TaskBulkDeleteParams as TaskBulkDeleteParams

# ==============================================================================
# Test Case Types
# ==============================================================================
# Test case parameters
from .test_case_create_params import TestCaseCreateParams as TestCaseCreateParams
from .test_case_update_params import TestCaseUpdateParams as TestCaseUpdateParams
from .agent_bulk_delete_params import AgentBulkDeleteParams as AgentBulkDeleteParams

# Scenario responses
# (Scenario responses now use generic APIResponse[ScenarioAPIResource], APIResponse[ScenarioPreviewAPIResource], and APIResponse[List[ScenarioAPIResource])
# ==============================================================================
# Audit Types
# ==============================================================================
# Audit parameters
from .audit_list_entity_params import AuditListEntityParams as AuditListEntityParams
from .check_bulk_delete_params import CheckBulkDeleteParams as CheckBulkDeleteParams
from .correctness_params_param import CorrectnessParamsParam as CorrectnessParamsParam

# ==============================================================================
# Evaluation Types
# ==============================================================================
# Evaluation parameters
from .evaluation_create_params import EvaluationCreateParams as EvaluationCreateParams

# Evaluation responses
from .evaluation_update_params import EvaluationUpdateParams as EvaluationUpdateParams
from .success_execution_status import SuccessExecutionStatus as SuccessExecutionStatus

# Agent responses
from .groundedness_params_param import GroundednessParamsParam as GroundednessParamsParam
from .string_match_params_param import StringMatchParamsParam as StringMatchParamsParam
from .audit_display_api_resource import AuditDisplayAPIResource as AuditDisplayAPIResource
from .chat_message_with_metadata import ChatMessageWithMetadata as ChatMessageWithMetadata
from .dataset_bulk_delete_params import DatasetBulkDeleteParams as DatasetBulkDeleteParams

# Dataset search types
from .simple_test_case_api_resource import SimpleTestCaseAPIResource as SimpleTestCaseAPIResource
from .dataset_test_case_check_counts import DatasetTestCaseCheckCounts as DatasetTestCaseCheckCounts
from .dataset_test_case_status_counts import DatasetTestCaseStatusCounts as DatasetTestCaseStatusCounts
from .dataset_test_case_tag_counts import DatasetTestCaseTagCounts as DatasetTestCaseTagCounts
from .dataset_test_cases_search_filters import (
    DatasetTestCasesSearchFilters as DatasetTestCasesSearchFilters,
    DatasetTestCasesSearchFiltersParam as DatasetTestCasesSearchFiltersParam,
)
from .dataset_test_cases_sort_by import (
    DatasetTestCasesSortBy as DatasetTestCasesSortBy,
    DatasetTestCasesSortByParam as DatasetTestCasesSortByParam,
)
from .dataset_search_test_cases_params import DatasetSearchTestCasesParams as DatasetSearchTestCasesParams
from .dataset_search_selection_summary_params import (
    DatasetSearchSelectionSummaryParams as DatasetSearchSelectionSummaryParams,
)
from .dataset_test_case_selection_summary_api_resource import (
    DatasetTestCaseSelectionSummaryAPIResource as DatasetTestCaseSelectionSummaryAPIResource,
)

# Dataset responses
from .evaluation_retrieve_params import EvaluationRetrieveParams as EvaluationRetrieveParams
from .knowledge_base_list_params import KnowledgeBaseListParams as KnowledgeBaseListParams
from .project_bulk_delete_params import ProjectBulkDeleteParams as ProjectBulkDeleteParams
from .semantic_similarity_params import SemanticSimilarityParams as SemanticSimilarityParams
from .agent_test_connection_params import AgentTestConnectionParams as AgentTestConnectionParams
from .error_execution_status_param import ErrorExecutionStatusParam as ErrorExecutionStatusParam
from .evaluation_run_single_params import EvaluationRunSingleParams as EvaluationRunSingleParams

# Check responses
# (Check responses now use generic APIResponse[CheckAPIResource] and APIResponse[List[CheckAPIResource])
# ==============================================================================
# Knowledge Base Types
# ==============================================================================
# Knowledge base parameters
from .knowledge_base_create_params import KnowledgeBaseCreateParams as KnowledgeBaseCreateParams
from .knowledge_base_update_params import KnowledgeBaseUpdateParams as KnowledgeBaseUpdateParams
from .test_case_bulk_delete_params import TestCaseBulkDeleteParams as TestCaseBulkDeleteParams
from .test_case_bulk_update_params import TestCaseBulkUpdateParams as TestCaseBulkUpdateParams
from .test_case_check_config_param import TestCaseCheckConfigParam as TestCaseCheckConfigParam
from .evaluation_bulk_delete_params import EvaluationBulkDeleteParams as EvaluationBulkDeleteParams
from .scenario_preview_api_resource import ScenarioPreviewAPIResource as ScenarioPreviewAPIResource
from .evaluation_create_local_params import EvaluationCreateLocalParams as EvaluationCreateLocalParams
from .success_execution_status_param import SuccessExecutionStatusParam as SuccessExecutionStatusParam
from .test_case_evaluation_reference import TestCaseEvaluationReference as TestCaseEvaluationReference
from .agent_generate_completion_params import AgentGenerateCompletionParams as AgentGenerateCompletionParams
from .chat_message_with_metadata_param import ChatMessageWithMetadataParam as ChatMessageWithMetadataParam
from .scheduled_evaluation_list_params import ScheduledEvaluationListParams as ScheduledEvaluationListParams
from .semantic_similarity_params_param import SemanticSimilarityParamsParam as SemanticSimilarityParamsParam
from .agent_autofill_description_params import AgentAutofillDescriptionParams as AgentAutofillDescriptionParams
from .knowledge_base_bulk_delete_params import KnowledgeBaseBulkDeleteParams as KnowledgeBaseBulkDeleteParams

# ==============================================================================
# Scheduled Evaluation Types
# ==============================================================================
# Scheduled evaluation parameters
from .scheduled_evaluation_create_params import ScheduledEvaluationCreateParams as ScheduledEvaluationCreateParams

# Scheduled evaluation responses
from .scheduled_evaluation_update_params import ScheduledEvaluationUpdateParams as ScheduledEvaluationUpdateParams
from .dataset_generate_adversarial_params import DatasetGenerateAdversarialParams as DatasetGenerateAdversarialParams
from .scheduled_evaluation_retrieve_params import ScheduledEvaluationRetrieveParams as ScheduledEvaluationRetrieveParams
from .dataset_generate_document_based_params import (
    DatasetGenerateDocumentBasedParams as DatasetGenerateDocumentBasedParams,
)
from .dataset_generate_scenario_based_params import (
    DatasetGenerateScenarioBasedParams as DatasetGenerateScenarioBasedParams,
)
from .knowledge_base_search_documents_params import (
    KnowledgeBaseSearchDocumentsParams as KnowledgeBaseSearchDocumentsParams,
)
from .scheduled_evaluation_bulk_delete_params import (
    ScheduledEvaluationBulkDeleteParams as ScheduledEvaluationBulkDeleteParams,
)
from .knowledge_base_document_row_api_resource import (
    KnowledgeBaseDocumentRowAPIResource as KnowledgeBaseDocumentRowAPIResource,
)
from .knowledge_base_document_detail_api_resource import (
    KnowledgeBaseDocumentDetailAPIResource as KnowledgeBaseDocumentDetailAPIResource,
)
from .scheduled_evaluation_list_evaluations_params import (
    ScheduledEvaluationListEvaluationsParams as ScheduledEvaluationListEvaluationsParams,
)

# Knowledge base responses

__all__ = [
    # Common types
    "APIResponse",
    "APIPaginatedResponse",
    "APIPaginatedMetadata",
    "APIResponseWithIncluded",
    # Core models
    "Agent",
    "AgentOutput",
    "Dataset",
    "TestCase",
    "TestCaseComment",
    "KnowledgeBase",
    "ScheduledEvaluation",
    "User",
    # API resources
    "AuditAPIResource",
    "CheckAPIResource",
    "EvaluationAPIResource",
    "ProjectAPIResource",
    "ScenarioAPIResource",
    "ScenarioPreviewAPIResource",
    "TaskAPIResource",
    "KnowledgeBaseDocumentRowAPIResource",
    "KnowledgeBaseDocumentDetailAPIResource",
    # Reference types
    "ProbeAttemptReference",
    "TestCaseReferencence",
    "TestCaseEvaluationReference",
    # Agent types
    "AgentAPIReference",
    "AgentCreateParams",
    "AgentUpdateParams",
    "AgentListParams",
    "AgentBulkDeleteParams",
    "AgentTestConnectionParams",
    "AgentGenerateCompletionParams",
    "AgentAutofillDescriptionParams",
    # Dataset types
    "DatasetCreateParams",
    "DatasetUpdateParams",
    "DatasetListParams",
    "DatasetBulkDeleteParams",
    "DatasetGenerateDocumentBasedParams",
    "DatasetGenerateScenarioBasedParams",
    "DatasetGenerateAdversarialParams",
    "DatasetSubset",
    "DatasetSubsetParam",
    # Dataset search types
    "SimpleTestCaseAPIResource",
    "DatasetTestCaseCheckCounts",
    "DatasetTestCaseStatusCounts",
    "DatasetTestCaseTagCounts",
    "DatasetTestCasesSearchFilters",
    "DatasetTestCasesSearchFiltersParam",
    "DatasetTestCasesSortBy",
    "DatasetTestCasesSortByParam",
    "DatasetSearchTestCasesParams",
    "DatasetSearchSelectionSummaryParams",
    "DatasetTestCaseSelectionSummaryAPIResource",
    # Evaluation types
    "EvaluationCreateParams",
    "EvaluationCreateLocalParams",
    "EvaluationUpdateParams",
    "EvaluationListParams",
    "EvaluationRetrieveParams",
    "EvaluationBulkDeleteParams",
    "EvaluationRunSingleParams",
    # Project types
    "ProjectCreateParams",
    "ProjectUpdateParams",
    "ProjectBulkDeleteParams",
    # Scan types
    "ScanCreateParams",
    "ScanListParams",
    "ScanRetrieveParams",
    "ScanBulkDeleteParams",
    "ScanResult",
    "ScanCategory",
    # Check types
    "CheckCreateParams",
    "CheckUpdateParams",
    "CheckListParams",
    "CheckBulkDeleteParams",
    # Task types
    "TaskCreateParams",
    "TaskUpdateParams",
    "TaskListParams",
    "TaskBulkDeleteParams",
    "TaskStatus",
    "TaskPriority",
    # Knowledge base types
    "KnowledgeBaseCreateParams",
    "KnowledgeBaseUpdateParams",
    "KnowledgeBaseListParams",
    "KnowledgeBaseBulkDeleteParams",
    "KnowledgeBaseSearchDocumentsParams",
    # Scheduled evaluation types
    "ScheduledEvaluationCreateParams",
    "ScheduledEvaluationUpdateParams",
    "ScheduledEvaluationListParams",
    "ScheduledEvaluationRetrieveParams",
    "ScheduledEvaluationBulkDeleteParams",
    "ScheduledEvaluationListEvaluationsParams",
    # Test case types
    "TestCaseCreateParams",
    "TestCaseUpdateParams",
    "TestCaseBulkDeleteParams",
    "TestCaseBulkUpdateParams",
    "TestCaseCheckConfig",
    "TestCaseCheckConfigParam",
    # Scenario types
    "ScenarioCreateParams",
    "ScenarioUpdateParams",
    "ScenarioPreviewParams",
    # Audit types
    "AuditListEntityParams",
    "AuditSearchParams",
    "AuditDiffKind",
    "AuditDiffItem",
    "AuditDisplayAPIResource",
    # Shared component types
    "ChatMessage",
    "ChatMessageParam",
    "ChatMessageWithMetadata",
    "ChatMessageWithMetadataParam",
    "Header",
    "HeaderParam",
    "MinimalModel",
    "MinimalModelParam",
    "ModelOutput",
    "ModelOutputParam",
    "ExecutionError",
    "ExecutionErrorParam",
    "ErrorExecutionStatus",
    "ErrorExecutionStatusParam",
    "SuccessExecutionStatus",
    "SuccessExecutionStatusParam",
    "MetadataParams",
    "MetadataParamsParam",
    "OutputAnnotation",
    "PaginatedMetadata",
    "TaskProgress",
    "TaskProgressParam",
    # Check/evaluation configuration
    "ConformityParams",
    "ConformityParamsParam",
    "CorrectnessParams",
    "CorrectnessParamsParam",
    "GroundednessParams",
    "GroundednessParamsParam",
    "SemanticSimilarityParams",
    "SemanticSimilarityParamsParam",
    "StringMatchParams",
    "StringMatchParamsParam",
    # Enums
    "ActionType",
    "FrequencyOption",
    "Metric",
    # Evaluation results types
    "TaskState",
    "FailureCategory",
    "FailureCategoryParam",
    "ResultListParams",
    "ResultSearchParams",
    "ResultRetrieveParams",
    "ResultUpdateParams",
    "ResultUpdateVisibilityParams",
    "ResultSubmitLocalOutputParams",
    "TestCaseEvaluationAPIResource",
    # Scan probe types
    "Severity",
    "ReviewStatus",
    "ScanProbeResult",
    "ScanProbeAttempt",
    "AttemptUpdateParams",
    # Test case comment types
    "CommentAddParams",
    "CommentEditParams",
]
