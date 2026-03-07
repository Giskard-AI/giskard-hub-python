# File generated for ContextAnnotation schema

from __future__ import annotations

from giskard_hub.types import ContextAnnotation


class TestContextAnnotation:
    def test_context_annotation_creation(self) -> None:
        annotation = ContextAnnotation.construct(
            end_char_index=100,
            label="test_label",
            start_char_index=50,
            text="sample text",
            type="context",
        )
        assert annotation.end_char_index == 100
        assert annotation.label == "test_label"
        assert annotation.start_char_index == 50
        assert annotation.text == "sample text"
        assert annotation.type == "context"

    def test_context_annotation_type_validation(self) -> None:
        annotation = ContextAnnotation.construct(
            end_char_index=100,
            label="label",
            start_char_index=50,
            text="text",
            type="context",
        )
        assert annotation.type == "context"

    def test_context_annotation_serialization(self) -> None:
        annotation = ContextAnnotation.construct(
            end_char_index=100,
            label="label",
            start_char_index=50,
            text="text",
            type="context",
        )
        data = annotation.model_dump()
        assert data["end_char_index"] == 100
        assert data["label"] == "label"
        assert data["start_char_index"] == 50
        assert data["text"] == "text"
        assert data["type"] == "context"
