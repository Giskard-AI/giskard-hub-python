# Type Organization and Naming Conventions

## Naming Patterns

### Resource Models (BaseModel classes)
- Pattern: `{Resource}` (e.g., `Agent`, `Dataset`, `Project`)
- Purpose: Core domain models
- Location: Root types folder

### API Resources (BaseModel classes)
- Pattern: `{Resource}APIResource` (e.g., `ProjectAPIResource`, `EvaluationAPIResource`)
- Purpose: API-specific resource representations
- Location: Root types folder

### Parameter Types (TypedDict)
- Pattern: `{Resource}{Operation}Params` (e.g., `AgentCreateParams`, `DatasetUpdateParams`)
- Purpose: Input parameters for API operations
- Operations: `Create`, `Update`, `List`, `BulkDelete`, `Retrieve`, etc.
- Location: Root types folder

### Parameter Input Types (TypedDict) 
- Pattern: `{Type}Param` (singular, e.g., `HeaderParam`, `ModelOutputParam`)
- Purpose: TypedDict versions of BaseModel classes for input
- Location: Root types folder

### Response Types (BaseModel)
- Pattern: `{Resource}{Operation}Response` (e.g., `AgentListResponse`, `ScanCreateResponse`)
- Purpose: Response models for specific operations
- Location: Root types folder

### API Response Wrappers (BaseModel)
- Pattern: `APIResponse{Resource}` (e.g., `APIResponseAgent`, `APIResponseDataset`)
- Purpose: Generic API envelope wrapping resource data
- Location: Root types folder or `common/responses.py` for generic versions

## Type Categories

### 1. Common Types (`common/`)
- Generic response wrappers
- Shared parameter types
- Common enums and literals

### 2. Resource-Specific Types
Organized by resource (agents, datasets, evaluations, etc.):
- Create/Update/List params
- Response types
- Resource-specific models

### 3. Subdirectories
- `evaluations/` - Evaluation result types
- `scans/` - Scan probe and attempt types
- `test_cases/` - Test case comment types

## Consolidation Opportunities

### API Response Wrappers
Many API response wrappers follow the same pattern:
```python
class APIResponse{Resource}(BaseModel):
    data: {Resource}
```

These can be replaced with a generic `APIResponse[T]` type from `common/responses.py`.

### List Responses  
List response types follow a similar pattern:
```python
class {Resource}ListResponse(BaseModel):
    data: List[{Resource}]
```

These can use a generic `APIResponse[List[T]` type.

## Migration Strategy

1. Keep existing files for backward compatibility
2. Create aliases using generic types
3. Update new code to use generic types
4. Gradually deprecate specific wrapper types
