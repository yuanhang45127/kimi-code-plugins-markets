# Completion Sound Plugin for Kimi Code

Plays a configurable sound when the assistant finishes a response.

## How it works

The plugin registers a `Stop` lifecycle hook. Every time the model is about to end its turn, Kimi Code runs `hooks/play-sound.mjs`, which reads `config.json` and plays the configured sound if enabled.

## Installation

From the Kimi Code TUI in this project's directory:

```
/plugins install ./completion-sound
/reload
```

Or install once and then reload:

```bash
kimi plugins install ./completion-sound
```

Then start a new session or run `/reload`.

## Configuration

Edit `config.json` in the installed plugin directory (`~/.kimi-code/plugins/managed/completion-sound/config.json`):

```json
{
  "enabled": true,
  "sound": "ding"
}
```

- `enabled`: `true` or `false`
- `sound`: a built-in preset (`ding`, `beep`, `asterisk`, `hand`, `question`) or an absolute path to a `.wav` file

### Disable the sound

```json
{
  "enabled": false,
  "sound": "ding"
}
```

### Use a custom WAV file

```json
{
  "enabled": true,
  "sound": "C:/Users/me/sounds/finished.wav"
}
```

## Notes

- The hook is fail-open: if the sound fails to play for any reason, the assistant turn still completes normally.
- On Windows, custom sounds must be `.wav` files (the script uses `System.Media.SoundPlayer`).
