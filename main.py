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
                                . . . . . . 4 4 4 4 . . . . . . 
                                . . . . 4 4 4 4 4 4 4 4 . . . . 
                                . . . 4 4 4 4 4 4 4 4 4 4 . . . 
                                . . . 4 4 4 4 4 4 4 4 4 4 . . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . . 4 4 4 4 4 4 4 4 4 4 . . . 
                                . . e 4 4 4 4 4 4 4 4 4 e . . . 
                                . . 4 d d e 7 7 7 7 7 f 4 . . . 
                                . . . 4 e e f f f f f f e . . . 
                                . . . . . . . . . 8 8 8 . . . .
            """))
            pause(100)
            mySprite.set_image(img("""
                . . . . . . 4 4 4 4 . . . . . . 
                                . . . . 4 4 4 4 4 4 4 4 . . . . 
                                . . . 4 4 4 4 4 4 4 4 4 4 . . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . 4 4 4 4 4 4 4 4 4 4 4 4 4 4 . 
                                . 4 4 4 4 4 4 4 4 4 4 4 4 4 4 . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . . 4 4 4 4 4 4 4 4 4 4 . . . 
                                . . e f 4 4 4 4 4 4 4 4 f e . . 
                                . . 4 d f 7 7 7 7 7 7 f d 4 . . 
                                . . 4 4 f 7 7 7 7 7 7 f 4 4 . . 
                                . . . . . 8 8 8 8 8 8 . . . . . 
                                . . . . . 8 8 . . 8 8 . . . . .
            """))
            pause(100)
            mySprite.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . . . 4 4 4 4 . . . . . . 
                                . . . . 4 4 4 4 4 4 4 4 . . . . 
                                . . . 4 4 4 4 4 4 4 4 4 4 . . . 
                                . . . 4 4 4 4 4 4 4 4 4 4 . . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . 4 4 4 4 4 4 4 4 4 4 4 4 4 4 . 
                                . 4 4 4 4 4 4 4 4 4 4 4 4 4 4 . 
                                . . . 4 4 4 4 4 4 4 4 4 4 . . . 
                                . . . e 4 4 4 4 4 4 4 4 4 e . . 
                                . . . 4 f 7 7 7 7 7 e d d 4 . . 
                                . . . e f f f f f f e e 4 . . . 
                                . . . . 8 8 8 . . . . . . . . .
            """))
            pause(100)
            mySprite.set_image(img("""
                . . . . . . 4 4 4 4 . . . . . . 
                                . . . . 4 4 4 4 4 4 4 4 . . . . 
                                . . . 4 4 4 4 4 4 4 4 4 4 . . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . 4 4 4 4 4 4 4 4 4 4 4 4 4 4 . 
                                . 4 4 4 4 4 4 4 4 4 4 4 4 4 4 . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . . 4 4 4 4 4 4 4 4 4 4 . . . 
                                . . e f 4 4 4 4 4 4 4 4 f e . . 
                                . . 4 d f 7 7 7 7 7 7 f d 4 . . 
                                . . 4 4 f 7 7 7 7 7 7 f 4 4 . . 
                                . . . . . 8 8 8 8 8 8 . . . . . 
                                . . . . . 8 8 . . 8 8 . . . . .
            """))
            pause(100)
    elif Carla:
        while controller.up.is_pressed():
            mySprite.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . . . e e e e . . . . . . 
                                . . . . e e e e e e e e . . . . 
                                . . . e e e e e e e e e e . . . 
                                . . . e e e e e e e e e e . . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . . f f e e e e e e e e . . . 
                                . . e 4 e f e e e e e e e . . . 
                                . . 4 d d f e e e e e f 4 . . . 
                                . . . 4 e e f f f f f f e . . . 
                                . . . . . . . . . f f f . . . .
            """))
            pause(100)
            mySprite.set_image(img("""
                . . . . . . e e e e . . . . . . 
                                . . . . e e e e e e e e . . . . 
                                . . . e e e e e e e e e e . . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . . e e e e e e e e e e . . . 
                                . . e 4 e e e e e e e e 4 e . . 
                                . . 4 d f e e e e e e f d 4 . . 
                                . . 4 4 f b e e e e b f 4 4 . . 
                                . . . . . f f f f f f . . . . . 
                                . . . . . f f . . f f . . . . .
            """))
            pause(100)
            mySprite.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . . . e e e e . . . . . . 
                                . . . . e e e e e e e e . . . . 
                                . . . e e e e e e e e e e . . . 
                                . . . e e e e e e e e e e . . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . . e e e e e e e e f f . . . 
                                . . . e e e e e e e f e 4 e . . 
                                . . . 4 f e e e e e f d d 4 . . 
                                . . . e f f f f f f e e 4 . . . 
                                . . . . f f f . . . . . . . . .
            """))
            pause(100)
            mySprite.set_image(img("""
                . . . . . . e e e e . . . . . . 
                                . . . . e e e e e e e e . . . . 
                                . . . e e e e e e e e e e . . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . . e e e e e e e e e e . . . 
                                . . e 4 e e e e e e e e 4 e . . 
                                . . 4 d f e e e e e e f d 4 . . 
                                . . 4 4 f b e e e e b f 4 4 . . 
                                . . . . . f f f f f f . . . . . 
                                . . . . . f f . . f f . . . . .
            """))
            pause(100)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile(sprite, location):
    global Martin, Esteban, Carla
    Martin = True
    Esteban = False
    Carla = False
    scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
    tile4
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite, location):
    statusbar.value += -0.1
    scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.floor_light_moss,
    on_overlap_tile2)

def on_overlap_tile3(sprite, location):
    global PersonajeSec1, PersonajeSec2
    if tiles.tile_at_location_equals(tiles.get_tile_location(17, 5),
        assets.tile("""
        tile7
        """)) or tiles.tile_at_location_equals(tiles.get_tile_location(17, 4),
        assets.tile("""
        tile7
        """)):
            tiles.set_tilemap(tilemap("""
            level3
        """))
        tiles.set_tilemap(tilemap("""
        level1
        """))
        tiles.place_on_tile(mySprite, tiles.get_tile_location(15, 59))
        pause(100)
        music.play_melody("E - E - E - E - ", 640)
        if Martin:
            PersonajeSec1 = sprites.create(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . 4 4 4 4 4 4 4 4 . . . . 
                                    . . . 4 4 4 4 4 4 4 4 4 4 . . . 
                                    . . . 4 4 4 4 4 4 4 4 4 4 . . . 
                                    . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                    . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                    . . 4 4 4 4 e e e e 4 4 4 4 . . 
                                    . 4 4 e 4 b 7 4 4 7 b 4 e 4 4 . 
                                    . 4 4 e 4 1 7 d d 7 1 4 e 4 4 . 
                                    . . 4 e e d d d d d d e e 4 . . 
                                    . . . f e e 4 4 4 4 e e f . . . 
                                    . . e 4 f 7 7 7 7 7 7 f 4 e . . 
                                    . . 4 d f 7 7 7 7 7 7 f d 4 . . 
                                    . . 4 4 f 7 7 7 7 7 7 f 4 4 . . 
                                    . . . . . 8 8 8 8 8 8 . . . . . 
                                    . . . . . 8 8 . . 8 8 . . . . .
                """),
                SpriteKind.secondary)
            tiles.place_on_tile(PersonajeSec1, tiles.get_tile_location(14, 5))
            PersonajeSec2 = sprites.create(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . e e e e e e e e . . . . 
                                    . . . e e e e e e e e e e . . . 
                                    . . . e e e e e e e e e e . . . 
                                    . . e e e e e e e e e e e e . . 
                                    . . e e e e e e e e e e e e . . 
                                    . . e e e f f e e f f e e e e . 
                                    . . e e f 1 9 4 4 9 1 f e e e . 
                                    . e e e e 1 9 d d 9 1 e e e . . 
                                    . e e e e d d d d d d e e e . . 
                                    . . e e e e 4 4 4 4 e e e e . . 
                                    . . 4 4 e e a a a a a f 4 4 . . 
                                    . . 4 d f a a a a a a f d 4 . . 
                                    . . 4 4 f c c c c c c f 4 4 . . 
                                    . . . . . f f f f f f . . . . . 
                                    . . . . . f f . . f f . . . . .
                """),
                SpriteKind.secondary)
            tiles.place_on_tile(PersonajeSec2, tiles.get_tile_location(14, 10))
        elif Esteban:
            PersonajeSec1 = sprites.create(img("""
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
                SpriteKind.secondary)
            tiles.place_on_tile(PersonajeSec1, tiles.get_tile_location(14, 5))
            PersonajeSec2 = sprites.create(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . e e e e e e e e . . . . 
                                    . . . e e e e e e e e e e . . . 
                                    . . . e e e e e e e e e e . . . 
                                    . . e e e e e e e e e e e e . . 
                                    . . e e e e e e e e e e e e . . 
                                    . . e e e f f e e f f e e e e . 
                                    . . e e f 1 9 4 4 9 1 f e e e . 
                                    . e e e e 1 9 d d 9 1 e e e . . 
                                    . e e e e d d d d d d e e e . . 
                                    . . e e e e 4 4 4 4 e e e e . . 
                                    . . 4 4 e e a a a a a f 4 4 . . 
                                    . . 4 d f a a a a a a f d 4 . . 
                                    . . 4 4 f c c c c c c f 4 4 . . 
                                    . . . . . f f f f f f . . . . . 
                                    . . . . . f f . . f f . . . . .
                """),
                SpriteKind.secondary)
            tiles.place_on_tile(PersonajeSec2, tiles.get_tile_location(14, 10))
        elif Carla:
            PersonajeSec1 = sprites.create(img("""
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
                SpriteKind.secondary)
            tiles.place_on_tile(PersonajeSec1, tiles.get_tile_location(14, 5))
            PersonajeSec2 = sprites.create(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . 4 4 4 4 4 4 4 4 . . . . 
                                    . . . 4 4 4 4 4 4 4 4 4 4 . . . 
                                    . . . 4 4 4 4 4 4 4 4 4 4 . . . 
                                    . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                    . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                    . . 4 4 4 4 e e e e 4 4 4 4 . . 
                                    . 4 4 e 4 b 7 4 4 7 b 4 e 4 4 . 
                                    . 4 4 e 4 1 7 d d 7 1 4 e 4 4 . 
                                    . . 4 e e d d d d d d e e 4 . . 
                                    . . . f e e 4 4 4 4 e e f . . . 
                                    . . e 4 f 7 7 7 7 7 7 f 4 e . . 
                                    . . 4 d f 7 7 7 7 7 7 f d 4 . . 
                                    . . 4 4 f 7 7 7 7 7 7 f 4 4 . . 
                                    . . . . . 8 8 8 8 8 8 . . . . . 
                                    . . . . . 8 8 . . 8 8 . . . . .
                """),
                SpriteKind.secondary)
            tiles.place_on_tile(PersonajeSec2, tiles.get_tile_location(14, 10))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
    tile7
    """),
    on_overlap_tile3)

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
                                . . . f 7 7 e d d e f . . . . . 
                                . . 8 8 7 7 f e e f f 8 . . . . 
                                . . 8 8 8 f f f f f 8 8 . . . . 
                                . . . 8 8 8 . . . 8 8 . . . . .
            """))
            pause(100)
            mySprite.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . 4 4 4 4 4 4 . . . . . . 
                                . . . 4 4 4 4 4 4 4 4 . . . . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 . . . 
                                . 4 4 4 4 4 4 4 4 4 4 4 4 . . . 
                                . 4 4 4 4 4 4 4 4 4 4 4 4 . . . 
                                . 4 4 4 e e e 4 4 4 4 4 4 4 . . 
                                . 4 e e 4 4 7 b e 4 4 e 4 4 . . 
                                . . f e d d 7 1 4 d 4 e e 4 . . 
                                . . . f d d d d 4 e e e f . . . 
                                . . . f e 4 4 4 e e f f . . . . 
                                . . . f 7 7 7 e d d 4 . . . . . 
                                . . . f 7 7 7 e d d e . . . . . 
                                . . . f 7 7 7 f e e f . . . . . 
                                . . . . f f f f f f . . . . . . 
                                . . . . . . 8 8 8 . . . . . . .
            """))
            pause(100)
    elif Carla:
        while controller.left.is_pressed():
            mySprite.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . e e e e e e . . . . . . 
                                . . . e e e e e e e e e . . . . 
                                . . e e e e e e e e e e e . . . 
                                . . e e e e e e e e e e e . . . 
                                . . e e e e e e e e e e e . . . 
                                . . e e e e e e e e e e e . . . 
                                . . e e e e f f e e e e e e . . 
                                . . e e 4 4 9 b f e e e e e . . 
                                . . . e d d 9 1 f e e e e e . . 
                                . . . f d d d e e f e e e . . . 
                                . . . f e 4 e d d e f e . . . . 
                                . . . f a a e d d e f . . . . . 
                                . . f f b b f e e f f f . . . . 
                                . . f f f f f f f f f f . . . . 
                                . . . f f f . . . f f . . . . .
            """))
            pause(100)
            mySprite.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . e e e e e e . . . . . . 
                                . . . e e e e e e e e . . . . . 
                                . . e e e e e e e e e e e . . . 
                                . . e e e e e e e e e e e . . . 
                                . . e e e e e e e e e e e . . . 
                                . . e e e e f f e e e e e e . . 
                                . . e e 4 4 9 b f e e e e e . . 
                                . . . e d d 9 1 4 e e e e e . . 
                                . . . f d d d d 4 f e e e . . . 
                                . . . f e 4 4 4 e e f e e . . . 
                                . . . f a a a e d d 4 f e . . . 
                                . . . f a a a e d d e f e . . . 
                                . . . f b b b f e e f e e . . . 
                                . . . . f f f f f f . . . . . . 
                                . . . . . . f f f . . . . . . .
            """))
            pause(100)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile4(sprite, location):
    statusbar.value += 2
    scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile4)

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
                                . . . . . . 4 4 4 4 4 4 . . . . 
                                . . . . 4 4 4 4 4 4 4 4 4 . . . 
                                . . . 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . . 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . . 4 4 4 4 4 4 4 4 4 4 4 4 . 
                                . . . 4 4 4 4 4 4 4 4 4 4 4 4 . 
                                . . 4 4 4 4 4 4 4 e e e 4 4 4 . 
                                . . 4 4 e 4 4 e b 7 4 4 e e 4 . 
                                . . 4 e e 4 d 4 1 7 d d e f . . 
                                . . . f e e e 4 d d d d f . . . 
                                . . . . 4 d d e 4 4 4 e f . . . 
                                . . . . e d d e 7 7 7 7 f . . . 
                                . . . . 8 e e f 7 7 7 7 f 8 . . 
                                . . . . 8 8 f f f f f f 8 8 . . 
                                . . . . . 8 8 . . . 8 8 8 . . .
            """))
            pause(100)
            mySprite.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . . 4 4 4 4 4 4 4 4 . . . 
                                . . . . 4 4 4 4 4 4 4 4 4 . . . 
                                . . . . 4 4 4 4 4 4 4 4 4 4 . . 
                                . . . 4 4 4 4 4 4 4 4 4 4 4 4 . 
                                . . . 4 4 4 4 4 4 4 4 4 4 4 4 . 
                                . . 4 4 4 4 4 4 4 e e e 4 4 4 . 
                                . . 4 4 e 4 4 e b 7 4 4 e e 4 . 
                                . . 4 e e 4 d 4 1 7 d d e f . . 
                                . . . f e e e 4 d d d d f . . . 
                                . . . . f f e e 4 4 4 e f . . . 
                                . . . . . 4 d d e 7 7 7 f . . . 
                                . . . . . e d d e 7 7 7 f . . . 
                                . . . . . f e e f 7 7 7 f . . . 
                                . . . . . . f f f f f f . . . . 
                                . . . . . . . 8 8 8 . . . . . .
            """))
            pause(100)
    elif Carla:
        while controller.right.is_pressed():
            mySprite.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . . . e e e e e e . . . . 
                                . . . . e e e e e e e e e . . . 
                                . . . e e e e e e e e e e e . . 
                                . . . e e e e e e e e e e e . . 
                                . . . e e e e e e e e e e e . . 
                                . . . e e e e e e e e e e e . . 
                                . . e e e e e e f f e e e e . . 
                                . . e e e e e f b 9 4 4 e e . . 
                                . . e e e f f 4 1 9 d d e . . . 
                                . . e e f e e 4 d d d d f . . . 
                                . . e f 4 d d e 4 4 4 e f . . . 
                                . . e f e d d e a a a a f . . . 
                                . . e e f e e f b b b b f f . . 
                                . . . . f f f f f f f f f f . . 
                                . . . . . f f . . . f f f . . .
            """))
            pause(100)
            mySprite.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . . e e e e e e e e . . . 
                                . . . . e e e e e e e e e . . . 
                                . . . . e e e e e e e e e e . . 
                                . . . e e e e e e e e e e e . . 
                                . . . e e e e e e e e e e e . . 
                                . . e e e e e e f f e e e e . . 
                                . . e e e e e f b 9 4 4 e e . . 
                                . . e e e e e 4 1 9 d d e . . . 
                                . . . e e e f 4 d d d d f . . . 
                                . . . e e f e e 4 4 4 e f . . . 
                                . . . e f 4 d d e a a a f . . . 
                                . . . e f e d d e a a a f . . . 
                                . . . . e f e e f b b b f . . . 
                                . . . . . . f f f f f f . . . . 
                                . . . . . . . f f f . . . . . .
            """))
            pause(100)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_overlap_tile5(sprite, location):
    global Carla, Martin, Esteban
    Carla = True
    Martin = False
    Esteban = False
    scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
    tile5
    """),
    on_overlap_tile5)

def on_overlap_tile6(sprite, location):
    global Esteban, Martin, Carla
    Esteban = True
    Martin = False
    Carla = False
    scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
    tile6
    """),
    on_overlap_tile6)

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
                                . . . . . . 4 4 4 4 . . . . . . 
                                . . . . 4 4 4 4 4 4 4 4 . . . . 
                                . . . 4 4 4 4 4 4 4 4 4 4 . . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . 4 4 4 4 4 4 4 4 4 4 4 4 4 4 . 
                                . 4 4 4 4 4 e e e e 4 4 4 4 4 . 
                                . . 4 e 4 b 7 4 4 7 b 4 e 4 . . 
                                . . 4 e 4 1 7 d d 7 1 4 e 4 . . 
                                . . . f e 4 d d d d 4 e f e . . 
                                . . f e f 7 7 7 7 e d d 4 e . . 
                                . . e 4 f 7 7 7 7 e d d e . . . 
                                . . . . f 7 7 7 7 f e e . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . . 8 8 8 . . . . . . . . .
            """))
            pause(100)
            mySprite.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . 4 4 4 4 4 4 4 4 . . . . 
                                . . . 4 4 4 4 4 4 4 4 4 4 . . . 
                                . . . 4 4 4 4 4 4 4 4 4 4 . . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . 4 4 4 4 e e e e 4 4 4 4 . . 
                                . 4 4 e 4 b 7 4 4 7 b 4 e 4 4 . 
                                . 4 4 e 4 1 7 d d 7 1 4 e 4 4 . 
                                . . 4 e e d d d d d d e e 4 . . 
                                . . . f e e 4 4 4 4 e e f . . . 
                                . . e 4 f 7 7 7 7 7 7 f 4 e . . 
                                . . 4 d f 7 7 7 7 7 7 f d 4 . . 
                                . . 4 4 f 7 7 7 7 7 7 f 4 4 . . 
                                . . . . . 8 8 8 8 8 8 . . . . . 
                                . . . . . 8 8 . . 8 8 . . . . .
            """))
            pause(100)
            mySprite.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . . . 4 4 4 4 . . . . . . 
                                . . . . 4 4 4 4 4 4 4 4 . . . . 
                                . . . 4 4 4 4 4 4 4 4 4 4 . . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . 4 4 4 4 4 4 4 4 4 4 4 4 4 4 . 
                                . 4 4 4 4 4 e e e e 4 4 4 4 4 . 
                                . . 4 e 4 b 7 4 4 7 b 4 e 4 . . 
                                . . 4 e 4 1 7 d d 7 1 4 e 4 . . 
                                . . e f e 4 d d d d 4 e f . . . 
                                . . e 4 d d e 7 7 7 7 f e f . . 
                                . . . e d d e 7 7 7 7 f 4 e . . 
                                . . . . e e f 7 7 7 7 f . . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . . . . . . 8 8 8 . . . .
            """))
            pause(100)
            mySprite.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . 4 4 4 4 4 4 4 4 . . . . 
                                . . . 4 4 4 4 4 4 4 4 4 4 . . . 
                                . . . 4 4 4 4 4 4 4 4 4 4 . . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                                . . 4 4 4 4 e e e e 4 4 4 4 . . 
                                . 4 4 e 4 b 7 4 4 7 b 4 e 4 4 . 
                                . 4 4 e 4 1 7 d d 7 1 4 e 4 4 . 
                                . . 4 e e d d d d d d e e 4 . . 
                                . . . f e e 4 4 4 4 e e f . . . 
                                . . e 4 f 7 7 7 7 7 7 f 4 e . . 
                                . . 4 d f 7 7 7 7 7 7 f d 4 . . 
                                . . 4 4 f 7 7 7 7 7 7 f 4 4 . . 
                                . . . . . 8 8 8 8 8 8 . . . . . 
                                . . . . . 8 8 . . 8 8 . . . . .
            """))
            pause(100)
    elif Carla:
        while controller.down.is_pressed():
            mySprite.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . e e e e e e e e . . . . 
                                . . . e e e e e e e e e e . . . 
                                . . . e e e e e e e e e e . . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e e . 
                                . . e e e f f e e f f e e e e . 
                                . e e e f 1 9 4 4 9 1 f e e . . 
                                . e e e e 1 9 d d 9 1 e e e . . 
                                . . e e e d d d d d d e e e . . 
                                . . e e e e 4 4 4 4 e e e e . . 
                                . . e 4 e e a a a a a f 4 e . . 
                                . . 4 d f a a a a a a f d 4 . . 
                                . . 4 4 f b b b b b b f 4 4 . . 
                                . . . . . f f f f f f . . . . . 
                                . . . . . f f . . f f . . . . .
            """))
            pause(100)
            mySprite.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . . . e e e e . . . . . . 
                                . . . . e e e e e e e e . . . . 
                                . . . e e e e e e e e e e . . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e f f e e f f e e e . . 
                                . . e e e b 9 4 4 9 b f e e . . 
                                . . e e e 1 9 d d 9 1 4 e e . . 
                                . . e f e e d d d d 4 e f e . . 
                                . . f e f a a a a e d d 4 e . . 
                                . . e 4 f a a a a e d d e . . . 
                                . . . . f b b b b f e e . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . . f f f . . . . . . . . .
            """))
            pause(100)
            mySprite.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . e e e e e e e e . . . . 
                                . . . e e e e e e e e e e . . . 
                                . . . e e e e e e e e e e . . . 
                                . . e e e e e e e e e e e . . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e f f e e f f e e e . . 
                                . . e e f b 9 4 4 9 b e e e . . 
                                . . e e e 1 9 d d 9 1 e e e . . 
                                . . e f e 4 d d d d 4 e f e . . 
                                . . e 4 d d e a a a a f e f . . 
                                . . . e d d e a a a a f 4 e . . 
                                . . . . e e f b b b b f . . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . . . . . . f f f . . . .
            """))
            pause(100)
            mySprite.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . e e e e e e e e . . . . 
                                . . . e e e e e e e e e e . . . 
                                . . . e e e e e e e e e e . . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e e e e e e e e e e . . 
                                . . e e e f f e e f f e e e e . 
                                . . e e f 1 9 4 4 9 1 f e e e . 
                                . e e e e 1 9 d d 9 1 e e e . . 
                                . e e e e d d d d d d e e e . . 
                                . . e e e e 4 4 4 4 e e e e . . 
                                . . 4 4 e e a a a a a f 4 4 . . 
                                . . 4 d f a a a a a a f d 4 . . 
                                . . 4 4 f c c c c c c f 4 4 . . 
                                . . . . . f f f f f f . . . . . 
                                . . . . . f f . . f f . . . . .
            """))
            pause(100)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

projectile: Sprite = None
PersonajeSec2: Sprite = None
PersonajeSec1: Sprite = None
statusbar: StatusBarSprite = None
mySprite: Sprite = None
Carla = False
Esteban = False
Martin = False
Martin = True
Esteban = False
Carla = False
tiles.set_tilemap(tilemap("""
level2
"""))
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
