---
name: completion-sound
description: Use when the user wants to change the completion sound plugin settings
---

# Completion Sound

This plugin plays a sound when the assistant finishes a response (the `Stop` lifecycle event).

## Configuration

The plugin reads `config.json` in its root directory. The default location after installation is `~/.kimi-code/plugins/managed/completion-sound/config.json`.

```json
{
  "enabled": true,
  "sound": "ding"
}
```

- `enabled` (`boolean`): turn the completion sound on or off.
- `sound` (`string`): either a built-in preset or an absolute path to a `.wav` file.

### Built-in presets

| Preset | Windows behavior |
|--------|------------------|
| `ding` | `SystemSounds.Exclamation` |
| `beep` | `SystemSounds.Beep` |
| `asterisk` | `SystemSounds.Asterisk` |
| `hand` | `SystemSounds.Hand` |
| `question` | `SystemSounds.Question` |

### Custom sound

Set `sound` to an absolute path to a `.wav` file:

```json
{
  "enabled": true,
  "sound": "C:/Users/me/sounds/done.wav"
}
```

## How to change settings

When the user asks to enable, disable, or change the completion sound, locate the installed `config.json` and edit it directly. Confirm the new setting briefly.
