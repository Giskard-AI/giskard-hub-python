"""Type definitions for the Giskard Hub API.

Types are organized by domain into consolidated modules:

- common: Generic response wrappers, filter/order helpers, TaskState, TaskProgress
- chat: ChatMessage, Header and their param variants
- user: User, UserReference
- execution: ExecutionError, execution status types
- agent: Agent, AgentOutput, MinimalAgent and params
- check: Check, assertions, annotations and params
- audit: Audit, AuditDisplay and params
- task: Task, TaskStatus, TaskPriority, references and params
- dataset: Dataset, DatasetSubset and params
- knowledge_base: KnowledgeBase, document types and params
- evaluation: Evaluation, Metric, TestCaseEvaluation, result params
- scan: ScanResult, ScanCategory, ScanProbe types and params
- scenario: Scenario, ScenarioPreview and params
- scheduled_evaluation: ScheduledEvaluation, FrequencyOption and params
- test_case: TestCase, TestCaseComment, comment params
- playground_chat: PlaygroundChat and params
- project: Project and params
"""

# -- common ----------------------------------------------------------------
from .common import (  # noqa: I001
    APIResponse as APIResponse,
    APIPaginatedMetadata as APIPaginatedMetadata,
    APIPaginatedResponse as APIPaginatedResponse,
    APIResponseWithIncluded as APIResponseWithIncluded,
    DateRangeFilterValueParam as DateRangeFilterValueParam,
    FilterValueParam as FilterValueParam,
    ListFilterValueParam as ListFilterValueParam,
    OrderByParam as OrderByParam,
    PaginatedMetadata as PaginatedMetadata,
    TaskProgress as TaskProgress,
    TaskProgressParam as TaskProgressParam,
    TaskState as TaskState,
)

# -- chat ------------------------------------------------------------------
from .chat import (
    ChatMessage as ChatMessage,
    ChatMessageParam as ChatMessageParam,
    ChatMessageWithMetadata as ChatMessageWithMetadata,
    ChatMessageWithMetadataParam as ChatMessageWithMetadataParam,
    Header as Header,
    HeaderParam as HeaderParam,
)

# -- user ------------------------------------------------------------------
from .user import (
    User as User,
    UserReference as UserReference,
)

# -- execution -------------------------------------------------------------
from .execution import (
    ErrorExecutionStatus as ErrorExecutionStatus,
    ErrorExecutionStatusParam as ErrorExecutionStatusParam,
    ExecutionError as ExecutionError,
    ExecutionErrorParam as ExecutionErrorParam,
    SuccessExecutionStatus as SuccessExecutionStatus,
    SuccessExecutionStatusParam as SuccessExecutionStatusParam,
)

# -- agent -----------------------------------------------------------------
from .agent import (
    Agent as Agent,
    AgentAutofillDescriptionParams as AgentAutofillDescriptionParams,
    AgentBulkDeleteParams as AgentBulkDeleteParams,
    AgentCreateParams as AgentCreateParams,
    AgentGenerateCompletionParams as AgentGenerateCompletionParams,
    AgentListParams as AgentListParams,
    AgentOutput as AgentOutput,
    AgentOutputParam as AgentOutputParam,
    AgentReference as AgentReference,
    AgentTestConnectionParams as AgentTestConnectionParams,
    AgentUpdateParams as AgentUpdateParams,
    MinimalAgent as MinimalAgent,
    MinimalAgentParam as MinimalAgentParam,
)

# -- check -----------------------------------------------------------------
from .check import (
    Check as Check,
    CheckBulkDeleteParams as CheckBulkDeleteParams,
    CheckConfig as CheckConfig,
    CheckConfigParam as CheckConfigParam,
    CheckCreateParams as CheckCreateParams,
    CheckListParams as CheckListParams,
    CheckResult as CheckResult,
    CheckType as CheckType,
    CheckTypeParam as CheckTypeParam,
    CheckUpdateParams as CheckUpdateParams,
    ConformityParams as ConformityParams,
    ConformityParamsParam as ConformityParamsParam,
    CorrectnessParams as CorrectnessParams,
    CorrectnessParamsParam as CorrectnessParamsParam,
    GroundednessParams as GroundednessParams,
    GroundednessParamsParam as GroundednessParamsParam,
    MetadataParams as MetadataParams,
    MetadataParamsParam as MetadataParamsParam,
    OutputAnnotation as OutputAnnotation,
    SemanticSimilarityParams as SemanticSimilarityParams,
    SemanticSimilarityParamsParam as SemanticSimilarityParamsParam,
    StringMatchParams as StringMatchParams,
    StringMatchParamsParam as StringMatchParamsParam,
    TestCaseCheckConfig as TestCaseCheckConfig,
    TestCaseCheckConfigParam as TestCaseCheckConfigParam,
)

# -- audit -----------------------------------------------------------------
from .audit import (
    ActionType as ActionType,
    Audit as Audit,
    AuditDiffItem as AuditDiffItem,
    AuditDiffKind as AuditDiffKind,
    AuditDisplay as AuditDisplay,
    AuditFiltersParam as AuditFiltersParam,
    AuditListEntityParams as AuditListEntityParams,
    AuditOrderByParam as AuditOrderByParam,
    AuditSearchParams as AuditSearchParams,
)

# -- task ------------------------------------------------------------------
from .task import (
    Task as Task,
    TaskBulkDeleteParams as TaskBulkDeleteParams,
    TaskCreateParams as TaskCreateParams,
    TaskListParams as TaskListParams,
    TaskPriority as TaskPriority,
    TaskStatus as TaskStatus,
    TaskUpdateParams as TaskUpdateParams,
)

# -- dataset ---------------------------------------------------------------
from .dataset import (
    Dataset as Dataset,
    DatasetBulkDeleteParams as DatasetBulkDeleteParams,
    DatasetCreateParams as DatasetCreateParams,
    DatasetGenerateAdversarialParams as DatasetGenerateAdversarialParams,
    DatasetGenerateDocumentBasedParams as DatasetGenerateDocumentBasedParams,
    DatasetGenerateScenarioBasedParams as DatasetGenerateScenarioBasedParams,
    DatasetImportParams as DatasetImportParams,
    DatasetListParams as DatasetListParams,
    DatasetReference as DatasetReference,
    DatasetSearchTestCasesParams as DatasetSearchTestCasesParams,
    DatasetSubset as DatasetSubset,
    DatasetSubsetParam as DatasetSubsetParam,
    DatasetUpdateParams as DatasetUpdateParams,
    TestCaseFiltersParam as TestCaseFiltersParam,
    TestCaseOrderByParam as TestCaseOrderByParam,
)

# -- knowledge_base --------------------------------------------------------
from .knowledge_base import (
    KnowledgeBase as KnowledgeBase,
    KnowledgeBaseReference as KnowledgeBaseReference,
    KnowledgeBaseBulkDeleteParams as KnowledgeBaseBulkDeleteParams,
    KnowledgeBaseCreateParams as KnowledgeBaseCreateParams,
    KnowledgeBaseDocumentDetail as KnowledgeBaseDocumentDetail,
    KnowledgeBaseDocumentFiltersParam as KnowledgeBaseDocumentFiltersParam,
    KnowledgeBaseDocumentOrderByParam as KnowledgeBaseDocumentOrderByParam,
    KnowledgeBaseDocumentRow as KnowledgeBaseDocumentRow,
    KnowledgeBaseListParams as KnowledgeBaseListParams,
    KnowledgeBaseSearchDocumentsParams as KnowledgeBaseSearchDocumentsParams,
    KnowledgeBaseUpdateParams as KnowledgeBaseUpdateParams,
    Topic as Topic,
)

# -- evaluation ------------------------------------------------------------
from .evaluation import (
    Evaluation as Evaluation,
    EvaluationReference as EvaluationReference,
    EvaluationBulkDeleteParams as EvaluationBulkDeleteParams,
    EvaluationCreateLocalParams as EvaluationCreateLocalParams,
    EvaluationCreateParams as EvaluationCreateParams,
    EvaluationListParams as EvaluationListParams,
    EvaluationRetrieveParams as EvaluationRetrieveParams,
    EvaluationRunSingleParams as EvaluationRunSingleParams,
    EvaluationUpdateParams as EvaluationUpdateParams,
    FailureCategory as FailureCategory,
    FailureCategoryParam as FailureCategoryParam,
    Metric as Metric,
    ResultFiltersParam as ResultFiltersParam,
    ResultListParams as ResultListParams,
    ResultOrderByParam as ResultOrderByParam,
    ResultRetrieveParams as ResultRetrieveParams,
    ResultSearchParams as ResultSearchParams,
    ResultSubmitLocalOutputParams as ResultSubmitLocalOutputParams,
    ResultUpdateParams as ResultUpdateParams,
    ResultUpdateVisibilityParams as ResultUpdateVisibilityParams,
    TestCaseEvaluation as TestCaseEvaluation,
    TestCaseEvaluationReference as TestCaseEvaluationReference,
)

# -- scan ------------------------------------------------------------------
from .scan import (
    AttemptUpdateParams as AttemptUpdateParams,
    ReviewStatus as ReviewStatus,
    ScanBulkDeleteParams as ScanBulkDeleteParams,
    ScanCategory as ScanCategory,
    ScanCreateParams as ScanCreateParams,
    ScanListParams as ScanListParams,
    ScanProbeAttempt as ScanProbeAttempt,
    ScanProbeAttemptReference as ScanProbeAttemptReference,
    ScanProbeResult as ScanProbeResult,
    ScanResult as ScanResult,
    ScanRetrieveParams as ScanRetrieveParams,
    Severity as Severity,
)

# -- scenario --------------------------------------------------------------
from .scenario import (
    Scenario as Scenario,
    ScenarioCreateParams as ScenarioCreateParams,
    ScenarioPreview as ScenarioPreview,
    ScenarioPreviewParams as ScenarioPreviewParams,
    ScenarioUpdateParams as ScenarioUpdateParams,
)

# -- scheduled_evaluation --------------------------------------------------
from .scheduled_evaluation import (
    FrequencyOption as FrequencyOption,
    ScheduledEvaluation as ScheduledEvaluation,
    ScheduledEvaluationBulkDeleteParams as ScheduledEvaluationBulkDeleteParams,
    ScheduledEvaluationCreateParams as ScheduledEvaluationCreateParams,
    ScheduledEvaluationListEvaluationsParams as ScheduledEvaluationListEvaluationsParams,
    ScheduledEvaluationListParams as ScheduledEvaluationListParams,
    ScheduledEvaluationRetrieveParams as ScheduledEvaluationRetrieveParams,
    ScheduledEvaluationUpdateParams as ScheduledEvaluationUpdateParams,
)

# -- test_case -------------------------------------------------------------
from .test_case import (
    BulkMoveTestCasesParams as BulkMoveTestCasesParams,
    CommentAddParams as CommentAddParams,
    CommentEditParams as CommentEditParams,
    TestCase as TestCase,
    TestCaseReference as TestCaseReference,
    TestCaseBulkDeleteParams as TestCaseBulkDeleteParams,
    TestCaseBulkUpdateParams as TestCaseBulkUpdateParams,
    TestCaseComment as TestCaseComment,
    TestCaseCreateParams as TestCaseCreateParams,
    TestCaseUpdateParams as TestCaseUpdateParams,
)

# -- playground_chat -------------------------------------------------------
from .playground_chat import (
    PlaygroundChat as PlaygroundChat,
    PlaygroundChatBulkDeleteParams as PlaygroundChatBulkDeleteParams,
    PlaygroundChatListParams as PlaygroundChatListParams,
    PlaygroundChatRetrieveParams as PlaygroundChatRetrieveParams,
)

# -- project ---------------------------------------------------------------
from .project import (
    Project as Project,
    ProjectBulkDeleteParams as ProjectBulkDeleteParams,
    ProjectCreateParams as ProjectCreateParams,
    ProjectUpdateParams as ProjectUpdateParams,
)


__all__ = [
    # common
    "APIResponse",
    "APIPaginatedMetadata",
    "APIPaginatedResponse",
    "APIResponseWithIncluded",
    "PaginatedMetadata",
    "TaskState",
    "TaskProgress",
    "TaskProgressParam",
    "FilterValueParam",
    "ListFilterValueParam",
    "DateRangeFilterValueParam",
    "OrderByParam",
    # chat
    "ChatMessage",
    "ChatMessageParam",
    "ChatMessageWithMetadata",
    "ChatMessageWithMetadataParam",
    "Header",
    "HeaderParam",
    # user
    "User",
    "UserReference",
    # execution
    "ExecutionError",
    "ExecutionErrorParam",
    "ErrorExecutionStatus",
    "ErrorExecutionStatusParam",
    "SuccessExecutionStatus",
    "SuccessExecutionStatusParam",
    # agent
    "Agent",
    "AgentReference",
    "AgentOutput",
    "AgentOutputParam",
    "MinimalAgent",
    "MinimalAgentParam",
    "AgentListParams",
    "AgentCreateParams",
    "AgentUpdateParams",
    "AgentBulkDeleteParams",
    "AgentTestConnectionParams",
    "AgentGenerateCompletionParams",
    "AgentAutofillDescriptionParams",
    # check
    "Check",
    "CheckResult",
    "CheckType",
    "CheckTypeParam",
    "ConformityParams",
    "ConformityParamsParam",
    "CorrectnessParams",
    "CorrectnessParamsParam",
    "GroundednessParams",
    "GroundednessParamsParam",
    "StringMatchParams",
    "StringMatchParamsParam",
    "SemanticSimilarityParams",
    "SemanticSimilarityParamsParam",
    "MetadataParams",
    "MetadataParamsParam",
    "OutputAnnotation",
    "CheckConfig",
    "CheckConfigParam",
    "TestCaseCheckConfig",
    "TestCaseCheckConfigParam",
    "CheckListParams",
    "CheckCreateParams",
    "CheckUpdateParams",
    "CheckBulkDeleteParams",
    # audit
    "ActionType",
    "AuditDiffKind",
    "AuditDiffItem",
    "Audit",
    "AuditDisplay",
    "AuditListEntityParams",
    "AuditSearchParams",
    "AuditOrderByParam",
    "AuditFiltersParam",
    # task
    "Task",
    "TaskStatus",
    "TaskPriority",
    "TaskListParams",
    "TaskCreateParams",
    "TaskUpdateParams",
    "TaskBulkDeleteParams",
    # dataset
    "Dataset",
    "DatasetReference",
    "DatasetSubset",
    "DatasetSubsetParam",
    "DatasetListParams",
    "DatasetCreateParams",
    "DatasetImportParams",
    "DatasetUpdateParams",
    "DatasetBulkDeleteParams",
    "DatasetSearchTestCasesParams",
    "TestCaseOrderByParam",
    "TestCaseFiltersParam",
    "DatasetGenerateAdversarialParams",
    "DatasetGenerateDocumentBasedParams",
    "DatasetGenerateScenarioBasedParams",
    # knowledge base
    "KnowledgeBase",
    "KnowledgeBaseReference",
    "Topic",
    "KnowledgeBaseDocumentRow",
    "KnowledgeBaseDocumentDetail",
    "KnowledgeBaseListParams",
    "KnowledgeBaseCreateParams",
    "KnowledgeBaseUpdateParams",
    "KnowledgeBaseBulkDeleteParams",
    "KnowledgeBaseSearchDocumentsParams",
    "KnowledgeBaseDocumentOrderByParam",
    "KnowledgeBaseDocumentFiltersParam",
    # evaluation
    "Metric",
    "Evaluation",
    "EvaluationReference",
    "EvaluationListParams",
    "EvaluationCreateParams",
    "EvaluationUpdateParams",
    "EvaluationRetrieveParams",
    "EvaluationRunSingleParams",
    "EvaluationCreateLocalParams",
    "EvaluationBulkDeleteParams",
    "FailureCategory",
    "FailureCategoryParam",
    "TestCaseEvaluation",
    "TestCaseEvaluationReference",
    "ResultListParams",
    "ResultSearchParams",
    "ResultUpdateParams",
    "ResultRetrieveParams",
    "ResultUpdateVisibilityParams",
    "ResultSubmitLocalOutputParams",
    "ResultFiltersParam",
    "ResultOrderByParam",
    # scan
    "ScanResult",
    "ScanCategory",
    "ScanListParams",
    "ScanCreateParams",
    "ScanRetrieveParams",
    "ScanBulkDeleteParams",
    "Severity",
    "ReviewStatus",
    "ScanProbeResult",
    "ScanProbeAttempt",
    "ScanProbeAttemptReference",
    "AttemptUpdateParams",
    # scenario
    "Scenario",
    "ScenarioPreview",
    "ScenarioCreateParams",
    "ScenarioUpdateParams",
    "ScenarioPreviewParams",
    # scheduled evaluation
    "FrequencyOption",
    "ScheduledEvaluation",
    "ScheduledEvaluationListParams",
    "ScheduledEvaluationCreateParams",
    "ScheduledEvaluationUpdateParams",
    "ScheduledEvaluationRetrieveParams",
    "ScheduledEvaluationBulkDeleteParams",
    "ScheduledEvaluationListEvaluationsParams",
    # test case
    "TestCase",
    "TestCaseReference",
    "TestCaseComment",
    "BulkMoveTestCasesParams",
    "TestCaseCreateParams",
    "TestCaseUpdateParams",
    "TestCaseBulkDeleteParams",
    "TestCaseBulkUpdateParams",
    "CommentAddParams",
    "CommentEditParams",
    # playground chat
    "PlaygroundChat",
    "PlaygroundChatListParams",
    "PlaygroundChatRetrieveParams",
    "PlaygroundChatBulkDeleteParams",
    # project
    "Project",
    "ProjectCreateParams",
    "ProjectUpdateParams",
    "ProjectBulkDeleteParams",
]
