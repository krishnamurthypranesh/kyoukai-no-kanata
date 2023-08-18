from unittest import mock
import uuid

from fastapi import status
from fastapi.testclient import TestClient
import pytest

from app.main import app

client = TestClient(app)

class TestDoOp:
    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self, request):
        with mock.patch("app.clients.httpbin.requests") as m:
            request.cls.mock_client = m

            yield

    @pytest.fixture(scope="function", autouse=True)
    def setup_function(self, provide_db):
        self.mock_client.reset_mock()

        yield

    def test_returns_uuid(self):
        gid = str(uuid.uuid1())

        self.mock_client.get.return_value.json.return_value = {"uuid": gid}
        response = client.post(
            "/v1/ops",
        )

        assert response is not None
        assert response.status_code == status.HTTP_200_OK

        assert response.json() == {"uuid": gid}

    def test_saves_record_correctly(self):
        assert 1 == 0

    def test_returns_500_if_uuid_cannot_be_generated(self):
        assert 1 == 0

