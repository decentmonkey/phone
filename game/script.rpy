# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define m = Character("Eileen")

define mcname = "Барди"
# The game starts here.


label start:

    $ phone_gallery = [
        "img_900000",
        "img_900001",
        "img_900002",
        "img_900003",
        "img_900004",
        "img_900005",
        "img_900006",
        "img_900007",
        "img_900008",
        "img_900009",
        "img_900010",
        "img_900011",
        "img_900012",
        "img_900013",
        "img_900014",
        "img_900015",
        "img_900016",
        "img_900017",
        "img_900018",
        "img_900019"
    ]

    $ phone_add_history("Sophie1", "Sophie", [
        ["cynthia", t_("Я сегодня задержусь у кузины.")],
        ["cynthia", "Ей нужно помочь с заданием по математике."],
        ["", t_("Окей. Если вечером не увидимся, завтра поболтаем :)")],
        ["cynthia", t_("Окей :)")],
    ])
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    call phone_init()
#    call phone_open()
    call phone_camera_open()

    e "You've created a new Ren'Py game."

    scene bg room
    call phone_open()

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

label remove_dialogue():
    python:
        renpy.hide_screen("say")
        renpy.hide_screen("choice")
        renpy.hide("window")
        dialogue_active_flag = False
    return
