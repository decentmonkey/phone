screen phone(phone_menu_active):
    layer "master"
    zorder 110
    button:
        background "#00000030"
        xfill True
        yfill True
        action [
            Return(["close"])
        ]
        alternate ShowMenu("save")
        at phone_background_fill

    frame:
        at phone_up_down
        pos(740,170)
        background None
        button:
            xsize 432
            ysize 886
            action [
                Return("None")
            ]
            alternate ShowMenu("save")

        if phone_menu_active == "main":
            add "/images/Phone/bg_1.png":
                pos(28,25)
            use phone_button_close()
            use phone_main()
        if phone_menu_active == "contacts":
#            add "#f8f9fa" xsize 376 ysize 130 pos(28, 25)
            add "#f8f9fa" xsize 376 ysize 812 pos(28, 25)
#            add "#ff0000" xsize 376 ysize 812 pos(28, 25)
            use phone_button_close()
            use phone_contacts()
        if phone_menu_active == "calling_screen":
            use phone_calling_screen()

        if phone_menu_active == "chat_live":
            add "#f8f9fa" xsize 376 ysize 812 pos(28, 25)
            use phone_button_close()
#            use phone_chat_live_screen()

        if phone_menu_active == "messages_list":
            add "#f8f9fa" xsize 376 ysize 812 pos(28, 25)
            use phone_button_close()
            use phone_messages_list_screen()

        if phone_menu_active == "open_history_chat":
            add "#f8f9fa" xsize 376 ysize 812 pos(28, 25)
            use phone_button_close()
            use phone_open_history_chat_screen()

        add "/images/Phone/frame.png"

screen phone_button_close():
    layer "master"
    zorder 111
    if phone_close_enabled == True:
        imagebutton:
            pos(350,42)
            idle "/images/Icons/window_close.png"
            hover im.MatrixColor("/images/Icons/window_close.png", im.matrix.brightness(0.1))
            action [
                Return(["close"])
            ]

screen phone_main():
    layer "master"
    zorder 112

    frame:
        pos(46,85)

        background None
        xmaximum 378
        hbox:
            spacing 15
            box_wrap_spacing 30
            box_wrap True
            for phone_button in phone_buttons_list:
                if phone_button["active"] == True:
                    $ idleImg = phone_button["img"]
                    if phone_buttons_new.has_key(phone_button["name"]) and phone_buttons_new[phone_button["name"]] == True:
                        $ idleImg = phone_button["img_new"]
                    $ hoveredImg = im.MatrixColor(idleImg, im.matrix.brightness(0.1))
                    frame:
                        background None
                        padding (0,0)
                        xsize 70
                        vbox:
                            imagebutton:
                                xysize (70,70)
#                                    xoffset -10
                                background None
                                idle idleImg
                                hover hoveredImg
                                focus_mask True
                                action [
                                    Return(["click_main_icon", phone_button["name"]])
                                ]
                            null height 8
                            text t__(phone_button["caption"]) style "phone_main_icon_caption":
                                xoffset 0
                                xanchor 0.5
                                xpos 0.5
                                xsize 70

screen phone_contacts():
    frame:
        pos(46,85)

        background None
        xmaximum 378
        text t__("Контакты") style "phone_header1":
            xpos -8
            ypos 16

        viewport id "vp2":
            draggable True
            xpos -24
            ypos 70
            xysize(378, 690)
            yinitial 0.0
            arrowkeys True
            mousewheel True
            vbox:
#                xpos -24
                spacing 0
                first_spacing 0
                box_wrap_spacing 0
                for contact in phone_contacts:
#                    $ contactImg = Image(contact["img"])
                    $ contactImg = Transform(contact["img"], size=(65,65))

                    button:
                        margin (0,0)
                        padding (0,0)
                        ypos 0
                        xpos 0
                        ysize 79
                        xsize 378
    #                    xpos -64

                        idle_background "#feffff"
                        hover_background "#e0e0e0"
                        add "/images/Phone/mess/bg_contact.png":
                            pos (0,0)
                        add AlphaMask(contactImg, "/images/Phone/mess/contact_circle.png"):
                            pos (8,4)
#                            xsize 65
#                            ysize 65
                        text t__(contact["caption"]) style "phone_contact_name":
                            xpos 83
                            ypos 5
                        add "/images/Phone/mess/ico1.png":
                            pos (83, 47)
                            xsize 15
                            ysize 15
                        text t__("Сообщения") style "phone_contact_name_underline":
                            xpos 102
                            ypos 43
                        action [
                            Return(["call_contact", contact["name"], contact])
                        ]
        vbar value YScrollValue("vp2") xpos 343 ypos 70 xsize 8 ysize 654


screen phone_calling_screen():
    fixed:
        add "/images/Phone/calling_screen.png":
            pos(0,-3)
        $ contactImg = Image(phone_contact["img"])
        frame:
            background None
            xpos 24
            xsize 378
            add AlphaMask(contactImg, "/images/Phone/mess/contact_circle2.png"):
                xanchor 0.5
                pos(0.5, 200)

            text t__(phone_contact["caption"]) style "phone_contact_name_calling":
                xanchor 0.5
                pos(0.5, 430)

screen phone_chat_live_screen():
    layer "master"
    zorder 111
    fixed:
        if phone_live_chat_closing == True:
            at phone_up_down

        pos(747,170)
        xmaximum 378
        add "#ffffff" xsize 376 ysize 630 pos(28, 160)
        add "#c2c2c2" xsize 376 ysize 1 pos(28,160)
        add "#c2c2c2" xsize 376 ysize 1 pos(28,130+660)
        $ contactImg = Transform(phone_contact["img"], size=(65,65))
        add AlphaMask(contactImg, "/images/Phone/mess/contact_circle.png"):
            pos (180,60)
        fixed:
            xmaximum 378
            xpos 24
            text t__(phone_contact["caption"]) style "phone_contact_name_chatting":
                xanchor 0.5
                pos(0.5, 130)

        viewport id "vp1":
            draggable True
            xpos 35
            ypos 161
            xysize(352, 629)
            yinitial 1.0
            arrowkeys True
            mousewheel True
            yminimum 629
            frame:
                # изображение пустого экрана
                background None
#                yfill True
                xminimum 352
                xmaximum 352
                yminimum 629
                top_padding 0
                vbox:
                    spacing 10
                    xfill True
                    yanchor 1.0
                    yalign 1.0
                    for chat_line in phone_current_chat:
                        if chat_line[0] == "" or chat_line[0] == "bardie" or chat_line[0] == "bardie_t":
                            # говорим мы
                            button:
                                xalign 1.1
                                background Frame("smsright", 60, 38)
                                left_padding 20
                                right_padding 20
                                top_padding 10
                                bottom_padding 10
                                if chat_line[1] == "image":
                                    add chat_line[2]:
                                        xsize 250
                                        fit "cover"
                                else:
                                    text t__(chat_line[1]) style "phone_chatting_bubble_right":
    #                                    justify True
                                        xmaximum 250
                        else:
                            button:
                                xalign 0.0
                                background Frame("smsleft", 60, 38)
                                left_padding 20
                                right_padding 20
                                top_padding 10
                                bottom_padding 10
                                if chat_line[1] == "image":
                                    add chat_line[2]:
                                        xsize 250
                                        fit "cover"
                                else:
                                    text t__(chat_line[1]) style "phone_chatting_bubble_left":
#                                    justify True
                                        xmaximum 250
                    null ysize 10



        vbar value YScrollValue("vp1") xpos 397 ypos 161 xsize 8 ysize 629

screen phone_messages_list_screen():
    frame:
        pos(46,85)

        background None
        xmaximum 378
        text t__("История") style "phone_header1":
            xpos -8
            ypos 16

        viewport id "vp3":
            draggable True
            xpos -24
            ypos 70
            xysize(378, 690)
            yinitial 0.0
            arrowkeys True
            mousewheel True
            vbox:
#                xpos -24
                spacing 0
                first_spacing 0
                box_wrap_spacing 0
                for history_cell in phone_chat_history:
                    $ contact_caption = ""
                    $ contact_name = ""
                    for contact in phone_contacts:
                        if contact["name"] == history_cell["contact_name"]:
                            $ contact_caption = contact["caption"]
                    $ message = ""
                    if len(history_cell["chat_content"]) > 0:
                        $ message = t__(history_cell["chat_content"][0][1])
                        if len(message) > 30:
                            $ message = message[:30] + "..."
                    $ contactImg = Transform(contact["img"], size=(28,28))
                    $ contactImgCircle = Transform("/images/Phone/mess/contact_circle.png", size=(28,28))
                    button:
                        margin (0,0)
                        padding (0,0)
                        ypos 0
                        xpos 0
                        ysize 79
                        xsize 378
    #                    xpos -64

                        idle_background "#feffff"
                        hover_background "#e0e0e0"
                        add "/images/Phone/mess/bg_contact.png":
                            pos (0,0)
                        add AlphaMask(contactImg, contactImgCircle):
#                        add contactImg:
                            pos (18,9)
                        text t__(contact_caption) style "phone_contact_name_history":
                            xpos 56
                            ypos 10
                        text t__(message) style "phone_contact_name_history_text":
                            xpos 18
                            ypos 42
                            xmaximum 370 - 42
                        action [
                            Return(["open_history_chat", history_cell["contact_name"], history_cell])
                        ]
        vbar value YScrollValue("vp3") xpos 343 ypos 70 xsize 8 ysize 654


screen phone_open_history_chat_screen():
    fixed:
        xmaximum 378
        add "#ffffff" xsize 376 ysize 630 pos(28, 160)
        add "#c2c2c2" xsize 376 ysize 1 pos(28,160)
        add "#c2c2c2" xsize 376 ysize 1 pos(28,130+660)
        $ contactImg = Transform(phone_contact["img"], size=(65,65))
        add AlphaMask(contactImg, "/images/Phone/mess/contact_circle.png"):
            pos (180,60)
        fixed:
            xmaximum 378
            xpos 24
            text t__(phone_contact["caption"]) style "phone_contact_name_chatting":
                xanchor 0.5
                pos(0.5, 130)

        viewport id "vp4":
            draggable True
            xpos 35
            ypos 161
            xysize(352, 629)
            yinitial 0.0
            arrowkeys True
            mousewheel True
            yminimum 629
            frame:
                # изображение пустого экрана
                background None
#                yfill True
                xminimum 352
                xmaximum 352
                yminimum 629
                top_padding 0
                vbox:
                    spacing 10
                    xfill True
                    yanchor 1.0
                    yalign 1.0
                    null ysize 20
                    for chat_line in phone_current_chat:
                        if chat_line[0] == "" or chat_line[0] == "bardie" or chat_line[0] == "bardie_t":
                            # говорим мы
                            button:
                                xalign 1.1
                                background Frame("smsright", 60, 38)
                                left_padding 20
                                right_padding 20
                                top_padding 10
                                bottom_padding 10
                                if chat_line[1] == "image":
                                    add chat_line[2]:
                                        xsize 250
                                        fit "cover"
                                else:
                                    text t__(chat_line[1]) style "phone_chatting_bubble_right":
    #                                    justify True
                                        xmaximum 250
                        else:
                            button:
                                xalign 0.0
                                background Frame("smsleft", 60, 38)
                                left_padding 20
                                right_padding 20
                                top_padding 10
                                bottom_padding 10
                                if chat_line[1] == "image":
                                    add chat_line[2]:
                                        xsize 250
                                        fit "cover"
                                else:
                                    text t__(chat_line[1]) style "phone_chatting_bubble_left":
#                                    justify True
                                        xmaximum 250
                    null ysize 10



        vbar value YScrollValue("vp4") xpos 397 ypos 161 xsize 8 ysize 629

#
