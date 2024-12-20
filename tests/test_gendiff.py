from gendiff.scripts.get_diff import generate_diff

with open("tests/fixtures/1stylysh_diff.txt", "r") as f:
    result_stylish = f.read().strip()
with open("tests/fixtures/2plain_diff.txt", "r") as f:
    result_plain = f.read().strip()
with open("tests/fixtures/3json_diff.txt", "r") as f:
    result_json = f.read().strip()
with open("tests/fixtures/excpected_stylish.txt", "r") as f:
    result_nested_stylish = f.read().strip()
with open("tests/fixtures/excpected_plain.txt", "r") as f:
    result_nested_plain = f.read().strip()
with open("tests/fixtures/expected.json.txt", "r") as f:
    result_nested_json = f.read().strip()


def test_flat_files_stylish():
    assert result_stylish == generate_diff(
        "tests/fixtures/file1.json", "tests/fixtures/file2.json"
    )
    assert result_stylish == generate_diff(
        "tests/fixtures/file1.yml", "tests/fixtures/file2.yml"
    )


def test_nested_files_stylish():
    assert result_nested_stylish == generate_diff(
        "tests/" "fixtures/file1_before.json",
        "tests/" "fixtures/file2_before.json",
        "stylish",
    )
    assert result_nested_stylish == generate_diff(
        "tests/" "fixtures/file1_before.yml",
        "tests/" "fixtures/file2_before.yml",
        "stylish",
    )


def test_flat_files_plain():
    with open("tests/fixtures/2plain_diff.txt", "r") as fixtures:
        expected_lines = fixtures.read()
        result_plain = generate_diff(
            "tests/fixtures/file1.json", "tests/fixtures/file2.json", "plain"
        )
    for line in expected_lines:
        assert line in result_plain


def test_nested_files_plain():
    with open("tests/fixtures/result1.txt", "w") as f3:
        f3.write(
            generate_diff(
                "tests/" "fixtures/file1_before.yml",
                "tests/" "fixtures/file2_before.yml",
                "plain",
            )
        )
    assert result_nested_plain == generate_diff(
        "tests/" "fixtures/file1_before.yml",
        "tests/" "fixtures/file2_before.yml",
        "plain",
    )


def test_flat_files_json():
    assert result_json == generate_diff(
        "tests/fixtures/" "file1.json", "tests/fixtures/" "file2.json", "json"
    )
    assert result_json == generate_diff(
        "tests/fixtures/" "file1.yml", "tests/fixtures/" "file2.yml", "json"
    )


def test_nested_files_json():
    assert result_nested_json == generate_diff(
        "tests/fixtures/" "file1_before.json",
        "tests/fixtures/" "file2_before.json",
        "json",
    )
    assert result_nested_json == generate_diff(
        "tests/fixtures/" "file1_before.yml",
        "tests/fixtures/" "file2_before.yml",
        "json",
    )
