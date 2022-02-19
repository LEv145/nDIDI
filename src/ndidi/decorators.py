from __future__ import annotations

import typing

import tanjun

from .binding_commands import (
    BindingSlashCommand,
    BindingMessageCommand,
    BindingMessageCommandGroup,
)


CallbackType = typing.Callable[..., typing.Awaitable[None]]
ABCCommandsType = typing.Union[
    tanjun.abc.MenuCommand[CallbackType, typing.Any],
    tanjun.abc.MessageCommand[CallbackType],
    tanjun.abc.SlashCommand[CallbackType],
]
DecoratorCallbackType = typing.Union[ABCCommandsType, CallbackType]


ABCCommandsClasses = (
    tanjun.abc.MenuCommand,
    tanjun.abc.MessageCommand,
    tanjun.abc.SlashCommand,
)


def as_binding_slash_command(
    name: str,
    description: str,
    *,
    always_defer: bool = False,
    default_permission: bool = True,
    default_to_ephemeral: typing.Optional[bool] = None,
    is_global: bool = True,
    sort_options: bool = True,
    **kwargs: typing.Any,
) -> typing.Callable[[DecoratorCallbackType], BindingSlashCommand[CallbackType]]:
    def decorator(callback: DecoratorCallbackType):
        if isinstance(callback, ABCCommandsClasses):
            return BindingSlashCommand(
                callback.callback,
                name,
                description,
                always_defer=always_defer,
                default_permission=default_permission,
                default_to_ephemeral=default_to_ephemeral,
                is_global=is_global,
                sort_options=sort_options,
                _wrapped_command=callback,
                **kwargs,
            )

        return BindingSlashCommand(
            callback,
            name,
            description,
            always_defer=always_defer,
            default_permission=default_permission,
            default_to_ephemeral=default_to_ephemeral,
            is_global=is_global,
            sort_options=sort_options,
            **kwargs,
        )

    return decorator


def as_binding_message_command(
    name: str,
    *names: str,
    **kwargs: typing.Any,
) -> typing.Callable[[DecoratorCallbackType], BindingMessageCommand[CallbackType]]:
    def decorator(callback: DecoratorCallbackType):
        if isinstance(callback, ABCCommandsClasses):
            return BindingMessageCommand(
                callback.callback,
                name,
                *names,
                _wrapped_command=callback,
            )

        return BindingMessageCommand(callback, name, *names, **kwargs)

    return decorator


def as_binding_message_command_group(
    name: str,
    *names: str,
    strict: bool = False,
    **kwargs: typing.Any,
) -> typing.Callable[[DecoratorCallbackType], BindingMessageCommandGroup[CallbackType]]:
    def decorator(callback: DecoratorCallbackType):
        if isinstance(callback, ABCCommandsClasses):
            return BindingMessageCommandGroup(
                callback.callback,
                name,
                *names,
                strict=strict,
                _wrapped_command=callback,
            )

        return BindingMessageCommandGroup(
            callback,
            name,
            *names,
            strict=strict,
            **kwargs,
        )

    return decorator
