#!/usr/bin/env -S uv run python
"""Connect a local echo agent to Giskard Hub until interrupted.

Hub creates the agent on connect and deletes it on disconnect.
Requires GISKARD_HUB_BASE_URL and GISKARD_HUB_API_KEY.
"""

from typing import Any

from giskard_hub import HubClient


def echo(payload: dict[str, Any]) -> dict[str, Any]:
    text = payload["messages"][-1]["content"]
    return {"response": {"role": "assistant", "content": text}}


def main() -> None:
    hub = HubClient()
    handshake = hub.connect_local_agent(handler=echo, name="Local echo")
    print(handshake)


if __name__ == "__main__":
    main()
