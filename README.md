# bedocu

## Getting Started

- Create Python virtual environment
  - `python3 -m venv .venv`
  - `source .venv/bin/activate`
- Install dependencies
  - `pip install -r requirements.txt`
- Login to `gcloud`
  - `gcloud auth application-default login`
  - `gcloud config set project fdc-gen-ai-test`
  - `gcloud auth application-default set-quota-project fdc-gen-ai-test`
