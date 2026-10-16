# apkpythonpi

A Python app for learning programming basics — Python, PHP, HTML, CSS and JavaScript — packaged as an Android APK with [Buildozer](https://buildozer.readthedocs.io/).

## About

The project walks through core concepts with examples and screenshots:

- **Python** — syntax, data types, variables, strings, numbers, loops, operators
- **HTML** — headings, paragraphs, lists, links, semantic markup, forms
- **CSS** — syntax, box model, display, flexbox, grid, backgrounds, borders, text styling
- **JavaScript** — variables, constants, loops, conditional statements, joining
- **PHP** — syntax, variables, loops, conditionals, operators
- **Databases** — basic query examples

## Requirements

- Python 3
- [Buildozer](https://buildozer.readthedocs.io/) and the Android SDK/NDK (to build the APK)

```bash
pip install buildozer
buildozer init   # if you don't have a buildozer.spec yet
buildozer -v android debug
```

The APK is written to `bin/`.

## Running on desktop

```bash
python main.py
```

## Project layout

- `main.py` — application entry point
- `buildozer.spec` — Buildozer/Android build configuration
- `*.png`, `*.jpg` — lesson illustrations and screenshots
- `bin/` — build output
- `.buildozer/` — Buildozer cache (not committed)

## License

See the repository owner for license details.
