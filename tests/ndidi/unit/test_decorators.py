import unittest
from unittest.mock import Mock

import hikari
import tanjun

from src.ndidi.decorators import (
    as_binding_slash_command,
    as_binding_message_command,
    as_binding_message_command_group,
    ABCCommandsClasses,
)
from src.ndidi.binding_commands import (
    BindingSlashCommand,
    BindingMessageCommand,
    BindingMessageCommandGroup,
)


class TestDecorators(unittest.TestCase):
    def test_as_binding_slash_command(self) -> None:
        # Test normal
        mock_callback = Mock()
        command = as_binding_slash_command(
            "test_name",
            "test_description",
            always_defer=True,
            default_permission=False,
            default_to_ephemeral=True,
            is_global=False,
            sort_options=False,
        )(mock_callback)

        self.assertIsInstance(command, BindingSlashCommand)

        self.assertEqual(command.callback, mock_callback)
        self.assertIsNone(command._wrapped_command)

        self.assertTrue(command._always_defer)
        self.assertEqual(command.name, "test_name")
        self.assertEqual(command.description, "test_description")
        self.assertEqual(command.build().default_permission, hikari.UNDEFINED)
        self.assertTrue(command.defaults_to_ephemeral)
        self.assertFalse(command.is_global)
        self.assertFalse(command._builder._sort_options)

        # Test with abc command classes
        for abc_command_class in ABCCommandsClasses:
            abc_command_class_mock = Mock(spec=abc_command_class)

            command = as_binding_slash_command(
                "test_name",
                "test_description",
                always_defer=True,
                default_permission=False,
                default_to_ephemeral=True,
                is_global=False,
                sort_options=False,
            )(abc_command_class_mock)

            self.assertIsInstance(command, BindingSlashCommand)

            self.assertEqual(command.callback, abc_command_class_mock.callback)
            self.assertEqual(command._wrapped_command, abc_command_class_mock)

            self.assertTrue(command._always_defer)
            self.assertEqual(command.name, "test_name")
            self.assertEqual(command.description, "test_description")
            self.assertEqual(command.build().default_permission, hikari.UNDEFINED)
            self.assertTrue(command.defaults_to_ephemeral)
            self.assertFalse(command.is_global)
            self.assertFalse(command._builder._sort_options)
            self.assertIsInstance(command, tanjun.SlashCommand)

    def test_as_binding_message_command(self) -> None:
        # Test normal
        mock_callback = Mock()
        command = as_binding_message_command(
            "test_name1",
            "test_name2",
        )(mock_callback)

        self.assertIsInstance(command, BindingMessageCommand)

        self.assertEqual(command.callback, mock_callback)
        self.assertIsNone(command._wrapped_command)

        self.assertEqual(command.names, ["test_name1", "test_name2"])

        # Test with abc command classes
        for abc_command_class in ABCCommandsClasses:
            abc_command_class_mock = Mock(spec=abc_command_class)

            command = as_binding_message_command(
                "test_name1",
                "test_name2",
            )(abc_command_class_mock)

            self.assertIsInstance(command, BindingMessageCommand)

            self.assertEqual(command.callback, abc_command_class_mock.callback)
            self.assertEqual(command._wrapped_command, abc_command_class_mock)

            self.assertEqual(command.names, ["test_name1", "test_name2"])

    def test_as_message_command_group(self) -> None:
        # Test normal
        mock_callback = Mock()
        command = as_binding_message_command_group(
            "test_name1",
            "test_name2",
            strict=True,
        )(mock_callback)

        self.assertIsInstance(command, BindingMessageCommandGroup)
        self.assertIsNone(command._wrapped_command)

        self.assertEqual(command.callback, mock_callback)

        self.assertEqual(command.names, ["test_name1", "test_name2"])
        self.assertTrue(command.is_strict)

        # Test with abc command classes
        for abc_command_class in ABCCommandsClasses:
            abc_command_class_mock = Mock(spec=abc_command_class)

            command = as_binding_message_command_group(
                "test_name1",
                "test_name2",
                strict=True,
            )(abc_command_class_mock)

            self.assertIsInstance(command, BindingMessageCommandGroup)

            self.assertEqual(command.callback, abc_command_class_mock.callback)
            self.assertEqual(command._wrapped_command, abc_command_class_mock)

            self.assertEqual(command.names, ["test_name1", "test_name2"])
            self.assertTrue(command.is_strict)
