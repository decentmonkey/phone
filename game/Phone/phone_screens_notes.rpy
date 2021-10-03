screen phone_notes_screen():
    fixed:
        viewport id "vp9":
            draggable True
            xpos 28
            ypos 95
            xysize(380, 742)
            yinitial 0.0
            arrowkeys True
            mousewheel True
            frame:
                padding (20,10)
                background None
                xsize 368
                text "Test: gdggdfg rlgkerlk regklerglk lergkelrk {s}gergre{/s}" style "phone_notes_text"

    vbar value YScrollValue("vp9") xpos 396 ypos 96 xsize 8 ysize 730
