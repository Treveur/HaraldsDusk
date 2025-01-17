#Checkpoint
label gameover:
    call game_over_combat(checkpoint) from _call_game_over_combat_8

#Moira vengeance
label moira_vengence:
    "En un éclair d'acier, elle poignarde Einar."
    "Surpris, le viking n'a pas le temps de repousser l'attaque, et la lame s'enfonce profondément entre ses côtes."
    "Sans laisser le temps à Einar de réagir, elle arrache la lame et le poignarde à nouveau, encore et encore."
    "Après quelques minutes, Moira continue de poignarder le cadavre du viking."
    "Ses larmes ont séché ; son regard est fixe et vide."
    call game_over_combat(checkpoint)

#Ending
label bad_ending_1:
    "Le meneur des assaillants tranche la gorge d'Einar, de la même manière que Logan. Après de longues minutes à se noyer dans son propre sang, Einar meurt."
    hide einar with dissolve
    "Fin 01/22"
    jump credits

label bad_ending_2:
    show einar prisonnier_furieux_mid at left
    e "Je n'ai qu'une parole. Vous pouvez aller vous faire foutre !"
    show ogma debout_contrarie_mid at center
    o "C'est décevant... Tu crois être unique ? Si ce n'est pas toi, un autre fera le travail à ta place."
    "Ogma égorge Einar alors qu'il est entravé."
    show einar prisonnier_blesse_mid at left, shake
    e "Grrblbhh..."
    hide einar with dissolve
    "Après s'être étouffé avec son propre sang, Einar meurt. Son corps est alors ramené sur les lieux de l'embuscade et est laissé à pourrir aux côtés de ses compagnons."
    "Fin 02/22"
    call game_over_combat('refuser_trahir_village_2') from _call_game_over_combat

label bad_ending_3:
    show bg chateau_rempart_crepuscule with dissolve
    show einar debout_determine_mid at left
    "Au moment où Einar s'apprête à actionner le mécanisme de la porte, une flèche est décochée dans son dos."
    show einar debout_blesse_mid at left, shake
    "Lorsqu'il se retourne pour voir d'où provient le tir, il voit Harald le désigner depuis la cour en donnant des ordres à ses archers."
    "Une volée de flèches vient frapper Einar et le fait basculer par dessus les remparts."
    "Les mauvais menteurs sont toujours punis."
    show einar debout_blesse_mid at left, shake
    hide einar with dissolve
    "Fin 03/22"
    call game_over_combat('interieur_grande_porte_chateau_1') from _call_game_over_combat_1

label bad_ending_4:
    show ogma combat_furieux_mid at left with moveinleft
    show ogma combat_furieux_mid_flip
    "La furie sanguinaire du Hurleur est incontrôlable."
    hide einar with dissolve
    show re combat_normal_mid at right with moveinright
    "Les rebelles continuent d'affluer dans l'enceinte, et Ogma tombe à genoux devant le cadavre d'Einar."
    show ogma debout_attriste_mid_flip:
        xoffset 0
    o "Grrr..."
    "Il tire une dague et commence à poignarder et mutiler sans relâche les restes du viking..."
    "Fin 04/22"
    call game_over_combat('interieur_grande_porte_chateau_1')

label bad_ending_5:
    "Fin 05/22"
    call game_over_combat("checkpoint_2")
    jump credits

label bad_ending_6:
    show harald combat_hache_furieux_mid_flip at center
    "Harald décapite Einar d'un coup unique et ample, sans lui laisser le temps de répliquer."
    hide einar with dissolve
    show harald combat_hache_determine_mid_flip at center
    h "Et maintenant, au tour des écossais..."
    "Fin 06/22"
    jump credits

label good_ending_7:

    play music ending

    show einar combat_hache_normal_mid at left
    show ogma debout_determine_mid at center
    e "Voici la Hache."
    show einar debout_normal_mid at left
    o "Merci beaucoup. Combien auraient cédé à l'appel du pouvoir ?"
    show ogma debout_souriant_mid at center
    o "Peu d'hommes auraient eu ta droiture et ton humilité !"
    e "Vous allez détruire la Hache ?"
    show ogma debout_determine_mid at center
    o "Oui. Je la ferai fondre en une arme nouvelle, une claymore."
    o "Elle sera destinée à ma famille, le clan Wallace. Elle symbolisera la fin de l'oppression et l'émergence de la Liberté !"
    show re debout_normaux_mid at right
    ge "HOURRAAA !"
    "Fin 07/22"
    jump credits

label good_ending_8:

    "Sur le dos de son cheval chargé d'or, Einar s'éloigne peu à peu de Perth."
    "Les villageois lui font leurs adieux et petit à petit, la place se vide."

    menu :
        "(Quel soulagement d'avoir détruit la Hache)":
            e "(Me voilà débarrassé de tous mes engagements...)"
            e "(Maintenant que le monde est privé de la Hache, l'équilibre devrait revenir.)"
            e "(Enfin, j'espère...)"

            play music ending

            "Le monde se souviendra d'Einar, Libérateur de l'Ecosse ; mais une part d'ombre subsistera."
            "Einar était-il plus qu'un homme ? Comment a-t-il pu détruire la Hache Sainte et vaincre son porteur, élu de Dieu ?"

        "(Allons récupérer la Hache !)":
            e "(Les abrutis ! Ils ont réellement cru que j'allais détruire une merveille pareille ?)"
            e "(Il est temps de la récupérer ! Ce genre de choses ne devrait pas rester à traîner dans la nature...)"

            e "(Et ensuite, à moi le pouvoir !)"
            play music ending

            "L'Histoire ne se souviendra pas d'Einar comme d'un homme, mais comme d'un Dieu retors et rusé, traversant les âges armé de la Hache Sainte."
            "Jusqu'où iront ses conquêtes ? A quel point s'étendront ses royaumes infinis ?"

    "Fin 08/22"
    jump credits

label good_ending_9:
    scene bg plaine_cotiere_crepuscule
    "Einar porte une tenue de général et mène une armée innombrable face à ce qui semble être une armée asiatique, dans un paysage exotique fait de montagnes et de cultures en étages."
    show einar combat_hache_furieux_mid at center
    e "Aujourd'hui, le dernier peuple dissident s'inclinera devant nous !"
    e "CHARGEEEEEEEEZ !"
    "Fin 09/22"
    jump credits

label normal_ending_10:
    show ogma debout_souriant_mid at right
    o "Merci..."
    hide einar with dissolve
    "Ogma s'empare de la Hache et la brandit aux yeux de tous."
    show ogma debout_determine_mid at center with moveinleft
    o "Aujourd'hui, nous nous sommes libérés de nos chaînes !"
    o "L'Ecosse est libre ! Et désormais, un écossais porte la relique ! La Hache Sainte !"
    show ogma debout_souriant_mid at center
    show re debout_normaux_mid at left
    ge "Gloire à Ogma !"
    hide re
    show ogma debout_determine_mid at center
    o "Nous ne nous arrêterons pas en si bon chemin... Car Dieu est avec nous !"
    o "Il est temps de libérer le reste de la Grande-Bretagne ! Libérer l'Europe ! Libérer le monde !"
    o "Le monde mérite un empereur écossais !"
    show re debout_normaux_mid at left
    ge "HOURRAAAA !"
    hide re
    play music ending
    "Fin 10/22"
    jump credits

label good_ending_11:
    scene bg village
    show ogma debout_souriant_mid at center zorder 0 with dissolve
    o "Aujourd'hui et au nom du peuple d'Ecosse, je te remercie, Einar !"
    o "Nous te sommes tous redevables !"
    show re debout_normaux_mid at right zorder 1 with dissolve:
        xoffset 300
    ge "HOURRAAA !"
    hide re with dissolve
    show einar debout_normal_mid at left with dissolve
    o "Tu as agit pour le bien du plus grand nombre, ne l'oublie jamais."
    o "Comme promis, tu es désormais libre d'aller où bon te semble. Un cheval harnaché avec des fontes remplies d'or t'attends."
    e "Merci."
    o "Tu as l'air contrarié... Savoure ta victoire !"
    menu:
        "Tout va bien, merci":
            show einar debout_souriant_mid at left
            e "Excuse-moi, j'étais dans mes pensées !"
            o "Ah, j'aime mieux ça !"

        "Vous avez trahi votre parole en tuant Harald":
            show einar debout_contrarie_mid at left
            e "Une victoire, certes... Mais une victoire amère."
            show ogma debout_normal_mid at center
            o "Pourquoi ça ?"
            e "Vous n'avez pas été fidèles à notre marché. Vous avez tué le roi."
            o "Je comprends ta rancoeur. Mais je ne pouvais pas te dire la vérité."
            o "Aurais-tu accepté de nous aider si je t'avais dit que le but était de tuer le roi ?"
            show einar debout_determine_mid at left
            e "Je ne sais pas."
            o "Peu importe ! Tu as libéré notre peuple, et nous t'avons offert tout ce que nous t'avions promis. Et même plus !"

    show ogma debout_normal_mid at center
    o "Nous avons organisé un grand repas pour fêter la victoire, nous aimerions que tu te joignes à nous."
    show einar debout_normal_mid at left
    e "Je ne suis pas sûr..."
    show ogma debout_souriant_mid at center
    o "A vrai dire, il y a une raison particulière à ta présence."
    show einar debout_souriant_mid at left
    e "Ah ?"
    o "Je serais heureux de compter le libérateur de mon peuple dans ma famille."
    o "J'ai l'honneur de t'offrir la main de ma fille, si tu l'acceptes."
    menu :
        "Oui !":
            e "Et comment ! Je n'aurais pû espérer mieux !"
            o "C'est sans doute la plus belle conclusion à apporter à cette histoire ! La liberté retrouvée, une fête, un mariage."
            "..."
            hide einar
            hide ogma
            with dissolve
            scene bg village_crepuscule with dissolve
            "Le soir venu, lors du festin organisé en l'honneur d'Einar, Ogma annonce les noces sous une ovation tonitruante."
            "Les deux fiancés font l'objet de toutes les bénédictions et des félicitations des villageois, alors que personne ne remarque les larmes discrètes de Moira."
            "Perth fête sa liberté retrouvée ; l'Ecosse va reprendre son destin en main."
            "Le nom d'Einar restera gravé dans les mémoires pour des centaines d'années."
            "Einar le Libérateur."

        "Non...":
            show einar debout_normal_mid at left
            e "Votre offre m'honore, mais je ne peux accepter."
            show ogma debout_attriste_mid at center
            o "Pourquoi ?"
            e "Je ne souhaite pas me marier à Moira ; vous exposer mes raisons ne changerait rien à l'affaire."
            o "Je ne comprend pas ta réaction... Elle sera profondément blessée."
            e "Rien n'est moins sûr."
            hide einar
            hide ogma
            with dissolve
            scene bg village_crepuscule with dissolve
            if moira_abuse ==False:
                "Le soir venu, lors du festin organisé en l'honneur d'Einar, Moira vient chercher le guerrier viking."
                m "Merci."
                e "Pour ?"
                m "Ne pas avoir accepté l'offre de mon père."
                play music ending
                "Perth fête sa liberté retrouvée ; l'Ecosse va reprendre son destin en main."
                "Le nom d'Einar restera gravé dans les mémoires pour des centaines d'années."
                "Einar le Libérateur."

            else:
                play music ending
                "Le soir venu, lors du festin organisé en l'honneur d'Einar, Moira reste ostensiblement à l'écart du viking."
                "Perth fête sa liberté retrouvée ; l'Ecosse va reprendre son destin en main."
                "Le nom d'Einar restera gravé dans les mémoires pour des centaines d'années."
                "Einar le Libérateur."

    "Fin 11/22"
    jump credits

label bad_ending_12:
    scene bg chateau_couloir_crepuscule with dissolve
    show einar combat_determine_mid_flip at right with moveinleft
    show einar combat_determine_mid_flip at right, shake
    show harald combat_furieux_mid_flip at left with moveinleft
    h "Tu n'as aucune chance ! J'ai été choisi par Dieu !"
    show harald combat_furieux_mid_flip at center with moveinleft:
        xoffset 300
    show einar combat_furieux_mid_flip at right, shake
    show harald combat_furieux_mid_flip at center, shake:
        xoffset 0
    show einar combat_furieux_mid_flip at right, shake
    "Les deux vikings rendent coup pour coup."
    "Mais le roi projette Einar contre le mur avant de se ruer sur lui."
    show harald combat_furieux_mid_flip at right with moveinleft
    h "MEURS !"
    "Einar meurt étranglé par son roi, les vertèbres craquant sous l'étreinte du monarque."
    hide einar with dissolve
    "Fin 12/22"
    call game_over_combat('checkpoint_3')

label good_ending_13:
    play music ending
    "Les villageois lui font leurs adieux et petit à petit, la place se vide."
    "Sur le dos de son cheval chargé d'or, Einar s'éloigne peu à peu de Perth."
    "L'Histoire se souviendra d'Einar le Régicide, celui qui libéra le monde du joug du plus terrible tyran."
    "Fin 13/22"
    jump credits

label bad_ending_14(tuer):

    if tuer:
        "Einar s'éloigne en silence du corps de Moira."
        "..."
        "Tous se souviendront d'Einar comme du héros libérateur de l'Ecosse ; mais personne ne découvrira jamais qui a tué Moira."

    else:
        show moira debout_souriant_close at right
        show einar debout_souriant_close at left
        with dissolve

        play music ending

        "Einar poursuit son chemin, laissant la jeune femme derrière lui."
        "..."
        "Tous se souviendront d'Einar comme du héros libérateur de l'Ecosse ; une écossaise nommée Moira veillera à la transmission de son histoire."

    "Fin 14/22"
    jump credits

label good_ending_15(marier):

    if marier:
        "Moira s'approche lentement devant Einar, sans oser le regarder dans les yeux."

        menu:
            "Ne t'inquiète pas":
                e "Ne t'inquiète pas. Je ne te ferai aucun mal."
                "La jeune femme sourit vaguement, regardant à peine Einar."

            "(sourire)":
                if moira_abuse == False:
                    "Einar adresse un sourire à Moira, qui semble un peu plus sereine."

                else:
                    "Einar adresse un sourire lourd de sens à Moira."
                    "La jeune femme serre les poings et semble au bord des larmes."
        play music ending
        "Le soir venu, le village fête les noces annoncées d'Einar et Moira."
        "Le monde se souviendra d'un Héros, Einar le Libérateur."
        "Mais à quel genre d'homme sera mariée Moira ?"

    else:
        o "Peu importe ce que tu feras de ta vie ; tu trouveras toujours des amis à Perth."
        e "Il est temps pour moi de partir."
        play music ending
        "Einar enfourche son cheval et part, seul avec ses pensées."
        "Derrière lui, une jeune femme rousse le regarde s'éloigner."
    "Fin 15/22"
    jump credits

label bad_ending_16:
    "Harald effectue un moulinet rapide qui désarme Einar. En se retournant, il le fend en deux d'un seul coup et laisse le cadavre tomber au sol."
    "Le roi quitte la pièce en sifflotant."
    "Fin 16/22"
    call game_over_combat('e_bruler_donjon_obeir_donjon')

label bad_ending_17:
    "Il est de plus en plus difficile de résister à la force d'Ogma, et Einar perd peu à peu sa concentration alors qu'il est absorbé par l'effort."
    "Le viking ne remarque pas l'archer qui le vise de l'autre côté du pont-levis ; une flèche vient frapper Einar à l'épaule."
    show einar combat_furieux_close at left, shake
    "Ogma profite de cette ouverture pour transperçer le viking de sa lame, et laisse tomber son cadavre dans les douves."
    show einar combat_furieux_close at left, shake
    "Fin 17/22"
    jump credits

label normal_ending_18:
    stop ambiance fadeout 1
    play music ending
    "Le repas se poursuit toute la nuit, célébrant les exploits d'Einar autant que l'éradication des rebelles..."
    "Si l'Histoire ne se souviendra pas du nom d'Einar, la victoire retentissante du roi-empereur Harald Sigurdsson contre les rebelles restera gravée dans les mémoires."
    "Car nul n'osera plus jamais s'élever contre le viking élu de Dieu."
    "Fin 18/22"
    jump credits

label bad_ending_19:
    "Les regards d'Einar et Moira se croisent et se fixent."
    "Alors que les flammes commencent à la dévorer, elle ne hurle pas."
    "Elle contient toute sa rage et sa colère, adressant un regard de haine pure à Einar alors que des larmes coulent sur ses joues."
    "Dans les hurlements des prisonniers, les flammes de la rébellion s'éteignent."
    "Fin 19/22"
    jump credits

label bad_ending_20:
    show einar debout_determine_mid_flip at left with moveinleft
    "Einar fend la foule, s'élance vers le bûcher et tente de détacher Moira."
    show moira debout_normal_close_flip at left
    show einar debout_determine_close_flip at center
    with dissolve
    "Lorsqu'il parvient à trancher ses liens, un archer lui décoche une flèche dans l'abdomen."
    show einar debout_attriste_close_flip at center, shake
    e "Argh... Cours ! Va t'en !"
    "Moira n'essaie même pas de bouger."
    show moira debout_furieux_close_flip at left
    "Elle arrache la hachette de la ceinture d'Einar et lui en assène un coup violent en travers de la gorge."
    show einar prisonnier_attriste_close_flip at center, shake
    hide einar with dissolve
    "Alors qu'Einar s'effondre, il ne voit rien d'autre que les yeux larmoyants de haine de Moira."
    "Dans les hurlements des prisonniers, les flammes de la rébellion s'éteignent."
    "Fin 20/22"
    jump credits

label bad_ending_21:
    scene bg plaine_chateau_crepuscule with dissolve
    show einar debout_normal_close at center with moveinleft
    "Einar s'éloigne du château en enjambant sans distinction les cadavres écossais et vikings, tâchant ses vêtements dans la végétation imbibée de sang."
    show einar debout_normal_close at right with moveinright
    hide einar with dissolve
    "Derrière lui, Dunbar brûle."
    "Fin 21/22"
    jump credits

label bad_ending_22:
    "Ogma atteint Einar."
    "Avant même que le viking n'ait pu esquisser le moindre mouvement, Ogma le massacre sur place."
    "L'écossais ne laisse rien de reconnaissable, continuant à frapper bien après la mort d'Einar."
    "Lorsque après de longues minutes il cesse d'abattre la Hache, il ne reste plus qu'une bouillie informe et rouge au milieu de la plaine."
    "Fin 22/22"
    jump credits

label game_over_combat(label_name):

    scene bg game_over

    if label_name != "":
        menu:
            "Réessayer":
                $ renpy.jump (label_name)
            "Quitter":
                jump credits

label credits:

    stop ambiance

    scene bg black with dissolve
    centered "{font=fonts/Celtknot.ttf}{size=+80}Harald's Dusk{/size}{/font}"
    with Pause(2.5)
    centered "{font=fonts/Celtknot.ttf}{size=+20}Design et Programmation :{/size}{/font}\n
    Alexandre Allais\n
    Benjamin Ramauge\n
    Nicolas Duval"
    centered "{font=fonts/Celtknot.ttf}{size=+20}Graphisme :{/size}{/font} \n
    Rafael David\n
    Céline Lascaux\n
    Farah Merand\n
    Raphaëlle Maniere\n
    Samuel Amar\n
    Sandy Chhun\n
    Sarah-Cheyenne Laurence Gilbercovici"
    centered "{font=fonts/Celtknot.ttf}{size=+20}Son :{/size}{/font} \n
    Julien Laguerre\n
    Nicolas Lorion"
    stop music
    $ renpy.full_restart()
