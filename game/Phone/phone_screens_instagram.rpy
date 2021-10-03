screen phone_instagram_screen():
    fixed:
        add "#ffffff" xsize 376 ysize 571 pos(28, 100)
        add "#c2c2c2" xsize 376 ysize 1 pos(28,100)
    viewport id "vp8":
        draggable True
        xpos 28
        ypos 95
        xysize(380, 742)
        yinitial 0.0
        arrowkeys True
        mousewheel True
        vbox:
            spacing 0
            first_spacing 0
            box_wrap_spacing 0
            for post in phone_instagram_posts:
                $ instagramPost = Image(post[0])
                $ imgSize = getImageSize(instagramPost, post[0])
                $ postWidth = 368
                $ postHeight = int(imgSize[1] * (imgSize[0]/postWidth))
                button:
                    margin (0,0)
                    padding (0,0)
                    ypos 0
                    xpos 0
                    xsize 380
                    ysize postHeight
                    background None
                    add post[0]:
                        xsize postWidth
                        ysize postHeight
                    if len(post)>1:
                        frame:
                            xmaximum 348
                            yminimum 50
                            background "#ffffff"
                            pos(10,485)
                            text t__(post[1]) style "phone_instagram_caption":
                                pos(0, 0.5)
                                yanchor 0.5
                                line_spacing 3
                    action [
                        Return([False])
                    ]

    vbar value YScrollValue("vp8") xpos 396 ypos 96 xsize 8 ysize 730
