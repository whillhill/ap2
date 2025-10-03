# ap2 (Agent Payments Protocol for Python)

This repository provides a Python package for the Agent Payments Protocol (AP2), plus example roles and runnable scenarios mirroring the official repository. The PyPI package contains only the core library under `src/ap2`.

Repository: `https://github.com/whillhill/ap2`

<p align="center">
  <img src="docs_ap2/assets/ap2_graphic.png" alt="Agent Payments Protocol Graphic">
  
</p>

## Intro to AP2 Video

[Watch the introduction video](https://goo.gle/ap2-video)

## About the Examples

The example scenarios use Google's Agent Development Kit (ADK) and Gemini 2.5 Flash in the official repo. AP2 itself does not require ADK or Gemini; you can use any stack that can speak the protocol. In this repository, examples are mirrored under `examples/` for convenience and do not ship in the PyPI package.

## Installation

From PyPI (recommended when published):
```bash
pip install ap2
```

From source (editable):
```bash
pip install -e .
# or
uv pip install -e .
```

Optional dependencies for running examples:
```bash
pip install "ap2[examples]"
```

## Quickstart

Minimal Payment Request model (aligned with the W3C Payment Request concepts):

```python
from ap2.types.payment_request import (
    PaymentCurrencyAmount, PaymentItem, PaymentDetailsInit,
    PaymentMethodData, PaymentRequest,
)

amount = PaymentCurrencyAmount(currency="USD", value=10.0)
total = PaymentItem(label="Total", amount=amount)
details = PaymentDetailsInit(id="order-1", display_items=[total], total=total)
req = PaymentRequest(
    method_data=[PaymentMethodData(supported_methods="basic-card")],
    details=details,
)
payload = req.model_dump()
```

Runtime helpers live in `ap2.common.*` (server scaffolding, executors, tool resolver, etc.). They are optional and replaceable.

## Repository Layout

```
src/ap2/
  types/   # Canonical protocol models (Payment Request, Contact Picker, Mandates)
  common/  # Runtime scaffolding (server, base executor, tool resolver)
examples/
  roles/       # Reference role implementations (demo-only)
  scenarios/   # Mirrored scenario scripts from the official repo
docs_ap2/      # Official documentation mirror (read-only)
```

Note: `examples/*` and `docs_ap2/*` are not included in the PyPI package.

## Prerequisites (for examples)

- Python 3.10+
- Optional: [`uv`](https://docs.astral.sh/uv/getting-started/installation/) package manager

## Setup (Credentials for LLM-backed scenarios)

You can authenticate using either a Google API Key or Vertex AI. Set these as environment variables in your shell or in a local `.env` file.

Google API Key (recommended for development):
```bash
export GOOGLE_API_KEY='your_key'
```

Vertex AI (recommended for production):
```bash
export GOOGLE_GENAI_USE_VERTEXAI=true
export GOOGLE_CLOUD_PROJECT='your-project-id'
export GOOGLE_CLOUD_LOCATION='global'
# Then authenticate, for example:
gcloud auth application-default login
# or set a service account:
export GOOGLE_APPLICATION_CREDENTIALS='/path/to/service-account-key.json'
```

## How to Run a Scenario (examples)

Each scenario contains a `README.md` and a `run.sh` script. A typical flow:

```bash
# from repo root
bash examples/scenarios/a2a/human-present/cards/run.sh
```

Open the shopping agent URL indicated by the script and follow the instructions.

## Build and Publish

```bash
python -m build
twine upload dist/*
```

The `pyproject.toml` is configured for an src-layout and packages only the `ap2*` namespace. License files (including third-party notices) are included.

## Documentation

- Local mirror: `docs_ap2/` (sourced from the official AP2 repository)
  - High-level overview: `docs_ap2/topics/what-is-ap2.md`
  - Life of a transaction: `docs_ap2/topics/life-of-a-transaction.md`
  - AP2 with A2A/MCP: `docs_ap2/topics/ap2-a2a-and-mcp.md`
  - Privacy & Security: `docs_ap2/topics/privacy-and-security.md`
  - Full specification: `docs_ap2/specification.md`

## License

- This repository: MIT (see `LICENSE`).
- Upstream assets: Portions mirrored from the official AP2 repository under Apache-2.0 (see `THIRD_PARTY_LICENSES/`).

## Acknowledgements

This project aligns with and mirrors content from the official AP2 repository: `google-agentic-commerce/AP2`.
