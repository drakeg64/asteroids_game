# Asteroids Game

A classic Asteroids arcade game implemented in Python using Pygame.

## Overview

This is a Python implementation of the classic Asteroids arcade game. Players control a spaceship and must destroy incoming asteroids while avoiding collisions. The game features collision detection, asteroid physics, and progressive difficulty.

## Project Structure

- **main.py** - Entry point for the game; initializes and runs the game loop
- **player.py** - Player spaceship class with movement and shooting mechanics
- **asteroid.py** - Individual asteroid class with rotation and movement
- **asteroidfield.py** - Manages the spawning and tracking of asteroids
- **circleshape.py** - Base class for circular game objects (collision detection)
- **constants.py** - Game configuration constants (screen size, speeds, etc.)
- **logger.py** - Logging utilities for debugging and game events

## Requirements

- Python 3.x (see `.python-version` for specific version)
- Pygame
- Project uses `uv` for dependency management

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/drakeg64/asteroids_game.git
   cd asteroids_game
   ```

2. Install dependencies using `uv`:
   ```bash
   uv sync
   ```

   Or using pip:
   ```bash
   pip install pygame
   ```

## Running the Game

Start the game by running:
```bash
python main.py
```

## Gameplay

- **Controls**: Use WASD keys to rotate and move your spaceship, F to use warpdrive
- **Shooting**: Press spacebar to shoot asteroids
- **Objective**: Destroy all asteroids without colliding with them
- **Difficulty**: Each progressing wave has an extra asteroid from the last. Asteroids break into smaller pieces when destroyed. Every five waves has a boss asteroid that gets bigger each boss wave.

## Game Mechanics

### Player
- Rotation and forward movement
- Can shoot projectiles
- Collision detection with asteroids

### Asteroids
- Spawn randomly on screen
- Rotate and move across the screen
- Break into smaller asteroids when hit
- Eventually disappear when destroyed

### Collision Detection
- Uses circular collision detection (implemented in `circleshape.py`)
- Player loses a life if hit by an asteroid
- Asteroids destroyed when hit by projectiles

## Configuration

Game constants can be modified in `constants.py`:
- Screen dimensions
- Player speed and rotation speed
- Asteroid speed
- Other gameplay parameters

## Development

This project uses:
- **Python 3.x** - Programming language
- **Pygame** - Graphics and game loop library
- **uv** - Fast Python package manager
- **.python-version** - Specifies the Python version
- **.gitignore** - Excludes build artifacts and cache files

## Future Enhancements

Potential improvements for future versions:
- Score tracking and high scores
- Sound effects and background music
- Different difficulty levels
- Power-ups and special weapons
- Enemy ships
- ~~Particle effects~~

## License

This project is open source. Feel free to use, modify, and distribute as needed.

## Author

drakeg64

---

Have fun playing! 🚀
