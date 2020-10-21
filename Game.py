import random
import arcade

# Constants
SPRITE_SCALING_PLAYER = 1
SPRITE_SCALING_COIN = 1
COIN_COUNT = 100

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "COIN COLLECT"

class Game(arcade.Window):
    """ Main Application Class """

    def __init__(self):
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Variables that will hold sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Set background color
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # setup game here

        # Create sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("venv/images/p1_stand.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50  # starting pos
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):
            # create the coin instance
            coin = arcade.Sprite("venv/images/coinGold.png", SPRITE_SCALING_COIN)

            # position each coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # add the coin to the lists
            self.coin_list.append(coin)

    def on_draw(self):
        """ Render the screen """
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()

        # Text on screen
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ All the logic to move, and game logic here """

        self.coin_list.update()

        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        for coin in coins_hit_list:
            coin.kill()
            self.score += 1

        if self.score == COIN_COUNT:
            arcade.close_window()





def main():
    game = Game()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()