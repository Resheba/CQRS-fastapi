import pytest

# from src.infrastructure.exceptions.command import InvalidCommandTypeException
from src.infrastructure.commands.post import CreatePostCommandHandler, DeletePostCommandHandler
from src.infrastructure.exceptions.command import InvalidCommandTypeException
from src.infrastructure.repository.post.memory import PostMemoryRepository
from src.domain.exceptions.descriptors import TooLongValueException, TooShortValueException
from src.infrastructure.commands.post import CreatePostCommand, DeletePostCommand, Post, Text, Title


@pytest.fixture(scope='class')
def create_handler(post_repo: PostMemoryRepository):
    return CreatePostCommandHandler(repository=post_repo)

@pytest.fixture(scope='class')
def delete_handler(post_repo: PostMemoryRepository):
    return DeletePostCommandHandler(repository=post_repo)
    

class TestCreatePostCommandHandler:
    @pytest.mark.asyncio
    async def test_create_post_success(self, post_repo: PostMemoryRepository, create_handler: CreatePostCommandHandler):
        command: CreatePostCommand = CreatePostCommand(
            text='Simple text test',
            title='Just a Title',
            user_id='user_id'
        )
        post: Post = await create_handler.handle(command=command)
        assert len(await post_repo.get()) == 1
        assert post.text == Text('Simple text test')
        assert post.title == Title('Just a Title')
        assert post.user_id == 'user_id'

    @pytest.mark.asyncio
    async def test_create_post_invalid_title_failure(self, post_repo: PostMemoryRepository, create_handler: CreatePostCommandHandler):
        command: CreatePostCommand = CreatePostCommand(
            text='Simple text test',
            title='a'*100,
            user_id='user_id'
        )
        with pytest.raises(TooLongValueException):
            await create_handler.handle(command=command)
        
    @pytest.mark.asyncio
    async def test_create_post_invalid_text_failure(self, post_repo: PostMemoryRepository, create_handler: CreatePostCommandHandler):
        command: CreatePostCommand = CreatePostCommand(
            text='',
            title='Just a Title',
            user_id='user_id'
        )

        with pytest.raises(TooShortValueException):
            await create_handler.handle(command=command)
            
    @pytest.mark.asyncio
    async def test_create_post_success2(self, post_repo: PostMemoryRepository, create_handler: CreatePostCommandHandler):
        command: CreatePostCommand = CreatePostCommand(
            text='Simple text test 2',
            title='Just a Title 2',
            user_id='user_id2'
        )
        post = await create_handler.handle(command=command)
        print(post)
        assert len(await post_repo.get()) == 2
    
    @pytest.mark.asyncio
    async def test_create_post_command_invalid_command_failure(self, post_repo: PostMemoryRepository, create_handler: CreatePostCommandHandler):
        bad_command: str = 'Bad Bad Command'

        with pytest.raises(InvalidCommandTypeException):
            await create_handler.handle(command=bad_command)
            


class TestDeletePostCommandHandler:
    @pytest.mark.asyncio
    async def test_delete_post_success(self, post_repo: PostMemoryRepository, delete_handler: DeletePostCommandHandler):
        posts: list[Post] = await post_repo.get()
        command: DeletePostCommand = DeletePostCommand(
            post_id=posts[0].id
        )
        await delete_handler.handle(command=command)
        assert len(await post_repo.get()) == 1
    
    @pytest.mark.asyncio
    async def test_delete_post_invalid_command(self):
        with pytest.raises(TypeError):
            DeletePostCommand()

    @pytest.mark.asyncio
    async def test_delete_success2(self, post_repo: PostMemoryRepository, delete_handler: DeletePostCommandHandler):
        posts: list[Post] = await post_repo.get()
        command: DeletePostCommand = DeletePostCommand(
            post_id=posts[0].id
        )
        await delete_handler.handle(command=command)
        assert len(await post_repo.get()) == 0

    @pytest.mark.asyncio
    async def test_delete_post_command_invalid_command_failure(self, post_repo: PostMemoryRepository, delete_handler: DeletePostCommandHandler):
        bad_command: str = 'Bad Bad Command'

        with pytest.raises(InvalidCommandTypeException):
            await delete_handler.handle(command=bad_command)
