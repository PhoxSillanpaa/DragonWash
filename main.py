import arcade

import Player
import Dragon

# Constraints
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024
SCREEN_TITLE = "Dragon Wash"

# Constraints used to scale sprites from their original size

PLAYER_MOVEMENT_SPEED = 10

LAYER_NAME_PLAYER = "Player"
LAYER_NAME_DRAGON = "Dragon"
LAYER_NAME_BASE_OBJECTS = "BASE_OBJECTS"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        # Call the parent class and set up the game window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.tile_map = None

        # Powers Movement
        self.physics_engine = None

        self.dragon = Dragon.Dragon(1, 1)
        self.player = Player.PC()

        # Buttons State
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.water_pressed = False

        self.scene = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        arcade.set_background_color(arcade.csscolor.LAWNGREEN)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        map_name = "images/arena.json"

        layer_options = {
            "LAYER_NAME_DRAGON": {
            },
            "LAYER_NAME_PLAYER": {
            },
            "LAYER_NAME_BASE_OBJECTS": {
                "use>spatial_hash": False
            }
        }

        self.tile_map = arcade.load_tilemap(map_name, 1, layer_options)

        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # Set up the player at these coordinates
        self.player.center_x = SCREEN_WIDTH // 4
        self.player.center_y = SCREEN_HEIGHT // 4
        self.scene.add_sprite(LAYER_NAME_PLAYER, self.player)
        self.scene.add_sprite(LAYER_NAME_DRAGON, self.dragon)
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player,
            walls=self.scene[LAYER_NAME_BASE_OBJECTS],
        )

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.scene.draw(pixelated=True)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False

    def on_update(self, delta_time):

        self.player.change_x = 0
        self.player.change_y = 0

        if self.player.left < 6:
            self.player.left = 6
        elif self.player.right > SCREEN_WIDTH - 6:
            self.player.right = SCREEN_WIDTH - 6

        if self.player.bottom < 0:
            self.player.bottom = 0
        elif self.player.top > SCREEN_HEIGHT - 6:
            self.player.top = SCREEN_HEIGHT - 6

        if self.up_pressed and not self.down_pressed:
            self.player.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player.change_y = -PLAYER_MOVEMENT_SPEED

            # Process left/right
        if self.right_pressed and not self.left_pressed:
            self.player.change_x = PLAYER_MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self.player.change_x = -PLAYER_MOVEMENT_SPEED

        self.physics_engine.update()

        # Update Animations

        self.scene.update_animation(
            delta_time, [LAYER_NAME_PLAYER]
        )


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
