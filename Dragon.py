import arcade


class Dragon:

    def clear(self):
        pass

    def __init__(self, level_id, color_id):

        super().__init__()

        self.action = "initial"
        self.body_sprites = arcade.SpriteList()
        self.body_parts_textures = []

        # Head [0]
        self.head = arcade.Sprite()
        self.body_parts_textures.append(
            arcade.load_texture(f"images/dragon_{color_id}.png", x=24, y=28, width=144, height=140))
        self.head.texture = self.body_parts_textures[0]
        self.head.hit_box_algorithm = "Simple"
        self.head.center_y = 128
        self.head.center_x = 512
        # Head center is 72, 70
        self.head_joint_rear = (self.head.center_x, self.head.center_y + 64)

        # Neck [1]
        self.neckA = arcade.Sprite()
        self.neckB = arcade.Sprite()
        self.neckC = arcade.Sprite()
        self.neckD = arcade.Sprite()

        self.body_parts_textures.append(
            arcade.load_texture(f"images/dragon_{color_id}.png", x=216, y=56, width=144, height=86))

        self.neckA.texture = self.body_parts_textures[1]

        self.neckA.center_x = self.head_joint_rear[0]
        self.neckA.center_y = self.head_joint_rear[1]
        self.neckA_joint_rear = (self.neckA.center_x, self.neckA.center_y + 60)

        self.neckB.texture = self.body_parts_textures[1]

        self.neckB.center_x = self.neckA_joint_rear[0]
        self.neckB.center_y = self.neckA_joint_rear[1]
        self.neckB_joint_rear = (self.neckB.center_x, self.neckB.center_y + 60)

        self.neckC.texture = self.body_parts_textures[1]

        self.neckC.center_x = self.neckB_joint_rear[0]
        self.neckC.center_y = self.neckB_joint_rear[1]
        self.neckC_joint_rear = (self.neckC.center_x, self.neckC.center_y + 60)

        self.neckD.texture = self.body_parts_textures[1]

        self.neckD.center_x = self.neckC_joint_rear[0]
        self.neckD.center_y = self.neckC_joint_rear[1]
        self.neckD_joint_rear = (self.neckD.center_x, self.neckD.center_y + 200)

        # Body [2]
        self.body = arcade.Sprite()

        self.body_parts_textures.append(
            arcade.load_texture(f"images/dragon_{color_id}.png", x=16, y=240, width=160, height=396))

        self.body.texture = self.body_parts_textures[2]

        self.body.center_x = self.neckD_joint_rear[0]
        self.body.center_y = self.neckD_joint_rear[1]
        self.body_joint_rear = (self.body.center_x, self.body.center_y + 206)

        # Wings [3]
        self.wings = arcade.Sprite()

        self.body_parts_textures.append(
            arcade.load_texture(f"images/dragon_{color_id}.png", x=284, y=200, width=392, height=468))

        self.wings.texture = self.body_parts_textures[3]

        self.wings.center_x = self.body.center_x
        self.wings.center_y = self.body.center_y

        # Tail segment A [4]
        self.tailAa = arcade.Sprite()

        self.body_parts_textures.append(
            arcade.load_texture(f"images/dragon_{color_id}.png", x=420, y=60, width=120, height=76))

        self.tailAa.texture = self.body_parts_textures[4]

        self.tailAa.center_x = self.body_joint_rear[0]
        self.tailAa.center_y = self.body_joint_rear[1]
        self.tailAa_joint_rear = (self.tailAa.center_x, self.tailAa.center_y + 38)

        self.tailAb = arcade.Sprite()

        self.tailAb.texture = self.body_parts_textures[4]

        self.tailAb.center_x = self.tailAa_joint_rear[0]
        self.tailAb.center_y = self.tailAa_joint_rear[1]
        self.tailAb_joint_rear = (self.tailAb.center_x, self.tailAb.center_y + 38)

        self.body_sprites.append(self.tailAb)

        # Tail segment B [5]
        self.tailBa = arcade.Sprite()

        self.body_parts_textures.append(
            arcade.load_texture(f"images/dragon_{color_id}.png", x=620, y=72, width=104, height=64))

        self.tailBa.texture = self.body_parts_textures[5]

        self.tailBa.center_x = self.tailAb_joint_rear[0]
        self.tailBa.center_y = self.tailAb_joint_rear[1]
        self.tailBa_joint_rear = (self.tailAb.center_x, self.tailAb.center_y + 38)

        self.tailBb = arcade.Sprite()

        self.tailBb.texture = self.body_parts_textures[5]

        self.body_sprites.append(self.tailBa)
        self.body_sprites.append(self.tailBb)

        # Tail segment C [6]
        self.tailCa = arcade.Sprite()
        self.tailCb = arcade.Sprite()
        self.body_parts_textures.append(
            arcade.load_texture(f"images/dragon_{color_id}.png", x=836, y=72, width=60, height=56))
        self.tailCa.texture = self.body_parts_textures[6]
        self.tailCb.texture = self.body_parts_textures[6]
        self.body_sprites.append(self.tailCa)
        self.body_sprites.append(self.tailCb)

        # Tail segment D [7]
        self.tailDa = arcade.Sprite()
        self.tailDb = arcade.Sprite()
        self.body_parts_textures.append(
            arcade.load_texture(f"images/dragon_{color_id}.png", x=1032, y=72, width=52, height=48))
        self.tailDa.texture = self.body_parts_textures[7]
        self.tailDb.texture = self.body_parts_textures[7]
        self.body_sprites.append(self.tailDa)
        self.body_sprites.append(self.tailDb)

        # Tail Tip [8]
        self.tailtip = arcade.Sprite()
        self.body_parts_textures.append(
            arcade.load_texture(f"images/dragon_{color_id}.png", x=1172, y=4, width=104, height=116))
        self.tailtip.texture = self.body_parts_textures[8]
        self.body_sprites.append(self.tailtip)

        self.body_sprites.append(self.tailAa)
        self.body_sprites.append(self.wings)
        self.body_sprites.append(self.body)
        self.body_sprites.append(self.neckD)
        self.body_sprites.append(self.neckC)
        self.body_sprites.append(self.neckB)
        self.body_sprites.append(self.neckA)
        self.body_sprites.append(self.head)

    def draw(self):
        self.head.center_y = 512
        self.head.center_x = 512
        self.body_sprites.draw()


    def update_animation(self, delta_time: float = 1 / 60):
        pass

    def perform_action(self, action):
        pass
