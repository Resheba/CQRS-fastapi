import pytest

from src.infrastructure.queries.post import GetPostQuery, GetPostQueryHandler


@pytest.fixture(scope='class')
def query_handler(repo):
    return GetPostQueryHandler(repository=repo)


class TestGetPostQueryHandler:
    @pytest.mark.asyncio
    async def test_get_post_query_handler_success(self, query_handler: GetPostQueryHandler):
        assert query_handler
        assert await query_handler.handle(GetPostQuery()) == ()

    @pytest.mark.asyncio
    async def test_get_post_query_handler_invalid_query(self, query_handler: GetPostQueryHandler):
        with pytest.raises(TypeError):
            await query_handler.handle()

