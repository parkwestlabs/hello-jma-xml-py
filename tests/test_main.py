from main import main


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello from hello-jma-xml-py!" in captured.out
