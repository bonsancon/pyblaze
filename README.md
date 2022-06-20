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

| Method                   | Description                    |
|--------------------------|--------------------------------|
| `announcement()`         | Get current announcement.      |
| `chat_rooms()`           | Get chat rooms config.         |
| `chat_room(chat_number)` | Get messages from a chat room. |
| `country()`              | Get country config.            |
| `currencies()`           | Get currencies config.         |
| `settings()`             | Get Blaze platform settings.   |
| `time()`                 | Get time (for what?).          |
| `version()`              | Get Blaze platform version.    |

### Games

| Method                                                      | Description                               |
|-------------------------------------------------------------|-------------------------------------------|
| `current()`                                                 | Get current game.                         |
| `get_game_by_id(id)`                                        | Get game data by id.                      |
| `get_previous_game_hash_by_hash(hash_code)`                 | Get previous game hash by the given hash. |
| `get_previous_games_to_hash_by_hash(hash_code, hash_match)` | Get previous games to hash.               |
| `get_previous_n_games_by_hash(hash_code, number_of_games)`  | Get previous N games by the given hash.   |
| `get_result_by_hash(game_hash)`                             | Get result by the given hash.             |
| `recent()`                                                  | Get recent results.                       |
| `recent_history()`                                          | Get recent results.                       |

**TO DO**: fix Double methods to previous games.

## Contributing

Contributions are more than welcome. Fork, improve and make a pull request.
For bugs, ideas for improvement or other, please create an [issue][issues].

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

[game-crash]: https://blaze.com/pt/games/crash
[game-double]: https://blaze.com/pt/games/double
[issues]: https://github.com/bonsancon/pyblaze/issues
