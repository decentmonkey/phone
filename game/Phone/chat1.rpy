label cynthia_chat1:
    $ phone_start_new_chat("cynthia1", "Cynthia")
    $ chat = [
        ["cynthia", t_("[mcname], как дела? Ты еще в колледже?")],
        ["cynthia", "image", "/images/Phone/insta/1.jpg", 2],
        ["", t_("Привет. Да, еще в колледже.")],
        ["", t_("Скоро буду дома. А ты где?")],
        ["cynthia", t_("Я сегодня задержусь у кузины.")],
        ["cynthia", t_("Ей нужно помочь с заданием по математике.")],
        ["", t_("Окей. Если вечером не увидимся, завтра поболтаем :)")],
        ["cynthia", t_("Окей :)")]
    ]
    call phone_chat(chat)
    pause
    m "chat_end"
    return
    cynthia "[mcname], как дела? Ты еще в колледже?"
    menu:
        "Ответить.":
            menu:
                "Я еще в колледже.":
#                    sound iphone_typing
                    bardi "Привет. Да, еще в колледже."
                    bardi "А ты где?"
                    pass
                "Уже освободился.":
#                    sound iphone_typing
                    bardi "Привет. Уже освободился."
                    bardi "Скоро буду дома. А ты где?"
                    pass
#            sound iphone_text_message2
            cynthia "Я сегодня задержусь у кузины."
            cynthia "Ей нужно помочь с заданием по математике."
#            sound iphone_typing
            bardi "Окей. Если вечером не увидимся, завтра поболтаем :)"
#            sound iphone_text_message2
            cynthia "Окей :)"
            return
        "Не отвечать.":
            bardi_t "Позже ей отвечу."
            return

    m "here"
    return
