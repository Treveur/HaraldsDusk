#Acte 3

#Sequence 1
label cote_2S:

    play ambiance coast

    scene bg plaine_chateau_matin with dissolve

    "Et après trois jours de marche depuis Perth..."

    show einar debout_normal_mid at center with dissolve

    e "Dunbar. Déjà..."
    e "..."

    jump exterieur_chateau_1S

#Sequence 2
label exterieur_chateau_1S:

    stop ambiance
    #play ambiance castle

    scene bg chateau_porte with dissolve

    show einar debout_normal_mid at left with moveinleft
    show gv debout_normaux_mid at right with dissolve

    e "Je ne saurais pas dire si je suis content de revoir leurs trognes..."

    gc "Einar ! C'est bien toi ?"
    e "..."
    gc "Tout le monde te croyait mort !"
    gc "Qu'est-il arrivé aux autres ?"

    menu :

        "Pousse-toi":
            show einar debout_determine_mid at left
            e "Écarte-toi, Geir! Je dois parler au roi sans tarder !"
            gc "Bien sûr, excuse-moi."

        "Pas mal de choses...":
            e "Il m'est arrivé toutes sorte de chose que je n'ai ni le temps ni l'envie de te raconter. Les autres sont tous morts et j'ai bien failli y passer aussi."
            e "Maintenant, laisse-moi passer."
            gc "Bien sûr, excuse-moi."

        "Ne me barre pas la route !":
            show einar debout_determine_mid at left
            e "Laisse-moi passer, andouille. On ne barre pas la route à un huscarl ! Je dois voir le roi au plus vite !"
            gc "Bien sûr, excuse-moi."


    hide gv with dissolve
    hide einar with dissolve

    jump cour_chateau_1S

#Sequence 3
label cour_chateau_1S:

    #Augmenter le son progressivement
    #play ambiance castle

    $ retour_silence_1 = False
    $ soupcon_harald_1 = False
    $ mentir_harald_1 = False
    $ interpose_bucher = False

    scene bg cour_chateau with dissolve

    "Harald est en grande discussion avec un huscarl au milieu de la cour"

    show einar debout_normal_mid at left with dissolve
    e "Sire ! Sire !"
    show harald debout_normal_mid at right with dissolve
    h "... doit nous faire venir de nouveaux navires de guerre, et..."
    h "Einar ? Que... D'où viens-tu ? Où as-tu passé tout ce temps ? Où sont tes compagnons ? J'ai beaucoup de questions à te poser !"

    menu:

        "Je suis content de vous revoir":
            show einar debout_souriant_mid at left
            e "Quel plaisir de vous retrouver, mon roi !"
            h "La surprise est bonne ! Je désesperais de te revoir un jour. J'étais convaincu d'avoir perdu l'un de mes meilleurs huscarls !"
            h "A vrai dire, je tenais pour acquis que tu étais mort quelque part dans le nord, victime des rebelles..."

        "J'ai cru ne pas pouvoir revenir":
            show einar debout_attriste_mid at left
            e "J'ai bien cru ne jamais revenir, sire."
            h "Eh bien après tous ce temps, on te croyait mort. J'étais persuadé que toi et tes compagnons étiez morts de la main des rebelles !"
            h "J'ai d'ailleurs passé tout le temps depuis ta disparition à envoyer des troupes raser l'Ecosse. Ces ordures de rebelles finiront par se montrer en voyant leur peuple se faire exterminer."
            h "Crois-moi, les écossais ont payé le prix fort pour votre disparition, à toi et tes hommes !"
            show einar debout_souriant_mid at left
            e "C'est un honneur que d'être vengé par son roi !"

        "Ne rien dire":
            show einar debout_attriste_mid at left
            e "..."
            h "J'imagine que tu as dû vivre des choses terribles..."

    h "Mais dis-moi, que t'est-il arrivé ?"
    h "Et l'escorte qui t'accompagnait ? Et Logan ?"

    menu:
        "Je n'en sais rien (mentir)":
            show einar debout_normal_mid at left
            e "Je ne sais pas. Nous traversions une forêt en pleine nuit. J'ai été assommé... A mon réveil, il n'y avait plus personne et j'étais abandonné au fond d'un fossé."
            h "Un fossé ?"
            e "Oui, au détour d'un sentier en pleine forêt."
            h "Et tes blessures ? Comment les as-tu soignées ?"
            jump menu_assome_cour_chateauS

        "Nous sommes tombés dans une embuscade":
        #modifaction pour indiquer le lieu par la suite
            show einar debout_normal_mid at left
            e "Nous venions de traverser le village de Perth, que nous soupçonnions d'abriter les rebelles."
            e "Nous étions ensuite repartis. Les hommes discutaient entre eux, nous étions sûrs de nous. Puis la nuit est tombée."
            e "Il nous ont prit au dépourvu. Une bande d'une trentaine de guerriers écossais nous est tombée dessus sans que nous ne puissions nous défendre."
            show einar debout_attriste_mid at left
            e "Des archers dissimulés dans l'obscurité ont lancé une salve qui a touché un grand nombre des nôtres."
            e "Ensuite, le meneur s'est approché de moi. Il a égorgé Logan sous mes yeux puis m'a assommé."
            h "Qui t'a soigné ? Tu devais être blessé... Je te connais, rien ne t'arrête jamais quand il s'agit de combattre !"

            jump menu_embuscade_ou_silence_cour_chateauS

        "Ne rien dire":
            show einar debout_attriste_mid at left
            e "..."
            h "Tu dois tout me raconter, Einar. Je ne suis pas idiot, je sais que tes compagnons sont morts. C'est évident. Pourquoi serais-tu revenu seul, sinon ?"
            h "Tu dois me dire ce qu'il s'est passé. Nous devons venger la mort de nos hommes ! Nous devons éradiquer les rebelles !"

            $ retour_silence_1 = True

            jump menu_embuscade_ou_silence_cour_chateauS


    menu menu_assome_cour_chateauS:

        "Je me suis débrouillé (mentir)":
            show einar debout_normal_mid at left
            e "Je me suis remis, lentement mais sûrement, dans la nature."
            "Harald hausse les sourcils"
            h "Dans la nature ? J'ai du mal à te croire..."
            e "J'ai trouvé des plantes et des baies qui m'ont permit de me soigner."
            h "Mmmh..."
            $ soupcon_harald_1 = True

        "J'ai reçu l'aide d'un autochtone (mentir)":
            show einar debout_normal_mid at left
            e "J'ai été soigné par un vieux paysan."
            h "Un paysan ?"
            e "Oui. Il s'appelait Murray. C'était un brave homme. Il m'a trouvé alors qu'il emmenait paître ses moutons. Lorsqu'il a vu mes blessures, il a eu pitié de moi."
            e "Il m'a gardé dans sa cabane pendant un mois entier, à me soigner et à me nourrir."
            e "Une fois remis sur pieds, il m'a laissé partir. Je lui ai promis de le dédommager quand je le pourrais, et il a refusé !"
            h "Tu as eu bien de la chance de tomber sur un homme pareil. Certains t'auraient égorgé sur place."

    menu menu_embuscade_ou_silence_cour_chateauS:

        "Je me suis retrouvé dans un village, des gens m'ont aidé":
            show einar debout_normal_mid at left
            e "J'ai été aidé par le village que nous avions visité un peu plus tôt, Perth."
            e "Un chasseur m'a trouvé alors qu'il allait relever des collets. Il m'a ramené à son village puis sa fille s'est occupée de moi. Elle s'appelait Moira."
            e "Pendant un mois, cette jeune femme m'a prodigué les soins nécessaires. Lorsqu'enfin mon état s'est amélioré, j'ai pu repartir."
            h "Il ne s'agissait donc pas des rebelles ?"
            e "..."

        "J'ai reçu l'aide d'un autochtone (mentir)":
            show einar debout_normal_mid at left
            e "J'ai été soigné par un vieux paysan."
            h "Un paysan ?"
            e "Oui. Il s'appelait Murray. C'était un brave homme. Il m'a trouvé alors qu'il emmenait paître ses moutons. Lorsqu'il a vu mes blessures, il a eu pitié de moi."
            e "Il m'a gardé dans sa cabane pendant un mois entier, à me soigner et à me nourrir."
            e "Une fois remis sur pieds, il m'a laissé partir. Je lui ai promis de le dédommager quand je le pourrais, et il a refusé !"
            h "Tu as eu bien de la chance de tomber sur un homme pareil. Certains t'auraient égorgé sur place."

        "J'ai perdu la mémoire (mentir)" if retour_silence_1:
            show einar debout_normal_mid at left
            e "Je ne me rappelle de rien... Simplement de ce coup à la tête."
            e "Après, il n'y a qu'un grand vide jusqu'à il y a trois jours, lorsque je me suis réveillé dans les bois."
            e "Mes blessures étaient soignées et un repas était posé à côté de moi. Je l'ai mangé et ai prit la route pour revenir jusqu'ici."
            $ soupcon_harald_1 = True

    h "..."
    show einar debout_normal_close at left with dissolve
    show harald debout_determine_close at right with dissolve
    h "J'espère que tout ce que tu me dis là est vrai."
    h "Je ne tolère pas le mensonge, Einar. Ton histoire me paraît bien obscure. Je te fais confiance, mais si j'apprends que tu m'as menti..."
    h "Es-tu certain de m'avoir dit la vérité ? Si ce n'est pas le cas, je suis prêt à te pardonner pourvu que tu m'avoues ce qu'il s'est réellement passé."
    e "(C'est maintenant ou jamais...)"

    menu :
        "Voici toute la vérité":
            show einar debout_normal_close at left
            e "Très bien. Voici la vérité."
            e "Après avoir traversé le village de Perth, nous sommes tombés dans une embuscade des rebelles. Ils avaient probablement été prévenus de notre arrivée."
            show einar debout_attriste_close at left
            e "Tous mes compagnons sont morts, y compris Logan."
            h "Et toi ? Tu t'es enfui ?"
            e "Non. Alors que j'avais été mis à terre, le meneur des rebelles s'est approché de moi. J'ai cru mon heure arrivée."
            e "Il s'est penché sur moi puis m'a demandé de coopérer. Je n'ai pas eu d'autre choix que d'accepter."
            e "J'ai ensuite été assommé. A mon réveil, j'étais dans l'une de ces maisons écossaises, comme nous en avions vu au village."
            show einar debout_normal_close at left
            e "Pendant un mois, une jeune femme s'est occupée de moi. Elle s'appelait Moira et était la fille du meneur des rebelles, Ogma le Hurleur."
            h "Ogma le Hurleur ? Ce n'est pas un nom..."
            e "Dans ce cas, je ne connaît pas sa véritable identité."
            e "Lorsqu'enfin mes blessures étaient guéries, un mois s'était écoulé. Alors que je m'apprêtais à partir, Ogma m'a rappelé mon engagement."
            h "Ton engagement ?"
            e "Oui. Il était question que je survive à condition que je vous trahisse en ouvrant le pont-levis du château aux rebelles."
            h "Ils comptent lancer une attaque ? Quand !?"
            e "Hélas, je n'en sais rien, sire. Mais je présage que cet assaut aura lieu très prochainement."
            e "Quoi qu'il en soit, je n'ai jamais cessé de vous être fidèle. Tout ce que j'ai fait, c'était dans votre intérêt. J'ai patiemment attendu le moment où je pourrais vous révéler leurs intentions. Et voilà."

        "Je vous suis fidèle (mentir)":
            show einar debout_determine_close at left
            e "Nul ne vous est plus fidèle que moi !"
            $ mentir_harald_1 = True

        "J'ai rusé dans votre intérêt (mentir)":
            show einar debout_determine_close at left
            e "J'ai rusé de toutes les manières possibles uniquement dans le but de revenir à votre service."
            $ mentir_harald_1 = True

    if mentir_harald_1:
        show einar debout_normal_close at left
        h "Je te remercie pour ta sincérité, Einar."
        show harald debout_determine_close at right
        h "Grâce à toi, nous allons profiter de toutes les informations que tu as pu glâner pendant ce mois dans les Highlands."
        show harald debout_normal_close at right
        h "Mais pour le moment tu devrais rejoindre les autres soldats. Ils seront heureux de retrouver l'un des leurs."
        e "Bien mon Roi."

    else:
        show harald debout_contrarie_close at right
        show einar debout_normal_close at left
        h "Si ces salopards comptent attaquer prochainement,il faut impérativement préparer nos défenses !"
        e "Le château n'est pas suffisant ?"
        h "Si, mais uniquement si les hommes qui le défendent sont à leurs postes !"
        h "Je te remercie de m'avoir tout avoué. J'ai eu des doutes sur toi pendant un instant, mais me voilà rassuré."
        show harald debout_determine_close at right
        h "Pendant que je vais planifier la défense du château, tu devrais aller à la rencontre des autres soldats. Ils seront heureux de te retrouver."
        h "Les morts ne reviennent pas tous les jours !"
        show einar debout_souriant_close at left
        e "Bien mon Roi."

    hide einar
    hide harald


    #play ambiance buchet
#    "Un grand nombre de vikings est massé autour de trois bûchers. Des écossais y sont attachés."

#    show patrick debout_normal_mid at center with dissolve

#    p "Que Dieu, ait pitié de vous ! Les flammes purificatrices vont laver tous vos pêchés."
#    p "Deus propitius tibi!"

#    show patrick debout_normal_mid at left
#    show ve buchet_normaux_mid at right with dissolve

#    pe3 "Arrêtez ! Je suis enceinte !"
#    show patrick debout_furieux_mid at left
#    p "Je n'ai que faire de tes mensonges, femme !"
#    p "Tes ruses perfides n'obscurciront pas mon jugement !"

#    hide ve
#    show einar debout_normal_mid at left with dissolve
#    show patrick debout_normal_mid at right

#    menu:
#        "Arrêtez le massacre !":
#            show einar debout_furieux_mid at left
#            e "Stop! Arrêtez-tout, ce ne sont que de simples paysans !"
#            show patrick debout_normal_mid at right
#            p "Einar ? Tu étais porté disparu depuis un mois !"
#            show patrick debout_furieux_mid at right
#            p "Et te voilà sorti de nul part, prêt à défendre ces hérétiques !"
#            p "Ces gens ne sont pas innocents ! Ils ont été capturés alors qu'ils menacaient de m'assassiner !"
#            show einar debout_attriste_mid at left
#            e "Une femme enceinte ? Y croyez-vous vraiment, Excellence ?"
#            p "Elle était avec eux lorsque nous les avons capturés. Elle ne peut être innocente : elle a avoué !"
#            show einar debout_furieux_mid at left
#            e "Sous la torture ? Vous auriez pu lui faire avouer n'importe quoi !"
#            p "Comment peux-tu savoir que ces gens sont innocents ? As-tu des révélations à nous faire ?"

#            $ interpose_bucher = True

#            jump menu_sauver_rebelle_cour_chateau

#        "Ne rien dire":
#            show einar debout_attriste_mid at left
#            e "..."

#        "Brûlez-les":
#            show einar debout_determine_mid at left
#            e "Vous avez raison, Excellence !"
#            e "Brûlez-les !"

#    if interpose_bucher:

#        menu menu_sauver_rebelle_cour_chateau:
#            "Je ne les ai pas vus à Perth":
#                show einar debout_normal_mid at left
#                e "Je ne les ai pas vus lorsque j'étais parmi les rebelles de Perth."
#                e "Ils ne peuvent donc pas être avec les rebelles que nous recherchons !"
#                show patrick debout_furieux_mid at right
#                p "Mensonge ! Ils ont tenté de m'assassiner ! Ils ont tout avoué !"
#                p "Ils se sont opposés à un homme de Dieu et ont agi à l'encontre du porteur de la Hache Sainte !"

#                if mentir_harald_1 == False and soupcon_harald_1 == False:
#                    $ soupcon_harald_1 = True

#            "Ils ont l'air innoffensifs":
#                show einar debout_normal_mid at left
#                e "Je ne sais rien d'eux, mais croyez-vous vraiment que ces trois paysans soient responsables d''une tentative d'assassinat ?"
#                e "Une mère ne mettrait pas la vie de son enfant en danger !"

#        show patrick debout_normal_mid at right
#        p "Ne t'interpose pas avec la volonté de Dieu !"
#        p "Je pourrais croire que tu cherches à leur épargner le châtiment qu'ils méritent..."
#        p "Et tu vois toi-même le sort réservé aux traîtres !"

#    show patrick debout_normal_mid at right
#    p "Amenez les torches, et que brûlent les hérétiques !"

#    show patrick debout_furieux_mid at left
#    show ve buchet_pleurent at right

#    #A intégrer plus tards

#    pe1 "Pitié ! Epargnez ma femme !"
#    pe3 "Je porte un enfant ! Vous ne pouvez pas faire ça !"
#    pe2 "Laissez partir les autres ! Je suis responsable de tout !"

#    show patrick debout_furieux_mid at left
#    p "Plus rien ne vous sauvera, misérables ! Que s'accomplisse le châtiment !"

#    hide patrick
#    hide ve
#    with dissolve

#    "Un homme apporte une torche. Un par un, il allume les bûchers."

#    show gv debout_rire with dissolve

#    gv "Regardez-les s'agiter comme des vers, ha ha !"
#    hide gv with dissolve

#    show einar debout_normal_mid at left with dissolve
#    show jgv debout_normal_mid at right with dissolve

#    "Alors que l'assistance se réjouit devant ce triste spectacle, Einar remarque un jeune soldat en retrait."
#    "Le soldat semble mal à l'aise et au bord des larmes. Einar se dirige vers lui."

#    #Variable
#    $ reponse_reconfort = ""

#    menu :

#        "Une bande de porcs qui rôtissent !":
#            show einar debout_souriant_close at left
#            e "Ha, souris un peu, gamin ! Ecoute leur graisse bouillir, à ces porcs !"
#            $ reponse_reconfort = "pleurer"

#        "Ne pleure pas ces parasites":
#            e "Ne pleure pas ces parasites, ils ne le méritent pas."
#            show einar debout_determine_close at left
#            e "Le roi nous a fait venir ici précisément pour punir les traîtres et les infidèles. "
#            e "Alors réjouis-toi, gamin ! En voilà trois de moins !"
#            $ reponse_reconfort = "pleurer"

#        "Nous n'y pouvons rien":
#            show einar debout_attriste_close at left
#            e "Tu n'aurais rien pu faire. L'évêque est un malade sanguinaire."
#            $ reponse_reconfort = "larme_aux_yeux"

#        "Ne rien dire":
#            show einar debout_attriste_close at left
#            e "..."
#            $ reponse_reconfort = "larme_aux_yeux"

#        "L'évêque peut se tromper, mais pas Dieu":
#            e "L'évêque peut se tromper, mais pas le Seigneur. S'ils étaient justes, les condamnés iront au paradis."
#            $ reponse_reconfort = "rassure"

#    if reponse_reconfort == "pleurer":
#        show jgv debout_pleurant_close at right
#        "Le jeune soldat pleure sans se cacher."
#    elif reponse_reconfort == "larme_aux_yeux":
#        show jgv debout_pleurant_close at right
#        "Le jeune soldat semble toujours aussi bouleversé."
#    else:
#        "Le jeune soldat semble rassuré."

#    hide einar
#    hide jgv

#    jump cour_chateau_2

#Sequence 4
label cour_chateau_2S:

    #toujours ambiance chateau
    show bg cour_chateau_crepuscule with dissolve

    "Au crépuscule..."
    show gv debout_normaux_mid at left with dissolve
    show harald debout_normal_mid at right with dissolve
    gv "Sire ! Sire !"
    h "Qu'y a-t-il ? Parle !"
    gv "Hjalmar vient de repérer des centaines de torches sorties de la forêt ! Ils convergent tous vers le château !"
    show harald debout_furieux_mid at right
    h "Les chiens, ils ne manquent pas d'audace ! Ils lancent déjà leur attaque !"
    show harald combat_determine_mid at right

    h "Tous à vos postes de combat ! Huscarls, préparez-vous à défendre la porte ! Je veux vingt archers sur les remparts !"
    "Une fois ses ordres donnés, Harald disparaît dans le donjon."

    hide harald
    hide gv

    jump interieur_grande_porte_chateau_1S

#Sequence 5
label interieur_grande_porte_chateau_1S:

    #interieur chateau
    #play ambiance interieur_castle

    show bg chateau_porte_interieur_crepuscule with dissolve

    show gv debout_enthousiastes_mid with dissolve
    gv "Ha ha ! Depuis le temps que j'attendais ça ! On va casser du rebelle !"
    hide gv
    "La horde progresse en courant à travers la plaine."
    "A une centaine de mètres du château, un double son de cor retentit : le signal convenu avec Ogma pour ouvrir le pont-levis."
    play sound double_horn

    "Einar est posté à proximité du système d'ouverture des portes."


    menu:
        "Ouvrir le pont-levis":

            play sound drawbrigde
            pause (3)

            hide einar
            if soupcon_harald_1:
                jump bad_ending_3
            else:
                jump pont_levis_baisseS

        "Laisser fermé":
            hide einar
            if soupcon_harald_1:
                jump soupcon_harald_defendre_porteS
            else:
                jump harald_defendre_porteS


#Baisser pont-levis
label pont_levis_baisseS:

    #???
    #Ambiance bruit cliqueti boucliers et épée
    show gv combat_normaux_mid at center with dissolve

    gv "Attendez... Attendez..."
    gv "Tirez ! Abattez-moi ces salopards !"
    "Une volée de flèches abat une partie des rebelles qui foncent vers le château."
    "Le pont s'abaisse brutalement, laissant le champ libre."
    gv "Trahison ! Bloquez le passage, vite !"
    "..."

    "Les soldats proches se tournent vers Einar."

    show gv combat_normaux_mid at right
    show einar debout_normal_mid at left with dissolve

    menu:

        "Reculez !":
            show einar combat_determine_mid at left
            e "Arrière ! Je vous ferai rendre gorge !"

        "C'est une tactique du roi":
            show einar combat_normal_mid at left
            e "C'était une tactique imaginée par notre roi !"

        "Venez, je vous attends !":
            show einar combat_furieux_mid at left
            e "Tuez-moi, chiens. Mieux vaut être un traître qu'un oppresseur !"

        "Ne rien dire":
            show einar debout_furieux_mid at left
            e "..."

    hide gv
    hide einar
    with dissolve

    "La horde avance en une masse compacte et nombre de rebelles succombent sous les flèches des vikings."
    "Le gros des forces parvient à franchir le pont-levis et la masse rebelle déferle dans l'enceinte."
    "Au même moment, la horde rebelle pénètre l'enceinte, ce qui détourne l'attention des soldats qui attaquaient Einar."
    show re debout_enthousiastes_mid at left
    show gv debout_determines_mid at right
    with dissolve
    #Ajouter un shake camera
    ge "HAAAAA !"
    gv "En formation ! Dressez les boucliers ! Aucun rebelle ne foutra un pied dans cette enceinte !"

    play ambiance fight

    hide gv
    hide re
    with dissolve

    if moira_dead:

        "Ogma surgit au milieu de la mêlée, franchissant la Grande Porte. Il se rue sur Einar, un regard fou dans les yeux et la bave aux lèvres. Il hurle le nom de sa fille."

        show einar debout_normal_mid at left
        show ogma combat_furieux_mid at right
        with dissolve


        o "MOIRAAAAAAAA !"
        o "POURQUOI L'AVOIR TUÉE ?"

        menu:

            "J'avais juste envie":
                show einar combat_normal_mid at left
                e "L'envie de voir de près un salopard d'écossais déborder de rage !"

            "Votre fille m'insupportait":
                show einar combat_furieux_mid at left
                e "J'aimais votre cause, pas votre fille !"

            "C'est parti tout seul":
                show einar combat_normal_mid at left
                e "Je n'ai pas réfléchi !"

            "Viens te battre !":
                show einar combat_determine_mid at left
                e "Ferme la et bats-toi, raclure !"

        show ogma combat_determine_mid at right
        o "Tout s'achève, ici et maintenant !"

        #Phase combat impossible à gagner WIP
        $ time = 5
        $ timer_range = 5
        $ timer_jump = 'game_over_combat'

        "Ogma se jette sur Einar, levant son épée pour préparer une attaque haute !"

        show screen countdown
        menu :

            "Esquiver":
                hide screen countdown
                "Abattant son épée sur le sol, Ogma manque Einar de justesse."

            "Attaquer":
                hide screen countdown
                "Ogma détourne le coup d'Einar et le frappe au flanc."
                jump game_over_combat

        $ time = 2.5
        $ timer_range = 2.5
        $ timer_jump = 'game_over_combat'

        "Fou de rage, Ogma attaque une fois de plus vers la droite, d'un coup de taille."

        show screen countdown

        menu :
            "Parer":
                hide screen countdown
                "Einar parvient à bloquer l'attaque, mais Ogma profite du contrecoup pour asséner au viking un violent coup de pied à l'estomac."
                "Ogma enchaîne immédiatement, d'un geste fulgurant !"

            "Esquiver":
                hide screen countdown
                "Einar effectue une roulage pour esquiver l'attaque mais Ogma est bien trop rapide et furieux : il lance immédiatement une seconde attaque !"

        $ time = 0.5
        $ timer_range = 0.5
        $ timer_jump = 'game_over_combat'

        "Dans un hurlement bestial, Ogma prend Einar à contre-pied et tente un nouveau coup de taille. Il y a une ouverture dans sa garde !"

        show screen countdown

        menu :
            "Attaquer":
                hide screen countdown
                "Einar plonge dans la garde ouverte d'Ogma. Mais c'était une ruse !"
                "Ogma tourne sur lui-même et empale le viking sur son épée."

            "Esquiver":
                hide screen countdown
                "Le coup est bien trop rapide pour être esquivé, et les appuis d'Einar sont faibles : le ventre du viking s'ouvre, déversant un torrent de viscères sur le sol."


        hide einar
        hide ogma
        with dissolve

        jump bad_ending_4

    else:

        "Pris entre les deux forces, Einar se retrouve face à ses anciens confrères huscarls."

        show einar combat_normal_mid at left
        show huscarls combat_normaux_mid at right
        with dissolve

        hu "Tu as trahi les tiens pour ça ? Pour rejoindre des paysans ?"
        hu "Ha, il a du tomber sur un beau garçon de ferme !"
        hu "Défend-toi, traître !"

        #"Affronter ses anciens confrères huscarls. WIP"
        #Phase combat

        $ time = 3
        $ timer_range = 3
        $ timer_jump = 'game_over_combat'


        "Les huscarls encerclent Einar pour ne lui laisser aucune chance. Une pluie de haches s'abat sur Einar !"

        show screen countdown
        menu:

            "Parer":
                hide screen countdown
                "Uniquement armé de sa hache, Einar ne parvient pas à se protéger : les huscarls prennent le dessus."

            "Attaquer":
                hide screen countdown
                "Einar contre-attaque furieusement, faisant reculer la masse des guerriers d'élite."
                jump game_over_combat

        $ time = 4
        $ timer_range = 4
        $ timer_jump = 'game_over_combat'

        "Les huscarls tentent de consolider leur cercle et d'attaquer Einar sur ses arrières !"

        show screen countdown

        menu :
            "Attaque ample":
                hide screen countdown
                "D'un coup ample et rapide, Einar parvient à désarmer et blesser plusieurs de ses opposants."
                "Le cercle d'assaillants se fragmente, et les rebelles profitent de cet instant pour attaquer les huscarls à leur tour."

            "Attaque précise":
                hide screen countdown
                "Einar tranche la tête d'un huscarl, mais l'un des guerriers d'élite atteint Einar dans le dos."
                "La colonne vertébrale brisée, Einar s'écroule."
                jump bad_ending_5

        "Ogma rejoint la mêlée et trouve Einar entrain d'achever un huscarl."
        show einar combat_normal_mid at left
        show ogma combat_normal_mid at right
        with dissolve
        o "Einar ! Ne reste pas ici ! Tu dois incendier le donjon, vite !"
        e "Le donjon ? Pourquoi ?"
        o "Si Harald n'est pas encore entrain de se battre, c'est parce qu'il n'a pas encore fini de s'équiper !"
        show ogma combat_determine_mid at right
        o "Nous pouvons le prendre au piège ! Le donjon doit brûler !"

        menu :

            "Ne me donne pas d'ordres":
                show einar combat_normal_mid at left
                e "Je n'ai pas d'ordres à recevoir !"

                hide einar
                hide ogma
                with dissolve

                jump e_bruler_donjon_desobeir_donjonS

            "J'y vais !":
                show einar combat_determine_mid at left
                e "J'y vais!"
                hide einar
                hide ogma
                with dissolve
                jump e_bruler_donjon_obeir_donjonS

label e_bruler_donjon_desobeir_donjonS:

    "Le jeune soldat qui pleurait lors du jugement survient face à Einar. Il a l'air terrorisé mais résolu, et tue un rebelle."

    show einar combat_normal_mid at left
    show jgv debout_normal_mid at right
    with dissolve

    menu :

        "Désolé (le tuer)":
            show einar combat_determine_mid at left
            e "Désolé, petit. Nous ne sommes plus dans le même camp."
            "Einar fend l'épaule du soldat jusqu'à atteindre son coeur, le tuant instantanément."

        "Saisi ta chance (l'assommer)":
            show einar combat_determine_mid at left
            e "Je t'offre l'occasion de refaire ta vie, saisi-la."
            "Du plat de sa hache, Einar frappe le soldat à la tempe. Il s'écroule à terre, inconscient"

        "L'ignorer":
            #animation einar sortir
            e "(Je n'ai pas le temps de m'occuper de lui.)"

    "Harald jaillit du donjon, protégé par son armure et portant la terrible Hache Sainte."

    show harald combat_hache_determine_mid at center
    show huscarls combat_enthousiaste_mid at right

    h "A moi, huscarls ! Suivez votre roi !"
    hu "HAAAAAA !"
    "Harald se jette dans les combats et taille un chemin sanglant jusqu'à la porte. Ragaillardis par la présence du roi-empereur, les vikings repoussent les rebelles."

    hide huscarls with dissolve
    show einar combat_normal_mid at left with dissolve

    "Harald arrive devant Einar, couvert du sang de ses victimes."


    show harald combat_hache_normal_mid at right
    h "Je te libère de ton allégeance. Je n'ai plus besoin de tes services."

    menu:
        "Sans regrets !":
            show einar combat_determine_mid at left with dissolve
            e "Je ne regrette rien."

        "Pardon":
            show einar debout_attriste_mid at left with dissolve
            e "Je regrette tout et vous demande pardon, Sire."

        "Je ne vois aucun roi !":
            show einar combat_normal_mid at left with dissolve
            e "Je ne vois aucun souverain ici..."
            show einar combat_furieux_mid at left
            e "Il n'y a personne pour me libérer d'une allégeance quelconque !"

    show harald combat_hache_furieux_mid at right
    h "Garde ta langue de traître derrière tes dents !"

    jump bad_ending_6

label e_bruler_donjon_obeir_donjonS:

    $ prendre_hache = False

    #Animation
    "Einar s'élance en direction du donjon, passant à l'arrière des affrontements."
    "Dans le donjon, Einar s'empare d'une torche et commence à mettre le feu aux tapisseries."
    "..."
    "En se déplacant dans les couloirs, Einar voit Harald par l'embrasure d'une porte."
    "Le roi est entrain de s'équiper de son armure."
    "Dans la pièce attenante, la Hache Sainte est accrochée à un râtelier qui lui est réservé."

    show einar combat_normal_mid at center with dissolve

    menu:
        "Prendre la Hache":
            show einar combat_hache_normal_mid at left
            show harald combat_normal_mid at right with dissolve
            e "(C'est tout ? Je m'attendais à une grande lumière, quelque chose comme ça...)"
            $ prendre_hache = True
            jump e_confrontation_harald_pont_baisse_donjonS

        "Se débarrasser de la Hache":
            show einar debout_determine_mid at center
            "Einar jette la Hache à la mer à travers une meurtrière."
            call e_confrontation_harald_pont_baisse_donjonS pass (jetee = True) from _call_e_confrontation_harald_pont_baisse_donjonS

        "Ignorer la Hache":
            show einar debout_normal_mid at center
            e "..."
            jump e_confrontation_harald_pont_axe_laissee_baisse_donjonS

label e_confrontation_harald_pont_baisse_donjonS(jetee = False):

    $ epargner_harld_donjon = False

    show einar combat_normal_mid at left
    show harald combat_normal_mid at right
    with dissolve

    if jetee:
        menu :

            "Einar ? Que fais-tu ici ? Où est la Hache ?"

            "Je l'ai jetée":
                show einar combat_determine_mid at left
                e "La Hache est perdue. Tout est terminé."
                show harald combat_furieux_mid at left
                h "Tu es fou ? Tu mens !"
                h "Où l'as-tu mise ? Tu veux la garder pour toi !"
                e "Votre relique est dans la vase, sous l'eau."

            "Je ne sais pas":
                show einar combat_normal_mid at left
                e "Je ne sais pas."
                show harald combat_furieux_mid at left
                h "Tu me mens ! Encore !"

            "Geir l'a volée (mentir)":
                show einar combat_normal_mid at left
                e "J'ai vu Geir la voler !"
                show harald combat_furieux_mid at left
                h "Cesse de me mentir !"

    else:

        show einar combat_hache_normal_mid at left
        show harald combat_normal_mid at right

        menu:
            "Einar ? Que fais-tu avec ma Hache ?"

            "Vous n'êtes plus rien":
                show einar combat_hache_normal_mid at left
                e "Je l'ai prise, en même temps que le pouvoir. Vous n'êtes plus rien."
                show harald combat_furieux_mid at right
                h "Tu ne peux pas faire ça ! Dieu m'a choisi !"
                show einar combat_hache_determine_mid at left
                e "Alors il vous a abandonné !"

            "Je suis un Dieu":
                show einar combat_hache_furieux_mid at left
                e "La relique me revient de droit ! Je suis un Dieu !"
                show harald combat_furieux_mid at right
                h "Tu es complètement fou !"

            "Je rétablis l'équilibre":
                show einar combat_hache_determine_mid at left
                e "Je l'ai prise pour vous en priver. Il est temps de rétablir l'ordre naturel des choses."

    show harald combat_normal_mid at right
    h "Comment oses-tu ?!"
    show harald combat_furieux_mid at right
    h "CETTE HACHE EST A MOI !"

    "Harald devient comme fou et se jette sur Einar."

    if prendre_hache:
        "Harald place un coup de dague très rapide au flanc d'Einar."
        "Einar n'est pas blessé et n'a même pas ressenti le coup."

        show einar combat_hache_determine_mid at left
        e "J'ai la Hache. Vous ne pouvez rien contre moi !"

        menu:
            "Fin de votre règne (le tuer)":
                show einar combat_hache_normal_mid at left
                e "Votre règne s'achève ici et maintenant. Vous allez mourir."
                show harald combat_blesse_mid at right
                h "Je m'avoue vaincu ! Ne me tue pas !"
                show einar combat_hache_determine_mid at left
                e "Pardon ?"
                h "J'ai fait de toi l'homme que tu es aujourd'hui ! Sois reconnaissant et épargne-moi. Pitié !"

            "Pas de répit pour vous (le tuer)":
                show einar combat_hache_normal_mid at left
                e "Pas de paix. Pas de répit. Pas de rémission. Il n'y a que la guerre. Je recommande votre âme."
                show harald combat_furieux_mid at right
                h "Tu es fou !"

            "Vous avez déjà perdu (épargner)":
                show einar combat_hache_normal_mid at left
                e "Vous avez déjà perdu. Je vais vous épargner."
                show harald combat_normal_mid at right
                h "Merci ! J'ai toujours su que tu étais un homme bon !"
                show einar combat_hache_determine_mid at left
                e "Ne vous réjouissez pas trop vite."
                h "Que vas-tu faire de moi?"
                $ epargner_harld_donjon = True

            "Je vous suis supérieur (épargner)":
                show einar combat_hache_determine_mid at left
                e "Je ne compte pas vous tuer : j'ai déjà prouvé ma superiorité sur vous."
                show harald combat_blesse_mid at right
                h "Alors tu t'es donné tout ce mal uniquement pour m'humilier ?"
                h "Que t'ai-je fait ?"
                show einar combat_hache_normal_mid at left
                e "Ce n'est pas le moment de discuter."
                h "Que vas-tu faire de moi?"
                $ epargner_harld_donjon = True
    else:
        "Le combat s'engage entre le roi et son huscarl"

        # "Phase combat WIP"

        $ time = 5
        $ timer_range = 5
        $ timer_jump = 'game_over_combat'


        "Harald se jete sur Einar et tente de la frapper à l'aide de ses poings"

        show screen countdown
        menu:

            "Esquiver":
                hide screen countdown
                "Abattant son épée sur le sol sur le sol, Einar réussi à éviter in extrmis"

            "Se jeter Harald":
                hide screen countdown
                "En se jetant sur les huscarls, Einar se fait couper de par en par"
                jump game_over_combat

        $ time = 5
        $ timer_range = 5
        $ timer_jump = 'game_over_combat'

        "Une fois son esquive effectuée, enchaine directement avec un crocher du droit"

        show screen countdown

        menu :
            "Faire attaque tournoyante":
                hide screen countdown
                "Einar réussi à les eloigner suffisament Harald et poursuit par une nouvelle attaque directement"
                "Et lui assigner un coup fatal dans la nuque"
                jump win_battle_harald_no_axe_pont_baisse_donjon

            "Bugler pour l'effrayer":
                hide screen countdown
                jump bad_ending_12

    if epargner_harld_donjon:
        menu :
            "Partez d'ici":

                show einar combat_hache_furieux_mid at left
                e "Partez d'ici. Ne revenez jamais en Ecosse."
                show harald combat_blesse_mid at right
                h "Tu me laisse m'enfuir ? Pourquoi ?"
                show einar combat_hache_normal_mid at left
                e "Vous êtes vaincu et vous n'avez plus votre Hache."
                e "Le règne du roi-empereur Harald Sigurdsson est terminé !"
                e "La nouvelle de votre défaite va se répandre à travers le monde. L'empire que vous avez bâti va s'écrouler."
                show einar combat_hache_determine_mid at left
                e "Vous tuer ici ne servirait à rien. Partez !"
                "Harald s'enfuit sans demander son reste"
                jump fuite_harald_pont_baisse_donjonS

            "Ogma veut vous rencontrer...":
                e "Le Hurleur sera heureux de vous rencontrer, j'en suis sûr..."
                scene bg chateau_rempart_crepuscule with dissolve
                "Quelques minutes plus tard, alors que les combats sont terminés..."
                "Sur les remparts, Ogma se tient au-dessus des rebelles et des survivants vikings. Harald est à genoux devant lui."
                show einar combat_hache_normal_mid at left
                show ogma combat_determine_mid at right
                o "Voyez ! La liberté a vaincu le tyran !"
                o "Demain, le monde se libèrera des chaînes que lui a imposé un seul homme !"
                show ogma combat_furieux_mid at right
                o "Le règne du roi-empereur est terminé !"
                "Ogma tranche la gorge du roi, qui laisse s'échapper un torrent de sang."
                show ogma combat_determine_mid at right
                o "VOUS ÊTES LIBRES !"
                "Ogma repousse du pied le corps du roi, qui bascule par-dessus les remparts et tombe à la mer."
                "Dans la lumière du crépuscule, Dunbar continue de brûler."
                jump good_ending_11

    else:
        show einar combat_hache_normal_mid at left
        show ogma combat_determine_mid at right

        o "Félicitations, Einar !"
        show re debout_rire at center
        ge "HOURRAAA !"
        hide re
        show ogma debout_souriant_mid at right
        o "Tu as libéré l'Ecosse ! Tu as libéré le reste du monde !"
        show re debout_rire at center
        ge "HOURRAAA !"
        hide re
        o "Pour que la victoire soit complète, nous devons détruire la Hache."
        show einar combat_hache_determine_mid at left
        e "Pourquoi ?"
        show ogma debout_contrarie_mid at right
        o "Si la Hache tombe à nouveau dans les mains d'un conquérant, le monde sera à nouveau enchaîné."
        show ogma debout_determine_mid at right
        o "Nous devons nous assurer que la Hache soit détruite !"
        o "Donne la moi, s'il-te-plaît."

        menu:
            "La voilà.":
                jump good_ending_7
            "Elle est à moi !":
                jump e_garder_hache_pont_baisse_donjonS

label e_confrontation_harald_pont_axe_laissee_baisse_donjonS:
    "Einar continue son oeuvre, incendiant le mobilier et tout ce qui peut l'être. Les flammes sont de plus en plus importantes et dévorent la structure du donjon."

    show einar combat_normal_mid at left
    show harald combat_hache_normal_mid at right

    h "Einar ? Que fais-tu ?!"

    menu :
        "Pour la Liberté":
            e "J'ai voulu croire en la liberté d'un peuple sur ses propres terres."
            h "Tu es ridicule ! Ces gens se sont servis de toi !"
            e "Sans doutes... Mais j'aurai libéré un peuple."
            show einar combat_determine_mid at left
            e "Les écossais en ont assez de recevoir des ordres. Il est temps pour eux de reprendre leur destin en main !"
            show harald combat_hache_furieux_mid at right
            h "Tu penses réellement que ce peuple de paysans arriéré serait capable de prendre les bonnes décisions ?"
            h "Sans moi, sans l'empire, ils sont voués à rester à l'état de petits clans épars, rongé par leurs petites guerres ridicules !"
            h "Ton altruisme irraisonné m'écoeure !"
            show einar combat_normal_mid at left
            e "Le choix ne vous appartient plus, désormais."

        "Las des promesses":
            e "J'étais las de vos promesses de terres et d'or qui ne se concrétisaient jamais, alors j'ai changé de camp."
            show harald combat_hache_furieux_mid at right
            h "C'est l'appât du gain qui te fait te rebeller contre moi ? Tu es prêt à condamner tout l'empire par caprice ?"
            h "Tu es complètement fou !"
            show einar combat_determine_mid at left
            e "Peut-être."

        "Vous êtes un monstre":
            show einar combat_normal_mid at left
            e "J'ai rencontré une jeune femme et son père, qui m'ont convaincu que vous êtes un monstre."
            e "Le monde ne devrait jamais être entre les mains d'un seul homme."
            e "Vous n'avez fait qu'enchaîner massacres sur prises de pouvoir, vous avez privé le monde de son libre arbitre."
            show harald combat_hache_furieux_mid at right
            h "Je suis l'élu divin ! Dieu a fait de moi son émissaire ! Je rassemble tous les peuples sous Sa bannière !"
            e "Je ne sais pas si vous y croyez vous-même."
            h "Je suis le porteur de la Hache ! J'ai été guidé par le Seigneur jusqu'aux Clous de la Sainte-Croix !"

        "J'avais envie de déranger l'ordre établi":
            show einar combat_normal_mid at left
            e "L'ordre des choses m'ennuyait..."
            e "J'ai simplement eu l'envie de mettre un coup de pied dans la fourmilière."
            show harald combat_hache_furieux_mid at right
            h "Tu es complètement fou !"
            e "Probable."

    show harald combat_hache_normal_mid at right
    h "Tu me déçois, Einar. D'entre tous mes huscarls, il a fallu que ce soit toi qui me trahisse."
    h "Tu crois être unique ? D'autres prendront ta place."
    show harald combat_hache_determine_mid at right
    h "Mon règne se poursuivra longtemps après ta mort."
    "Harald brandit la Hache"
    h "Es-tu conscient de ta totale impuissance ?"

    menu :
        "Que répondre ?"

        "J'ai mon amulette protectrice !":
            show einar combat_normal_mid at left
            e "C'est l'occasion de voir si ce vieux grigri fonctionne vraiment..."
            e "Voyez, Sire ! C'est un crucifix sculpté une nuit de pleine lune à l'équinoxe de printemps !"
            show harald combat_hache_furieux_mid at right
            h "Même à l'article de la mort, tu ne cesses pas d'être insolent..."
            h "Ce sera ton dernier blasphème, traître."

        "Peu importe, je suis satisfait":
            show einar combat_normal_mid at left
            e "Peu importe. J'ai fait ce que je devais faire."
            show harald combat_hache_normal_mid at right
            h "Au moins, tu auras suivi tes convictions..."
            h "Quitte à trahir ton roi et à provoquer la mort de tous ceux qui te comptaient comme un ami !"

        "Pardon":
            show einar combat_normal_mid at left
            e "Et si j'implore votre pardon, Sire ?"

        "Vous avez déjà perdu":
            e "Me tuer ne changera rien au fait que vous avez perdu cette bataille."
            show einar combat_determine_mid at left
            e "Le château n'est plus sous votre contrôle et vous n'avez plus d'hommes ici. Vous allez quitter l'Ecosse !"
            show harald combat_hache_furieux_mid at right
            h "Rassure-toi, ce petit soulèvement paysan n'écornera pas ma toute-puissance."
            h "L'Histoire ne se souviendra même pas de cet incident !"

    jump bad_ending_16

label win_battle_harald_no_axe_pont_baisse_donjonS:

    $ epargner_harld__no_axe_donjon = False

    show einar combat_furieux_mid at left
    show harald combat_furieux_mid at right

    "Einar parvient à briser le bras du roi et à lui infliger un coup sérieux au visage."
    show harald combat_blesse_mid
    h "Hggghh..."
    h "Je suis vaincu. Tu as gagné."
    h "... Laisse-moi vivre, s'il-te-plaît."


    menu :
        "Que dire à Harald ?"

        "Fin de votre règne (le tuer)":
            show einar combat_determine_mid at left
            e "Votre règne s'achève ici et maintenant. Vous allez mourir."
            h "Je m'avoue vaincu ! Ne me tue pas !"
            e "Pardon ?"
            h "J'ai fait de toi l'homme que tu es aujourd'hui ! Sois reconnaissant et épargne-moi. Pitié !"

        "Pas de répit pour vous (le tuer)":
            show einar combat_determine_mid at left
            e "Pas de paix. Pas de répit. Pas de rémission. Il n'y a que la guerre. Je recommande votre âme."
            show harald combat_furieux_mid at right
            h "Tu es fou !"

        "Vous avez déjà perdu (épargner)":
            show einar combat_normal_mid at left
            e "Vous avez déjà perdu. Je vais vous épargner."
            show harald combat_normal_mid at right
            h "Merci ! J'ai toujours su que tu étais un homme bon !"
            show einar combat_determine_mid at left
            e "Ne vous réjouissez pas trop vite."
            $ epargner_harld__no_axe_donjon = True

        "Je vous suis supérieur (épargner)":
            show einar combat_normal_mid at left
            e "Je ne compte pas vous tuer : j'ai déjà prouvé ma superiorité sur vous."
            show harald combat_normal_mid at right
            h "Alors tu t'es donné tout ce mal uniquement pour m'humilier ?"
            h "Que t'ai-je fait ?"
            e "Ce n'est pas le moment de discuter."
            $ epargner_harld__no_axe_donjon = True


    if epargner_harld__no_axe_donjon:
        jump e_epargne_harald_no_axe_donjonS
    else:
        call lieu_encore_inconnu_1S pass (axe = False) from _call_lieu_encore_inconnu_1S

label e_epargne_harald_no_axe_donjonS:

    $ harald_echape_no_axe = True

    show einar combat_normal_mid at left
    show harald combat_normal_mid at right

    h "Tu comptes me laisser en vie ? Que vas-tu faire de moi ?"

    menu:

        "Je ne veux pas tuer un roi (Laisser fuir)":
            show einar combat_determine_mid at left
            e "Vous êtes privé de la Hache et vous avez été vaincu. Votre Empire s'écroulera."
            e "Je n'ai pas besoin de me faire régicide pour savoir que j'ai gagné."
            e "Partez, maintenant."

        "Partez maintenant (Laisser fuir)":
            show einar combat_furieux_mid at left
            e "Fuyez, avant que je ne change d'avis. Ne me demandez pas d'explications."

        "Je vais vous livrer à Ogma":
            e "Je vais vous livrer au Hurleur, il saura quoi faire de vous. Tout ceci n'est plus de mon ressort."
            $ harald_echape_no_axe = False

        "Des gens veulent vous rencontrer":
            e "Je connais quelques personnes qui voudraient vous rencontrer..."
            $ harald_echape_no_axe = False

    if harald_echape_no_axe:
        "Harald s'échappe sans demander son reste."
        show harald combat_furieux_mid at right
        h "Je me vengerai ! Ta clémence a condamné cette île ! Tu m'entends ?"
        h "JE ME VENGERAI !"
        "..."

        hide harald
        hide einar
        with dissolve

        "Par une meurtrière, Einar remarque une petite embarcation qui quitte le château."
        "Harald s'échappe par la mer, seul sur sa barque."
        #Retour à l'extérieur
        "La bataille arrive à sa fin. Les rebelles achèvent les quelques vikings qui rampent au sol."
        "Sur les remparts, la silouhette d'Ogma se découpe sur le ciel."
        "Le Hurleur semble observer la mer."

        "Un peu plus tard..."

        show einar debout_normal_mid at left
        show ogma debout_normal_mid at right
        o "Pourquoi l'avoir laissé s'enfuir ?"
        o "Nous tenions celui qui a asservi le monde entier, privé de sa Hache..."
        o "Nous pouvions libérer le monde !"
        show einar debout_attriste_mid at right
        e "Je..."
        show ogma debout_contrarie_mid at right
        o "Ne répond pas à ma question, je préfère ne pas savoir."
        show ogma debout_normal_mid at right
        o "Tu avais sûrement une excellente raison de le laisser partir."
        show ogma debout_souriant_mid at right
        o "Quoi qu'il en soit, je te suis reconnaissant. Sans toi, rien de tout ceci n'aurait été possible."
        show ogma debout_souriant_mid at right
        o "L'empire va s'effondrer grace à nous. Privé de la Hache Sainte, Harald n'est plus rien."

        jump village_5S

    else:
        "Un peu plus tard, alors que les combats ont cessé..."
        "..."
        show ogma combat_normal_mid at left
        show einar debout_blesse at right
        show ogma combat_normal_mid at left
        show einar debout_blesse at right
        "Sur les remparts, Ogma se tient au-dessus des rebelles et des survivants vikings. Harald est à genoux devant lui."
        show ogma combat_determine_mid at left
        o "Voyez ! La liberté a vaincu le tyran !"
        o "Demain, le monde se libèrera des chaînes que lui a imposé un seul homme !"
        o "Le règne du roi-empereur est terminé !"
        "Ogma tranche la gorge du roi, qui laisse s'échapper un torrent de sang."
        o "VOUS ÊTES LIBRES !"
        "Ogma repousse du pied le corps du roi, qui bascule par-dessus les remparts et tombe à la mer."
        "Dans la lumière du crépuscule, Dunbar continue de brûler."
        hide ogma
        hide harald
        with dissolve
        jump village_6S

label village_5S:

    play ambiance village

    "..."

    show einar debout_normal_mid at left
    show ogma debout_normal_mid at right

    o "Voici ton or."
    o "Nous avons décidé de t'offrir un cheval. Il te mènera où bon te semble."
    show einar debout_contrarie_mid at left
    e "Et si je souhaite rester ici ?"
    o "Je ne peux pas te laisser cette liberté."
    o "Malgré tout ce que tu as fait pour nous et l'affection que te porte Moira, je ne peux pas t'autoriser à rester parmi nous."
    o "Tu nous a offert la victoire, et pour cela l'Ecosse te sera toujours redevable."
    show ogma debout_contrarie_mid at right
    o "Mais tu as laissé s'enfuir notre ennemi. Je veux que tu quittes l'Ecosse pour toujours."
    o "Ne reviens jamais ici."

    menu:

        "J'ai été juste":
            show einar debout_attriste_mid at left
            e "Lorsque vous m'avez capturé, vous m'avez expliqué que vous vouliez chasser le roi de vos terres."
            e "J'ai rempli ma part du contrat et fait ce qui me semblait juste. Je regrette que nous nous séparions en ces termes."
            e "Adieu."

        "Je suis désolé":
            show einar debout_attriste_mid at left
            e "Je regrette de l'avoir laissé partir. J'espère que vous me pardonnerez."
            o "Crois bien que je suis aussi navré que toi. Pars, maintenant."

        "Adieu":
            show einar debout_contrarie_mid at left
            e "Je ne comptais pas rester ici. Adieu."

    hide einar
    hide ogma
    with dissolve

    jump foret_4S

label village_6S:

    play ambiance village

    $ refuer_ogma_main_moira = False

    "Moira se tient légèrement à l'écart."
    show einar debout_normal_mid at left
    show moira debout_normal_mid at right
    show ogma debout_normal_mid at right
    with dissolve

    o "Toute l'Ecosse t'es redevable, Einar !"
    o "Tu nous a rendu la liberté et provoqué la fin de l'empire !"
    o "Comme promis, voici ton or et un cheval prêt à t'emmener où bon te semble."

    menu:
        "Merci":
            show einar debout_souriant_mid at left
            e "Je vous remercie."
            e "En vingt ans, jamais Harald ne m'avait offert autant de récompenses !"
            e "Libérer un peuple et repartir avec de l'or..."
            e "C'est bien plus gratifiant que de servir un roi qui ne tient pas ses promesses !"

        "L'or ne rachètera pas les morts":
            show einar debout_contrarie_mid at left
            e "L'or ne rachètera pas les vies qui ont été perdues, ni ma traîtrise envers les miens."
            show ogma debout_attriste_mid at right
            o "Je comprends. J'espère que ton amertume s'estompera avec le temps."

        "C'était une question de survie (refuser l'or)":
            show einar debout_contrarie_mid at left
            e "Ce que j'ai fait, je l'ai fait pour survivre, vous m'y obligiez. Je ne veux pas de cet or."
            show ogma debout_attriste_mid at right
            o "Ton humilité est toute à ton honneur."
            o "Nous n'avons pas eu le choix. Nous avions besoin d'un instrument pour nous aider à faire basculer le roi."
            o "Malheureusement pour toi, tu as été notre élu."
            o "J'espère que tu nous pardonneras un jour..."
            show ogma debout_determine_mid at right
            o "Vois ces gens autour de toi : tu es leur libérateur !"

    show ogma debout_normal_mid at right
    o "Il y a autre chose dont j'aimerais te parler. Une dernière faveur."
    e "..."
    o "Cela concerne Moira."
    show ogma debout_souriant_mid at right
    o "Je crois savoir que vous vous portez une grande affection..."
    o "Je serais heureux de compter le libérateur de mon peuple dans ma famille."
    o "J'ai l'honneur de t'offrir la main de ma fille, si tu l'acceptes."
    show ogma debout_normal_mid at right

    show moira debout_souriant_mid at right
    "Bien qu'à l'écart, Moira fait un grand sourire à Einar."

    menu:

        "Même sans votre consentement !":
            show einar debout_souriant_mid at left
            e "Si vous ne me l'aviez pas proposé, j'aurais enlevé votre fille ! Ha ha !"
            show ogma debout_souriant_mid at right
            o "À la bonne heure !"

        "C'est un honneur":
            show einar debout_souriant_mid at left
            e "J'accepte. C'est un grand honneur que vous me faites."
            show ogma debout_souriant_mid at right
            e "Je n'aurais pas pu espérer une plus belle récompense !"

        "Pas de sentiments pour Moira":
            show einar debout_attriste_mid at left
            e "Ces sentiments ne sont pas partagés. Je préfère conserver ma liberté."
            show ogma debout_contrarie_mid at right
            show moira debout_attriste_mid at right
            o "..."
            o "Très bien. Ma déception est grande, mais je comprend."
            $ refuer_ogma_main_moira = True

    if refuer_ogma_main_moira:

        #Animation moira part
        hide moira debout_attriste_mid with dissolve
        "Moira s'en va."
        show ogma debout_attriste_mid at right
        o "A vrai dire, la déception de ma fille doit être encore plus grande..."
        o "Elle était à l'origine de cette demande."
        e "..."
        show ogma debout_normal_mid at right
        o "Que comptes-tu faire désormais ?"

        menu:

            "Ermite en Ecosse":
                show einar debout_normal_mid at left
                e "Rester ici, en Ecosse. Seul."
                o "L'isolement... Peu d'hommes le supportent, mais je comprends ton choix."
                o "Si la solitude ne te convient plus, sache que tu trouveras toujours des amis à Perth."

            "Je vais rentrer en Norvège":
                show einar debout_determine_mid at left
                e "Rentrer en Norvège, malgré le danger. C'est ma seule demeure, et je ne l'ai pas vue depuis bien trop longtemps."
                show ogma debout_attriste_mid at right
                o "La nostalgie des terres natales..."
                o "Prend garde à toi une fois là-bas. Les gens voudront sans doute retrouver celui qui a condamné leur roi et fait basculer leur empire."

            "Je vivrai au jour le jour":
                show einar debout_normal_mid at left
                e "Errer. Je n'ai pas d'idées bien déterminées concernant la suite."
                o "J'imagine qu'à ta place, je n'en saurais pas plus."
                o "L'errance a du bon. C'est dans ces moments là que l'on fait les rencontres les plus étonnantes."

            "J'irai en Asie":
                show einar debout_normal_mid at left
                e "Aller en Asie, là où personne ne viendra me chercher. J'ai toujours été intrigué par cette région du monde."
                show ogma debout_souriant_mid at right
                o "C'est assez... Surprenant !"
                o "Il ne me reste plus qu'à te souhaiter bon voyage."
                o "Si le coeur t'en dit, n'hésite pas à revenir ici. Tu trouveras toujours des amis à Perth."

                hide ogma
                hide einar
                with dissolve

        call good_ending_15S pass (marier = False) from _call_good_ending_15S
    else:
        jump good_ending_15

label foret_4S:

    play ambiance village

    $ rejeter_moira_foret_4 = False

    "..."
    "Moira apparaît sur le sentier."

    show einar debout_normal_mid at left with dissolve
    show moira debout_normal_mid at right with moveinright

    if premier_refus_moira_foret_4 == False:
        e "Qu'est-ce que tu fais là ?"
        m "Je viens avec toi."
        show einar debout_attriste_mid at left
        e "Pardon ? Tu n'as pas entendu ce qu'à dit ton père ?"
        show moira debout_contrarie_mid at right
        m "Mon père a été injuste. Tu as fait tout ce qu'il t'avait demandé et plus encore."
        show moira debout_determine_mid at right
        m "Je t'aime. Je veux venir avec toi."
    else:
        e "Qu'est-ce que tu fais là ?"
        show moira debout_furieux_mid at right
        m "Pourquoi est-ce que tu es parti ? Pourquoi m'avoir abandonnée ?"

        menu :
            "Excuse-moi":
                e "Je regrette d'avoir fait ça..."
                m "Pourquoi être parti ? Je pensais pouvoir te faire confiance."
                e "Tu peux avoir confiance en moi !"
                e "Simplement... J'étais enfermé depuis si longtemps... J'ai vu une occasion de reprendre ma liberté, et je l'ai saisie."
                e "Ce qui ne m'a pas empêché de tenir mes engagements envers ton père."
                m "Je vois..."
                e "..."
                m "C'est idiot mais... Je veux partir avec toi."
                show einar debout_attriste_mid at left
                e "Pardon ? Tu n'as pas entendu ce qu'à dit ton père ?"
                show moira debout_contrarie_mid at right
                m "Mon père a été injuste. Tu as fait tout ce qu'il t'avait demandé et plus encore."
                e "Mais je t'ai trahie ! Je t'ai laissé seule, nue, dans la forêt !"
                show moira debout_determine_mid at right
                m "Oui, et j'en ai été profondément déçue, et humiliée."
                m "Mais malgré tout, je comprends ce qui a pu te pousser à agir ainsi."
                m "Je t'aime. Je veux venir avec toi."

            "Je n'ai rien à faire avec toi":
                e "Je suis un militaire. J'ai voyagé à travers tous les continents et rencontré plus de femmes que tu ne peux l'imaginer."
                e "Tu ne m'interesse pas. Je n'ai rien à faire avec une paysanne écossaise, aussi belle soit-elle."
                e "Tu trouveras sans doute quelqu'un de plus... adapté à ta vie."
                e "Au revoir."
                call good_ending_14S pass (rejete = True) from _call_good_ending_14S

            "Je me suis servi de toi":
                e "Au risque de te faire de la peine, je ne ressentais et ne ressens toujours rien pour toi."
                e "Lorsque j'ai compris que tu m'offrais une opportunité de m'enfuir, j'ai saisi l'occasion."
                e "Je me suis juste servi de toi."
                m "..."
                call good_ending_14S pass (rejete = True) from _call_good_ending_14S

    menu menu_reponse_moira_suivre_einarS:

        "Tu n'as pas de raison de me suivre":
            show einar debout_attriste_mid at left

            e "Je ne sais pas où je vais. Tu n'as aucune raison de venir avec moi."
            e "Reste ici, avec ton père et les autres."
            show moira debout_attriste_mid at right
            m "..."
            m "Est-ce que tu reviendras ?"
            e "Je ne sais pas. Rentre chez-toi, maintenant."
            "..."

        "Je ne veux pas contrarier Ogma":
            show einar debout_attriste_mid at left

            e "Je ne veux pas me mettre en porte-à-faux vis à vis de ton père."
            show einar debout_contrarie_mid at left
            e "Il m'a interdit de rester ici, et il ne me permettra certainement pas de partir avec sa fille."
            e "Laisse moi partir."
            show moira debout_contrarie_mid at right
            m "Je me fiche de tout ça ! Je n'appartient pas à mon père ! Si j'en ai envie, rien ne m'empêche de te suivre !"
            show einar debout_attriste_mid at left
            e "Tu connais ton père. Il a déjà organisé l'assassinat d'un intendant pour venger sa femme, il n'hésitera pas à me traquer jusqu'au bout du monde pour te retrouver."
            e "Je n'irai pas contre son avis. N'insiste pas."
            e "Au revoir, Moira."

        "Nous n'éprouvons pas les même sentiments":
            show einar debout_normal_mid at left
            e "Je ne t'aime pas, Moira."
            show einar debout_souriant_mid at left
            e "Je te suis reconnaissant pour tous tes soins, et j'ai apprécié le temps que nous avons passé ensemble."
            show einar debout_attriste_mid at left
            e "Mais je ne t'aime pas."
            show moira debout_attriste_mid at right
            m "Tu dis ça pour que je ne te suive pas !"
            e "Non, je regrette. Laisse-moi partir maintenant, s'il-te-plaît."
            $ rejeter_moira_foret_4 = True

        "(Tendre les bras)":
            show einar debout_souriant_mid at left
            show moira debout_souriant_mid at right

            "Sans dire un mot, Einar tend les bras vers Moira."
            "La jeune femme se précipite vers le viking et l'étreint."
            "Einar et Moira passent quelques minutes à profiter de l'instant."

        "Viens avec moi":
            show einar debout_souriant_mid at left

            e "Viens avec moi, Moira."
            show moira debout_attriste_mid at right
            "La jeune femme se précipite vers le viking et l'étreint."
            "Einar et Moira passent quelques minutes à profiter de l'instant."

        #"Autre choix refus" if premier_refus_moira:
            #show einar debout_determine_mid at left
            #e "Je me servi de toi pour quitter le village"
            #show moira debout_attriste_mid at right
            #$ rejeter_moira_foret_4 = True

    hide moira
    hide einar
    with dissolve

    if rejeter_moira_foret_4:
        call good_ending_14S pass (rejete = True) from _call_good_ending_14S
    else:
        jump good_ending_14

label fuite_harald_pont_baisse_donjonS:

    show harald debout_furieux_mid at left with dissolve

    h "Je me vengerai ! Ta clémence a condamné cette île ! Tu m'entends ?"
    h "JE ME VENGERAI !"
    "..."
    "Par une meurtrière, Einar remarque une petite embarcation qui quitte le château."
    "Harald s'échappe par la mer, seul sur sa barque."

    #animation harald partir vers la droite
    hide harald
    with dissolve

    #Retour à l'extérieur
    "La bataille arrive à sa fin. Les rebelles achèvent les quelques vikings qui rampent au sol."
    "Sur les remparts, la silouhette d'Ogma se découpe sur le ciel."
    "Le Hurleur semble observer la mer."
    "..."

    show ogma debout_normal_mid at right
    show einar debout_normal_mid at left
    with dissolve

    o "Bravo Einar, la réussite est totale ! Mais pourquoi avoir laissé partir le roi ?"
    show einar debout_attriste_mid at left
    e "Je..."
    show ogma debout_contrarie_mid at right
    o "Ne réponds pas à ma question, je préfère ne pas savoir."
    o "Le roi est vaincu et tu as la Hache Sainte, tu n'avais aucune raison de le tuer."
    o "La Hache a l'air si... ordinaire."
    show einar debout_normal_mid at left
    e "Je peux vous assurer qu'elle n'a rien d'ordinaire !"
    show ogma debout_normal_mid at right
    o "Sans doutes..."
    o "Il va falloir que tu t'en sépare, désormais. Nous devons la détruire."
    o "Donne-la moi, s'il-te-plaît."

    menu:
        "Elle est à moi !":
            show einar combat_hache_determine_mid
            jump e_garder_hache_pont_baisse_donjonS

        "La voilà":
            hide einar
            hide ogma
            with dissolve

            jump normal_ending_10

label e_garder_hache_pont_baisse_donjonS:

    show ogma debout_contrarie_mid at right
    o "Ne sois pas idiot ! Nous devons la détruire sans tarder !"
    show ogma debout_determine_mid at right
    o "Je suis prêt à aller jusqu'au bout pour m'en débarrasser !"
    o "Donne-moi cette Hache !"
    "Ogma tend la main."

    menu :
        "Reculez !":
            show einar combat_hache_determine_mid at left
            e "Reculez ! Je suis le possesseur de la Hache, vous ne pouvez rien contre moi !"
        "Je la mérite":
            show einar combat_hache_determine_mid at left
            e "J'ai pris cette Hache des mains du roi-empereur. Je suis le seul à la mériter !"
            e "Vous n'avez aucun moyen de m'en priver !"

    show ogma debout_attriste_mid at right
    o "Très bien..."
    o "Tu as raison, je ne peux rien faire contre toi."
    o "Que comptes-tu faire de la relique ? Elle doit être détruite. Elle a déjà provoqué suffisamment de malheurs et asservi trop d'hommes."

    menu:

        "Je la détruirai moi-même":
            show einar combat_hache_normal_mid at left
            e "Je la détruirai moi-même. C'est mon devoir."
            o "Tu ne me fais pas confiance ?"
            e "Ce n'est pas le problème. Je veux simplement être absolument certain que personne n'en profitera plus jamais."
            hide einar with dissolve
            jump lieu_encore_inconnu_1S

        "Je la garde !":
            show einar combat_hache_determine_mid at left
            e "Je l'ai prise, elle m'appartient."
            e "J'ai bien mieux à faire que de détruire une telle merveille. Le monde m'appartient !"
            e "Harald n'était qu'un mou, il a cessé ses conquêtes bien trop tôt !"
            show einar combat_hache_determine_mid at left
            e "Le monde se pliera devant moi !"
            e "A genoux, manants ! HA HA HA !"
            o "Tu es fou ! Nous ne te laisserons pas faire !"
            e "Idiots ! La Hache me rend immortel !"
            hide einar with dissolve
            jump good_ending_9


label lieu_encore_inconnu_1S(axe = True):

    play ambiance village

    $ demander_main_moira = False
    $ refuser_or = False

    show einar debout_normal_mid at left
    show ogma debout_normal_mid at right
    show moira debout_normal_mid at right
    with dissolve

    if axe:
        "..."
        "Moira se tient à l'écart mais semble interessée pas la conversation."
        o "Merci pour tout, Einar."
        o "Tu as vaincu le roi, tu as libéré mon peuple et surtout, tu as débarrassé le monde de la Hache Sainte."
        o "Plus aucun tyran ne pourra abuser de la relique."
        o "A vrai dire, je suis heureux que tu ais choisi de te débarrasser de la Hache toi-même."
        o "J'aurais pu être tenté d'en fair un mauvais usage..."
        o "Aucun homme ne devrait jamais avoir un tel pouvoir entre ses mains."
        show einar debout_contrarie_mid at left
        e "Je dois admettre qu'avoir la Hache était assez... grisant."
        o "Tu as su rester humble et faire passer le reste du monde avant toi. Beaucoup d'autres auraient cédé à l'appel du pouvoir !"
        o "Nous t'avons préparé un cheval, et avons rempli ses fontes d'or, comme promis."
        o "Oh, et bien sûr, l'antidote."
        "Einar avale les quelques gouttes contenues dans la fiole."
        o "D'après le vieux Murray, tout devrait rentrer dans l'ordre d'ici deux jours."

    else:
        show ogma debout_souriant_mid at right
        "..."
        "Moira se tient à l'écart mais semble interessée pas la conversation."
        o "Merci pour tout, Einar."
        o "Tu as vaincu le roi, tu as libéré mon peuple et surtout, tu as libéré le monde du joug du roi."
        o "Je ne sais pas ce que tu as fait de la Hache, mais je ne veux pas le savoir. Ne révèle jamais à personne ton secret."
        o "A vrai dire, je suis heureux que tu ais choisi de te débarrasser de la Hache toi-même."
        o "Aucun homme ne devrait jamais avoir un tel pouvoir entre ses mains."
        show einar debout_contrarie_mid at left
        e "Je dois admettre qu'avoir la Hache était assez... grisant."
        o "Tu as su rester humble et faire passer le reste du monde avant toi. Beaucoup d'autres auraient cédé à l'appel du pouvoir !"
        o "Nous t'avons préparé un cheval, et avons rempli ses fontes d'or, comme promis."
        o "Oh, et bien sûr, l'antidote."
        "Einar avale les quelques gouttes contenues dans la fiole."
        o "D'après le vieux Murray, tout devrait rentrer dans l'ordre d'ici deux jours."

    show einar debout_normal_mid at left

    menu:

        "Je voudrais la main de votre fille":
            e "Ogma, j'aimerais vous demander plus."
            o "Je t'écoute ?"
            e "Je vous demande la main de votre fille."
            "Ogma soupire."
            show ogma debout_contrarie_mid at right
            o "Je suis sincèrement navré, Einar, mais je ne peux pas accepter."
            o "Je refuse que ma fille et sa descendance partagent le nom d'un régicide."
            $ demander_main_moira = True

        "Merci":
            show einar debout_souriant_mid at left
            e "Je vous remercie."
            e "Je n'étais pas certain que vous tiendriez votre parole."
            show ogma debout_contrarie_mid at right
            o "Et je n'étais pas certain que tu tiendrais la tienne !"
            show ogma debout_souriant_mid at right
            o "Nous sommes quittes."

        "L'or ne rachètera pas les morts":
            show einar debout_attriste_mid at left
            e "L'or ne rachètera pas les vies qui ont été perdues, ni ma traîtrise envers les miens."
            show ogma debout_attriste_mid at right
            o "Ce que nous t'avons fait faire était cruel, mais nous n'avions pas d'autre choix, tu le sais."
            o "Je comprends que tu éprouves de la rancoeur, mais ne la dirige pas vers l'Ecosse ni les gens d'ici."
            o "Dirige-la vers moi. Je suis responsable de tout ce qui t'es arrivé."
            e "..."

        "C'était une question de survie (refuser l'or)":
            show einar debout_contrarie_mid at left
            e "Ce que j'ai fait, je l'ai fait pour survivre, vous m'y obligiez. Je ne veux pas de cet or."
            o "Voilà une belle preuve d'humilité."
            show ogma debout_attriste_mid at right
            o "Je suis désolé de t'avoir entraîné dans ce massacre, mais je n'avais pas le choix."
            show ogma debout_determine_mid at right
            o "Ce que j'ai fait, c'était avant tout pour le bien de l'Ecosse et du reste du monde."
            show einar debout_attriste_mid at left
            e "Sans doute."
            $ refuser_or = True


    if demander_main_moira:
        menu menu_demande_main_moira_lieu_encore_inconnu_1S:

            "Je comprends":
                show einar debout_attriste_mid at left
                e "Je comprends. Si j'avais su, j'aurais épargné le roi..."
                show ogma debout_normal_mid at right
                o "..."

            "Moira, qu'en penses-tu ?":
                show einar debout_determine_mid at left
                e "Moira, qu'en penses-tu ?"
                #Animation moira se rapprochant
                "Elle se rapproche des deux hommes, comprenant de quoi il est question."
                show moira debout_attriste_mid at right
                m "Je... Je suis d'accord avec mon père."
                "Les larmes lui montent aux yeux."

            "Ce n'est pas à vous de décider":
                show einar debout_determine_mid at left
                e "Ce n'est pas à vous d'en décider. Votre fille doit choisir elle-même. Il s'agit de son propre avenir, pas du votre !"
                show ogma debout_furieux_mid at right
                o "J'aurais punis ton insolence si je ne comprenais pas ton désarroi."
                show moira debout_attriste_mid at right
                m "Calme-toi, Einar. Je n'ai pas d'autre choix que de me ranger à l'avis de mon père."
                "Les larmes lui montent aux yeux."

    show ogma debout_normal_mid at right
    hide moira with dissolve

    if refuser_or:

        o "Refuser l'or de la trahison et du sang t'honore. Et maintenant, que vas-tu faire ?"
    else:
        o "Et maintenant, que vas-tu faire ?"


    menu plan_futur_lieu_encore_inconnu_1S:

        "Je vais me payer des femmes et des jeux !" if refuser_or == False:
            show einar debout_souriant_mid at left
            e "Je vais dépenser l'or en femmes et en jeux, ha ha !"
            show einar debout_normal_mid at left
            e "De toutes manières, je n'ai plus grand chose à faire."
            e "Ma carrière militaire est terminée et je n'ai nul part où aller en particulier."
            show einar debout_souriant_mid at left
            e "Je suis seul au monde ! Un peu de chaleur humaine ne me fera pas de mal !"

        "Ermite en Ecosse":
            show einar debout_attriste_mid at left
            e "Rester ici, en Ecosse. Seul."
            e "J'ai déjà suffisamment donné de ma personne."
            show ogma debout_attriste_mid at right
            o "L'isolement... Peu d'hommes le supportent, mais je comprends ton choix."
            o "Si la solitude ne te convient plus, sache que tu trouveras toujours des amis à Perth."

        "Je rentrerai en Norvège":
            show einar debout_attriste_mid at left
            e "Rentrer en Norvège, malgré le danger. C'est ma seule demeure, et je ne l'ai pas vue depuis bien trop longtemps."
            o "La nostalgie des terres natales..."
            show ogma debout_attriste_mid at right
            o "Prend garde à toi une fois là-bas. Les gens voudront sans doute retrouver celui qui a condamné leur roi et fait basculer leur empire."

        "Je vivrai au jour le jour":
            show einar debout_normal_mid at left
            e "Errer. Je n'ai pas d'idées bien déterminées concernant la suite."
            o "J'imagine qu'à ta place, je n'en saurais pas plus."
            show ogma debout_souriant_mid at right
            o "L'errance a du bon. C'est dans ces moments là que l'on fait les rencontres les plus étonnantes."

        "J'irai en Asie":
            show einar debout_normal_mid at left
            e "Aller en Asie, là où personne ne viendra me chercher. J'ai toujours été intrigué par cette région du monde."
            o "C'est assez... Surprenant !"
            show ogma debout_normal_mid at right
            o "Il ne me reste plus qu'à te souhaiter bon voyage."
            show ogma debout_souriant_mid at right
            o "Si le coeur t'en dit, n'hésite pas à revenir ici. Tu trouveras toujours des amis à Perth."

    hide einar
    hide ogma
    with dissolve

    if axe:
        jump good_ending_8
    else:
        jump good_ending_13

#Défendre porte
label soupcon_harald_defendre_porteS:

    show re combat_normaux_mid at left
    show gv combat_normaux_mid at right
    with dissolve

    "La horde avance en une masse compacte et nombre de rebelles succombent sous les flèches des vikings."
    ge "L'échelle ! Apportez l'échelle !"
    gv "Les rebelles dressent une échelle par-dessus les douves !"
    "Au même moment une troupe de guerriers d'élite, dissimulée à l'extérieur du château, surgit sur les flancs et l'arrière des rebelles."
    "Rapidement, les vikings repoussent les rebelles massés devant le pont-levis. En même temps, l'échelle est abattue et brisée."
    show gv combat_normaux_mid at right
    gv "Crevez, salopards ! Ha ha !"
    show harald combat_determine_mid at center with dissolve
    h "Consolidez les rangs !"
    hide harald with dissolve
    "Les rebelles sont contraints de reculer et restent à distance des remparts."
    "Alors que les vikings se réjouissent de leur supériorité, un cri retentit sur leurs arrières."
    gv "Par la mer ! Ils arrivent par la mer !"
    "Profitant des combats, un groupe conséquent d'écossais a pénétré l'enceinte par la mer pour débarquer discrètement derrière les vikings."
    "Ils lancent un deuxième assaut sur l'arrière des vikings, dans l'enceinte."
    "A l'extérieur, les rebelles lancent un nouvel assaut et après avoir tendu des planches en travers des douves, commencent à détruire le tablier du pont à coup de haches."
    gv "Ça va céder !"
    show harald combat_determine_mid at center with dissolve
    h "Einar ! Prends le commandement des huscarls ! Mène le combat au-delà de la porte !"
    hide harald
    hide gv
    hide re
    with dissolve

    show einar combat_normal_mid at left
    show huscarls combat_normaux_mid at right
    with dissolve

    menu:
        "Suivez-moi !":
            show einar combat_determine_mid at left
            e "A moi, huscarls !"
            e "Suivez-moi et ne me lâchez pas !"
            show huscarls combat_enthousiaste_mid at right

        "Dressez vos boucliers":
            show einar combat_determine_mid at left
            e "Je veux une ligne parfaite ! Dressez vos boucliers !"
            e "Vous avez déjà affronté bien pire que des paysans ! Souvenez-vous des éléphants de guerre !"
            show huscarls combat_enthousiaste_mid at right

        "Ils ne passseront pas ! ":
            show einar combat_furieux_mid at left
            e "Ces raclures ne passeront pas la porte !"
            e "Vengeance ! Pour le roi, pour Logan et pour tous les autres !"
            show huscarls combat_furieux_mid at right

    "Alors que la porte menace de céder, les vikings l'ouvrent et prennent de court les rebelles."
    "Immédiatement, les rebelles tentent de s'engouffrer dans l'ouverture, face à Einar et aux huscarls."
    "Une silouhette familière émerge des rebelles."

    hide huscarls
    show ogma combat_furieux_mid at right
    with dissolve

    show einar combat_normal_mid at left

    o "Traître ! Tu t'es joué de nous pour sauver ta vie de lâche !"
    o "Regarde combien d'hommes meurent aujourd'hui par ta faute !"

    menu:

        "Massacrez-les":
            show einar combat_determine_mid at left
            e "Huscarls, massacrez ces foutus écossais, sans exception ! Mais laissez-moi le chef !"

        "Que des porcs":
            show einar combat_furieux_mid at left
            e "Quels hommes ? Je ne vois que des porcs."

        "Ne rien dire":
            e "..."

        "Je vais m'occuper de ta fille !":
            show einar combat_furieux_mid at left
            e "J'en termine avec toi, et ensuite je retourne m'occuper de ta fille !"

    "Un combat s'engage entre Ogma et Einar !"
    #"Mini jeu combat WIP"

    #Phase combat

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'game_over_combat'


    "Ogma furieux de la trahison de Einar se jette sur lui"
    "L'épée brandie, Ogma s'aprête à frapper de tout ses forces."

    show screen countdown
    menu :

        "Esquiver":
            hide screen countdown
            "Abattant son épée sur le sol, Einar réussi à éviter in extrmis"

        "Se jeter sur Ogma":
            hide screen countdown
            "En se jetant sur Ogma, Einar se fait couper de par en par"
            jump game_over_combat

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'game_over_combat'

    "Une fois son esquive effectuée, Attaque de nouveau"

    show screen countdown

    menu :
        "Gagner":
            hide screen countdown

            show ogma combat_normal_mid at right
            "Einar frappe Ogma en travers du torse avec sa hachette, et le propulse dans les douves."
            "Terrorisés, les rebelles prennent la fuite."
            hide ogma with dissolve

            show harald combat_normal_mid at right with dissolve
            h "Ha ha ! Ils fuient, les lâches !"
            show harald combat_determine_mid at right
            h "Ventre à terre, huscarls ! Suivez-moi ! Donnons-leur la chasse !"

            "Harald s'élance à la poursuite des fuyards, le rire aux lèvres."
            "Les rebelles, déjà affaiblis et effrayés, se font massacrer par les vikings et Harald, hilares."

        "Perdre":
            hide screen countdown
            jump bad_ending_17

    hide einar
    hide harald
    with dissolve

    "Un peu plus tard..."

    show einar debout_normal_mid at left
    show harald debout_normal_mid at right
    with dissolve

    h "... un honneur ! Comme nul autre avant lui, Einar a fait preuve de sa fidélité et de sa bravoure !"
    show harald debout_normal_mid at right
    h "Il est le meilleur homme que j'ai eu sous mes ordres, et Dieu sait combien d'hommes valeureux j'ai eu à mon service !"
    h "Tu es du bois dont on fait les héros, Einar !"
    show harald debout_normal_mid at right

    menu:

        "Merci":
            show einar debout_souriant_mid at left
            e "Merci, mon roi."
            h "Ne me remercie pas ! Tu nous a tous sauvés, c'est à nous de te remercier !"

        "Je suis resté fidèle":
            show einar debout_attriste_mid at left
            e "Je suis resté fidèle à mon allégeance. La victoire, nous la devons à tous ceux qui sont morts aujourd'hui."
            show harald debout_normal_mid at right
            h "C'est vrai, mais ton mérite et ton honneur n'en sont pas amoindris ! Sans toi, nous étions perdus !"

        "Que l'on se souvienne de moi !":
            show einar debout_determine_mid at left
            e "J'ai mené l'assaut final et tué le chef rebelle, qu'on se souvienne longtemps de mes exploits !"
            h "Personne ne peut t'enlever les exploits que tu as accompli. La gloire t'appartient aujourd'hui ! "

    show harald debout_normal_mid at right
    show harald debout_normal_mid at right
    h "J'ai décidé de récompenser ta valeur."
    h "Je t'offre Stirling et les terres alentours ! Le village a brûlé il y a peu, mais les terres fourniront de bons revenus d'ici quelques années !"
    h "En outre, je t'offre le titre d'Intendant d'Ecosse !"

    menu :

        "Merci !":
            show einar debout_souriant_mid at left
            e "... Merci, je n'en attendais pas tant !"
            h "Ton désinteressement s'ajoute à tes prouesses ! On ne pourrait rêver d'avoir un meilleur homme à son service !"

        "Quel honneur !":
            show einar debout_souriant_mid at left
            e "Quel honneur ! Merci, mon roi !"
            show harald debout_normal_mid at right
            h "Depuis tout ce temps passé à mon service et toutes les promesses que je t'avais faites, te récompenser aujourd'hui me paraissait être une obligation !"

        #A vérifier
        "Des terres brûlées ?":
            show einar debout_contrarie_mid at left
            e "Des terres brûlées et un village rasé qui ne fourniront rien avant plusieurs années, dans un territoire hostile et isolé ? "
            show einar debout_attriste_mid at left
            e "Le titre d'intendant d'un peuple révolté et que j'ai trahi ?"
            show einar debout_contrarie_mid at left
            e "Vous vous moquez de moi, sire !"
            show gv debout_contraries_mid at center with dissolve
            gv "Sire !"
            show harald debout_contrarie_mid at right
            h "Laissez-le. Je pardonne son amertume, son insolence et son ingratitude."
            hide gv with dissolve
            show harald debout_normal_mid at right
            h "Tes exploits ne te dispensent pas de respecter ton roi et empereur, Einar."
            h "Ne t'adresse plus jamais à moi de cette façon, ou la sanction sera exemplaire."
            e "..."
            show einar debout_attriste_mid at left
            e "Sire, pardonnez mon attitude..."

    hide harald
    hide einar
    with dissolve

    jump normal_ending_18

label harald_defendre_porteS:

    #Animation rebelles
    "Une volée de flèches abat une partie des rebelles qui foncent vers le pont relevé."
    "Harald jaillit du donjon, armé de pied en cap."

    show harald combat_determine_mid at right
    show einar combat_normal_mid at left
    with dissolve

    h "Baissez le pont ! Tous avec moi !"

    menu :

        "Suivez le roi !":
            show einar combat_determine_mid at left
            e "Suivez le roi ! Suivez le !"

        "Massacrez-les":
            show einar combat_furieux_mid at left
            e "En avant, sire ! Massacrez ces chiens !"

        "Ne rien dire":
            e "..."

    hide harald
    hide einar
    with dissolve

    show re combat_blesse_mid at right
    show ogma combat_normal_mid at left
    with dissolve

    "Le roi lance une grande contre-offensive à la tête de son armée."
    "Désorganisés, les rebelles sont séparés en deux groupes. Certains rompent les rangs."
    ge "Tout est perdu ! Fuyez !"
    "Les combats sont déportés dans la plaine devant le château."
    show ogma combat_furieux_mid at left
    o "Restez en place ! J'étriperai moi-même ceux qui s'enfuient !"
    hide re with dissolve
    "Harald parvient au contact d'Ogma et un duel s'engage."
    show harald combat_normal_mid at right with dissolve
    h "Ha ! Tu es celui qui a assassiné mon intendant ?"
    show ogma combat_determine_mid at left
    o "Oui, et je suis prêt à réitérer l'exploit avec un roi !"
    show harald combat_furieux_mid at right
    h "Pourriture ! Tu vas rendre gorge !"
    "La force et la technique de Harald s'opposent à la vitesse et à la ruse d'Ogma."
    "D'une feinte, l'écossais parvient à atteindre le roi au ventre ; pas une goutte de sang ne coule."
    "Harald prend l'avantage petit à petit : la Hache le rend invincible."
    show harald combat_normal_mid at right
    h "Tu ne peux rien contre moi ! Personne ne peut rien ! Rends-toi !"
    show ogma combat_normal_mid at left
    o "Jamais !"
    show harald combat_furieux_mid at right
    h "Meurs, chien maigre !"
    "Du plat de sa hache, Harald frappe Ogma au torse, lui brisant les côtes et le jetant à terre."
    "Le roi s'apprête à achever le chef rebelle."

    show einar debout_normal_mid at center with dissolve

    menu :

        "Tuez-le !":
            show einar debout_furieux_mid at center
            e "Tuez-le, sire !"
            jump e_laisse_ogma_mort_defendre_porteS
        "Ne le tuez pas ! (s'interposer)":
            show einar debout_furieux_mid at center
            e "Non ! Ne l'achevez pas !"
            jump e_sauve_ogma_defendre_porteS


label e_laisse_ogma_mort_defendre_porteS:

    show ogma combat_normal_mid at left
    "La Hache Sainte s'abat. Ogma est tranché en deux, répandant ses entrailles sur le sol."
    hide ogma with dissolve
    "Immédiatement, les rebelles se dispersent, traumatisés de voir leur héros vaincu par le roi viking."

    show einar combat_normal_mid at left

    menu :
        "Joli !":
            show einar debout_souriant_mid at left
            e "Beau coup, sire !"
            show harald debout_normal_mid at right
            h "Ha ha ! Le compliment me va droit au coeur !"
            h "Regarde ses yeux ! Je suis sûr qu'il est encore conscient !"
            "Un huscarl s'approche pour achever l'écossais."
            show harald debout_normal_mid at right
            h "Non ! Laisse-le comme ça ! Je veux qu'il pourrisse ici !"

        "Regardez les fuir !":
            show einar debout_souriant_mid at left
            e "Regardez-les détaler comme des lapins !"
            show harald debout_normal_mid at right
            h "Ha ha ! Fabuleux !"
            show harald debout_determine_mid at right
            h "Rattrappez-les, vous autres !"

        "J'aurais dû faire ça moi-même":
            show einar debout_normal_mid at left
            e "Si je n'ai qu'un regret, c'est de ne pas l'avoir tué moi-même !"
            show harald debout_normal_mid at right
            h "Ha ha ! Tu pourras passer tes nerfs sur les prisonniers que nous allons faire !"

    hide einar
    hide harald
    with dissolve

    jump cour_chateau_ogma_mort_defendre_porteS

label cour_chateau_ogma_mort_defendre_porteS:

    "..."
    "Dans la cour du château, les prisonniers rebelles sont tous attachés sur des bûchers."
    "Parmi les dizaines d'écossais, une jeune femme rousse se distingue par son visage impassible."
    show einar debout_normal_mid at left
    show gv debout_rire at right
    with dissolve
    gv "Regarde-moi celle là ! Si c'est pas dommage qu'elle soit condamnée ! Je lui aurai bien fait son affaire !"
    gv "Hé, la rouquine ! On se retrouve là-haut ? Ha ha ha !"
    hide gv with dissolve
    show einar debout_attriste_mid at left
    e "..."
    show moira debout_normal_mid at left with dissolve
    "Lorsqu'elle remarque Einar dans la foule, Moira se crispe et son regard s'emplit de haine."
    show moira debout_furieux_mid at right
    show patrick debout_normal_mid at right with dissolve
    p "Vous avez défié l'élu divin, porteur de la Hache Sainte !"
    show patrick debout_furieux_mid at right
    p "Pour vos blasphèmes, votre hérésie et votre félonie, il n'est d'autre jugement que la mort !"
    hide moira with dissolve
    show harald debout_determine_mid at left with dissolve
    h "Hâtez-vous, Patrick ! Il me tarde de les voir se tortiller sur leurs poteaux !"
    show patrick debout_normal_mid at right
    p "Bien, bien. Que Dieu ait pitié de vos âmes !"
    "Deux hommes amènent des torches et commencent à embraser les bûchers."
    show harald debout_normal_mid at left
    h "Ha ha ! Le Seigneur nous offre un beau spectacle à travers son jugement !"
    "Les porteurs de torches s'approchent du bûcher de Moira."

    hide harald
    hide patrick
    with dissolve

    show moira debout_attriste_mid at left with dissolve

    menu :
        "Qu'elle brûle comme les autres":
            show einar debout_furieux_mid at left
            jump bad_ending_19
        "Je dois sauver Moira !":
            show einar debout_determine_mid at left
            jump bad_ending_20

label e_sauve_ogma_defendre_porteS:

    show einar combat_normal_mid at center
    show harald combat_hache_furieux_mid at left
    show ogma combat_furieux_mid at right
    with dissolve

    "Einar dévie le coup de hache du roi et sauve Ogma."
    "Emporté par son élan et son propre poids, la Hache se fiche dans le sol, déstabilisant Harald."
    "Voyant que le roi a relâché son emprise sur la relique, Ogma en profite pour trancher les deux tendons d'achille du roi."
    "Harald tombe aux côtés d'Ogma, qui l'achève en lui enfonçant son coutelas dans la gorge."
    hide einar
    hide harald
    with dissolve
    "Aussitôt la horde rebelle resserre son étau sur les vikings, investie par une nouvelle vigueur."
    "Pris au coeur de la mêlée, Einar est piétiné et laissé pour mort."

    "..."
    show ogma combat_hache_brandir at right
    "Lorsqu'il reprend ses esprits, Einar voit Ogma sur les remparts, brandissant la Hache Sainte. Derrière lui, le château brûle."
    "Depuis les remparts, Ogma semble remarquer le mouvement d'Einar au milieu des cadavres."

    #Rerpise
    show einar debout_blesse at left with dissolve
    show ogma combat_hache_determine_mid at right

    if moira_dead:
        "Ogma court vers Einar, la Hache levée."

        menu :
            "En colère pour Moira ?":
                show einar debout_blesse at right
                e "Tu es en colère à cause de ta fille, c'est ça ?"
                e "Rien ne m'obligeait à la tuer, je l'ai fait parce que j'en avait envie !"

            "J'aurais voulu un combat plus équitable":
                show einar combat_blesse_mid at right
                e "J'aurais souhaité un combat honorable, un peu plus juste !"
                show ogma combat_hache_determine_mid at right
                o "PAS D'HONNEUR !"

            "Elle était toute excitée !":
                show einar debout_souriant_mid at right
                e "Au moment où j'ai tué ta fille, elle s'apprêtait à me chevaucher comme une folle !"

        hide einar
        hide ogma
        with dissolve

        jump bad_ending_22

    else:

        show ogma debout_normal_mid at right
        show einar debout_blesse at left
        "..."
        o "Je ne comprends pas tes actes."
        o "Je te suis malgré tout reconnaissant pour la victoire sur Harald, et pour m'avoir sauvé la vie alors que rien ne t'y obligeait."
        show ogma debout_attriste_mid at right
        o "Néanmoins, ta double trahison a coûté la vie à bien plus d'hommes que nécessaire, dans un camp comme dans l'autre."
        o "Pourquoi avoir agi ainsi ?"

        menu :

            "J'ai eu des remords":
                show einar debout_attriste_mid at left
                e "J'ai été le jouet de mes propres remords."
                show ogma debout_contrarie_mid at right
                o "Ton inconstance a été terriblement coûteuse..."
                o "J'en viendrais presque à regretter de t'avoir choisi pour cette \"mission\"..."

            "J'ai pensé à Moira":
                show einar debout_attriste_mid at left
                e "J'ai pensé à ce qu'il adviendrait de Moira si Harald triomphait."
                show ogma debout_contrarie_mid at right
                o "Alors c'est l'affection que tu portes à ma fille qui m'a sauvé ?"
                o "Je crois que c'est pire que ce que je pensait..."
                o "Tu imagines bien qu'après tout ça, tu ne verras plus ma fille."

            "Ce n'est qu'un jeu":
                show einar debout_souriant_mid at left
                e "J'ai simplement eu l'envie de prendre à leur propre jeu deux dirigeants ambitieux."
                show ogma debout_furieux_mid at right
                o "Je ne sais pas si tu es terriblement cruel ou bien complètement fou."
                o "Combien sont morts aujourd'hui par ta faute ?"
                show ogma debout_contrarie_mid at right
                o "Tu as pris à la légère des enjeux qui te dépassaient complètement."
                show ogma debout_furieux_mid at right
                o "Tu pouvais devenir un héros, un libérateur ! Tu aurais même pu devenir un nouvel empereur, si tu avais été suffisamment égoïste et ambitieux !" #Tu étais l'élu !
                o "Je crois que j'aurais préféré cette alternative, plutôt que d'avoir à subir un tel massacre..."

        show ogma debout_attriste_mid at right
        o "Quoi qu'il en soit... Je vais t'épargner. Crois bien que l'envie de te tuer est grande, mais je refuse de tuer une personne de plus aujourd'hui. Et je te dois la vie."
        o "Prend cet antidote. Ce sera ta seule récompense."
        "Einar boit le contenu de la petite fiole."
        show ogma debout_determine_mid at right
        o "Cependant, je te banni d'Ecosse à tout jamais. Bien entendu, tu n'auras pas l'or promis."
        o "J'espère que tu nous considères comme quittes."
        o "Tu n'as plus qu'à partir sur le champ."
        "Des guerriers rebelles entourent Einar."

        menu :
            "Adieu":
                show einar debout_normal_mid at left
                e "Adieu."
                o "..."

            "Et Moira ?":
                show einar debout_normal_mid at left
                e "Et Moira ? Où est-elle ?"
                show ogma debout_furieux_mid at right
                o "Ne prononce même pas son nom. Je ne veux plus que tu ais le moindre rapport avec elle. Elle ne le veut pas non plus."
                show ogma debout_normal_mid at right
                o "Pars, maintenant."

            "Je rentre en Norvège":
                show einar debout_normal_mid at left
                e "Je ne comptais pas rester. Il est temps que je rentre en Norvège."
                show ogma debout_normal_mid at right
                o "Peu importe où tu vas, pourvu que tu quittes l'Ecosse."

            "Quel ingrat !":
                show einar debout_contrarie_mid at left
                e "Quelle ingratitude ! Et dire que je vous trouvais sympathique !"
                show einar debout_normal_mid at left
                show ogma debout_contrarie_mid at right
                o "Je ne suis pas certain que l'humour soit opportun."
                o "Va-t-en, avant que je ne te tue."

        hide einar
        hide ogma
        with dissolve

        jump bad_ending_21
