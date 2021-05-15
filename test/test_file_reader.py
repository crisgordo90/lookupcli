import pytest
import file_reader


@pytest.fixture()
def fr() -> list:
    return file_reader.fetch_ips("../fixtures/list_of_ips.txt")


def test_all_ips_found(fr):
    assert len(fr) == 5000


def test_first_ip_present(fr):
    assert "244.36.171.60" in fr


def test_last_ip_present(fr):
    assert "189.77.141.131" in fr


def test_ips_in_same_phrase_present(fr):
    assert "81.44.150.240" in fr


def test_random_ip_between_present(fr):
    assert "163.52.36.226" in fr


def test_ip_is_not_present(fr):
    assert "8.8.4.4" not in fr
