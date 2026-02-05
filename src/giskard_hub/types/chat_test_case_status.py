from typing_extensions import Literal

__all__ = ["ChatTestCaseStatus"]

ChatTestCaseStatus = Literal["pass", "fail", "error", "skipped"]
