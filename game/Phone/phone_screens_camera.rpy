screen phone_camera_screen(phone_camera_image):
    tag phone
    layer "master"
    zorder 130
    button:
        background "#00000030"
        xfill True
        yfill True
        action [
            Return(["close"])
        ]
        alternate ShowMenu("save")
    frame:
        at camera_rotate
        pos(740+432/2,170 + 886/2)
        background None
        xysize(432,886)
        xanchor(0.5)
        yanchor(0.5)
        button:
            xsize 432
            ysize 886
            action [
                Return("None")
            ]
            alternate ShowMenu("save")

        fixed:
            pos (28,22)
            add "/images/Phone/bg_photo.png"

            imagebutton:
                pos(150,700)
                idle "/images/Phone/icons/photo_button.png"
                hover "/images/Phone/icons/photo_button_hover.png"
                action [
                    Return(["camera_shoot"])
                ]
            add phone_get_gallery_image_path(phone_camera_image):
                xsize 645
                ysize 380
                pos(190, 330)
                xanchor 0.5
                yanchor 0.5
                rotate -90
                at camera_picture
        imagebutton:
            pos(45,42)
            idle "/images/Icons/window_close.png"
            hover im.MatrixColor("/images/Icons/window_close.png", im.matrix.brightness(0.1))
            action [
                Return(["close"])
            ]
        add "/images/Phone/frame.png"


screen phone_camera_screen2(phone_camera_image):
    tag phone
    layer "master"
    zorder 130
    button:
        background "#00000030"
        xfill True
        yfill True
        action [
            Return(["close"])
        ]
        alternate ShowMenu("save")
    frame:
        at camera_show
        pos(740+432/2,170 + 886/2)
        background None
        xysize(432,886)
        xanchor(0.5)
        yanchor(0.5)
        button:
            xsize 432
            ysize 886
            action [
                Return("None")
            ]
            alternate ShowMenu("save")

        fixed:
            pos (28,22)
            add "/images/Phone/bg_photo.png"

            imagebutton:
                pos(150,700)
                idle "/images/Phone/icons/photo_button.png"
                hover "/images/Phone/icons/photo_button_hover.png"
                action [
                    Return(["camera_shoot"])
                ]
            add phone_get_gallery_image_path(phone_camera_image):
                xsize 645
                ysize 380
                pos(190, 330)
                xanchor 0.5
                yanchor 0.5
                rotate -90
                at camera_picture
        imagebutton:
            pos(45,42)
            idle "/images/Icons/window_close.png"
            hover im.MatrixColor("/images/Icons/window_close.png", im.matrix.brightness(0.1))
            action [
                Return(["close"])
            ]
        add "/images/Phone/frame.png"
