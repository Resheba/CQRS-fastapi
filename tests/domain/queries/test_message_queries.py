from src.domain.queries.message import GetMessageQuery


class TestGetMessageQuery:
    def test_create_message_query_success(self):
        assert GetMessageQuery(id="idd", message="tmessage", user_id="idd")

    def test_create_message_query_success2(self):
        assert GetMessageQuery()
            