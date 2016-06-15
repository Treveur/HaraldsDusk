#Ending
label bad_ending_1:
    "Le meneur des assaillants tranche la gorge d'Einar, de la même manière que Logan. Après de longues minutes à se noyer dans son propre sang, Einar meurt."
    hide einar with dissolve
    jump credits

label bad_ending_2:
    show einar debout_furieux_mid at left
    e "Je n'ai qu'une parole. Vous pouvez aller vous faire foutre !"
    show ogma debout_contrarie_mid at right
    o "C'est décevant... Tu crois être unique ? Si ce n'est pas toi, un autre fera le travail à ta place."
    "Ogma égorge Einar alors qu'il est entravé."
    e "Grrblbhh..."
    hide einar with dissolve
    "Après s'être étouffé avec son propre sang, Einar meurt. Son corps est alors ramené sur les lieux de l'embuscade et est laissé à pourrir aux côtés de ses compagnons."
    call game_over_combat('refuser_trahir_village_2')

label bad_ending_3:
    show einar debout_determine_mid at left
    "Au moment où Einar s'apprête à actionner le mécanisme de la porte, une flèche est décochée dans son dos."
    show einar debout_blesse_mid at left
    "Lorsqu'il se retourne pour voir d'où provient le tir, il voit Harald le désigner depuis la cour en donnant des ordres à ses archers."
    "Une volée de flèches vient frapper Einar et le fait basculer par dessus les remparts."
    hide einar with dissolve
    call game_over_combat('interieur_grande_porte_chateau_1')

label bad_ending_4:
    show ogma combat_furieux_mid at right
    "La furie sanguinaire d'Ogma est incontrôlable. Einar est massacré sur place."
    hide einar with dissolve
    "Alors que les rebelles continuent d'affluer dans l'enceinte, Ogma tombe à genoux devant le cadavre d'Einar."
    o "Grrr..."
    "Il tire une dague et commence à poignarder et mutiler sans relâche les restes du viking..."
    jump credits

label bad_ending_5:
    show huscarls combat_normaux_mid at right
    show einar combat_blesse_mid at left
    "Les forces coordonnées des huscarls surpassent le talent d'Einar, qui est jeté au sol."
    show huscarls combat_furieux_mid at right
    "Les huscarls le transforment en une pulpe sanglante sous une pluie de coups furieux."
    hide einar with dissolve
    jump credits

label bad_ending_6:
    show harald combat_hache_furieux_mid at right
    "Harald décapite Einar d'un coup unique et ample, sans lui laisser le temps de répliquer."
    hide einar with dissolve
    show harald combat_hache_determine_mid at right
    h "Et maintenant, au tour des écossais..."
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
    show re debout_enthousiastes_mid at center
    ge "HOURRAAA !"

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

    jump credits

label good_ending_9:
    scene bg plaine_plaine_crepuscule
    "Einar porte une tenue de général et mène une armée innombrable face à ce qui semble être une armée asiatique, dans un paysage exotique fait de montagnes et de cultures en étages."
    show einar combat_hache_determine_mid at center
    e "Aujourd'hui, le dernier peuple dissident s'inclinera devant nous !"
    show einar combat_hache_furieux_mid at center
    e "CHARGEEEEEEEEZ !"
    jump credits

label normal_ending_10:
    o "Merci..."
    "Ogma s'empare de la Hache et la brandit aux yeux de tous."
    o "Aujourd'hui, nous nous sommes libérés de nos chaînes !"
    o "L'Ecosse est libre ! Et désormais, un écossais porte la relique ! La Hache Sainte !"
    ge "Gloire à Ogma !"
    o "Nous ne nous arrêterons pas en si bon chemin... Car Dieu est avec nous !"
    o "Il est temps de libérer le reste de la Grande-Bretagne ! Libérer l'Europe ! Libérer le monde !"
    o "Le monde mérite un empereur écossais !"
    ge "HOURRAAAA !"
    jump credits

label good_ending_11:
    o "Aujourd'hui et au nom du peuple d'Ecosse, je te remercie, Einar !"
    o "Nous te sommes tous redevables !"
    ge "HOURRAAA !"
    o "Tu as agit pour le bien du plus grand nombre, ne l'oublie jamais."
    o "Comme promis, tu es désormais libre d'aller où bon te semble. Un cheval harnaché avec des fontes remplies d'or t'attends."
    e "Merci."
    o "Nous avons organisé un grand repas pour fêter la victoire, nous aimerions que tu te joignes à nous."
    e "Je ne suis pas sûr..."
    o "A vrai dire, il y a quelqu'un en particulier qui tient énormément à ta présence."
    e "Ah ?"
    o "Je sais que Moira et toi êtes devenus très proches..."
    o "Aussi, j'ai décidé de t'offrir la main de ma fille !"
    jump credits

label bad_ending_12:
    "Les deux vikings rendent coup pour coup."
    "Mais le roi projette Einar contre le mur avant de se ruer sur lui."
    h "MEURS !"
    "Einar meurt étranglé par son roi, les vertèbres craquant sous l'étreinte du monarque."
    jump credits

label good_ending_13:
    "Sur le dos de son cheval chargé d'or, Einar s'éloigne peu à peu de Perth."
    "Les villageois lui font leurs adieux et petit à petit, la place se vide."
    "Mais alors qu'Einar est déjà loin, une seule personne reste à la sortie du village, regardant Einar s'éloigner inexorablement."
    "Moira."
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
    jump credits

label good_ending_15(marier):
    if marier:
        "Une tornade rousse se précipite vers les deux hommes."
        "Moira se jette dans les bras d'Einar et l'embrasse."
        ve "HOURRAAAA !"
    else:
        "Einar enfourche son cheval et part, seul avec ses pensées."
    jump credits

label bad_ending_16:
    "Harald effectue un moulinet rapide qui désarme Einar. En se retournant, il le fend en deux d'un seul coup et laisse le cadavre tomber au sol."
    "Le roi quitte la pièce en sifflotant."
    jump credits

label bad_ending_17:
    "En plein combat, une flèche vient frapper Einar à l'épaule."
    "Ogma profite de cette ouverture pour transperçer le viking de sa lame, et laisse tomber son cadavre dans les douves."
    jump credits

label normal_ending_18:
    "Le repas se poursuit toute la nuit, célébrant les exploits d'Einar autant que l'éradication des rebelles..."
    jump credits

label bad_ending_19:
    "Les regards d'Einar et Moira se croisent et se fixent."
    "Alors que les flammes commencent à la dévorer, elle ne hurle pas."
    "Elle contient toute sa rage et sa colère, adressant un regard de haine pure à Einar alors que des larmes coulent sur ses joues."
    "Dans les hurlements des prisonniers, les flammes de la rébellion s'éteignent."
    jump credits

label bad_ending_20:
    "Einar fend la foule, s'élance vers le bûcher et tente de détacher Moira."
    "Lorsqu'il parvient à trancher ses liens, un archer lui décoche une flèche dans l'abdomen."
    e "Argh... Cours ! Va t'en !"
    "Moira n'essaie même pas de bouger."
    "Elle arrache la hachette de la ceinture d'Einar et lui en assène un coup violent en travers de la gorge."
    "Alors qu'Einar s'effondre, il ne voit rien d'autre que les yeux larmoyants de haine de Moira."
    jump credits

label bad_ending_21:
    "Einar s'éloigne du château en enjambant sans distinction les cadavres écossais et vikings, tâchant ses vêtements dans la végétation imbibée de sang."
    "Derrière lui, Dunbar brûle."
    jump credits

label bad_ending_22:
    "Ogma atteint Einar."
    "Avant même que le viking n'ait pu esquisser le moindre mouvement, Ogma le massacre sur place."
    "L'écossais ne laisse rien de reconnaissable, continuant à frapper bien après la mort d'Einar."
    "Lorsque après de longues minutes il cesse d'abattre la Hache, il ne reste plus qu'une bouillie informe et rouge au milieu de la plaine."
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
