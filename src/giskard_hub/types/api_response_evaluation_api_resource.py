from .._models import BaseModel
from .evaluation_api_resource import EvaluationAPIResource

__all__ = ["APIResponseEvaluationAPIResource"]


class APIResponseEvaluationAPIResource(BaseModel):
    data: EvaluationAPIResource
