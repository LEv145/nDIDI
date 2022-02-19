import unittest
from unittest.mock import Mock

from src.ndidi.binding_commands import (
    BindingCommandMixin,
    BindingSlashCommand,
    BindingMessageCommand,
    BindingMessageCommandGroup,
)


# noinspection PyUnresolvedReferences
class TestBindingCommandMixin(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        command_class = type(
            "CommandClass",
            (),
            {
                "_callback": Mock(),
                "load_into_component": Mock(),
            },
        )
        self._mixed_command = type(
            "MixedBindingCommand",
            (BindingCommandMixin, command_class),
            {},
        )()

    def test_load_into_component(self) -> None:

        # Test `bonded`
        self.assertFalse(self._mixed_command._is_bonded)
        self._mixed_command.load_into_component(Mock())
        self.assertTrue(self._mixed_command._is_bonded)

        # TODO: Test super().load_into_component

    def test_is_bonded(self) -> None:
        # Test dependencies of `is_bonded` on `_is_bonded`
        self._mixed_command._is_bonded = False
        self.assertFalse(self._mixed_command.is_bonded)

        self._mixed_command._is_bonded = True
        self.assertTrue(self._mixed_command.is_bonded)


class TestBindingBindingSlashCommand(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self._command_class = BindingSlashCommand(Mock(), "test", "test")
        self._callback_mock: Mock = self._command_class._callback

    def test___init__(self):
        pass


class TestBindingMessageCommand(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self._command_class = BindingMessageCommand(Mock(), "test", "test")
        self._callback_mock: Mock = self._command_class._callback

    def test___init__(self):
        pass


class TestBindingMessageCommandGroup(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self._command_class = BindingMessageCommandGroup(Mock(), "test", "test")
        self._callback_mock: Mock = self._command_class._callback

    def test___init__(self):
        pass
