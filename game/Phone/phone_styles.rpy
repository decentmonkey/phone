transform phone_background_fill:
    on show:
        alpha 0.0
        linear 0.2 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0

transform phone_up_down:
    on show:
        yoffset 1220
        linear 0.2 yoffset 0
    on hide:
        yoffset 0
        linear 0.2 yoffset 1220

transform camera_rotate:
#    on show:
#    alpha 0
#    pause 0.5
#    alpha 1
    yoffset 0
    ypos 170 + 886/2
    linear 0.7 rotate 90 ypos 500
#    linear 0.7 rotate 90 xalign 0.5 yalign -0.1
    on hide:
        linear 0.7 ypos 1900

transform camera_show:
    ypos 1900
    rotate 90
#    on show:
    linear 0.7 ypos 513
    on hide:
        linear 0.7 ypos 1900

transform camera_picture:
    alpha 0.0
#    on show:
#        alpha 0.0
    pause 0.7
    linear 0.5 alpha 1.0

style phone_main_icon_caption:
#    font "fonts/OpenSans-Regular.ttf"
#    font "fonts/arial.ttf"
    font "fonts/SF-Pro-Display-Regular.otf"

    size 15
    color "#ffffff"
    outlines [(3, "#000000", 0, 0)]

style phone_header1:
    color "#030304"
    size 34
    font "fonts/SF-Pro-Display-Bold.otf"

style phone_contact_name:
    color "#151516"
    size 28
    font "fonts/SF-Pro-Display-Regular.otf"

style phone_contact_name_calling:
    color "#feffff"
    size 40
    font "fonts/SF-Pro-Display-Regular.otf"

style phone_contact_name_chatting:
    color "#060606"
    size 18
    font "fonts/SF-Pro-Display-Regular.otf"

style phone_chatting_bubble_left:
    color "#000000"
    size 24
    font "fonts/SF-Pro-Display-Regular.otf"

style phone_chatting_bubble_right:
    color "#ffffff"
    size 24
    font "fonts/SF-Pro-Display-Regular.otf"


style phone_contact_name_underline:
    color "#b0b0b0"
    size 18
    font "fonts/SF-Pro-Display-Regular.otf"

style phone_contact_name_history:
    color "#151516"
    size 22
    font "fonts/SF-Pro-Display-Regular.otf"

style phone_contact_name_history_text:
    color "#b0b0b0"
    size 22
    font "fonts/SF-Pro-Display-Regular.otf"

style phone_chatting_menu_option:
    color "#060606"
    size 24
    font "fonts/SF-Pro-Display-Regular.otf"

style phone_chatting_typing:
    color "#909090"
    size 20
    font "fonts/SF-Pro-Display-Regular.otf"

style phone_gallery_pagination:
    color "#303030"
    size 46
    font "fonts/tahoma.ttf"

style phone_preferences_menu:
    color "#060606"
    size 30
    font "fonts/SF-Pro-Display-Regular.otf"

style phone_instagram_caption:
    color "#060606"
    size 14
    font "fonts/SF-Pro-Display-Bold.otf"

style phone_notes_text:
    size 32
    color "#38383a"
#    font "fonts/tahoma.ttf"
    font "fonts/baskerville_bolditalic_win95bt.ttf"

style phone_notes_category_text:
    underline True
