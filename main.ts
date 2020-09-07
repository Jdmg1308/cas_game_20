controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
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
    pause(500)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
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
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestClosed, function (sprite, location) {
    music.playMelody("D E F G - - C - ", 300)
    music.stopAllSounds()
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
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
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
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
})
let projectile: Sprite = null
let mySprite: Sprite = null
tiles.setTilemap(tiles.createTilemap(hex`1000100002020202020202020202020101010101020202020202020202020201010101010202020202040202020202010101010101010101020202020202020101010101010101010202050502020202020202040101010102020502020202020202020201010101020505020202040202020202010101010205020202020202020202030202020202050202020202020204020204020202020502020202020202020202020202020205020202020202020202020202020202050202020202010101010102020402020505020202020101010101010101010205020202020201010101010101010102020202020202010101010101010101020202020202020101010101`, img`
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
    `, [myTiles.transparency16,sprites.builtin.forestTiles0,sprites.castle.tileDarkGrass1,sprites.dungeon.chestClosed,sprites.castle.tileDarkGrass2,sprites.castle.tileDarkGrass3], TileScale.Sixteen))
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
controller.moveSprite(mySprite)
scene.cameraFollowSprite(mySprite)
