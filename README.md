# Animated Kaleidoscope

A browser-based kaleidoscope with an animation written in Python and rendered
on an HTML canvas using PyScript.

## Run locally

From this directory, start Python's built-in web server:

```powershell
python -m http.server 8000
```

Then open <http://localhost:8000> in a modern browser. The page loads PyScript
from its CDN, so an internet connection is needed the first time it runs.

## Files

- `main.py` draws and animates the kaleidoscope.
- `index.html` loads the page and PyScript.
- `style.css` styles the page.
