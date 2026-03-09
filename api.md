# Agents

Types:

```python
from giskard_hub.types import (
    Agent,
    AgentOutput,
    ChatMessage,
    Header,
    APIResponse,
)
```

Methods:

- <code title="post /v2/agents">client.agents.<a href="./src/giskard_hub/resources/agents.py">create</a>(\*\*<a href="src/giskard_hub/types/agent_create_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/agent.py">Agent</a>]</code>
- <code title="get /v2/agents/{agent_id}">client.agents.<a href="./src/giskard_hub/resources/agents.py">retrieve</a>(agent_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/agent.py">Agent</a>]</code>
- <code title="patch /v2/agents/{agent_id}">client.agents.<a href="./src/giskard_hub/resources/agents.py">update</a>(agent_id, \*\*<a href="src/giskard_hub/types/agent_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/agent.py">Agent</a>]</code>
- <code title="get /v2/agents">client.agents.<a href="./src/giskard_hub/resources/agents.py">list</a>(\*\*<a href="src/giskard_hub/types/agent_list_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[List[<a href="./src/giskard_hub/types/agent.py">Agent</a>]]</code>
- <code title="delete /v2/agents/{agent_id}">client.agents.<a href="./src/giskard_hub/resources/agents.py">delete</a>(agent_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>
- <code title="delete /v2/agents">client.agents.<a href="./src/giskard_hub/resources/agents.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/agent_bulk_delete_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>
- <code title="post /v2/agents/{agent_id}/generate-completion">client.agents.<a href="./src/giskard_hub/resources/agents.py">generate_completion</a>(agent_id, \*\*<a href="src/giskard_hub/types/agent_generate_completion_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/agent.py">AgentOutput</a>]</code>
- <code title="post /v2/agents/test-connection">client.agents.<a href="./src/giskard_hub/resources/agents.py">test_connection</a>(\*\*<a href="src/giskard_hub/types/agent_test_connection_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/agent.py">AgentOutput</a>]</code>
- <code title="post /v2/agents/{agent_id}/autofill-description">client.agents.<a href="./src/giskard_hub/resources/agents.py">autofill_description</a>(agent_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[str]</code>

# Audit

Types:

```python
from giskard_hub.types import (
    AuditAPIResource,
    AuditDisplayAPIResource,
    APIPaginatedResponse,
)
```

Methods:

- <code title="post /v2/audit/search">client.audit.<a href="./src/giskard_hub/resources/audit.py">search</a>(\*\*<a href="src/giskard_hub/types/audit_search_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIPaginatedResponse</a>[List[<a href="./src/giskard_hub/types/audit_api_resource.py">AuditAPIResource</a>], None]</code>
- <code title="get /v2/audit/{entity_type}/{entity_id}">client.audit.<a href="./src/giskard_hub/resources/audit.py">list_entities</a>(entity_id, entity_type, \*\*<a href="src/giskard_hub/types/audit_list_entity_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIPaginatedResponse</a>[List[<a href="./src/giskard_hub/types/audit_display_api_resource.py">AuditDisplayAPIResource</a>], None]</code>

# Checks

Types:

```python
from giskard_hub.types import (
    CheckAPIResource,
    ConformityParams,
    CorrectnessParams,
    GroundednessParams,
    MetadataParams,
    SemanticSimilarityParams,
    StringMatchParams,
    APIResponse,
)
```

Methods:

- <code title="post /v2/checks">client.checks.<a href="./src/giskard_hub/resources/checks.py">create</a>(\*\*<a href="src/giskard_hub/types/check_create_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/check_api_resource.py">CheckAPIResource</a>]</code>
- <code title="get /v2/checks/{check_id}">client.checks.<a href="./src/giskard_hub/resources/checks.py">retrieve</a>(check_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/check_api_resource.py">CheckAPIResource</a>]</code>
- <code title="patch /v2/checks/{check_id}">client.checks.<a href="./src/giskard_hub/resources/checks.py">update</a>(check_id, \*\*<a href="src/giskard_hub/types/check_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/check_api_resource.py">CheckAPIResource</a>]</code>
- <code title="get /v2/checks">client.checks.<a href="./src/giskard_hub/resources/checks.py">list</a>(\*\*<a href="src/giskard_hub/types/check_list_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[List[<a href="./src/giskard_hub/types/check_api_resource.py">CheckAPIResource</a>]]</code>
- <code title="delete /v2/checks/{check_id}">client.checks.<a href="./src/giskard_hub/resources/checks.py">delete</a>(check_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>
- <code title="delete /v2/checks">client.checks.<a href="./src/giskard_hub/resources/checks.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/check_bulk_delete_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>

# Datasets

Types:

```python
from giskard_hub.types import (
    Dataset,
    TestCase,
    TaskProgress,
    APIResponse,
    APIPaginatedResponse,
)
```

Methods:

- <code title="post /v2/datasets">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">create</a>(\*\*<a href="src/giskard_hub/types/dataset_create_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/dataset.py">Dataset</a>]</code>
- <code title="post /v2/datasets/import">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">upload</a>(\*\*<a href="src/giskard_hub/types/dataset_import_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/dataset.py">Dataset</a>]</code>
- <code title="get /v2/datasets/{dataset_id}">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">retrieve</a>(dataset_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/dataset.py">Dataset</a>]</code>
- <code title="patch /v2/datasets/{dataset_id}">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">update</a>(dataset_id, \*\*<a href="src/giskard_hub/types/dataset_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/dataset.py">Dataset</a>]</code>
- <code title="get /v2/datasets">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">list</a>(\*\*<a href="src/giskard_hub/types/dataset_list_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[List[<a href="./src/giskard_hub/types/dataset.py">Dataset</a>]]</code>
- <code title="delete /v2/datasets/{dataset_id}">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">delete</a>(dataset_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>
- <code title="delete /v2/datasets">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/dataset_bulk_delete_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>
- <code title="post /v2/datasets/generate-scenario-based">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">generate_scenario_based</a>(\*\*<a href="src/giskard_hub/types/dataset_generate_scenario_based_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/dataset.py">Dataset</a>]</code>
- <code title="post /v2/datasets/generate-document-based">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">generate_document_based</a>(\*\*<a href="src/giskard_hub/types/dataset_generate_document_based_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/dataset.py">Dataset</a>]</code>
- <code title="get /v2/datasets/{dataset_id}/tags">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">list_tags</a>(dataset_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[List[str]]</code>
- <code title="get /v2/datasets/{dataset_id}/test-cases">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">list_test_cases</a>(dataset_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[List[<a href="./src/giskard_hub/types/test_case.py">TestCase</a>]]</code>
- <code title="post /v2/datasets/{dataset_id}/test-cases/search">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">search_test_cases</a>(dataset_id, \*\*<a href="src/giskard_hub/types/dataset_search_test_cases_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIPaginatedResponse</a>[<a href="./src/giskard_hub/types/test_case.py">TestCase</a>, None]</code>

# Evaluations

Types:

```python
from giskard_hub.types import (
    Agent,
    AgentOutput,
    Dataset,
    DatasetSubset,
    EvaluationAPIResource,
    CheckAPIResource,
    Metric,
    MinimalAgent,
    OutputAnnotation,
    APIResponse,
    APIResponseWithIncluded,
)
```

Methods:

- <code title="post /v2/evaluations">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">create</a>(\*\*<a href="src/giskard_hub/types/evaluation_create_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/evaluation_api_resource.py">EvaluationAPIResource</a>]</code>
- <code title="get /v2/evaluations/{evaluation_id}">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">retrieve</a>(evaluation_id, \*\*<a href="src/giskard_hub/types/evaluation_retrieve_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponseWithIncluded</a>[<a href="./src/giskard_hub/types/evaluation_api_resource.py">EvaluationAPIResource</a>, <a href="./src/giskard_hub/types/agent.py">Agent</a> | <a href="./src/giskard_hub/types/dataset.py">Dataset</a>]</code>
- <code title="patch /v2/evaluations/{evaluation_id}">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">update</a>(evaluation_id, \*\*<a href="src/giskard_hub/types/evaluation_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/evaluation_api_resource.py">EvaluationAPIResource</a>]</code>
- <code title="get /v2/evaluations">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">list</a>(\*\*<a href="src/giskard_hub/types/evaluation_list_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponseWithIncluded</a>[List[<a href="./src/giskard_hub/types/evaluation_api_resource.py">EvaluationAPIResource</a>], <a href="./src/giskard_hub/types/agent.py">Agent</a> | <a href="./src/giskard_hub/types/dataset.py">Dataset</a>]</code>
- <code title="delete /v2/evaluations/{evaluation_id}">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">delete</a>(evaluation_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>
- <code title="delete /v2/evaluations">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/evaluation_bulk_delete_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>
- <code title="post /v2/evaluations/create-local">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">create_local</a>(\*\*<a href="src/giskard_hub/types/evaluation_create_local_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/evaluation_api_resource.py">EvaluationAPIResource</a>]</code>
- <code title="post /v2/evaluations/{evaluation_id}/rerun-errored-results">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">rerun_errored_results</a>(evaluation_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/evaluation_api_resource.py">EvaluationAPIResource</a>]</code>
- <code title="post /v2/evaluations/run-single">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">run_single</a>(\*\*<a href="src/giskard_hub/types/evaluation_run_single_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[List[<a href="./src/giskard_hub/types/check_api_resource.py">CheckAPIResource</a>]]</code>

## Results

Types:

```python
from giskard_hub.types.evaluations import (
    FailureCategory,
    TaskState,
    TestCaseEvaluationAPIResource,
)
from giskard_hub.types import (
    TestCase,
    APIResponse,
    APIResponseWithIncluded,
    APIPaginatedResponse,
)
```

Methods:

- <code title="get /v2/evaluations/{evaluation_id}/results/{result_id}">client.evaluations.results.<a href="./src/giskard_hub/resources/evaluations/results.py">retrieve</a>(result_id, \*, evaluation_id, \*\*<a href="src/giskard_hub/types/evaluations/result_retrieve_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponseWithIncluded</a>[<a href="./src/giskard_hub/types/evaluations/test_case_evaluation_api_resource.py">TestCaseEvaluationAPIResource</a>, <a href="./src/giskard_hub/types/test_case.py">TestCase</a>]</code>
- <code title="patch /v2/evaluations/{evaluation_id}/results/{result_id}">client.evaluations.results.<a href="./src/giskard_hub/resources/evaluations/results.py">update</a>(result_id, \*, evaluation_id, \*\*<a href="src/giskard_hub/types/evaluations/result_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/evaluations/test_case_evaluation_api_resource.py">TestCaseEvaluationAPIResource</a>]</code>
- <code title="get /v2/evaluations/{evaluation_id}/results">client.evaluations.results.<a href="./src/giskard_hub/resources/evaluations/results.py">list</a>(evaluation_id, \*\*<a href="src/giskard_hub/types/evaluations/result_list_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponseWithIncluded</a>[List[<a href="./src/giskard_hub/types/evaluations/test_case_evaluation_api_resource.py">TestCaseEvaluationAPIResource</a>], <a href="./src/giskard_hub/types/test_case.py">TestCase</a>]</code>
- <code title="post /v2/evaluations/{evaluation_id}/results/{result_id}/rerun-test-case">client.evaluations.results.<a href="./src/giskard_hub/resources/evaluations/results.py">rerun_test_case</a>(result_id, \*, evaluation_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/evaluations/test_case_evaluation_api_resource.py">TestCaseEvaluationAPIResource</a>]</code>
- <code title="post /v2/evaluations/{evaluation_id}/results/{result_id}/submit-local-output">client.evaluations.results.<a href="./src/giskard_hub/resources/evaluations/results.py">submit_local_output</a>(result_id, \*, evaluation_id, \*\*<a href="src/giskard_hub/types/evaluations/result_submit_local_output_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/evaluations/test_case_evaluation_api_resource.py">TestCaseEvaluationAPIResource</a>]</code>
- <code title="post /v2/evaluations/{evaluation_id}/results/search">client.evaluations.results.<a href="./src/giskard_hub/resources/evaluations/results.py">search</a>(evaluation_id, \*\*<a href="src/giskard_hub/types/evaluations/result_search_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIPaginatedResponse</a>[<a href="./src/giskard_hub/types/evaluations/test_case_evaluation_api_resource.py">TestCaseEvaluationAPIResource</a>, <a href="./src/giskard_hub/types/test_case.py">TestCase</a>]</code>
- <code title="patch /v2/evaluations/{evaluation_id}/results/{result_id}/visibility">client.evaluations.results.<a href="./src/giskard_hub/resources/evaluations/results.py">update_visibility</a>(result_id, \*, evaluation_id, \*\*<a href="src/giskard_hub/types/evaluations/result_update_visibility_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/evaluations/test_case_evaluation_api_resource.py">TestCaseEvaluationAPIResource</a>]</code>

# KnowledgeBases

Types:

```python
from giskard_hub.types import (
    KnowledgeBase,
    KnowledgeBaseDocumentRowAPIResource,
    KnowledgeBaseDocumentDetailAPIResource,
    APIResponse,
    APIPaginatedResponse,
)
```

Methods:

- <code title="post /v2/knowledge-bases">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">create</a>(\*\*<a href="src/giskard_hub/types/knowledge_base_create_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/knowledge_base.py">KnowledgeBase</a>]</code>
- <code title="get /v2/knowledge-bases/{knowledge_base_id}">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">retrieve</a>(knowledge_base_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/knowledge_base.py">KnowledgeBase</a>]</code>
- <code title="patch /v2/knowledge-bases/{knowledge_base_id}">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">update</a>(knowledge_base_id, \*\*<a href="src/giskard_hub/types/knowledge_base_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/knowledge_base.py">KnowledgeBase</a>]</code>
- <code title="get /v2/knowledge-bases">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">list</a>(\*\*<a href="src/giskard_hub/types/knowledge_base_list_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[List[<a href="./src/giskard_hub/types/knowledge_base.py">KnowledgeBase</a>]]</code>
- <code title="delete /v2/knowledge-bases/{knowledge_base_id}">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">delete</a>(knowledge_base_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>
- <code title="delete /v2/knowledge-bases">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/knowledge_base_bulk_delete_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>
- <code title="post /v2/knowledge-bases/{knowledge_base_id}/documents/search">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">search_documents</a>(knowledge_base_id, \*\*<a href="src/giskard_hub/types/knowledge_base_search_documents_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIPaginatedResponse</a>[List[<a href="./src/giskard_hub/types/knowledge_base_document_row_api_resource.py">KnowledgeBaseDocumentRowAPIResource</a>], None]</code>
- <code title="get /v2/knowledge-bases/{knowledge_base_id}/documents/{document_id}">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">retrieve_document</a>(knowledge_base_id, document_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/knowledge_base_document_detail_api_resource.py">KnowledgeBaseDocumentDetailAPIResource</a>]</code>

# Projects

Types:

```python
from giskard_hub.types import (
    ProjectAPIResource,
    APIResponse,
)
```

Methods:

- <code title="post /v2/projects">client.projects.<a href="./src/giskard_hub/resources/projects/projects.py">create</a>(\*\*<a href="src/giskard_hub/types/project_create_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/project_api_resource.py">ProjectAPIResource</a>]</code>
- <code title="get /v2/projects/{project_id}">client.projects.<a href="./src/giskard_hub/resources/projects/projects.py">retrieve</a>(project_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/project_api_resource.py">ProjectAPIResource</a>]</code>
- <code title="patch /v2/projects/{project_id}">client.projects.<a href="./src/giskard_hub/resources/projects/projects.py">update</a>(project_id, \*\*<a href="src/giskard_hub/types/project_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/project_api_resource.py">ProjectAPIResource</a>]</code>
- <code title="get /v2/projects">client.projects.<a href="./src/giskard_hub/resources/projects/projects.py">list</a>() -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[List[<a href="./src/giskard_hub/types/project_api_resource.py">ProjectAPIResource</a>]]</code>
- <code title="delete /v2/projects/{project_id}">client.projects.<a href="./src/giskard_hub/resources/projects/projects.py">delete</a>(project_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>
- <code title="delete /v2/projects">client.projects.<a href="./src/giskard_hub/resources/projects/projects.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/project_bulk_delete_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>

## Scenarios

Types:

```python
from giskard_hub.types import (
    ScenarioAPIResource,
    ScenarioPreviewAPIResource,
    APIResponse,
)
```

Methods:

- <code title="post /v2/projects/{project_id}/scenarios">client.projects.scenarios.<a href="./src/giskard_hub/resources/projects/scenarios.py">create</a>(project_id, \*\*<a href="src/giskard_hub/types/scenario_create_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/scenario_api_resource.py">ScenarioAPIResource</a>]</code>
- <code title="get /v2/projects/{project_id}/scenarios/{scenario_id}">client.projects.scenarios.<a href="./src/giskard_hub/resources/projects/scenarios.py">retrieve</a>(scenario_id, \*, project_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/scenario_api_resource.py">ScenarioAPIResource</a>]</code>
- <code title="patch /v2/projects/{project_id}/scenarios/{scenario_id}">client.projects.scenarios.<a href="./src/giskard_hub/resources/projects/scenarios.py">update</a>(scenario_id, \*, project_id, \*\*<a href="src/giskard_hub/types/scenario_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/scenario_api_resource.py">ScenarioAPIResource</a>]</code>
- <code title="get /v2/projects/{project_id}/scenarios">client.projects.scenarios.<a href="./src/giskard_hub/resources/projects/scenarios.py">list</a>(project_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[List[<a href="./src/giskard_hub/types/scenario_api_resource.py">ScenarioAPIResource</a>]]</code>
- <code title="delete /v2/projects/{project_id}/scenarios/{scenario_id}">client.projects.scenarios.<a href="./src/giskard_hub/resources/projects/scenarios.py">delete</a>(scenario_id, \*, project_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>
- <code title="post /v2/projects/{project_id}/scenarios/preview">client.projects.scenarios.<a href="./src/giskard_hub/resources/projects/scenarios.py">preview</a>(project_id, \*\*<a href="src/giskard_hub/types/scenario_preview_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/scenario_preview_api_resource.py">ScenarioPreviewAPIResource</a>]</code>

# Scans

Types:

```python
from giskard_hub.types import (
    Agent,
    AgentAPIReference,
    KnowledgeBase,
    ScanResult,
    ScanCategory,
    ScanProbeResult,
    APIResponse,
    APIResponseWithIncluded,
)
```

Methods:

- <code title="post /v2/scans">client.scans.<a href="./src/giskard_hub/resources/scans/scans.py">create</a>(\*\*<a href="src/giskard_hub/types/scan_create_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/scan_result.py">ScanResult</a>]</code>
- <code title="get /v2/scans/{scan_result_id}">client.scans.<a href="./src/giskard_hub/resources/scans/scans.py">retrieve</a>(scan_result_id, \*\*<a href="src/giskard_hub/types/scan_retrieve_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponseWithIncluded</a>[<a href="./src/giskard_hub/types/scan_result.py">ScanResult</a>, Union[<a href="./src/giskard_hub/types/agent.py">Agent</a>, <a href="./src/giskard_hub/types/knowledge_base.py">KnowledgeBase</a>]]</code>
- <code title="get /v2/scans">client.scans.<a href="./src/giskard_hub/resources/scans/scans.py">list</a>(\*\*<a href="src/giskard_hub/types/scan_list_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponseWithIncluded</a>[List[<a href="./src/giskard_hub/types/scan_result.py">ScanResult</a>], Union[<a href="./src/giskard_hub/types/agent.py">Agent</a>, <a href="./src/giskard_hub/types/knowledge_base.py">KnowledgeBase</a>]]</code>
- <code title="delete /v2/scans/{scan_result_id}">client.scans.<a href="./src/giskard_hub/resources/scans/scans.py">delete</a>(scan_result_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>
- <code title="delete /v2/scans">client.scans.<a href="./src/giskard_hub/resources/scans/scans.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/scan_bulk_delete_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>
- <code title="get /v2/scan-categories">client.scans.<a href="./src/giskard_hub/resources/scans/scans.py">list_categories</a>() -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[List[<a href="./src/giskard_hub/types/scan_result.py">ScanCategory</a>]]</code>
- <code title="get /v2/scans/{scan_result_id}/probes">client.scans.<a href="./src/giskard_hub/resources/scans/scans.py">list_probes</a>(scan_result_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[List[<a href="./src/giskard_hub/types/scans/scan_probe_result.py">ScanProbeResult</a>]]</code>

## Probes

Types:

```python
from giskard_hub.types.scans import (
    ScanProbeResult,
    ScanProbeAttempt,
)
from giskard_hub.types import APIResponse
```

Methods:

- <code title="get /v2/scan-probes/{probe_result_id}">client.scans.probes.<a href="./src/giskard_hub/resources/scans/probes.py">retrieve</a>(probe_result_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/scans/scan_probe_result.py">ScanProbeResult</a>]</code>
- <code title="get /v2/scan-probes/{probe_result_id}/attempts">client.scans.probes.<a href="./src/giskard_hub/resources/scans/probes.py">list_attempts</a>(probe_result_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[List[<a href="./src/giskard_hub/types/scans/scan_probe_attempt.py">ScanProbeAttempt</a>]]</code>

## Attempts

Types:

```python
from giskard_hub.types.scans import (
    ReviewStatus,
    ScanProbeAttempt,
    Severity,
)
from giskard_hub.types import APIResponse
```

Methods:

- <code title="patch /v2/scan-attempts/{probe_attempt_id}">client.scans.attempts.<a href="./src/giskard_hub/resources/scans/attempts.py">update</a>(probe_attempt_id, \*\*<a href="src/giskard_hub/types/scans/attempt_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/scans/scan_probe_attempt.py">ScanProbeAttempt</a>]</code>

# ScheduledEvaluations

Types:

```python
from giskard_hub.types import (
    Agent,
    Dataset,
    ScheduledEvaluation,
    EvaluationAPIResource,
    ErrorExecutionStatus,
    FrequencyOption,
    SuccessExecutionStatus,
    APIResponse,
    APIResponseWithIncluded,
)
```

Methods:

- <code title="post /v2/scheduled-evaluations">client.scheduled_evaluations.<a href="./src/giskard_hub/resources/scheduled_evaluations.py">create</a>(\*\*<a href="src/giskard_hub/types/scheduled_evaluation_create_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/scheduled_evaluation.py">ScheduledEvaluation</a>]</code>
- <code title="get /v2/scheduled-evaluations/{scheduled_evaluation_id}">client.scheduled_evaluations.<a href="./src/giskard_hub/resources/scheduled_evaluations.py">retrieve</a>(scheduled_evaluation_id, \*\*<a href="src/giskard_hub/types/scheduled_evaluation_retrieve_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponseWithIncluded</a>[<a href="./src/giskard_hub/types/scheduled_evaluation.py">ScheduledEvaluation</a>, List[<a href="./src/giskard_hub/types/evaluation_api_resource.py">EvaluationAPIResource</a>]]</code>
- <code title="patch /v2/scheduled-evaluations/{scheduled_evaluation_id}">client.scheduled_evaluations.<a href="./src/giskard_hub/resources/scheduled_evaluations.py">update</a>(scheduled_evaluation_id, \*\*<a href="src/giskard_hub/types/scheduled_evaluation_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/scheduled_evaluation.py">ScheduledEvaluation</a>]</code>
- <code title="get /v2/scheduled-evaluations">client.scheduled_evaluations.<a href="./src/giskard_hub/resources/scheduled_evaluations.py">list</a>(\*\*<a href="src/giskard_hub/types/scheduled_evaluation_list_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponseWithIncluded</a>[List[<a href="./src/giskard_hub/types/scheduled_evaluation.py">ScheduledEvaluation</a>], List[<a href="./src/giskard_hub/types/evaluation_api_resource.py">EvaluationAPIResource</a>]]</code>
- <code title="delete /v2/scheduled-evaluations/{scheduled_evaluation_id}">client.scheduled_evaluations.<a href="./src/giskard_hub/resources/scheduled_evaluations.py">delete</a>(scheduled_evaluation_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>
- <code title="delete /v2/scheduled-evaluations">client.scheduled_evaluations.<a href="./src/giskard_hub/resources/scheduled_evaluations.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/scheduled_evaluation_bulk_delete_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>
- <code title="get /v2/scheduled-evaluations/{scheduled_evaluation_id}/evaluations">client.scheduled_evaluations.<a href="./src/giskard_hub/resources/scheduled_evaluations.py">list_evaluations</a>(scheduled_evaluation_id, \*\*<a href="src/giskard_hub/types/scheduled_evaluation_list_evaluations_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponseWithIncluded</a>[List[<a href="./src/giskard_hub/types/evaluation_api_resource.py">EvaluationAPIResource</a>], <a href="./src/giskard_hub/types/agent.py">Agent</a> | <a href="./src/giskard_hub/types/dataset.py">Dataset</a>]</code>

# TestCases

Types:

```python
from giskard_hub.types import (
    TestCase,
    TestCaseComment,
    TestCaseCheckConfig,
    ChatMessageWithMetadata,
    APIResponse,
)
```

Methods:

- <code title="post /v2/test-cases">client.test_cases.<a href="./src/giskard_hub/resources/test_cases/test_cases.py">create</a>(\*\*<a href="src/giskard_hub/types/test_case_create_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/test_case.py">TestCase</a>]</code>
- <code title="get /v2/test-cases/{test_case_id}">client.test_cases.<a href="./src/giskard_hub/resources/test_cases/test_cases.py">retrieve</a>(test_case_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/test_case.py">TestCase</a>]</code>
- <code title="patch /v2/test-cases/{test_case_id}">client.test_cases.<a href="./src/giskard_hub/resources/test_cases/test_cases.py">update</a>(test_case_id, \*\*<a href="src/giskard_hub/types/test_case_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/test_case.py">TestCase</a>]</code>
- <code title="delete /v2/test-cases/{test_case_id}">client.test_cases.<a href="./src/giskard_hub/resources/test_cases/test_cases.py">delete</a>(test_case_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>
- <code title="delete /v2/test-cases">client.test_cases.<a href="./src/giskard_hub/resources/test_cases/test_cases.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/test_case_bulk_delete_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>
- <code title="patch /v2/test-cases">client.test_cases.<a href="./src/giskard_hub/resources/test_cases/test_cases.py">bulk_update</a>(\*\*<a href="src/giskard_hub/types/test_case_bulk_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[List[<a href="./src/giskard_hub/types/test_case.py">TestCase</a>]]</code>
- <code title="post /v2/test-cases/bulk-move">client.test_cases.<a href="./src/giskard_hub/resources/test_cases/test_cases.py">bulk_move</a>(\*\*<a href="src/giskard_hub/types/bulk_move_test_cases_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>

## Comments

Types:

```python
from giskard_hub.types import (
    TestCaseComment,
    APIResponse,
)
```

Methods:

- <code title="delete /v2/test-cases/{test_case_id}/comments/{comment_id}">client.test_cases.comments.<a href="./src/giskard_hub/resources/test_cases/comments.py">delete</a>(comment_id, \*, test_case_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>
- <code title="post /v2/test-cases/{test_case_id}/comments">client.test_cases.comments.<a href="./src/giskard_hub/resources/test_cases/comments.py">add</a>(test_case_id, \*\*<a href="src/giskard_hub/types/test_cases/comment_add_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/test_case.py">TestCaseComment</a>]</code>
- <code title="patch /v2/test-cases/{test_case_id}/comments/{comment_id}">client.test_cases.comments.<a href="./src/giskard_hub/resources/test_cases/comments.py">edit</a>(comment_id, \*, test_case_id, \*\*<a href="src/giskard_hub/types/test_cases/comment_edit_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/test_case.py">TestCaseComment</a>]</code>

# Tasks

Types:

```python
from giskard_hub.types import (
    TaskAPIResource,
    TaskStatus,
    TaskPriority,
    APIResponse,
)
```

Methods:

- <code title="post /v2/tasks">client.tasks.<a href="./src/giskard_hub/resources/tasks.py">create</a>(\*\*<a href="src/giskard_hub/types/task_create_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/task_api_resource.py">TaskAPIResource</a>]</code>
- <code title="get /v2/tasks/{task_id}">client.tasks.<a href="./src/giskard_hub/resources/tasks.py">retrieve</a>(task_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/task_api_resource.py">TaskAPIResource</a>]</code>
- <code title="patch /v2/tasks/{task_id}">client.tasks.<a href="./src/giskard_hub/resources/tasks.py">update</a>(task_id, \*\*<a href="src/giskard_hub/types/task_update_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[<a href="./src/giskard_hub/types/task_api_resource.py">TaskAPIResource</a>]</code>
- <code title="get /v2/tasks">client.tasks.<a href="./src/giskard_hub/resources/tasks.py">list</a>(\*\*<a href="src/giskard_hub/types/task_list_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[List[<a href="./src/giskard_hub/types/task_api_resource.py">TaskAPIResource</a>]]</code>
- <code title="delete /v2/tasks/{task_id}">client.tasks.<a href="./src/giskard_hub/resources/tasks.py">delete</a>(task_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>
- <code title="delete /v2/tasks">client.tasks.<a href="./src/giskard_hub/resources/tasks.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/task_bulk_delete_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>

# PlaygroundChats

Types:

```python
from giskard_hub.types import (
    Agent,
    PlaygroundChatAPIResource,
    APIResponse,
    APIResponseWithIncluded,
)
```

Methods:

- <code title="get /v2/playground-chats">client.playground_chats.<a href="./src/giskard_hub/resources/playground_chats.py">list</a>(\*\*<a href="src/giskard_hub/types/playground_chat_list_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponseWithIncluded</a>[List[<a href="./src/giskard_hub/types/playground_chat_api_resource.py">PlaygroundChatAPIResource</a>], <a href="./src/giskard_hub/types/agent.py">Agent</a>]</code>
- <code title="get /v2/playground-chats/{chat_id}">client.playground_chats.<a href="./src/giskard_hub/resources/playground_chats.py">retrieve</a>(chat_id, \*\*<a href="src/giskard_hub/types/playground_chat_retrieve_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponseWithIncluded</a>[<a href="./src/giskard_hub/types/playground_chat_api_resource.py">PlaygroundChatAPIResource</a>, <a href="./src/giskard_hub/types/agent.py">Agent</a>]</code>
- <code title="delete /v2/playground-chats/{chat_id}">client.playground_chats.<a href="./src/giskard_hub/resources/playground_chats.py">delete</a>(chat_id) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>
- <code title="delete /v2/playground-chats">client.playground_chats.<a href="./src/giskard_hub/resources/playground_chats.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/playground_chat_bulk_delete_params.py">params</a>) -> <a href="./src/giskard_hub/types/common/responses.py">APIResponse</a>[None]</code>
