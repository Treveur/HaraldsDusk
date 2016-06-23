# Ce fichier est dans le domaine public. N'hésitez pas à la modifier pour vos
# propres écrans

##############################################################################
# Dialogues
#
# Écrans utilisés pour le mode ADV
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Valeurs par défaut de 'side_image' et 'two_window'
    default side_image = None
    default two_window = False

    # Options selon le que l'on soit en mode une fenêtre ou deux fenêtres.
    if not two_window:

        # Cas avec une fenêtre.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # Cas avec deux fenêtres.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # Si il y a une image latérale, on la montre au dessus du texte.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.065 yalign 0.9615

    # Utilisation du menu rapide.
    # use quick_menu

    #Utilisation du menu ingame
    use ingame_menu


##############################################################################
# Choix
#
# Écran utilisé pour les menus au sein du jeu
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 5

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "cm_button"

                        text caption style "cm_button_text"

                else:
                    text caption style "menu_caption"

    #Utilisation du menu ingame
    use ingame_menu

init -2 python:
    config.narrator_menu = True

    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)
    #style.menu_choice.font="FILE NAME HERE"


##############################################################################
# Entrée
#
# Écran utilisé lors de l'utilisation de renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    # use quick_menu

##############################################################################
# Nvl
#
# Écran utilisé pour les dialogues et les menus en mode NVL
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Affiche un dialogue
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Affiche un menu si il y en a un
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    # use quick_menu

##############################################################################
# Menu principal
#
# Écran utilisé pour le menu principal, quand Ren'Py démarre
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    # Pour être sûr que tout autre menu est remplacé
    tag menu

    # Le fond du menu principal
    window:
        style "mm_root"

    vbox:
        spacing 20
        xalign 0.5
        yalign 0.7

        button:
            style "mm_button"
            text "Start Game" style "mm_button_text"
            action ShowMenu("choose_lenght")

        button:
            style "mm_button"
            text "Charger" style "mm_button_text"
            action ShowMenu("load")

        button:
            style "mm_button"
            text "Options" style "mm_button_text"
            action ShowMenu("preferences")

        button:
            style "mm_button"
            text "Quit" style "mm_button_text"
            action Quit()



init -2 python:

    # Donne la même taille à tous les boutons du menu.
    style.mm_button.size_group = "mm"


##############################################################################
# Navigation
#
# Écran inclue dans d'autres écrans pour afficher le menu jeu,
# et le fond.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # Fond du menu jeu
    window:
        style "gm_root"

    vbox:
        spacing 20
        xalign 0.745
        yalign 0.5

        button:
            style "gm_button"
            text "Return" style "mm_button_text"
            action Return()

        button:
            style "gm_button"
            text "Options" style "mm_button_text"
            action ShowMenu("preferences")

        button:
            style "gm_button"
            text "Sauvegarder" style "mm_button_text"
            action ShowMenu("save")

        button:
            style "gm_button"
            text "Charger" style "mm_button_text"
            action ShowMenu("load")

        button:
            style "gm_button"
            text "Main Menu" style "mm_button_text"
            action MainMenu()

        button:
            style "gm_button"
            text "Quit" style "mm_button_text"
            action Quit()

        # has vbox
        #
        # textbutton _("Return") action Return()
        # textbutton _("Text History") action [SetVariable("yvalue", 1.0), ShowMenu('text_history')]
        # textbutton _("Preferences") action ShowMenu("preferences")
        # textbutton _("Save Game") action ShowMenu("save")
        # textbutton _("Load Game") action ShowMenu("load")
        # textbutton _("Main Menu") action MainMenu()
        # textbutton _("Help") action Help()
        # #Enlever confirm=False pour la build final
        # textbutton _("Quit") action Quit(confirm=False)

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"


##############################################################################
# Sauvegarder, Charger
#
# Écrans permettant à l'utilisateur de sauvegarder ou charger un jeu
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Puisque la sauvegarde et le chargement sont deux actions proches
# nous utilisons un seul écran pour les deux. On utilise un l'écran
# file_picker depuis les écrans de sauvegarde et et de chargement.

screen file_picker:

    $ columns = 4
    $ rows = 2
    $ k = 0

    #Display a grid of file slots.
    #grid columns rows:
    vbox:
        spacing 50
        for j in range (1,5):
            hbox:
                xpos 150
                ypos 40

                spacing 50

                # Display ten file slots, numbered 1 - 10.
                for i in range (1,3):
                    $ k = k + 1
                    button:
                        style "sm_button"
                        action FileAction(k)

                        has vbox spacing 50

                        add FileScreenshot(k) size(192,108) ypos 20 xpos 37

                        $ file_name = FileSlotName(k, columns * rows)
                        $ file_time = FileTime(k, empty=_("Empty Slot"))
                        $ save_name = FileSaveName(k)

                        text "[file_name]. [file_time!t]\n" xpos 37

    # frame:
    #     style "file_picker_frame"
    #
    #     has vbox
    #
    #     # Les boutons en haut permettent à l'utilisateur
    #     # de sélectionner une page de fichiers.
    #     hbox:
    #         style_group "file_picker_nav"
    #
    #         textbutton _("Previous"):
    #             action FilePagePrevious()
    #
    #         textbutton _("Auto"):
    #             action FilePage("auto")
    #
    #         for i in range(1, 3):
    #             textbutton str(i):
    #                 action FilePage(i)
    #
    #         textbutton _("Next"):
    #             action FilePageNext()
    #
    #     $ columns = 1
    #     $ rows = 3
    #
    #     # Affiche une grille d'emplacements de sauvegarde
    #     grid columns rows:
    #         transpose True
    #         xfill True
    #         style_group "file_picker"
    #
    #         # Montre dix emplacements, numérotés de 1 à 10.
    #         for i in range(1, columns * rows + 1):
    #
    #             # Chaque emplacement est un bouton.
    #             button:
    #                 action FileAction(i)
    #                 xfill True
    #
    #                 has hbox
    #
    #                 # Ajoute un screenshot.
    #                 add FileScreenshot(i)
    #
    #                 $ file_name = FileSlotName(i, columns * rows)
    #                 $ file_time = FileTime(i, empty=_("Empty Slot."))
    #                 $ save_name = FileSaveName(i)
    #
    #                 text "[file_name]. [file_time!t]\n[save_name!t]"
    #
    #                 key "save_delete" action FileDelete(i)

screen save:

    # Pour être sûr que tout autre menu est remplacé.
    tag menu

    use navigation
    use file_picker

screen load:

    # Pour être sûr que tout autre menu est remplacé.
    tag menu

    use navigation
    use file_picker

init -2 python:
    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)

##############################################################################
# Longueur histoire
#
# Écrans permettant à l'utilisateur de choisir la longueur de la VN

screen choose_lenght:
    tag menu

    # Le fond du menu principal
    window:
        style "mm_root"

    vbox:
        spacing 40
        xalign 0.5
        yalign 0.7

        button:
            style "mm_button"
            text "Version Courte" style "mm_button_text"
            action [SetVariable("short_version",True), Start()]

        button:
            style "mm_button"
            text "Version Longue" style "mm_button_text"
            action [SetVariable("short_version",False), Start()]

        button:
            style "mm_button"
            text "Return" style "mm_button_text"
            action Return()

init -2 python:
    short_version = False

##############################################################################
# Préférences
#
# Écran permettant à l'utilisateur de changer les préférences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences:

    tag menu

    # Inclus la navigation.
    use navigation

    # Met les colonnes de navigation dans une grille de largeur 3.



    # Colonne de gauche.
    vbox:
        style_group "prefs"

        frame:
            style_group "pref"
            has vbox

            label _("Display") style_group "pref"
            hbox:
                xpos 230
                ypos -15
                spacing 10
                button:
                    style "pref_button"
                    text "Window" style "pref_button_text"
                    action Preference("display", "window")
                button:
                    style "pref_button"
                    text "Fullscreen" style "pref_button_text"
                    action Preference("display", "fullscreen")

        frame:
            style_group "pref"
            has vbox

            label _("Transitions") style_group "pref"
            hbox:
                xpos 230
                ypos -15
                spacing 10
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

        frame:
            style_group "pref"
            has hbox style_group "special"

            label _("Text Speed") style_group "pref"
            bar value Preference("text speed")

        frame:
            style_group "pref"
            has hbox style_group "special"

            label _("Auto-Forward Time") style_group "pref"
            bar value Preference("auto-forward time")

        frame:
            style_group "pref"
            has hbox style_group "special"

            label _("Music Volume") style_group "pref"
            bar value Preference("music volume")

        frame:
            style_group "pref"
            has hbox style_group "special"

            label _("Sound Volume") style_group "pref"
            textbutton _("Test"):
                action Play("sound", config.sample_sound)
                style "soundtest_button"
            bar value Preference("sound volume")


        frame:
            style_group "pref"
            has hbox style_group "special"

            label _("Volume de l'ambiance sonore") style_group "pref"
            bar value MixerValue("ambiance")


init -2 python:

    style.prefs_vbox.ypos = 0.5
    style.prefs_vbox.yanchor = 0.5

    style.pref_frame.left_margin = 150
    style.pref_frame.xpadding = 30
    style.pref_frame.bottom_margin = -10

    style.pref_label_text.ypos = 40

    style.pref_button.background = Frame("interface/buttons/mainmenu/minibutton.png",25,16)
    style.pref_button.hover_background = Frame(im.MatrixColor("interface/buttons/mainmenu/minibutton.png",im.matrix.brightness(-0.05)),25,16)
    style.pref_button.xminimum = 190
    style.pref_button.yminimum = 32
    style.pref_button.xalign = 1.0

    style.pref_button_text.xalign = 0.5

    style.pref_frame.background = Frame("interface/box/save_box.png", 50, 50)
    style.pref_vbox.yminimum = 110
    style.pref_vbox.xminimum = 630

    style.special_hbox.yminimum = 110
    style.special_hbox.xminimum = 630

    style.special_slider.xmaximum = 200
    style.special_slider.xalign = 1.0
    style.special_slider.xanchor = 1.1
    style.special_slider.yalign = 0.5

    style.special_button.size_group = "pref"

    style.soundtest_button.xpos = 50
    style.soundtest_button.background = Frame("interface/buttons/mainmenu/minibutton.png",25,16)
    style.soundtest_button.hover_background = Frame(im.MatrixColor("interface/buttons/mainmenu/minibutton.png",im.matrix.brightness(-0.05)),25,16)
    style.soundtest_button.xminimum = 110
    style.soundtest_button.yminimum = 32

    style.soundtest_button.yalign = 0.5

    style.special_slider.thumb = "interface/scrollbar/scrollh.png"
    style.special_slider.left_bar = "interface/scrollbar/barh.png"
    style.special_slider.right_bar = im.MatrixColor("interface/scrollbar/barh.png",im.matrix.brightness(-0.5))
    style.special_slider.thumb_offset = 15




##############################################################################
# Menu Oui/Non
#
# Écran proposant à l'utilisateur une question oui ou non
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    # frame:
    #     style_group "yesno"
    #
    #     xfill True
    #     xmargin .05
    #     ypos .1
    #     yanchor 0
    #     ypadding .05

    label _(message):
        yalign 0.45
        xalign 0.5

    hbox:
        yalign 0.55
        xalign 0.5
        spacing 100

        button:
            style "yn_button"
            text "Yes" style "mm_button_text"
            action yes_action

        button:
            style "yn_button"
            text "No" style "mm_button_text"
            action no_action


    # Clic droit ou échap pour "non"
    key "game_menu" action no_action

init -2 python:
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5
    style.yesno_label_text.layout = "subtitle"


##############################################################################
# Menu rapide
#
# Écran inclus par défaut pour les dialogues, ajoutant un accès rapide à
# plusieurs fontions utiles
screen quick_menu:

    # Ajoute un menu rapide au sein du jeu
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 12
    style.quick_button_text.idle_color = "#8888"
    style.quick_button_text.hover_color = "#ccc"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#4448"

##############################################################################
# In-game UI
screen ingame_menu:

        vbox xalign 0.994 yalign 0.99:
            spacing 10
            imagebutton auto "interface/buttons/pause/pause_%s.png" action ShowMenu("save")
            imagebutton auto "interface/buttons/log/log_%s.png" action [SetVariable("yvalue", 1.0), ShowMenu('text_history')]
        # vbox xalign 0.97 yalign 0.03:
        #     imagebutton auto "interface/buttons/pause/pause_%s.png" action ShowMenu("save")
