namespace SpriteKind {
    export const secondary = SpriteKind.create()
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Martin) {
        while (controller.up.isPressed()) {
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
        }
    } else if (Esteban) {
        while (controller.up.isPressed()) {
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
        }
    } else if (Carla) {
        while (controller.up.isPressed()) {
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
        }
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`tile4`, function (sprite, location) {
    Martin = true
    Esteban = false
    Carla = false
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.floorLightMoss, function (sprite, location) {
    statusbar.value += -0.1
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`tile7`, function (sprite, location) {
    if (tiles.tileAtLocationEquals(tiles.getTileLocation(17, 5), assets.tile`tile7`) || tiles.tileAtLocationEquals(tiles.getTileLocation(17, 4), assets.tile`tile7`)) {
        tiles.setTilemap(tilemap`level1`)
        tiles.placeOnTile(mySprite, tiles.getTileLocation(15, 59))
        pause(100)
        music.playMelody("E - E - E - E - ", 640)
        if (Martin) {
            PersonajeSec1 = sprites.create(img`
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
                `, SpriteKind.secondary)
            tiles.placeOnTile(PersonajeSec1, tiles.getTileLocation(14, 5))
            PersonajeSec2 = sprites.create(img`
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
                `, SpriteKind.secondary)
            tiles.placeOnTile(PersonajeSec2, tiles.getTileLocation(14, 10))
        } else if (Esteban) {
            PersonajeSec1 = sprites.create(img`
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
                `, SpriteKind.secondary)
            tiles.placeOnTile(PersonajeSec1, tiles.getTileLocation(14, 5))
            PersonajeSec2 = sprites.create(img`
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
                `, SpriteKind.secondary)
            tiles.placeOnTile(PersonajeSec2, tiles.getTileLocation(14, 10))
        } else if (Carla) {
            PersonajeSec1 = sprites.create(img`
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
                `, SpriteKind.secondary)
            tiles.placeOnTile(PersonajeSec1, tiles.getTileLocation(14, 5))
            PersonajeSec2 = sprites.create(img`
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
                `, SpriteKind.secondary)
            tiles.placeOnTile(PersonajeSec2, tiles.getTileLocation(14, 10))
        }
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, mySprite, 69, 0)
    music.pewPew.play()
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Martin) {
        while (controller.left.isPressed()) {
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
        }
    } else if (Esteban) {
        while (controller.left.isPressed()) {
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
        }
    } else if (Carla) {
        while (controller.left.isPressed()) {
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
        }
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestClosed, function (sprite, location) {
    statusbar.value += 2
})
statusbars.onZero(StatusBarKind.Health, function (status) {
    game.over(false)
    game.reset()
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Martin) {
        while (controller.right.isPressed()) {
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
        }
    } else if (Esteban) {
        while (controller.right.isPressed()) {
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
        }
    } else if (Carla) {
        while (controller.right.isPressed()) {
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
        }
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`tile5`, function (sprite, location) {
    Carla = true
    Martin = false
    Esteban = false
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`tile6`, function (sprite, location) {
    Esteban = true
    Martin = false
    Carla = false
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Martin) {
        while (controller.down.isPressed()) {
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
        }
    } else if (Esteban) {
        while (controller.down.isPressed()) {
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
        }
    } else if (Carla) {
        while (controller.down.isPressed()) {
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
            mySprite.setImage(img`
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
                `)
            pause(100)
        }
    }
})
let projectile: Sprite = null
let PersonajeSec2: Sprite = null
let PersonajeSec1: Sprite = null
let statusbar: StatusBarSprite = null
let mySprite: Sprite = null
let Carla = false
let Esteban = false
let Martin = false
Martin = true
Esteban = false
Carla = false
tiles.setTilemap(tilemap`level2`)
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mySprite, 100, 100)
scene.cameraFollowSprite(mySprite)
statusbar = statusbars.create(16, 2, StatusBarKind.Health)
statusbar.attachToSprite(mySprite)
statusbar.value = 200
