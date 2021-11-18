import arcade


class Dragon(arcade.Sprite):

    def __init__(self, level_id, color_id):

        super().__init__()

        self.action = "initial"

        self.body_parts_textures = []
        # Head [0]
        head = arcade.Sprite
        self.body_parts_textures.append(
            arcade.load_texture(f"images/dragon_{color_id}.png", x=24, y=28, width=144, height=140))
        head.texture = self.body_parts_textures[0]

        # Neck [1]
        neckA = arcade.Sprite
        neckB = arcade.Sprite
        neckC = arcade.Sprite
        neckD = arcade.Sprite
        self.body_parts_textures.append(
            arcade.load_texture(f"images/dragon_{color_id}.png", x=216, y=56, width=144, height=86))
        neckA.texture = self.body_parts_textures[1]
        neckB.texture = self.body_parts_textures[1]
        neckC.texture = self.body_parts_textures[1]
        neckD.texture = self.body_parts_textures[1]

        # Body [2]
        body = arcade.Sprite
        self.body_parts_textures.append(
            arcade.load_texture(f"images/dragon_{color_id}.png", x=16, y=240, width=160, height=396))
        body.texture = self.body_parts_textures[2]

        # Wings [3]
        wings = arcade.Sprite
        self.body_parts_textures.append(
            arcade.load_texture(f"images/dragon_{color_id}.png", x=284, y=200, width=392, height=468))
        wings.texture = self.body_parts_textures[3]

        # Tail segment A [4]
        tailAa = arcade.Sprite
        tailAb = arcade.Sprite
        self.body_parts_textures.append(
            arcade.load_texture(f"images/dragon_{color_id}.png", x=420, y=60, width=120, height=76))
        tailAa.texture = self.body_parts_textures[4]
        tailAb.texture = self.body_parts_textures[4]

        # Tail segment B [5]
        tailBa = arcade.Sprite
        tailBb = arcade.Sprite
        self.body_parts_textures.append(
            arcade.load_texture(f"images/dragon_{color_id}.png", x=620, y=72, width=104, height=64))
        tailBa.texture = self.body_parts_textures[5]
        tailBb.texture = self.body_parts_textures[5]

        # Tail segment C [6]
        tailCa = arcade.Sprite
        tailCb = arcade.Sprite
        self.body_parts_textures.append(
            arcade.load_texture(f"images/dragon_{color_id}.png", x=836, y=72, width=60, height=56))
        tailCa.texture = self.body_parts_textures[6]
        tailCb.texture = self.body_parts_textures[6]

        # Tail segment D [7]
        tailDa = arcade.Sprite
        tailDb = arcade.Sprite
        self.body_parts_textures.append(
            arcade.load_texture(f"images/dragon_{color_id}.png", x=1032, y=72, width=52, height=48))
        tailDa.texture = self.body_parts_textures[7]
        tailDb.texture = self.body_parts_textures[7]

        # Tail Tip [8]
        tailtip = arcade.Sprite
        self.body_parts_textures.append(
            arcade.load_texture(f"images/dragon_{color_id}.png", x=1172, y=4, width=104, height=116))
        tailtip.texture = self.body_parts_textures[8]

    def update_animation(self, delta_time: float = 1 / 60):
        pass

    def perform_action(self, action):
        pass
