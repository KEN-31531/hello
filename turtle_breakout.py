#!/usr/bin/env python3
"""
Turtle Breakout Game
A classic brick-breaker game implemented using Python's turtle graphics library.
"""

import turtle
import time

# Game configuration
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
BALL_SIZE = 20
BRICK_WIDTH = 75
BRICK_HEIGHT = 20
BRICK_ROWS = 5
BRICK_COLS = 10
BRICK_PADDING = 5
BALL_SPEED = 3

class Paddle:
    def __init__(self):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("blue")
        self.paddle.shapesize(stretch_wid=PADDLE_HEIGHT/20, stretch_len=PADDLE_WIDTH/20)
        self.paddle.penup()
        self.paddle.goto(0, -250)

    def move_left(self):
        x = self.paddle.xcor()
        if x > -SCREEN_WIDTH/2 + PADDLE_WIDTH/2:
            self.paddle.setx(x - 20)

    def move_right(self):
        x = self.paddle.xcor()
        if x < SCREEN_WIDTH/2 - PADDLE_WIDTH/2:
            self.paddle.setx(x + 20)

    def get_position(self):
        return self.paddle.xcor(), self.paddle.ycor()

class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color("red")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.dx = BALL_SPEED
        self.dy = -BALL_SPEED

    def move(self):
        self.ball.setx(self.ball.xcor() + self.dx)
        self.ball.sety(self.ball.ycor() + self.dy)

    def bounce_x(self):
        self.dx *= -1

    def bounce_y(self):
        self.dy *= -1

    def get_position(self):
        return self.ball.xcor(), self.ball.ycor()

    def reset(self):
        self.ball.goto(0, 0)
        self.dy = -abs(self.dy)  # Always start going down

class Brick:
    def __init__(self, x, y, color):
        self.brick = turtle.Turtle()
        self.brick.speed(0)
        self.brick.shape("square")
        self.brick.color(color)
        self.brick.shapesize(stretch_wid=BRICK_HEIGHT/20, stretch_len=BRICK_WIDTH/20)
        self.brick.penup()
        self.brick.goto(x, y)
        self.visible = True

    def hide(self):
        self.brick.hideturtle()
        self.visible = False

    def get_position(self):
        return self.brick.xcor(), self.brick.ycor()

class Game:
    def __init__(self):
        # Setup screen
        self.screen = turtle.Screen()
        self.screen.title("Turtle Breakout")
        self.screen.bgcolor("black")
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.tracer(0)

        # Create game objects
        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = []
        self.score = 0
        self.lives = 3

        # Create bricks
        self.create_bricks()

        # Score display
        self.score_display = turtle.Turtle()
        self.score_display.speed(0)
        self.score_display.color("white")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.goto(-350, 260)
        self.update_score()

        # Keyboard bindings
        self.screen.listen()
        self.screen.onkey(self.paddle.move_left, "Left")
        self.screen.onkey(self.paddle.move_right, "Right")
        self.screen.onkey(self.paddle.move_left, "a")
        self.screen.onkey(self.paddle.move_right, "d")

        self.game_running = True

    def create_bricks(self):
        colors = ["red", "orange", "yellow", "green", "blue"]
        start_x = -SCREEN_WIDTH/2 + (SCREEN_WIDTH - BRICK_COLS * (BRICK_WIDTH + BRICK_PADDING)) / 2 + BRICK_WIDTH/2
        start_y = SCREEN_HEIGHT/2 - 100

        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                x = start_x + col * (BRICK_WIDTH + BRICK_PADDING)
                y = start_y - row * (BRICK_HEIGHT + BRICK_PADDING)
                brick = Brick(x, y, colors[row % len(colors)])
                self.bricks.append(brick)

    def update_score(self):
        self.score_display.clear()
        self.score_display.write(f"Score: {self.score}  Lives: {self.lives}",
                                align="left", font=("Courier", 16, "bold"))

    def check_collision_with_paddle(self):
        ball_x, ball_y = self.ball.get_position()
        paddle_x, paddle_y = self.paddle.get_position()

        if (ball_y - BALL_SIZE/2 <= paddle_y + PADDLE_HEIGHT/2 and
            ball_y - BALL_SIZE/2 >= paddle_y - PADDLE_HEIGHT/2 and
            ball_x >= paddle_x - PADDLE_WIDTH/2 and
            ball_x <= paddle_x + PADDLE_WIDTH/2):
            return True
        return False

    def check_collision_with_brick(self, brick):
        if not brick.visible:
            return False

        ball_x, ball_y = self.ball.get_position()
        brick_x, brick_y = brick.get_position()

        if (ball_x + BALL_SIZE/2 >= brick_x - BRICK_WIDTH/2 and
            ball_x - BALL_SIZE/2 <= brick_x + BRICK_WIDTH/2 and
            ball_y + BALL_SIZE/2 >= brick_y - BRICK_HEIGHT/2 and
            ball_y - BALL_SIZE/2 <= brick_y + BRICK_HEIGHT/2):
            return True
        return False

    def check_win(self):
        return all(not brick.visible for brick in self.bricks)

    def show_game_over(self, won=False):
        message = turtle.Turtle()
        message.speed(0)
        message.color("white")
        message.penup()
        message.hideturtle()
        message.goto(0, 0)

        if won:
            text = "YOU WIN!"
        else:
            text = "GAME OVER"

        message.write(f"{text}\nFinal Score: {self.score}\n\nClose window to exit",
                     align="center", font=("Courier", 24, "bold"))

    def run(self):
        while self.game_running:
            self.screen.update()
            time.sleep(0.01)

            # Move ball
            self.ball.move()

            # Check wall collisions
            ball_x, ball_y = self.ball.get_position()

            # Side walls
            if ball_x >= SCREEN_WIDTH/2 - BALL_SIZE or ball_x <= -SCREEN_WIDTH/2 + BALL_SIZE:
                self.ball.bounce_x()

            # Top wall
            if ball_y >= SCREEN_HEIGHT/2 - BALL_SIZE:
                self.ball.bounce_y()

            # Bottom wall (lose a life)
            if ball_y <= -SCREEN_HEIGHT/2 + BALL_SIZE:
                self.lives -= 1
                self.update_score()

                if self.lives <= 0:
                    self.game_running = False
                    self.show_game_over(False)
                else:
                    self.ball.reset()
                    time.sleep(1)

            # Check paddle collision
            if self.check_collision_with_paddle():
                self.ball.bounce_y()
                # Add some english based on where the ball hits the paddle
                paddle_x, _ = self.paddle.get_position()
                offset = (ball_x - paddle_x) / (PADDLE_WIDTH / 2)
                self.ball.dx += offset * 0.5

            # Check brick collisions
            for brick in self.bricks:
                if self.check_collision_with_brick(brick):
                    brick.hide()
                    self.ball.bounce_y()
                    self.score += 10
                    self.update_score()

                    # Check win condition
                    if self.check_win():
                        self.game_running = False
                        self.show_game_over(True)
                    break

        # Keep window open
        self.screen.mainloop()

def main():
    """Main entry point for the game."""
    print("Starting Turtle Breakout Game...")
    print("Controls:")
    print("  Left Arrow or 'A' - Move paddle left")
    print("  Right Arrow or 'D' - Move paddle right")
    print("\nClose the window to exit the game.")

    game = Game()
    game.run()

if __name__ == "__main__":
    main()
