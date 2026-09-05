from calculator.cli.main import main


def test_cli_displays_all_results(capsys) -> None:
    exit_code = main(["10", "2"])

    output = capsys.readouterr().out
    assert exit_code == 0
    assert "Addition:       12.0" in output
    assert "Subtraction:    8.0" in output
    assert "Multiplication: 20.0" in output
    assert "Division:       5.0" in output


def test_cli_handles_division_by_zero(capsys) -> None:
    exit_code = main(["10", "0"])

    output = capsys.readouterr().out
    assert exit_code == 0
    assert "Addition:       10.0" in output
    assert "Division:       Cannot divide by zero." in output
