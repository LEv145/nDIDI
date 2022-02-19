# nDIDI (No Dynamic Import Dependency Injection)

## Install

```
pip install git+https://github.com/LEv145/nDIDI.git
```

## How to use

No hard:3
```py
...
from components import TestComponent


def main() -> None:
    ...
    client.add_component(TestComponent(name="Test", music_client=MusicClient()))
    ...


if __name__ == "__main__":
    main()
```
And now we provide complete independence of the client from the component!

## What are the advantages? OwO

* Easy to use
* Changing component properties from the main file (Component name and other)
* We have completely independent entities
Before loading the component, now you don't need to depend on the fact that we have implemented dependencies in the client
```py
>>> client(
...     .set_type_dependency(MusicClient, music_client)
...     .load_modules("components.music_component")
... )
MissingDependencyError: ... 
```

* Encapsulation of component 
The data is linked into a single object!
And inside the object, you can transmit any data

```py
class TestComponent(ndidi.BaseComponent):
    def __init__(self, client: ABCClient) -> None:
        self._client = client

    @ndidi.as_slash_command("work", "command")
    async def work(self, ctx: tanjun.abc.MessageContext) -> None:
        await ctx.respond(self._client.work())
```

* Inheritance
Gives you the opportunity to inherit from the component and make the command in your own way!
```py
class MyComponent(MyFriendComponent):
    @ndidi.as_slash_command("new_command", "new_command")
    def new_command(self, ...): ...
```

* The ability to make abstraction over components
```py
music_component: ABCMusicComponent = LavalinkMusicComponent(...)
client.add_component(music_component)
```

* And More!

## Links

* https://martinfowler.com/articles/injection.html
