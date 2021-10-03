default phone_max_typing_time = 3.0
default phone_default_image_typing_time = 2.0
default phone_pause_before_typing_time = 1.0
default phone_buttons_list = []
default phone_buttons_new = {}
default phone_menu_active = "main"
default phone_chat_history = []
default phone_chat_history_new_flags = {}
default phone_contact = False
default phone_current_chat = []
default phone_current_chat_name = False
default phone_typing = False
default phone_typing_name = False
default phone_close_enabled = True
default phone_live_chat_closing = False
default phone_gallery = []
default phone_gallery_page = 0
default phone_gallery_items_on_page = 10
default phone_last_contacts_count = 0
default phone_orientation = 0
default phone_camera_image = False
default phone_background = 0
default phone_backgrounds_list = []
default phone_preferences_list = []
default phone_instagram_posts = []
#history:
# [{"chat_name":name, "contact_name":contact_name, "chat_content":[]}]
# chat format:
# ["speaker", "message", pause]

# phone_add_history(chat_name, contact_name, chat_list)
# phone_set_new(menu_name)
# call phone_open() - открывается на главном меню
# call phone_open_menu(menu_name) - открывается на определенном меню
# call phone_hide() - закрывается
# call phone_camera_open() - открывается в режиме камеры
label phone_open:
    $ phone_menu_active = "main"
    $ phone_orientation = 0
    call phone_controller()
    return

label phone_open_menu(menu_active):
    $ phone_menu_active = "main"
    $ phone_orientation = 0
    call phone_controller()
    return

label phone_hide:
    hide screen phone
    return

label phone_camera_open:
    $ phone_menu_active = "camera"
    $ phone_orientation = 1
    $ phone_camera_image = phone_camera_get_current_image()
    show screen phone_camera_screen2(phone_camera_image)
label phone_camera_open_loop1:
    $ interact_data = None
    $ interact_data = ui.interact()
    if interact_data != None and interact_data != False:
        if interact_data[0] == "close":
            hide screen phone_camera_screen2
            return
        if interact_data[0] == "camera_shoot":
            python:
                if phone_camera_image in phone_gallery:
                    phone_gallery.remove(phone_camera_image)
                phone_gallery.insert(0, phone_camera_image)
            m "shoot!"
            hide screen phone_camera_screen2
            return

    jump phone_camera_open_loop1

label phone_init:
    $ phone_buttons_new = {
        "contacts": False,
        "messages": False,
        "gallery": True,
        "notes": False,
        "camera": False,
        "instagram": True,
        "preferences": False
    }
    $ phone_contacts = [
        {"name": "Sophie", "caption":t_("Sophie"), "img":"/images/Phone/contacts/Contacts_Sophie.png"},
        {"name": "Sean", "caption":t_("Sean"), "img":"/images/Phone/contacts/Contacts_Sean.png"},
        {"name": "Olivia", "caption":t_("Sophie"), "img":"/images/Phone/contacts/Contacts_Olivia.png"},
        {"name": "Cynthia", "caption":t_("Cynthia"), "img":"/images/Phone/contacts/Contacts_Cynthia.png"}
    ]

    $ phone_buttons_list = [
        {"name": "contacts", "caption": "Contacts", "img":"/images/Phone/icons/contacts.png", "img_new":"/images/Phone/icons/contacts_new.png", "active":True},
        {"name": "messages", "caption": "Messages",  "img":"/images/Phone/icons/messager.png", "img_new":"/images/Phone/icons/messager_new.png", "active":True},
        {"name": "gallery", "caption": "  Photos",  "img":"/images/Phone/icons/gal.png", "img_new":"/images/Phone/icons/gal_new.png", "active":True},
        {"name": "notes", "caption": "  Notes",  "img":"/images/Phone/icons/notes.png", "img_new":"/images/Phone/icons/notes_new.png", "active":True},
        {"name": "camera", "caption": "  Camera",  "img":"/images/Phone/icons/photo.png", "img_new":"/images/Phone/icons/photo_new.png", "active":True},
        {"name": "instagram", "caption": " Instagram",  "img":"/images/Phone/icons/instagram.png", "img_new":"/images/Phone/icons/instagram_new.png", "active":True},
        {"name": "preferences", "caption": "Preferences",  "img":"/images/Phone/icons/preferens.png", "img_new":"/images/Phone/icons/preferens_new.png", "active":True}
#        {"name": "contacts", "caption": t_("Контакты"), "img":"/images/Phone/icons/contacts.png", "img_new":"/images/Phone/icons/contacts_new.png", "active":True},
#        {"name": "messages", "caption": t_("Сообщения"),  "img":"/images/Phone/icons/messager.png", "img_new":"/images/Phone/icons/messager_new.png", "active":True},
#        {"name": "gallery", "caption": t_("Галерея"),  "img":"/images/Phone/icons/gal.png", "img_new":"/images/Phone/icons/gal_new.png", "active":True},
#        {"name": "notes", "caption": t_("Блокнот"),  "img":"/images/Phone/icons/notes.png", "img_new":"/images/Phone/icons/notes_new.png", "active":True},
#        {"name": "camera", "caption": t_("Камера"),  "img":"/images/Phone/icons/photo.png", "img_new":"/images/Phone/icons/photo_new.png", "active":True},
#        {"name": "instagram", "caption": t_("Инстаграм"),  "img":"/images/Phone/icons/instagram.png", "img_new":"/images/Phone/icons/instagram_new.png", "active":True},
#        {"name": "preferences", "caption": t_("Настройки"),  "img":"/images/Phone/icons/preferens.png", "img_new":"/images/Phone/icons/preferens_new.png", "active":True}
    ]
    $ phone_preferences_list = [
        {"name":"preferences_rrmeter", "caption": t_("RR Meter")},
        {"name":"preferences_backgrounds", "caption": t_("Изменить фон")}
    ]
    $ phone_backgrounds_list = [
        "/images/Phone/bg_1.png",
        "/images/Phone/option/bg_2.png"
    ]

    return

label phone_controller:

label phone_open_loop1:
    window hide
    call remove_dialogue()

    python:
        # check new history messages
        for history_flag in phone_chat_history_new_flags:
            if phone_chat_history_new_flags[history_flag] == True:
                phone_buttons_new["messages"] = True
            else:
                phone_buttons_new["messages"] = False

        # check new contacts
        if phone_last_contacts_count != len(phone_contacts):
            phone_buttons_new["contacts"] = True
        else:
            phone_buttons_new["contacts"] = False

    if phone_menu_active != "camera":
        show screen phone(phone_menu_active)
    $ interact_data = None
    $ interact_data = ui.interact()
    if interact_data != None and interact_data != False:
        if interact_data[0] == "click_main_icon":
            if interact_data[1] == "contacts":
                $ phone_menu_active = "contacts"
                $ phone_last_contacts_count = len(phone_contacts)
#                $ phone_buttons_new["contacts"] = False
                jump phone_open_loop1
            if interact_data[1] == "messages":
#                $ phone_buttons_new["messages"] = False
                $ phone_menu_active = "messages_list"
                jump phone_open_loop1
            if interact_data[1] == "gallery":
                $ phone_menu_active = "gallery"
                $ phone_gallery_page = 0
                jump phone_open_loop1
            if interact_data[1] == "camera":
                $ phone_menu_active = "camera"
                $ phone_orientation = 1
                $ phone_camera_image = phone_camera_get_current_image()
#                hide screen phone
#                show screen phone_camera_screen()
                show screen phone_camera_screen(phone_camera_image)
                jump phone_open_loop1
            if interact_data[1] == "preferences":
                $ phone_menu_active = "preferences_menu"
                jump phone_open_loop1
            if interact_data[1] == "instagram":
                $ phone_menu_active = "instagram"
                jump phone_open_loop1
            if interact_data[1] == "notes":
                $ phone_menu_active = "notes"
                jump phone_open_loop1

        if interact_data[0] == "close":
            if phone_menu_active == "main" or phone_menu_active == "chat_live":
                hide screen phone
                hide screen phone_chat_live_screen
                return
            if phone_menu_active == "contacts" or phone_menu_active == "preferences_menu" or phone_menu_active == "preferences_backgrounds" or phone_menu_active == "instagram" or phone_menu_active == "notes" or phone_menu_active=="preferences_rrmeter":
                $ phone_menu_active = "main"
                jump phone_open_loop1
            if phone_menu_active == "messages_list":
                $ phone_menu_active = "main"
                jump phone_open_loop1
            if phone_menu_active == "open_history_chat":
                $ phone_menu_active = "messages_list"
                jump phone_open_loop1
            if phone_menu_active == "gallery":
                $ phone_menu_active = "main"
                jump phone_open_loop1

            if phone_menu_active == "camera":
                hide screen phone_camera_screen
                return
#                $ phone_menu_active = "main"
#                jump phone_open_loop1


        if interact_data[0] == "call_contact":
            $ obj_name = interact_data[1]
            $ phone_contact = interact_data[2]
            $ phone_menu_active = "calling_screen"
            show screen phone(phone_menu_active)
            pause 2.0
#            call process_hooks("call_contact", "phone")
            $ phone_current_chat = []
            call cynthia_chat1()
            jump phone_open_loop1

        if interact_data[0] == "open_history_chat":
            if phone_chat_history_new_flags.has_key(interact_data[2]["chat_name"]):
                $ phone_chat_history_new_flags[interact_data[2]["chat_name"]] = False
            $ phone_contact = phone_get_contact_by_contact_name(interact_data[1])
            $ phone_current_chat = interact_data[2]["chat_content"]
            $ phone_menu_active = "open_history_chat"
            jump phone_open_loop1

        if interact_data[0] == "gallery_pagination":
            if interact_data[1] == "left" and phone_gallery_page > 0:
                $ phone_gallery_page -= 1
            if interact_data[1] == "right" and len(phone_gallery) - (phone_gallery_page+1)*phone_gallery_items_on_page > 0:
                $ phone_gallery_page += 1
            jump phone_open_loop1

        if interact_data[0] == "open_gallery_image":
            $ galleryImagePath = phone_get_gallery_image_path(phone_gallery[interact_data[1]])
            if galleryImagePath != False:
                show screen phone_gallery_image_screen(galleryImagePath)
#                with fade
                pause
                hide screen phone_gallery_image_screen
            jump phone_open_loop1

        if interact_data[0] == "preferences_rrmeter":
            $ phone_menu_active = "preferences_rrmeter"
            jump phone_open_loop1

        if interact_data[0] == "preferences_backgrounds":
            $ phone_menu_active = "preferences_backgrounds"
            jump phone_open_loop1

        if interact_data[0] == "preferences_backgrounds_select":
            $ phone_background = interact_data[1]
            $ phone_menu_active = "main"
            jump phone_open_loop1



    jump phone_open_loop1

label phone_chat(chat):
    window hide
    call remove_dialogue()
    $ phone_menu_active = "chat_live"
    $ chat_line_idx = 0
    $ phone_close_enabled = False
    $ phone_live_chat_closing = False
    show screen phone(phone_menu_active)
label phone_chat_loop1:
    $ chat_line = chat[chat_line_idx]
    python:
        if chat_line[1] != "image":
            message_pause = float(len(chat_line[1])) * 0.1
        else:
            message_pause = phone_default_image_typing_time
        if message_pause > phone_max_typing_time:
            message_pause = phone_max_typing_time
        if len(chat_line) > 2 and chat_line[1] != "image":
            message_pause = float(chat_line[2])
        if len(chat_line) > 3 and chat_line[1] == "image":
            message_pause = float(chat_line[3])

        if chat_line_idx == 0 and chat_line[0] != "" and chat_line[0] != "bardie" and chat_line[0] != "bardie_t":
            message_pause = 0.3
        phone_typing = True

    if chat_line[0] == "" or chat_line[0] == "bardie" or chat_line[0] == "bardie_t":
#        sound iphone_typing
        $ phone_typing_name = "[mcname]"
        pass
    else:
        $ phone_typing_name = phone_contact["caption"]
    hide screen phone_chat_live_screen
    show screen phone_chat_live_screen()
    pause float(message_pause)
    if chat_line[0] != "" and chat_line[0] != "bardie" and chat_line[0] != "bardie_t":
#        sound iphone_text_message2
        pass
    $ phone_typing = False
    $ phone_current_chat.append(chat_line)
    $ phone_add_history_line(phone_current_chat_name, chat_line)
    hide screen phone_chat_live_screen
    show screen phone_chat_live_screen()
    pause float(phone_pause_before_typing_time)
    $ chat_line_idx += 1
    if chat_line_idx < len(chat):
        jump phone_chat_loop1

    $ phone_close_enabled = True
    return
label phone_chat_loop2:
    show screen phone(phone_menu_active)
    $ interact_data = None
    $ interact_data = ui.interact()
    if interact_data != None and interact_data != False:
        if interact_data[0] == "close":
            $ phone_live_chat_closing = True
            hide screen phone
            hide screen phone_chat_live_screen
            return
    jump phone_chat_loop2
    return

label phone_chat_menu(chat_menu):
    $ phone_close_enabled = False
    call screen phone_live_chat_menu_screen(chat_menu)
    $ phone_close_enabled = True
    return _return


init python:
    def phone_start_new_chat(chat_name, contact_name):
        global phone_chat_history, phone_current_chat_name
        for idx in range(0, len(phone_chat_history)):
            if phone_chat_history[idx]["chat_name"] == chat_name:
                # нашли такой же чат, удаляем
                del phone_chat_history[idx]
        new_chat = {"chat_name": chat_name, "contact_name": contact_name, "chat_content":[]}
        phone_chat_history.insert(0, new_chat)
        phone_current_chat_name = chat_name
        return

    def phone_add_history_line(chat_name, chat_line):
        global phone_chat_history
        for idx in range(0, len(phone_chat_history)):
            if phone_chat_history[idx]["chat_name"] == chat_name:
                phone_chat_history[idx]["chat_content"].append(chat_line)
        return

    def phone_add_history(chat_name, contact_name, chat_list):
        global phone_chat_history, phone_chat_history_new_flags
        for idx in range(0, len(phone_chat_history)):
            if phone_chat_history[idx]["chat_name"] == chat_name:
                # нашли такой же чат, удаляем
                del phone_chat_history[idx]
        new_chat = {"chat_name": chat_name, "contact_name": contact_name, "chat_content":chat_list}
        phone_chat_history.insert(0, new_chat)
        phone_chat_history_new_flags[chat_name] = True
        return



    def phone_get_contact_by_contact_name(contact_name):
        global phone_contacts
        for contact in phone_contacts:
            if contact["name"] == contact_name:
                return contact

    def phone_set_new(menu_name):
        global phone_buttons_new
        if phone_buttons_new.has_key(menu_name):
            phone_buttons_new[menu_name] = True
        return

    def phone_get_gallery_image_path(image_name):
        return image_name

    def phone_camera_get_current_image():
        return "/images/Slides/img_900002.jpg"

#
