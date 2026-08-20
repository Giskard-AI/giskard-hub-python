"""Deprecated scenario aliases of the prompt preset types."""

from typing import Any, Dict, List
from typing_extensions import deprecated

from .prompt_preset import (
    PromptPreset,
    PromptPresetPreview,
    PromptPresetCreateParams,
    PromptPresetUpdateParams,
    PromptPresetPreviewParams,
)

__all__ = [
    "Scenario",
    "ScenarioPreview",
    "ScenarioCreateParams",
    "ScenarioUpdateParams",
    "ScenarioPreviewParams",
]


class Scenario(PromptPreset):
    pass


class ScenarioPreview(PromptPresetPreview):
    @property
    @deprecated("`ScenarioPreview.conversation` is deprecated; read `inputs` instead.")
    def conversation(self) -> List[Dict[str, Any]]:
        """Deprecated alias for `inputs`."""
        return self.inputs


ScenarioCreateParams = PromptPresetCreateParams
ScenarioUpdateParams = PromptPresetUpdateParams
ScenarioPreviewParams = PromptPresetPreviewParams
