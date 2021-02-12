@namespace
class SpriteKind:
    secondary = SpriteKind.create()

def on_up_pressed():
    if Martin:
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
    elif Esteban:
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
    elif Carla:
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

def on_overlap_tile(sprite, location):
    statusbar.value += -0.1
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.floor_light_moss,
    on_overlap_tile)

def on_overlap_tile2(sprite, location):
    global Martin, Esteban, Carla
    Martin = True
    Esteban = False
    Carla = False
scene.on_overlap_tile(SpriteKind.player, myTiles.tile4, on_overlap_tile2)

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
    if Martin:
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
    elif Esteban:
        while controller.left.is_pressed():
            mySprite.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . 4 4 4 4 4 4 . . . . . . 
                                . . . 4 4 4 4 4 4 4 4 4 . . . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 . . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 . . . 
                                . 4 4 4 4 4 4 4 4 4 4 4 4 . . . 
                                . 4 4 4 4 4 4 4 4 4 4 4 4 . . . 
                                . 4 4 4 e e e 4 4 4 4 4 4 4 . . 
                                . 4 e e 4 4 7 b e 4 4 e 4 4 . . 
                                . . f e d d 7 1 4 d 4 e e 4 . . 
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
    elif Carla:
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

def on_on_overlap(sprite, otherSprite):
    music.play_melody("C E G B C5 G D E ", 300)
    game.set_dialog_cursor(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . f f f . . . . 
                . . . . . . f f f 2 2 f . . . . 
                . . . . . . f 2 2 2 2 f . . . . 
                . . . . . . . f 2 2 f . . . . . 
                . . . . . . f 2 f 2 f . . . . . 
                . . . . . f 2 f . f f . . . . . 
                . . . . f 2 f . . . . . . . . . 
                . . . . f f . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    game.show_long_text("Peeepeee poopoo", DialogLayout.BOTTOM)
sprites.on_overlap(SpriteKind.player, SpriteKind.secondary, on_on_overlap)

def on_overlap_tile3(sprite, location):
    statusbar.value += 2
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile3)

def on_on_zero(status):
    game.over(False)
    game.reset()
statusbars.on_zero(StatusBarKind.health, on_on_zero)

def on_right_pressed():
    if Martin:
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
    elif Esteban:
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
    elif Carla:
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

def on_overlap_tile4(sprite, location):
    global Esteban, Martin, Carla
    Esteban = True
    Martin = False
    Carla = False
scene.on_overlap_tile(SpriteKind.player, myTiles.tile6, on_overlap_tile4)

def on_down_pressed():
    if Martin:
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
    elif Esteban:
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
    elif Carla:
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

def on_overlap_tile5(sprite, location):
    global Carla, Martin, Esteban
    Carla = True
    Martin = False
    Esteban = False
scene.on_overlap_tile(SpriteKind.player, myTiles.tile5, on_overlap_tile5)

projectile: Sprite = None
statusbar: StatusBarSprite = None
mySprite: Sprite = None
Carla = False
Esteban = False
Martin = False
Martin = True
Esteban = False
Carla = False
tiles.set_tilemap(tiles.create_tilemap(hex("""
            100010000303060303030304030304010101010103070404040504040503040101010101030303030303060304030401010101010101010103040304040304010101010101010101070407040403040303030303010101010304030407030303040703070101010103040304050304040404040401010101070404040404040403030302030303030304030604040404050403030704040404110312041307040704040403030503040304050403030303030303070406030404030404030308090a090903030303030403040403030b0d0e0d0e01010101030404050403030b0f100f1001010101030504060503030c0d0e0d0e01010101030303030303030c0f100f10
        """),
        img("""
            . . . . . . . . . . . 2 2 2 2 2 
                . . . . . . . . . . . 2 2 2 2 2 
                . . . . . . . . . . . 2 2 2 2 2 
                2 2 2 2 . . . . . . . 2 2 2 2 2 
                2 2 2 2 . . . . . . . . . . . . 
                2 2 2 2 . . . . . . . . . . . . 
                2 2 2 2 . . . . . . . . . . . . 
                2 2 2 2 . . . . . . . . . . 2 . 
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
            sprites.dungeon.chest_closed,
            sprites.dungeon.floor_light1,
            sprites.dungeon.floor_light0,
            sprites.dungeon.floor_light5,
            sprites.dungeon.floor_light_moss,
            sprites.dungeon.floor_light2,
            sprites.dungeon.green_outer_north_west,
            sprites.dungeon.green_outer_north0,
            sprites.dungeon.green_outer_north1,
            sprites.dungeon.green_outer_west1,
            sprites.dungeon.green_outer_west0,
            sprites.dungeon.green_inner_north_west,
            sprites.dungeon.green_inner_north_east,
            sprites.dungeon.green_inner_south_west,
            sprites.dungeon.green_inner_south_east,
            myTiles.tile4,
            myTiles.tile5,
            myTiles.tile6],
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
statusbar = statusbars.create(16, 2, StatusBarKind.health)
statusbar.attach_to_sprite(mySprite)
statusbar.value = 200
mySprite2 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . 5 5 5 . . . . . . 
            . . . . . . 5 5 5 5 5 . . . . . 
            . . . . . 5 5 5 5 5 5 . . . . . 
            . . . . . 5 f 5 5 5 5 . . . . . 
            . . . . . 5 5 5 5 f 5 . . . . . 
            . . . . . 5 5 5 5 5 5 . . . . . 
            . . . . . 5 5 5 5 5 5 . . . . . 
            . . . . . 5 5 5 5 5 5 . . . . . 
            . . . . . 5 5 5 5 5 5 . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.secondary)
tiles.place_on_tile(mySprite2, tiles.get_tile_location(14, 7))