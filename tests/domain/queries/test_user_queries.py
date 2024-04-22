from src.domain.queries.user import GetUserQuery


class TestGetUserQuery:
    def test_create_user_query_success(self):
        assert GetUserQuery("idd", "username")

    def test_create_user_query_success2(self):
        assert GetUserQuery()
            