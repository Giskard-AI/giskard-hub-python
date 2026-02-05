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

# ==============================================================================
# Common Types - Generic response wrappers and shared utilities
# ==============================================================================

from .common import (
    APIResponse as APIResponse,
    APIListResponse as APIListResponse,
    APIPaginatedResponse as APIPaginatedResponse,
    APIPaginatedMetadata as APIPaginatedMetadata,
    APIResponseWithIncluded as APIResponseWithIncluded,
)

# ==============================================================================
# Core Models - Main domain objects
# ==============================================================================

from .agent import Agent as Agent
from .dataset import Dataset as Dataset
from .test_case import TestCase as TestCase
from .knowledge_base import KnowledgeBase as KnowledgeBase
from .scheduled_evaluation import ScheduledEvaluation as ScheduledEvaluation

# ==============================================================================
# API Resources - API-specific resource representations
# ==============================================================================

from .audit_api_resource import AuditAPIResource as AuditAPIResource
from .check_api_resource import CheckAPIResource as CheckAPIResource
from .evaluation_api_resource import EvaluationAPIResource as EvaluationAPIResource
from .project_api_resource import ProjectAPIResource as ProjectAPIResource
from .scenario_api_resource import ScenarioAPIResource as ScenarioAPIResource
from .scenario_preview_api_resource import ScenarioPreviewAPIResource as ScenarioPreviewAPIResource
from .knowledge_base_document_row_api_resource import KnowledgeBaseDocumentRowAPIResource as KnowledgeBaseDocumentRowAPIResource
from .knowledge_base_document_detail_api_resource import KnowledgeBaseDocumentDetailAPIResource as KnowledgeBaseDocumentDetailAPIResource

# ==============================================================================
# Agent Types
# ==============================================================================

# Agent parameters
from .agent_api_reference import AgentAPIReference as AgentAPIReference
from .agent_create_params import AgentCreateParams as AgentCreateParams
from .agent_update_params import AgentUpdateParams as AgentUpdateParams
from .agent_list_params import AgentListParams as AgentListParams
from .agent_bulk_delete_params import AgentBulkDeleteParams as AgentBulkDeleteParams
from .agent_test_connection_params import AgentTestConnectionParams as AgentTestConnectionParams
from .agent_generate_completion_params import AgentGenerateCompletionParams as AgentGenerateCompletionParams
from .agent_autofill_description_params import AgentAutofillDescriptionParams as AgentAutofillDescriptionParams

# Agent responses
from .agent_list_response import AgentListResponse as AgentListResponse
from .api_response_agent import APIResponseAgent as APIResponseAgent
from .api_response_agent_output import APIResponseAgentOutput as APIResponseAgentOutput

# ==============================================================================
# Dataset Types
# ==============================================================================

# Dataset parameters
from .dataset_create_params import DatasetCreateParams as DatasetCreateParams
from .dataset_update_params import DatasetUpdateParams as DatasetUpdateParams
from .dataset_list_params import DatasetListParams as DatasetListParams
from .dataset_bulk_delete_params import DatasetBulkDeleteParams as DatasetBulkDeleteParams
from .dataset_generate_document_based_params import DatasetGenerateDocumentBasedParams as DatasetGenerateDocumentBasedParams
from .dataset_generate_scenario_based_params import DatasetGenerateScenarioBasedParams as DatasetGenerateScenarioBasedParams
from .dataset_generate_adversarial_params import DatasetGenerateAdversarialParams as DatasetGenerateAdversarialParams
from .dataset_subset import DatasetSubset as DatasetSubset
from .dataset_subset_param import DatasetSubsetParam as DatasetSubsetParam

# Dataset responses
from .dataset_list_response import DatasetListResponse as DatasetListResponse
from .dataset_list_tags_response import DatasetListTagsResponse as DatasetListTagsResponse
from .api_response_dataset import APIResponseDataset as APIResponseDataset

# ==============================================================================
# Evaluation Types
# ==============================================================================

# Evaluation parameters
from .evaluation_create_params import EvaluationCreateParams as EvaluationCreateParams
from .evaluation_create_local_params import EvaluationCreateLocalParams as EvaluationCreateLocalParams
from .evaluation_update_params import EvaluationUpdateParams as EvaluationUpdateParams
from .evaluation_list_params import EvaluationListParams as EvaluationListParams
from .evaluation_retrieve_params import EvaluationRetrieveParams as EvaluationRetrieveParams
from .evaluation_bulk_delete_params import EvaluationBulkDeleteParams as EvaluationBulkDeleteParams
from .evaluation_run_single_params import EvaluationRunSingleParams as EvaluationRunSingleParams

# Evaluation responses
from .evaluation_list_response import EvaluationListResponse as EvaluationListResponse
from .evaluation_retrieve_response import EvaluationRetrieveResponse as EvaluationRetrieveResponse
from .evaluation_run_single_response import EvaluationRunSingleResponse as EvaluationRunSingleResponse
from .api_response_evaluation_api_resource import APIResponseEvaluationAPIResource as APIResponseEvaluationAPIResource

# ==============================================================================
# Project Types
# ==============================================================================

# Project parameters
from .project_create_params import ProjectCreateParams as ProjectCreateParams
from .project_update_params import ProjectUpdateParams as ProjectUpdateParams
from .project_bulk_delete_params import ProjectBulkDeleteParams as ProjectBulkDeleteParams

# Project responses
from .project_list_response import ProjectListResponse as ProjectListResponse
from .api_response_project_api_resource import APIResponseProjectAPIResource as APIResponseProjectAPIResource

# ==============================================================================
# Scan Types
# ==============================================================================

# Scan parameters
from .scan_create_params import ScanCreateParams as ScanCreateParams
from .scan_list_params import ScanListParams as ScanListParams
from .scan_retrieve_params import ScanRetrieveParams as ScanRetrieveParams
from .scan_bulk_delete_params import ScanBulkDeleteParams as ScanBulkDeleteParams

# Scan types and responses
from .scan_result import ScanResult as ScanResult
from .scan_list_response import ScanListResponse as ScanListResponse
from .scan_retrieve_response import ScanRetrieveResponse as ScanRetrieveResponse
from .scan_create_response import ScanCreateResponse as ScanCreateResponse
from .scan_list_categories_response import ScanListCategoriesResponse as ScanListCategoriesResponse
from .scan_list_probes_response import ScanListProbesResponse as ScanListProbesResponse

# ==============================================================================
# Check Types
# ==============================================================================

# Check parameters
from .check_create_params import CheckCreateParams as CheckCreateParams
from .check_update_params import CheckUpdateParams as CheckUpdateParams
from .check_list_params import CheckListParams as CheckListParams
from .check_bulk_delete_params import CheckBulkDeleteParams as CheckBulkDeleteParams

# Check responses
from .check_list_response import CheckListResponse as CheckListResponse
from .api_response_check import APIResponseCheck as APIResponseCheck

# ==============================================================================
# Knowledge Base Types
# ==============================================================================

# Knowledge base parameters
from .knowledge_base_create_params import KnowledgeBaseCreateParams as KnowledgeBaseCreateParams
from .knowledge_base_update_params import KnowledgeBaseUpdateParams as KnowledgeBaseUpdateParams
from .knowledge_base_list_params import KnowledgeBaseListParams as KnowledgeBaseListParams
from .knowledge_base_bulk_delete_params import KnowledgeBaseBulkDeleteParams as KnowledgeBaseBulkDeleteParams
from .knowledge_base_search_documents_params import KnowledgeBaseSearchDocumentsParams as KnowledgeBaseSearchDocumentsParams

# Knowledge base responses
from .knowledge_base_list_response import KnowledgeBaseListResponse as KnowledgeBaseListResponse
from .api_response_knowledge_base import APIResponseKnowledgeBase as APIResponseKnowledgeBase
from .api_response_knowledge_base_document_detail_api_resource import APIResponseKnowledgeBaseDocumentDetailAPIResource as APIResponseKnowledgeBaseDocumentDetailAPIResource
from .paginated_api_response_knowledge_base_document_row_api_resource import PaginatedAPIResponseKnowledgeBaseDocumentRowAPIResource as PaginatedAPIResponseKnowledgeBaseDocumentRowAPIResource

# ==============================================================================
# Scheduled Evaluation Types
# ==============================================================================

# Scheduled evaluation parameters
from .scheduled_evaluation_create_params import ScheduledEvaluationCreateParams as ScheduledEvaluationCreateParams
from .scheduled_evaluation_update_params import ScheduledEvaluationUpdateParams as ScheduledEvaluationUpdateParams
from .scheduled_evaluation_list_params import ScheduledEvaluationListParams as ScheduledEvaluationListParams
from .scheduled_evaluation_retrieve_params import ScheduledEvaluationRetrieveParams as ScheduledEvaluationRetrieveParams
from .scheduled_evaluation_bulk_delete_params import ScheduledEvaluationBulkDeleteParams as ScheduledEvaluationBulkDeleteParams
from .scheduled_evaluation_list_evaluations_params import ScheduledEvaluationListEvaluationsParams as ScheduledEvaluationListEvaluationsParams

# Scheduled evaluation responses
from .scheduled_evaluation_list_response import ScheduledEvaluationListResponse as ScheduledEvaluationListResponse
from .scheduled_evaluation_list_evaluations_response import ScheduledEvaluationListEvaluationsResponse as ScheduledEvaluationListEvaluationsResponse
from .api_response_scheduled_evaluation import APIResponseScheduledEvaluation as APIResponseScheduledEvaluation

# ==============================================================================
# Test Case Types
# ==============================================================================

# Test case parameters
from .test_case_create_params import TestCaseCreateParams as TestCaseCreateParams
from .test_case_update_params import TestCaseUpdateParams as TestCaseUpdateParams
from .test_case_bulk_delete_params import TestCaseBulkDeleteParams as TestCaseBulkDeleteParams
from .test_case_bulk_update_params import TestCaseBulkUpdateParams as TestCaseBulkUpdateParams
from .test_case_check_config import TestCaseCheckConfig as TestCaseCheckConfig
from .test_case_check_config_param import TestCaseCheckConfigParam as TestCaseCheckConfigParam

# Test case responses
from .api_response_test_case import APIResponseTestCase as APIResponseTestCase
from .api_response_list_test_case import APIResponseListTestCase as APIResponseListTestCase

# ==============================================================================
# Scenario Types
# ==============================================================================

# Scenario parameters
from .scenario_create_params import ScenarioCreateParams as ScenarioCreateParams
from .scenario_update_params import ScenarioUpdateParams as ScenarioUpdateParams
from .scenario_preview_params import ScenarioPreviewParams as ScenarioPreviewParams

# Scenario responses
from .api_response_scenario import APIResponseScenario as APIResponseScenario
from .api_response_scenario_preview import APIResponseScenarioPreview as APIResponseScenarioPreview
from .api_response_list_scenario import APIResponseListScenario as APIResponseListScenario

# ==============================================================================
# Audit Types
# ==============================================================================

# Audit parameters
from .audit_list_entity_params import AuditListEntityParams as AuditListEntityParams
from .audit_search_params import AuditSearchParams as AuditSearchParams

# Audit types and responses
from .audit_diff_kind import AuditDiffKind as AuditDiffKind
from .audit_diff_item import AuditDiffItem as AuditDiffItem
from .audit_display_api_response import AuditDisplayAPIResponse as AuditDisplayAPIResponse
from .api_response_audit import APIResponseAudit as APIResponseAudit
from .api_response_audit_display import APIResponseAuditDisplay as APIResponseAuditDisplay

# ==============================================================================
# Shared Component Types - Used across multiple resources
# ==============================================================================

# Chat and messaging
from .chat_message import ChatMessage as ChatMessage
from .chat_message_param import ChatMessageParam as ChatMessageParam
from .chat_message_with_metadata import ChatMessageWithMetadata as ChatMessageWithMetadata
from .chat_message_with_metadata_param import ChatMessageWithMetadataParam as ChatMessageWithMetadataParam

# Headers
from .header import Header as Header
from .header_param import HeaderParam as HeaderParam

# Models and outputs
from .minimal_model import MinimalModel as MinimalModel
from .minimal_model_param import MinimalModelParam as MinimalModelParam
from .model_output import ModelOutput as ModelOutput
from .model_output_param import ModelOutputParam as ModelOutputParam

# Execution status and errors
from .execution_error import ExecutionError as ExecutionError
from .execution_error_param import ExecutionErrorParam as ExecutionErrorParam
from .error_execution_status import ErrorExecutionStatus as ErrorExecutionStatus
from .error_execution_status_param import ErrorExecutionStatusParam as ErrorExecutionStatusParam
from .success_execution_status import SuccessExecutionStatus as SuccessExecutionStatus
from .success_execution_status_param import SuccessExecutionStatusParam as SuccessExecutionStatusParam

# Metadata and annotations
from .metadata_params import MetadataParams as MetadataParams
from .metadata_params_param import MetadataParamsParam as MetadataParamsParam
from .output_annotation import OutputAnnotation as OutputAnnotation
from .paginated_metadata import PaginatedMetadata as PaginatedMetadata

# Task progress
from .task_progress import TaskProgress as TaskProgress
from .task_progress_param import TaskProgressParam as TaskProgressParam

# ==============================================================================
# Check/Evaluation Configuration Types
# ==============================================================================

from .conformity_params import ConformityParams as ConformityParams
from .conformity_params_param import ConformityParamsParam as ConformityParamsParam
from .correctness_params import CorrectnessParams as CorrectnessParams
from .correctness_params_param import CorrectnessParamsParam as CorrectnessParamsParam
from .groundedness_params import GroundednessParams as GroundednessParams
from .groundedness_params_param import GroundednessParamsParam as GroundednessParamsParam
from .semantic_similarity_params import SemanticSimilarityParams as SemanticSimilarityParams
from .semantic_similarity_params_param import SemanticSimilarityParamsParam as SemanticSimilarityParamsParam
from .string_match_params import StringMatchParams as StringMatchParams
from .string_match_params_param import StringMatchParamsParam as StringMatchParamsParam

# ==============================================================================
# Enums and Literals
# ==============================================================================

from .action_type import ActionType as ActionType
from .frequency_option import FrequencyOption as FrequencyOption
from .metric import Metric as Metric

# ==============================================================================
# Evaluation Results Types (from evaluations/ subdirectory)
# ==============================================================================

from .evaluations import (
    TaskState as TaskState,
    FailureCategory as FailureCategory,
    FailureCategoryParam as FailureCategoryParam,
    ResultListParams as ResultListParams,
    ResultListResponse as ResultListResponse,
    ResultSearchParams as ResultSearchParams,
    ResultSearchResponse as ResultSearchResponse,
    ResultRetrieveParams as ResultRetrieveParams,
    ResultRetrieveResponse as ResultRetrieveResponse,
    ResultUpdateParams as ResultUpdateParams,
    ResultUpdateVisibilityParams as ResultUpdateVisibilityParams,
    ResultSubmitLocalOutputParams as ResultSubmitLocalOutputParams,
    TestCaseEvaluationAPIResource as TestCaseEvaluationAPIResource,
    APIResponseTestCaseEvaluationAPIResource as APIResponseTestCaseEvaluationAPIResource,
)

# ==============================================================================
# Scan Probe Types (from scans/ subdirectory)
# ==============================================================================

from .scans import (
    Severity as Severity,
    ReviewStatus as ReviewStatus,
    ScanProbeResult as ScanProbeResult,
    ScanProbeAttempt as ScanProbeAttempt,
    AttemptUpdateParams as AttemptUpdateParams,
    AttemptUpdateResponse as AttemptUpdateResponse,
    ProbeRetrieveResponse as ProbeRetrieveResponse,
    ProbeListAttemptsResponse as ProbeListAttemptsResponse,
)

# ==============================================================================
# Test Case Comment Types (from test_cases/ subdirectory)
# ==============================================================================

from .test_cases import (
    CommentAddParams as CommentAddParams,
    CommentEditParams as CommentEditParams,
    APIResponseTestCaseComment as APIResponseTestCaseComment,
)

# ==============================================================================
# Generic API Response Wrappers
# ==============================================================================

from .api_response_none import APIResponseNone as APIResponseNone
from .api_response_str import APIResponseStr as APIResponseStr

__all__ = [
    # Common types
    "APIResponse",
    "APIListResponse",
    "APIPaginatedResponse",
    "APIPaginatedMetadata",
    "APIResponseWithIncluded",
    # Core models
    "Agent",
    "Dataset",
    "TestCase",
    "KnowledgeBase",
    "ScheduledEvaluation",
    # API resources
    "AuditAPIResource",
    "CheckAPIResource",
    "EvaluationAPIResource",
    "ProjectAPIResource",
    "ScenarioAPIResource",
    "ScenarioPreviewAPIResource",
    "KnowledgeBaseDocumentRowAPIResource",
    "KnowledgeBaseDocumentDetailAPIResource",
    # Agent types
    "AgentAPIReference",
    "AgentCreateParams",
    "AgentUpdateParams",
    "AgentListParams",
    "AgentBulkDeleteParams",
    "AgentTestConnectionParams",
    "AgentGenerateCompletionParams",
    "AgentAutofillDescriptionParams",
    "AgentListResponse",
    "APIResponseAgent",
    "APIResponseAgentOutput",
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
    "DatasetListResponse",
    "DatasetListTagsResponse",
    "APIResponseDataset",
    # Evaluation types
    "EvaluationCreateParams",
    "EvaluationCreateLocalParams",
    "EvaluationUpdateParams",
    "EvaluationListParams",
    "EvaluationRetrieveParams",
    "EvaluationBulkDeleteParams",
    "EvaluationRunSingleParams",
    "EvaluationListResponse",
    "EvaluationRetrieveResponse",
    "EvaluationRunSingleResponse",
    "APIResponseEvaluationAPIResource",
    # Project types
    "ProjectCreateParams",
    "ProjectUpdateParams",
    "ProjectBulkDeleteParams",
    "ProjectListResponse",
    "APIResponseProjectAPIResource",
    # Scan types
    "ScanCreateParams",
    "ScanListParams",
    "ScanRetrieveParams",
    "ScanBulkDeleteParams",
    "ScanResult",
    "ScanListResponse",
    "ScanRetrieveResponse",
    "ScanCreateResponse",
    "ScanListCategoriesResponse",
    "ScanListProbesResponse",
    # Check types
    "CheckCreateParams",
    "CheckUpdateParams",
    "CheckListParams",
    "CheckBulkDeleteParams",
    "CheckListResponse",
    "APIResponseCheck",
    # Knowledge base types
    "KnowledgeBaseCreateParams",
    "KnowledgeBaseUpdateParams",
    "KnowledgeBaseListParams",
    "KnowledgeBaseBulkDeleteParams",
    "KnowledgeBaseSearchDocumentsParams",
    "KnowledgeBaseListResponse",
    "APIResponseKnowledgeBase",
    "APIResponseKnowledgeBaseDocumentDetailAPIResource",
    "PaginatedAPIResponseKnowledgeBaseDocumentRowAPIResource",
    # Scheduled evaluation types
    "ScheduledEvaluationCreateParams",
    "ScheduledEvaluationUpdateParams",
    "ScheduledEvaluationListParams",
    "ScheduledEvaluationRetrieveParams",
    "ScheduledEvaluationBulkDeleteParams",
    "ScheduledEvaluationListEvaluationsParams",
    "ScheduledEvaluationListResponse",
    "ScheduledEvaluationListEvaluationsResponse",
    "APIResponseScheduledEvaluation",
    # Test case types
    "TestCaseCreateParams",
    "TestCaseUpdateParams",
    "TestCaseBulkDeleteParams",
    "TestCaseBulkUpdateParams",
    "TestCaseCheckConfig",
    "TestCaseCheckConfigParam",
    "APIResponseTestCase",
    "APIResponseListTestCase",
    # Scenario types
    "ScenarioCreateParams",
    "ScenarioUpdateParams",
    "ScenarioPreviewParams",
    "APIResponseScenario",
    "APIResponseScenarioPreview",
    "APIResponseListScenario",
    # Audit types
    "AuditListEntityParams",
    "AuditSearchParams",
    "AuditDiffKind",
    "AuditDiffItem",
    "AuditDisplayAPIResponse",
    "APIResponseAudit",
    "APIResponseAuditDisplay",
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
    # Generic wrappers
    "APIResponseNone",
    "APIResponseStr",
    # Evaluation results types
    "TaskState",
    "FailureCategory",
    "FailureCategoryParam",
    "ResultListParams",
    "ResultListResponse",
    "ResultSearchParams",
    "ResultSearchResponse",
    "ResultRetrieveParams",
    "ResultRetrieveResponse",
    "ResultUpdateParams",
    "ResultUpdateVisibilityParams",
    "ResultSubmitLocalOutputParams",
    "TestCaseEvaluationAPIResource",
    "APIResponseTestCaseEvaluationAPIResource",
    # Scan probe types
    "Severity",
    "ReviewStatus",
    "ScanProbeResult",
    "ScanProbeAttempt",
    "AttemptUpdateParams",
    "AttemptUpdateResponse",
    "ProbeRetrieveResponse",
    "ProbeListAttemptsResponse",
    # Test case comment types
    "CommentAddParams",
    "CommentEditParams",
    "APIResponseTestCaseComment",
]
