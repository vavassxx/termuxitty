# Termuxitty Android package

Termuxitty uses the Android application id `com.ttymux`, so it can be installed alongside the original `com.termux` app without replacing it.

The Java source namespace remains `com.termux` for now. Android component names are explicit where needed, while the runtime package identity and Termux `$PREFIX` use `com.ttymux`.

## Bootstrap

Termux bootstrap binaries contain `/data/data/com.termux/...` paths. The Android application id was deliberately chosen to have the same byte length as `com.termux`. During the Gradle bootstrap download step, `scripts/patch-bootstrap-package.py` rewrites those embedded package strings to `com.ttymux`.

This keeps the existing upstream bootstrap artifacts usable without making the original Termux installation or its `$PREFIX` part of the fork.
