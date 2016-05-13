#Acte 3

#Sequence 1
label cote_2:
    scene bg mer with dissolve

    show einar debout_normal at center with dissolve

    e "Dunbar. Déjà..."
    e "..."

    jump exterieur_chateau_1

#Sequence 2
label exterieur_chateau_1:

    scene bg pont_levis with dissolve

    show einar debout_normal with moveinleft
    show garde_chateau normal at right with dissolve

    e "Je ne saurais pas dire si je suis content de revoir leurs trognes..."

    gc "Einar ! C'est bien toi ?"
    e "..."
    gc "Tout le monde te croyait mort !"
    gc "Qu'est-il arrivé aux autres ?"

    menu :

        "Pousse-toi":
            e "Écarte-toi, Geir! Je dois parler au roi sans tarder !"
            gc "Bien sûr, excuse-moi."

        "Explications vagues":
            e "Il m'est arrivé toutes sorte de chose que je n'ai ni le temps ni l'envie de te raconter. Les autres sont tous morts et j'ai bien failli y passer aussi."
            e "Maintenant, laisse-moi passer."
            gc "Bien sûr, excuse-moi."

        "Menacer":
            e "Laisse-moi passer, andouille. On ne barre pas la route à un huscarl ! Je dois voir le roi au plus vite !"
            gc "Bien sûr, excuse-moi."


    hide garde_chateau with dissolve

    jump cours_chateau_1

#Sequence 3
label cours_chateau_1:

    scene bg cours_chateau with dissolve

    $ retour_silence_1 = False
    $ soupcon_harald_1 = False
    $ mentir_harald_1 = False
    $ interpose_bucher = False

    show einar debout_normal at center with dissolve

    "*Harald est en grande discussion avec un huscarl au milieu de la cour*"
    e "Sire ! Sire !"
    h "... dois nous faire venir de nouveaux navires de guerre, et..."
    h "Einar ? Que... D'où viens-tu ? Où as-tu passé tout ce temps ? Où sont tes compagnons ? J'ai beaucoup de questions à te poser !"

    show einar debout_normal at left
    show harald debout_normal at right

    menu:

        "Content d'être rentré":
            e "Quel plaisir de vous retrouver, mon roi !"
            h "La surprise est bonne ! Je désesperais de te revoir un jour. J'étais convaincu d'avoir perdu l'un de mes meilleurs huscarls !"
            h "A vrai dire, je tenais pour acquis que tu étais mort quelque part dans le nord, victime des rebelles..."

        "Peur de ne pas revenir":
            e "J'ai bien cru ne jamais revenir, sire."
            h "Eh bien après tous ce temps, on te croyait mort. J'étais persuadé que toi et tes compagnons étiez morts de la main des rebelles !"
            h "J'ai d'ailleurs passé tout le temps depuis ta disparition à envoyer des troupes raser l'Ecosse. Ces ordures de rebelles finiront par se montrer en voyant leur peuple se faire exterminer."
            h "Crois-moi, les écossais ont payé le prix fort pour votre disparition, à toi et tes hommes !"
            e "C'est un honneur que d'être vengé par son roi !"

        "Ne rien dire":
            e "..."
            h "J'imagine que tu as dû vivre des choses terribles, et que tu dois être épuisé."

    h "Mais dis-moi, que t'est-il arrivé ?"
    h "Et l'escorte qui t'accompagnais ? Et Logan ?"

    menu:
        "Dire ne rien savoir (mentir)":
            e "Je ne sais pas. Nous traversions une forêt en pleine nuit. J'ai été assommé... A mon réveil, il n'y avait plus personne et j'étais abandonné au fond d'un fossé."
            h "Un fossé ?"
            e "Oui, au détour d'un sentier en pleine forêt."
            h "Et tes blessures ? Comment les as-tu soignées ?"
            jump menu_assome_cours_chateau

        "Raconter l'embuscade":
        #modifaction pour indiquer le lieu par la suite
            e "Nous venions de traverser le village de Perth, que nous soupçonnions d'abriter les rebelles."
            e "Nous étions ensuite repartis. Les hommes discutaient entre eux, nous étions sûrs de nous. Puis la nuit est tombée."
            e "Il nous ont prit au dépourvu. Une bande d'une trentaine de guerriers écossais nous est tombée dessus sans que nous ne puissions nous défendre."
            e "Des archers dissimulés dans l'obscurité ont lancé une salve qui a touché un grand nombre des nôtres."
            e "Ensuite, le meneur s'est approché de moi. Il a égorgé Logan sous mes yeux puis m'a assommé."
            h "Qui t'a soigné ? Tu devais être blessé... Je te connais, rien ne t'arrête jamais quand il s'agit de combattre !"

            jump menu_embusscade_ou_silence_cours_chateau

        "Ne rien dire":
            e "..."
            h "Tu dois tout me raconter, Einar. Je ne suis pas idiot, je sais que tes compagnons sont morts. C'est évident. Pourquoi serais-tu revenu seul, sinon ?"
            h "Tu dois me dire ce qu'il s'est passé. Nous devons venger la mort de nos hommes ! Nous devons éradiquer les rebelles !"

            $ retour_silence_1 = True

            jump menu_embusscade_ou_silence_cours_chateau


    menu menu_assome_cours_chateau:

        "Je me suis débrouillé (mentir)":
            e "Je me suis remis, lentement mais sûrement, dans la nature."
            "*Harald hausse les sourcils*"
            h "Dans la nature ? J'ai du mal à te croire..."
            e "J'ai trouvé des plantes et des baies qui m'ont permit de me soigner."
            h "Mmmh..."
            $ soupcon_harald_1 = True

        "J'ai reçu l'aide d'un autochtone (mentir)":
            e "J'ai été soigné par un vieux paysan."
            h "Un paysan ?"
            e "Oui. Il s'appelait Murray. C'était un brave homme. Il m'a trouvé alors qu'il emmenait paître ses moutons. Lorsqu'il a vu mes blessures, il a eu pitié de moi."
            e "Il m'a gardé dans sa cabane pendant un mois entier, à me soigner et à me nourrir."
            e "Une fois remis sur pieds, il m'a laissé partir. Je lui ai promis de le dédommager quand je le pourrais, et il a refusé !"
            h "Tu as eu bien de la chance de tomber sur un homme pareil. Certains t'auraient égorgé sur place."

    menu menu_embusscade_ou_silence_cours_chateau:

        "Village et Moira":
            e "J'ai été aidé par le village que nous avions visité un peu plus tôt, Perth."
            e "Un chasseur m'a trouvé alors qu'il allait relever des collets. Il m'a ramené à son village puis sa fille s'est occupée de moi. Elle s'appelait Moira."
            e "Pendant un mois, cette jeune femme m'a prodigué les soins nécessaires. Lorsqu'enfin mon état s'est amélioré, j'ai pu repartir."
            h "Il ne s'agissait donc pas des rebelles ?"
            e "..."

        "J'ai reçu l'aide d'un autochtone (mentir)":
            e "J'ai été soigné par un vieux paysan."
            h "Un paysan ?"
            e "Oui. Il s'appelait Murray. C'était un brave homme. Il m'a trouvé alors qu'il emmenait paître ses moutons. Lorsqu'il a vu mes blessures, il a eu pitié de moi."
            e "Il m'a gardé dans sa cabane pendant un mois entier, à me soigner et à me nourrir."
            e "Une fois remis sur pieds, il m'a laissé partir. Je lui ai promis de le dédommager quand je le pourrais, et il a refusé !"
            h "Tu as eu bien de la chance de tomber sur un homme pareil. Certains t'auraient égorgé sur place."

        "Perte de mémoire (mentir)" if retour_silence_1:
            e "Je ne me rappelle de rien... Simplement de ce coup à la tête."
            e "Après, il n'y a qu'un grand vide jusqu'à il y a trois jours, lorsque je me suis réveillé dans les bois."
            e "Mes blessures étaient soignées et un repas était posé à côté de moi. Je l'ai mangé et ai prit la route pour revenir jusqu'ici."
            $ soupcon_harald_1 = True

    h "..."
    h "J'espère que tout ce que tu me dis là est vrai."
    h "Je ne tolère pas le mensonge, Einar. Ton histoire me paraît bien obscure. Je te fais confiance, mais si j'apprends que tu m'as menti..."
    h "Es-tu certain de m'avoir dit la vérité ? Si ce n'est pas le cas, je suis prêt à te pardonner pourvu que tu m'avoues ce qu'il s'est réellement passé."

    menu :
        e "(C'est maintenant ou jamais...)"

        "Dire toute la vérité":
            e "Très bien. Voici la vérité."
            e "Après avoir traversé le village de Perth, nous sommes tombés dans une embuscade des rebelles. Ils avaient probablement été prévenus de notre arrivée."
            e "Tous mes compagnons sont morts, y compris Logan."
            h "Et toi ? Tu t'es enfui ?"
            e "Non. Alors que j'avais été mis à terre, le meneur des rebelles s'est approché de moi. J'ai cru mon heure arrivée."
            e "Il s'est penché sur moi puis m'a demandé de coopérer. Je n'ai pas eu d'autre choix que d'accepter."
            e "J'ai ensuite été assommé. A mon réveil, j'étais dans l'une de ces maisons écossaises, comme nous en avions vu au village."
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
            e "Nul ne vous est plus fidèle que moi !"
            $ mentir_harald_1 = True

        "J'ai rusé dans votre intérêt (mentir)":
            e "J'ai rusé de toutes les manières possibles uniquement dans le but de revenir à votre service."
            $ mentir_harald_1 = True

    if mentir_harald_1:
        h "Je te remercie pour ta sincérité, Einar."
        h "Grâce à toi, nous allons profiter de toutes les informations que tu as pu glâner pendant ce mois dans les Highlands."
        h "Mais pour le moment tu devrais rejoindre les autres soldats. Ils seront heureux de retrouver l'un des leurs."
        e "Bien mon Roi."

    else:
        h "Ces salopards comptent attaquer prochainement ? Il faut impérativement préparer nos défenses !"
        e "Le château n'est pas suffisant ?"
        h "Si, mais uniquement si les hommes qui le défendent sont à leurs postes !"
        h "Je te remercie de m'avoir tout avoué. J'ai eu des doutes sur toi pendant un instant, mais me voilà rassuré."
        h "Pendant que je vais planifier la défense du château, tu devrais aller à la rencontre des autres soldats. Ils seront heureux de te retrouver."
        h "Les morts ne reviennent pas tous les jours !"
        e "Bien mon Roi."

    "*Un grand nombre de vikings est massé autour de trois bûchers. Des écossais y sont attachés.*"

    hide einar
    hide harald

    show patrick normal at center with dissolve



    p "Que Dieu, ait pitié de vous ! Les flammes purificatrices vont laver tous vos pêchés."
    p "Deus propitius tibi!"

    show patrick normal at left
    show prisonnier normal at right with dissolve

    pe3 "Arrêtez ! Je suis enceinte !"
    p "Je n'ai que faire de tes mensonges, femme !"
    p "Tes ruses perfides n'obscurciront pas mon jugement !"

    hide prisonnier
    show einar debout_normal at left with dissolve
    show patrick normal at right

    menu:
        "Arrêter le massacre":
            e "Stop! Arrêtez-tout, ce ne sont que de simples paysans !"
            p "Einar ? Tu étais porté disparu depuis un mois !"
            p "Et te voilà sorti de nul part, prêt à défendre ces hérétiques !"
            p "Ces gens ne sont pas innocents ! Ils ont été capturés alors qu'ils menacaient de m'assassiner !"
            e "Une femme enceinte ? Y croyez-vous vraiment, Excellence ?"
            p "Elle était avec eux lorsque nous les avons capturés. Elle ne peut être innocente : elle a avoué !"
            e "Sous la torture ? Vous auriez pu lui faire avouer n'importe quoi !"
            p "Comment peux-tu savoir que ces gens sont innocents ? As-tu des révélations à nous faire ?"

            $ interpose_bucher = True

            jump menu_sauver_rebelle_cours_chateau

        "Ne rien dire":
            e "..."
            
        "Brûlez-les":
            e "Vous avez raison, Excellence !"
            e "Brûlez-les !"

    if interpose_bucher:


        menu menu_sauver_rebelle_cours_chateau:
            "Pas vus à Perth":
                e "Je ne les ai pas vus lorsque j'étais parmi les rebelles de Perth."
                e "Ils ne peuvent donc pas être avec les rebelles que nous recherchons !"
                p "Mensonge ! Ils ont tenté de m'assassiner ! Ils ont tout avoué !"
                p "Ils se sont opposés à un homme de Dieu et ont agi à l'encontre du porteur de la Hache Sainte !"

                if mentir_harald_1 == False and soupcon_harald_1 == False:
                    $ soupcon_harald_1 = True

            "Ils ont l'air innoffensifs":
                e "Je ne sais rien d'eux, mais croyez-vous vraiment que ces trois paysans soient responsables d''une tentative d'assassinat ?"
                e "Une mère ne mettrait pas la vie de son enfant en danger !"

        p "Ne t'interpose pas avec la volonté de Dieu !"
        p "Je pourrais croire que tu cherches à leur épargner le châtiment qu'ils méritent..."
        p "Et tu vois toi-même le sort réservé aux traîtres !"

    p "Amenez les torches, et que brûlent les hérétiques !"
    
    pe1 "Pitié ! Epargnez ma femme !"
    pe3 "Je porte un enfant ! Vous ne pouvez pas faire ça !"
    pe2 "Laissez partir les autres ! Je suis responsable de tout !"
    
    p "Plus rien ne vous sauvera, misérables ! Que s'accomplisse le châtiment !"
    
    "*Un homme apporte une torche. Un par un, il allume les bûchers."
    gv "Regardez-les s'agiter comme des vers, ha ha !"
    "*Alors que l'assistance se réjouit devant ce triste spectacle, Einar remarque un jeune soldat en retrait.*"
    "*Le soldat semble mal à l'aise et au bord des larmes. Einar se dirige vers lui.*"

    #Variable
    $ reponse_reconfort = ""

    menu :

        "Une bande de porcs qui rôtissent !":
            e "Ha, souris un peu, gamin ! Ecoute leur graisse bouillir, à ces porcs !"
            $ reponse_reconfort = "pleurer"
        "Pas besoin de les pleurer":
            e "Ne pleure pas ces parasites, ils ne le méritent pas."
            e "Le roi nous a fait venir ici précisément pour punir les traîtres et les infidèles. "
            e "Alors réjouis-toi, gamin ! En voilà trois de moins !"
            $ reponse_reconfort = "pleurer"
        "Nous n'y pouvons rien":
            e "Tu n'aurais rien pu faire. L'évêque est un malade sanguinaire."
            $ reponse_reconfort = "larme_aux_yeux"
        "Ne rien dire":
            e "..."
            $ reponse_reconfort = "larme_aux_yeux"
        "L'évêque peut se tromper, mais pas Dieu":
            e "L'évêque peut se tromper, mais pas le Seigneur. S'ils étaient Justes, les condamnés iront au paradis."
            $ reponse_reconfort = "rassure"

    if reponse_reconfort == "pleurer":
        "*Le jeune soldat pleure sans se cacher.*"
    elif reponse_reconfort == "larme_aux_yeux":
        "*Le jeune soldat semble toujours aussi bouleversé.*"
    else:
        "*Le jeune soldat semble rassuré.*"

    jump cours_chateau_2

#Sequence 4
label cours_chateau_2:
    
    "*Au crépuscule...*"
    gv "Sire ! Sire !"
    h "Qu'y a-t-il ? Parle !"
    gv "Hjalmar vient de repérer des centaines de torches sorties de la forêt ! Ils convergent tous vers le château !"
    h "Les chiens, ils ne manquent pas d'audace ! Ils lancent déjà leur attaque !"
    h "Tous à vos postes de combat ! Huscarls, préparez-vous à défendre la porte ! Je veux vingt archers sur les remparts !"
    "*Une fois ses ordres donnés, Harald disparaît dans le donjon.*"

    jump interieur_grande_porte_chateau_1

#Sequence 5
label interieur_grande_porte_chateau_1:

    "*Einar est posté à proximité du système d'ouverture des portes.*"
    gv "Ha ha ! Depuis le temps que j'attendais ça ! On va casser du rebelle !"
    "*La horde progresse en courant à travers la plaine.*" 
    "*A une centaine de mètres du château, un double son de cor retentit : le signal convenu avec Ogma pour ouvrir le pont-levis.*"

    menu:
        "Ouvrir le pont-levis":
            if soupcon_harald_1:
                jump bad_ending_3
            else:
                jump pont_levis_baisse

        "Laisser fermé":
            if soupcon_harald_1:
                jump soupcon_harald_defendre_porte
            else:
                jump harald_defendre_porte


#Baisser pont-levis
label pont_levis_baisse:
    
    gv "Attendez... Attendez..."
    gv "Tirez ! Abattez-moi ces salopards !"
    "*Une volée de flèches abat une partie des rebelles qui foncent vers le château.*"
    "*Le pont s'abaisse brutalement, laissant le champ libre.*"
    gv "Trahison ! Bloquez le passage, vite !"
    "..."
    "*Les soldats proches se tournent vers Einar.*"

    menu:

        "Reculez !":
            e "Arrière ! Je vous ferai rendre gorge !"
        "Tactique du roi":
            e "C'était une tactique imaginée par notre roi !"
        "Venez, je vous attends !":
            e "Tuez-moi, chiens. Mieux vaut être un traître qu'un oppresseur !"
        "Ne rien dire":
            e "..."

    "*Au même moment, la horde rebelle pénètre l'enceinte, ce qui détourne l'attention des soldats qui attaquaient Einar.*"
    ge "HAAAAA !"
    gv "En formation ! Dressez les boucliers ! Aucun rebelle ne foutra un pied dans cette enceinte !"
    

    "*La horde avance en une masse compacte et nombre de rebelles succombent sous les flèches des vikings.*"
    "*Le gros des forces parvient à franchir le pont-levis et la masse rebelle déferle dans l'enceinte.*"

    if moira_dead:

        "Ogma surgit au milieu de la mêlée, franchissant la Grande Porte. Il se rue sur Einar, un regard fou dans les yeux et la bave aux lèvres. Il hurle le nom de sa fille."

        o "MOIRAAAAAAAAAAAAAAA"

        menu:

            "Je dois essayer de le raisonner"

            "Tuer le père":
                e "L'envie de voir de près un salopard d'écossais déborder de rage !"
            "Votre fille m'insuportait":
                e "J'aimais votre cause, pas votre fille !"
            "C'est parti tout seul":
                e "Je n'ai pas réfléchi !"
            "Viens te battre":
                e "Ferme la et bats-toi, raclure !"

        "Phase de combat, impossible à gagner WIP"

        jump bad_ending_4

    else:

        $ loose_battle = False

        "Pris entre les deux forces, Einar se retrouve face à ses anciens confrères huscarls. Ils le défient et l'insultent."

        "Einar se retrouve pris entre les deux forces et est contraint d'affronter ses anciens confrères huscarls. (Mini-jeu combat) WIP"

        if loose_battle:

            jump bad_ending_5

        else:
            "Ogma rejoint la mêlée et trouve Einar entrain d'achever un huscarl."
            "Il lui demande de brûler le donjon en urgence : si Harald n'est pas encore entrain de se battre, c'est qu'il n'a surement pas fini de s'équiper : il est possible de le piéger !"

            "Ogma réclame que l'on brûle le donjon en urgence."

            menu :
                "Que faire ?"

                "Tu ne me donnes pas d'ordres":
                    e "Je n'ai pas d'ordres à recevoir !"
                    jump e_bruler_donjon_desobeir_donjon

                "Choice 2":
                    e "J'y vais!"
                    jump e_bruler_donjon_obeir_donjon

label e_bruler_donjon_desobeir_donjon:

    "Le jeune soldat qui pleurait lors du jugement survient face à Einar. Il a l'air terrorisé mais résolu, et tue un rebelle."

    menu :
        "Que faire ?"

        "Le tuer":
            e "Désolé petit"
            "Tuer le jeune soldat"

        "L'assommer":
            e "Tu auras peut être la chance de survivre"
            "L'assommer d'un bon coup de poing"

        "L'ignorer":
            e "(Je n'ai pas le temps de m'occuper de lui)"

    "Harald jaillit du donjon, protégé par son armure et portant le terrible Hache Sainte."
    "Il se jette dans les combats et taille un chemin sanglant jusqu'à la porte. La présence de Harald semble redonner courage aux vikings, qui balaient les rebelles."

    "Harald arrive devant Einar, couvert du sang de ses victimes. Il lui explique qu'il le libère de son allégeance, car il n'a plus besoin de ses services."

    menu:
        "Que répondre ?"

        "Ne rien regretter":
            e "Je ne regrette rien."
            h "Crève"

        "Demander pardon":
            e "Je regrette tout et vous demande pardon."
            h "Non"
        "Aucun roi présent":
            e "Je ne vois aucun souverain ici : il n'y a personne pour me libérer d'une allégeance quelconque !"
            h "C'est comme ça que tu me remercie ?"

    "Garde ta langue de traître derrière tes dents ! Harald décapite Einar d'un coup unique et ample, sans lui laisser le temps de parler."

    jump bad_ending_6

label e_bruler_donjon_obeir_donjon:

    $ prendre_hache = False

    "Einar s'élance en direction du donjon, passant à l'arrière des affrontements."
    "Dans le donjon, Einar s'empare d'une torche et commence à mettre le feu aux tapisseries."

    "\"Incendier le donjon\""

    "En se déplacant dans les couloirs, Einar voit Harald par l'embrasure d'une porte, entrain de terminer de s'équiper de son armure. Dans la pièce attenante, la Hache Sainte est accrochée à un râtelier qui lui est réservé."

    "Alors qu'il commence à mettre le feu au donjon, Einar découvre la Hache Sainte, accrochée à un râtelier dans la chambre du roi."

    menu:
        "Que faire de la hache ?"

        "La prendre":
            e "je ressents la puissance!"
            "Harald arrive dans le dos d'Einar et lui demande ce qu'il fait avec la Hache."
            $ prendre_hache = True
            jump e_confrontation_harald_pont_baisse_donjon

        "S'en débarasser":
            "Einar jette la Hache à la mer à travers une meurtrière de la pièce."
            call e_confrontation_harald_pont_baisse_donjon pass (jetee = True) from _call_e_confrontation_harald_pont_baisse_donjon

        "L'ignorer":
            e "Le donjon est en feu, que cette maudite hache brûle avec"
            jump e_confrontation_harald_pont_axe_laissee_baisse_donjon

label e_confrontation_harald_pont_baisse_donjon(jetee = False):

    $ epargner_harld_donjon = False

    if jetee:
        menu :

            "Harald arrive dans le dos d'Einar et lui demande ce qu'il a fait de la Hache."

            "Je l'ai jeté":
                e "La Hache est perdue. Tout est terminé."
            "Je ne sais pas":
                e "Je ne sais pas."
            "Mentir":
                e "J'ai vu Geir la voler !"

    else:

        menu:
            "Harald arrive dans le dos d'Einar et lui demande ce qu'il fait avec la Hache."

            "Harald n'est plus rien":
                e "Je l'ai prise, en même temps que le pouvoir. Vous n'êtes plus rien. Dieu vous a abandonné."
            "Je suis un Dieu":
                e "L'opportunité de posséder une relique sainte était trop grande : me voilà élu divin !"
            "Rétablir l'équilibre":
                e "Je l'ai prise pour vous en priver. Il est temps de rétablir l'ordre naturel des choses."

    h "Comment oses-tu ?"

    "Harald devient comme fou et se jette sur Einar."

    if prendre_hache:
        "Harald place un coup de dague très rapide au flanc d'Einar. Mais il n'est pas blessé. La Hache lui a donné ses pouvoirs."

        menu:
            "Que dire à Harald ?"

            "Fin du règne":
                e "Votre règne s'achève ici et maintenant. Vous allez mourir."
            "Pas de répit":
                e "Pas de paix. Pas de répit. Pas de rémission. Il n'y a que la guerre. Je recommande votre âme."
            "Épargner":
                e "Vous avez déjà perdu. Je vais vous épargner."
                $ epargner_harld_donjon = True
            "Je te suis supérieur":
                e "Je ne compte pas vous tuer : j'ai déjà prouvé ma superiorité sur vous."
                $ epargner_harld_donjon = True
    else:
        "Le combat s'engage entre le roi et l'huscarl"
        "Phase combat WIP"

        menu:
            "Gagner":
                jump win_battle_harald_no_axe_pont_baisse_donjon
            "Perdre":
                jump bad_ending_12

    if epargner_harld_donjon:
        menu :
            "Que dois-je faire de lui ?"
            "Le laisser s'enfuir":
                jump fuite_harald_pont_baisse_donjon

            "Le livrer à Ogma":
                "Ogma se place au dessus des remparts avec Harald à genoux devant lui, s'assurant que les rebelles ainsi que les survivants vikings voient leur roi se faire trancher la gorge avant d'être précipité dans la mer."
                "Le château brûle."
                jump good_ending_11

    else:
        "Dans la cour, Ogma félicite Einar pour avoir triomphé de Harald. Einar est le libérateur des écossais."
        "Ogma réclame la Hache : elle doit être détruite."

        menu:
            "Que faire ?"
            "Donner hache":
                jump good_ending_7
            "Donner hache":
                jump e_garder_hache_pont_baisse_donjon

label e_confrontation_harald_pont_axe_laissee_baisse_donjon:
    "Einar continue son oeuvre, incendiant le mobilier et tout ce qui peut l'être. Les flammes sont de plus en plus importantes et dévorent la structure."
    "Harald arrive dans le dos d'Einar et lui demande ce qu'il a fait, et pourquoi."

    menu :
        "Que répondre ?"
        "Liberté":
            "J'ai voulu croire en la Liberté d'un peuple sur ses propres terres."
        "Las des promesses":
            "J'étais las de vos promesses de terres et d'or qui ne se réalisaient jamais"
        "Vous être un monstre":
            "J'ai rencontré une jeune femme et son père, qui ont su me convaincre que vous êtes un monstre."
        "Provoquer":
            "Simplement l'envie de mettre un coup de pied dans la fourmilière."

    "Harald est déçu. Il brandit la Hache et demande à Einar s'il est conscient qu'il va mourir sans rien pouvoir y faire."

    menu :
        "Que répondre ?"

        "J'ai mon amulette protectrice":
            e "C'est l'occasion de voir si ce vieux grigri fonctionne vraiment."
            e "Même à l'article de la mort, tu continues à être insolent."

        "C'est mon choix":
            e "Peu importe : j'ai fait ce que je devais faire"
            e "Au moins, Einar aura suivi ses convictions. Quitte à trahir les siens et tuer ses frères."

        "Demander pardon":
            e "Et si j'implore votre pardon ?"
            e "C'est une blague ?"

        "Vous avez déjà perdu":
            e "Me tuer ne changera rien au fait que vous avez perdu cette bataille."
            h "Harald rassure Einar : ce petite soulèvement écossais n'écornera pas sa toute-puissance"

    "Harald effectue un moulinet rapide qui désarme Einar. En se retournant, il le fend en deux d'un seul coup et laisse le cadavre tomber au sol. Il quitte la pièce en marchant."

    jump bad_ending_16

label win_battle_harald_no_axe_pont_baisse_donjon:

    $ epargner_harld__no_axe_donjon = False

    "Einar parvient à briser le bras du roi et à lui infliger un coup sérieux au visage. Harald est au sol. Il reconnaît la supériorité d'Einar et implore sa pitié."


    menu :
        "Que dire à Harald ?"

        "Fin du règne":
            e "Votre règne s'achève ici et maintenant. Vous allez mourir."
        "Pas de répit":
            e "Pas de paix. Pas de répit. Pas de rémission. Il n'y a que la guerre. Je recommande votre âme."
        "Épargner":
            e "Vous avez déjà perdu. Je vais vous épargner."
            $ epargner_harld__no_axe_donjon = True
        "Je te suis supérieur":
            e "Je ne compte pas vous tuer : j'ai déjà prouvé ma superiorité sur vous."
            $ epargner_harld__no_axe_donjon = True


    if epargner_harld__no_axe_donjon:
        jump e_epargne_harald_no_axe_donjon
    else:
        call lieu_encore_inconnu_1 pass (axe = False) from _call_lieu_encore_inconnu_1

label e_epargne_harald_no_axe_donjon:

    $ harald_echape_no_axe = True

    h "Tu comptes me laisser en vie ? Mais pourquoi ?"

    menu:
        "Que répondre"

        "Choice 1":
            e "Vous pouvez fuir, seul. Vous êtes privé de la Hache et vous avez été vaincu. Votre Empire s'écroulera. Je n'ai pas besoin de me faire régicide pour savoir que j'ai gagné."
        "Choice 2":
            e "Fuyez, avant que je ne change d'avis. Ne me demandez pas d'explications."
        "Livrer au Hurleur":
            e "Je vais vous livrer au Hurleur. Il saura quoi faire de vous. Tout ceci n'est plus de mon ressort."
            $ harald_echape_no_axe = False
        "Faire peur":
            e "Je connais quelques personnes qui voudraient vous rencontrer."
            $ harald_echape_no_axe = False

    if harald_echape_no_axe:
        "Harald s'échappe sans demander son reste. Par une meurtrière, Einar voit le roi sur une barque, sortant d'une anfractuosité au pied de la falaise."
        "Harald s'échappe par la mer, empruntant une petite barque qu'il semblait avoir dissimulé dans une anfractuosité naturelle."
        "La bataille arrive à sa fin. Les rebelles achèvent les vikings qui rampent au sol."
        "Depuis les remparts, Ogma observe Harald fuir sur la mer. Puis il regarde Einar, semblant lui faire comprendre qu'il sait qu'il lui a permit de s'enfuir."

        "Un peu plus tard..."

        "Ogma est déçu mais comprend pourquoi Einar a laissé s'enfuir le roi : sans sa Hache, l'empire va s'effondrer sous peu."

        jump village_5
    else:
        "Un peu plus tard"
        "Ogma est sur les remparts, au dessus de la mer. Harald est à genoux devant lui."
        "Sous les yeux des rebelles et des survivants vikings, Il tranche la gorge du roi et propulse son cadavre dans la mer. Derrière, le château brûle."
        jump village_6

label village_5:
    "Ogma remercie Einar pour avoir tenu sa parole et lui donne l'or convenu."
    "Mais il lui explique qu'il ne pourra jamais avoir une totale confiance envers celui qui a son ennemi de s'enfuir : il demande à Einar de quitter l'Ecosse pour toujours."

    menu:
        "Que lui répondre ?"

        "Suivi sont coeur":
            e "J'ai fait ce qui me semblait juste. Je regrette que nous nous éparions en ces termes."
        "Etre désolé":
            e "Je regrette de l'avoir laissé partir. J'espère que vous me pardonnerez. "
        "Partir":
            e "Je ne comptais pas rester ici. Adieu."


    jump foret_4

label village_6:

    $ refuer_ogma_main_moira = False

    "Ogma félicite Einar pour avoir triomphé de Harald. Il lui donne la part de trésor promise. Moira se tient légèrement à l'écart."

    menu:
        "Que dire ?"
        "Remercier":
            e "Je vous remercie."
        "Regrets":
            e "L'or ne rachètera pas les vies qui ont été perdues, ni ma traîtrise envers les miens."
        "Juste une question de survie":
            e "Ce que j'ai fait, je l'ai fait pour survivre, vous m'y obligiez. Je ne veux pas de cet or."
            o "Cette décision t'honore."

    "Ogma décide d'offrir la main de sa fille à Einar : parce qu'il sait qu'ils s'aiment, et qu'il serait heureux d'avoir celui qui a permis la libération de son peuple dans sa famille."
    "Moira lance un regard plein d'espoir vers Einar."

    menu:
        "Accepter de se marrier avec Moira ?"
        "Même sans votre concentement":
            e "SI vous ne me l'aviez pas proposé, j'aurais enlevé votre fille ! Ha ha !"
        "Un honneur":
            e "J'accepte. C'est un grand honneur que vous me faites."
        "Pas de sentiments":
            e "Ces sentiments ne sont pas partagés. Je préfère conserver ma liberté."
            $ refuer_ogma_main_moira = True

    if refuer_ogma_main_moira:
        "Moira s'en va. Elle pleure probablement mais ne le montre pas. Ogma est profondément déçu et demande à Einar ce qu'il compte faire désormais"

        menu:
            "Que faire par la suite ?"
            "Ermite":
                e "Rester ici, en Ecosse. Seul."
            "Norvège":
                e "Rentrer en Norvège, malgré le danger. C'est sa seule demeure."
            "Vivre au jour le jour":
                e "Errer. Il n'y a pas de plan bien déterminé."
            "Asie":
                e "Aller en Asie, là où personne ne viendra le chercher. C'est une région du monde qui l'a toujours intrigué."

        call good_ending_15 pass (marier = False) from _call_good_ending_15
    else:
        jump good_ending_15

label foret_4:

    $ premier_refus_moira_foret_4 = False
    $ rejeter_moira_foret_4 = False

    "Dans la forêt, Einar voit Moira sur le sentier. Elle lui explique qu'elle a décidé de venir avec lui. Elle trouve son père injuste et elle aime Einar."

    menu menu_reponse_moira_suivre_einar:
        "Que dire ?"

        "Pas de raison de le suivre" if premier_refus_moira_foret_4 == False:
            e "Je ne sais pas où je vais. Tu n'as aucune raison de venir avec moi."
            $ premier_refus_moira_foret_4 = False

        "Pas contrarier Ogma" if premier_refus_moira == False:
            e "Je ne veux pas me mettre en porte-à-faux vis à vis de ton père. Laisse moi partir seul."
            $ premier_refus_moira_foret_4 = False

        "Pas les même sentiments":
            e "Nous ne partageons pas les même sentiments. Je ne t'aime pas. Rentre chez toi."
            $ rejeter_moira_foret_4 = True

        "Tendre les bras":
            "(Ne rien dire mais lui tendre les bras.)"
        "Viens":
            "Viens avec moi"

    if rejeter_moira_foret_4:
        call good_ending_14 pass (rejete = True) from _call_good_ending_14
    else:
        jump good_ending_14

label fuite_harald_pont_baisse_donjon:
    "Harald s'échappe sans demander son reste. Par une meurtrière, Einar voit le roi sur une barque, sortant d'une anfractuosité au pied de la falaise."
    "Harald s'échappe par la mer, empruntant une petite barque qu'il semblait avoir dissimulé dans une anfractuosité naturelle."
    "La bataille arrive à sa fin. Les rebelles achèvent les vikings qui rampent au sol."
    "Depuis les remparts, Ogma observe Harald fuir sur la mer. Puis il regarde Einar et remarque qu'il est en possession de la Hache. Il la lui réclame."

    menu:
        "Que faire ?"
        "Conserver la Hache":
            jump e_garder_hache_pont_baisse_donjon
        "Donner la Sainte Hache":
            jump normal_ending_10


label e_garder_hache_pont_baisse_donjon:
    "Ogma se montre menaçant et tend la main pour se saisir de la Hache."

    menu :
        "Que dire ?"
        "Reculez !":
            e "Recule !"
        "Je la mérite":
            e "J'ai pris cette Hache des mains d'un empereur. Je suis le seul à la mériter."

    "Ogma est désarçonné par l'attitude d'Einar : il le sait désormais immortel et invincible."

    o "Que comptes-tu faire de la relique ? Elle devrait être détruite. Elle a déjà provoqué suffisament de malheurs et asservi trop d'hommes."

    menu:
        "Répondre quoi ?"
        "La détruire soi-même":
            e "Je la détruirai moi-même. C'est mon devoir."
            jump lieu_encore_inconnu_1
        "La garder !":
            "Je l'ai prise, elle m'appartient. J'ai bien mieux à faire que de détruire une telle merveille. Le monde m'appartient."
            jump good_ending_9


label lieu_encore_inconnu_1(axe = True):

    $ demander_main_moira = False
    $ refuser_or = False

    if axe:
        "Ogma remercie Einar d'avoir détruit la hache : il aurait surement été tenté d'en faire mauvais usage. Einar reçoit sa part du trésor. Moira se tient à l'écart."
    else:
        "Ogma félicite Einar pour avoir triomphé de Harald. Il lui donne la part de trésor promise. Moira se tient légèrement à l'écart."

    menu:
        "Que dire ?"

        "Demander la main de Moira":
            e "Ogma, j'aimerais vous demander plus. La main de votre fille."
            "Je ne peux accepter. Je refuse de condamner ma fille et sa descendance à partager le nom d'un régicide. Comprends bien que je sois navré et que tout ceci me remplisse d'amertume."
            $ demander_main_moira = True

        "Remercier":
            e "Je vous remercie."

        "Prendre l'or avec amertume":
            e "L'or ne rachètera pas les vies qui ont été perdues, ni ma traîtrise envers les miens."

        "Refuser l'or":
            e "Ce que j'ai fait, je l'ai fait pour survivre, vous m'y obligiez. Je ne veux pas de cet or."
            $ refuser_or = True


    if demander_main_moira:
        menu menu_demande_main_moira_lieu_encore_inconnu_1:
            "Comment réagir ?"
            "Accepter la décision":
                e "Je comprends."
            "Avis Moira":
                e "Moira, qu'en penses-tu ?"
                "Elle répond qu'elle est triste mais qu'elle ne peut que se ranger à l'avis de son père."
            "Pas à Ogma de décider":
                e "Moira, qu'en penses-tu ?"
                "Elle demande à Einar de se calmer. Elle est triste mais elle ne peut que se ranger à l'avis de son père."

    if refuser_or:
        o "Cette décision t'honore. Et maintenant ? Que vas-tu faire ?"
    else:
        o "Ogma demande à Einar ce qu'il compte faire désormais"


    menu plan_futur_lieu_encore_inconnu_1:
        "Que faire par la suite ?"

        "Profiter" if refuser_or == False:
            e "Dépenser l'or en femmes et en jeux."
        "Choisir la voie de l'ermite":
            e "Rester ici, en Ecosse. Seul."
        "Rentrer en Norvège":
            e "Rentrer en Norvège, malgré le danger. C'est sa seule demeure."
        "Décider au jour le jour":
            e "Errer. Il n'y a pas de plan bien déterminé."
        "Découvrir l'Asie":
            e "Aller en Asie, là où personne ne viendra le chercher. C'est une région du monde qui l'a toujours intrigué."

    if axe:
        jump good_ending_8
    else:
        jump good_ending_13

#Défendre porte
label soupcon_harald_defendre_porte:

    "Une volée de flèches abat une partie des rebelles qui foncent vers le pont relevé."
    "Lorsque les rebelles parviennent au pont-levis, ils s'apprêtent à dresser une échelle par dessus les douves."
    "Au même moment une troupe de vikings d'élite, dissimulés à l'extérieur du château, prend les rebelles à revers et repousse sans peine la masse devant le pont-levis."
    "Un groupe de rebelles arrive par la mer, profitant du brouillard pour débarquer discrètement à l'intérieur de l'enceinte, derrière les vikings. Ils lancent un deuxième assaut qui divise les efforts des vikings."
    "Harald demande à Einar de mener les huscarls au combat au delà de la porte, qui va céder."

    menu:
        "Mener les huscarls"

        "Autoritaire":
            e "A moi, huscarls !"
        "Dressez vos boucliers":
            e "Je veux une ligne parfaite ! Dressez vos boucliers !"
        "Porte inatteignable":
            e "Nous ne pouvons pas franchir la porte !"

    "La porte finit par s'ouvrir et Ogma pénètre dans l'enceinte. Il fait face à Einar."

    o"Traître ! Tu t'es joué de nous uniquement pour sauver ta vie de lâche ! Regarde combien d'hommes meurent aujourd'hui par ta faute !"

    menu:
        "Que répondre ?"
        "Massacrez-les":
            e "Huscarls, massacrez les rebelles, sans exception ! Mais laissez-moi le chef !"
        "Que des porcs":
            e "Quels hommes ? Je ne vois que des porcs."
        "Ne rien dire":
            e "..."
        "Provoquer":
            e "J'en fini avec toi, et ensuite je retourne m'occuper de ta fille !"

    menu :
        "Un combat s'engage entre Ogma et Einar"
        "Mini jeu combat WIP"
        "Gagner":
            "Einar frappe Ogma en travers du torse avec sa hachette, ce qui le propulse dans les douves."
            "Terrorisés, les rebelles commencent à prendre la fuite. Harald se lance à leur poursuite sur le dos de son cheval et massacre les fuyards en s'amusant."

        "Perdre":
            jump bad_ending_17

    "Un peu plus tard"

    "Harald félicite publiquement Einar pour sa fidélité et sa bravoure."

    menu:
        "Que réondre ?"
        "Remercier":
            e "Merci, mon roi."
            h "Pas de modestie ! Tu nous a tous sauvés."

        "Fidèle":
            e "Je n'ai fait qu'être fidèle. La victoire, nous la devons à tous ceux qui sont morts aujourd'hui."
            h "C'est vrai. Mais ne sois pas si sombre !"

        "Que l'on se souvienne de moi":
            e "J'ai mené l'assaut final et tué le chef rebelle : qu'on se souvienne longtemps de mes exploits !"
            h "C'est vrai. C'est une attitude peu modeste, mais il s'agit véritablement d'exploits. La gloire t'appartient aujourd'hui ! "

    h "Pour tes exploits, voici ta récompense : Stirling et les terres alentours ! J'ai brûlé le village il y a peu, mais les terres fourniront de bons revenus d'ici quelques années."

    menu :
        "Que répondre ?"
        "Remercier":
            e "Merci."
        "Honneur":
            e "Quel grand honneur ! Merci, mon roi !"
        "Terre infertiles":
            e "Des terres brûlées et un village rasé qui ne fourniront rien avant plusieurs années, dans un territoire hostile et isolé ?  "

    jump normal_ending_18

label harald_defendre_porte:

    "Une volée de flèches abat une partie des rebelles qui foncent vers le pont relevé."
    "Harald survient et alnce immédiatement une grande contre-offensive en ouvrant la porte et en chargeant les assaillants personnellement. Désorganisés, les rebelles sont séparés en deux groupes."

    menu :
        "Que faire ?"

        "Suivre le roi":
            e "Suivez le roi ! Suivez le !"
        "Massacrez-les":
            e "En avant, sire ! Massacrez ces chiens !"
        "Ne rien dire":
            e "..."

    "Harald pârvient au contact d'Ogma et un combat s'engage."
    "Harald survient et concentre les efforts de ses troupes sur la grande porte, parvenant à lancer une grande contre-offensive tranchant net dans la progression des rebelles."
    "Les vikings séparent les rangs ennemis en deux et atteignent Ogma. Un combat féroce s'engage entre les deux chefs."
    "Harald prend nettement l'avantage : la Hache le rend invincible. Ogma est au sol et le roi s'apprête à l'achever."

    "Au cours du combat Harald prend l'ascendant et s'apprête à achever Ogma le Hurleur."

    menu :
        "Ogma est en mauvaise posture"

        "Tuez-le !":
            e "Tuez-le, sire ! "
            jump e_laisse_ogma_mort_defendre_porte
        "Arrêtez !":
            e "Non ! Ne l'achevez pas !"
            jump e_sauve_ogma_defendre_porte


label e_laisse_ogma_mort_defendre_porte:

    "Ogma est tranché en deux par l'énorme hache à double tranchant de Harald. Immédiatement les rebelles se dispersent, traumatisés de voir leur héros détruit par le roi viking."

    menu :
        "Que dire ?"
        "Beau coup !":
            e "Beau coup, sire !"
        "Se moquer des rebelles":
            e "Regardez-les détaler comme des lapins ! "
        "J'aurais dû le tuer moi-même il y a déjà longtemps."

    jump cour_chateau_ogma_mort_defendre_porte

label cour_chateau_ogma_mort_defendre_porte:

    "Dans la cour du château, les rebelles survivants sont tous attachés sur des bûchers. Moira fait partie d'eux."
    "Einar assiste à la scène depuis la foule, tandis que Patrick s'apprête à mettre le feu aux bûchers. Harald exulte."

    menu :
        "Que faire ?"
        "Regarder":
            jump bad_ending_19
        "Sauver Moira":
            jump bad_ending_20

label e_sauve_ogma_defendre_porte:

    "Einar dévie le coup de hache et sauve Ogma. Ce dernier en profite pour trancher les deux tendons d'achille du roi et l'achever au sol alors qu'il a laissé sa hache lui échapper des mains."
    "Aussitôt la horde resserre son étau sur les vikings en les massacrant. Einar est piétiné et laissé pour mort."

    "Encore sur le champ de bataille, Einar voit Ogma sur les remparts, brandissant la Hache Sainte."

    "En se réveillant sur le champ de bataille, Einar voit le château brûler. Ogma est sur les remparts, brandissant la hache."

    if moira_dead:
        "Ogma voit Einar et se jette immédiatement sur lui, Hache levée."

        menu :
            "Pourquoi m'attaques-tu ?"
            "Moira ?":
                e "Tu es en colère à cause de ta fille, c'est ça ?"
            "Combat un peu plus honorable":
                e "J'aurais souhaité un combat honorable."
            "Provoquer":
                e "Au moment où j'ai tué ta fille, elle s'apprêtait à me chevaucher comme une folle !"

        "Ogma atteint Einar et le massacre sur place, ne laissant rien de reconnaissable."

        jump bad_ending_22

    else:
        "Ogma remercie Einar pour la victoire sur Harald, mais sa double trahison a coûté la vie à bien plus d'hommes que nécessaire. Pourquoi avoir agi ainsi ?"

        menu :
            "Que dire ?"

            "Remords":
                e "J'ai été le jouet de mes propres remords."
            "Ce n'est qu'un jeu":
                e "L'envie de prendre à leur propre jeu deux dirigeants ambitieux."
            "Étourderie":
                e "L'étourderie, peut-être ?"

        "Ogma pardonne. Mais Einar est banni d'Ecosse à tout jamais et privé de sa récompense. Il n'a plus qu'à partir immédiatement. Des guerriers rebelles l'entourent."

        menu :
            "Que dire ?"

            "Adieu":
                e "Adieu, et sans rancune."
            "Et Moira ?":
                e "Et Moira ? Où est-elle ?"
                o "Ne prononce même pas son nom. Je ne veux plus que tu ais le moindre rapport avec elle. Elle ne le veut pas non plus. Pars, maintenant."
            "Norvège":
                e "Je ne comptais pas rester. Il est temps que je rentre en Norvège."
            "Quel ingrat":
                e "Quelle ingratitude ! Et dire que je vous trouvais sympathique !"

        jump bad_ending_21
