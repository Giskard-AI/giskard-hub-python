# Type Naming Conventions Guide

## Overview

This guide explains the naming conventions used for types in the Giskard Hub SDK. Following these conventions ensures consistency and makes the codebase easier to understand.

## Type Categories and Naming Patterns

### 1. Core Models (Response Types)
**Pattern**: `{Resource}`  
**Purpose**: Main domain objects representing API resources in responses  
**Base**: `BaseModel` (Pydantic)  
**Examples**: `Agent`, `Dataset`, `Project`, `TestCase`

### 2. API Resources  
**Pattern**: `{Resource}APIResource`  
**Purpose**: API-specific representations that may differ from core models  
**Base**: `BaseModel` (Pydantic)  
**Examples**: `ProjectAPIResource`, `EvaluationAPIResource`, `CheckAPIResource`

### 3. Input Parameters (Operation-Specific)
**Pattern**: `{Resource}{Operation}Params`  
**Purpose**: Input parameters for specific API operations  
**Base**: `TypedDict`  
**Operations**: `Create`, `Update`, `List`, `Retrieve`, `BulkDelete`, etc.  
**Examples**: 
- `AgentCreateParams` - Parameters for creating an agent
- `DatasetUpdateParams` - Parameters for updating a dataset
- `EvaluationListParams` - Query parameters for listing evaluations

### 4. Input Parameter Types (Component-Level)
**Pattern**: `{Type}Param` (singular)  
**Purpose**: TypedDict versions of BaseModel types for use as input parameters  
**Base**: `TypedDict`  
**Relationship**: For each `{Type}` BaseModel, there's often a `{Type}Param` TypedDict  
**Examples**:
- `Header` (BaseModel) ↔ `HeaderParam` (TypedDict)
- `ChatMessage` (BaseModel) ↔ `ChatMessageParam` (TypedDict)
- `ModelOutput` (BaseModel) ↔ `ModelOutputParam` (TypedDict)
- `ExecutionError` (BaseModel) ↔ `ExecutionErrorParam` (TypedDict)

**Why both?**
- `BaseModel` types are used for response parsing and validation
- `TypedDict` types (`*Param`) are used for input parameters to provide better IDE support and type checking without Pydantic overhead

### 5. Response Wrappers
**Pattern**: `{Resource}{Operation}Response`  
**Purpose**: Response models for specific operations  
**Base**: `BaseModel`  
**Examples**:
- `AgentListResponse` - Response for listing agents
- `ScanCreateResponse` - Response for creating a scan
- `EvaluationRunSingleResponse` - Response for running a single evaluation

### 6. Generic API Response Wrappers
**Pattern**: `APIResponse{Resource}` or use generic `APIResponse[T]`  
**Purpose**: Generic envelope wrapping API responses  
**Base**: `BaseModel`  
**Examples**:
- `APIResponseAgent` wraps `Agent`
- `APIResponseDataset` wraps `Dataset`
- Or use: `APIResponse[Agent]`, `APIResponse[Dataset]`

### 7. Check/Evaluation Configuration Types
**Pattern**: `{ConfigType}Params` and `{ConfigType}ParamsParam`  
**Purpose**: Configuration for specific check types  
**Examples**:
- `ConformityParams` (BaseModel) ↔ `ConformityParamsParam` (TypedDict)
- `CorrectnessParams` (BaseModel) ↔ `CorrectnessParamsParam` (TypedDict)
- `GroundednessParams` (BaseModel) ↔ `GroundednessParamsParam` (TypedDict)

### 8. Enums and Literals
**Pattern**: `{Name}` (PascalCase, no suffix)  
**Purpose**: Enumerated types and string literals  
**Base**: `str`, `Enum`, or `Literal` types  
**Examples**: `ActionType`, `FrequencyOption`, `Metric`, `Severity`, `ReviewStatus`

## Special Cases

### Execution Status Types
Status types follow a special pattern with both model and param versions:
- `SuccessExecutionStatus` / `SuccessExecutionStatusParam`
- `ErrorExecutionStatus` / `ErrorExecutionStatusParam`

### Audit Types
- `AuditAPIResource` - The audit resource
- `AuditDisplayAPIResponse` - Display-friendly audit response
- `AuditDiffItem` - Individual diff item
- `AuditDiffKind` - Type of diff operation

### Paginated Responses
For responses with pagination metadata:
- Use `APIPaginatedResponse[T]` from `common/responses.py`
- Or specific types like `APIResponseAudit` which include `PaginatedMetadata`

## Best Practices

### When to Create New Types

1. **Create a `*Params` TypedDict** when defining input parameters for an API operation
2. **Create a `*Param` TypedDict** when you have a BaseModel that needs an input equivalent
3. **Create a `*Response` BaseModel** when the operation returns a complex response structure
4. **Use generic types** (like `APIResponse[T]`) when possible instead of creating resource-specific wrappers

### When to Use Existing Generics

Instead of creating new types, use these generics from `common/`:
- `APIResponse[T]` - Single resource response
- `APIResponse[List[T]` - List of resources response  
- `APIPaginatedResponse[T]` - Paginated list with metadata
- `APIResponseWithIncluded[T, TIncluded]` - Response with included related resources

### Import Organization

Types are organized in `__init__.py` by category:
1. Common types (generics)
2. Core models
3. API resources
4. Resource-specific types (grouped by resource: Agent, Dataset, etc.)
5. Shared component types
6. Enums

## Examples

### Creating Parameters for a New Operation

```python
# Good: Clear operation name
class DatasetGenerateParams(TypedDict, total=False):
    project_id: Required[str]
    agent_id: Required[str]
    n_examples: int

# Bad: Unclear purpose
class DatasetParams(TypedDict):
    ...
```

### Using Generic Response Types

```python
# Good: Use generic type
response: APIResponse[Agent] = client.agents.retrieve(agent_id)

# Also acceptable: Use specific wrapper if it exists
response: APIResponseAgent = client.agents.retrieve(agent_id)
```

### Creating Input Parameter Types

```python
# Core model (for responses)
class ChatMessage(BaseModel):
    role: str
    content: str

# Input parameter version (for requests)
class ChatMessageParam(TypedDict, total=False):
    role: Required[str]
    content: Required[str]
```

## Migration Notes

When adding new types:
1. Follow the established patterns above
2. Add to appropriate section in `__init__.py`
3. Add to `__all__` export list
4. Document in this guide if creating a new pattern
