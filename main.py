def on_up_pressed():
    while controller.up.is_pressed():
        mySprite.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f f f f f f f . . . . 
                        . . . f f f f f f f f f f . . . 
                        . . . f f f f f f f f f f . . . 
                        . . f f f f f f f f f f f f . . 
                        . . f f f f f f f f f f f f . . 
                        . . f f f f f f f f f f f f . . 
                        . . f f f f f f f f f f f f . . 
                        . f f f f f f f f f f f f f f . 
                        . f f f f f f f f f f f f f f . 
                        . . . f f f f f f f f f f . . . 
                        . . e 4 f f f f f f f f e . . . 
                        . . 4 d d e 6 6 6 6 6 f 4 . . . 
                        . . . 4 e e f f f f f f e . . . 
                        . . . . . . . . . f f f . . . .
        """))
        pause(100)
        mySprite.set_image(img("""
            . . . . . . f f f f . . . . . . 
                        . . . . f f f f f f f f . . . . 
                        . . . f f f f f f f f f f . . . 
                        . . f f f f f f f f f f f f . . 
                        . . f f f f f f f f f f f f . . 
                        . . f f f f f f f f f f f f . . 
                        . . f f f f f f f f f f f f . . 
                        . f f f f f f f f f f f f f f . 
                        . f f f f f f f f f f f f f f . 
                        . . f f f f f f f f f f f f . . 
                        . . . f f f f f f f f f f . . . 
                        . . e 4 f f f f f f f f 4 e . . 
                        . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                        . . 4 4 f 9 9 9 9 9 9 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
        """))
        pause(100)
        mySprite.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f f f f f f f . . . . 
                        . . . f f f f f f f f f f . . . 
                        . . . f f f f f f f f f f . . . 
                        . . f f f f f f f f f f f f . . 
                        . . f f f f f f f f f f f f . . 
                        . . f f f f f f f f f f f f . . 
                        . . f f f f f f f f f f f f . . 
                        . f f f f f f f f f f f f f f . 
                        . f f f f f f f f f f f f f f . 
                        . . . f f f f f f f f f f . . . 
                        . . . e f f f f f f f f 4 e . . 
                        . . . 4 f 6 6 6 6 6 e d d 4 . . 
                        . . . e f f f f f f e e 4 . . . 
                        . . . . f f f . . . . . . . . .
        """))
        pause(100)
        mySprite.set_image(img("""
            . . . . . . f f f f . . . . . . 
                        . . . . f f f f f f f f . . . . 
                        . . . f f f f f f f f f f . . . 
                        . . f f f f f f f f f f f f . . 
                        . . f f f f f f f f f f f f . . 
                        . . f f f f f f f f f f f f . . 
                        . . f f f f f f f f f f f f . . 
                        . f f f f f f f f f f f f f f . 
                        . f f f f f f f f f f f f f f . 
                        . . f f f f f f f f f f f f . . 
                        . . . f f f f f f f f f f . . . 
                        . . e 4 f f f f f f f f 4 e . . 
                        . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                        . . 4 4 f 9 9 9 9 9 9 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
        """))
        pause(100)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    if mySprite.x == x and mySprite.y == y:
        while controller.B.is_pressed() and mySprite.y - y < 200:
            mySprite.vy += -20
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . 7 7 . . . . . . . . . 
                    . . . . . 7 7 . . . . . . . . . 
                    . . . . . . . 2 2 2 . . . . . . 
                    . . . . . 2 2 2 2 2 2 2 . . . . 
                    . . . . . 2 2 2 2 1 2 2 . . . . 
                    . . . . 2 2 2 2 2 2 1 2 2 . . . 
                    . . . . 2 2 2 2 2 2 2 2 2 . . . 
                    . . . . 2 2 2 2 2 2 2 2 2 . . . 
                    . . . . . 2 2 2 2 2 2 2 . . . . 
                    . . . . . 2 2 2 2 2 2 2 . . . . 
                    . . . . . . . 2 2 2 . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        69,
        0)
    music.pew_pew.play()
    pause(500)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    while controller.left.is_pressed():
        mySprite.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . f f f f f f f f f . . . . 
                        . . f f f f f f f f f f f . . . 
                        . . f f f f f f f f f f f . . . 
                        . f f f f f f f f f f f f . . . 
                        . f f f f f f f f f f f f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 8 b e 4 4 e f f . . 
                        . . f e d d 8 1 4 d 4 e e f . . 
                        . . . f d d d e e e e e f . . . 
                        . . . f e 4 e d d 4 f . . . . . 
                        . . . f 6 6 e d d e f . . . . . 
                        . . f f 9 9 f e e f f f . . . . 
                        . . f f f f f f f f f f . . . . 
                        . . . f f f . . . f f . . . . .
        """))
        pause(100)
        mySprite.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . f f f f f f f f . . . . . 
                        . . f f f f f f f f f f f . . . 
                        . f f f f f f f f f f f f . . . 
                        . f f f f f f f f f f f f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 8 b e 4 4 e f f . . 
                        . . f e d d 8 1 4 d 4 e e f . . 
                        . . . f d d d d 4 e e e f . . . 
                        . . . f e 4 4 4 e e f f . . . . 
                        . . . f 6 6 6 e d d 4 . . . . . 
                        . . . f 6 6 6 e d d e . . . . . 
                        . . . f 9 9 9 f e e f . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . . . f f f . . . . . . .
        """))
        pause(100)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile(sprite, location):
    music.play_melody("D E F G - - C - ", 300)
    music.stop_all_sounds()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile)

def on_right_pressed():
    while controller.right.is_pressed():
        mySprite.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . f f f f f f f f f . . . 
                        . . . f f f f f f f f f f f . . 
                        . . . f f f f f f f f f f f . . 
                        . . . f f f f f f f f f f f f . 
                        . . . f f f f f f f f f f f f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b 8 4 4 e e f . 
                        . . f e e 4 d 4 1 8 d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . 4 d d e 4 4 4 e f . . . 
                        . . . . e d d e 6 6 6 6 f . . . 
                        . . . . f e e f 9 9 9 9 f f . . 
                        . . . . f f f f f f f f f f . . 
                        . . . . . f f . . . f f f . . .
        """))
        pause(100)
        mySprite.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . f f f f f f f f . . . 
                        . . . . f f f f f f f f f . . . 
                        . . . . f f f f f f f f f f . . 
                        . . . f f f f f f f f f f f f . 
                        . . . f f f f f f f f f f f f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b 8 4 4 e e f . 
                        . . f e e 4 d 4 1 8 d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . f f e e 4 4 4 e f . . . 
                        . . . . . 4 d d e 6 6 6 f . . . 
                        . . . . . e d d e 6 6 6 f . . . 
                        . . . . . f e e f 9 9 9 f . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . . . . f f f . . . . . .
        """))
        pause(100)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    while controller.down.is_pressed():
        mySprite.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f f f f f f f . . . . 
                        . . . f f f f f f f f f f . . . 
                        . . f f f f f f f f f f f f . . 
                        . . f f f f f f f f f f f f . . 
                        . f f f f f f f f f f f f f f . 
                        . f f f f f e e e e f f f f f . 
                        . . f e f b 8 4 4 8 b f e f . . 
                        . . f e 4 1 8 d d 8 1 4 e f . . 
                        . . . f e 4 d d d d 4 e f e . . 
                        . . f e f 6 6 6 6 e d d 4 e . . 
                        . . e 4 f 6 6 6 6 e d d e . . . 
                        . . . . f 9 9 9 9 f e e . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . . f f f . . . . . . . . .
        """))
        pause(100)
        mySprite.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f f f . . . . 
                        . . . f f f f f f f f f f . . . 
                        . . . f f f f f f f f f f . . . 
                        . . f f f f f f f f f f f f . . 
                        . . f f f f f f f f f f f f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f b 8 4 4 8 b f e f f . 
                        . f f e 4 1 8 d d 8 1 4 e f f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 6 6 6 6 6 6 f 4 e . . 
                        . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                        . . 4 4 f 9 9 9 9 9 9 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
        """))
        pause(100)
        mySprite.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f f f f f f f . . . . 
                        . . . f f f f f f f f f f . . . 
                        . . f f f f f f f f f f f f . . 
                        . . f f f f f f f f f f f f . . 
                        . f f f f f f f f f f f f f f . 
                        . f f f f f e e e e f f f f f . 
                        . . f e f b 8 4 4 8 b f e f . . 
                        . . f e 4 1 8 d d 8 1 4 e f . . 
                        . . e f e 4 d d d d 4 e f . . . 
                        . . e 4 d d e 6 6 6 6 f e f . . 
                        . . . e d d e 6 6 6 6 f 4 e . . 
                        . . . . e e f 9 9 9 9 f . . . . 
                        . . . . . f f f f f f f . . . . 
                        . . . . . . . . . f f f . . . .
        """))
        pause(100)
        mySprite.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f f f . . . . 
                        . . . f f f f f f f f f f . . . 
                        . . . f f f f f f f f f f . . . 
                        . . f f f f f f f f f f f f . . 
                        . . f f f f f f f f f f f f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f b 8 4 4 8 b f e f f . 
                        . f f e 4 1 8 d d 8 1 4 e f f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 6 6 6 6 6 6 f 4 e . . 
                        . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                        . . 4 4 f 9 9 9 9 9 9 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
        """))
        pause(100)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

projectile: Sprite = None
y = 0
x = 0
mySprite: Sprite = None
tiles.set_tilemap(tiles.create_tilemap(hex("""
            1000100002020202020202020202020101010101020202020202020202020201010101010202020202040202020202010101010101010101020202020202020101010101010101010202050502020202020202040101010102020502020202020202020201010101020505020202040202020202010101010205020202020202020202030202020202050202020202020204020204020202020502020202020202020202020202020205020202020202020202020202020202050202020202010101010102020402020505020202020101010101010101010205020202020201010101010101010102020202020202010101010101010101020202020202020101010101
        """),
        img("""
            . . . . . . . . . . . 2 2 2 2 2 
                . . . . . . . . . . . 2 2 2 2 2 
                . . . . . . . . . . . 2 2 2 2 2 
                2 2 2 2 . . . . . . . 2 2 2 2 2 
                2 2 2 2 . . . . . . . . . . . . 
                2 2 2 2 . . . . . . . . . . . . 
                2 2 2 2 . . . . . . . . . . . . 
                2 2 2 2 . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . 2 2 2 2 2 
                . . . . . . . . . . . 2 2 2 2 2 
                2 2 2 2 . . . . . . . 2 2 2 2 2 
                2 2 2 2 . . . . . . . 2 2 2 2 2 
                2 2 2 2 . . . . . . . 2 2 2 2 2
        """),
        [myTiles.transparency16,
            sprites.builtin.forest_tiles0,
            sprites.castle.tile_dark_grass1,
            sprites.dungeon.chest_closed,
            sprites.castle.tile_dark_grass2,
            sprites.castle.tile_dark_grass3],
        TileScale.SIXTEEN))
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . f f f f f f f f . . . . 
            . . . f f f f f f f f f f . . . 
            . . . f f f f f f f f f f . . . 
            . . f f f f f f f f f f f f . . 
            . . f f f f f f f f f f f f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b 8 4 4 8 b f e f f . 
            . f f e 4 1 8 d d 8 1 4 e f f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 6 6 6 6 6 6 f 4 e . . 
            . . 4 d f 6 6 6 6 6 6 f d 4 . . 
            . . 4 4 f 9 9 9 9 9 9 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
scene.camera_follow_sprite(mySprite)

def on_update_interval():
    global x, y
    x = mySprite.x
    y = mySprite.y
game.on_update_interval(2000, on_update_interval)
