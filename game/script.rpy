# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
#Image représentant les personnages
#Einar
image einar serious = "einar_1.png"

#Logan
image logan fache = "logan.png"

#Harald
image harald normal = "harald_min.png"

#Scene
image bg forest = "foret_cabane.jpg"
image bg village = "village.jpg"
image bg mer = "chateau_mer.jpg"

#Fond uni
image bg black = "#000"

# Déclarez les personnages utilisés dans le jeu.
define e = Character('Einar', color="#e74c3c")
define l = Character('Logan', color="#f1c40f")
define h = Character('Harald', color="#3498db")
define gv = Character('Guerriers Vikings', color="#e67e22")
define vm = Character('Villageois', color="#3498db")
define o = Character('Ogma', color="#d35400")
define ge = Character('Guerriers écossais', color="#f39c12")






# Le jeu commence ici

label start:

    scene bg black
    "petit texte introduction"
    jump intro

#ACTE 1

#Sequence 1
label intro:

    #Stop music s'il y en a une en cours
    stop music

    #Variables
    $ intro_dial = False
    $ eclaireur_dial = False

    scene bg forest

    "Dans la forêt de la Westruther du caca, une troupe de vikings se dirige vers le chateau de Dunbar pour s'y installer et préparer répréssion des rebelles"

    "En effet, les écossais ont tué l'intendant d'Ecosse"

    "Parmis ces vikings Einar, général d'Harald qui se trouve justement à coté de lui mais aussi à Logan son ami"

    menu:
        "Parler à Harald":
            jump harald_choice
        "Parler à Logan":
            jump logan_choice
        "Ne rien dire":
            jump plaine

    show einar serious

label harald_choice:

    show einar serious

    if intro_dial == False:

        e "Mon Roi, celà un moment que nous sommes venu ici"

        show einar serious at left
        show harald normal at right with dissolve

        h "En effet, Einar, celà me rapelle les batailles contre les païens"

        h "Nous les avons réduit en poussière en un rien de temps"

        e "Et les voilà qui se rebellent en tuant Clyde"

        $ intro_dial = True

    menu:
        "se remémorer la bataille":
            jump h_souvenir_bataille

        "Parler de la région":
            jump h_info_region

        "Se montrer enthousiaste sur la mission":
            jump h_enthousiaste

        "Pourquoi tant de confiance ?":
            jump h_confiance

        "Est-il vraiment nécessaire de tuer des innocents?":
            jump h_innocents

        "Continuer silencieusement":
            jump plaine



label logan_choice :

    show einar serious

    if intro_dial == False:

        e "Logan, cela ne te rappele donc pas des souvenir ?"

        show einar serious at left
        show logan fache at right with dissolve

        l "En effet, Einar, celà me rapelle les batailles contre les païens"

        l "Nous les avons réduit en poussière en un rien de temps"

        e "Et les voilà qui se rebellent en tuant Clyde"

        $ intro_dial = True

    menu:
        "se remémorer la bataille":
            jump l_souvenir_bataille

        "Parler de la région":
            jump l_info_region

        "Se montrer enthousiaste sur la mission":
            jump l_enthousiaste

        "Pourquoi Harald est si confiant ?":
            jump l_confiance

        "Est-il vraiment nécessaire de tuer des innocents?":
            jump l_innocents

        "Continuer silencieusement":
            jump plaine


#Harald
label h_souvenir_bataille :
    e "Quelles batailles incroyable que nous avons vécu ici"

    h "En effet, de nombreux ennemis se sont mis en travers de notre route"

    h "Ils étaient braves et courageux mais fasse à ma hache, ils n'ont pas fait le poids"

    e "Nous en avons fait une bouché"

    jump harald_choice

label h_info_region :
    e "Mon Roi, Celà fait un moment que nous somme ici, est-ce que tu me rappeler les caratactérique de la régions ?"

    h "Eh bien, les Highlands sont pincipalement composés de plaines"

    h "Il y a aussi des reliefs abrupts mais aussi de côtes maritimes"

    h "C'est d'ailleurs là où nous nous rendons, au chateau de Dunbar"

    e "Hatons nous mon Roi, la fatigue me guète"

    h "Patience mon ami, notre périple est loin d'être terminé"

    jump harald_choice

label h_enthousiaste :
    e "Ils y trop longtemps que nous avons eu droit à une bataille"

    e "A cause de notre puissance, les ennemis n'osent même plus ce battre"

    e "Grâce à vaine \"résistance\", je vais enfin pouvoir me défouler."

    h "Haha!!! Ils n'ont aucunes chance."

    jump harald_choice

label h_confiance :
    e "Vous paraissez confiant à propos de expédition punitive"

    h "Il n'y a pas de quoi s'inquiéter Einar"

    h "Tant que j'aurais ma hache, nous serons invincible"

    e "C'est que grâce aux cloux de sainte croix incrustées dans ta hache "

    jump harald_choice

label h_innocents :
    e "Mon Roi, est-il vraiment nécessaire de tuer des villageois ?"

    #h "En tuant, l'intendant que j'avais nommé, ils se sont attaqués à moi"

    h "Ils se cachent quelque part dans MES terres!"

    h "Quoi de mieux pour les faire sortir que s'attaquer à leurs familles ?"

    e "Vous avez raison mon Roi"

    e "Ils finiront bien par sortir pour éviter les pertes inutiles"
    jump harald_choice

#Logan
label l_souvenir_bataille :
    e "Quelles batailles incroyable que nous avons vécu ici"

    l "En effet, de nombreux ennemis se sont mis en travers de notre route"

    l "Ils étaient braves et courageux mais à Harald et sa hache, ils n'ont pas fait le poids"

    e "Nous en avons fait une bouché"
    jump logan_choice

label l_info_region :
    e "Peux-tu me rafraîchir un peu la mémoire sujet cette région ?"

    e "Cà fait bien longtemps que nous sommes partis de ces terres?"

    l "Eh bien, les Highlands sont pincipalement composés de plaines"

    l "Il y a aussi des reliefs abrupts mais aussi de côtes maritimes"

    l "C'est d'ailleurs là où nous nous rendons, au chateau de Dunbar"

    e "Hatons nous mon Roi, la fatigue me guète"

    l "Patience mon ami, notre périple est loin d'être terminé"

    jump logan_choice

label l_enthousiaste :
    e "Ils y trop longtemps que nous avons eu droit à une bataille"

    e "A cause de notre puissance, les ennemis n'osent même plus ce battre"

    e "Grâce à vaine \"résistance\", je vais enfin pouvoir me défouler."

    l "Haha!!! Ils n'ont aucunes chance."
    jump logan_choice

label l_confiance :
    e "Ne trouve tu pas notre Roi un peu trop confiant ?"

    l "Il n'y a pas de quoi s'inquiéter Einar"

    l "Avec sa hache, il n'y aucune chance que l'on perde"

    l "Grâce aux cloux de sainte croix incrustées dans sa hache, nous sommes invincibles "
    jump logan_choice

label l_innocents :
    e "est-ce que tu penses qu'il est vraiment nécessaire de tuer des villageois ?"

    #h "En tuant, l'intendant que j'avais nommé, ils se sont attaqués à moi"

    l "Si Harald nous l'ordonne, je le ferai sans problème"

    l "Ils nous l'a démontré maintes et maintes fois, on ne peut lui résister"

    e "Tu as raison"

    e "Et puis, les résistants finiront par sortir pout éviter des pertes inutiles"
    jump logan_choice


#Sequence 2
label plaine :

    scene bg mer

    if eclaireur_dial == False :
        h "Continue vers le nord pour découvrir ou se cache le village rebelle"

        e "phrase d'intro ?"

    $ eclaireur_dial = True

    menu :
        "Refuser":
            jump h_refus_village
        "Pourquoi ?":
            jump h_demande_information
        "Danger ?":
            jump h_demande_nb_detachement
        "Accepter":
            jump h_accepter
        "Accepter fayot":
            jump h_accepter_fayot

label h_refus_village :
    e "Je refuse"

    h "je suis ton ROI tg"

    e "infomation"

    jump plaine

label h_demande_information :

    e "Pourquoi moi ?"

    h "je suis ton ROI tg"

    e "infomation"

    jump plaine

label h_demande_nb_detachement :

    e "Pourquoi si peu ? Danger ?"

    h "je suis ton ROI tg"

    e "infomation"

    jump plaine

label h_accepter :

    e "À vos odres"

    h "je suis ton ROI tg"

    jump logan_aide

label h_accepter_fayot :

    e "À vos odres, Ohhhn mon Roi Empereur Adoré"

    h "je suis ton ROI tg"

    jump logan_aide

label logan_aide :

    l "Hey BFF, je viens t'aider"

    menu:
        "Cool merci beaucoup":
            jump e_reconnaissant
        "Pas moyen mec":
            jump e_refus
        "Ooooook mais fait gaffe ok...":
            jump e_contrecoeur


label e_reconnaissant :

    e "Thx bro"

    l "..."

    jump plaine_2

label e_refus :
    e "Nope, t'es vraiment trop con"

    l "..."
    jump plaine_2

label e_contrecoeur :

    e "Fais pas ta tarlouse"

    l "..."

    jump plaine_2

#Sequence 3
label plaine_2:

    e "Bon les gars, j'ai quelque chose à vous dire"

    menu:
        "Mettre en garde" :
            jump e_mettre_en_garde
        "On s'en branle" :
            jump e_ininteret_mission
        "Motiver les troupes" :
            jump e_motiver_troupe_plaine_2
        "Logan, t'es qu'un PD" :
            jump e_chambrer_logan_plaine_2
        "Bon, les gars, c'est moi qui vous l'dit, descendez d'un étage dans votre tête" :
            jump e_jouer_chef

label e_mettre_en_garde:

    e "Bon faite gaffe"

    gv "ok"

    jump foret_1

label e_ininteret_mission:

    e "A vrai dire, j'en ai rien à faire de cette mission"

    l "Comment oses-tu ?"

    gv "Ouai, c'est pas cool"

    jump foret_1

label e_motiver_troupe_plaine_2:

    e "On va tous les défoncer!"

    gv "Ahou ahou"

    jump foret_1

label e_chambrer_logan_plaine_2:

    e "Logan, t'es vraiment qu'un PD"

    l "Mais euh"

    gv "hahahahah"

    jump foret_1

label e_jouer_chef:

    e "Bon pour cette mission, c'est moi qui commande alors pas de connerie"

    e "Sinon, c'est moi qui encule"

    gv "Ohhhh. :("

    jump foret_1

#Scequence 4
label foret_1:

    e "Bon les gars"

    menu:
        "Se montrer impatient de rentrer en Norvège":
            jump e_impatient_norvege
        "Se moquer de  gens de la région" :
            jump e_se_moquer_foret_1
        "Impatient de terminer la misison" :
            jump e_impatient_mision_foret_1
        "Allez les gars, on se bouge le cul" :
            jump e_motiver_troupe_foret_1
        "Chambrer Logan" :
            jump e_chambrer_logan_foret_1
        "Demander à Logan ce qu'il pense de la mission" :
            jump e_avis_logan_mission_foret_1

label e_impatient_norvege:

    e "Plus le temps passe, plus la Norvège me manque"

    gv "Ouai, moi aussi maggle"

    menu:
        "Je suis préssé de recevoir mes terres promises rapidement":
            jump e_espoir_terre_norvege_foret_1
        "Fermez-là bande de bolosse":
            jump e_ordre_taire_guerrier_foret_1

label e_se_moquer_foret_1:

    e "quel bande de pequenot!"

    jump village_1

label e_impatient_mision_foret_1:

    e "je suis impatient de terminer cette mission"

    jump village_1

label e_motiver_troupe_foret_1:

    e "Allez les gars, on se motive"

    jump village_1

label e_chambrer_logan_foret_1:

    e "Logan, t'es qu'un pd"

    jump village_1

label e_avis_logan_mission_foret_1:

    e "Hey Loggy, que penses-ty de cette mission"

    l "Bah tu sais moi je suis un pe con con"

    menu:
        "Pourquoi as-tu décidé de m'accompagné ?":
            jump e_pourquoi_logan_accompagne_foret_1
        "Thx bro, d'être venu":
            jump e_reconnaissant_logan_foret_1
        "Tu aurais du rester avec Harald":
            jump e_rester_haral_foret_1

label e_espoir_terre_norvege_foret_1:

    e "Snif, je veux rentrer"
    jump village_1

label e_ordre_taire_guerrier_foret_1:

    e "OHhhhhhhhhhhh fermez-vos gueule de gogole"

    gv "Oui maître"

    jump village_1

label e_pourquoi_logan_accompagne_foret_1:

    e "Pour m'a tu accompagné"

    l "Parce que tu es mon bro"

    jump village_1

label e_reconnaissant_logan_foret_1:

    e "Je remercie de m'avoir accompagné"

    l "C'est normal, il faut bien se serrer les coudes et bien plus ;)"

    jump village_1

label e_rester_haral_foret_1:

    e "Tu aurais du rester avec Harald! Abruti!"

    l "Et pourquoi donc ?"

    menu:
        "Je n'ai pas envie de mettre ta vie en danger":
            jump e_attention_logan_foret_1
        "Pas besoin d'un boulet":
            jump e_poids_logan_foret_1

label e_attention_logan_foret_1:

    e "C'est parce que je n'ai pas envie de mettre ta vie en jeu"

    l "Nous sommes des guerriers, bon sans de bois"

    jump village_1

label e_poids_logan_foret_1:

    e "Tu vas me gêner tout le long de la mission"

    l "Sympa l'ami..."

    jump village_1

#Scequence 5
#Scene 1
label village_1:

    show bg village

    e "bon les gars, nous sommes arrivé au village"

    menu:
        "Massacrez-les tous!!!!":
            jump e_massacre_village_1
        "Demander des infomation sur les rebelles":
            jump e_demander_information_village_1
        "Fouiller le village!":
            jump e_fouiller_village_1
        "Chercher soi-même dans le village":
            call e_fouiller_village_1 pass (einarFouille = True)

label e_massacre_village_1:

    gv "yeah, buttons tlm"


    call choix_retour_village_1 pass (massacre = True)

label e_demander_information_village_1:

    e "Avez vous des information sur les rebelles ?"

    vm "On ne sait rien, promis juré craché!"

    menu:
        "Tuer un Villageois afin de les forcer à parler":
            jump e_tuer_villageois_village_1

        "Hausser le ton":
            jump e_intimider_villageois_village_1

label e_fouiller_village_1(einarFouille = False):

    if einarFouille:
        e "Bande d'andouille, c'est moi qui fouille"

        "Entre dans une maison"

        e "Eh madmoiselle, vous'tes bien bonne"

    else:
        e "Fouillez bande de chien galleux"

        gv "Yeahhhhhhh"

        gv "Hey, Einar vient voir ça"

        e "Mais que ce passe-t-il ?"

        gv "Regarde c'est Natalie et nous, nous sommes les méchants"

        e "Mais qui voilà"


    menu menu_maison_1:
        "Hey la meuf, c'est quoi ton nom? File moi ton 06":
            jump e_nom_villageoise_maison_1
        "Pourquoi t'fais la tepu à rester caché?":
            jump e_cache_villageoise_maison_1
        "Aurais-tu des info ou un mail pour joindre les rebelles? ":
            jump e_info_rebelle_maison_1

    #Si Einar à déjà parlé une fois à Moira
    menu menu_maison_2:
        "Hey la meuf, c'est quoi ton nom? File moi ton 06":
            jump e_nom_villageoise_maison_1
        "Pourquoi t'fais la tepu à rester caché?":
            jump e_cache_villageoise_maison_1
        "Aurais-tu des info ou un mail pour joindre les rebelles? ":
            jump e_info_rebelle_maison_1
        "Tuer la villageoise":
            jump e_tuer_moira_maison_1
        "La laisser partir":
            jump e_villagoise_partir_maison_1

label e_tuer_villageois_village_1:

    e "Toi approche"

    vm "Mais euh"

    e "Plus près"

    vm "C'est que vous savez..."

    e "Chabite, non je déconne, tu vas crever"

    call choix_retour_village_1 pass (massacre = True)

label e_intimider_villageois_village_1:
    e "Si vous ne dites rien, je vais finir par me facher et bouder !"

    vm "Mais je vous jure, je n'en sais rien"

    e "Ouin"

    jump choix_retour_village_1

#Scequence 6 (alternative)
label e_nom_villageoise_maison_1:
    e "Hey siva, dis-moi ton nom la bonnase"

    vm "Tu me parle pas comme ça ! Et je m'appelle Moira"

    e "Une belle histoire"

    jump menu_maison_2

label e_cache_villageoise_maison_1:
    e "Pourquoi n'es-tu pas avec les autres?"

    vm "Parce que je suis trop une bonnasse pour vous"

    e "Hannnnnn"

    jump menu_maison_2

label e_info_rebelle_maison_1:
    e "Aurais-tu des infos sur les rebelles ?"

    vm "Non"

    jump menu_maison_2

label e_tuer_moira_maison_1:

    e "Dommage pour toi, je vais te tuer"

    vm "oh je me meure"

    e "Alors vous allez parler bande de bolosse"

    l "Oh je suis outré"

    jump e_massacre_village_1

label e_villagoise_partir_maison_1:
    e "Va et que je ne te revois plus"

    vm "Oh merci mon seigneur"

    jump choix_retour_village_1
#fin Scequence 6

label choix_retour_village_1(massacre = False):

    if massacre:
        e "J'espère que ça leur servira de leçon"
    else:
        e "Ils vont rien nous apprendre de plus, tirons-nous"

    e "Bon ou allons nous continuer ?"

    if massacre:
        menu:
            "Rentrer au Chateau de Dunbar":
                jump massacre_foret_2
            "Poursuivre vers le nord":
                jump massacre_foret_2
    else:
        menu:
            "Rentrer au Chateau de Dunbar":
                jump foret_2
            "Poursuivre vers le nord":
                jump foret_2

#Scequence 7
label foret_2:


#Fin alternative n°1
label massacre_foret_2:
    "Sur le chemin du retour"

    e "Bon les gars"

    menu:
        "Mettre en garde":
            call attaque_massacre_foret_2 pass (message = 1)
        "Déçu par la mission":
            call attaque_massacre_foret_2 pass (message = 2)
        "Se moquer des villageois":
            call attaque_massacre_foret_2 pass (message = 3)
        "Chambrer Logan":
            call attaque_massacre_foret_2 pass (message = 4)

label attaque_massacre_foret_2(message = 0):

    if message = 1:
        e "Faites-attention, j'ai la nette impression que nous sommes oberservé!"

        gv "Bof rien ne peut nous atteindre"

    elif message = 2:

        e "Ce n'était que du menu fretin, je vais me plaindre auprès d'Harald une fois rentré"

    elif message = 3:
        e "Les bolosses, ça craquait sous ma hache"

    else:
        e "logan, t'es qu'un PD"

################A separer
    o "Vous allez payer pour ce que vous avez fait au villageois"

    o "Venez que je vous bute sales enculés"

    e "Salaud! Viens ici que je te bute enculé"

    "Einar tombe à terre un flèche dans l'épaule"

    e "Aieuhhhh"

    "Logan tombe et est égorgé au sol"

    "Einar recoit du sang de la tafiolle sur le visage"

    e "Comment as-tu osé ? Espèce de **** **** de ***"

    "Une grosse masse de muscle s'approche de Einar"

    menu:
        "Qui est tu ?":
            call e_demande_nom_foret_2 pass (bad_ending = true)
        "Non ne me tue pas, je te donnerai un sandwitch à la fraise":
            call e_implore_pitie_foret_2 pass (bad_ending = true)
        "Menacer le lourdeau":
            call e_menace_foret_2 pass (bad_ending = true)



label bad_ending_1:

    "Einar se fait tuer comme une merde parce qu'il n'a pas eu l'intelligence de réfléchir"

    "Et oui, il faut réfléchir"

    return
