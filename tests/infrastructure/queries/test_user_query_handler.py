import pytest

from src.infrastructure.queries.user import GetUserQuery, GetUserQueryHandler


@pytest.fixture(scope='class')
def query_handler(user_repo):
    return GetUserQueryHandler(repository=user_repo)


class TestGetUserQueryHandler:
    @pytest.mark.asyncio
    async def test_get_user_query_handler_success(self, query_handler: GetUserQueryHandler):
        assert query_handler
        assert await query_handler.handle(GetUserQuery()) == ()

    @pytest.mark.asyncio
    async def test_get_user_query_handler_invalid_query(self, query_handler: GetUserQueryHandler):
        with pytest.raises(TypeError):
            await query_handler.handle()
    