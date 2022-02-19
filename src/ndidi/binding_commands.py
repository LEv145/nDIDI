from __future__ import annotations

import types
import typing

import tanjun


class CommandProtocol(typing.Protocol):
    _callback: tanjun.injecting.CallbackDescriptor

    def load_into_component(self, component: tanjun.abc.Component, /) -> None: ...


# noinspection PyUnresolvedReferences
class BindingCommandMixin():
    def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        self._is_bonded = False
        super().__init__(*args, **kwargs)

    def load_into_component(
        self: CommandProtocol | BindingCommandMixin,
        component: tanjun.abc.Component,
        _copy: bool = True,
    ) -> None:
        super().load_into_component(component)

        if self._is_bonded:
            return

        # Binding
        # noinspection PyAttributeOutsideInit
        self._callback = tanjun.injecting.CallbackDescriptor(
            types.MethodType(self._callback.callback, component),
        )
        self._is_bonded = True

    @property
    def is_bonded(self) -> bool:
        return self._is_bonded


class BindingMessageCommand(BindingCommandMixin, tanjun.MessageCommand):
    __slots__ = ()


class BindingMessageCommandGroup(BindingCommandMixin, tanjun.MessageCommandGroup):
    __slots__ = ()


class BindingSlashCommand(BindingCommandMixin, tanjun.SlashCommand):
    __slots__ = ()

