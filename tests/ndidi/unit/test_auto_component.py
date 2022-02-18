import unittest
from unittest.mock import Mock

from src.ndidi.auto_component import AutoComponent
from src.ndidi.components import (
    BindingMessageCommandGroup,
    BindingSlashCommand,
    BindingMessageCommand,
)


class TestAutoComponent(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self._auto_component = AutoComponent()

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
            (AutoComponent,),
            {
                "test_slash_command": test_slash_command,
                "test_message_command": test_message_command,
                "test_message_command_group": test_message_command_group,
            }
        )().load_commands()

        test_slash_command.load_into_component.assert_called()
        test_message_command.load_into_component.assert_called()
        test_message_command_group.load_into_component.assert_called()
