import unittest
from unittest.mock import Mock

from src.ndidi.base_component import BaseComponent
from src.ndidi.binding_commands import (
    BindingMessageCommandGroup,
    BindingSlashCommand,
    BindingMessageCommand,
)


class TestAutoComponent(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self._auto_component = BaseComponent()

    def test_load_commands(self):
        # Test with `cls`
        test_slash_command = Mock(BindingSlashCommand)
        test_message_command = Mock(BindingMessageCommand)
        test_message_command_group = Mock(BindingMessageCommandGroup)

        self._auto_component.load_commands(
            type(
                "TestComponent",
                (),
                {
                    "test_slash_command": test_slash_command,
                    "test_message_command": test_message_command,
                    "test_message_command_group": test_message_command_group,
                }
            )
        )
        test_slash_command.load_into_component.assert_called()
        test_message_command.load_into_component.assert_called()
        test_message_command_group.load_into_component.assert_called()

        # Test with object self
        test_slash_command = Mock(BindingSlashCommand)
        test_message_command = Mock(BindingMessageCommand)
        test_message_command_group = Mock(BindingMessageCommandGroup)

        type(
            "TestComponent",
            (BaseComponent,),
            {
                "test_slash_command": test_slash_command,
                "test_message_command": test_message_command,
                "test_message_command_group": test_message_command_group,
            }
        )().load_commands()

        test_slash_command.load_into_component.assert_called()
        test_message_command.load_into_component.assert_called()
        test_message_command_group.load_into_component.assert_called()
