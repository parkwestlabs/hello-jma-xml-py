import pytest

from main import main


def test_main(caplog: pytest.LogCaptureFixture):
    main()

    assert "Hello from hello-jma-xml-py!" in caplog.text
