"""Type definitions for the Giskard Hub API.

Types are organized by domain into consolidated modules:

- common: Generic response wrappers, filter/order helpers, TaskState, TaskProgress
- chat: ChatMessage, Header and their param variants
- user: User, UserReference
- execution: ExecutionError, execution status types
- agent: Agent, AgentOutput, MinimalAgent and params
- check: Check, spec, annotations and params
- audit: Audit, AuditDisplay and params
- task: Task, TaskStatus, TaskPriority, references and params
- dataset: Dataset, DatasetSubset and params
- knowledge_base: KnowledgeBase, document types and params
- evaluation: Evaluation, Metric, TestCaseEvaluation, result params
- scan: Scan, ScanCategory, ScanProbe types and params
- prompt_preset: PromptPreset, PromptPresetPreview and params
- scenario: deprecated aliases of the prompt preset types
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
    GroupReference as GroupReference,
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
    AgentInterface as AgentInterface,
    ForwardBinding as ForwardBinding,
    ForwardBindingParam as ForwardBindingParam,
    AggregateBinding as AggregateBinding,
    AggregateBindingParam as AggregateBindingParam,
    AutoBinding as AutoBinding,
    AutoBindingParam as AutoBindingParam,
    GenerateCompletionOutput as GenerateCompletionOutput,
    MinimalAgent as MinimalAgent,
    MinimalAgentParam as MinimalAgentParam,
)

# -- check -----------------------------------------------------------------
from .check import (
    Annotation as Annotation,
    Check as Check,
    CheckBulkDeleteParams as CheckBulkDeleteParams,
    CheckConfig as CheckConfig,
    CheckConfigParam as CheckConfigParam,
    CheckCreateParams as CheckCreateParams,
    CheckListParams as CheckListParams,
    CheckResult as CheckResult,
    CheckSource as CheckSource,
    CheckType as CheckType,
    CheckTypeParam as CheckTypeParam,
    CheckUpdateParams as CheckUpdateParams,
    ConformityParams as ConformityParams,
    ConformityParamsParam as ConformityParamsParam,
    ContextAnnotation as ContextAnnotation,
    ContradictionParams as ContradictionParams,
    ContradictionParamsParam as ContradictionParamsParam,
    EqualsParams as EqualsParams,
    EqualsParamsParam as EqualsParamsParam,
    GreaterThanParams as GreaterThanParams,
    GreaterThanParamsParam as GreaterThanParamsParam,
    GreaterThanEqualsParams as GreaterThanEqualsParams,
    GreaterThanEqualsParamsParam as GreaterThanEqualsParamsParam,
    FlatCheckSpec as FlatCheckSpec,
    FlatCheckSpecParam as FlatCheckSpecParam,
    GroundednessParams as GroundednessParams,
    GroundednessParamsParam as GroundednessParamsParam,
    Interaction as Interaction,
    InteractionCheckConfig as InteractionCheckConfig,
    InteractionCheckConfigParam as InteractionCheckConfigParam,
    InteractionParam as InteractionParam,
    InteractionResultData as InteractionResultData,
    JsonPathRule as JsonPathRule,
    JsonPathRuleParam as JsonPathRuleParam,
    HubConformityParams as HubConformityParams,
    HubConformityParamsParam as HubConformityParamsParam,
    HubCorrectnessParams as HubCorrectnessParams,
    HubCorrectnessParamsParam as HubCorrectnessParamsParam,
    HubGroundednessParams as HubGroundednessParams,
    HubGroundednessParamsParam as HubGroundednessParamsParam,
    HubMetadataParams as HubMetadataParams,
    HubMetadataParamsParam as HubMetadataParamsParam,
    JsonValidParams as JsonValidParams,
    JsonValidParamsParam as JsonValidParamsParam,
    LessThanParams as LessThanParams,
    LessThanParamsParam as LessThanParamsParam,
    LessThanEqualsParams as LessThanEqualsParams,
    LessThanEqualsParamsParam as LessThanEqualsParamsParam,
    LLMJudgeParams as LLMJudgeParams,
    LLMJudgeParamsParam as LLMJudgeParamsParam,
    NotEqualsParams as NotEqualsParams,
    NotEqualsParamsParam as NotEqualsParamsParam,
    ReadabilityParams as ReadabilityParams,
    ReadabilityParamsParam as ReadabilityParamsParam,
    RegexMatchingParams as RegexMatchingParams,
    RegexMatchingParamsParam as RegexMatchingParamsParam,
    AnswerRelevanceParams as AnswerRelevanceParams,
    AnswerRelevanceParamsParam as AnswerRelevanceParamsParam,
    ToxicityParams as ToxicityParams,
    ToxicityParamsParam as ToxicityParamsParam,
    OutputAnnotation as OutputAnnotation,
    SemanticSimilarityParams as SemanticSimilarityParams,
    SemanticSimilarityParamsParam as SemanticSimilarityParamsParam,
    StringMatchingParams as StringMatchingParams,
    StringMatchingParamsParam as StringMatchingParamsParam,
    TestCaseCheckConfigParam as TestCaseCheckConfigParam,
)

# -- audit -----------------------------------------------------------------
from .audit import (
    ActionType as ActionType,
    Audit as Audit,
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
    DatasetGeneratePresetBasedParams as DatasetGeneratePresetBasedParams,
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
    DivergenceWarning as DivergenceWarning,
    Evaluation as Evaluation,
    EvaluationReference as EvaluationReference,
    EvaluationBulkDeleteParams as EvaluationBulkDeleteParams,
    EvaluationCreateLocalParams as EvaluationCreateLocalParams,
    EvaluationCreateParams as EvaluationCreateParams,
    EvaluationListParams as EvaluationListParams,
    EvaluationRetrieveParams as EvaluationRetrieveParams,
    EvaluationRunInteractionChecksParams as EvaluationRunInteractionChecksParams,
    EvaluationUpdateParams as EvaluationUpdateParams,
    EvaluationUploadParams as EvaluationUploadParams,
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
    ScanProbeAttemptUpdateParams as ScanProbeAttemptUpdateParams,
    ReviewStatus as ReviewStatus,
    ScanBulkDeleteParams as ScanBulkDeleteParams,
    ScanCategory as ScanCategory,
    ScanAvailableProbe as ScanAvailableProbe,
    ScanCreateParams as ScanCreateParams,
    ScanListParams as ScanListParams,
    ScanProbeAttempt as ScanProbeAttempt,
    ScanProbeAttemptReference as ScanProbeAttemptReference,
    ScanProbe as ScanProbe,
    Scan as Scan,
    ScanRetrieveParams as ScanRetrieveParams,
    Severity as Severity,
)

# -- prompt_preset ---------------------------------------------------------
from .prompt_preset import (
    PromptPreset as PromptPreset,
    PromptPresetCreateParams as PromptPresetCreateParams,
    PromptPresetPreview as PromptPresetPreview,
    PromptPresetPreviewParams as PromptPresetPreviewParams,
    PromptPresetUpdateParams as PromptPresetUpdateParams,
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
    TestCaseSchemaValidation as TestCaseSchemaValidation,
    TestCaseBulkDeleteParams as TestCaseBulkDeleteParams,
    TestCaseBulkUpdateParams as TestCaseBulkUpdateParams,
    TestCaseComment as TestCaseComment,
    TestCaseCreateParams as TestCaseCreateParams,
    TestCaseStatus as TestCaseStatus,
    TestCaseUpdateParams as TestCaseUpdateParams,
)

# -- playground_chat -------------------------------------------------------
from .playground_chat import (
    PlaygroundChat as PlaygroundChat,
    PlaygroundExchange as PlaygroundExchange,
    PlaygroundChatBulkDeleteParams as PlaygroundChatBulkDeleteParams,
    PlaygroundChatCreateParams as PlaygroundChatCreateParams,
    PlaygroundChatListParams as PlaygroundChatListParams,
    PlaygroundChatRetrieveParams as PlaygroundChatRetrieveParams,
    PlaygroundChatUpdateParams as PlaygroundChatUpdateParams,
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
    "GroupReference",
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
    "AgentInterface",
    "ForwardBinding",
    "ForwardBindingParam",
    "AggregateBinding",
    "AggregateBindingParam",
    "AutoBinding",
    "AutoBindingParam",
    "GenerateCompletionOutput",
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
    "CheckSource",
    "CheckType",
    "CheckTypeParam",
    "ConformityParams",
    "ConformityParamsParam",
    "ContradictionParams",
    "ContradictionParamsParam",
    "EqualsParams",
    "EqualsParamsParam",
    "GreaterThanParams",
    "GreaterThanParamsParam",
    "GreaterThanEqualsParams",
    "GreaterThanEqualsParamsParam",
    "FlatCheckSpec",
    "FlatCheckSpecParam",
    "GroundednessParams",
    "GroundednessParamsParam",
    "Interaction",
    "InteractionCheckConfig",
    "InteractionCheckConfigParam",
    "InteractionParam",
    "InteractionResultData",
    "StringMatchingParams",
    "StringMatchingParamsParam",
    "SemanticSimilarityParams",
    "SemanticSimilarityParamsParam",
    "HubConformityParams",
    "HubConformityParamsParam",
    "HubCorrectnessParams",
    "HubCorrectnessParamsParam",
    "HubGroundednessParams",
    "HubGroundednessParamsParam",
    "HubMetadataParams",
    "HubMetadataParamsParam",
    "JsonValidParams",
    "JsonValidParamsParam",
    "LessThanParams",
    "LessThanParamsParam",
    "LessThanEqualsParams",
    "LessThanEqualsParamsParam",
    "LLMJudgeParams",
    "LLMJudgeParamsParam",
    "NotEqualsParams",
    "NotEqualsParamsParam",
    "ReadabilityParams",
    "ReadabilityParamsParam",
    "RegexMatchingParams",
    "RegexMatchingParamsParam",
    "AnswerRelevanceParams",
    "AnswerRelevanceParamsParam",
    "ToxicityParams",
    "ToxicityParamsParam",
    "JsonPathRule",
    "JsonPathRuleParam",
    "Annotation",
    "OutputAnnotation",
    "ContextAnnotation",
    "CheckConfig",
    "CheckConfigParam",
    "TestCaseCheckConfigParam",
    "CheckListParams",
    "CheckCreateParams",
    "CheckUpdateParams",
    "CheckBulkDeleteParams",
    # audit
    "ActionType",
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
    "DatasetGeneratePresetBasedParams",
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
    "DivergenceWarning",
    "Evaluation",
    "EvaluationReference",
    "EvaluationListParams",
    "EvaluationCreateParams",
    "EvaluationUpdateParams",
    "EvaluationRetrieveParams",
    "EvaluationRunInteractionChecksParams",
    "EvaluationCreateLocalParams",
    "EvaluationUploadParams",
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
    "Scan",
    "ScanCategory",
    "ScanAvailableProbe",
    "ScanListParams",
    "ScanCreateParams",
    "ScanRetrieveParams",
    "ScanBulkDeleteParams",
    "Severity",
    "ReviewStatus",
    "ScanProbe",
    "ScanProbeAttempt",
    "ScanProbeAttemptReference",
    "ScanProbeAttemptUpdateParams",
    # prompt preset
    "PromptPreset",
    "PromptPresetPreview",
    "PromptPresetCreateParams",
    "PromptPresetUpdateParams",
    "PromptPresetPreviewParams",
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
    "TestCaseSchemaValidation",
    "TestCaseStatus",
    "BulkMoveTestCasesParams",
    "TestCaseCreateParams",
    "TestCaseUpdateParams",
    "TestCaseBulkDeleteParams",
    "TestCaseBulkUpdateParams",
    "CommentAddParams",
    "CommentEditParams",
    # playground chat
    "PlaygroundChat",
    "PlaygroundExchange",
    "PlaygroundChatListParams",
    "PlaygroundChatCreateParams",
    "PlaygroundChatUpdateParams",
    "PlaygroundChatRetrieveParams",
    "PlaygroundChatBulkDeleteParams",
    # project
    "Project",
    "ProjectCreateParams",
    "ProjectUpdateParams",
    "ProjectBulkDeleteParams",
]
