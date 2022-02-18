import unittest
from unittest.mock import Mock

import tanjun

from src.ndidi.components import (
    BindingSlashCommand,
    BindingMessageCommand,
    BindingMessageCommandGroup,
)


class TestBindingSlashCommand(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self._command_class = BindingSlashCommand(Mock(), "test", "test")
        self._command_class_callback: Mock = self._command_class._callback

    def test_load_into_component(self):
        self._command_class.load_into_component(Mock())

        self.assertIsInstance(
            self._command_class._callback,
            tanjun.injecting.CallbackDescriptor,
        )


class TestBindingMessageCommand(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self._command_class = BindingMessageCommand(Mock(), "test", "test")
        self._command_class_callback: Mock = self._command_class._callback

    def test_load_into_component(self):
        self._command_class.load_into_component(Mock())

        self.assertIsInstance(
            self._command_class._callback,
            tanjun.injecting.CallbackDescriptor,
        )


class TestBindingMessageCommandGroup(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self._command_class = BindingMessageCommandGroup(Mock(), "test", "test")
        self._command_class_callback: Mock = self._command_class._callback

    def test_load_into_component(self):
        self._command_class.load_into_component(Mock())

        self.assertIsInstance(
            self._command_class._callback,
            tanjun.injecting.CallbackDescriptor,
        )

