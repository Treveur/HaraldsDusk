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
    show einar prisonnier_blesse_mid at left
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
    show einar debout_blesse_mid at left, shake
    hide einar with dissolve
    "Fin 03/22"
    call game_over_combat('interieur_grande_porte_chateau_1') from _call_game_over_combat_1

label bad_ending_4:
    show ogma combat_furieux_mid at center
    "La furie sanguinaire d'Ogma est incontrôlable. Einar est massacré sur place."
    hide einar with dissolve
    show re combat_normal_mid at right with moveinright
    "Les rebelles continuent d'affluer dans l'enceinte, et Ogma tombe à genoux devant le cadavre d'Einar."
    show ogma debout_attriste_mid at center
    o "Grrr..."
    "Il tire une dague et commence à poignarder et mutiler sans relâche les restes du viking..."
    "Fin 04/22"
    jump credits

label bad_ending_5:
    show huscarls combat_normal_mid at right
    show einar combat_blesse_mid at left
    "Les forces coordonnées des huscarls surpassent le talent d'Einar, qui est jeté au sol."
    show huscarls combat_furieux_mid at right
    "Les huscarls le transforment en une pulpe sanglante sous une pluie de coups furieux."
    hide einar with dissolve
    "Fin 05/22"
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
    show einar combat_hache_normal_mid at left
    show ogma debout_determine_mid at right
    e "Voici la Hache."
    show einar debout_normal_mid at left
    o "Merci beaucoup. Combien auraient cédé à l'appel du pouvoir ?"
    show ogma debout_souriant_mid at right
    o "Peu d'hommes auraient eu ta droiture et ton humilité !"
    e "Vous allez détruire la Hache ?"
    show ogma debout_determine_mid at right
    o "Oui. Je la ferai fondre en une arme nouvelle, une claymore."
    o "Elle sera destinée à ma famille, le clan Wallace. Elle symbolisera la fin de l'oppression et l'émergence de la Liberté !"
    show re debout_normaux_mid at center
    ge "HOURRAAA !"
    "Fin 07/22"
    jump credits

label good_ending_8:
    "Sur le dos de son cheval chargé d'or, Einar s'éloigne peu à peu de Perth."
    "Les villageois lui font leurs adieux et petit à petit, la place se vide."
    "Mais alors qu'Einar est déjà loin, une seule personne reste à la sortie du village, regardant Einar s'éloigner inexorablement."
    "Moira."

    menu :
        "(Quel soulagement d'avoir détruit la Hache)":
            e "(Me voilà débarrassé de tous mes engagements...)"
            e "(Maintenant que le monde est privé de la Hache, l'équilibre devrait revenir.)"
            e "(Enfin, j'espère...)"

        "(Allons récupérer la Hache !)":
            e "(Les abrutis ! Ils ont réellement cru que j'allais détruire une merveille pareille ?)"
            e "(Il est temps de la récupérer ! Ce genre de choses ne devrait pas rester à traîner dans la nature...)"
            e "(Et ensuite, à moi le pouvoir !)"

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
    "Fin 10/22"
    jump credits

label good_ending_11:
    scene bg village
    show ogma debout_souriant_mid at center zorder 0 with dissolve
    o "Aujourd'hui et au nom du peuple d'Ecosse, je te remercie, Einar !"
    o "Nous te sommes tous redevables !"
    show re debout_normaux_mid at right zorder 1 with dissolve
    ge "HOURRAAA !"
    hide re with dissolve
    o "Tu as agit pour le bien du plus grand nombre, ne l'oublie jamais."
    o "Comme promis, tu es désormais libre d'aller où bon te semble. Un cheval harnaché avec des fontes remplies d'or t'attends."
    show einar debout_normal_mid at left
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
    o "A vrai dire, il y a quelqu'un en particulier qui tient énormément à ta présence."
    show einar debout_souriant_mid at left
    e "Ah ?"
    o "Je sais que Moira et toi êtes devenus très proches..."
    o "Aussi, j'ai décidé de t'offrir la main de ma fille !"
    o "N'est-ce pas la plus belle récompense ?"
    menu :
        "Oui !":
            e "Et comment ! Je n'aurais pû espérer mieux !"
            o "Merveilleux !"
            "..."
            hide einar
            hide ogma
            with dissolve
            scene bg village_crepuscule with dissolve
            "Le soir venu, lors du festin organisé en l'honneur d'Einar, Ogma annonce les noces sous une ovation tonitruante."
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
            hide einar
            hide ogma
            with dissolve
            scene bg village_crepuscule with dissolve
            "Le soir venu, lors du festin organisé en l'honneur d'Einar, on remarque le visage fermé et la froideur de Moira."
            "Perth fête sa liberté retrouvée ; l'Ecosse va reprendre son destin en main."
            "Le nom d'Einar restera gravé dans les mémoires pour des centaines d'années."
            "Einar le Libérateur."
    
    "Fin 11/22"
    jump credits

label bad_ending_12:
    "Les deux vikings rendent coup pour coup."
    "Mais le roi projette Einar contre le mur avant de se ruer sur lui."
    h "MEURS !"
    "Einar meurt étranglé par son roi, les vertèbres craquant sous l'étreinte du monarque."
    "Fin 12/22"
    jump credits

label good_ending_13:
    "Sur le dos de son cheval chargé d'or, Einar s'éloigne peu à peu de Perth."
    "Les villageois lui font leurs adieux et petit à petit, la place se vide."
    "Mais alors qu'Einar est déjà loin, une seule personne reste à la sortie du village, regardant Einar s'éloigner inexorablement."
    "Moira."
    "Fin 13/22"
    jump credits

label good_ending_14(rejete):
    if rejete:
        "Einar dépasse Moira qui reste immobile au milieu du sentier, les poings serrés, fixant le sol."
    else:
        show moira debout_souriant_close at right
        show einar debout_souriant_close at left
        with dissolve

        m "Où allons-nous ?"
        e "Loin d'ici !"
        e "Quand ton père aura compris que tu t'es enfuie pour m'accompagner, il se lancera à notre recherche."
        show einar debout_attriste_close at left
        e "Et je n'ai aucune envie de me retrouver à nouveau enfermé dans une cahutte pendant un mois !"
        m "Ha ha ha !"
        show einar debout_souriant_close at left
        e "Il y a un endroit en particulier que tu voudrais voir ?"
        m "Je ne sais pas... J'hésite entre la Norvège et la Méditerrannée."
        e "Alors nous irons voir la Méditerrannée ! Retourner en Norvège, ce serait du suicide..."
        "Les deux voyageurs disparaissent dans les bois, prenant la direction du sud..."
    "Fin 14/22"
    jump credits

label good_ending_15(marier):
    if marier:
        "Une tornade rousse se précipite vers les deux hommes."
        "Moira se jette dans les bras d'Einar et l'embrasse."
        ve "HOURRAAAA !"
    else:
        "Einar enfourche son cheval et part, seul avec ses pensées."
    "Fin 15/22"
    jump credits

label bad_ending_16:
    "Harald effectue un moulinet rapide qui désarme Einar. En se retournant, il le fend en deux d'un seul coup et laisse le cadavre tomber au sol."
    "Le roi quitte la pièce en sifflotant."
    "Fin 16/22"
    jump credits

label bad_ending_17:
    "Il est de plus en plus difficile de résister à la force d'Ogma, et Einar perd peu à peu sa concentration alors qu'il est absorbé par l'effort."
    "Le viking ne remarque pas l'archer qui le vise de l'autre côté du pont-levis ; une flèche vient frapper Einar à l'épaule."
    show einar combat_furieux_close at left, shake
    "Ogma profite de cette ouverture pour transperçer le viking de sa lame, et laisse tomber son cadavre dans les douves."
    show einar combat_furieux_close at left, shake
    "Fin 17/22"
    jump credits

label normal_ending_18:
    "Le repas se poursuit toute la nuit, célébrant les exploits d'Einar autant que l'éradication des rebelles..."
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
    show einar debout_determine_mid at center with move
    "Einar fend la foule, s'élance vers le bûcher et tente de détacher Moira."
    "Lorsqu'il parvient à trancher ses liens, un archer lui décoche une flèche dans l'abdomen."
    show einar debout_blesse_mid at center
    e "Argh... Cours ! Va t'en !"
    "Moira n'essaie même pas de bouger."
    show moira debout_furieux_mid at right
    "Elle arrache la hachette de la ceinture d'Einar et lui en assène un coup violent en travers de la gorge."
    "Alors qu'Einar s'effondre, il ne voit rien d'autre que les yeux larmoyants de haine de Moira."
    "Fin 20/22"
    jump credits

label bad_ending_21:
    "Einar s'éloigne du château en enjambant sans distinction les cadavres écossais et vikings, tâchant ses vêtements dans la végétation imbibée de sang."
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

    scene black
    centered "Game over \n
    Checkpoint a venir \n
    Pensez à sauvegarder :)"

    if label_name != "":
        menu:
            "Réessayer":
                $ renpy.jump (label_name)
            "Quitter":
                jump credits

label credits:

    stop ambiance

    scene bg black with dissolve
    centered "HARALD'S DUSK"
    with Pause(2.5)
    centered "DESIGN ET PROGRAMMATION :\n
    Alexandre Allais\n
    Benjamin Ramauge\n
    Nicolas Duval"
    centered "GRAPHISME :\n
    Alexandre Rafael David\n
    Céline Lascaux\n
    Farah Merand\n
    Raphaëlle Maniere\n
    Samuel Amar\n
    Sandy Chhun\n
    Sarah-Cheyenne Laurence Gilbercovici"
    centered "SON :\n
    Julien Laguerre\n
    Nicolas Lorion"

    $ renpy.full_restart()
