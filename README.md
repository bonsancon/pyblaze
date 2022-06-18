# PyBlaze

<a href="https://pypi.org/project/bonsancon-pyblaze/">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/bonsancon-pyblaze.svg">
</a>

Python package to access Blaze API resources.

```bash
pip install bonsancon-pyblaze
```

**Games available**:

- [Crash][game-crash]
- [Double][game-double]

## How to use

```python
from pyblaze import BlazeClient

client = BlazeClient()
client.version()  # Version(version='2.159.0')
```

If you want to get data from specific game, you can:

```python
from pyblaze.games import Crash

client = Crash()
client.current()  # CurrentResponse(crash_point=None, total_eur_bet=5454.341490738392, ...)
```

## Clients and methods

The package have 3 clients:

| Client        | Description          | `import`                           |
|---------------|----------------------|------------------------------------|
| `BlazeClient` | Blaze API Client.    | `from pyblaze import BlazeClient`  |
| `Crash`       | Blaze Crash Client.  | `from pyblaze.games import Crash`  |
| `Double`      | Blaze Double Client. | `from pyblaze.games import Double` |

### BlazeClient

| Method         | Description                    | Example                 |
|----------------|--------------------------------|-------------------------|
| `announcement` | Get current announcement.      | `client.announcement()` |
| `chat_rooms`   | Get chat rooms config.         | `client.chat_rooms()`   |
| `chat_room`    | Get messages from a chat room. | `client.chat_room(2)`   |
| `country`      | Get country config.            | `client.country()`      |
| `currencies`   | Get currencies config.         | `client.currencies()`   |
| `settings`     | Get Blaze platform settings.   | `client.settings()`     |
| `time`         | Get time (for what?).          | `client.time()`         |
| `version`      | Get Blaze platform version.    | `client.version()`      |

### Games

| Method    | Description          | Example            |
|-----------|----------------------|--------------------|
| `recents` | Get recents results. | `client.recents()` |
| `current` | Get current game.    | `client.game()`    |

## Contributing

Contributions are more than welcome. Fork, improve and make a pull request.
For bugs, ideas for improvement or other, please create an [issue][issues].

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

[game-crash]: https://blaze.com/pt/games/crash
[game-double]: https://blaze.com/pt/games/double
[issues]: https://github.com/bonsancon/pyblaze/issues
