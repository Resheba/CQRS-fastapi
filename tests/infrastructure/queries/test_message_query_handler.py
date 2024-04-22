import pytest

from src.infrastructure.queries.message import GetMessageQuery, GetMessageQueryHandler


@pytest.fixture(scope='class')
def query_handler(message_repo):
    return GetMessageQueryHandler(repository=message_repo)


class TestGetMessageQueryHandler:
    @pytest.mark.asyncio
    async def test_get_message_query_handler_success(self, query_handler: GetMessageQueryHandler):
        assert query_handler
        assert await query_handler.handle(GetMessageQuery()) == ()

    @pytest.mark.asyncio
    async def test_get_message_query_handler_invalid_query(self, query_handler: GetMessageQueryHandler):
        with pytest.raises(TypeError):
            await query_handler.handle()


