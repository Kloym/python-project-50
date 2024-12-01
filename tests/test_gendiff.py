from gendiff.scripts.gen_diff import generate_diff


def test_json():
    with open("tests/fixtures/diff.txt", "r") as f3:
        result = f3.read()

    actual_diff = generate_diff(
        "tests/fixtures/file1.json", "tests/fixtures/file2.json"
    )
    assert actual_diff == result


def test_yaml():
    with open("tests/fixtures/diff.txt", "r") as f3:
        result = f3.read()
    actual_diff = generate_diff("tests/fixtures/file1.yml", "tests/fixtures/file2.yml")
    assert actual_diff == result
