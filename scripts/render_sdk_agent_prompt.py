import argparse
from pathlib import Path


def render_prompt(summary: str) -> str:
    template_path = (
        Path(__file__).resolve().parents[1] / "prompts" / "sdk_agent_prompt.md"
    )
    template = template_path.read_text(encoding="utf-8")
    return template.replace("{{SUMMARY}}", summary)


def main() -> None:
    parser = argparse.ArgumentParser(description="Render SDK agent prompt content")
    parser.add_argument(
        "--summary",
        default="",
        help="API changes summary to embed in the prompt",
    )
    args = parser.parse_args()
    print(render_prompt(args.summary))


if __name__ == "__main__":
    main()
