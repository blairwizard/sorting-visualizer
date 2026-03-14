# Sorting Visualizer

A real-time sorting algorithm visualizer built with Python and Pygame.

## Algorithms
- **Bubble Sort** - Simple comparison-based sorting. O(n²)
- **Merge Sort** - Divide and conquer sorting. O(n log n)
- **Quick Sort** - Partition-based sorting. O(n log n) average

## How to Use
- Click **Bubble Sort**, **Merge Sort**, or **Quick Sort** to select an algorithm
- Click **Start** to begin the visualization
- Click **Reset** to generate a new random array
- Click **Exit** or press **Q** to quit

## What You'll See
- 🟢 **Green bars** — unsorted elements
- 🔴 **Red bars** — elements currently being compared or swapped

## Setup

### Prerequisites
- Python 3.x
- Pygame

### Installation
```
pip install pygame
```

### Run
```
python visualizer.py
```

## Concepts Learned
- Generator functions and `yield` for step-by-step visualization
- Recursion with `yield from` for recursive algorithms
- Pygame event handling and real-time rendering
- Time complexity differences between O(n²) and O(n log n) algorithms

## Projects
This is part of a series of Python projects:
- [Snake Game](https://github.com/blairwizard/snake-pygame)
- Sorting Visualizer (this repo)
