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
    "Au moment où Einar s'apprête à actionner le mécanisme de la porte, une flèche est décochée dans son dos."
    " Lorsqu'il se retourne pour voir d'où provient le tir, il voit Harald le désigner depuis la cour en donnant des ordres à ses archers. Une volée de flèches vient frapper Einar et le fait basculer par dessus les remparts."
    jump credits

label bad_ending_4:
    "A l'instant où Ogma franchit la porte, il se rue sur Einar. La furie sanguinaire d'Ogma est incontrôlable et Einar est massacré sur place."
    jump credits

label bad_ending_5:
    "Einar est massacré alors que les huscarls le transforment en une pulpe sanglante sous une pluie de coups."
    jump credits

label bad_ending_6:
    "Harald surgit au coeur de la mêlée, armé de sa hache. Il rassemble les vikings autour de lui et lance une contre-attaque imparable. Les rebelles sont balayés avec violence et Einar est décapité par le roi en personne"
    jump credits

label good_ending_7:
    "Ogma souligne la droiture et l'humilité d'Einar. Le chef rebelle annonce qu'il compte la faire fondre en une claymore pour sa famille, le clan Wallace."
    "Ogma annonce qu'il souhaite faire fondre la hache en une nouvelle épée, une claymore, qu'il déclare destinée à sa famille : le clan Wallace. Cette épée symbolise la destruction de l'oppression et l'émergence de la Liberté."
    jump credits

label good_ending_8:
    "Ogma remercie Einar d'avoir détruit la hache : il en aurait probablement fait un mauvais usage. C'est une preuve de sagesse que de savoir s'arrêter le moment venu. Einar reçoit sa part du trésor, comme convenu."
    jump credits

label good_ending_9:
    "Einar est à la tête d'une vaste armée et porte une tenue de général. Il s'apprête à affronter uner armée asiatique sur leurs propres terres."
    "Einar mène une armée innombrable face à ce qui semble être une armée asiatique"
    jump credits

label normal_ending_10:
    "Ogma s'empare de la hache et la brandit aux yeux de tous. Il tient alors un discours annonçant son ambition de \"libérer\" le reste de la Grande-Bretagne et pourquoi pas le reste de l'Europe. Le monde mérite un empereur écossais !"
    jump credits

label good_ending_11:
    "Revenus au village, Ogma félicite Einar et annonce publiquement qu'il lui donne la main de sa fille."
    jump credits

label bad_ending_12:
    "Einar meurt étranglé par son roi, ses vertèbres craquant sous l'étreinte du monarque."
    jump credits

label good_ending_13:
    "Revenus au village, Ogma félicite Einar. Il refuse cependant de marier sa fille, Moira, à un régicide."
    jump credits

label good_ending_14(rejete = True):
    if rejete:
        "Moira reste immobile au milieu du chemin alors qu'Einar la dépasse."
    else:
        "Elle court vers Einar et se jette dans ses bras."
    jump credits

label good_ending_15(marier = True):
    if marier:
        "Moira se jette dans les bras d'Einar et l'embrasse."
    else:
        "Einar décide continuer sa vie seul"
    jump credits

label bad_ending_16:
    "Dans le donjon, Einar tombe nez-à-nez avec Harald. Le roi est en position de force : il brandit sa hache sainte. D'un moulinet il désarme Einar avant de le fendre en deux sans effort."
    jump credits

label bad_ending_17:
    "En plein combat, une flèche vient frapper Einar à l'épaule. Ogma profite de cette ouverture pour transperçer le viking de sa lame, et laisse tomber son cadavre dans les douves."
    jump credits

label normal_ending_18:
    "Le soir, Harald annonce au cours d'un grand repas qu'il souhaite récompenser Einar en lui offrant des terres autour de Stirling, le village qu'il a ordonné de brûler quelques jours plus tôt."
    jump credits

label bad_ending_19:
    "Les bûchers prennent feu, un à un. Lorsque vient le tour de Moira, elle découvre Einar et leurs regardes se fixent. Alors que les flammes commencent à la dévorer, elle ne hurle pas."
    "Elle contient toute sa rage et sa colère, adressant un regard de haine pure à Einar alors que des larmes coulent sur ses joues."
    jump credits

label bad_ending_20:
    "Einar s'élance vers le bûcher et tente de détacher Moira. Il y parvient, mais un archer lui lance une flèche dans l'abdomen. Moira n'essaie même pas de s'enfuir."
    "Elle arrache sa hachette de la ceinture d'Einar et lui en assène un coup violent au milieu du dos."
    jump credits

label bad_ending_21:
    "Ogma s'adresse à Einar en lui disant qu'il lui était redevable pour la victoire sur Harald, mais que sa trahison envers les vikings et les rebelles a provoqué bien plus de morts que nécessaire. Aussi, il est banni d'Ecosse et privé de toute récompense."
    jump credits

label bad_ending_22:
    "Ogma s'élance vers Einar dès qu'il l'aperçoit, hache levée. Einar n'a même pas le temps d'engager le combat. Ogma se jette sur lui et le massacre, le démembrant et le rendant impossible à reconnaître."
    jump credits

label credits:
    scene bg black with dissolve
    with Pause(2.5)

    $ renpy.full_restart()
