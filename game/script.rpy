# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("John Pork", color="#a802ad")
define t = Character("Tim Cheese", color="#ad020a")

$ porklove = 0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg sigma at truecenter
    with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show j happy at truecenter
    with dissolve
    j "hi guys"
    show j angry at truecenter
    with dissolve
    j "you made me angry"

    menu:
        "Apologize":
            jump happyplace
            $ porklove += 100
        "Provoke":
            jump grave
            $ porklove -= 100

    pause 2

    "wow"

    # These display lines of dialogue.

    j "You've created a new Ren'Py game."

    t "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

    label happyplace:
        scene bg happyplace at truecenter
        with fade

        "John Pork notices you..."

        show j happy at truecenter
        with dissolve
        j "Thank you for apologizing!"

    return
    
    label grave:
        scene bg grave at truecenter
        with fade

        "John Pork appears behind you..."

        show j angry at truecenter
        with dissolve
        j "You will pay!"

        "The actions mr pork does to you are undescribable."
        pause 2
        "You lose"

    return