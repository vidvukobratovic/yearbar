# yearbar

A tiny terminal app to visualize how much of the year has passed.

Inspired by small, delightful CLI tools like `cbonsai`, `pipes.sh`, and `neofetch`.

---

## What it does

`yearbar` shows the progress of the current year using simple terminal-friendly visuals.
It is intentionally minimal, fast, and dependency-free.

Examples include:
- A classic progress bar
- A dot-based view
- A numerical stats view
- A minimalist “zen” mode

---

## Examples

### Default (bar)

```bash
2026
[██████████░░░░░░░░░░░░░░] 31.5%
Day 115 / 365
```

### Dots 

```
● ● ● ● ● ● ● ● ● ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○
```

### Stats 

```
Year       : 2026
Day        : 115
Days total : 365
Days left  : 250
Progress   : 31.51%
```


### Zen 

```
██████████░░░░░░░░░░░░░░░░
```


## Installation (local)
```
clone the repository and install in editable mode:
git clone git@github.com:vidvukobratovic/yearbar.git
cd yearbar
pip install -e .
```


## Usage
yearbar

## Flags
1. --dots : show progress using filled and hollow dots
2. --stats : show numberical statistics instead of visuals
3. --zen : minimal output with no labels
4. --h, --help : show help text 
