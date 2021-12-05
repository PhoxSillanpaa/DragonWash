import arcade

CHARACTER_SCALING = 1

RIGHT_FACING = 2
DOWN_FACING = 0
LEFT_FACING = 1
UP_FACING = 3


class PC(arcade.Sprite):

    def __init__(self):

        super().__init__()

        # Define which direction the character is looking (Using integers 0-3.)
        self.character_face_direction = DOWN_FACING

        # Determines what appearance has been chosen.
        self.spriteID = 25

        # Are we cleaning a dragon?
        self.spraying = False

        # Handle the textures and build directional lists.
        self.scale = CHARACTER_SCALING
        self.current_texture = 0

        # --- Animation control ---
        # Idle animations. This loop loops through the top four sprites on the sprite sheet.
        self.idle_animation_list = []
        self.shooting_animation_list = []
        self.hurt_animation_list = []
        self.walking_left_animation_list = []
        self.walking_down_animation_list = []
        self.walking_right_animation_list = []
        self.walking_up_animation_list = []
        self.action = 0
        # Handles the idle sprites
        for x in range(4):
            self.idle_animation_list.append(
                arcade.load_texture(f"images/PC_{self.spriteID}.png", x=64 * x, y=0, width=64, height=64))

        # Handles populating the list for walking sprites.
        for row in range(4):
            for col in range(4):
                if row == 1:
                    self.walking_down_animation_list.append(
                        arcade.load_texture(f"images/PC_{self.spriteID}.png", x=0, y=col * 64, width=64, height=64))
                elif row == 2:
                    self.walking_left_animation_list.append(
                        arcade.load_texture(f"images/PC_{self.spriteID}.png", x=64, y=col * 64, width=64, height=64))
                elif row == 3:
                    self.walking_right_animation_list.append(
                        arcade.load_texture(f"images/PC_{self.spriteID}.png", x=128, y=col * 64, width=64, height=64))
                else:
                    self.walking_up_animation_list.append(
                        arcade.load_texture(f"images/PC_{self.spriteID}.png", x=192, y=col * 64, width=64, height=64))

        # Handles the shooting sprites.
        for x in range(4):
            self.shooting_animation_list.append(
                arcade.load_texture(f"images/PC_{self.spriteID}.png", x=64 * x, y=320, width=64, height=64))

        # Handles the hurt sprites.
        for x in range(4):
            self.hurt_animation_list.append(
                arcade.load_texture(f"images/PC_{self.spriteID}.png", x=64 * x, y=384, width=64, height=64))

        # Default sprite when game loads in.
        self.texture = self.idle_animation_list[0]

        self.set_hit_box([[-12, -20], [12, -20], [12, -40], [-12, -40]])

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

        if self.change_x == 0 and self.change_y == 0 and self.action == 0:
            self.texture = self.idle_animation_list[self.character_face_direction]
        elif self.action == 1:
            self.texture = self.shooting_animation_list[self.character_face_direction]

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
