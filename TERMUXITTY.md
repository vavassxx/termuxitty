# Termuxitty

Termuxitty keeps Termux's Android session/runtime model while building its own frontend experience.

## Current fork feature

The session drawer now exposes a small Termuxitty dashboard:

- current session PID and working directory;
- number of active terminal sessions;
- **Run command** action for sending a command directly to the focused shell.

The command action deliberately writes to the existing `TerminalSession`, so it does not create a second shell or bypass Termux's session lifecycle.
