![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/maniac-en/maze_solver/pytest.yml?label=Build)

# Maniac's Maze Solver (mms)

Maze solving program built using python [tkinter](https://tkdocs.com/)

## What and why?

This program is built for educational purpose of visualizing the [Depth-first
search](https://en.wikipedia.org/wiki/Depth-first_search) algorithm using a
maze where-in the maze is built as well as solved both using the DFS!

## How to run

- Initialize your virtual environment
- This should setup and build a binary called `mms` in your path

```sh
pip install --editable .
```

- Now run `mms` to run the maze solver!

> By-default the maze size is 15 rows and 15 columns but you can also change it
> in command line argument as follows:

```
(venv) ~/w/maze_solver (main) $ mms --help
Usage: mms [OPTIONS]

  Welcome to Maniac's Maze solver

Options:
  --maze-size <INTEGER INTEGER>...
                                  row, column for the maze  [default: 15, 15]
  --help                          Show this message and exit.

(venv) ~/w/maze_solver (main) $ mms --maze-size 12, 19
```

## Demo Video
- Red path is overall solution and partial gray paths are backtracked paths.
- Video somehow doesn't load in firefox, works fine in chrome/chromium based!

https://github.com/maniac-en/maze_solver/assets/45049766/fa1422a5-7fb5-4bb7-91e5-e889afc7cb7f
