# Agents

Types:

```python
from giskard_hub.types import (
    Agent,
    AgentOutput,
    ChatMessage,
    Header,
)
```

Methods:

- <code title="post /v2/agents">client.agents.<a href="./src/giskard_hub/resources/agents.py">create</a>(\*\*<a href="src/giskard_hub/types/agent.py">params</a>) -> <a href="./src/giskard_hub/types/agent.py">Agent</a></code>
- <code title="get /v2/agents/{agent_id}">client.agents.<a href="./src/giskard_hub/resources/agents.py">retrieve</a>(agent_id) -> <a href="./src/giskard_hub/types/agent.py">Agent</a></code>
- <code title="patch /v2/agents/{agent_id}">client.agents.<a href="./src/giskard_hub/resources/agents.py">update</a>(agent_id, \*\*<a href="src/giskard_hub/types/agent.py">params</a>) -> <a href="./src/giskard_hub/types/agent.py">Agent</a></code>
- <code title="get /v2/agents">client.agents.<a href="./src/giskard_hub/resources/agents.py">list</a>(\*\*<a href="src/giskard_hub/types/agent.py">params</a>) -> List[<a href="./src/giskard_hub/types/agent.py">Agent</a>]</code>
- <code title="delete /v2/agents/{agent_id}">client.agents.<a href="./src/giskard_hub/resources/agents.py">delete</a>(agent_id) -> None</code>
- <code title="delete /v2/agents">client.agents.<a href="./src/giskard_hub/resources/agents.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/agent.py">params</a>) -> None</code>
- <code title="post /v2/agents/{agent_id}/generate-completion">client.agents.<a href="./src/giskard_hub/resources/agents.py">generate_completion</a>(agent_id, \*\*<a href="src/giskard_hub/types/agent.py">params</a>) -> <a href="./src/giskard_hub/types/agent.py">AgentOutput</a></code>
- <code title="post /v2/agents/test-connection">client.agents.<a href="./src/giskard_hub/resources/agents.py">test_connection</a>(\*\*<a href="src/giskard_hub/types/agent.py">params</a>) -> <a href="./src/giskard_hub/types/agent.py">AgentOutput</a></code>
- <code title="post /v2/agents/{agent_id}/autofill-description">client.agents.<a href="./src/giskard_hub/resources/agents.py">generate_description</a>(agent_id) -> str</code>

# Audit

Types:

```python
from giskard_hub.types import (
    Audit,
    AuditDisplay,
    APIPaginatedMetadata,
)
```

Methods:

- <code title="post /v2/audit/search">client.audit.<a href="./src/giskard_hub/resources/audit.py">search</a>(\*\*<a href="src/giskard_hub/types/audit.py">params</a>, include_metadata: bool = False) -> List[<a href="./src/giskard_hub/types/audit.py">Audit</a>] | Tuple[List[<a href="./src/giskard_hub/types/audit.py">Audit</a>], <a href="./src/giskard_hub/types/common/__init__.py">APIPaginatedMetadata</a>]</code>
- <code title="get /v2/audit/{entity_type}/{entity_id}">client.audit.<a href="./src/giskard_hub/resources/audit.py">list_entities</a>(entity_id, entity_type, \*\*<a href="src/giskard_hub/types/audit.py">params</a>, include_metadata: bool = False) -> List[<a href="./src/giskard_hub/types/audit.py">AuditDisplay</a>] | Tuple[List[<a href="./src/giskard_hub/types/audit.py">AuditDisplay</a>], <a href="./src/giskard_hub/types/common/__init__.py">APIPaginatedMetadata</a>]</code>

# Checks

Types:

```python
from giskard_hub.types import (
    Check,
    CheckResult,
    ConformityParams,
    CorrectnessParams,
    GroundednessParams,
    MetadataParams,
    SemanticSimilarityParams,
    StringMatchParams,
)
```

Methods:

- <code title="post /v2/checks">client.checks.<a href="./src/giskard_hub/resources/checks.py">create</a>(\*\*<a href="src/giskard_hub/types/check.py">params</a>) -> <a href="./src/giskard_hub/types/check.py">Check</a></code>
- <code title="get /v2/checks/{check_id}">client.checks.<a href="./src/giskard_hub/resources/checks.py">retrieve</a>(check_id) -> <a href="./src/giskard_hub/types/check.py">Check</a></code>
- <code title="patch /v2/checks/{check_id}">client.checks.<a href="./src/giskard_hub/resources/checks.py">update</a>(check_id, \*\*<a href="src/giskard_hub/types/check.py">params</a>) -> <a href="./src/giskard_hub/types/check.py">Check</a></code>
- <code title="get /v2/checks">client.checks.<a href="./src/giskard_hub/resources/checks.py">list</a>(\*\*<a href="src/giskard_hub/types/check.py">params</a>) -> List[<a href="./src/giskard_hub/types/check.py">Check</a>]</code>
- <code title="delete /v2/checks/{check_id}">client.checks.<a href="./src/giskard_hub/resources/checks.py">delete</a>(check_id) -> None</code>
- <code title="delete /v2/checks">client.checks.<a href="./src/giskard_hub/resources/checks.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/check.py">params</a>) -> None</code>

# Datasets

Types:

```python
from giskard_hub.types import (
    Dataset,
    TestCase,
    TaskProgress,
    APIPaginatedMetadata,
)
```

Methods:

- <code title="post /v2/datasets">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">create</a>(\*\*<a href="src/giskard_hub/types/dataset.py">params</a>) -> <a href="./src/giskard_hub/types/dataset.py">Dataset</a></code>
- <code title="post /v2/datasets/import">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">upload</a>(\*\*<a href="src/giskard_hub/types/dataset.py">params</a>) -> <a href="./src/giskard_hub/types/dataset.py">Dataset</a></code>
- <code title="get /v2/datasets/{dataset_id}">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">retrieve</a>(dataset_id) -> <a href="./src/giskard_hub/types/dataset.py">Dataset</a></code>
- <code title="patch /v2/datasets/{dataset_id}">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">update</a>(dataset_id, \*\*<a href="src/giskard_hub/types/dataset.py">params</a>) -> <a href="./src/giskard_hub/types/dataset.py">Dataset</a></code>
- <code title="get /v2/datasets">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">list</a>(\*\*<a href="src/giskard_hub/types/dataset.py">params</a>) -> List[<a href="./src/giskard_hub/types/dataset.py">Dataset</a>]</code>
- <code title="delete /v2/datasets/{dataset_id}">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">delete</a>(dataset_id) -> None</code>
- <code title="delete /v2/datasets">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/dataset.py">params</a>) -> None</code>
- <code title="post /v2/datasets/generate-scenario-based">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">generate_scenario_based</a>(\*\*<a href="src/giskard_hub/types/dataset.py">params</a>) -> <a href="./src/giskard_hub/types/dataset.py">Dataset</a></code>
- <code title="post /v2/datasets/generate-document-based">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">generate_document_based</a>(\*\*<a href="src/giskard_hub/types/dataset.py">params</a>) -> <a href="./src/giskard_hub/types/dataset.py">Dataset</a></code>
- <code title="get /v2/datasets/{dataset_id}/tags">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">list_tags</a>(dataset_id) -> List[str]</code>
- <code title="get /v2/datasets/{dataset_id}/test-cases">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">list_test_cases</a>(dataset_id) -> List[<a href="./src/giskard_hub/types/test_case.py">TestCase</a>]</code>
- <code title="post /v2/datasets/{dataset_id}/test-cases/search">client.datasets.<a href="./src/giskard_hub/resources/datasets.py">search_test_cases</a>(dataset_id, \*\*<a href="src/giskard_hub/types/dataset.py">params</a>, include_metadata: bool = False) -> List[<a href="./src/giskard_hub/types/test_case.py">TestCase</a>] | Tuple[List[<a href="./src/giskard_hub/types/test_case.py">TestCase</a>], <a href="./src/giskard_hub/types/common/__init__.py">APIPaginatedMetadata</a>]</code>

# Evaluations

Types:

```python
from giskard_hub.types import (
    Agent,
    AgentOutput,
    CheckResult,
    Dataset,
    DatasetSubset,
    Evaluation,
    Metric,
    MinimalAgent,
    OutputAnnotation,
)
```

Methods:

- <code title="post /v2/evaluations">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">create</a>(\*\*<a href="src/giskard_hub/types/evaluation.py">params</a>) -> <a href="./src/giskard_hub/types/evaluation.py">Evaluation</a></code>
- <code title="get /v2/evaluations/{evaluation_id}">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">retrieve</a>(evaluation_id, \*\*<a href="src/giskard_hub/types/evaluation.py">params</a>) -> <a href="./src/giskard_hub/types/evaluation.py">Evaluation</a></code>
- <code title="patch /v2/evaluations/{evaluation_id}">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">update</a>(evaluation_id, \*\*<a href="src/giskard_hub/types/evaluation.py">params</a>) -> <a href="./src/giskard_hub/types/evaluation.py">Evaluation</a></code>
- <code title="get /v2/evaluations">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">list</a>(\*\*<a href="src/giskard_hub/types/evaluation.py">params</a>) -> List[<a href="./src/giskard_hub/types/evaluation.py">Evaluation</a>]</code>
- <code title="delete /v2/evaluations/{evaluation_id}">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">delete</a>(evaluation_id) -> None</code>
- <code title="delete /v2/evaluations">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/evaluation.py">params</a>) -> None</code>
- <code title="post /v2/evaluations/create-local">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">create_local</a>(\*\*<a href="src/giskard_hub/types/evaluation.py">params</a>) -> <a href="./src/giskard_hub/types/evaluation.py">Evaluation</a></code>
- <code title="post /v2/evaluations/{evaluation_id}/rerun-errored-results">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">rerun_errored_results</a>(evaluation_id) -> <a href="./src/giskard_hub/types/evaluation.py">Evaluation</a></code>
- <code title="post /v2/evaluations/run-single">client.evaluations.<a href="./src/giskard_hub/resources/evaluations/evaluations.py">run_single</a>(\*\*<a href="src/giskard_hub/types/evaluation.py">params</a>) -> List[<a href="./src/giskard_hub/types/check.py">CheckResult</a>]</code>

## Helpers

The `helpers` resource exposes convenience methods for common workflows such as running evaluations and waiting for completion.

Types:

```python
from giskard_hub.resources.helpers import (
    HelpersResource,
    AsyncHelpersResource,
)
from giskard_hub.types import (
    Evaluation,
    ChatMessage,
)
```

Methods:

- `client.helpers.wait_for_completion(entity, *, poll_interval=5.0, max_retries=360, running_states={"running"}, error_states={"error"}, raise_on_error=True) -> TStateful`
  Waits until a task-like entity (such as an evaluation) leaves a running state or reaches an error state.

- `client.helpers.evaluate(agent, *, dataset, project=None, name=None, tags=None) -> Evaluation`
  Run an evaluation for a given agent over a dataset. The `agent` can be:
  - a remote agent identifier (`str` or `Agent`), which creates a regular evaluation, or
  - a local Python callable with signature `(messages: list[ChatMessage]) -> AgentReturn`, which creates a local evaluation and submits outputs on your behalf.

- `client.helpers.print_metrics(entity) -> None`
  Print metrics for an evaluation or scan result to the console. For an evaluation, displays a table of metric names, success rates, and pass/fail/error/skipped counts. For a scan result, displays probe categories, names, severity, and issue/attack counts.

For asynchronous usage, use the corresponding methods on `async_client.helpers` (for example, `await async_client.helpers.evaluate(...)`).

## Results

Types:

```python
from giskard_hub.types.evaluation import (
    FailureCategory,
    TaskState,
    TestCaseEvaluation,
)
from giskard_hub.types import (
    TestCase,
    APIPaginatedMetadata,
)
```

Methods:

- <code title="get /v2/evaluations/{evaluation_id}/results/{result_id}">client.evaluations.results.<a href="./src/giskard_hub/resources/evaluations/results.py">retrieve</a>(result_id, \*, evaluation_id, \*\*<a href="src/giskard_hub/types/evaluation.py">params</a>) -> <a href="./src/giskard_hub/types/evaluation.py">TestCaseEvaluation</a></code>
- <code title="patch /v2/evaluations/{evaluation_id}/results/{result_id}">client.evaluations.results.<a href="./src/giskard_hub/resources/evaluations/results.py">update</a>(result_id, \*, evaluation_id, \*\*<a href="src/giskard_hub/types/evaluation.py">params</a>) -> <a href="./src/giskard_hub/types/evaluation.py">TestCaseEvaluation</a></code>
- <code title="get /v2/evaluations/{evaluation_id}/results">client.evaluations.results.<a href="./src/giskard_hub/resources/evaluations/results.py">list</a>(evaluation_id, \*\*<a href="src/giskard_hub/types/evaluation.py">params</a>) -> List[<a href="./src/giskard_hub/types/evaluation.py">TestCaseEvaluation</a>]</code>
- <code title="post /v2/evaluations/{evaluation_id}/results/{result_id}/rerun-test-case">client.evaluations.results.<a href="./src/giskard_hub/resources/evaluations/results.py">rerun_test_case</a>(result_id, \*, evaluation_id) -> <a href="./src/giskard_hub/types/evaluation.py">TestCaseEvaluation</a></code>
- <code title="post /v2/evaluations/{evaluation_id}/results/{result_id}/submit-local-output">client.evaluations.results.<a href="./src/giskard_hub/resources/evaluations/results.py">submit_local_output</a>(result_id, \*, evaluation_id, \*\*<a href="src/giskard_hub/types/evaluation.py">params</a>) -> <a href="./src/giskard_hub/types/evaluation.py">TestCaseEvaluation</a></code>
- <code title="post /v2/evaluations/{evaluation_id}/results/search">client.evaluations.results.<a href="./src/giskard_hub/resources/evaluations/results.py">search</a>(evaluation_id, \*\*<a href="src/giskard_hub/types/evaluation.py">params</a>, include_metadata: bool = False) -> List[<a href="./src/giskard_hub/types/evaluation.py">TestCaseEvaluation</a>] | Tuple[List[<a href="./src/giskard_hub/types/evaluation.py">TestCaseEvaluation</a>], <a href="./src/giskard_hub/types/common/__init__.py">APIPaginatedMetadata</a>]</code>
- <code title="patch /v2/evaluations/{evaluation_id}/results/{result_id}/visibility">client.evaluations.results.<a href="./src/giskard_hub/resources/evaluations/results.py">update_visibility</a>(result_id, \*, evaluation_id, \*\*<a href="src/giskard_hub/types/evaluation.py">params</a>) -> <a href="./src/giskard_hub/types/evaluation.py">TestCaseEvaluation</a></code>

# KnowledgeBases

Types:

```python
from giskard_hub.types import (
    KnowledgeBase,
    KnowledgeBaseDocumentRow,
    KnowledgeBaseDocumentDetail,
    APIPaginatedMetadata,
)
```

Methods:

- <code title="post /v2/knowledge-bases">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">create</a>(\*\*<a href="src/giskard_hub/types/knowledge_base.py">params</a>) -> <a href="./src/giskard_hub/types/knowledge_base.py">KnowledgeBase</a></code>
- <code title="get /v2/knowledge-bases/{knowledge_base_id}">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">retrieve</a>(knowledge_base_id) -> <a href="./src/giskard_hub/types/knowledge_base.py">KnowledgeBase</a></code>
- <code title="patch /v2/knowledge-bases/{knowledge_base_id}">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">update</a>(knowledge_base_id, \*\*<a href="src/giskard_hub/types/knowledge_base.py">params</a>) -> <a href="./src/giskard_hub/types/knowledge_base.py">KnowledgeBase</a></code>
- <code title="get /v2/knowledge-bases">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">list</a>(\*\*<a href="src/giskard_hub/types/knowledge_base.py">params</a>) -> List[<a href="./src/giskard_hub/types/knowledge_base.py">KnowledgeBase</a>]</code>
- <code title="delete /v2/knowledge-bases/{knowledge_base_id}">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">delete</a>(knowledge_base_id) -> None</code>
- <code title="delete /v2/knowledge-bases">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/knowledge_base.py">params</a>) -> None</code>
- <code title="post /v2/knowledge-bases/{knowledge_base_id}/documents/search">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">search_documents</a>(knowledge_base_id, \*\*<a href="src/giskard_hub/types/knowledge_base.py">params</a>, include_metadata: bool = False) -> List[<a href="./src/giskard_hub/types/knowledge_base.py">KnowledgeBaseDocumentRow</a>] | Tuple[List[<a href="./src/giskard_hub/types/knowledge_base.py">KnowledgeBaseDocumentRow</a>], <a href="./src/giskard_hub/types/common/__init__.py">APIPaginatedMetadata</a>]</code>
- <code title="get /v2/knowledge-bases/{knowledge_base_id}/documents/{document_id}">client.knowledge_bases.<a href="./src/giskard_hub/resources/knowledge_bases.py">retrieve_document</a>(knowledge_base_id, document_id) -> <a href="./src/giskard_hub/types/knowledge_base.py">KnowledgeBaseDocumentDetail</a></code>

# Projects

Types:

```python
from giskard_hub.types import (
    Project,
)
```

Methods:

- <code title="post /v2/projects">client.projects.<a href="./src/giskard_hub/resources/projects/projects.py">create</a>(\*\*<a href="src/giskard_hub/types/project.py">params</a>) -> <a href="./src/giskard_hub/types/project.py">Project</a></code>
- <code title="get /v2/projects/{project_id}">client.projects.<a href="./src/giskard_hub/resources/projects/projects.py">retrieve</a>(project_id) -> <a href="./src/giskard_hub/types/project.py">Project</a></code>
- <code title="patch /v2/projects/{project_id}">client.projects.<a href="./src/giskard_hub/resources/projects/projects.py">update</a>(project_id, \*\*<a href="src/giskard_hub/types/project.py">params</a>) -> <a href="./src/giskard_hub/types/project.py">Project</a></code>
- <code title="get /v2/projects">client.projects.<a href="./src/giskard_hub/resources/projects/projects.py">list</a>() -> List[<a href="./src/giskard_hub/types/project.py">Project</a>]</code>
- <code title="delete /v2/projects/{project_id}">client.projects.<a href="./src/giskard_hub/resources/projects/projects.py">delete</a>(project_id) -> None</code>
- <code title="delete /v2/projects">client.projects.<a href="./src/giskard_hub/resources/projects/projects.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/project.py">params</a>) -> None</code>

## Scenarios

Types:

```python
from giskard_hub.types import (
    Scenario,
    ScenarioPreview,
)
```

Methods:

- <code title="post /v2/projects/{project_id}/scenarios">client.projects.scenarios.<a href="./src/giskard_hub/resources/projects/scenarios.py">create</a>(project_id, \*\*<a href="src/giskard_hub/types/scenario.py">params</a>) -> <a href="./src/giskard_hub/types/scenario.py">Scenario</a></code>
- <code title="get /v2/projects/{project_id}/scenarios/{scenario_id}">client.projects.scenarios.<a href="./src/giskard_hub/resources/projects/scenarios.py">retrieve</a>(scenario_id, \*, project_id) -> <a href="./src/giskard_hub/types/scenario.py">Scenario</a></code>
- <code title="patch /v2/projects/{project_id}/scenarios/{scenario_id}">client.projects.scenarios.<a href="./src/giskard_hub/resources/projects/scenarios.py">update</a>(scenario_id, \*, project_id, \*\*<a href="src/giskard_hub/types/scenario.py">params</a>) -> <a href="./src/giskard_hub/types/scenario.py">Scenario</a></code>
- <code title="get /v2/projects/{project_id}/scenarios">client.projects.scenarios.<a href="./src/giskard_hub/resources/projects/scenarios.py">list</a>(project_id) -> List[<a href="./src/giskard_hub/types/scenario.py">Scenario</a>]</code>
- <code title="delete /v2/projects/{project_id}/scenarios/{scenario_id}">client.projects.scenarios.<a href="./src/giskard_hub/resources/projects/scenarios.py">delete</a>(scenario_id, \*, project_id) -> None</code>
- <code title="post /v2/projects/{project_id}/scenarios/preview">client.projects.scenarios.<a href="./src/giskard_hub/resources/projects/scenarios.py">preview</a>(project_id, \*\*<a href="src/giskard_hub/types/scenario.py">params</a>) -> <a href="./src/giskard_hub/types/scenario.py">ScenarioPreview</a></code>

# Scans

Types:

```python
from giskard_hub.types import (
    Agent,
    AgentReference,
    KnowledgeBase,
    Scan,
    ScanCategory,
    ScanProbe,
)
```

Methods:

- <code title="post /v2/scans">client.scans.<a href="./src/giskard_hub/resources/scans/scans.py">create</a>(\*\*<a href="src/giskard_hub/types/scan.py">params</a>) -> <a href="./src/giskard_hub/types/scan.py">Scan</a></code>
- <code title="get /v2/scans/{scan_id}">client.scans.<a href="./src/giskard_hub/resources/scans/scans.py">retrieve</a>(scan_id, \*\*<a href="src/giskard_hub/types/scan.py">params</a>) -> <a href="./src/giskard_hub/types/scan.py">Scan</a></code>
- <code title="get /v2/scans">client.scans.<a href="./src/giskard_hub/resources/scans/scans.py">list</a>(\*\*<a href="src/giskard_hub/types/scan.py">params</a>) -> List[<a href="./src/giskard_hub/types/scan.py">Scan</a>]</code>
- <code title="delete /v2/scans/{scan_id}">client.scans.<a href="./src/giskard_hub/resources/scans/scans.py">delete</a>(scan_id) -> None</code>
- <code title="delete /v2/scans">client.scans.<a href="./src/giskard_hub/resources/scans/scans.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/scan.py">params</a>) -> None</code>
- <code title="get /v2/scan-categories">client.scans.<a href="./src/giskard_hub/resources/scans/scans.py">list_categories</a>() -> List[<a href="./src/giskard_hub/types/scan.py">ScanCategory</a>]</code>
- <code title="get /v2/scans/{scan_id}/probes">client.scans.<a href="./src/giskard_hub/resources/scans/scans.py">list_probes</a>(scan_id) -> List[<a href="./src/giskard_hub/types/scan.py">ScanProbe</a>]</code>

## Probes

Types:

```python
from giskard_hub.types.scan import (
    ScanProbe,
    ScanProbeAttempt,
)
```

Methods:

- <code title="get /v2/scan-probes/{probe_id}">client.scans.probes.<a href="./src/giskard_hub/resources/scans/probes.py">retrieve</a>(probe_id) -> <a href="./src/giskard_hub/types/scan.py">ScanProbe</a></code>
- <code title="get /v2/scan-probes/{probe_id}/attempts">client.scans.probes.<a href="./src/giskard_hub/resources/scans/probes.py">list_attempts</a>(probe_id) -> List[<a href="./src/giskard_hub/types/scan.py">ScanProbeAttempt</a>]</code>

## Attempts

Types:

```python
from giskard_hub.types.scan import (
    ReviewStatus,
    ScanProbeAttempt,
    Severity,
)
```

Methods:

- <code title="patch /v2/scan-attempts/{probe_attempt_id}">client.scans.attempts.<a href="./src/giskard_hub/resources/scans/attempts.py">update</a>(probe_attempt_id, \*\*<a href="src/giskard_hub/types/scan.py">params</a>) -> <a href="./src/giskard_hub/types/scan.py">ScanProbeAttempt</a></code>

# ScheduledEvaluations

Types:

```python
from giskard_hub.types import (
    Agent,
    Dataset,
    ScheduledEvaluation,
    Evaluation,
    ErrorExecutionStatus,
    FrequencyOption,
    SuccessExecutionStatus,
)
```

Methods:

- <code title="post /v2/scheduled-evaluations">client.scheduled_evaluations.<a href="./src/giskard_hub/resources/scheduled_evaluations.py">create</a>(\*\*<a href="src/giskard_hub/types/scheduled_evaluation.py">params</a>) -> <a href="./src/giskard_hub/types/scheduled_evaluation.py">ScheduledEvaluation</a></code>
- <code title="get /v2/scheduled-evaluations/{scheduled_evaluation_id}">client.scheduled_evaluations.<a href="./src/giskard_hub/resources/scheduled_evaluations.py">retrieve</a>(scheduled_evaluation_id, \*\*<a href="src/giskard_hub/types/scheduled_evaluation.py">params</a>) -> <a href="./src/giskard_hub/types/scheduled_evaluation.py">ScheduledEvaluation</a></code>
- <code title="patch /v2/scheduled-evaluations/{scheduled_evaluation_id}">client.scheduled_evaluations.<a href="./src/giskard_hub/resources/scheduled_evaluations.py">update</a>(scheduled_evaluation_id, \*\*<a href="src/giskard_hub/types/scheduled_evaluation.py">params</a>) -> <a href="./src/giskard_hub/types/scheduled_evaluation.py">ScheduledEvaluation</a></code>
- <code title="get /v2/scheduled-evaluations">client.scheduled_evaluations.<a href="./src/giskard_hub/resources/scheduled_evaluations.py">list</a>(\*\*<a href="src/giskard_hub/types/scheduled_evaluation.py">params</a>) -> List[<a href="./src/giskard_hub/types/scheduled_evaluation.py">ScheduledEvaluation</a>]</code>
- <code title="delete /v2/scheduled-evaluations/{scheduled_evaluation_id}">client.scheduled_evaluations.<a href="./src/giskard_hub/resources/scheduled_evaluations.py">delete</a>(scheduled_evaluation_id) -> None</code>
- <code title="delete /v2/scheduled-evaluations">client.scheduled_evaluations.<a href="./src/giskard_hub/resources/scheduled_evaluations.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/scheduled_evaluation.py">params</a>) -> None</code>
- <code title="get /v2/scheduled-evaluations/{scheduled_evaluation_id}/evaluations">client.scheduled_evaluations.<a href="./src/giskard_hub/resources/scheduled_evaluations.py">list_evaluations</a>(scheduled_evaluation_id, \*\*<a href="src/giskard_hub/types/scheduled_evaluation.py">params</a>) -> List[<a href="./src/giskard_hub/types/evaluation.py">Evaluation</a>]</code>

# TestCases

Types:

```python
from giskard_hub.types import (
    TestCase,
    TestCaseComment,
    TestCaseCheckConfig,
    ChatMessageWithMetadata,
)
```

Methods:

- <code title="post /v2/test-cases">client.test_cases.<a href="./src/giskard_hub/resources/test_cases/test_cases.py">create</a>(\*\*<a href="src/giskard_hub/types/test_case.py">params</a>) -> <a href="./src/giskard_hub/types/test_case.py">TestCase</a></code>
- <code title="get /v2/test-cases/{test_case_id}">client.test_cases.<a href="./src/giskard_hub/resources/test_cases/test_cases.py">retrieve</a>(test_case_id) -> <a href="./src/giskard_hub/types/test_case.py">TestCase</a></code>
- <code title="patch /v2/test-cases/{test_case_id}">client.test_cases.<a href="./src/giskard_hub/resources/test_cases/test_cases.py">update</a>(test_case_id, \*\*<a href="src/giskard_hub/types/test_case.py">params</a>) -> <a href="./src/giskard_hub/types/test_case.py">TestCase</a></code>
- <code title="delete /v2/test-cases/{test_case_id}">client.test_cases.<a href="./src/giskard_hub/resources/test_cases/test_cases.py">delete</a>(test_case_id) -> None</code>
- <code title="delete /v2/test-cases">client.test_cases.<a href="./src/giskard_hub/resources/test_cases/test_cases.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/test_case.py">params</a>) -> None</code>
- <code title="patch /v2/test-cases">client.test_cases.<a href="./src/giskard_hub/resources/test_cases/test_cases.py">bulk_update</a>(\*\*<a href="src/giskard_hub/types/test_case.py">params</a>) -> List[<a href="./src/giskard_hub/types/test_case.py">TestCase</a>]</code>
- <code title="post /v2/test-cases/bulk-move">client.test_cases.<a href="./src/giskard_hub/resources/test_cases/test_cases.py">bulk_move</a>(\*\*<a href="src/giskard_hub/types/test_case.py">params</a>) -> None</code>

## Comments

Types:

```python
from giskard_hub.types import (
    TestCaseComment,
)
```

Methods:

- <code title="delete /v2/test-cases/{test_case_id}/comments/{comment_id}">client.test_cases.comments.<a href="./src/giskard_hub/resources/test_cases/comments.py">delete</a>(comment_id, \*, test_case_id) -> None</code>
- <code title="post /v2/test-cases/{test_case_id}/comments">client.test_cases.comments.<a href="./src/giskard_hub/resources/test_cases/comments.py">add</a>(test_case_id, \*\*<a href="src/giskard_hub/types/test_case.py">params</a>) -> <a href="./src/giskard_hub/types/test_case.py">TestCaseComment</a></code>
- <code title="patch /v2/test-cases/{test_case_id}/comments/{comment_id}">client.test_cases.comments.<a href="./src/giskard_hub/resources/test_cases/comments.py">edit</a>(comment_id, \*, test_case_id, \*\*<a href="src/giskard_hub/types/test_case.py">params</a>) -> <a href="./src/giskard_hub/types/test_case.py">TestCaseComment</a></code>

# Tasks

Types:

```python
from giskard_hub.types import (
    Task,
    TaskStatus,
    TaskPriority,
)
```

Methods:

- <code title="post /v2/tasks">client.tasks.<a href="./src/giskard_hub/resources/tasks.py">create</a>(\*\*<a href="src/giskard_hub/types/task.py">params</a>) -> <a href="./src/giskard_hub/types/task.py">Task</a></code>
- <code title="get /v2/tasks/{task_id}">client.tasks.<a href="./src/giskard_hub/resources/tasks.py">retrieve</a>(task_id) -> <a href="./src/giskard_hub/types/task.py">Task</a></code>
- <code title="patch /v2/tasks/{task_id}">client.tasks.<a href="./src/giskard_hub/resources/tasks.py">update</a>(task_id, \*\*<a href="src/giskard_hub/types/task.py">params</a>) -> <a href="./src/giskard_hub/types/task.py">Task</a></code>
- <code title="get /v2/tasks">client.tasks.<a href="./src/giskard_hub/resources/tasks.py">list</a>(\*\*<a href="src/giskard_hub/types/task.py">params</a>) -> List[<a href="./src/giskard_hub/types/task.py">Task</a>]</code>
- <code title="delete /v2/tasks/{task_id}">client.tasks.<a href="./src/giskard_hub/resources/tasks.py">delete</a>(task_id) -> None</code>
- <code title="delete /v2/tasks">client.tasks.<a href="./src/giskard_hub/resources/tasks.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/task.py">params</a>) -> None</code>

# PlaygroundChats

Types:

```python
from giskard_hub.types import (
    Agent,
    PlaygroundChat,
)
```

Methods:

- <code title="get /v2/playground-chats">client.playground_chats.<a href="./src/giskard_hub/resources/playground_chats.py">list</a>(\*\*<a href="src/giskard_hub/types/playground_chat.py">params</a>) -> List[<a href="./src/giskard_hub/types/playground_chat.py">PlaygroundChat</a>]</code>
- <code title="get /v2/playground-chats/{chat_id}">client.playground_chats.<a href="./src/giskard_hub/resources/playground_chats.py">retrieve</a>(chat_id, \*\*<a href="src/giskard_hub/types/playground_chat.py">params</a>) -> <a href="./src/giskard_hub/types/playground_chat.py">PlaygroundChat</a></code>
- <code title="delete /v2/playground-chats/{chat_id}">client.playground_chats.<a href="./src/giskard_hub/resources/playground_chats.py">delete</a>(chat_id) -> None</code>
- <code title="delete /v2/playground-chats">client.playground_chats.<a href="./src/giskard_hub/resources/playground_chats.py">bulk_delete</a>(\*\*<a href="src/giskard_hub/types/playground_chat.py">params</a>) -> None</code>
