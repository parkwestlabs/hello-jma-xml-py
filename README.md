# hello-jma-xml-py
気象庁の天気予報 XML を Python lxml でパースする hello world example コードです。

## Init Project Notes

```bash
uv init --app .
mkdir src tests
mv main.py ./src

uv add --dev ruff pyright pytest

uv run pytest
uv run src/main.py
```
