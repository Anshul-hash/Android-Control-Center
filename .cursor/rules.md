# Android Control Center Coding Rules

## General

- Python 3.13
- Use PySide6
- Use type hints everywhere
- Follow PEP 8
- Use pathlib instead of os.path
- Prefer dataclasses where appropriate
- Keep functions under 40 lines when practical
- Keep classes focused on a single responsibility

## Architecture

Use a layered architecture:

UI
↓
Services
↓
Core
↓
Utilities

UI must never call ADB directly.

All ADB communication goes through the services layer.

## Imports

Prefer absolute imports.

## Logging

Never use print().

Always use logging.

## Documentation

Every public class and function must have a docstring.

## Error Handling

Never silently ignore exceptions.

Catch only expected exceptions.

## Git

One feature per commit.

Never commit broken code.