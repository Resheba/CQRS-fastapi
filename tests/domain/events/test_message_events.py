import pytest
from uuid import UUID

from src.domain.entities.message import Message, MessageText
from src.domain.events.message import MessageSent


class TestMessageSentEvent:
    def test_message_sent_success(self):
        message = Message(message=MessageText("hello"), user=UUID(int=1))
        event = MessageSent(message=message)
        assert event.message.message.as_generic() == "hello"
        assert event.message.user == UUID(int=1)

    def test_message_sent_invalid_message_failure(self):
        with pytest.raises(TypeError):
            MessageSent()
