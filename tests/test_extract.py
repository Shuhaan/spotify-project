from extract import extract
import pytest


class TestExtract:
    def test_extract_function_execution_is_successful(self):
        response = extract("https://api.spotify.com")

        assert response.status_code == 200
