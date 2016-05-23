#Ending
label bad_ending_1:
    "*Le meneur des assaillants tranche la gorge d'Einar, de la même manière que Logan. Après de longues minutes à se noyer dans son propre sang, Einar meurt.*"
    jump credits

label bad_ending_2:
    e "Je n'ai qu'une parole. Vous pouvez aller vous faire foutre."
    o "C'est décevant... Tu crois être unique ? Si ce n'est pas toi, un autre fera le travail à ta place."
    "*Ogma égorge Einar alors qu'il est entravé.*"
    e "Grrblbhh..."
    "Après s'être étouffé avec son propre sang, Einar meurt. Son corps est alors ramené sur les lieux de l'embuscade et est laissé à pourrir aux côtés de ses compagnons."
    jump credits

label bad_ending_3:
    "*Au moment où Einar s'apprête à actionner le mécanisme de la porte, une flèche est décochée dans son dos.*"
    "*Lorsqu'il se retourne pour voir d'où provient le tir, il voit Harald le désigner depuis la cour en donnant des ordres à ses archers.*"
    "*Une volée de flèches vient frapper Einar et le fait basculer par dessus les remparts.*"
    jump credits

label bad_ending_4:
    "*La furie sanguinaire d'Ogma est incontrôlable et Einar est massacré sur place.*"
    "*Alors que les rebelles continuent d'affluer dans l'enceinte, Ogma tombe à genoux devant le cadavre d'Einar.*"
    o "Grrr..."
    "*Il tire une dague et commence à poignarder et mutiler sans relâche les restes du viking...*"
    jump credits

label bad_ending_5:
    "*Les forces coordonnées des huscarls surpassent le talent d'Einar, qui est jeté au sol.*"
    "*Les huscarls le transforment en une pulpe sanglante sous une pluie de coups furieux.*"
    jump credits

label bad_ending_6:
    "*Harald décapite Einar d'un coup unique et ample, sans lui laisser le temps de répliquer.*"
    h "Et maintenant, au tour des écossais..."
    jump credits

label good_ending_7:
    e "Voici la Hache."
    o "Merci beaucoup. Combien auraient cédé à l'appel du pouvoir ?"
    o "Peu d'hommes auraient eu ta droiture et ton humilité !"
    e "Vous allez détruire la Hache ?"
    o "Oui. Je la ferai fondre en une arme nouvelle, une claymore."
    o "Elle sera destinée à ma famille, le clan Wallace. Elle symbolisera la fin de l'oppression et l'émergence de la Liberté !"
    ge "HOURRAAA !"

    jump credits

label good_ending_8:
    "Ogma remercie Einar d'avoir détruit la hache : il en aurait probablement fait un mauvais usage. C'est une preuve de sagesse que de savoir s'arrêter le moment venu. Einar reçoit sa part du trésor, comme convenu."
    jump credits

label good_ending_9:
    "*Einar porte une tenue de général et mène une armée innombrable face à ce qui semble être une armée asiatique, dans un paysage exotique fait de montagnes et de cultures en étages.*"
    e "Aujourd'hui, le dernier peuple dissident s'inclinera devant nous !"
    e "CHARGEEEEEEEEZ !"
    jump credits

label normal_ending_10:
    "Ogma s'empare de la hache et la brandit aux yeux de tous. Il tient alors un discours annonçant son ambition de \"libérer\" le reste de la Grande-Bretagne et pourquoi pas le reste de l'Europe. Le monde mérite un empereur écossais !"
    jump credits

label good_ending_11:
    "Revenus au village, Ogma félicite Einar et annonce publiquement qu'il lui donne la main de sa fille."
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
    "*Les deux vikings rendent coup pour coup.*"
    "*Mais le roi projette Einar contre le mur avant de se ruer sur lui.*"
    h "MEURS !"
    "*Einar meurt étranglé par son roi, les vertèbres craquant sous l'étreinte du monarque.*"
    jump credits

label good_ending_13:
    "*Sur le dos de son cheval chargé d'or, Einar s'éloigne peu à peu de Perth.*"
    "*Les villageois lui font leurs adieux et petit à petit, la place se vide.*"
    "*Mais alors qu'Einar est déjà loin, une seule personne reste à la sortie du village, regardant Einar s'éloigner inexorablement.*"
    "*Moira.*"
    jump credits

label good_ending_14(rejete = True):
    if rejete:
        "*Einar dépasse Moira qui reste immobile au milieu du sentier, les poings serrés, fixant le sol.*"
    else:
        m "Où allons-nous ?"
        e "Loin d'ici !"
        e "Quand ton père aura compris que tu t'es enfuie pour m'accompagner, il se lancera à notre recherche."
        e "Et je n'ai aucune envie de me retrouver à nouveau enfermé dans une cahutte pendant un mois !"
        m "Ha ha ha !"
        e "Il y a un endroit en particulier que tu voudrais voir ?"
        m "Je ne sais pas... J'hésite entre la Norvège et la Méditerrannée."
        e "Alors nous irons voir la Méditerrannée ! Retourner en Norvège, ce serait du suicide..."
        "*Les deux voyageurs disparaissent dans les bois, prenant la direction du sud...*"
    jump credits

label good_ending_15(marier = True):
    if marier:
        "*Une tornade rousse se précipite vers les deux hommes.*"
        "*Moira se jette dans les bras d'Einar et l'embrasse.*"
        ve "HOURRAAAA !"
    else:
        "*Einar enfourche son cheval et part, seul avec ses pensées.*"
    jump credits

label bad_ending_16:
    "*Harald effectue un moulinet rapide qui désarme Einar. En se retournant, il le fend en deux d'un seul coup et laisse le cadavre tomber au sol.*" 
    "*Le roi quitte la pièce en marchant.*"
    jump credits

label bad_ending_17:
    "*En plein combat, une flèche vient frapper Einar à l'épaule.*"
    "*Ogma profite de cette ouverture pour transperçer le viking de sa lame, et laisse tomber son cadavre dans les douves.*"
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
    "Einar s'éloigne du château en enjambant sans distinction les cadavres écossais et vikings, tâchant ses vêtements dans la végétation imbibée de sang. Derrière lui, Dunbar brûle."
    jump credits

label bad_ending_22:
    "Ogma atteint Einar."
    "Avant même que le viking n'ait pu esquisser le moindre mouvement, Ogma le massacre sur place."
    "L'écossais ne laisse rien de reconnaissable, continuant à frapper bien après la mort d'Einar."
    "Lorsque après de longues minutes il cesse d'abattre la Hache, il ne reste plus qu'une bouillie informe et rouge au milieu de la plaine."
    jump credits

label credits:
    scene bg black with dissolve
    with Pause(2.5)

    $ renpy.full_restart()
