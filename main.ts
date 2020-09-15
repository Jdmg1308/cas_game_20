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
    } else if (Carla) {
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
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.floorLightMoss, function (sprite, location) {
    statusbar.value += -0.1
})
scene.onOverlapTile(SpriteKind.Player, myTiles.tile4, function (sprite, location) {
    Martin = true
    Esteban = false
    Carla = false
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
    } else if (Carla) {
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
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.secondary, function (sprite, otherSprite) {
    music.playMelody("C E G B C5 G D E ", 300)
    game.setDialogCursor(img`
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
        `)
    game.showLongText("Peeepeee poopoo", DialogLayout.Bottom)
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
    } else if (Carla) {
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
    }
})
scene.onOverlapTile(SpriteKind.Player, myTiles.tile6, function (sprite, location) {
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
    } else if (Carla) {
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
    }
})
scene.onOverlapTile(SpriteKind.Player, myTiles.tile5, function (sprite, location) {
    Carla = true
    Martin = false
    Esteban = false
})
let projectile: Sprite = null
let statusbar: StatusBarSprite = null
let mySprite: Sprite = null
let Carla = false
let Esteban = false
let Martin = false
Martin = true
Esteban = false
Carla = false
tiles.setTilemap(tiles.createTilemap(hex`100010000303060303030304030304010101010103070404040504040503040101010101030303030303060304030401010101010101010103040304040304010101010101010101070407040403040303030303010101010304030407030303040703070101010103040304050304040404040401010101070404040404040403030302030303030304030604040404050403030704040404110312041307040704040403030503040304050403030303030303070406030404030404030308090a090903030303030403040403030b0d0e0d0e01010101030404050403030b0f100f1001010101030504060503030c0d0e0d0e01010101030303030303030c0f100f10`, img`
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
    `, [myTiles.transparency16,sprites.builtin.forestTiles0,sprites.dungeon.chestClosed,sprites.dungeon.floorLight1,sprites.dungeon.floorLight0,sprites.dungeon.floorLight5,sprites.dungeon.floorLightMoss,sprites.dungeon.floorLight2,sprites.dungeon.greenOuterNorthWest,sprites.dungeon.greenOuterNorth0,sprites.dungeon.greenOuterNorth1,sprites.dungeon.greenOuterWest1,sprites.dungeon.greenOuterWest0,sprites.dungeon.greenInnerNorthWest,sprites.dungeon.greenInnerNorthEast,sprites.dungeon.greenInnerSouthWest,sprites.dungeon.greenInnerSouthEast,myTiles.tile4,myTiles.tile5,myTiles.tile6], TileScale.Sixteen))
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
let mySprite2 = sprites.create(img`
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
    `, SpriteKind.secondary)
tiles.placeOnTile(mySprite2, tiles.getTileLocation(14, 7))
