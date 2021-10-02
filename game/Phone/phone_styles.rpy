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
