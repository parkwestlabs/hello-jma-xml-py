# hello-jma-xml-py
気象庁の天気予報 XML を Python lxml でパースする hello world example コードです。

## Quick Start

```bash
uv sync
./check.sh
uv run pytest -v

# uv run に .env を読ませる設定
# (VSCodeのTerminalは自動で.envを読み込むので不要)
cp .env.example .env
export UV_ENV_FILE=".env"

uv run src/main.py
```

## Init Project Notes

```bash
uv init --app .
mkdir src tests
mv main.py ./src

uv add --dev ruff pyright pytest pytest-cov
```
