screen phone_gallery_screen:

    frame:
        pos(46,85)

        background None
        xmaximum 378
        text t__("Галерея") style "phone_header1":
            xpos -8
            ypos 16
    fixed:
        add "#ffffff" xsize 376 ysize 630 pos(28, 160)
        add "#c2c2c2" xsize 376 ysize 1 pos(28,160)
        add "#c2c2c2" xsize 376 ysize 1 pos(28,130+660)

    frame:
        pos(31,168)
        background None
        xmaximum 378
        hbox:
            spacing 0
            box_wrap_spacing 0
            box_wrap True
            for gal_idx in range(phone_gallery_page*phone_gallery_items_on_page, phone_gallery_page*phone_gallery_items_on_page+phone_gallery_items_on_page-1):
                if gal_idx < len(phone_gallery):
                    $ galleryImg = Transform(phone_gallery[gal_idx], size=(115,67))
                    button:
                        margin (0,0)
                        padding (0,0)
                        ypos 0
                        xpos 0
                        ysize 71
                        xsize 120
                        add galleryImg:
                            pos (0,0)
