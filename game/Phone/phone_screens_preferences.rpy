screen phone_preferences_rrmeter():
    fixed:
        $ barValue = float(rrmeter + 50)/100
        if barValue >= 0.5:
            bar:
                xpos 170
                ypos 220
                value AnimatedValue(barValue, 1.0, 1.0, barValue)
                xoffset 5
                xysize (69,327)
                bar_vertical True
                top_bar "/icons/bar/bar_empty.png"
                bottom_bar "/icons/bar/bar_full.png"
                thumb "/icons/bar/bar_thumb.png"
                bottom_gutter 15
                top_gutter 18
                thumb_offset 22
        else:
            bar:
                xpos 170
                ypos 220
                value AnimatedValue(barValue, 1.0, 1.0, barValue)
                xoffset 5
                xysize (69,327)
                bar_vertical True
                top_bar "/icons/bar/bar3_empty.png"
                bottom_bar "/icons/bar/bar3_full.png"
                thumb "/icons/bar/bar3_thumb.png"
                bottom_gutter 15
                top_gutter 18
                thumb_offset 22

        add "/images/Phone/rrmeter_rabbit.png":
            pos(230,187)
        add "/images/Phone/rrmeter_rat.png":
            pos(120,460)

screen phone_preferences_backgrounds():
    frame:
        pos(46,85)

        background None
        xmaximum 378
        text t__("Фон") style "phone_header1":
            xpos -8
            ypos 16
    fixed:
        add "#ffffff" xsize 376 ysize 571 pos(28, 160)
        add "#c2c2c2" xsize 376 ysize 1 pos(28,160)
        add "#c2c2c2" xsize 376 ysize 1 pos(28,130+600)

    frame:
        pos(46,86)
        background None
        xmaximum 378
        viewport id "vp6":
            draggable True
            xpos 10
            ypos 70
            xysize(378, 568)
            yinitial 0.0
            arrowkeys True
            mousewheel True
            hbox:
                spacing 0
                box_wrap_spacing 0
                box_wrap True
                for background_idx in range(0, len(phone_backgrounds_list)):
                    frame:
                        background None
                        margin (0,0)
                        padding (0,0)
                        ypos 0
                        xpos 0
                        xsize 180
                        ysize 240
                        button:
                            background "#ffffff"
                            hover_background "#e0e0e0"
                            margin (0,0)
                            padding (0,0)
                            ypos 20
                            xpos 0
                            ysize 220
                            xsize 120
                            add phone_backgrounds_list[background_idx]:
                                pos (15,11)
                                xsize 90
                                ysize 195
                                #2,16533333
                            action [
                                Return(["preferences_backgrounds_select", background_idx])
                            ]

        vbar value YScrollValue("vp6") xpos 343 ypos 70 xsize 8 ysize 568


#
