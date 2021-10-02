screen phone_gallery_screen:

    frame:
        pos(46,85)

        background None
        xmaximum 378
        text t__("Галерея") style "phone_header1":
            xpos -8
            ypos 16
    fixed:
        add "#ffffff" xsize 376 ysize 571 pos(28, 160)
        add "#c2c2c2" xsize 376 ysize 1 pos(28,160)
        add "#c2c2c2" xsize 376 ysize 1 pos(28,130+600)

    frame:
        pos(31,168)
        background None
        xmaximum 378
        hbox:
            spacing 0
            box_wrap_spacing 0
            box_wrap True
            for gal_idx in range(phone_gallery_page*phone_gallery_items_on_page, phone_gallery_page*phone_gallery_items_on_page+phone_gallery_items_on_page):
                if gal_idx < len(phone_gallery):
                    $ galleryImg = Transform(phone_get_gallery_image_path(phone_gallery[gal_idx]), size=(175,103))
                    button:
                        margin (0,0)
                        padding (0,0)
                        ypos 0
                        xpos 0
                        ysize 110
                        xsize 180
                        add galleryImg:
                            pos (0,0)
                        action [
                            Return(["open_gallery_image", gal_idx])
                        ]
    fixed:
        pos(28,130+601)
        imagebutton:
            pos(65, 20)
            idle "/images/Phone/phone_arrow_left.png"
            hover im.MatrixColor("/images/Phone/phone_arrow_left.png", im.matrix.brightness(0.1))
            action [
                Return (["gallery_pagination", "left"])
            ]
        $ rightArrow = Transform(im.MatrixColor("/images/Phone/phone_arrow_left.png", im.matrix.brightness(0.1)), xzoom=-1)
        imagebutton:
            pos (240, 20)
            idle Transform("/images/Phone/phone_arrow_left.png", xzoom=-1)
            hover rightArrow
            action [
                Return (["gallery_pagination", "right"])
            ]
        text str(phone_gallery_page+1) style "phone_gallery_pagination":
            pos(185,17)
            xanchor 0.5

screen phone_gallery_image_screen(gallery_image):
    layer "master"
    zorder 130
    add gallery_image
    
