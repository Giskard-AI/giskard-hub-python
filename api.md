# Agents

Types:

```python
from giskard_hub.types import (
    Agent,
    APIResponseAgent,
    APIResponseAgentOutput,
    APIResponseNone,
    ChatMessage,
    ExecutionError,
    Header,
    AgentListResponse,
)
```

Methods:

- <code title="post /v2/agents">client.agents.<a href="./src/giskard_hub/resources/agents.py">create</a>(\*\*<a href="src/giskard_hub/types/agent_create_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_agent.py">APIResponseAgent</a></code>
- <code title="get /v2/agents/{agent_id}">client.agents.<a href="./src/giskard_hub/resources/agents.py">retrieve</a>(agent_id) -> <a href="./src/giskard_hub/types/api_response_agent.py">APIResponseAgent</a></code>
- <code title="patch /v2/agents/{agent_id}">client.agents.<a href="./src/giskard_hub/resources/agents.py">update</a>(agent_id, \*\*<a href="src/giskard_hub/types/agent_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_agent.py">APIResponseAgent</a></code>
- <code title="get /v2/agents">client.agents.<a href="./src/giskard_hub/resources/agents.py">list</a>(\*\*<a href="src/giskard_hub/types/agent_list_params.py">params</a>) -> <a href="./src/giskard_hub/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /v2/agents/{agent_id}">client.agents.<a href="./src/giskard_hub/resources/agents.py">delete</a>(agent_id) -> <a href="./src/giskard_hub/types/api_response_none.py">APIResponseNone</a></code>
- <code title="delete /v2/agents">client.agents.<a href="./src/giskard_hub/resources/agents.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/agent_bulk_delete_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_none.py">APIResponseNone</a></code>
- <code title="post /v2/agents/{agent_id}/generate-completion">client.agents.<a href="./src/giskard_hub/resources/agents.py">generate_completion</a>(agent_id, \*\*<a href="src/giskard_hub/types/agent_generate_completion_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_agent_output.py">APIResponseAgentOutput</a></code>
- <code title="post /v2/agents/test-connection">client.agents.<a href="./src/giskard_hub/resources/agents.py">test_connection</a>(\*\*<a href="src/giskard_hub/types/agent_test_connection_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_agent_output.py">APIResponseAgentOutput</a></code>

# Checks

Types:

```python
from giskard_hub.types import (
    APIResponseCheck,
    CheckAPIResource,
    ConformityParams,
    CorrectnessParams,
    GroundednessParams,
    MetadataParams,
    SemanticSimilarityParams,
    StringMatchParams,
    CheckListResponse,
)
```

Methods:

- <code title="post /v2/checks">client.checks.<a href="./src/giskard_hub/resources/checks.py">create</a>(\*\*<a href="src/giskard_hub/types/check_create_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_check.py">APIResponseCheck</a></code>
- <code title="get /v2/checks/{check_id}">client.checks.<a href="./src/giskard_hub/resources/checks.py">retrieve</a>(check_id) -> <a href="./src/giskard_hub/types/api_response_check.py">APIResponseCheck</a></code>
- <code title="patch /v2/checks/{check_id}">client.checks.<a href="./src/giskard_hub/resources/checks.py">update</a>(check_id, \*\*<a href="src/giskard_hub/types/check_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_check.py">APIResponseCheck</a></code>
- <code title="get /v2/checks">client.checks.<a href="./src/giskard_hub/resources/checks.py">list</a>(\*\*<a href="src/giskard_hub/types/check_list_params.py">params</a>) -> <a href="./src/giskard_hub/types/check_list_response.py">CheckListResponse</a></code>
- <code title="delete /v2/checks/{check_id}">client.checks.<a href="./src/giskard_hub/resources/checks.py">delete</a>(check_id) -> <a href="./src/giskard_hub/types/api_response_none.py">APIResponseNone</a></code>
- <code title="delete /v2/checks">client.checks.<a href="./src/giskard_hub/resources/checks.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/check_bulk_delete_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_none.py">APIResponseNone</a></code>

# Datasets

Types:

```python
from giskard_hub.types import (
    APIResponseDataset,
    APIResponseListTestCase,
    Dataset,
    TaskProgress,
    DatasetListResponse,
    DatasetListTagsResponse,
)
```

Methods:

- <code title="post /v2/datasets">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">create</a>(\*\*<a href="src/giskard_hub/types/dataset_create_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_dataset.py">APIResponseDataset</a></code>
- <code title="get /v2/datasets/{dataset_id}">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">retrieve</a>(dataset_id) -> <a href="./src/giskard_hub/types/api_response_dataset.py">APIResponseDataset</a></code>
- <code title="patch /v2/datasets/{dataset_id}">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">update</a>(dataset_id, \*\*<a href="src/giskard_hub/types/dataset_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_dataset.py">APIResponseDataset</a></code>
- <code title="get /v2/datasets">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">list</a>(\*\*<a href="src/giskard_hub/types/dataset_list_params.py">params</a>) -> <a href="./src/giskard_hub/types/dataset_list_response.py">DatasetListResponse</a></code>
- <code title="delete /v2/datasets/{dataset_id}">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">delete</a>(dataset_id) -> <a href="./src/giskard_hub/types/api_response_none.py">APIResponseNone</a></code>
- <code title="delete /v2/datasets">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/dataset_bulk_delete_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_none.py">APIResponseNone</a></code>
- <code title="post /v2/datasets/generate-adversarial">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">generate_adversarial</a>(\*\*<a href="src/giskard_hub/types/dataset_generate_adversarial_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_dataset.py">APIResponseDataset</a></code>
- <code title="post /v2/datasets/generate-document-based">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">generate_document_based</a>(\*\*<a href="src/giskard_hub/types/dataset_generate_document_based_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_dataset.py">APIResponseDataset</a></code>
- <code title="get /v2/datasets/{dataset_id}/tags">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">list_tags</a>(dataset_id) -> <a href="./src/giskard_hub/types/dataset_list_tags_response.py">DatasetListTagsResponse</a></code>
- <code title="get /v2/datasets/{dataset_id}/test-cases">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">list_test_cases</a>(dataset_id) -> <a href="./src/giskard_hub/types/api_response_list_test_case.py">APIResponseListTestCase</a></code>

# Evaluations

Types:

```python
from giskard_hub.types import (
    APIResponseEvaluationAPIResource,
    DatasetSubset,
    EvaluationAPIResource,
    Metric,
    MinimalModel,
    ModelOutput,
    OutputAnnotation,
    EvaluationRetrieveResponse,
    EvaluationListResponse,
    EvaluationRunSingleResponse,
)
```

Methods:

- <code title="post /v2/evaluations">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">create</a>(\*\*<a href="src/giskard_hub/types/evaluation_create_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_evaluation_api_resource.py">APIResponseEvaluationAPIResource</a></code>
- <code title="get /v2/evaluations/{evaluation_id}">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">retrieve</a>(evaluation_id, \*\*<a href="src/giskard_hub/types/evaluation_retrieve_params.py">params</a>) -> <a href="./src/giskard_hub/types/evaluation_retrieve_response.py">EvaluationRetrieveResponse</a></code>
- <code title="patch /v2/evaluations/{evaluation_id}">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">update</a>(evaluation_id, \*\*<a href="src/giskard_hub/types/evaluation_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_evaluation_api_resource.py">APIResponseEvaluationAPIResource</a></code>
- <code title="get /v2/evaluations">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">list</a>(\*\*<a href="src/giskard_hub/types/evaluation_list_params.py">params</a>) -> <a href="./src/giskard_hub/types/evaluation_list_response.py">EvaluationListResponse</a></code>
- <code title="delete /v2/evaluations/{evaluation_id}">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">delete</a>(evaluation_id) -> <a href="./src/giskard_hub/types/api_response_none.py">APIResponseNone</a></code>
- <code title="delete /v2/evaluations">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/evaluation_bulk_delete_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_none.py">APIResponseNone</a></code>
- <code title="post /v2/evaluations/create-local">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">create_local</a>(\*\*<a href="src/giskard_hub/types/evaluation_create_local_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_evaluation_api_resource.py">APIResponseEvaluationAPIResource</a></code>
- <code title="post /v2/evaluations/{evaluation_id}/rerun-errored-results">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">rerun_errored_results</a>(evaluation_id) -> <a href="./src/giskard_hub/types/api_response_evaluation_api_resource.py">APIResponseEvaluationAPIResource</a></code>
- <code title="post /v2/evaluations/run-single">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">run_single</a>(\*\*<a href="src/giskard_hub/types/evaluation_run_single_params.py">params</a>) -> <a href="./src/giskard_hub/types/evaluation_run_single_response.py">EvaluationRunSingleResponse</a></code>

## Results

Types:

```python
from giskard_hub.types.evaluations import (
    APIResponseTestCaseEvaluationAPIResource,
    FailureCategory,
    TaskState,
    TestCaseEvaluationAPIResource,
    ResultListResponse,
)
```

Methods:

- <code title="patch /v2/evaluations/{evaluation_id}/results/{result_id}">client.evaluations.results.<a href="./src/giskard_hub/resources/evaluations/results.py">update</a>(result_id, \*, evaluation_id, \*\*<a href="src/giskard_hub/types/evaluations/result_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/evaluations/api_response_test_case_evaluation_api_resource.py">APIResponseTestCaseEvaluationAPIResource</a></code>
- <code title="get /v2/evaluations/{evaluation_id}/results">client.evaluations.results.<a href="./src/giskard_hub/resources/evaluations/results.py">list</a>(evaluation_id, \*\*<a href="src/giskard_hub/types/evaluations/result_list_params.py">params</a>) -> <a href="./src/giskard_hub/types/evaluations/result_list_response.py">ResultListResponse</a></code>
- <code title="post /v2/evaluations/{evaluation_id}/results/{result_id}/rerun-test-case">client.evaluations.results.<a href="./src/giskard_hub/resources/evaluations/results.py">rerun_test_case</a>(result_id, \*, evaluation_id) -> <a href="./src/giskard_hub/types/evaluations/api_response_test_case_evaluation_api_resource.py">APIResponseTestCaseEvaluationAPIResource</a></code>
- <code title="post /v2/evaluations/{evaluation_id}/results/{result_id}/submit-local-output">client.evaluations.results.<a href="./src/giskard_hub/resources/evaluations/results.py">submit_local_output</a>(result_id, \*, evaluation_id, \*\*<a href="src/giskard_hub/types/evaluations/result_submit_local_output_params.py">params</a>) -> <a href="./src/giskard_hub/types/evaluations/api_response_test_case_evaluation_api_resource.py">APIResponseTestCaseEvaluationAPIResource</a></code>

# KnowledgeBases

Types:

```python
from giskard_hub.types import (
    APIResponseKnowledgeBase,
    KnowledgeBase,
    KnowledgeBaseListResponse,
    KnowledgeBaseListDocumentsResponse,
)
```

Methods:

- <code title="post /v2/knowledge-bases">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">create</a>(\*\*<a href="src/giskard_hub/types/knowledge_base_create_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_knowledge_base.py">APIResponseKnowledgeBase</a></code>
- <code title="get /v2/knowledge-bases/{knowledge_base_id}">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">retrieve</a>(knowledge_base_id) -> <a href="./src/giskard_hub/types/api_response_knowledge_base.py">APIResponseKnowledgeBase</a></code>
- <code title="patch /v2/knowledge-bases/{knowledge_base_id}">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">update</a>(knowledge_base_id, \*\*<a href="src/giskard_hub/types/knowledge_base_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_knowledge_base.py">APIResponseKnowledgeBase</a></code>
- <code title="get /v2/knowledge-bases">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">list</a>(\*\*<a href="src/giskard_hub/types/knowledge_base_list_params.py">params</a>) -> <a href="./src/giskard_hub/types/knowledge_base_list_response.py">KnowledgeBaseListResponse</a></code>
- <code title="delete /v2/knowledge-bases/{knowledge_base_id}">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">delete</a>(knowledge_base_id) -> <a href="./src/giskard_hub/types/api_response_none.py">APIResponseNone</a></code>
- <code title="delete /v2/knowledge-bases">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/knowledge_base_bulk_delete_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_none.py">APIResponseNone</a></code>
- <code title="get /v2/knowledge-bases/{knowledge_base_id}/documents">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">list_documents</a>(knowledge_base_id) -> <a href="./src/giskard_hub/types/knowledge_base_list_documents_response.py">KnowledgeBaseListDocumentsResponse</a></code>

# Projects

Types:

```python
from giskard_hub.types import APIResponseProjectAPIResource, ProjectAPIResource, ProjectListResponse
```

Methods:

- <code title="post /v2/projects">client.projects.<a href="./src/giskard_hub/resources/projects.py">create</a>(\*\*<a href="src/giskard_hub/types/project_create_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_project_api_resource.py">APIResponseProjectAPIResource</a></code>
- <code title="get /v2/projects/{project_id}">client.projects.<a href="./src/giskard_hub/resources/projects.py">retrieve</a>(project_id) -> <a href="./src/giskard_hub/types/api_response_project_api_resource.py">APIResponseProjectAPIResource</a></code>
- <code title="patch /v2/projects/{project_id}">client.projects.<a href="./src/giskard_hub/resources/projects.py">update</a>(project_id, \*\*<a href="src/giskard_hub/types/project_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_project_api_resource.py">APIResponseProjectAPIResource</a></code>
- <code title="get /v2/projects">client.projects.<a href="./src/giskard_hub/resources/projects.py">list</a>() -> <a href="./src/giskard_hub/types/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /v2/projects/{project_id}">client.projects.<a href="./src/giskard_hub/resources/projects.py">delete</a>(project_id) -> <a href="./src/giskard_hub/types/api_response_none.py">APIResponseNone</a></code>
- <code title="delete /v2/projects">client.projects.<a href="./src/giskard_hub/resources/projects.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/project_bulk_delete_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_none.py">APIResponseNone</a></code>

# Scans

Types:

```python
from giskard_hub.types import (
    AgentAPIReference,
    ScanResult,
    ScanCreateResponse,
    ScanRetrieveResponse,
    ScanListResponse,
    ScanListCategoriesResponse,
    ScanListAttemptsResponse,
    ScanListProbesResponse,
)
```

Methods:

- <code title="post /v2/scans">client.scans.<a href="./src/giskard_hub/resources/scans/scans.py">create</a>(\*\*<a href="src/giskard_hub/types/scan_create_params.py">params</a>) -> <a href="./src/giskard_hub/types/scan_create_response.py">ScanCreateResponse</a></code>
- <code title="get /v2/scans/{scan_result_id}">client.scans.<a href="./src/giskard_hub/resources/scans/scans.py">retrieve</a>(scan_result_id, \*\*<a href="src/giskard_hub/types/scan_retrieve_params.py">params</a>) -> <a href="./src/giskard_hub/types/scan_retrieve_response.py">ScanRetrieveResponse</a></code>
- <code title="get /v2/scans">client.scans.<a href="./src/giskard_hub/resources/scans/scans.py">list</a>(\*\*<a href="src/giskard_hub/types/scan_list_params.py">params</a>) -> <a href="./src/giskard_hub/types/scan_list_response.py">ScanListResponse</a></code>
- <code title="delete /v2/scans/{scan_result_id}">client.scans.<a href="./src/giskard_hub/resources/scans/scans.py">delete</a>(scan_result_id) -> <a href="./src/giskard_hub/types/api_response_none.py">APIResponseNone</a></code>
- <code title="delete /v2/scans">client.scans.<a href="./src/giskard_hub/resources/scans/scans.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/scan_bulk_delete_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_none.py">APIResponseNone</a></code>
- <code title="get /v2/scan-categories">client.scans.<a href="./src/giskard_hub/resources/scans/scans.py">list_categories</a>() -> <a href="./src/giskard_hub/types/scan_list_categories_response.py">ScanListCategoriesResponse</a></code>
- <code title="get /v2/scans/{scan_result_id}/attempts">client.scans.<a href="./src/giskard_hub/resources/scans/scans.py">list_probe_attempts</a>(scan_result_id) -> <a href="./src/giskard_hub/types/scan_list_attempts_response.py">ScanListAttemptsResponse</a></code>
- <code title="get /v2/scans/{scan_result_id}/probes">client.scans.<a href="./src/giskard_hub/resources/scans/scans.py">list_probes</a>(scan_result_id) -> <a href="./src/giskard_hub/types/scan_list_probes_response.py">ScanListProbesResponse</a></code>

## Probes

Types:

```python
from giskard_hub.types.scans import (
    ScanProbeResult,
    ProbeRetrieveResponse,
    ProbeListAttemptsResponse,
)
```

Methods:

- <code title="get /v2/scan-probes/{probe_result_id}">client.scans.probes.<a href="./src/giskard_hub/resources/scans/probes.py">retrieve</a>(probe_result_id) -> <a href="./src/giskard_hub/types/scans/probe_retrieve_response.py">ProbeRetrieveResponse</a></code>
- <code title="get /v2/scan-probes/{probe_result_id}/attempts">client.scans.probes.<a href="./src/giskard_hub/resources/scans/probes.py">list_attempts</a>(probe_result_id) -> <a href="./src/giskard_hub/types/scans/probe_list_attempts_response.py">ProbeListAttemptsResponse</a></code>

## Attempts

Types:

```python
from giskard_hub.types.scans import ReviewStatus, ScanProbeAttempt, Severity, AttemptUpdateResponse
```

Methods:

- <code title="patch /v2/scan-attempts/{probe_attempt_id}">client.scans.attempts.<a href="./src/giskard_hub/resources/scans/attempts.py">update</a>(probe_attempt_id, \*\*<a href="src/giskard_hub/types/scans/attempt_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/scans/attempt_update_response.py">AttemptUpdateResponse</a></code>

# ScheduledEvaluations

Types:

```python
from giskard_hub.types import (
    APIResponseScheduledEvaluation,
    ErrorExecutionStatus,
    FrequencyOption,
    ScheduledEvaluation,
    SuccessExecutionStatus,
    ScheduledEvaluationListResponse,
    ScheduledEvaluationListEvaluationsResponse,
    ScheduledEvaluationListLatestRunsResponse,
)
```

Methods:

- <code title="post /v2/scheduled-evaluations">client.scheduled_evaluations.<a href="./src/giskard_hub/resources/scheduled_evaluations.py">create</a>(\*\*<a href="src/giskard_hub/types/scheduled_evaluation_create_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_scheduled_evaluation.py">APIResponseScheduledEvaluation</a></code>
- <code title="get /v2/scheduled-evaluations/{scheduled_evaluation_id}">client.scheduled_evaluations.<a href="./src/giskard_hub/resources/scheduled_evaluations.py">retrieve</a>(scheduled_evaluation_id) -> <a href="./src/giskard_hub/types/api_response_scheduled_evaluation.py">APIResponseScheduledEvaluation</a></code>
- <code title="patch /v2/scheduled-evaluations/{scheduled_evaluation_id}">client.scheduled_evaluations.<a href="./src/giskard_hub/resources/scheduled_evaluations.py">update</a>(scheduled_evaluation_id, \*\*<a href="src/giskard_hub/types/scheduled_evaluation_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_scheduled_evaluation.py">APIResponseScheduledEvaluation</a></code>
- <code title="get /v2/scheduled-evaluations">client.scheduled_evaluations.<a href="./src/giskard_hub/resources/scheduled_evaluations.py">list</a>(\*\*<a href="src/giskard_hub/types/scheduled_evaluation_list_params.py">params</a>) -> <a href="./src/giskard_hub/types/scheduled_evaluation_list_response.py">ScheduledEvaluationListResponse</a></code>
- <code title="delete /v2/scheduled-evaluations/{scheduled_evaluation_id}">client.scheduled_evaluations.<a href="./src/giskard_hub/resources/scheduled_evaluations.py">delete</a>(scheduled_evaluation_id) -> <a href="./src/giskard_hub/types/api_response_none.py">APIResponseNone</a></code>
- <code title="delete /v2/scheduled-evaluations">client.scheduled_evaluations.<a href="./src/giskard_hub/resources/scheduled_evaluations.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/scheduled_evaluation_bulk_delete_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_none.py">APIResponseNone</a></code>
- <code title="get /v2/scheduled-evaluations/{scheduled_evaluation_id}/evaluations">client.scheduled_evaluations.<a href="./src/giskard_hub/resources/scheduled_evaluations.py">list_evaluations</a>(scheduled_evaluation_id) -> <a href="./src/giskard_hub/types/scheduled_evaluation_list_evaluations_response.py">ScheduledEvaluationListEvaluationsResponse</a></code>
- <code title="get /v2/scheduled-evaluation-runs">client.scheduled_evaluations.<a href="./src/giskard_hub/resources/scheduled_evaluations.py">list_latest_runs</a>(\*\*<a href="src/giskard_hub/types/scheduled_evaluation_list_latest_runs_params.py">params</a>) -> <a href="./src/giskard_hub/types/scheduled_evaluation_list_latest_runs_response.py">ScheduledEvaluationListLatestRunsResponse</a></code>

# TestCases

Types:

```python
from giskard_hub.types import (
    APIResponseTestCase,
    ChatMessageWithMetadata,
    TestCase,
    TestCaseCheckConfig,
)
```

Methods:

- <code title="post /v2/test-cases">client.test_cases.<a href="./src/giskard_hub/resources/test_cases/test_cases.py">create</a>(\*\*<a href="src/giskard_hub/types/test_case_create_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_test_case.py">APIResponseTestCase</a></code>
- <code title="get /v2/test-cases/{test_case_id}">client.test_cases.<a href="./src/giskard_hub/resources/test_cases/test_cases.py">retrieve</a>(test_case_id) -> <a href="./src/giskard_hub/types/api_response_test_case.py">APIResponseTestCase</a></code>
- <code title="patch /v2/test-cases/{test_case_id}">client.test_cases.<a href="./src/giskard_hub/resources/test_cases/test_cases.py">update</a>(test_case_id, \*\*<a href="src/giskard_hub/types/test_case_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_test_case.py">APIResponseTestCase</a></code>
- <code title="delete /v2/test-cases/{test_case_id}">client.test_cases.<a href="./src/giskard_hub/resources/test_cases/test_cases.py">delete</a>(test_case_id) -> <a href="./src/giskard_hub/types/api_response_none.py">APIResponseNone</a></code>
- <code title="delete /v2/test-cases">client.test_cases.<a href="./src/giskard_hub/resources/test_cases/test_cases.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/test_case_bulk_delete_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_none.py">APIResponseNone</a></code>
- <code title="patch /v2/test-cases">client.test_cases.<a href="./src/giskard_hub/resources/test_cases/test_cases.py">bulk_update</a>(\*\*<a href="src/giskard_hub/types/test_case_bulk_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/api_response_list_test_case.py">APIResponseListTestCase</a></code>

## Comments

Types:

```python
from giskard_hub.types.test_cases import APIResponseTestCaseComment
```

Methods:

- <code title="delete /v2/test-cases/{test_case_id}/comments/{comment_id}">client.test_cases.comments.<a href="./src/giskard_hub/resources/test_cases/comments.py">delete</a>(comment_id, \*, test_case_id) -> <a href="./src/giskard_hub/types/api_response_none.py">APIResponseNone</a></code>
- <code title="post /v2/test-cases/{test_case_id}/comments">client.test_cases.comments.<a href="./src/giskard_hub/resources/test_cases/comments.py">add</a>(test_case_id, \*\*<a href="src/giskard_hub/types/test_cases/comment_add_params.py">params</a>) -> <a href="./src/giskard_hub/types/test_cases/api_response_test_case_comment.py">APIResponseTestCaseComment</a></code>
- <code title="patch /v2/test-cases/{test_case_id}/comments/{comment_id}">client.test_cases.comments.<a href="./src/giskard_hub/resources/test_cases/comments.py">edit</a>(comment_id, \*, test_case_id, \*\*<a href="src/giskard_hub/types/test_cases/comment_edit_params.py">params</a>) -> <a href="./src/giskard_hub/types/test_cases/api_response_test_case_comment.py">APIResponseTestCaseComment</a></code>
