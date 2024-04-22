from src.domain.queries.post import GetPostQuery


class TestGetPostQuery:
    def test_create_post_query_success(self):
        assert GetPostQuery(id="idd", title="ttitle", text="ttext", user_id="idd")

    def test_create_post_query_success2(self):
        assert GetPostQuery()
            