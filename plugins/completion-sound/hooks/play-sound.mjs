#!/usr/bin/env node
// Stop hook: play a completion sound when the assistant turn ends.
// Reads config.json next to this script to decide whether/what to play.

import { readFileSync } from 'fs';
import { join } from 'path';
import { execSync } from 'child_process';

const PLUGIN_ROOT = process.env.KIMI_PLUGIN_ROOT || process.cwd();
const CONFIG_PATH = join(PLUGIN_ROOT, 'config.json');

let config = { enabled: true, sound: 'ding' };
try {
  config = JSON.parse(readFileSync(CONFIG_PATH, 'utf8'));
} catch {
  // Config missing or malformed: fall back to defaults.
}

if (config.enabled !== true) {
  process.exit(0);
}

const sound = config.sound || 'ding';
const platform = process.platform;

function playOnWindows(sound) {
  let command;
  if (sound === 'beep') {
    command = '[System.Media.SystemSounds]::Beep.Play()';
  } else if (sound === 'ding' || sound === 'exclamation') {
    command = '[System.Media.SystemSounds]::Exclamation.Play()';
  } else if (sound === 'asterisk') {
    command = '[System.Media.SystemSounds]::Asterisk.Play()';
  } else if (sound === 'hand') {
    command = '[System.Media.SystemSounds]::Hand.Play()';
  } else if (sound === 'question') {
    command = '[System.Media.SystemSounds]::Question.Play()';
  } else {
    // Treat as a file path; SoundPlayer only supports .wav files.
    command = `(New-Object System.Media.SoundPlayer "${sound}").PlaySync()`;
  }
  try {
    execSync(
      `powershell -NoProfile -ExecutionPolicy Bypass -Command "${command}"`,
      { stdio: 'ignore', timeout: 5000 }
    );
  } catch {
    // Fail-open: don't block the assistant turn because of a sound error.
  }
}

function playOnMacOS(sound) {
  const file = sound === 'ding' || sound === 'beep'
    ? '/System/Library/Sounds/Glass.aiff'
    : sound;
  try {
    execSync(`afplay "${file}"`, { stdio: 'ignore', timeout: 5000 });
  } catch {}
}

function playOnLinux(sound) {
  const file = sound === 'ding' || sound === 'beep'
    ? '/usr/share/sounds/freedesktop/stereo/complete.oga'
    : sound;
  try {
    execSync(`paplay "${file}"`, { stdio: 'ignore', timeout: 5000 });
  } catch {
    try {
      execSync(`aplay "${file}"`, { stdio: 'ignore', timeout: 5000 });
    } catch {}
  }
}

if (platform === 'win32') {
  playOnWindows(sound);
} else if (platform === 'darwin') {
  playOnMacOS(sound);
} else {
  playOnLinux(sound);
}

process.exit(0);
