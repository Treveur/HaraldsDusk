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

    scene bg forest with dissolve

    play sound "sounds/sfx/SFX_WarHorn.mp3"

    "Dans la forêt de Westruther, au coeur de l'Ecosse, une troupe de vikings se dirige vers le chateau de Dunbar pour s'y installer et préparer l'expédition punitive visant à mater les rebelles."
    show harald debout_normal at center with dissolve
    "A la tête de la cohorte, Harald, roi-empereur des vikings. Il a décidé de venir punir lui-même les insolents ayant osé défier son pouvoir."
    "A ses côtés marche une armée de cent vikings, guerriers et huscarls, impatients d'en découdre : cela fait déjà longtemps qu'ils ne se sont pas battus."
    show logan debout_normal at right with dissolve
    "A l'avant du contingent un guerrier écossais éclaire la voie ; Logan a juré fidélité à Harald depuis longtemps et le mène jusqu'au château de Dunbar."
    show einar debout_normal at left with dissolve
    "Einar est l'un des huscarls : un guerrier d'élite, chef militaire et garde personnel du roi."

    menu:
        "Parler à Harald":
            hide logan debout_normal

            e "Mon Roi, sommes-nous proches ?"

            show einar debout_normal at left
            show harald debout_normal at right

            h "Nous n'en avons plus pour très longtemps. Une heure, tout au plus."

            menu menu_harald_choice_foret:
                "Quel est le plan ?" if plan_choice:

                    e "Quelles sont les instructions, sire ? A quoi devons-nous nous préparer ?"

                    h "Tout d'abord, nous allons atteindre le château de Dunbar. Là, l'évêque Patrick d'Edimbourg nous accueillera."

                    h "Ensuite, je détacherai un groupe d'éclaireurs. Je veux retrouver le village des rebelles le plus vite possible."

                    h "Après, j'aviserai. Mais ces foutus écossais n'apprécieront pas ce qui va leur arriver, tu peux me croire !"

                    $ plan_choice = False

                    jump menu_harald_choice_foret

                "Parler de la région" if region_choice:

                    e "Qu'indiquent les cartes à propos de la région, sire ? Je n'ai pas eu le loisir de les consulter."

                    h "Pas grand chose. Des plaines d'herbe rase, des rocailles abruptes, quelques forêts. Et surtout, la mer."

                    h "Nous ne sommes encore que dans les Lowlands ; les Highlands sont plus au nord."

                    h "Et hormis le nom, je dois dire que je ne vois que peu de différences entre ces deux territoires. "

                    e "La région a l'air inhospitalière..."

                    $ region_choice = False

                    jump menu_harald_choice_foret

                "Se montrer enthousiaste" if enthousiaste_choice:

                    e "Sire, il me tarde de massacrer quelques paysans !"

                    h "Ha ha ! Ne sois pas si hatif, il ne s'agit pas de tuer tout ce qui bouge. Pas pour le moment ! "

                    e "Sauf votre respect, Sire, votre Hache nous a privé de nombreuses batailles. D'habitude, vos ennemis se rendent dès qu'ils la voient !"

                    e "Un soulèvement paysan, c'est une chance inespérée !"

                    h "Ton enthousiasme fait plaisir à voir !"

                    $ enthousiaste_choice = False

                    jump menu_harald_choice_foret

                "Pourquoi tant de confiance ?" if confiance_choice:

                    e "Sire, votre présence ici m'intrigue... Pourquoi risquer votre vie dans une expedition de moindre importance ? Vous pourriez recevoir une flèche !"

                    h "Je suis l'élu divin, je porte une relique du Christ !"

                    h "La Hache me rend immortel. Une flèche me ferait rire, rien de plus."

                    h "Harald Sigurdsson, roi-empereur des vikings, abattu par une flèche de paysan rebelle ! Ha ha !"

                    e "Ha ! Les dirigeants du monde entier craindraient les écossais !"

                    $ confiance_choice = False

                    jump menu_harald_choice_foret

                "Continuer silencieusement":
                    e "..."

        "Parler à Logan":
            e "Ça va, Logan ? Tu n'as pas desserré les dents depuis Newcastle. "

            show einar debout_normal at left
            show logan debout_normal at right

            l "... Je n'ai pas revu l'Ecosse depuis plus de dix ans."

            e "Depuis tout ce temps passé en campagne, j'en avais oublié tes racines."

            l "Je me demande si Aberdeen a beaucoup changé."

            e "La nostalgie de la maison, hein ? Si tu veux, je peux peut-être glisser un mot au roi pour..."

            l "Non, merci. Je ne tiens pas à y retourner."

            menu menu_logan_choice_foret:
                "Se remémorer un bon souvenir" if plan_choice:

                    e "Tu te souviens de la bataille de Wertheim ?"

                    l "L'automne dernier ? Et comment ! Je revois encore les seins de la petite que j'avais attrapé ! J'ai passé une bonne nuit cette fois là !"

                    l "Je ne me rappelle même pas de son nom. Dorthe, Dorothe, quelque chose comme ça. Le lendemain, sur le départ, elle a insisté pour que je l'emmène ! La garce ! Ha ha ! "

                    e "Tu as toujours de la chance quand il s'agit de dégoter de belles filles. Même au milieu de nul part !"

                    l "Remarque, ça fait un moment que je ne t'ai pas vu avec une fille. Pas une captive, rien ! Monsieur cherche le grand amour ? A moins qu'il ne soit plus du genre à embrasser les garçons ?"

                    e "Ferme la, sale porc. Quand je passe du bon temps, j'aime que la fille ne sois pas entrain de se débattre."

                    l "Chacun son truc !"

                    $ plan_choice = False

                    jump menu_logan_choice_foret

                "Parler de la région" if region_choice:

                    e "Tu reconnais la région ?"

                    l "Pas vraiment. Aberdeen est bien plus loin au nord, je ne suis jamais venu jusqu'ici."

                    l "Cela dit, je ne suis pas dépaysé..."

                    $ region_choice = False

                    jump menu_logan_choice_foret

                "Se montrer enthousiaste" if enthousiaste_choice:

                    e "Ma hache me démange. Je fracasserais bien quelques crânes !"

                    l "Moi aussi ! Je ne supporte plus ces voyages interminables. Deux mois que nous n'avons pas combattu ! Et plus d'un an depuis la dernière vraie bataille. Il est grand temps de nous dégourdir un peu !"

                    e "Tuer des écossais ne te posera pas de problème ?"

                    l "Je n'aurai pas plus de problèmes que toi. Ces gens ont tué l'un des vassaux du roi. C'est une motivation amplement suffisante pour trancher la tête de quelques compatriotes."

                    $ enthousiaste_choice = False

                    jump menu_logan_choice_foret

                "Pourquoi Harald est-il si confiant ?" if confiance_choice:

                    e "Le roi me paraît bien confiant."

                    l "Il a toutes les raisons de l'être !"

                    l "Il est le plus grand souverain que le monde connaisse. Il porte une hache incrustée des Clous de la Sainte Croix."

                    l "Il est immortel, invincible, et une armée de vétérans marche avec lui."

                    l "S'il y a bien une personne sur cette terre qui peut avoir confiance en lui-même, c'est notre roi !"

                    $ confiance_choice = False

                    jump menu_logan_choice_foret

                "Continuer silencieusement":
                    e "..."

        "Ne rien dire":
            e "..."

    gv "Sire ! Un rapport des éclaireurs !"
    h "Donne-moi ça..."
    "*Harald lit rapidement le rapport.*"

    hide einar debout_normal
    hide logan fache
    hide harald debout_normal

    jump plaine_1

#Sequence 2
label plaine_1 :

    scene bg mer with dissolve

    "*Une heure plus tard.*"

    show harald debout_normal at right with dissolve

    h "Ha ! Dunbar, enfin. Un bon repas nous attend."

    show einar debout_normal at left with dissolve

    e "Dois-je envoyer un émissaire annoncer notre arrivée ?"

    h "Non, je compte sur toi pour autre chose."

    e "Autre chose ?"

    h "Nos éclaireurs ont repéré des mouvements au nord."

    e "Les rebelles ?"

    h "Je ne suis sûr de rien. J'ai besoin d'envoyer un groupe de reconnaissance à l'avant de l'armée, afin de tirer cette affaire au clair."

    h "Je compte sur toi pour diriger la troupe. Les hommes t'écouteront et ton expérience du pistage vous facilitera la tâche."

    menu menu_harald_eclaireur_foret_1:

        "J'accepte":

            e "Bien, sire. Où les éclaireurs ont-ils repéré ces mouvements ?"

            h "Les rapports manquent de détails, mais Logan m'a parlé de plusieurs petits villages qui pourraient abriter la rébellion."

        "Pourquoi moi ?":

            e "Pourquoi dois-je mener ce groupe de reconnaissance ?"

            h "Parce que je te le demande. Comme je te l'ai dit, je suis convaincu que tes qualités te permettront de mener à bien cette mission mieux que quiconque."

            h "Cette reconnaissance est très importante : elle me permettra de cibler précisément le village à châtier. Nous gagnerons un temps précieux et nous épargnerons les villages n'ayant aucun rapport avec cette rébellion."

            jump menu_harald_eclaireur_foret_1

        "A quels dangers dois-je m'attendre ?":

            e "Sire, quels sont les dangers de cette mission ? A quoi dois-je m'attendre ?"

            h "Il n'y a aucun danger. Dans le pire des cas, tu pourrais te faire insulter par une bande de villageois chétifs. Tu mènes un groupe de guerriers vikings. Tu es un huscarl. Rien ne va te résister."

            jump menu_harald_eclaireur_foret_1




    show logan debout_normal at center
    l "Je vais t'accompagner, Einar."

    menu:
        "Merci Logan !":

            e "Merci beaucoup Logan. Je suis heureux de pouvoir compter sur toi !"

            l "J'aurais préféré manger à la table du roi ce soir, mais j'avais peur que tu te perdes en forêt !"

            h "Ne vous inquiétez pas. Vous aurez tout les deux de quoi boire et manger une fois revenus !"

            h "Partez dès maintenant, il n'y a pas de temps à perdre. Vous atteindrez Stirling avant la nuit."

            h "Vous atteindrez les villages signalés par les éclaireurs d'ici demain."


        "Je regrette, mais non.":

            e "Non, je refuse. Je n'ai pas besoin de toi, Logan. C'est une mission de reconnaissance : moins nous sommes, mieux c'est."

            l "..."

            h "J'ai personnellement demandé à Logan de t'accompagner. Il est le seul à connaître la région, et il facilitera les relations avec les écossais."

            h "Partez dès maintenant, il n'y a pas de temps à perdre. Vous atteindrez Stirling avant la nuit."

            h "Vous atteindrez les villages signalés par les éclaireurs d'ici demain."

    hide logan debout_normal
    hide einar debout_normal
    hide harald debout_normal

    jump plaine_2

#Sequence 3
label plaine_2:

    scene bg cote1 with dissolve

    "*Le lendemain...*"

    show gv debout_normaux at center with dissolve

    gv "Cette mission n'a rien de terrible... Je suis déçu."
    gv "Nous aurions dû rester plus longtemps à Stirling. Il y avait une bien belle tavernière qui semblait prête à me sauter sur les genoux !"

    show einar debout_normal at left with dissolve

    menu:
        "Motiver les troupes" :

            e "Et je suis convaincu que nous ne rencontrerons rien de plus excitant qu'une tavernière au milieu de toute cette foutue caillasse !"

            e "Ha ! Se défouler sur des villageois, ce sera notre récompense !"

            e "Plus vite le problème sera réglé, plus vite nous pourrons glisser nos pieds sous la table et nous remplir la panse !"

            gv "Ha ha ! Bien parlé !"

        "Mettre en garde" :

                e "Méfiez vous, le roi n'est pas avec nous."

                e "Sans la Hache, nous sommes à la merci de n'importe quel piège. Restez aux aguets !"

                e "Rien qu'en t'écoutant, je suis sûr que les rebelles connaissent déjà ton nom, celui de tes parents et la taille de ta queue, Alvin."

                gv "Vous avez entendu, les gars ? Ouvrez l'oeil."

        "C'est une mission sans intérêt" :

                e "Je suis bien d'accord..."
                e "Et je suis certain que nous ne rencontrerons rien de pire que des landes et des forêts. Pourquoi nous envoyer battre la campagne à la recherche d'une bande de péquenauds ?"

                hide gv debout_normaux with dissolve

                show logan debout_normal at right with dissolve

                l "Tu le prends comme une punition ?"

                e "Oui ! J'estime qu'après tout ce temps à servir Harald, il aurait pu choisir quelqu'un d'autre pour accomplir ce genre de mission."

                e "Je n'en suis plus à mon coup d'essai, bordel !"

        "Chambrer Logan" :

            e "Tu ne parles pas beaucoup, Logan... Tu as un problème, ou bien tu attends une autorisation du roi pour l'ouvrir ?"

            hide gv debout_normaux with dissolve

            show logan debout_normal at right with dissolve

            l "..."

            e "Ha, il est obéissant en plus ! Tu attends aussi des autorisations royales pour baiser ? Notre bon Harald doit te la tenir ?"

            l "..."

            gv "Ha ha ha !"

        "Silence ! Je veux deux groupes à l'avant..." :

            hide gv debout_normaux with dissolve

            e "Taisez-vous. Je veux deux groupes à l'avant, deux groupes à l'arrière. Au centre, Logan et moi. Et magnez-vous le train !"

            show logan debout_normal at right with dissolve

            l "Les gars sont aussi fatigués que nous. Tu devrais..."

            e "Toi aussi, tais-toi. Je veux que nous menions cette mission de la façon la plus exemplaire possible."

            l "Bien."

    hide einar debout_normal
    hide logan debout_normal

    jump foret_1

#Scequence 4
label foret_1:

    scene bg forest with dissolve

    "*Un jour plus tard...*"

    show einar debout_normal at left with dissolve

    e "Une forêt. Encore..."

    menu:
        "Impatient de rentrer en Norvège":

            e "Plus le temps passe, plus la Norvège me manque..."

            e "Je ne sais même plus depuis combien de temps je n'y ai pas foutu les pieds."

            gv "J'aimerais retrouver la Suède. Je n'ai aucunes nouvelles de ma famille depuis notre campagne d'Egypte."

            gv "Je n'ai pas de nouvelles non plus. Mon vieux père pourrait bien être mort sans que je n'en sache rien !"
            show logan debout_normal at right with dissolve
            l "Harald doit ressentir la même chose. Il n'a pas vu sa femme ni ses enfants depuis aussi longtemps que nous."
            show gv debout_normaux at center with dissolve
            gv "Qu'est-ce que tu en sais, Logan ? C'est nous ta seule famille !"

            l "..."
            hide gv debout_normaux with dissolve

            menu:
                "J'ai hâte de recevoir les récompens qui m'ont été promises":

                    e "Ça fait des années que le roi me fait miroiter des récompenses sans jamais me les offrir..."

                    e "Depuis le temps qu'il me promet des terres, je devrais déjà vivre comme un prince !"

                    show logan debout_normal at right with dissolve

                    l "Et si ces terres ne sont pas en Norvège ?"

                    e "Peu importe. Tout ce que je veux, c'est enfin pouvoir me sentir chez moi."

                "Assez de niaiseries pour aujourd'hui":

                    e "Taisez-vous maintenant. La route est encore longue et j'en ai déjà assez d'écouter vos histoires de bonnefemmes."

                    e "Logan ? Où en sommes-nous ?"

                    show logan debout_normal at right with dissolve

                    l "Nous atteindrons Perth demain matin. C'est le premier village sur notre chemin."

                    l "D'après les rapports, les rebelles sont venus de cette région."

                    l "C'est un petit village sans défenses. Si nous ne trouvons rien, nous poursuivrons jusqu'à Dundee."

        "Se moquer des autochtones" :

            e "J'imagine la tête des sauvages qui vivent dans la région. C'est une bonne chose que les écossais aient intégré l'empire : ça les civilise un peu !"

            e "Je suis persuadé qu'ils vivent dans des cabanes délabrées et qu'ils couchent avec leurs chèvres !"
            show gv debout_normaux at center with dissolve
            gv "Ha ha !"

            show logan debout_normal at right with dissolve

            l "Non. Nous vivons dans des maisons de pierre."

            l "Et pour le reste, tu constateras que nous avons bien plus de raisons de coucher avec nos femmes qu'avec nos chèvres."

            hide gv debout_normaux with dissolve

        "Impatient de terminer la mission" :

            e "Je commence à être lassé de cette saloperie de randonnée."

            e "Une journée à crapahuter sans voir âme qui vive... "

            e "On trouve le village et on rentre au château. Et à bride abattue !"

        "Motiver les troupes" :

            e "Ne relâchez pas l'effort. D'ici une journée, nous nous serons suffisamment enfoncés dans les Highlands pour avoir une chance de trouver le village des rebelles."

        "Chambrer Logan" :

            e "Toujours pas envie de parler, Logan ? Trop occupé à rêver du corps d'une de ces magnifiques brebis écossaises ?"

            show logan debout_normal at right with dissolve

            l "..."
            show gv debout_normaux at center with dissolve
            gv "Ha ha !"
            hide gv debout_normaux with dissolve
        "Demander à Logan ce qu'il pense de la mission" :

            e "Tu es le seul à ne pas encore t'être plaint..."
            show logan debout_normal at right with dissolve
            l "Je ne vois pas de raisons de me plaindre. J'accomplis mon devoir. Le roi nous récompensera à notre retour."

            e "Il se fout de nous ! Depuis le temps qu'il me promet des terres..."

            menu:
                "Pourquoi as-tu décidé de m'accompagner ?":

                    e "Pourquoi avoir choisi de m'accompagner ? "

                    l "Même sans être natif du coin, je connais la région mieux qu'aucun d'entre vous."

                    l "Et ma présence facilitera les relations avec les autres écossais."

                    e "Ils ne risquent pas de mal le prendre, au contraire ?"

                    l "C'est une autre possibilité."

                "Je suis content que tu sois là":

                    e "Quoi qu'il en soit, merci d'avoir choisi de m'accompagner."

                    l "Si un jour une campagne m'amène en Norvège, je serai heureux de compter sur toi."

                "Tu aurais du rester au château":

                    e "Tu aurais du rester avec Harald !"

                    l "Pourquoi ?"

                    menu:
                        "Une vie de plus en danger":

                            e "C'est une mission de reconnaissance. Nous pourrions tomber dans une embuscade à tout moment !"

                            l "Ces gens ne sont que des paysans. Ils fuiraient rien qu'en nous entendant arriver."

                            e "Peut-être pas. Tu as mis ta vie en jeu sans raison. Et tu nous rends plus repérables. "

                            l "Plus repérables ? Vraiment ? Quelle différence entre onze et douze hommes ?"

                            e "..."

                        "Tu es inutile":

                            e "Nous étions déjà bien assez nombreux. Onze guerriers vikings dont un huscarl !"

                            l "Aucun d'entre vous ne connaît la région."

                            e "Je me fout de tes compétences ! Nous ne sommes pas là pour observer un panorama ou cueillir des champignons !"

                            e "Ces salopards d'écossais sont hostiles. Je n'envisage même pas un dialogue avec eux ! Nous n'avions pas besoin de toi."

    hide einar debout_normal
    hide logan debout_normal

    jump village_1

#Scequence 5
#Scene 1
label village_1:

    $ moira_met = False

    scene bg village with dissolve
    "*Peu après midi, la troupe parvient en vue d'un village...*"
    show logan debout_normal at right zorder 5 with dissolve
    l "Nous y sommes. Perth."

    "*Les villageois vaquent à leurs occupations. Certains d'entre eux ont remarqué l'arrivée des guerriers vikings et affichent une expression craintive.*"
    show einar debout_normal at left zorder 5 with dissolve
    e "Ça me semble bien calme."
    show gv debout_normaux at center with dissolve
    gv "On dirait qu'il n'y a pas grand monde..."

    e "Uniquement des vieillards, des femmes et des enfants."

    gv "Ça sent le traquenard..."

    hide gv debout_normaux with dissolve
    show gv debout_normaux at left zorder 1 with dissolve
    show ve debout_craintifs at right zorder 1 with dissolve

    menu menu_fouille_village:

        "Demander des infomations sur les rebelles":
            jump e_demander_information_village_1
        "Fouillez le village!":
            jump e_fouiller_village_1
        "Chercher soi-même dans le village":
            call e_fouiller_village_1 pass (einarFouille = True) from _call_e_fouiller_village_1
        "Massacrez-les !":
            jump e_massacre_village_1

label e_massacre_village_1:

    e "Massa..."

    l "Einar, non ! Nous ne sommes sûrs de rien !"

    l "Harald nous a envoyé en reconnaissance ! Nous ne sommes pas là pour tuer ces gens !"

    l "Nous risquons d'aggraver la situation en rasant Perth. Le roi sera furieux !"

    l "Et je ne parle même pas des écossais ! Nous ne pourrions pas revenir au château sans nous faire égorger sur le chemin !"

    menu:

        "Massacrez-les quand même":
            jump e_massacre_village_2
        "Se raviser":
            jump menu_fouille_village

label e_massacre_village_2:

    e "Je me fout de ton avis, Logan !"

    e "Massacrez-moi tout ça ! Et brûlez leurs cabanes !"

    gv "HAAAAA !"

    ve "Sauvez les enfants ! Les enfants !"

    call choix_retour_village_1 pass (massacre = True) from _call_choix_retour_village_1

label e_demander_information_village_1:

    e "Que savez-vous des rebelles ? Où sont-ils ?"

    l "Parle, vieil homme. Je suis écossais. Nous ne vous voulons aucun mal."

    ve "Ecossais ? Traître à ta terre et à ton sang ! Tu mènes des envahisseurs parmi les tiens ! *crache*"

    e "Quel succès, Logan."

    e "Qui traitez-vous d'envahisseurs ? Ces terres appartiennent au roi-empereur Harald Sigurdsson de Norvège, porteur de le Hache Sainte."

    e "Votre attitude ressemble à un aveu de trahison !"

    l "Calme-toi Einar. Comment réagirais-tu si tu voyais une armée byzantine débarquer en Norvège ?"

    e "..."

    menu:
        "Hausser le ton":
            jump e_intimider_villageois_village_1
        "Tuer un villageois pour les faire parler":
            jump e_tuer_villageois_village_1

label e_fouiller_village_1(einarFouille = False):


    $ moira_met = True
    $ already_talk = False

    if einarFouille:
        e "Bien. Je vais moi-même jeter un oeil. Mieux vaudrait pour vous que vous ne cachiez rien."

        e "Si qui que ce soit tente de s'enfuir ou se montre agressif, tuez-le."

        "*Einar entre dans une maison*"


    else:
        e "Fouillez moi ces taudis ! Si vous trouvez quoi que ce soit, ramenez-le moi !"

        gv "HAAAAA !"

        "..."

        gv "Einar ! Une fille, dans une maison !"

        e "Je suis à peine surpris... J'arrive !"

    scene bg house
    show moira debout_normal at center with dissolve
    show einar debout_normal at left with dissolve
    menu menu_maison_1:
        "Qui es-tu ?":
            jump e_nom_villageoise_maison_1
        "Pourquoi être cachée ?":
            jump e_cache_villageoise_maison_1
        "Où sont les rebelles ?":
            jump e_info_rebelle_maison_1
        #Si Einar à déjà parlé une fois à Moira
        "La laisser partir" if already_talk:
            jump e_villagoise_partir_maison_1
        "Tuer la villageoise" if already_talk:
            jump e_tuer_moira_maison_1
    hide moira with dissolve
    hide einar with dissolve


label e_tuer_villageois_village_1:
    show ve 

    e "Toi. Approche."

    ve "Moi ?"

    e "Oui ! Dépêche toi !"

    ve "Monseigneur, je ..."

    "*Einar tranche la gorge du villageois d'un seul coup.*"

    ve "Pourritures ! Salauds !"

    e "Parfait. Maintenant, parlez."

    ve "Nous ne savons rien ! Absolument rien !"

    e "Et vos hommes, où sont-ils ?"

    ve "La plupart d'entre eux ont descendu la rivière Tay jusqu'à Dundee pour y échanger du bétail. Rien de plus !"

    e "Foutus mensonges !"

    l "Non Einar. C'est bien possible. Ces gens sont une petite cinquantaine tout au plus. L'absence des hommes se fait remarquer, c'est tout."

    e "Très bien. Remerciez celui que vous appelez traître pour avoir défendu votre cause. Nous partons."

    call choix_retour_village_1 pass (massacre = True) from _call_choix_retour_village_1_1

label e_intimider_villageois_village_1:

    e "Vous devriez parler. Maintenant. Les soldats que vous avez devant vous ont tué plus d'hommes que vous n'en avez jamais rencontré dans votre vie."

    e "Vous ne tiendriez pas trois minutes face à nous. Parlez avant que je ne donne l'ordre de tout raser."

    ve "Nous ne savons rien ! Absolument rien !"

    e "Et vos hommes, où sont-ils ?"

    ve "La plupart d'entre eux ont descendu la rivière Tay jusqu'à Dundee pour y échanger du bétail. Rien de plus !"

    e "Foutus mensonges !"

    l "Non Einar. C'est bien possible. Ces gens sont une petite cinquantaine tout au plus. L'absence des hommes se fait remarquer, c'est tout."

    e "Très bien. Remerciez celui que vous appelez traître pour avoir défendu votre cause. Nous partons."

    jump choix_retour_village_1

#Scequence 6 (alternative)
label e_nom_villageoise_maison_1:

    e "Qui es-tu ?"

    ve "Ne m'adressez pas la parole !"

    e "Je me suis montré courtois, mais ça pourrait vite changer. Répond : qui es-tu ?"

    m "Moira."

    $ already_talk = True

    jump menu_maison_1

label e_cache_villageoise_maison_1:
    e "Pourquoi te cacher ?"

    ve "Parce que je connais les porcs dans votre genre."

    e "Mmmh."

    $ already_talk = True

    jump menu_maison_1

label e_info_rebelle_maison_1:
    e "Que sais-tu des rebelles ?"

    ve "Rien."

    e "Tu es aussi belle que décevante."

    $ already_talk = True

    jump menu_maison_1

label e_villagoise_partir_maison_1:
    e "Sors d'ici et rejoint les autres."

    ve "..."

    jump choix_retour_village_1


label e_tuer_moira_maison_1:

    e "Cette rencontre s'achève ici."

    "*Einar tire son épée et tue la villageoise*"

    ve "Vengeanghghh..."

    l "Cette fille était sans défenses !"

    e "Ferme-la. Et maintenant, voyons si les bouseux sont plus enclins à parler."

    scene bg village with dissolve

    ve "Monstres ! Ils ont tué Moira !"

    e "Parfait. Maintenant, parlez."

    ve "Nous ne savons rien ! Absolument rien !"

    e "Et vos hommes, où sont-ils ?"

    ve "La plupart d'entre eux ont descendu la rivière Tay jusqu'à Dundee pour y échanger du bétail. Rien de plus !"

    e "Foutus mensonges !"

    l "Non Einar. C'est bien possible. Ces gens sont une petite cinquantaine tout au plus. L'absence des hommes se fait remarquer, c'est tout."

    e "Très bien. Remerciez celui que vous appelez traître pour avoir défendu votre cause. Nous partons."

    jump e_massacre_village_1
#fin Scequence 6

label choix_retour_village_1(massacre = False):

    if massacre:
        e "Empilez les cadavres avant le départ."

        l "Nous étions censés trouver le village rebelle, pas massacrer des paysans !"

        e "Ta détermination flanche ? Harald sera sûrement satisfait de voir le travail accompli."

        e "Si c'était les rebelles, nous avons éliminé le problème. Si les gens de Perth étaient innocents, les villages alentours nous craindront."

        e "Nous gagnons sur tous les tableaux."

        l "Mieux vaudrait que tu ais raison..."

    else:
        l "Ces gens ne savaient rien, j'en mettrais ma main à couper."

        e "J'espère pour toi que tu as raison, Logan."

    gv "Où allons-nous ?"

    if massacre:
        menu:
            "Rentrer au Chateau de Dunbar":
                call massacre_foret_2 pass (lieu = "chateau") from _call_massacre_foret_2
            "Poursuivre vers le nord":
                call massacre_foret_2 pass (lieu = "nord") from _call_massacre_foret_2_1
    else:
        menu:
            "Rentrer au Chateau de Dunbar":
                call foret_2 pass (lieu = "chateau") from _call_foret_2
            "Poursuivre vers le nord":
                call foret_2 pass (lieu = "nord") from _call_foret_2_1

#Scequence 7
label foret_2(lieu = ""):
    scene bg forest with dissolve

    if lieu == "chateau":

        "Sur le chemin du retour..."

        gv "Pourquoi sommes-nous déjà sur le retour ?"

        e "Parce que j'ai de sérieux doutes sur ce village. Les gens de Perth étaient bien trop louches, quoi qu'en dise Logan."

        l "Tu penses avoir trouvé le village des rebelles ? Si facilement ?"

        e "Je ne suis sûr de rien."

    else:
        "En poursuivant vers le nord..."

        gv "Pourquoi devons-nous poursuivre vers le nord ? Je croyais que nous avions trouvé les rebelles !"

        e "Rien ne permet d'affirmer ça. J'ai beau avoir des doutes sur Perth, je pense qu'une visite des villages plus au nord sera bénéfique."

    scene bg forest_night with dissolve
    "..."

    gv "... et à ce moment là Logan sort de la taverne en feu, une fille sous un bras et la tête du père sous l'autre ! Ha ha !"

    gv "La fille était tellement choquée qu'elle n'a rien dit pendant deux jours ! Cinq de nos gars lui sont passés dessus, elle n'a même pas réagit !"

    gv "Ha Ha Ha !"

    e "Du favoritisme pour les écossais, Logan ? En temps ordinaires tu ne te serais pas privé de tuer quelques personnes et de profiter d'une jolie fille !"

    l "J'ai eu pitié de ces gens. Ils me faisaient penser à Aberdeen."

    e "Je croyais que tu n'aurais aucun problème à tuer des écossais !"

    l "Des écossais rebelles, oui. Pas des innocents."

    e "Tu te ramollis, mon vieux Logan..."

    menu:
        "Mettre en garde le groupe":
            call attaque_massacre_einar_sauf_foret_2 pass (message = "attentif") from _call_attaque_massacre_einar_sauf_foret_2
        "La mission est décevante...":
            call attaque_massacre_einar_sauf_foret_2 pass (message = "deception") from _call_attaque_massacre_einar_sauf_foret_2_1
        "Attitude suspecte des villageois":
            call attaque_massacre_einar_sauf_foret_2 pass (message = "attitude") from _call_attaque_massacre_einar_sauf_foret_2_2
        "Chambrer Logan":
            call attaque_massacre_einar_sauf_foret_2 pass (message = "chambre_logan") from _call_attaque_massacre_einar_sauf_foret_2_3

label attaque_massacre_einar_sauf_foret_2(message = ""):

    if message == "attentif":
        e "Nous sommes en terre hostile. N'importe qui pourrait nous suivre sans que nous ne nous en rendions compte... Vous avez entendu, vous autres ? Faites moins de bruit !"

        gv "S'il n'y a rien de pire que des paysans, je ne redoute pas d'être suivi !"

        e "Tu fanfaronneras moins avec une fourche en travers du gosier, Alvin !"

    elif message == "deception":

        e "Je suis de plus en plus déçu par la mission que nous a confié Harald. Marcher, marcher, marcher... Et quand nous rencontrons enfin une opposition, ce ne sont que des paysans."

        l "Les autres ne semblent pas apprécier le voyage non plus..."

        gv "Le pain de voyage va me rendre fou. Et je ne supporte plus de voir le cul du cheval de Garm devant moi !"

        e "..."

    elif message == "attitude":
        e "Ces villageois avaient l'air étranges..."

        l "Etranges ?"

        e "Oui, louches."

        menu :
            "Craindre un piège":

                jump menu_avertissement_villageois
            "Ils ont dû être effrayés":
                e "La vue de douze guerriers à dû les effrayer. Ils n'avaient probablement jamais vu autant d'armes à la fois !"
                l "Ils ont dû croire que nous étions là pour raser leur village. Ils sont forcément au courant du meurtre de Montgomery, ils auront fait le rapprochement en nous voyant arriver."
                e "A juste titre ! Je regrette presque de ne pas les avoir massa..."

            "Se moquer des villageois":
                l "Ils étaient effrayés, c'est évident."
                e "Ils ont dû être impressionnés par notre présence. C'était une bande d'abrutis congénitaux, ils n'avaient jamais vu d'hommes armés !"
                e "Isolés qu'ils sont dans leur village d'arriérés, à élever leurs chiards et leurs mout..."


        menu menu_avertissement_villageois:
            "Mettre en garde le groupe":
                call attaque_massacre_einar_sauf_foret_2 pass (message = "attentif") from _call_attaque_massacre_einar_sauf_foret_2_4
            "Ne pas craindre des paysans":
                e "J'ai bien l'impression que les villageois tramaient quelque chose contre nous. Qu'ils viennent ! Avec leurs fourches et leurs pelles ! Ils verront nos haches de près ! Ha ha !"
                gv "J'espère qu'ils nous attaqueront ! Un peu d'animation ne sera pas de trop !"
                gv "Un vieux m'a regardé de travers, j'espère pouvoir lui arracher sa tro..."

    else:
        e "D'ailleurs, en parlant de se ramollir... Tu aurais dû emmener une brebis du village, Logan ! J'en ai vu une qui te faisait de l'oeil !"
        gv "Ha ha !"
        l "..."
        e "Ne sois pas si déçu ! La prochaine fois que nous voyons un bélier, je te l'offre ! Je sais que tu les aime beaux et vigoureux !"
        gv "Ha ha ha !"
        l "Ferme la Ein..."

    "*Un cor retentit dans les bois, très proche.*"

    e "En position de combat, tous !"
    gv "Ça venait d'où ?"
    l "Sur la gauche ! Des torches !"

    "*Une volée de flèches siffle en sortant des frondaisons et frappe la plupart des guerriers vikings.*"
    "*Des dizaines de silouhettes jaillissent de l'obscurité et se jettent sur les guerriers encore debout.*"

    e "Regroupez-vous ! Dos-à-dos ! Dressez les boucliers !"

    "*Un meneur semble émerger du groupe des assaillants.*"
    "*Les vikings se font massacrer et ne répondent plus aux ordres d'Einar.*"

    ge "Mourrez, chiens ! Mourrez comme votre lâche d'intendant !"

    e "Approchez, charognes ! Je..."

    "*Une flèche frappe Einar de plein fouet à l'épaule, le désarmant.*"

    l "Einar ! Derrière toi !"

    e "Que..."

    "*L'un des assaillants arrive derrière Einar et lui transperce la cuisse avec un épieu, le faisant tomber au sol.*"

    e "Aaarrggh ! Logan, aide-moi !"

    l "Je suis là !"

    "*Logan est frappé derrière la tête et tombe au sol, face à Einar.*"

    "*Le meneur des assaillants se baisse et égorge Logan devant Einar, qui est au bord de l'évanouissement."

    e "Crevure... Tu..."

    "*Le meneur fixe Einar.*"

    ge "Les chiens du roi-empereur ont échoué."

    menu:
        "Qui es-tu ?":
            jump e_demande_nom_foret_2
        "Non ! Ne me tue pas, pitié !":
            jump e_implore_pitie_foret_2
        "Menacer le meneur":
            jump e_menace_foret_2

#Fin alternative n°1
label massacre_foret_2(lieu = ""):

    if lieu == "chateau":

        "Sur le chemin du retour..."

        gv "Pourquoi sommes-nous déjà sur le retour ?"

        e "Parce que nous avons massacré les rebelles. Mission accomplie, nous rentrons chez nous."

        l "Tu penses avoir trouvé le village des rebelles ? Si facilement ?"

        e "Bien sûr ! Leur manque de coopération était plus qu'évident. Ils étaient les rebelles. Harald sera satisfait !"

    else:
        "En poursuivant vers le nord..."

        gv "Pourquoi devons-nous poursuivre vers le nord ? Nous ne venons pas de massacrer les rebelles ?"

        e "Si, probablement. Mais j'ai tout de même un doute. Autant s'assurer d'avoir fait ce qu'il fallait !"

        e "Une visite des villages plus au nord s'impose. Et nous reproduirons les mêmes actions si nous rencontrons la moindre résistance !"

        gv "Voilà qui fait plaisir à entendre !"


    "..."

    gv "... et à ce moment là Logan sort de la taverne en feu, une fille sous un bras et la tête du père sous l'autre ! Ha ha !"

    gv "La fille était tellement choquée qu'elle n'a rien dit pendant deux jours ! Cinq de nos gars lui sont passés dessus, elle n'a même pas réagit !"

    gv "Ha Ha Ha !"

    e "Du favoritisme pour les écossais, Logan ? En temps ordinaires tu ne te serais pas privé de tuer quelques personnes et de profiter d'une jolie fille !"

    e "J'ai bien remarqué ton comportement à Perth. Tu n'as tué personne. Tu as à peine incendié une grange."

    l "J'ai eu pitié de ces gens. Ils me faisaient penser à Aberdeen."

    e "Je croyais que tu n'aurais aucun problème à tuer des écossais !"

    l "Des écossais rebelles, oui. Pas des innocents."

    e "Ne remet pas mes ordres en question. Tu te ramollis, mon vieux Logan."

    menu:
        "Mettre en garde le groupe":
            call attaque_massacre_foret_2 pass (message = "attentif") from _call_attaque_massacre_foret_2
        "La mission est décevante...":
            call attaque_massacre_foret_2 pass (message = "deception") from _call_attaque_massacre_foret_2_1
        "Se moquer des villageois":
            call attaque_massacre_foret_2 pass (message = "moquerie") from _call_attaque_massacre_foret_2_2
        "Chambrer Logan":
            call attaque_massacre_foret_2 pass (message = "chambre_logan") from _call_attaque_massacre_foret_2_3

label attaque_massacre_foret_2(message = ""):

    if message == "attentif":

        e "Nous sommes en terre hostile. N'importe qui pourrait nous suivre sans que nous ne nous en rendions compte... Vous avez entendu, vous autres ? Faites moins de bruit !"

        gv "Nous avons massacré le village ! Qui pourrait nous attaquer ?"

        e "Et les hommes, abruti ? Il n'y en avait presque aucun à Perth."

        gv "Les hommes ? Il n'y a que des fermiers, dans le coin !"

        e "Tu fanfaronneras moins avec une fourche en travers du gosier, Alvin !"

    elif message == "deception":

        e "Je suis de plus en plus déçu par la mission que nous a confié Harald. Marcher, marcher, marcher... Et quand nous rencontrons enfin une opposition, ce ne sont que des paysans."

        l "Les autres ne semblent pas apprécier le voyage non plus..."

        gv "Le pain de voyage va me rendre fou. Et je ne supporte plus de voir le cul du cheval de Garm devant moi !"

        e "Au moins, Perth nous aura fournit une petite distraction !"

        gv "J'aurais préféré des cibles qui se défendent..."

    elif message == "moquerie":
        gv "Hé, regardez ! J'ai une dent incrustée dans mon bouclier !"

        e "Ne la retire pas, ça porte bonheur, ha ha !"

        gv "Ils étaient tellement faibles ! Je me souviendrai de Perth comme..."

        e "On ne se souviendra de rien, Garm ! Ce serait faire trop d'honneur à un village d'abrutis consanguins perdu au bout du mon..."


    else:
        e "D'ailleurs, en parlant de se ramollir... Tu aurais dû emmener une brebis du village, Logan ! J'en ai vu une qui te faisait de l'oeil !"
        gv "Ha ha !"
        l "..."
        e "Ne sois pas si déçu ! La prochaine fois que nous voyons un bélier, je te l'offre ! Je sais que tu les aime beaux et vigoureux !"
        gv "Ha ha ha !"
        l "Ferme-la Ein..."

    "*Un cor retentit dans les bois, très proche.*"

    e "En position de combat, tous !"
    gv "Ça venait d'où ?"
    l "Sur la gauche ! Des torches !"

    "*Une volée de flèches siffle en sortant des frondaisons et frappe la plupart des guerriers vikings.*"
    "*Des dizaines de silouhettes jaillissent de l'obscurité et se jettent sur les guerriers encore debout.*"

    e "Regroupez-vous ! Dos-à-dos ! Dressez les boucliers !"

    "*Un meneur semble émerger du groupe des assaillants.*"
    "*Les vikings se font massacrer et ne répondent plus aux ordres d'Einar.*"

    ge "Mourrez, chiens ! Vous allez regretter ce que vous avez fait à Perth !"

    e "Approchez, charognes ! Je..."

    "*Une flèche frappe Einar de plein fouet à l'épaule, le désarmant.*"

    l "Einar ! Derrière toi !"

    e "Que..."

    "*L'un des assaillants arrive derrière Einar et lui transperce la cuisse avec un épieu, le faisant tomber au sol.*"

    e "Aaarrggh ! Logan, aide-moi !"

    l "Je suis là !"

    "*Logan est frappé derrière la tête et tombe au sol, face à Einar.*"

    "*Le meneur des assaillants se baisse et égorge Logan devant Einar, qui est au bord de l'évanouissement."

    e "Crevure... Tu..."

    "*Le meneur fixe Einar.*"

    ge "Les chiens du roi-empereur ont échoué."

    menu:
        "Qui es-tu ?":
            call e_demande_nom_foret_2 pass (bad_ending = True) from _call_e_demande_nom_foret_2
            #jump e_demande_nom_foret_2 pass (bad_ending = True)
        "Non ne me tue pas, pitié!":
            call e_implore_pitie_foret_2 pass (bad_ending = True) from _call_e_implore_pitie_foret_2
        "Menacer le meneur":
            call e_menace_foret_2 pass (bad_ending = True) from _call_e_menace_foret_2


label e_demande_nom_foret_2(bad_ending = False):

    e "Qui es-tu, lâche ?"

    if bad_ending:
        ge "..."
        jump bad_ending_1
    else:
        o "Ogma. Le Hurleur."
        "*Einar reçoit un violent coup au crâne et sombre dans les ténèbres, inconscient.*"
        jump e_reveil_village_2

label e_implore_pitie_foret_2(bad_ending = False):

    e "Par pitié, ne me tue pas ! Dites-moi quoi faire, et je le ferai !"

    if bad_ending:
        ge "Lâche jusqu'au bout..."
        jump bad_ending_1
    else:
        ge "Nous allons voir ça..."
        "*Einar reçoit un violent coup au crâne et sombre dans les ténèbres, inconscient.*"
        jump e_reveil_village_2

label e_menace_foret_2(bad_ending = False):

    e "Tuez-moi ! Le roi brûlera toute la Grande-Bretagne pour votre insolence !"

    if bad_ending:
        ge "Je ne crains pas ton roi."
        jump bad_ending_1
    else:
        ge "Je ne crains pas ton roi."
        "*Einar reçoit un violent coup au crâne et sombre dans les ténèbres, inconscient.*"
        jump e_reveil_village_2


#Sequence 8
label e_reveil_village_2:
    scene bg house with dissolve

    $ already_talk = False

    e "Huugh..."

    ge "Ogma ! Il se réveille !"

    o "Ah ! La belle endormie. "

    e "Arrgh... Mon épaule..."

    o "Oui je sais, ça fait mal. La tête de la flèche est toujours à sa place."

    e "Enfoiré ! Vous les avez tous tués !"

    o "..."

    e "Qui... Aarrgh... êtes vous ?"

    o "Ça me paraît assez évident. Nous sommes ceux que toi et les tiens cherchiez. Bravo, vous nous avez trouvé."

    e "Les rebelles ?"

    o "..."

    e "Où sont les autres ? Où sont mes compagnons ?"

    e "Ordure ! Je me rappelle ! C'est toi qui a tué Logan !"

    o "C'était un traître."

    e "C'est lui qui m'a retenu de massacrer Perth ! C'est lui qui a sauvé la vie de vos vieux et de vos truies de femmes !"

    o "Alors j'imagine que sa mort est regrettable."

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

            "*Ogma frappe Einar sur son épaule blessée*"

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
        "Insulter":
            $ choix_ogma_1 = "insulter"


    if choix_ogma_1 == "incomprehension":

        e "J'ai peur de ne pas tout comprendre."

        o "L'explication est simple."
    elif choix_ogma_1 == "insulter":
        e "Vous allez être déçus ! Vous n'obtiendrez rien de moi, charognes ! Vous ne me ferez pas trahir mon allégeance !"

        o "Calme toi. Les termes de mon offre suffiront à te faire changer d'avis, j'en suis sûr."
    else:
        "..."

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
        "Accepter":
            jump accepter_trahir_village_2
        "Vous me faites confiance ?" if already_talk == False:

            e "Qui vous dit que je tiendrai parole une fois remis en liberté ?"
            o "Pour faire simple, tu es obligé de respecter notre accord."
            o "J'ai des contacts partout en Grande-Bretagne et sur le continent, je te retrouverais en quelques jours à peine."
            o "Et tu n'aimerais pas que je te retrouve. Alors ?"

            $ already_talk = True

            jump menu_choix_trahison_village_2
        "Refuser":
            jump refuser_trahir_village_2

label refuser_trahir_village_2:

    e "Allez vous faire foutre. Je ne trahirai pas la parole que j'ai donné à mon roi."

    o "Mauvaise réponse."

    "*Ogma enfonce deux doigts dans la plaie de l'épaule d'Einar, pressant la pointe de flèche.*"

    e "AAAAARRRGH !"

    o "Tiens, on dirait que la pointe est coincée dans une articulation !"

    e "AAAHH ! STOP !"

    o "Jouer les fortes têtes ne te servira à rien ici. Tout ça est bien plus éprouvant pour toi que pour moi."

    e "ARRÊTEZ ! ARRÊTAAAARGH !"

    "*Ogma retire ses doigts de la plaie.*"

    o "Tu as changé d'avis sur la question ?"

    menu:
        "Céder":
            e "Très bien... Hhhggh... J'accepte..."
            o "Parfait !"
            jump accepter_trahir_village_2
        "Ne rien lâcher":
            jump bad_ending_2


label accepter_trahir_village_2:

    e "Très bien... Je vais faire ce que vous me demandez."
    o "Tu as fait le bon choix."
    e "Quand dois-je partir ?"
    o "Ha ha ! Pas d'enthousiasme excessif ! Si je te laissais partir maintenant, tu mourrais aussitôt ! Nous allons soigner tes blessures."
    o "Je vais te laisser. Nous nous retrouverons bientôt."

    jump interieur_maison_village_1
