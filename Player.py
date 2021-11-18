import arcade

CHARACTER_SCALING = 4

RIGHT_FACING = 1
DOWN_FACING = 0
LEFT_FACING = 3
UP_FACING = 2


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

        # Default sprite when game loads in.w
        self.texture = self.idle_animation_list[0]

        self.set_hit_box([[-3, -5], [3, -5], [3, -10], [-3, -10]])

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

        print(f"{self.current_texture}")
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
