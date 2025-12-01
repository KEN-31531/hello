# Turtle Breakout Game

A classic brick-breaker game implemented using Python's turtle graphics library.

## Description

This is a fun implementation of the classic Breakout (Arkanoid-style) game using Python's built-in turtle graphics module. Break all the bricks by bouncing the ball with your paddle!

## Features

- **Classic Gameplay**: Paddle, ball, and bricks - just like the original
- **Colorful Bricks**: 5 rows of bricks in different colors
- **Score Tracking**: Earn points for each brick you break
- **Lives System**: Start with 3 lives
- **Keyboard Controls**: Use arrow keys or A/D to move the paddle
- **Responsive Paddle**: Ball angle changes based on where it hits the paddle

## How to Play

### Requirements
- Python 3.x (with tkinter support)

### Running the Game

```bash
python3 turtle_breakout.py
```

### Controls
- **Left Arrow** or **A**: Move paddle left
- **Right Arrow** or **D**: Move paddle right

### Rules
- Keep the ball from falling off the bottom of the screen
- Break all the bricks to win
- Each brick is worth 10 points
- You start with 3 lives
- The game ends when you run out of lives or break all bricks

## Game Screenshot

The game features:
- A blue paddle at the bottom that you control
- A red ball that bounces around
- Colorful bricks arranged in 5 rows (red, orange, yellow, green, blue)
- Score and lives display at the top
- Black background for that classic arcade feel

## Code Structure

The game is organized into several classes:
- `Paddle`: Handles paddle movement and position
- `Ball`: Manages ball movement and bouncing
- `Brick`: Represents individual bricks
- `Game`: Main game loop and collision detection

Enjoy the game!