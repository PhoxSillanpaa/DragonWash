import arcade

# Constraints
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024
SCREEN_TITLE = "Dragon Wash"

# Constraints used to scale sprites from their original size
CHARACTER_SCALING = 4
PLAYER_MOVEMENT_SPEED = 15

RIGHT_FACING = 1
DOWN_FACING = 0
LEFT_FACING = 3
UP_FACING = 2

LAYER_NAME_PLAYER = "Player"
LAYER_NAME_ARENA = "Arena"
LAYER_NAME_WALL = "Wall"


class PC(arcade.Sprite):

    def __init__(self):

        super().__init__()

        # Define which direction the character is looking (Using integers 0-3.)
        self.character_face_direction = DOWN_FACING

        # Determines what appearance has been chosen.
        self.spriteID = 16

        # Are we cleaning a dragon?
        self.spraying = False

        # Handle the textures and build directional lists.
        self.scale = CHARACTER_SCALING
        self.current_texture = 0

        # --- Animation control ---
        # Idle animations. This loop loops through the top four sprites on the sprite sheet.
        self.idle_animation_list = []
        for x in range(4):
            self.idle_animation_list.append(
                arcade.load_texture(f"images/PC_{self.spriteID}.png", x=16 * x, y=0, width=16, height=17))

        # ToDo: This is fucked up. When we get new Sprite sheets, fix it.
        # Handles populating the list for walking left.
        self.walking_left_animation_list = []
        self.walking_left_animation_list.append(
            arcade.load_texture(f"images/PC_{self.spriteID}.png", x=48, y=0, width=16, height=17))
        self.walking_left_animation_list.append(
            arcade.load_texture(f"images/PC_{self.spriteID}.png", x=48, y=17, width=16, height=17))
        self.walking_left_animation_list.append(
            arcade.load_texture(f"images/PC_{self.spriteID}.png", x=48, y=0, width=16, height=17))
        self.walking_left_animation_list.append(
            arcade.load_texture(f"images/PC_{self.spriteID}.png", x=48, y=34, width=16, height=17))

        # ToDo: This is fucked up. When we get new Sprite sheets, fix it.
        # Handles populating the list for walking right.
        self.walking_right_animation_list = []
        self.walking_right_animation_list.append(
            arcade.load_texture(f"images/PC_{self.spriteID}.png", x=16, y=0, width=16, height=17))
        self.walking_right_animation_list.append(
            arcade.load_texture(f"images/PC_{self.spriteID}.png", x=16, y=17, width=16, height=17))
        self.walking_right_animation_list.append(
            arcade.load_texture(f"images/PC_{self.spriteID}.png", x=16, y=0, width=16, height=17))
        self.walking_right_animation_list.append(
            arcade.load_texture(f"images/PC_{self.spriteID}.png", x=16, y=34, width=16, height=17))

        # ToDo: This is fucked up. When we get new Sprite sheets, fix it.
        # Handles populating the list for walking up.
        self.walking_up_animation_list = []
        self.walking_up_animation_list.append(
            arcade.load_texture(f"images/PC_{self.spriteID}.png", x=32, y=0, width=16, height=17))
        self.walking_up_animation_list.append(
            arcade.load_texture(f"images/PC_{self.spriteID}.png", x=32, y=17, width=16, height=17))
        self.walking_up_animation_list.append(
            arcade.load_texture(f"images/PC_{self.spriteID}.png", x=32, y=0, width=16, height=17))
        self.walking_up_animation_list.append(
            arcade.load_texture(f"images/PC_{self.spriteID}.png", x=32, y=34, width=16, height=17))

        # ToDo: This is fucked up. When we get new Sprite sheets, fix it.
        # Handles populating the list for walking down.
        self.walking_down_animation_list = []
        self.walking_down_animation_list.append(
            arcade.load_texture(f"images/PC_{self.spriteID}.png", x=0, y=0, width=16, height=17))
        self.walking_down_animation_list.append(
            arcade.load_texture(f"images/PC_{self.spriteID}.png", x=0, y=17, width=16, height=17))
        self.walking_down_animation_list.append(
            arcade.load_texture(f"images/PC_{self.spriteID}.png", x=0, y=0, width=16, height=17))
        self.walking_down_animation_list.append(
            arcade.load_texture(f"images/PC_{self.spriteID}.png", x=0, y=34, width=16, height=17))

        # Default sprite when game loads in.
        self.texture = self.idle_animation_list[0]

        self.set_hit_box = [[-6, 7], [6, 7], [-6, -6], [6, -6]]

    def update_animation(self, delta_time: float = 1 / 60):

        # Figure out if we need to flip change sprites.
        if self.change_x > 0 and self.character_face_direction != RIGHT_FACING:
            self.character_face_direction = RIGHT_FACING
        elif self.change_x < 0 and self.character_face_direction != LEFT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_y < 0 and self.character_face_direction != DOWN_FACING:
            self.character_face_direction = DOWN_FACING
        elif self.change_y > 0 and self.character_face_direction != UP_FACING:
            self.character_face_direction = UP_FACING

        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_animation_list[self.character_face_direction]

        self.current_texture += 1
        if self.current_texture > 3:
            self.current_texture = 0

        if self.change_x != 0:
            if self.character_face_direction == RIGHT_FACING:
                self.texture = self.walking_right_animation_list[self.current_texture]
            elif self.character_face_direction == LEFT_FACING:
                self.texture = self.walking_left_animation_list[self.current_texture]

        if self.change_y != 0:
            if self.character_face_direction == UP_FACING:
                self.texture = self.walking_up_animation_list[self.current_texture]
            elif self.character_face_direction == DOWN_FACING:
                self.texture = self.walking_down_animation_list[self.current_texture]


class Arena(arcade.Sprite):

    def __init__(self):

        super().__init__()

        # Make the list that will populate the textures on the very base of the arena
        self.arena_ground_base_textures = []
        for row in range(3):
            for col in range(3):
                self.arena_ground_base_textures.append(
                    arcade.load_texture("images/tiles.png", x=64 * row, y=64 * col, width=64, height=64))

        self.texture = self.arena_ground_base_textures[2]


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        # Call the parent class and set up the game window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Powers Movement
        self.physics_engine = None

        # Buttons State
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.water_pressed = False

        # These are 'lists' that keep track of sprite. Each sprite goes into a list
        self.arena_list = None

        self.scene = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        arcade.set_background_color(arcade.csscolor.LAWNGREEN)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        # Create the Sprite lists
        self.arena_list = arcade.SpriteList()

        self.scene = arcade.Scene()
        self.player = PC()
        self.wall = arcade.Sprite()

        # Set up the player at these coordinates
        self.player.center_x = SCREEN_WIDTH // 4
        self.player.center_y = SCREEN_HEIGHT // 4
        self.scene.add_sprite(LAYER_NAME_PLAYER, self.player)
        self.scene.add_sprite(LAYER_NAME_WALL, self.wall)
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player,
            walls=self.scene[LAYER_NAME_WALL]
        )
        for ypos in range(16):
            for xpos in range(16):
                if ypos == 0 and xpos == 0:
                    self.arena = Arena()
                    self.arena.position = [32, 992]
                    self.arena.texture = self.arena.arena_ground_base_textures[0]
                    self.arena_list.append(self.arena)
                else:
                    self.arena = Arena()
                    self.arena.position = [992, 32]
                    self.arena.texture = self.arena.arena_ground_base_textures[8]
                    self.arena_list.append(self.arena)

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.arena_list.draw()
        self.scene.draw()

    def process_keychange(self):

        # Process up/down
        if self.up_pressed and not self.down_pressed:
            self.player.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player.change_y = -PLAYER_MOVEMENT_SPEED
        else:
            self.player.change_y = 0

        # Process left/right
        if self.right_pressed and not self.left_pressed:
            self.player.change_x = PLAYER_MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self.player.change_x = -PLAYER_MOVEMENT_SPEED
        else:
            self.player.change_x = 0

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

        self.process_keychange()

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

        self.process_keychange()

    def on_update(self, delta_time):
        """Movement and game logic"""
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
