# Day 18 – Hirst Painting Generator 🎨

A Python project that recreates a Hirst-style dot painting by extracting colors from an image and rendering them on screen using the `turtle` module.

## Project structure

```
day-18/
├── main.py        # Entry point — draws the dot grid
├── painting.py    # Color extraction from image using colorgram
└── image.jpg      # Source image for color palette
```

## How it works

1. **`painting.py`** uses `colorgram` to extract the 10 most dominant colors from `image.jpg` and stores them as a list of RGB dictionaries.
2. **`main.py`** prompts the user for a step size and dot size, then uses `turtle` to draw a square grid of randomly colored dots, picking from the extracted palette.

## Requirements

Install dependencies with:

```bash
pip install colorgram.py
```

`turtle` is part of Python's standard library — no extra install needed.

## Usage

1. Place a `image.jpg` file in the project directory (this is the source for the color palette).
2. Run:

```bash
python main.py
```

3. Enter the **step size** (spacing between dots) and **dot size** (diameter of each dot) when prompted.
   - If `dot_size > step_size`, the dot size is automatically capped to the step size to avoid overlaps.
4. Click anywhere on the turtle window to close it.

## Parameters

| Parameter   | Description                                  | Suggested values |
|-------------|----------------------------------------------|------------------|
| `STEP_SIZE` | Distance between dot centers (pixels)        | 40–80            |
| `DOT_SIZE`  | Diameter of each dot (pixels)                | 10–30            |

## Example output

A grid of colored dots fills an 800×800 pixel canvas, with colors randomly sampled from the palette extracted from your source image — inspired by Damien Hirst's *Spot Paintings*.

## Notes

- The canvas spans from `(-400, -400)` to `(+400, +400)`, giving an 800×800 area.
- The number of dots per row/column is computed automatically based on `STEP_SIZE`.
- Colors are selected randomly on each run, so every execution produces a unique result.
