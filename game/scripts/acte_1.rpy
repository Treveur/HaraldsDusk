#ACTE 1

#Sequence 1
label intro:

    #Stop music s'il y en a une en cours
    stop music



    #Variables
    $ intro_dial = False
    $ eclaireur_dial = False

    #Variable menu
    $ plan_choice = True
    $ region_choice = True
    $ enthousiaste_choice = True
    $ confiance_choice = True
    $ tuer_choice = True

    play ambiance wood

    scene bg forest with dissolve

    "Dans la forêt de Westruther, au coeur de l'Ecosse, une troupe de vikings se dirige vers le chateau de Dunbar pour s'y installer et préparer l'expédition punitive visant à mater les rebelles."
    show harald debout_normal_mid at center with dissolve
    "A la tête de la cohorte, Harald, roi-empereur des vikings. Il a décidé de venir punir lui-même les insolents ayant osé défier son pouvoir."
    "Il ne semble pas préoccupé par la situation et rit à gorge déployée avec ses hommes."
    "A ses côtés marche une armée de cent vikings, guerriers et huscarls, impatients d'en découdre : cela fait déjà longtemps qu'ils ne se sont pas battus."
    show logan debout_contrarie_mid at right with dissolve
    "A l'avant du contingent un guerrier écossais éclaire la voie ; Logan a juré fidélité à Harald depuis plus de dix ans et le mène à travers son Ecosse natale jusqu'au château de Dunbar."
    "Logan semble tendu, lui qui est d'ordinaire enjoué et sympathique."
    show einar debout_normal_mid at left with dissolve
    "Vous êtes Einar, l'un des huscarls : un guerrier d'élite, chef militaire et garde personnel du roi."
    "Après vingt ans de loyaux services, Einar est devenu relativement proche du roi et est respecté de tous."


    menu:
        "Sire, sommes-nous proches du château ?":
            hide logan
            with dissolve

            show einar debout_normal_mid at left with dissolve
            show harald debout_normal_mid at right with moveinright

            e "Mon Roi, sommes-nous proches de Dunbar ?"

            h "Nous n'en avons plus pour très longtemps. Une heure, tout au plus."

            menu menu_harald_choice_foret:
                "Quel est le plan ?" if plan_choice:

                    e "Quelles sont les instructions, sire ? A quoi devons-nous nous préparer ?"

                    h "Tout d'abord, nous allons atteindre le château de Dunbar. Là, l'évêque Patrick d'Edimbourg nous accueillera."

                    h "Ensuite, nous planifierons nos actions dans les Highlands. Je veux retrouver le village des rebelles le plus vite possible, mais il ne s'agit pas de raser toute la région !"

                    h "Les rebelles sont encore isolés et peu nombreux, mais un excès de violence de notre part risquerait de mettre le feu aux poudres et de les rendre sympathiques au reste du peuple."

                    e "Et une fois le village retrouvé ?"

                    h "J'aviserai. Mais ces foutus écossais n'apprécieront pas ce qui va leur arriver, tu peux me croire !"

                    $ plan_choice = False

                    jump menu_harald_choice_foret

                "Qu'y a-t-il à savoir sur la région ?" if region_choice:

                    e "Qu'indiquent les cartes à propos de la région, sire ? Je n'ai pas eu le loisir de les consulter."

                    h "Pas grand chose. Des plaines d'herbe rase, des rocailles abruptes, quelques forêts, et la mer."

                    h "Nous ne sommes encore que dans les Lowlands ; les Highlands sont plus au nord."

                    h "Et hormis le nom, je dois dire que je ne vois que peu de différences entre ces deux territoires !"

                    e "La région a l'air inhospitalière..."

                    $ region_choice = False

                    jump menu_harald_choice_foret

                "J'ai hâte de me battre !" if enthousiaste_choice:
                    show einar debout_souriant_mid at left

                    e "Sire, il me tarde de massacrer quelques paysans !"

                    h "Ha ha ! Ne sois pas si hatif, il ne s'agit pas de tuer tout ce qui bouge. Pas pour le moment !"

                    e "Sauf votre respect, Sire, votre Hache nous a privé de nombreuses batailles. D'habitude, vos ennemis se rendent dès qu'ils la voient !"

                    e "Un soulèvement paysan, c'est une chance inespérée !"

                    h "Ton enthousiasme fait plaisir à voir !"

                    $ enthousiaste_choice = False

                    jump menu_harald_choice_foret

                "Je crains pour votre vie" if confiance_choice:
                    show einar debout_contrarie_mid at left

                    e "Sire, votre présence ici m'intrigue... Pourquoi risquer votre vie dans une expedition de moindre importance ? Vous pourriez recevoir une flèche !"

                    h "Je suis l'élu divin, je porte une relique du Christ !"

                    h "La Hache me rend immortel. Une flèche me ferait rire, rien de plus."

                    h "Harald Sigurdsson, roi-empereur des vikings, abattu par une flèche de paysan rebelle ! Ha ha !"

                    e "Ha ! Les dirigeants du monde entier craindraient les écossais !"

                    h "Si j'ai décidé de venir, c'est pour montrer au reste du monde que je ne suis pas l'un de ces anciens rois, mous et immobiles."

                    h "Accompagner les miens sur le champ de bataille me paraît important. Et je ne voudrais pas passer à côté d'une belle bataille ! Ha ha !"

                    $ confiance_choice = False

                    jump menu_harald_choice_foret

                "Continuer silencieusement":
                    e "..."

        "Tu n'as pas l'air bien, Logan":
            hide einar
            hide logan
            hide harald
            with dissolve

            show einar debout_normal_mid at left with dissolve
            show logan debout_contrarie_mid at right with dissolve

            e "Ça va, Logan ? Tu n'as pas desserré les dents depuis Newcastle. "

            l "... Je n'ai pas revu l'Ecosse depuis plus de dix ans."

            l "Je me demande si Aberdeen a beaucoup changé."

            e "La nostalgie de la maison, hein ? Une fois tout ça terminé, tu auras peut-être l'occasion d'y retourner."

            l "Non, merci, je n'y tiens pas."

            menu menu_logan_choice_foret:
                "Tu te souviens de cette bataille ?" if plan_choice:
                    show einar debout_souriant_mid at left

                    e "Tu te souviens de la bataille de Wertheim ?"
                    show logan debout_souriant_mid at right

                    l "L'automne dernier ? Et comment ! Je revois encore les seins de la petite que j'avais attrapé ! J'ai passé une bonne nuit cette fois là !"

                    l "Je ne me rappelle même pas de son nom. Dorthe, Dorothe, quelque chose comme ça. Le lendemain, sur le départ, elle a insisté pour que je l'emmène ! La garce ! Ha ha ! "

                    e "Tu as toujours de la chance quand il s'agit de dégoter de belles filles. Même au milieu de nulle part !"

                    l "Remarque, ça fait un moment que je ne t'ai pas vu avec une fille. Pas une captive, rien ! Monsieur cherche le grand amour ? A moins qu'il ne soit plus du genre à embrasser les garçons ?"

                    e "Ferme la, sale porc. Quand je passe du bon temps, j'aime que la fille ne sois pas en train de se débattre."

                    l "Chacun son truc !"

                    $ plan_choice = False

                    jump menu_logan_choice_foret

                "Tu reconnais le coin ?" if region_choice:
                    show logan debout_normal_mid at right

                    e "Tu reconnais la région ?"

                    l "Pas vraiment. Aberdeen est bien plus loin au nord, je ne suis jamais venu jusqu'ici."

                    l "Cela dit, je ne suis pas dépaysé..."

                    $ region_choice = False

                    jump menu_logan_choice_foret

                "J'ai hâte de me battre !" if enthousiaste_choice:
                    show einar debout_souriant_mid at left

                    e "Ma hache me démange. Je fracasserais bien quelques crânes !"
                    show logan debout_souriant_mid at right

                    l "Moi aussi ! Je ne supporte plus ces voyages interminables. Deux mois que nous n'avons pas combattu ! Et plus d'un an depuis la dernière vraie bataille. Il est grand temps de nous dégourdir un peu !"

                    e "Tuer des écossais ne te posera pas de problème ?"
                    show logan debout_normal_mid at right

                    l "Je n'aurai pas plus de problèmes que toi. Ces gens ont tué l'un des vassaux du roi. C'est une motivation amplement suffisante pour trancher la tête de quelques compatriotes."

                    $ enthousiaste_choice = False

                    jump menu_logan_choice_foret

                "Le roi me paraît sûr de lui !" if confiance_choice:
                    show logan debout_normal_mid at right

                    e "Le roi me paraît bien confiant."

                    l "Il a toutes les raisons de l'être !"

                    l "Il est le plus grand souverain que le monde connaisse. Il porte une hache incrustée des Clous de la Sainte Croix."

                    l "Il est immortel, invincible, et une armée de vétérans marche avec lui."
                    show logan debout_souriant_mid at right

                    l "S'il y a bien une personne sur cette terre qui peut avoir confiance en lui-même, c'est notre roi !"

                    $ confiance_choice = False

                    jump menu_logan_choice_foret

                "Continuer silencieusement":
                    e "..."

        "Ne rien dire":
            e "..."



    hide einar
    hide logan
    hide harald
    with dissolve

    jump plaine_1

#Sequence 2
label plaine_1 :

    play ambiance coast

    scene bg plaine_chateau_matin with dissolve

    "Une heure plus tard, à proximité du château de Dunbar."

    show harald debout_normal_mid at right with dissolve

    h "Ha ! Dunbar, enfin. Un bon repas nous attend !"

    "Un cavalier arrive en trombe et descend de son cheval, avant de courir vers Harald."
    show gv debout_normaux_mid at left with moveinleft

    gv "Sire ! Un rapport des éclaireurs !"

    h "Donne-moi ça..."

    hide gv

    "Harald lit rapidement le rapport."

    h "Mmmh..."

    show einar debout_normal_mid at left with dissolve

    e "Dois-je envoyer un émissaire annoncer notre arrivée ?"

    h "Non, je compte sur toi pour autre chose."

    e "Autre chose ?"

    h "Nos éclaireurs ont repéré des mouvements de troupes au nord."

    e "Les rebelles ?"
    show harald debout_determine_mid at right

    h "Probablement, mais j'ai n'ai aucune certitude. Je veux envoyer un groupe de reconnaissance à l'avant de l'armée, et tirer cette affaire au clair."

    h "Si ce sont bien les rebelles, c'est une chance unique de découvrir où ils se cachent."

    h "Je compte sur toi pour diriger la troupe. Je te confie dix soldats. Ils t'écouteront et ton expérience du pistage vous facilitera la tâche."

    menu menu_harald_eclaireur_foret_1:

        "J'accepte":
            show einar debout_determine_mid at left

            e "Bien, sire. Où les éclaireurs ont-ils repéré ces mouvements ?"

            h "Les rapports manquent de détails, mais Logan m'a parlé de plusieurs petits villages qui pourraient abriter la rébellion."

        "Pourquoi moi ?":

            e "Pourquoi dois-je mener ce groupe de reconnaissance ?"

            h "Je t'envoie en tant qu'homme de confiance. Des éclaireurs ont déjà été assassinés, j'ai besoin d'envoyer quelqu'un qui sache se battre mais qui ait la tête sur les épaules."

            h "Je compte sur ton sang-froid. Il ne s'agit pas de massacrer tout ce que tu trouveras !"

            e "Pourquoi ne pas envoyer toute l'armée ?"

            h "Parce que je veux éviter que la situation ne s'envenime ! Il ne s'agit pas de faciliter la tâche des rebelles en provoquant un soulèvement populaire !"

            jump menu_harald_eclaireur_foret_1

        "Combien de rebelles ?":

            e "Sur combien de rebelles risquons-nous de tomber ? A quoi dois-je m'attendre ?"

            h "Le rapport n'indique que peu de détails. Ils n'étaient que quelques dizaines, cinquante, tout au plus."

            e "Cinquante ? Et nous ne partons qu'à onze ?"

            h "Il n'y a aucun danger. Ce n'est qu'une bande de villageois chétifs. Tu mènes un groupe de guerriers vikings, tu es un huscarl. Rien ne va te résister !"

            h "Mais surtout, tu n'es pas censé te battre contre eux ! Il s'agit d'une mission de reconnaissance, n'engage le combat que si c'est une nécessité absolue !"

            jump menu_harald_eclaireur_foret_1



    show logan debout_souriant_mid at center
    l "Je vais t'accompagner, Einar."

    menu:
        "Merci Logan !":
            show einar debout_souriant_mid at left

            e "Merci beaucoup Logan, tu ne seras pas de trop !"

            l "J'aurais préféré manger à la table du roi ce soir, mais j'avais peur que tu te perdes en forêt !"

            h "Ne vous inquiétez pas, vous aurez tous les deux de quoi boire et manger une fois revenus ! Ha ha !"


        "Je regrette, mais non.":
            show einar debout_determine_mid at left

            e "Je n'ai pas besoin de toi, Logan. C'est une mission de reconnaissance : moins nous sommes, mieux c'est."
            show logan debout_contrarie_mid at center

            l "..."

            h "J'ai personnellement demandé à Logan de t'accompagner. Il est le seul à connaître la région, et il facilitera les relations avec les écossais."

    show einar debout_normal_mid at left
    show logan debout_normal_mid at center
    l "J'ai déjà planifié notre voyage."
    l "Nous passerons Stirling avant la nuit. Demain, nous atteindrons Perth. C'est le premier village douteux sur notre passage. Puis nous nous dirigerons vers Dundee, Forfar..."
    h "Parfait ! Il ne vous reste plus qu'à partir, les hommes vous attendent."

    hide logan
    hide einar
    hide harald
    with dissolve

    jump plaine_2

#Sequence 3
label plaine_2:

    play ambiance coast

    scene bg plaine_cotière_matin with dissolve

    "Le lendemain..."

    show gv debout_normaux_mid at center with dissolve

    gv "Cette mission n'a rien de terrible... Je m'attendais à rencontrer de l'opposition !"
    show gv debout_rire_mid at center
    gv "Nous aurions dû rester plus longtemps à Stirling ! Il y avait une bien belle tavernière qui semblait prête à me sauter sur les genoux !"
    show logan debout_normal_mid at right with dissolve
    l "Ne vous sentez pas à l'abri. Nous ne sommes pas encore arrivés dans le territoire des rebelles, mais ça ne veut pas dire qu'ils ne peuvent pas nous tomber dessus."
    show gv debout_normaux_mid at center

    show einar debout_normal_mid at left with dissolve

    menu:
        "Je suis bien d'accord : on s'ennuie !" :

            e "Et je suis convaincu que nous ne rencontrerons rien de plus excitant qu'une tavernière au milieu de toute cette foutue caillasse !"
            show einar debout_souriant_mid at left

            e "Ha ! Se défouler sur des villageois, ce sera notre récompense !"

            e "Plus vite le problème sera réglé, plus vite nous pourrons glisser nos pieds sous la table et nous remplir la panse !"
            show gv debout_rire_mid at center

            gv "Ha ha ! Bien parlé !"

        "Logan a raison, méfiez-vous" :

                e "Méfiez vous, le roi n'est pas avec nous."

                e "Sans la Hache, nous sommes à la merci de n'importe quel piège. Restez aux aguets !"
                show einar debout_souriant_mid at left

                e "Rien qu'en t'écoutant, je suis sûr que les rebelles connaissent déjà ton nom, celui de tes parents et la taille de ta queue, Alvin."

                gv "Vous avez entendu, les gars ? Ouvrez l'oeil."

        "Envoyer des soldats d'élite est injustifié" :

                e "Je suis bien d'accord..."
                e "Et je suis certain que nous ne rencontrerons rien de plus terrible que des landes et des forêts ! Pourquoi nous envoyer battre la campagne à la recherche d'une bande de péquenauds ?"

                hide gv debout_normaux_mid with dissolve

                show logan debout_normal_close at right with dissolve

                l "Tu le prends comme une punition ?"
                show einar debout_furieux_close at left with dissolve

                e "Oui ! Après tout le temps que j'ai passé à servir Harald, il aurait pu m'attribuer une mission moins ingrate !"

                e "Je n'en suis plus à mon coup d'essai, bordel !"

        "Un problème, Logan ? (chambrer)" :
            show einar debout_souriant_mid at left

            e "Tu ne parles pas beaucoup, Logan... Tu as un problème, ou bien tu attends une autorisation du roi pour l'ouvrir ?"

            hide gv debout_normaux_mid with dissolve

            show logan debout_normal_mid at right with dissolve

            l "..."

            e "Ha, il est obéissant en plus !"

            e "Je suis sûr qu'il retrouvera la parole en présence d'un bel animal ! Séducteur de chèvres !"
            show logan debout_contrarie_mid at right

            l "..."

            gv "Ha ha ha !"

        "Silence ! Je veux deux groupes à l'avant..." :

            hide gv debout_normaux_mid with dissolve
            show einar debout_normal_mid at left

            e "Taisez-vous. Je veux deux groupes à l'avant, deux groupes à l'arrière. Au centre, Logan et moi. Et magnez-vous le train !"

            show logan debout_normal_mid at right with dissolve

            l "Les gars sont aussi fatigués que nous. Tu devrais..."

            e "Toi aussi, tais-toi. Je veux que nous menions cette mission de la façon la plus exemplaire possible."

            l "Bien."

    hide einar
    hide logan
    with dissolve

    jump foret_1

#Scequence 4
label foret_1:

    play ambiance wood

    scene bg forest with dissolve

    "Un jour plus tard..."

    show einar debout_normal_mid at left with dissolve
    show logan debout_normal_mid at center with dissolve

    l "Nous ne sommes plus très loin de Perth, nous devrions y arriver dans l'après-midi."
    show gv debout_normaux_mid at right with dissolve
    gv "J'ai l'impression d'avoir déjà vu cette forêt... Tout se ressemble ici !"
    l "Nous progressons, rassure-toi."
    show gv debout_contraries_mid at right
    gv "Pays de merde ! Le Danemark, ça ressemble quand même à autre chose !"

    menu:
        "La Norvège me manque":
            show einar debout_contrarie_mid at left

            e "Plus le temps passe, plus la Norvège me manque..."

            e "Je ne sais même plus depuis combien de temps je n'y ai pas foutu les pieds."

            gv "J'aimerais retrouver la Suède. Je n'ai aucunes nouvelles de ma famille depuis notre campagne d'Egypte."

            gv "Je n'ai pas de nouvelles non plus. Mon vieux père pourrait bien être mort sans que je n'en sache rien !"
            show logan debout_normal_mid at center with dissolve
            l "Harald doit ressentir la même chose. Il n'a pas vu sa femme ni ses enfants depuis aussi longtemps que nous."
            show gv debout_normaux_mid at right with dissolve
            gv "Qu'est-ce que tu en sais, Logan ? C'est nous ta seule famille !"
            show logan debout_contrarie_mid at center

            l "..."
            hide gv debout_normaux_mid with dissolve

            menu:
                "J'ai hâte de recevoir les terres qui m'ont été promises":
                    show einar debout_normal_mid at left

                    e "Ça fait des années que le roi me fait miroiter des terres en Norvège sans jamais me les offrir..."

                    e "Depuis le temps qu'il me les promet, je devrais déjà vivre comme un prince !"

                    show logan debout_normal_mid at right with dissolve

                    l "Et si ces terres ne sont pas en Norvège ?"

                    e "Peu importe. Tout ce que je veux, c'est enfin pouvoir me sentir chez moi."

                "Assez de niaiseries pour aujourd'hui":
                    show einar debout_normal_mid at left

                    e "Taisez-vous maintenant. La route est encore longue et j'en ai déjà assez d'écouter vos histoires de bonnes femmes."

                    e "Perth n'est plus très loin, restez silencieux."

                    show logan debout_normal_mid at right with dissolve


        "J'imagine la tête de ces salopards d'écossais !" :
            show einar debout_souriant_mid at left

            e "J'imagine la tête des sauvages qui vivent dans la région. Foutus écossais ! Il n'y a qu'à voir la trogne de Logan pour savoir que quelque chose ne tourne pas rond chez ces gens là !"

            e "Je suis persuadé qu'ils vivent dans des cabanes délabrées et qu'ils couchent avec leurs chèvres !"
            show gv debout_rire_mid at center with dissolve
            gv "Ha ha !"

            show logan debout_souriant_mid at right with dissolve

            l "Nous vivons dans des maisons de pierre, à la différence de vos cabanes en bois. Et pour le reste, tu constateras que nous avons bien plus de raisons de coucher avec nos femmes qu'avec nos chèvres."

            hide gv debout_rire_mid with dissolve

        "Je voudrais déjà être rentré" :
            show einar debout_normal_mid at left

            e "Je suis déjà lassé par cette foutue randonnée !"

            e "Une journée à crapahuter sans voir âme qui vive... "

            e "On trouve les rebelles et on rentre au château. Et à bride abattue !"

        "Ne vous découragez pas" :
            show einar debout_normal_mid at left

            e "Ne relâchez pas l'effort. Nous nous sommes suffisamment enfoncés dans les Highlands pour avoir une chance de trouver le village des rebelles."

            e "Tout ça sera bientôt terminé !"

        "Alors Logan ? Tu rêves de brebis ? (chambrer)" :
            show einar debout_souriant_mid at left

            e "Toujours pas envie de parler, Logan ? Trop occupé à rêver du corps d'une de ces magnifiques brebis écossaises ?"

            show logan debout_contrarie_mid at right with dissolve

            l "..."
            show gv debout_rire_mid at center with dissolve
            gv "Ha ha !"
            hide gv with dissolve

        "Que penses-tu de la mission, Logan ?" :

            e "Tu es le seul à ne pas encore t'être plaint..."
            show logan debout_normal_mid at right with dissolve
            l "Je ne vois pas de raisons de me plaindre. J'accomplis mon devoir. Le roi nous récompensera à notre retour."

            e "Il se fout de nous ! Depuis le temps qu'il me promet des terres..."

            menu:
                "Pourquoi as-tu décidé de m'accompagner ?":
                    show einar debout_normal_mid at left

                    e "Pourquoi avoir choisi de m'accompagner ?"

                    l "Même sans être natif du coin, je connais la région mieux qu'aucun d'entre vous."

                    l "Et ma présence facilitera les relations avec les autres écossais."

                    e "Ils ne risquent pas de mal le prendre, au contraire ?"

                    l "C'est une autre possibilité."

                "Je suis content que tu sois là":
                    show einar debout_souriant_mid at left

                    e "Quoi qu'il en soit, merci d'avoir choisi de m'accompagner."
                    show logan debout_souriant_mid at right

                    l "Si un jour une campagne m'amène en Norvège, je serai heureux de compter sur toi."

                "Tu aurais du rester au château":
                    show einar debout_contrarie_mid at left

                    e "Tu aurais du rester avec Harald !"

                    l "Pourquoi ?"

                    menu:
                        "Une vie de plus en danger":
                            show einar debout_normal_mid at left

                            e "C'est une mission de reconnaissance. Nous pourrions tomber dans une embuscade à tout moment !"
                            show logan debout_normal_mid at right

                            l "Ces gens ne sont que des paysans. Ils fuiraient rien qu'en nous entendant arriver."

                            e "Peut-être pas. Tu as mis ta vie en jeu sans raison. Et tu nous rends plus repérables. "

                            l "Plus repérables ? Vraiment ? Quelle différence entre onze et douze hommes ?"

                            e "..."

                        "Tu es inutile":
                            show einar debout_normal_mid at left

                            e "Nous étions déjà bien assez nombreux. Onze guerriers vikings dont un huscarl !"
                            show logan debout_normal_mid at right

                            l "Aucun d'entre vous ne connaît la région."
                            show einar debout_furieux_mid at left

                            e "Je me fout de tes compétences ! Nous ne sommes pas là pour observer un panorama ou cueillir des champignons !"
                            show logan debout_contrarie_mid at right
                            show einar debout_normal_mid at left

                            e "Ces salopards d'écossais sont hostiles. Je n'envisage même pas un dialogue avec eux ! Nous n'avions pas besoin de toi."

    hide einar
    hide logan
    with dissolve

    jump village_1

#Sequence 5
#Scene 1
label village_1:

    play ambiance village

    $ moira_met = False

    scene bg village with dissolve
    "Peu après midi, la dizaine de vikings parvient en vue d'un village..."
    show logan debout_normal_mid at right zorder 5 with dissolve
    l "Nous y sommes. Perth."

    "Les villageois vaquent à leurs occupations. Certains d'entre eux ont remarqué l'arrivée des guerriers vikings et affichent une expression craintive."
    show einar debout_normal_mid at left zorder 5 with dissolve
    e "Ça me semble bien calme."
    show gv debout_normaux_mid at center with dissolve
    gv "On dirait qu'il n'y a pas grand monde..."

    e "Uniquement des vieillards, des femmes et des enfants."

    gv "Ça sent le traquenard..."

    ve "Bonjour, étrangers. Nous pouvons vous aider ?"

    e "Je veux que tout le village se rassemble sur la place, maintenant !"

    e "Toute désobeissance sera punie !"

    ve "Très bien, restez calme."

    "Des villageois sortent de leurs maisons et abandonnent leurs activités pour se rassembler."
    "Il n'y a que très peu d'hommes parmi la cinquantaine de villageois."

    ve "Nous... Nous sommes tous là."

    hide gv debout_normaux_mid with dissolve
    show gv debout_normaux_mid at halfsize, left zorder 1 with dissolve
    show ve debout_craintifs_mid at halfsize, right zorder 1 with dissolve

    menu menu_fouille_village:

        "Où sont les rebelles ?":
            jump e_demander_information_village_1
        "Fouillez le village !":
            jump e_fouiller_village_1
        "Je vais voir moi-même ce que vous cachez ! (fouiller)":
            call e_fouiller_village_1 pass (einarFouille = True) from _call_e_fouiller_village_1
#        "Massacrez-les !":
#            jump e_massacre_village_1

#label e_massacre_village_1:

#    e "Massa..."

#    l "Einar, non ! Nous ne sommes sûrs de rien !"

#    l "Harald nous a envoyé en reconnaissance ! Nous ne sommes pas là pour tuer ces gens !"

#    l "Nous risquons d'aggraver la situation en rasant Perth. Le roi sera furieux !"

#    l "Et je ne parle même pas des écossais ! Nous ne pourrions pas revenir au château sans nous faire égorger sur le chemin !"

#    menu:

#        "Massacrez-les quand même":
#            jump e_massacre_village_2
#        "Tu as raison":
#            jump menu_fouille_village

#label e_massacre_village_2:

#    "Je me fout de ton avis, Logan !"

#    e "Massacrez-moi tout ça ! Et brûlez leurs cabanes !"

#    gv "HAAAAA !"
#    hide logan with dissolve
#    ve "Sauvez les enfants ! Les enfants !"
#    hide ve with moveoutright
#    hide gv with moveoutright
#    call choix_retour_village_1 pass (massacre = True) from _call_choix_retour_village_1


label e_demander_information_village_1:
    show einar debout_determine_mid at left

    e "Que savez-vous des rebelles ? Où sont-ils ?"

    show logan debout_souriant_mid at center with dissolve

    l "Parle, vieil homme. Je suis écossais. Nous ne vous voulons aucun mal."

    ve "Ecossais ? Traître à ta terre et à ton sang ! Tu mènes des envahisseurs parmi les tiens !"

    "Le vieil homme crache sur le sol, devant les pieds de Logan."

    e "Quel succès, Logan."

    hide logan with dissolve

    e "Qui traitez-vous d'envahisseurs ? Ces terres appartiennent au roi-empereur Harald Sigurdsson de Norvège, porteur de le Hache Sainte."
    show einar debout_furieux_mid at center with dissolve

    e "Votre attitude ressemble à un aveu de trahison !"
    show logan debout_normal_mid at center with dissolve

    l "Calme-toi Einar. Comment réagirais-tu si tu voyais une armée byzantine débarquer en Norvège ?"

    e "..."

    menu:
        "Vous voulez vraiment vous opposer à des guerriers d'élite ?":
            jump e_intimider_villageois_village_1
        "Parlez, ou je tue l'un de vos vieux !":
            jump e_tuer_villageois_village_1

label e_fouiller_village_1(einarFouille = False):


    $ moira_met = True
    $ already_talk = False

    if einarFouille:
        show einar debout_determine_mid at left
        e "Bien. Je vais moi-même jeter un oeil. Mieux vaudrait pour vous que vous ne cachiez rien !"

        e "Si qui que ce soit tente de s'enfuir ou se montre agressif, tuez-le."

        "Einar entre dans une maison"


    else:
        show einar debout_determine_mid at left
        e "Fouillez moi ces taudis ! Si vous trouvez quoi que ce soit, ramenez-le moi !"

        gv "HAAAAA !"

        "..."

        gv "Einar ! Une fille, dans une maison !"
        show einar debout_normal_mid at left

        e "Je suis à peine surpris... J'arrive !"

    stop ambiance
    scene bg house
    show moira debout_normal_mid at center with dissolve
    show einar debout_normal_mid at left with dissolve
    menu menu_maison_1:
        "Qui es-tu ?":
            jump e_nom_villageoise_maison_1
        "Pourquoi être cachée ?":
            jump e_cache_villageoise_maison_1
        "Où sont les rebelles ?":
            jump e_info_rebelle_maison_1
        #Si Einar à déjà parlé une fois à Moira
        "Rejoins les autres !" if already_talk:
            jump e_villagoise_partir_maison_1
        "Je n'aime pas qu'on ne suive pas mes instructions (la tuer)" if already_talk:
            jump e_tuer_moira_maison_1
    hide moira
    hide einar
    with dissolve


label e_tuer_villageois_village_1:
    show ve debout_normaux_mid
    show einar debout_furieux_mid at left

    e "Répondez à mes questions ! Je n'hésiterai pas à tuer l'un de vos vieux !"

    show logan debout_determine_mid at center

    l "Harald nous a envoyé en reconnaissance ! Nous ne sommes pas là pour tuer ces gens !"

    l "Nous risquons d'aggraver la situation en rasant Perth. Le roi sera furieux !"

    ve "Nous n'avons rien à vous dire ! Nous ne savons rien !"

    menu:

        "Votre détermination fait plaisir à voir":
            show einar debout_determine_mid at left

            e "Vous seriez prêt à laisser mourir l'un des votres pour couvrir votre rébellion ? Votre détermination fait plaisir à voir !"

            e "Vous n'avez aucun avenir en trahissant l'empire ! Le roi Harald saura se montrer clément avec ceux qui ont coopéré !"

            ve "Nous ne savons rien ! Absolument rien !"

            e "Et vos hommes, où sont-ils ?"

            ve "La plupart d'entre eux ont descendu la rivière Tay jusqu'à Dundee pour y échanger du bétail. Rien de plus !"
            show einar debout_furieux_mid at left

            e "Foutus mensonges !"

            show logan debout_determine_mid at center

            l "Non Einar. C'est bien possible. Ces gens sont une petite cinquantaine tout au plus. L'absence des hommes se fait remarquer, c'est tout."

            show einar debout_normal_mid at left

            e "Très bien. Remerciez celui que vous appelez traître pour avoir défendu votre cause. Nous partons."

            jump choix_retour_village_1


        "Vous l'aurez voulu ! (tuer un villageois)":
            show einar debout_determine_mid at left

            e "Vous l'avez cherché !"

            e "Toi. Approche."

            ve "Moi ?"

            e "Oui ! Dépêche toi !"

            ve "Monseigneur, je ..."

            "Einar tranche la gorge du villageois d'un seul coup."
            show ve debout_effrayes_mid at right

            ve "Pourritures ! Salauds !"

            e "Parfait. Maintenant, parlez."

            ve "Vous ne saurez rien !"

            "Les villageois commencent à se montrer hostiles. Certains brandissent des fourches tandis que d'autres jettent des pierres. Peu à peu, les écossais encerclent le groupe de vikings."

            "Alors qu'il tente de maîtriser la foule, l'un des vikings se fait fracasser le crâne par une pierre. Des écossais se jettent sur lui et le massacrent."

            show gv debout_furieux_mid at center

            gv "Vengeance !"

            e "Je..."

            show logan debout_determine_mid at right

            l "Il est trop tard pour réfléchir ! Ils vont nous massacrer si nous ne réagissons pas !"

            e "Battez-vous ! Tuez-les tous !"

            "Le combat s'engage. Rapidement, les vikings reprennent l'ascendant et réduisent à néant toute résistance."

            call choix_retour_village_1 pass (massacre = True) from _call_choix_retour_village_1_1



label e_intimider_villageois_village_1:
    show einar debout_determine_mid at left

    e "Vous devriez parler. Maintenant. Les soldats que vous avez devant vous ont tué plus d'hommes que vous n'en avez jamais rencontré dans votre vie."
    show ve debout_craintifs_mid at right

    ve "Nous ne savons rien ! Absolument rien !"

    e "Et vos hommes, où sont-ils ?"

    ve "La plupart d'entre eux ont descendu la rivière Tay jusqu'à Dundee pour y échanger du bétail. Rien de plus !"
    show einar debout_furieux_mid at left

    e "Foutus mensonges !"
    show logan debout_determine_mid at center

    l "Non Einar. C'est bien possible. Ces gens sont une petite cinquantaine tout au plus. L'absence des hommes se fait remarquer, c'est tout."
    show einar debout_normal_mid at left

    e "Très bien. Remerciez celui que vous appelez traître pour avoir défendu votre cause. Nous partons."

    jump choix_retour_village_1

#Scequence 6 (alternative)
label e_nom_villageoise_maison_1:
    show einar debout_normal_mid at left
    show moira debout_determine_mid at center

    e "Qui es-tu ?"

    ve "Ne m'adressez pas la parole !"
    show einar debout_determine_mid at left

    e "Je me suis montré courtois, mais ça pourrait vite changer. Réponds !"

    m "Moira."

    $ already_talk = True

    jump menu_maison_1

label e_cache_villageoise_maison_1:
    e "Pourquoi te cacher ?"

    ve "Parce que je connais les porcs dans votre genre."
    show einar debout_determine_mid at left

    e "Mmmh."

    $ already_talk = True

    jump menu_maison_1

label e_info_rebelle_maison_1:
    e "Que sais-tu des rebelles ?"

    ve "Rien."
    show einar debout_determine_mid at left

    e "Tu es aussi belle que décevante."

    $ already_talk = True

    jump menu_maison_1

label e_villagoise_partir_maison_1:
    show einar debout_determine_mid at left
    e "Sors d'ici et rejoint les autres."

    ve "..."

    hide moira

    jump choix_retour_village_1


label e_tuer_moira_maison_1:
    show einar debout_determine_mid at left

    e "Je n'aime pas qu'on se moque de moi. Mes instructions étaient claires ! Cette rencontre s'achève ici."

    "Einar tire la jeune femme par les cheveux sur la place, aux yeux de tous."
    scene bg village with dissolve
    show moira debout_furieux_mid at center

    ve "Lâchez-moi ! Salaud !"

    show logan debout_determine_mid at center

    l "Einar ! Non ! Cette pauvre fille n'a rien fait de mal ! Tu vas compromettre toute la mission ! Souviens-toi des instructions du roi !"

    menu :

        "Tais-toi ! (la tuer)":

            "Le viking abat sa hache sur la nuque de la femme, qui tombe au sol, inerte."
            hide moira
            show logan debout_attriste_mid at center

            l "Cette fille était sans défense !"

            e "Ferme-la. Et maintenant, voyons si les bouseux sont plus enclins à parler !"

            show ve debout_effrayes_mid at right zorder 1

            ve "Monstres ! Ils ont tué Moira !"

            e "Parfait. Maintenant, parlez."

            ve "Vous ne saurez rien !"

            "Les villageois commencent à se montrer hostiles. Certains brandissent des fourches tandis que d'autres jettent des pierres. Peu à peu, les écossais encerclent le groupe de vikings."

            "Alors qu'il tente de maîtriser la foule, l'un des vikings se fait fracasser le crâne par une pierre. Des écossais se jettent sur lui et le massacrent."
            show gv debout_furieux_mid at center

            gv "Vengeance !"

            e "Je..."
            show logan debout_determine_mid at right zorder 2

            l "Il est trop tard pour réfléchir ! Ils vont nous massacrer si nous ne réagissons pas !"

            e "Battez-vous ! Tuez-les tous !"

            "Le combat s'engage. Rapidement, les vikings reprennent l'ascendant et réduisent à néant toute résistance."

            call choix_retour_village_1 pass (massacre = True) from _call_choix_retour_village_1_1


        "... Tu as raison.":
            show einar debout_determine_mid at left

            e "Tu as raison. Elle ne mérite pas que j'émousse ma hache sur elle."

            e "J'ai déjà retenu ma main une fois. Parlez maintenant ! Je ne renoncerai pas deux fois de suite !"

            ve "Nous ne savons rien ! Absolument rien !"

            e "Et vos hommes, où sont-ils ?"

            ve "La plupart d'entre eux ont descendu la rivière Tay jusqu'à Dundee pour y échanger du bétail. Rien de plus !"
            show einar debout_furieux_mid at left

            e "Foutus mensonges !"
            show logan debout_determine_mid at center

            l "Non Einar. C'est bien possible. Ces gens sont une petite cinquantaine tout au plus. L'absence des hommes se fait remarquer, c'est tout."
            show einar debout_normal_mid at left

            e "Très bien. Remerciez celui que vous appelez traître pour avoir défendu votre cause. Nous partons."

            jump choix_retour_village_1


#fin Scequence 6

label choix_retour_village_1(massacre = False):

    hide ve with dissolve
    if massacre:
        show einar debout_normal_mid at left with dissolve
        e "Empilez les cadavres avant le départ."
        show logan debout_attriste_mid at right with dissolve

        l "Nous étions censés trouver le village rebelle, pas massacrer des paysans !"
        show einar debout_determine_mid at left

        e "Ta détermination flanche ? Harald sera sûrement satisfait de voir le travail accompli."

        e "Si c'était les rebelles, nous avons éliminé le problème. Si les gens de Perth étaient innocents, les villages alentours nous craindront."
        show einar debout_souriant_mid at left

        e "Nous gagnons sur tous les tableaux."

        l "J'espère que tu as raison..."

    else:
        show logan debout_determine_mid at right with dissolve
        l "Ces gens ne savaient rien, j'en mettrais ma main à couper."
        show einar debout_normal_mid at left with dissolve

        e "J'espère pour toi que tu as raison, Logan."

    show gv debout_normaux_mid at halfsize, center with dissolve
    gv "Où allons-nous ?"
    hide gv with dissolve
    if massacre:
        menu:
            "Nous retournons à Dunbar":
                call massacre_foret_2 pass (lieu = "chateau") from _call_massacre_foret_2
            "Nous poursuivons vers le nord":
                call massacre_foret_2 pass (lieu = "nord") from _call_massacre_foret_2_1
    else:
        menu:
            "Nous retournons à Dunbar":
                call foret_2 pass (lieu = "chateau") from _call_foret_2
            "Nous poursuivons vers le nord":
                call foret_2 pass (lieu = "nord") from _call_foret_2_1

#Sequence 7
label foret_2(lieu = ""):

    play ambiance wood

    scene bg forest with dissolve

    if lieu == "chateau":

        "Sur le chemin du retour..."
        show gv debout_normaux_mid at center with dissolve
        gv "Pourquoi sommes-nous déjà sur le retour ?"
        show einar debout_normal_mid at left
        e "Parce que j'ai de sérieux doutes sur ce village. Les gens de Perth étaient bien trop louches, quoi qu'en dise Logan."
        hide gv with dissolve
        show logan debout_normal_mid at right
        l "Tu penses avoir trouvé le village des rebelles ? Si facilement ?"

        e "Je ne suis sûr de rien."
        hide gv with dissolve
    else:
        "En poursuivant vers le nord..."
        show gv debout_normaux_mid at center with dissolve
        gv "Pourquoi devons-nous poursuivre vers le nord ? Je croyais que nous avions trouvé les rebelles !"
        show einar debout_normal_mid at left
        e "Rien ne permet d'affirmer ça. J'ai beau avoir des doutes sur Perth, je pense qu'une visite des villages plus au nord sera bénéfique."
        hide gv with dissolve

    play ambiance wood_night

    scene bg forest_night with dissolve
    hide einar with dissolve
    "..."
    show gv debout_normaux_mid at halfsize, center with dissolve
    gv "... et à ce moment là Logan sort de la taverne en feu, une fille sous un bras et la tête du père sous l'autre ! Ha ha !"

    gv "La fille était tellement choquée qu'elle n'a rien dit pendant deux jours ! Cinq de nos gars lui sont passés dessus, elle n'a même pas réagit !"
    show gv debout_rire_mid at halfsize, center
    gv "Ha Ha Ha !"
    show einar debout_normal_mid at left with dissolve
    e "Du favoritisme pour les écossais, Logan ? En temps ordinaires tu ne te serais pas privé de tuer quelques personnes et de profiter d'une jolie fille !"
    show logan debout_normal_mid at right
    l "J'ai eu pitié de ces gens. Ils me faisaient penser à Aberdeen."
    hide gv with dissolve
    e "Je croyais que tu n'aurais aucun problème à tuer des écossais !"

    l "Des écossais rebelles, oui. Pas des innocents."
    show einar debout_souriant_mid at left
    e "Tu te ramollis, mon vieux Logan..."
    show einar debout_normal_mid at left

    menu:
        "Ne relâchez pas votre attention":
            call attaque_massacre_einar_sauf_foret_2 pass (message = "attentif") from _call_attaque_massacre_einar_sauf_foret_2
        "La mission est décevante":
            call attaque_massacre_einar_sauf_foret_2 pass (message = "deception") from _call_attaque_massacre_einar_sauf_foret_2_1
        "Les villageois avaient une attitude suspecte":
            call attaque_massacre_einar_sauf_foret_2 pass (message = "attitude") from _call_attaque_massacre_einar_sauf_foret_2_2
        "J'ai vu une brebis qui te faisait de l'oeil, Logan !":
            call attaque_massacre_einar_sauf_foret_2 pass (message = "chambre_logan") from _call_attaque_massacre_einar_sauf_foret_2_3

label attaque_massacre_einar_sauf_foret_2(message = ""):

    if message == "attentif":
        hide logan with dissolve
        e "Nous sommes en terre hostile. N'importe qui pourrait nous suivre sans que nous ne nous en rendions compte... Vous avez entendu, vous autres ? Faites moins de bruit !"
        show gv debout_enthousiastes_mid at center with dissolve
        gv "S'il n'y a rien de pire que des paysans, je ne redoute pas d'être suivi !"

        e "Tu fanfaronneras moins avec une fourche en travers du gosier, Alvin !"

    elif message == "deception":

        show einar debout_contrarie_mid at left
        e "Je suis de plus en plus déçu par la mission que nous a confié Harald. Marcher, marcher, marcher... Et quand nous rencontrons enfin une opposition, ce ne sont que des paysans."

        l "Les autres ne semblent pas apprécier le voyage non plus..."
        show gv debout_contraries_mid at halfsize, center with dissolve
        gv "Le pain de voyage va me rendre fou. Et je ne supporte plus de voir le cul du cheval de Garm devant moi !"

        e "..."

    elif message == "attitude":
        e "Ces villageois avaient l'air étranges..."

        l "Etranges ?"

        e "Oui, louches."

        menu :
            "Je redoute un piège":
                jump menu_avertissement_villageois

            "Ils ont dû être effrayés":
                e "La vue de douze guerriers à dû les effrayer. Ils n'avaient probablement jamais vu autant d'armes à la fois !"
                l "Ils ont dû croire que nous étions là pour raser leur village. Ils sont forcément au courant du meurtre de Montgomery, ils auront fait le rapprochement en nous voyant arriver."
                e "A juste titre ! Je regrette presque de ne pas les avoir massa..."

            "C'était une bande d'abrutis !":
                l "Ils étaient effrayés, c'est évident."
                e "Ils ont dû être impressionnés par notre présence. C'était une bande d'abrutis congénitaux, ils n'avaient jamais vu d'hommes armés !"
                e "Isolés qu'ils sont dans leur village d'arriérés, à élever leurs chiards et leurs mout..."

        menu menu_avertissement_villageois:
            "Ne relâchez pas votre attention":
                call attaque_massacre_einar_sauf_foret_2 pass (message = "attentif") from _call_attaque_massacre_einar_sauf_foret_2_4
            "Nous ne craignons pas les paysans !":
                hide logan with dissolve
                e "J'ai bien l'impression que les villageois tramaient quelque chose contre nous. Qu'ils viennent ! Avec leurs fourches et leurs pelles ! Ils verront nos haches de près ! Ha ha !"
                show gv debout_normaux_mid at center with dissolve
                gv "J'espère qu'ils nous attaqueront ! Un peu d'animation ne sera pas de trop !"
                gv "Un vieux m'a regardé de travers, j'espère pouvoir lui arracher la tro..."


    else:
        show einar debout_souriant_mid at left with dissolve
        e "D'ailleurs, en parlant de se ramollir... Tu aurais dû emmener une brebis du village, Logan ! J'en ai vu une qui te faisait de l'oeil !"
        show gv debout_rire_mid at halfsize, center with dissolve
        gv "Ha ha !"
        l "..."
        e "Ne sois pas si déçu ! La prochaine fois que nous voyons un bélier, je te l'offre ! Je sais que tu les aime beaux et vigoureux !"
        gv "Ha ha ha !"
        l "Ferme la Ein..."
    hide einar
    hide logan
    hide gv
    with dissolve

    #Remplacer pas simple horn
    play sound war_horn
    "Un cor retentit dans les bois, très proche."

    show einar debout_determine_mid at left with dissolve
    e "En position de combat, tous !"
    show gv debout_determines_mid at halfsize, center with dissolve
    gv "Ça venait d'où ?"
    show logan debout_determine_mid at right with dissolve
    l "Sur la gauche ! Des torches !"

    "Une volée de flèches siffle en sortant des frondaisons et frappe la plupart des guerriers vikings."
    "Des dizaines de silouhettes jaillissent de l'obscurité et se jettent sur les guerriers encore debout."
    show einar combat_determine at left
    e "Regroupez-vous ! Dos-à-dos ! Dressez les boucliers !"
    hide gv with dissolve
    show ogma combat_determine at halfsize, center with dissolve
    "Un meneur semble émerger du groupe des assaillants."
    "Les vikings se font massacrer et ne répondent plus aux ordres d'Einar."
    hide ogma
    hide logan
    with dissolve
    show re combat_furieux at halfsize, right with dissolve
    ge "Mourrez, chiens ! Mourrez comme votre lâche d'intendant !"

    e "Approchez, charognes ! Je..."

    "Une flèche frappe Einar de plein fouet à l'épaule, le désarmant."
    hide re with dissolve
    show logan combat_normal at right zorder 2 with dissolve
    l "Einar ! Derrière toi !"

    e "Que..."

    "L'un des assaillants arrive derrière Einar et lui transperce la cuisse avec un épieu, le faisant tomber au sol."
    show einar combat_blesse at left with dissolve
    e "Aaarrggh ! Logan, aide-moi !"

    l "Je suis là !"

    "Logan est frappé derrière la tête et tombe au sol, face à Einar."
    show ogma combat_normal at right zorder 1 with dissolve
    hide logan with dissolve
    "Le meneur des assaillants se baisse et égorge Logan devant Einar, qui est au bord de l'évanouissement."

    e "Crevure... Tu..."

    "Le meneur fixe Einar."
    show re combat_normaux at halfsize, center with dissolve
    ge "Les chiens du roi-empereur ont échoué."
    hide re with dissolve

    menu:
        "Qui es-tu ?":
            jump e_demande_nom_foret_2
        "Non ! Ne me tue pas, pitié !":
            jump e_implore_pitie_foret_2
        "Vous mourrez tous !":
            jump e_menace_foret_2

#Fin alternative n°1
label massacre_foret_2(lieu = ""):

    play ambiance wood

    show bg forest with dissolve

    if lieu == "chateau":

        "Sur le chemin du retour..."
        show gv debout_contraries_mid at center with dissolve
        gv "Pourquoi sommes-nous déjà sur le retour ?"
        show einar debout_normal_mid at left with dissolve
        e "Parce que nous avons massacré les rebelles. Mission accomplie, nous rentrons chez nous."
        hide gv with dissolve
        show logan debout_contrarie_mid at right with dissolve
        l "Tu penses avoir trouvé le village des rebelles ? Si facilement ?"
        show einar debout_souriant_mid at left
        e "Bien sûr ! Leur manque de coopération était plus qu'évident. Ils étaient les rebelles. Harald sera satisfait !"

    else:
        "En poursuivant vers le nord..."
        show gv debout_contraries_mid at center with dissolve
        gv "Pourquoi devons-nous poursuivre vers le nord ? Nous ne venons pas de massacrer les rebelles ?"
        show einar debout_normal_mid at left with dissolve
        e "Si, probablement. Mais j'ai tout de même un doute. Autant s'assurer d'avoir fait ce qu'il fallait !"

        e "Une visite des villages plus au nord s'impose. Et nous reproduirons les mêmes actions si nous rencontrons la moindre résistance !"
        show gv debout_enthousiastes_mid at center
        gv "Voilà qui fait plaisir à entendre !"
        hide gv with dissolve

    show bg forest_night with dissolve

    play ambiance wood_night

    "..."
    show gv debout_enthousiastes_mid at halfsize, center with dissolve
    gv "... et à ce moment là Logan sort de la taverne en feu, une fille sous un bras et la tête du père sous l'autre ! Ha ha !"

    gv "La fille était tellement choquée qu'elle n'a rien dit pendant deux jours ! Cinq de nos gars lui sont passés dessus, elle n'a même pas réagit !"
    show gv debout_rire_mid at halfsize, center
    gv "Ha Ha Ha !"
    hide gv
    show einar debout_normal_close at left
    show logan debout_normal_close at right
    with dissolve
    e "Du favoritisme pour les écossais, Logan ? En temps ordinaires tu ne te serais pas privé de tuer quelques personnes et de profiter d'une jolie fille !"

    e "J'ai bien remarqué ton comportement à Perth. Tu n'as tué personne. Tu as à peine incendié une grange."

    l "J'ai eu pitié de ces gens. Ils me faisaient penser à Aberdeen."

    e "Je croyais que tu n'aurais aucun problème à tuer des écossais !"

    l "Des écossais rebelles, oui. Pas des innocents."

    e "Ne remet pas mes ordres en question. Tu te ramollis, mon vieux Logan."

    menu:
        "Ne relâchez pas votre attention":
            call attaque_massacre_foret_2 pass (message = "attentif") from _call_attaque_massacre_foret_2
        "La mission est décevante":
            call attaque_massacre_foret_2 pass (message = "deception") from _call_attaque_massacre_foret_2_1
        "Les villageois étaient pitoyables !":
            call attaque_massacre_foret_2 pass (message = "moquerie") from _call_attaque_massacre_foret_2_2
        "J'ai vu une brebis qui te faisait de l'oeil, Logan !":
            call attaque_massacre_foret_2 pass (message = "chambre_logan") from _call_attaque_massacre_foret_2_3

label attaque_massacre_foret_2(message = ""):

    hide einar
    hide logan
    hide gv
    with dissolve

    if message == "attentif":
        show einar debout_normal_mid at left with dissolve
        e "Nous sommes en terre hostile. N'importe qui pourrait nous suivre sans que nous ne nous en rendions compte... Vous avez entendu, vous autres ? Faites moins de bruit !"
        show gv debout_enthousiastes_mid at center with dissolve
        gv "Nous avons massacré le village ! Qui pourrait nous attaquer ?"

        e "Et les hommes, abruti ? Il n'y en avait presque aucun à Perth."

        gv "Les hommes ? Il n'y a que des fermiers, dans le coin !"

        e "Tu fanfaronneras moins avec une fourche en travers du gosier, Alvin !"

    elif message == "deception":
        show einar debout_contrarie_mid at left with dissolve
        e "Je suis de plus en plus déçu par la mission que nous a confié Harald. Marcher, marcher, marcher... Et quand nous rencontrons enfin une opposition, ce ne sont que des paysans."
        show logan debout_normal_mid at right with dissolve
        l "Les autres ne semblent pas apprécier le voyage non plus..."
        show gv debout_contraries_mid at center with dissolve
        hide logan with dissolve
        gv "Le pain de voyage va me rendre fou. Et je ne supporte plus de voir le cul du cheval de Garm devant moi !"
        show einar debout_normal_mid at left
        e "Au moins, Perth nous aura fournit une petite distraction !"

        gv "J'aurais préféré des cibles qui se défendent..."

    elif message == "moquerie":
        show gv debout_rire_mid at center with dissolve
        gv "Hé, regardez ! J'ai une dent incrustée dans mon bouclier !"
        show einar debout_souriant_mid at left with dissolve
        e "Ne la retire pas, ça porte bonheur, ha ha !"

        gv "Ils étaient tellement faibles ! Je me souviendrai de Perth comme..."
        show einar debout_normal_mid at left
        e "On ne se souviendra de rien, Garm ! Ce serait faire trop d'honneur à un village d'abrutis consanguins perdu au bout du mon..."


    else:
        show einar debout_souriant_mid at left with dissolve
        e "D'ailleurs, en parlant de se ramollir... Tu aurais dû emmener une brebis du village, Logan ! J'en ai vu une qui te faisait de l'oeil !"
        show gv debout_rire_mid at center with dissolve
        gv "Ha ha !"
        show logan debout_contrarie_mid at right with dissolve
        l "..."
        e "Ne sois pas si déçu ! La prochaine fois que nous voyons un bélier, je te l'offre ! Je sais que tu les aime beaux et vigoureux !"
        gv "Ha ha ha !"
        l "Ferme-la Ein..."

    hide einar
    hide logan
    hide gv
    with dissolve

    play sound war_horn
    "Un cor retentit dans les bois, très proche."

    show einar debout_determine_mid at left with dissolve
    e "En position de combat, tous !"
    show gv debout_determines_mid at halfsize, center with dissolve
    gv "Ça venait d'où ?"
    show logan debout_determine_mid at right with dissolve
    l "Sur la gauche ! Des torches !"

    "Une volée de flèches siffle en sortant des frondaisons et frappe la plupart des guerriers vikings."
    "Des dizaines de silouhettes jaillissent de l'obscurité et se jettent sur les guerriers encore debout."
    show einar combat_determine_mid at left with dissolve
    e "Regroupez-vous ! Dos-à-dos ! Dressez les boucliers !"
    hide gv with dissolve
    show ogma combat_determine_mid at halfsize, center with dissolve
    "Un meneur semble émerger du groupe des assaillants."
    "Les vikings se font massacrer et ne répondent plus aux ordres d'Einar."
    hide ogma
    hide logan
    with dissolve
    show re combat_furieux_mid at halfsize, right with dissolve
    ge "Mourrez, chiens ! Mourrez comme votre lâche d'intendant !"

    e "Approchez, charognes ! Je..."

    "Une flèche frappe Einar de plein fouet à l'épaule, le désarmant."
    hide re with dissolve
    show logan combat_normal_mid at right zorder 2 with dissolve
    l "Einar ! Derrière toi !"

    e "Que..."

    "L'un des assaillants arrive derrière Einar et lui transperce la cuisse avec un épieu, le faisant tomber au sol."
    show einar combat_blesse_mid at left with dissolve
    e "Aaarrggh ! Logan, aide-moi !"

    l "Je suis là !"

    "Logan est frappé derrière la tête et tombe au sol, face à Einar."
    show ogma combat_normal_mid at right zorder 1 with dissolve
    hide logan with dissolve
    "Le meneur des assaillants se baisse et égorge Logan devant Einar, qui est au bord de l'évanouissement."

    e "Crevure... Tu..."

    "Le meneur fixe Einar."
    show re combat_normaux_mid at halfsize, center with dissolve
    ge "Les chiens du roi-empereur ont échoué."
    hide re with dissolve

    menu:
        "Qui es-tu ?":
            call e_demande_nom_foret_2 pass (bad_ending = True) from _call_e_demande_nom_foret_2
            #jump e_demande_nom_foret_2 pass (bad_ending = True)
        "Non ne me tue pas, pitié!":
            call e_implore_pitie_foret_2 pass (bad_ending = True) from _call_e_implore_pitie_foret_2
        "Vous mourrez tous !":
            call e_menace_foret_2 pass (bad_ending = True) from _call_e_menace_foret_2

label e_demande_nom_foret_2(bad_ending = False):
    hide einar
    hide logan
    hide gv
    hide ogma
    show einar debout_blesse_mid at left with dissolve
    show ogma debout_normal_mid at right with dissolve
    e "Qui es-tu, lâche ?"

    if bad_ending:
        show ogma debout_contrarie_mid at right
        ge "..."
        hide einar with dissolve
        jump bad_ending_1
    else:
        o "Ogma. Le Hurleur."
        "Einar reçoit un violent coup au crâne et sombre dans les ténèbres, inconscient."
        hide einar with dissolve
        jump e_reveil_village_2

label e_implore_pitie_foret_2(bad_ending = False):
    hide einar
    hide logan
    hide gv
    hide ogma
    show einar debout_normal_mid at left with dissolve
    show re debout_normaux_mid at right with dissolve
    show ogma debout_normal_mid at center with dissolve
    e "Par pitié, ne me tue pas ! Dites-moi quoi faire, et je le ferai !"

    if bad_ending:
        ge "Lâche jusqu'au bout..."
        hide einar with dissolve
        jump bad_ending_1
    else:
        ge "Nous allons voir ça..."
        "Einar reçoit un violent coup au crâne et sombre dans les ténèbres, inconscient."
        hide einar with dissolve
        jump e_reveil_village_2

label e_menace_foret_2(bad_ending = False):
    hide einar
    hide logan
    hide gv
    hide ogma
    show einar debout_normal_mid at left with dissolve
    show re debout_normaux_mid at right with dissolve
    e "Tuez-moi ! Le roi brûlera toute la Grande-Bretagne pour votre insolence !"

    if bad_ending:
        ge "Je ne crains pas ton roi."
        hide einar with dissolve
        jump bad_ending_1
    else:
        ge "Je ne crains pas ton roi."
        "Einar reçoit un violent coup au crâne et sombre dans les ténèbres, inconscient."
        hide einar with dissolve
        jump e_reveil_village_2


#Sequence 8
label e_reveil_village_2:

    play ambiance village
    #play ambiance home

    scene bg house with dissolve

    $ already_talk = False

    show einar debout_blesse_mid at left with dissolve
    e "Huugh..."
    show re debout_normaux_mid at halfsize, center with dissolve
    ge "Ogma ! Il se réveille !"
    show ogma debout_souriant_mid at right with dissolve
    o "Ah ! La belle endormie. "
    hide re with dissolve
    e "Arrgh... Mon épaule..."

    o "La tête de la flèche est toujours à sa place."
    show einar debout_furieux_mid at left
    e "Enfoiré ! Vous les avez tous tués !"

    o "..."

    e "Qui... Aarrgh... êtes vous ?"

    o "Nous sommes ceux que toi et les tiens cherchiez. Toutes mes félicitations, vous nous avez trouvé."
    show einar debout_blesse_mid at left
    e "Les rebelles ?"

    o "..."
    show einar debout_furieux_mid at left
    e "Où sont les autres ? Où sont mes compagnons ?"

    e "Ordure ! Je me rappelle ! C'est toi qui a tué Logan !"
    show ogma debout_contrarie_mid at right
    o "C'était un traître."

    e "C'est lui qui m'a retenu de massacrer Perth ! C'est lui qui a sauvé la vie de vos vieux et de vos truies de femmes !"
    show ogma debout_attriste_mid at right
    o "Alors j'imagine que sa mort est regrettable."
    show ogma debout_normal_mid at right
    show einar debout_blesse_mid at left

    menu reveil_einar_village_2:
        "Pourquoi m'avoir laissé en vie ?":

            e "Pourquoi m'avoir épargné ? Pourquoi moi et pas les autres ?"

            o "J'ai donné l'ordre de t'épargner parce que tu étais le seul dont nous avions besoin."

            jump o_explication_vie_village_2

        "Il y a un rapport avec Perth ?":

            e "Est-ce qu'il y a un rapport avec le village d'hier ?"

            o "Perth. Et la réponse est oui. Nos éclaireurs avaient vu votre groupe et nous l'avaient signalé."

            o "Nous avons quitté le village peu avant votre arrivée, et nous avons observé la scène, avec la ferme intention de vous tendre une embuscade ensuite."

            o "Ce que, comme tu as pu le voir, nous avons fait."

            jump o_explication_vie_village_2
        "Crevure !" if already_talk == False:

            e "Salopards ! J'aurais du enfermer vos truies de femmes et leurs gamins dans vos cahutes merdeuses avant d'y foutre le feu !"

            "Ogma frappe Einar sur son épaule blessée"

            e "AAARGH !"

            o "Les insultes et les menaces n'ont que peu de poids venant de la part d'un soldat blessé, attaché et seul."

            o "Tu ferais mieux de contenir ta colère. J'ai décidé de t'épargner. Rien ne m'empêche de changer d'avis."

            e "Tu me demandes d'être reconnaissant, pourriture ?!"

            o "Oui. Tu me dois la vie."

            $ already_talk = True

            jump reveil_einar_village_2

label o_explication_vie_village_2:

    $ already_talk = False
    $ choix_ogma_1 = ""

    o "Tu n'es vivant que pour deux raisons."
    o "D'abord, tu t'es montré clément envers les miens. En tant que meneur, cette décision n'appartenait qu'à toi. Je te remercie."
    o "Ensuite, je sais que tu es proche de Harald. Ta tenue, la façon dont tu parlais à tes hommes : tu es un huscarl."
    e "Vous m'avez épargné pour m'utiliser contre mon roi ?"
    o "Oui."

    menu :
        "Quel est ton but ?":
            $ choix_ogma_1 = "incomprehension"
        "Ne rien dire":
            $ choix_ogma_1 = "silcence"
        "Vous n'obtiendrez rien de moi !":
            $ choix_ogma_1 = "insulter"


    if choix_ogma_1 == "incomprehension":

        e "Vous allez devoir m'en dire plus."

    elif choix_ogma_1 == "insulter":
        show einar debout_furieux_mid at left with dissolve
        e "Vous allez être déçus ! Vous n'obtiendrez rien de moi, charognes ! Vous ne me ferez pas trahir mon allégeance !"

        o "Calme toi. Les termes de mon offre suffiront à te faire changer d'avis, j'en suis sûr."
    else:
        "..."
    show einar debout_normal_mid at left
    o "Je ne veux que peu de choses. En échange de la trahison du roi, je t'offre le droit de survivre, de reprendre ta liberté et de partir avec ce que tu pourras porter d'or."
    e "Ma vie et de l'or contre la trahison du souverain le plus puissant ayant jamais existé ?"
    o "Exactement."
    o "Une fois que je t'aurai relâché, tu retourneras au château de Dunbar. Au signal que je te donnerai, tu abaisseras le pont-levis."
    e "C'est tout ? Harald ne me laissera jamais faire !"
    o "Peu importe la méthode. Tout ce que je demande, c'est que la porte soit ouverte quand mes troupes arriveront au château pour le roi."
    e "Les troupes ? Vos vingt fermiers ? Et que comptez-vous faire, une fois à l'intérieur ? Tuer le roi ? Ha ha ! Il pourrait vous affronter à lui tout seul !"
    o "Je ne veux pas le tuer. Pas nécessairement. Je veux uniquement l'obliger à quitter l'Ecosse. Je veux montrer au reste du monde que l'élu divin peut reculer face à des hommes déterminés."
    e "Et en admettant que j'accepte votre offre, quelles sont mes garanties de survie ensuite ? Le roi me fera chercher sur tout les continents."
    o "Tu pourras rester en Ecosse ou aller où tu veux. Ce n'est pas mon problème."
    o "Alors, quelle est ta décision ?"

    menu menu_choix_trahison_village_2:
        "J'accepte":
            jump accepter_trahir_village_2
        "Vous me faites confiance ?" if already_talk == False:

            e "Qui vous dit que je tiendrai parole une fois remis en liberté ?"
            o "... Je compte sur ta gratitude."
            e "Vous vous moquez de moi ?"
            o "Tu vas passer un certain temps ici. Nous allons te nourrir et te soigner, et tu verras que nous ne méritons pas le sort que nous réserve le roi."
            o "Alors ?"

            $ already_talk = True

            jump menu_choix_trahison_village_2
        "Jamais !":
            jump refuser_trahir_village_2

label refuser_trahir_village_2:
    show einar debout_furieux_mid at left
    e "Allez vous faire foutre. Je ne trahirai pas la parole que j'ai donné à mon roi."

    o "Mauvaise réponse."

    "Ogma enfonce deux doigts dans la plaie de l'épaule d'Einar, pressant la pointe de flèche."
    show einar debout_blesse_mid at left
    e "AAAAARRRGH !"
    show ogma debout_souriant_mid at right
    o "Tiens, on dirait que la pointe est coincée dans une articulation !"

    e "AAAHH ! STOP !"

    o "Jouer les fortes têtes ne te servira à rien ici. Tout ça est bien plus éprouvant pour toi que pour moi."

    e "ARRÊTEZ ! ARRÊTAAAARGH !"
    show ogma debout_normal_mid at right
    "Ogma retire ses doigts de la plaie."

    o "Tu as changé d'avis sur la question ?"

    menu:
        "J'accepte":
            e "Très bien... Hhhggh... J'accepte..."
            show ogma debout_souriant_mid at right
            o "Parfait !"
            jump accepter_trahir_village_2
        "Je ne trahirai personne !":
            jump bad_ending_2


label accepter_trahir_village_2:

    e "Très bien... Je vais faire ce que vous me demandez."
    show ogma debout_normal_mid at right
    o "Tu as fait le bon choix."
    e "Quand dois-je partir ?"
    show ogma debout_souriant_mid at right
    o "Ha ha ! Pas d'enthousiasme excessif ! Si je te laissais partir maintenant, tu mourrais aussitôt ! Nous allons soigner tes blessures."
    o "Je vais te laisser. Nous nous retrouverons bientôt."

    jump interieur_maison_village_1
