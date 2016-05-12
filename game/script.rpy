# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
#Image représentant les personnages
#Einar
define e = Character('Einar', color="#e74c3c")
image einar serious = "einar_1.png"

#Logan
define l = Character('Logan', color="#f1c40f")
image logan fache = "logan.png"

#Harald
define h = Character('Harald', color="#3498db")
image harald normal = "harald_min.png"

#Ogma
define o = Character('Ogma', color="#d35400")
image ogma normal = "ogma.png"

#Moira
define m = Character("Moira", color = "#f00")
image moira normal = "moira.png"

#Patrick
define p = Character("Patrick")
image patrick normal = "cure.png"

#Villageois
define pe1 = Character("Prissonier écossais 1")
image prisonnier normal = "prisonnier.png"
define pe2 = Character("Prissonier écossais 2")
define pe3 = Character("Prissonière écossais 1")

#Scene
image bg forest = "foret_cabane.jpg"
image bg forest_night = "forest_night.jpg"
image bg forest_crepuscule = "forest_crepuscule.jpg"
image bg little_heaven = "little_heaven.jpg"
image bg sentier_jour = "sentier_foret_jour.jpg"
image bg village = "village.jpg"
image bg village2_jour = "village2_jour.jpg"
image bg village2_crepuscule = "village2_crepuscule.jpg"
image bg house = "house.jpg"
image bg house2_jour = "house2_jour.jpg"
image bg house2_night = "house2_night.jpg"
image bg house2_aube = "house2_aube.jpg"
image bg mer = "chateau_mer.jpg"
image bg pont_levis = "pont_levis.jpg"
image bg cours_chateau = "cours_chateau.png"
image bg cote1 = "cote1.jpg"


#Fond uni
image bg black = "#000"

# Déclarez les personnages utilisés dans le jeu.



define gv = Character('Guerriers Vikings', color="#e67e22")
define vm = Character('Villageois', color="#3498db")

define gc = Character("Garde du Chateau")
image garde_chateau  normal= ("garde_chateau.png")

define ge = Character('Guerriers écossais', color="#f39c12")






# Le jeu commence ici

label start:

    scene bg black
    "En l'an 1038, Harald Sigurdsson de Norvège, frère d'Olaf le Saint, découvre les Clous de la Sainte Croix à Jérusalem alors qu'il est garde varègue au service de l'Impératrice Zoé de Constantinople."

    "Les Clous donnent à Harald la force et l'immortalité. Le viking, convaincu d'être un élu divin, décide d'orner sa hache des Clous. Il créé ainsi une nouvelle relique : la Hache Sainte."

    "Revenu triomphalement en Norvège, il est couronné roi et entame de grandes campagnes militaires visant à christianiser tout le monde connu ainsi qu'à asseoir sa suprématie."

    "En 1066, la bataille de Stamford Bridge est remportée par l'armée viking face aux anglais qui avaient pourtant planifié un attentat contre Harald. Le roi viking domine alors une vaste portion de l'Europe : sa volonté est désormais de partir à la conquête du reste du monde."

    "Armé de la Hache Sainte, Harald prend le contrôle du Moyen-Orient et d'une partie de l'Asie et de l'Afrique. En 1080, Harald est devenu l'équivalent d'Alexandre le Grand : un roi-empereur, une légende vivante, un demi-dieu."

    "L'hégémonie des vikings et du christianisme est presque totale."

    "Nous sommes en 1082. Des paysans écossais ont tué Clyde Montgomery, l'intendant que Harald avait placé à la tête de l'Ecosse. Le roi-empereur a décidé de revenir mater cette petite rébellion et d’en faire un exemple."

    "Nul ne peut remettre en question la toute-puissance de l'élu divin, du roi-empereur, du porteur de la Hache Sainte."

    jump intro

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

    "Dans la forêt de Westruther, au coeur de l'Ecosse, une troupe de vikings se dirige vers le chateau de Dunbar pour s'y installer et préparer l'expédition punitive visant à mater les rebelles."
    show harald normal at left with dissolve
    "A la tête de la cohorte, Harald, roi-empereur des vikings. Il a décidé de venir punir lui-même les insolents ayant osé défier son pouvoir."

    "A ses côtés marche une armée de cent vikings, guerriers et huscarls, impatients d'en découdre : cela fait déjà longtemps qu'ils ne se sont pas battus."
    show logan fache at right with dissolve
    "A l'avant du contingent un guerrier écossais éclaire la voie ; Logan a juré fidélité à Harald depuis longtemps et le mène jusqu'au château de Dunbar."
    show einar serious at center with dissolve
    "Einar est l'un des huscarls : un guerrier d'élite, chef militaire et garde personnel du roi."

    menu:
        "Parler à Harald":
            hide logan fache

            e "Mon Roi, sommes-nous proches ?"

            show einar serious at left
            show harald normal at right

            h "Nous n'en avons plus pour très longtemps. Une heure, tout au plus."

            menu menu_harald_choice_foret:
                "Quel est le plan ?" if plan_choice:

                    e "Quelles sont les instructions, sire ? A quoi devons-nous nous préparer ?"

                    h "Tout d'abord, nous allons atteindre le château de Dunbar. Là, l'évêque Patrick d'Edimbourg nous accueillera."

                    h "Ensuite je détacherai un groupe d'éclaireurs. Je veux retrouver le village des rebelles le plus vite possible."

                    h "Une fois le village retrouvé, j'aviserai. Mais ces foutus écossais n'apprécieront pas ce qui va leur arriver, tu peux me croire."

                    $ plan_choice = False

                    jump menu_harald_choice_foret

                "Parler de la région" if region_choice:

                    e "Qu'indiquent les cartes à propos de la région, sire ? Je n'ai pas eu le loisir de les consulter."

                    h "Pas grand chose. Des plaines d'herbe rase, des rocailles abruptes, quelques forêts. Et surtout, la mer."

                    h "Nous ne sommes encore que dans les Lowlands ; les Highlands sont plus au nord."

                    h "Et hormis le nom, je dois dire que je ne vois que peu de différences entre ces deux territoires. "

                    e "La région a l'air inhospitalière..."

                    h "Sauf pour les moutons. Il y a plus de moutons que d'hommes, par ici. Et quand je parle d'hommes, je suis encore trop élogieux. N'en déplaise à Logan."

                    $ region_choice = False

                    jump menu_harald_choice_foret

                "Se montrer enthousiaste" if enthousiaste_choice:

                    e "Sire, il me tarde de massacrer quelques paysans !"

                    h "Ha ha ! Ne sois pas si hatif, Einar. Il ne s'agit pas de tuer tout ce qui bouge. Pas pour le moment. "

                    e "Sauf votre respect, Sire, votre Hache nous a privé de nombreuses batailles. D'habitude, vos ennemis se rendent dès qu'ils la voient ! Alors un soulèvement paysan, c'est une chance inespérée !"

                    h "Ton enthousiasme fait plaisir à voir !"

                    $ enthousiaste_choice = False

                    jump menu_harald_choice_foret

                "Pourquoi tant de confiance ?" if confiance_choice:

                    e "Mon roi, votre présence ici m'intrigue : pourquoi risquer votre vie dans une expedition de moindre importance ? Vous pourriez recevoir une flèche !"

                    h "Je suis l'élu divin, Einar. Je porte une relique du Christ. La Hache me rend immortel. Une flèche me ferait rire, rien de plus."

                    h "Harald Sigurdsson, roi-empereur des vikings, abattu par une flèche de paysan rebelle ! Ha ha !"

                    e "Ha ! Les dirigeants du monde entier craindraient les écossais !"

                    $ confiance_choice = False

                    jump menu_harald_choice_foret

                "Est-il vraiment nécessaire de massacrer une bande paysans ?" if tuer_choice:

                    e "Mon Roi, est-il vraiment nécessaire de tuer des paysans ? Ne pensez-vous pas que de nombreux innocents risquent de perde la vie ?"

                    h "Quelle mollesse de ta part, Einar ! Je suis surpris !"

                    h "Il n'y a pas d'innocents sur ces terres. En tuant mon intendant, ils se sont attaqués à moi. Ils mourront tous pour l'exemple."

                    h "J'ai un message à faire passer au reste du monde. La moindre rébellion entraînera une sanction immédiate, sans distinction."

                    e "La mort."

                    h "Exactement !"

                    $ tuer_choice = False

                    jump menu_harald_choice_foret

                "Continuer silencieusement":
                    e "..."

        "Parler à Logan":
            e "Ça va, Logan ? Tu n'as pas desserré les dents depuis Newcastle. "

            show einar serious at left
            show logan fache at right

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

                    l "Cela dit, je ne suis pas dépaysé. La différence entre ici et chez moi, ce sont les montagnes."

                    l "Pour le reste, tout est identique : mêmes forêts, mêmes plaines herbeuses. Et la mer."

                    l "Quant aux gens qui vivent ici, j'imagine qu'ils sont identiques à ceux d'Aberdeen."

                    $ region_choice = False

                    jump menu_logan_choice_foret

                "Se montrer enthousiaste" if enthousiaste_choice:

                    e "Ma hache me démange. Je fracasserais bien quelques crânes."

                    l "Moi aussi ! Je ne supporte plus ces voyages interminables. Deux mois que nous n'avons pas combattu ! Et plus d'un an depuis la dernière vraie bataille. Il est grand temps de nous dégourdir un peu !"

                    e "Tuer des écossais ne te posera pas de problème ?"

                    l "Je n'aurai pas plus de problèmes que toi. Ces gens sont des inconnus, et ils ont tué l'un des vassaux de notre roi. C'est une motivation amplement suffisante pour trancher la tête de quelques compatriotes."

                    $ enthousiaste_choice = False

                    jump menu_logan_choice_foret

                "Pourquoi Harald est-il si confiant ?" if confiance_choice:

                    e "Le roi me paraît bien confiant."

                    l "Et pourquoi ne le serait-il pas ? Il est le plus grand souverain que le monde connaisse. Il porte une Hache Sainte incrustée des Clous de la Sainte Croix."

                    l "Il est immortel et invincible. Une armée de vétérans marche avec lui. S'il y a bien une personne sur cette terre qui puisse avoir confiance en lui-même, c'est notre roi."

                    $ confiance_choice = False

                    jump menu_logan_choice_foret

                "Est-il vraiment nécessaire de massacrer une bande de paysans ?" if tuer_choice:

                    e "Je me demande si le massacre de paysans innocents est justifié."

                    l "Tu te poses beaucoup de questions. Si notre roi nous le demande, nous le faisons."

                    l "Et à titre personnel, tuer des paysans ne me pose aucun problème. C'est un message que nous envoyons à tous les rebelles potentiels : trahissez Harald, et vous verrez vos familles mourir."

                    $ tuer_choice = False

                    jump menu_logan_choice_foret

                "Continuer silencieusement":
                    e "..."

        "Ne rien dire":
            e "..."

    show einar serious

    jump plaine_1

#Sequence 2
label plaine_1 :

    scene bg mer with dissolve

    "*Une heure plus tard.*"

    show harald normal at right with dissolve

    h "Ha ! Dunbar, enfin. Un bon repas nous attend."

    show einar serious at left with dissolve

    e "Dois-je envoyer un émissaire annoncer notre arrivée ?"

    h "Non. Je compte sur toi pour autre chose."

    e "Autre chose ?"

    h "Pas de repas pour toi, hélas. J'ai besoin d'envoyer un groupe de reconnaissance à l'avant de l'armée, afin de débusquer le village rebelle."

    h "Je compte sur toi pour diriger la troupe. Tu es un bon meneur d'hommes, et ton expérience du pistage te permettra de trouver les rebelles. Ça ne fait aucun doute !"

    menu menu_harald_eclaireur_foret_1:
        "Je refuse cette responsabilité":

            e "Mon roi, je me vois dans l'obligation de refuser cette responsabilité."

            h "Pardon ? C'est un ordre, Einar. Pas une proposition."

            e "Pardonnez-moi, sire. "

            jump menu_harald_eclaireur_foret_1

        "Pourquoi ?":

            e "Pourquoi dois-je mener ce groupe de reconnaissance ?"

            h "Parce que je te le demande. Comme je te l'ai dit, je suis convaincu que tes qualités te permettront de mener à bien cette mission mieux que quiconque."

            h "Cette reconnaissance est très importante : elle me permettra de cibler précisément le village à châtier. Nous gagnerons un temps précieux et nous épargnerons les villages n'ayant aucun rapport avec cette rébellion."

            jump menu_harald_eclaireur_foret_1

        "A quel dangers dois-je m'attendre ?":

            e "Sire, quels sont les dangers de cette mission ? A quoi dois-je m'attendre ?"

            h "Il n'y a aucun danger. Dans le pire des cas, tu pourrais te faire insulter par une bande de villageois chétifs. Tu mènes un groupe de guerriers vikings. Tu es un huscarl. Rien ne va te résister."

            jump menu_harald_eclaireur_foret_1

        "J'accepte":

            e "J'accepte cette mission."

            h "Et j'en suis satisfait. Part dès maintenant : il n'y a pas de temps à perdre. Tu atteindras Stirling avant la nuit. Les villages que je soupçonne d'être rebelles se trouvent à une journée plus loin."

            e "Fort bien. "

        "Avec grand plaisir !":

            e "Comme il vous plaira, mon roi. C'est un grand honneur que vous me faites ! "

            h "Cesse tes flagorneries et part sans tarder."

    show logan fache at center
    l "Einar, je t'accompagne ! Mes connaissances de la région ne seront pas de trop, et la vue d'un écossais parmi les vikings rassurera peut-être les villageois. "

    menu:
        "Merci Logan !":

            e "Merci beaucoup Logan. Je suis heureux de pouvoir compter sur toi !"

            l "J'aurais préféré manger à la table du roi ce soir, mais j'avais peur que tu te perdes en forêt !"

            h "Ne vous inquiétez pas. Vous aurez tout les deux de quoi boire et manger une fois revenus ! Maintenant, partez !"

        "Je regrette, mais non.":

            e "Non, je refuse. Je n'ai pas besoin de toi, Logan. C'est une mission de reconnaissance : moins nous sommes, mieux c'est."

            l "..."

            h "Ton ingratitude est exaspérante, Einar. Logan t'accompagnera, que tu le veuilles ou non. C'est un ordre !"

            l "Sire, vous..."

            h "Silence. Partez maintenant, ne perdez pas de temps."

        "Très bien, puisque tu insistes...":

            e "Très bien... Viens, mais tais-toi. J'en ai assez de voyager à travers tout le continent. Nous accomplissons notre devoir et nous rentrons au château. Arrange-toi pour ne pas me déranger."

            l "Moi aussi, j'aime voyager dans une ambiance chaleureuse."

            h "Parfait. Je suis certain que Logan saura se montrer utile. Partez, et ne revenez qu'après avoir trouvé les rebelles !"

    jump plaine_2

#Sequence 3
label plaine_2:
    hide logan fache
    hide einar serious
    hide harald normal
    "*Le lendemain...*"

    gv "Cette mission n'a rien de terrible... Je suis déçu."
    gv "Nous aurions dû rester plus longtemps à Stirling. Il y avait une bien belle tavernière qui semblait prête à me sauter sur les genoux !"

    show einar serious at left with dissolve

    menu:
        "Mettre en garde" :

                e "Méfiez vous. Le roi n'est pas avec nous. Sans la Hache, nous sommes à la merci de n'importe quel piège. Faites silence et restez aux aguets."

                e "Rien qu'en t'écoutant, je suis sûr que les rebelles connaissent déjà ton nom, celui de tes parents et la taille de ta queue, Alvin."

                gv "Vous avez entendu, les gars ? Ouvrez l'oeil."

        "C'est une mission sans intérêt" :

                e "Je suis bien d'accord. Et je suis certain que nous ne rencontrerons rien de pire que des landes et des forêts. Pourquoi nous envoyer battre la campagne à la recherche d'une bande de péquenauds ?"

                show logan fache at left with dissolve

                l "Tu le prends comme une punition ?"

                e "Oui. J'estime qu'après tout le temps passé en campagne aux côtés du roi, il aurait pu choisir quelqu'un d'autre pour accomplir ses basses besognes."

        "Motiver les troupes" :

            e "Et je suis convaincu que nous ne rencontrerons rien de plus excitant qu'une tavernière au milieu de toute cette foutue caillasse ! Ha, se défouler sur des villageois, ce sera notre récompense !"

            e "Plus vite le problème sera réglé, plus vite nous pourrons glisser nos pieds sous la table et nous remplir la panse !"

            gv "Ha ha ! Bien parlé !"

        "Chambrer Logan" :

            e "Tu ne parles pas beaucoup, Logan. Tu as un problème, ou bien tu attends une autorisation du roi pour l'ouvrir ?"

            show logan fache at left with dissolve

            l "..."

            e "Ha, il est obéissant en plus ! Tu attends aussi des autorisations royales pour baiser ? Notre bon Harald doit te la tenir ?"

            l "..."

            gv "Ha ha ha !"

        "Silence ! Je veux deux groupes à l'avant..." :


            e "Taisez-vous. Je veux deux groupes à l'avant, deux groupes à l'arrière. Au centre, Logan et moi. Et pressons le pas."

            show logan fache at left with dissolve

            l "Einar, les hommes sont aussi fatigués que nous. Tu devrais..."

            e "Toi aussi, tais-toi. Je veux que nous menions cette mission de la façon la plus exemplaire possible."

            l "Bien."

    jump foret_1

#Scequence 4
label foret_1:

    scene bg forest with dissolve

    "*Un jour plus tard...*"

    show einar serious at left with dissolve

    e "Une forêt. Encore..."

    menu:
        "Impatient de rentrer en Norvège":

            e "Plus le temps passe, plus la Norvège me manque. Depuis combien de temps n'y suis-je pas retourné ?"

            gv "J'aimerais retrouver la Suède. Je n'ai aucune nouvelles de ma famille depuis notre campagne d'Egypte."

            gv "Je n'ai pas de nouvelles non plus. Mon vieux père pourrait bien être mort sans que je n'en sache rien !"
            show logan fache at right with dissolve
            l "Harald doit ressentir la même chose. Il n'a pas vu sa femme ni ses enfants depuis aussi longtemps que nous."

            gv "Qu'est-ce que tu en sais, Logan ? C'est nous ta seule famille !"

            l "..."

            menu:
                "Il me tarde de recevoir mes terres":

                    e "Le roi m'a promit des terres. Ça fait des années qu'il me fait miroiter des récompenses sans jamais me les offrir."

                    e "Une fois sur mes terres, je ferai bâtir un manoir."

                    show logan fache at right with dissolve

                    l "Et si ces terres ne sont pas en Norvège ?"

                    e "Peu importe. Tout ce que je veux, c'est enfin pouvoir me sentir chez moi. Norvège ou pas."

                "Assez de niaiseries pour aujourd'hui":

                    e "Taisez-vous. Nous ne sommes qu'à mi-chemin, la route est encore longue. Demain, nous atteindrons Perth."

                    show logan fache at right with dissolve

                    l "Perth ?"

                    e "Oui. D'après les rapports, les rebelles sont venus de cette région. C'est un petit village sans défenses. Si nous ne trouvons rien, nous poursuivrons jusqu'à Dundee."

        "Se moquer des autochtones" :

            e "J'imagine la tête des sauvages qui vivent dans la région. C'est une bonne chose que les écossais aient intégré l'empire : ça les civilisera un peu !"

            e "Je suis persuadé qu'ils vivent dans des cabanes délabrées et qu'ils couchent avec leurs chèvres !"

            gv "Ha ha !"

            show logan fache at right with dissolve

            l "Non. Nous vivons dans des maisons de pierre. Et pour le reste, tu constateras que nous avons bien plus de raisons de coucher avec nos femmes qu'avec nos chèvres."

        "Impatient de terminer la mission" :

            e "Je commence à être lassé de notre petite randonnée. Une journée à crapahuter sur cette saloperie d'île sans voir âme qui vive. On trouve le village et on rentre au château. Et à bride abattue !"

        "Motiver les troupes" :

            e "Ne relâchez pas l'effort. D'ici une journée, nous nous serons suffisamment enfoncés dans les Highlands pour avoir une chance de trouver le village des rebelles."

        "Chambrer Logan" :

            e "Toujours pas envie de parler, Logan ? Trop occupé à rêver du corps sculptural d'une de ces magnifiques brebis écossaises ?"

            show logan fache at right with dissolve

            l "..."

            gv "Ha ha !"

        "Demander à Logan ce qu'il pense de la mission" :

            e "Tu es le seul à ne pas encore t'être plaint de la mission que nous a confié le roi."
            show logan fache at right with dissolve
            l "Je ne vois pas de raisons de me plaindre. J'accomplis mon devoir. Le roi nous récompensera à notre retour."

            e "Tu es bien optimiste ! Depuis le temps qu'il me promet des terres..."

            menu:
                "Pourquoi as-tu décidé de m'accompagner ?":

                    e "Pourquoi avoir choisi de m'accompagner ? "

                    l "Je l'ai déjà dit. Même sans être natif du coin, je connais la région mieux qu'aucun d'entre vous. Et ma présence facilitera les relations avec les autres écossais."

                    e "J'imagine."

                "Je suis content que tu sois là":

                    e "Quoi qu'il en soit, merci d'avoir choisi de m'accompagner."

                    l "Ce n'est rien. Si un jour une campagne m'amène en Norvège, je serai heureux de compter sur toi."

                "Tu aurais du rester au château":

                    e "Tu aurais du rester avec Harald!"

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

    jump village_1

#Scequence 5
#Scene 1
label village_1:
    hide einar serious
    $ moira_met = False

    scene bg village with dissolve
    "*Peu après midi, la troupe parvient en vue d'un village...*"
    show logan fache at right with dissolve
    l "Nous y sommes. Perth."

    "*Les villageois vaquent à leurs occupations. Certains d'entre eux ont remarqué l'arrivée des guerriers vikings et affichent une expression craintive.*"
    show einar serious at left with dissolve
    e "Ça me semble bien calme."

    gv "On dirait qu'il n'y a pas grand monde..."

    e "Si. Uniquement des vieillards, des femmes et des enfants."

    gv "Ça sent le traquenard... Einar ?"

    menu:
        "Massacrez-les !":
            jump e_massacre_village_1
        "Demander des infomation sur les rebelles":
            jump e_demander_information_village_1
        "Fouillez le village!":
            jump e_fouiller_village_1
        "Chercher soi-même dans le village":
            call e_fouiller_village_1 pass (einarFouille = True) from _call_e_fouiller_village_1

label e_massacre_village_1:

    e "Massacrez moi tout ça ! Je veux un beau charnier sur la place d'ici une heure !"

    gv "HAAAAA !"

    vm "Sauvez les enfants ! Les enfants !"


    call choix_retour_village_1 pass (massacre = True) from _call_choix_retour_village_1

label e_demander_information_village_1:

    e "Que savez-vous des rebelles ? Où sont-ils ?"

    l "Parle, vieil homme. Je suis écossais. Nous ne vous voulons aucun mal."

    vm "Ecossais ? Traître à ta terre et à ton sang ! Tu mènes des envahisseurs parmi les tiens ! *crache*"

    e "Quel succès, Logan."

    e "Qui traitez-vous d'envahisseurs ? Ces terres appartiennent au roi-empereur Harald Sigurdsson de Norvège, porteur de le Hache Sainte."

    e "Votre attitude ressemble à un aveu de trahison !"

    l "Calme-toi Einar. Comment réagirais-tu si tu voyais une armée byzantine débarquer en Norvège ?"

    e "..."

    menu:
        "Tuer un villageois pour les faire parler":
            jump e_tuer_villageois_village_1

        "Hausser le ton":
            jump e_intimider_villageois_village_1

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
    show moira at center
    show einar serious at left with dissolve
    menu menu_maison_1:
        "Qui es-tu ?":
            jump e_nom_villageoise_maison_1
        "Pourquoi être cachée ?":
            jump e_cache_villageoise_maison_1
        "Où sont les rebelles ?":
            jump e_info_rebelle_maison_1
        #Si Einar à déjà parlé une fois à Moira
        "Tuer la villageoise" if already_talk:
            jump e_tuer_moira_maison_1
        "La laisser partir" if already_talk:
            jump e_villagoise_partir_maison_1

label e_tuer_villageois_village_1:

    e "Toi. Approche."

    vm "Moi ?"

    e "Oui ! Dépêche toi !"

    vm "Monseigneur, je ..."

    "*Einar tranche la gorge du villageois d'un seul coup.*"

    vm "Pourritures ! Salauds !"

    e "Parfait. Maintenant, parlez."

    vm "Nous ne savons rien ! Absolument rien !"

    e "Et vos hommes, où sont-ils ?"

    vm "La plupart d'entre eux ont descendu la rivière Tay jusqu'à Dundee pour y échanger du bétail. Rien de plus !"

    e "Foutus mensonges !"

    l "Non Einar. C'est bien possible. Ces gens sont une petite cinquantaine tout au plus. L'absence des hommes se fait remarquer, c'est tout."

    e "Très bien. Remerciez celui que vous appelez traître pour avoir défendu votre cause. Nous partons."

    call choix_retour_village_1 pass (massacre = True) from _call_choix_retour_village_1_1

label e_intimider_villageois_village_1:

    e "Vous devriez parler. Maintenant. Les soldats que vous avez devant vous ont tué plus d'hommes que vous n'en avez jamais rencontré dans votre vie."

    e "Vous ne tiendriez pas trois minutes face à nous. Parlez avant que je ne donne l'ordre de tout raser."

    vm "Nous ne savons rien ! Absolument rien !"

    e "Et vos hommes, où sont-ils ?"

    vm "La plupart d'entre eux ont descendu la rivière Tay jusqu'à Dundee pour y échanger du bétail. Rien de plus !"

    e "Foutus mensonges !"

    l "Non Einar. C'est bien possible. Ces gens sont une petite cinquantaine tout au plus. L'absence des hommes se fait remarquer, c'est tout."

    e "Très bien. Remerciez celui que vous appelez traître pour avoir défendu votre cause. Nous partons."

    jump choix_retour_village_1

#Scequence 6 (alternative)
label e_nom_villageoise_maison_1:

    e "Qui es-tu ?"

    vm "Ne m'adressez pas la parole !"

    e "Je me suis montré courtois, mais ça pourrait vite changer. Répond : qui es-tu ?"

    m "Moira."

    $ already_talk = True

    jump menu_maison_1

label e_cache_villageoise_maison_1:
    e "Pourquoi te cacher ?"

    vm "Parce que je connais les porcs dans votre genre."

    e "Mmmh."

    $ already_talk = True

    jump menu_maison_1

label e_info_rebelle_maison_1:
    e "Que sais-tu des rebelles ?"

    vm "Rien."

    e "Tu es aussi belle que décevante."

    $ already_talk = True

    jump menu_maison_1

label e_villagoise_partir_maison_1:
    e "Sors d'ici et rejoint les autres."

    vm "..."

    jump choix_retour_village_1


label e_tuer_moira_maison_1:

    e "Cette rencontre s'achève ici."

    "*Einar tire son épée et tue la villageoise*"

    vm "Vengeanghghh..."

    l "Cette fille était sans défenses !"

    e "Ferme-la. Et maintenant, voyons si les bouseux sont plus enclins à parler."

    scene bg village with dissolve

    vm "Monstres ! Ils ont tué Moira !"

    e "Parfait. Maintenant, parlez."

    vm "Nous ne savons rien ! Absolument rien !"

    e "Et vos hommes, où sont-ils ?"

    vm "La plupart d'entre eux ont descendu la rivière Tay jusqu'à Dundee pour y échanger du bétail. Rien de plus !"

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
        "Insulter":
            $ choix_ogma_1 = "insulter"
        "Ne rien dire":
            $ choix_ogma_1 = "silcence"

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
        "Refuser":
            jump refuser_trahir_village_2
        "Quelles sont vos garanties ?" if already_talk == False:

            e "Qui vous dit que je tiendrai parole une fois remis en liberté ?"
            o "Pour faire simple, tu es obligé de respecter notre accord."
            o "J'ai des contacts partout en Grande-Bretagne et sur le continent, je te retrouverais en quelques jours à peine."
            o "Et tu n'aimerais pas que je te retrouve. Alors ?"

            $ already_talk = True

            jump menu_choix_trahison_village_2
        "Accepter":
            jump accepter_trahir_village_2

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

#Acte 2
#Sequence 1
label interieur_maison_village_1:
    scene bg house2_jour with dissolve

    $ critique_ogma = False

    "*Einar émerge du sommeil...*"
    e "Où... Je suis entravé ? Huuugh..."

    menu menu_rencontre_moira_blesse:
        "Toi ?" if moira_met:
            e "Toi ? ... Moira ?"
            m "Vous vous rappelez de moi ?"
            e "Oui. Tu étais à Perth."
            m "Ne me tutoyez pas, s'il vous plaît. J'étais bien à Perth quand vous êtes arrivés pour menacer nos anciens et terroriser nos enfants."
            jump menu_rencontre_moira_blesse

        "Qui es-tu ?":
            e "Qui es-tu ? Je t'ai déjà rencontré ?"
            m "Je suis Moira, fille d'Ogma. Celui que l'on surnomme \"Le Hurleur\"."
            m "J'étais à Perth lorsque vous êtes arrivés pour menacer nos anciens et terroriser nos enfants."
            e "J'aurais probablement dû t'accorder plus d'attention..."
            m "Ne me tutoyez pas."
            jump menu_rencontre_moira_blesse

        "Où sommes-nous ?":
            e "Où sommes-nous ? "
            m "Nous sommes à Perth. Cette maison appartient à mon père."
            m "Vous devriez vous habituer. Vous allez passer un certain temps ici."
            e "Pourquoi ?"
            m "Vos blessures sont graves. Une infection a déjà commencé à attaquer votre cuisse. Il vous faudra plus d'un mois pour vous remettre."
            jump menu_rencontre_moira_blesse

        "Arrière ! Laisse-moi !":
            e "Laisse-moi tranquille ! Où est Ogma ? Je veux sortir d'ici !"
            m "Du calme, du calme."
            m "Je n'ai aucune intention de vous faire du mal."

        "Faire une allusion sexuelle sarcastique":
            e "La situation est assez... satisfaisante. Je n'ai encore jamais été pris au piège par une jolie jeune fille comme ..."
            "* Moira s'approche et assène un violent coup de pied dans le genou d'Einar, sans qu'il ne puisse de défendre.*"
            m "A l'avenir, vous éviterez ce genre de... choses. Soyez correct avec moi et je serai correcte avec vous."

    "*Moira broie quelque chose avec un pilon*"

    menu:

        "Que fait-elle ?":
            e "Qu'est ce que c'est ? Qu'est-ce que vous faites ?"
            m "Je broie des plantes pour vous."
            e "Pour moi ?"
            m "Oui ! C'est du millepertuis, mélangé avec d'autres herbes."

        "Ne rien dire":
            e "..."
            m " Vous pouvez parler, j'ai le droit de vous répondre."
            e "..."
            m "J'imagine que vous ne dites rien par fierté ? Ne soyez pas idiot. Vous vous doutez que ce que je prépare vous est destiné !"
            e "Qu'est-ce que c'est ?"

        "Trait d'humour":
            e "J'ai encore mes dents, je n'ai pas besoin que l'on broie ma nourriture."
            m "... *elle esquisse un sourire fugace*"
            m "Ce n'est pas de la nourriture !"

        "Pas faim":
            e "Je n'ai pas faim, merci."
            m "... *elle esquisse un sourire fugace*"
            m "Ce n'est pas de la nourriture !"

    m "Je vous prépare un onguent, pour l'infection de votre cuisse."
    e "Un onguent ?"
    m "Soyez rassuré : c'est un ancien qui m'a donné les plantes, et il ne se trompe jamais !"
    e "Mmmh..."
    m "C'est mon père qui m'a demandé de vous soigner. Quand vous le verrez, essayez de vous montrer reconnaissant."

    menu :
        "La remercier":
            e "Merci. Je ne m'attendais pas à être soigné ici."
            m "Ce n'est pas moi que vous devez remercier, je ne fais que suivre les instructions de mon père."
        "Ne rien dire":
            e "..."
            m "..."
        "Pas de besoin d'attention":
            e "Je n'ai pas besoin des soins d'une rebelle. J'ai supporté des blessures plus terribles sans être soigné !"
            m "Vous êtes ridicule. Vous voulez que je vous laisse comme ça ? Dès ce soir vous serez tremblant de fièvre, et demain vous serez déjà mourant."
            m "Mais allez- y ! Allez vous promener dehors ! Ah, j'oublais, vous n'en avez pas le droit et vous êtes entravé."
            m "Laissez-moi faire ce qu'on m'a demandé. J'essaie de ne pas être désagréable, faites en autant."

    o "Alors ? Comment va le prisonnier ?"
    m "Plutôt bien ! Il a une infection à la jambe mais le vieux Murray m'a donné des plantes pour le soigner. D'ici une semaine, l'infection sera passée."
    o "Et l'épaule ?"
    m "La cicatrisation commence à peine, la blessure était profonde. Le vieux m'a aidé à extraire la tête de la flèche de son épaule, j'ai bien cru qu'il allait se vider de tout son sang !"
    e "Je ..."
    o "Tais-toi. Moira, finis les soins et rejoins moi dehors."

    hide ogma normal

    menu :
        "Un problème ?":
            e "Il a une dent contre moi ?"
            m "Pas contre vous en particulier, non."
        "J'aurais dû mourir...":
            e "J'aurais mieux fait de mourir avec les autres."
            m "Estimez-vous heureux d'être en vie. Il voulait tous vous tuer."
            e "Pourquoi cette colère contre nous ?"
            jump interieur_maison_village_2
        "Critiquer":
            e "Quel enfoiré ! Il ne m'a même pas adressé la parole !"
            $ critique_ogma = True
        "Il devrait avoir honte":
            e "A sa place, moi aussi j'aurais honte de m'adresser au chef d'une troupe assassinée lâchement au détour d'un sentier obscur. Bandits de grands chemins !"
            $ critique_ogma = True

    if critique_ogma:
        "*Moira gifle Einar*"
        m "C'est la dernière fois que vous manquez de respect à mon père. Ou bien vous irez vous faire voir dans l'enclos des boucs."

        menu :
            "Ne rien dire":
                e "..."
                m "Je n'agis pas par caprice, si c'est ce que vous pensez. Vous nous devez plusieurs vies."
                e "Plusieurs vies ?"
                m "La votre, dans un premier temps."
                e "Et ?"
                m "Et celle de Kennocha, ma mère."

            "Demander pardon":
                e "Excusez-moi."
                m "N'en parlons plus."
                e "..."
                m "Je n'agis pas par caprice, si c'est ce que vous pensez. Vous nous devez plusieurs vies."
                e "Plusieurs vies ?"
                m "La votre, dans un premier temps."
                e "Et ?"
                m "Et celle de Kennocha, ma mère."

            "Macho":
                e "Je n'ai pas d'ordres à recevoir d'une fifille à papa."
                "* Moira gifle Einar à nouveau, sur l'autre joue.*"
                m "J'ai omis de préciser que vous me deviez aussi le respect."
                m "Je n'agis pas par caprice, si c'est ce que vous pensez. Vous nous devez plusieurs vies."
                e "Plusieurs vies ?"
                m "La votre, dans un premier temps."
                e "Et ?"
                m "Et celle de Kennocha, ma mère."

    m "J'imagine que si le roi est venu en Ecosse, c'est pour punir ceux qui ont tué son intendant ?"
    e "Oui."
    m "Savez vous seulement pourquoi nous l'avons tué ? Je suis certaine que la question ne vous a même pas effleuré."
    e "Le roi nous a demandé de mater la rébellion et de venger l'intendant Montgomery. Le reste ne nous regarde pas."
    m "Montgomery méritait de mourir !"
    e "Qu'est-ce qui vous a donné le droit de le tuer ?"
    m "Il a tué ma mère, Kennocha."
    e "..."
    m "Clyde Montgomery n'était pas intendant. C'était un porc, doublé d'un tortionnaire ! Il saignait l'Ecosse à blanc ! Il exigeait de nous plus que ce que nous avions !"
    e "Quel rapport avec votre mère ?"
    m "Un matin, l'intendant est arrivé accompagné de ses sous-fifres. Il a exigé qu'on lui donne immédiatement l'impôt ainsi que de la nourriture pour ses hommes."
    m "Nous avons rassemblé tout ce que nous pouvions et le leur avons donné. Il ne nous restait presque rien."
    m "Montgomery n'était pas satisfait, et il a demandé à ses gardes de fouiller nos maisons."
    m "Ils ont découvert une réserve de nourriture que ma mère avait dissimulé. Sans rien dire, Montgomery s'est approché de ma mère et l'a tuée devant tout le village, sur la place."
    m "\"Ne me cachez rien, jamais.\" J'entends encore sa voix. Tous ceux qui ont essayé de sauver ma mère ont été tabassés, personne n'a pu faire quoi que ce soit."
    e "Où étiez-vous ? Où était votre père ?"
    m "J'étais parmi ceux que les gardes ont frappé. Quand j'ai vu ma mère tomber, j'ai voulu me jeter sur l'intendant. Je n'ai même pas pu passer ses gardes."
    m "Quand mon père est revenu, il a franchi le cercle que formaient les gens du village. Personne ne parlait. Il revenait de la rivière avec quelques prises du matin."
    m "A ce moment là, Montgomery était déjà parti. Mon père a retrouvé ma mère allongée dans la boue et dans son sang, devant tout le monde."
    m "La suite, vous la connaissez."
    e "Alors c'est Ogma lui-même qui a assassiné l'intendant..."
    m "Oui. Et je l'y ai aidé. Le garde qui m'avait frappé, je lui ai tranché la gorge. Il pleurait."
    e "..."
    m "Mon père n'est pas une mauvaise personne. Il a tué l'intendant de plein droit."
    e "..."
    e "Pourquoi toutes ces révélations ?"
    m "J'estime que vous avez le droit de savoir pourquoi vos hommes sont morts, et pourquoi vous allez trahir le roi."
    m "Je vais vous laisser. Je reviendrai demain changer vos bandages."



    jump interieur_maison_village_2

#Sequence 2
label interieur_maison_village_2:
    scene bg house2_night with dissolve
    "*Quelques jours plus tard...*"

    m "Bonjour ! Je viens changer vos bandages."
    e "Bonjour."

    menu:

        "Appelle moi Einar":
            e "Après ces quelques jours passés ensemble, plus la peine de me parler comme à un étranger. Appelez moi-Einar"
            m "Alors parle moi comme si j'étais ton amie."
            e "Très bien, Moira."

        "Remercier":
            e "Merci."
            m "Pour ?"
            e "Les soins, les bandages, tout."
            m "Vous n'allez pas me remercier à chaque fois que je viens m'occuper de vous ! "
            e "Je vous suis redevable !"
            m "..."
            e "Oui ?"
            m "Je suis lasse de devoir m'adresser à vous comme à un prisonnier."
            e "Alors appelez moi Einar."
            m "Parlez-moi comme vous le feriez à une amie."
            e "Très bien ! Alors voilà : je te remercie pour tes soins, Moira !"
            m "C'est mieux comme ça..."
            e "Quelque chose ne va pas ?"
            m "Non, tout va très bien, au contraire !"
            e "Tu en es certaine ?"
            m "Oui ! Ça va te sembler bizarre, mais j'apprécie ces moments."
            e "De quoi tu parles ?"
            m "Les moments où je te soigne. Pendant ce temps, je ne pense pas au reste. Ça me change les idées !"
            e "Tu te distrais en changeant les bandages souillés d'un prisonnier de guerre ?"
            m "Je préfère encore ça plutôt que de m'occuper des bêtes, bien que ce ne soit pas si différent !"

        "Faire de l'humour":
            e "Pas la peine d'insister : je ne suis toujours pas interessé !"
            m "Ne soit pas idiot !" #Elle sourit discrètement
            e "Tiens ? On se tutoie maintenant ?"
            m "Oui. J'en ai assez de devoir te parler comme à un étranger."
            e "Ça me va !"

    "* Les bandages d'Einar sont remplacés.*"
    m "Je vais te laisser, c'est tout pour aujourd'hui."
    e "A demain ?"
    m "A demain."

    jump interieur_maison_village_3

#Sequence 3
label interieur_maison_village_3:
    scene bg house2_jour with dissolve
    "Quelques semaines plus tard..."
    o "... je la voyait se débattre comme jamais une truite ne s'était débattue ! Je tire sur la ligne en essayant de la remonter, mais ce foutu poisson passe derrière un rocher : la ligne casse !"
    m "A ce moment là je saute dans la rivière depuis la berge !"
    o "Ta mère était folle ! Elle était persuadée que tu allais te noyer ! L'eau était vive et glacée, c'était au début du printemps."
    m "Et j'ai bien cru me noyer aussi !"
    o "On ne voyait plus que tes cheveux hors de l'eau ! Tu as dérivé sur une vingtaine de mètres, et puis tu as levé tes bras hors de l'eau !"
    m "Je tenais la truite au-dessus de moi ! Elle était énorme !"
    o "Pas si grosse que ça, mais tu étais à peine plus grande qu'elle, ha ha !"
    o "Ensuite ta mère t'a sortie de l'eau. Tu étais toute bleue, mais tu ne voulais pas lâcher le poisson ! On t'a ramenée à la maison et tu n'as lâché la truite qu'une fois rentrée !"
    m "J'aimerais retourner pêcher..."
    o "Pas pour le moment. Nous avons des choses à régler d'abord..."
    e "Logan aussi était un bon pêcheur..."
    o "D'où venait-il ?"
    e "D'Aberdeen, loin au nord."
    o "Je n'y suis jamais allé... Et vous Einar, vous n'avez rien à raconter ? D'où venez-vous ?"

    menu :

        "Être agressif":
            e "Ça ne vous regarde pas, salopard. Vous avez tué mes hommes et Logan."
            m "Einar !"
            "*Moira lève la main et s'apprête à gifler Einar. Ogma l'interromp en saisissant son bras au vol.*"
            o "Non... Laisse-le dire. Il n'a pas tort. J'ai tué ses amis."
            m "Mais il t'a insulté !"
            o "Il n'est pas responsable de grand chose dans cette histoire. Il a suivi les ordres de son roi."
            m "..."
            e "..."
            "Moira s'emporte et s'apprête à gifler Einar. Ogma l'interromp, et explique que le viking n'a pas totalement tort."
            "Il n'est pour rien dans cette histoire et n'a fait que suivre son roi."

        "Nostalgie de la Norvège":
            e "Je viens de Norvège. Le pays me manque..."
            m "A quoi ça ressemble, la Norvège ?"
            e "Ce n'est pas si différent de l'Ecosse. Nous avons le même climat, peut être un peu plus froid. Et il y a de grands fjords."
            o "Des fjords ?"
            e "Des rivières et des fleuves encaissés dans des vallées. C'est très beau."
            m "J'imagine..."
            e "Lorsqu'on va loin au nord, la nuit, on peut voir de grandes lumières vertes ou rouges dans le ciel. Certains disent que sont des hommages divins pour les héros morts au combat."
            m "J'aimerais beaucoup voir ça, un jour..."
            m "Tu as une femme, là-bas ? Une famille ?"
            e "Non. Je n'ai plus personne."

        "Éluder la question":
            e "Je ne souhaite pas en parler."
            o "Je comprends."
            m "..."

    vm "Ogma !"
    o "Fenella ? Quelque chose ne va pas ?"
    vm "Dunfermline a brûlé ce matin !"
    o "Le roi... Je ne suis pas surpris."
    e "Vous n'avez pas l'air affecté par la nouvelle !"
    m "Stirling et Falkirk ont déjà été rasée il y a quelques jours. Le roi est en marche."
    o "Depuis que vous avez été capturé, Harald n'a pas cessé de vous chercher. Nous avons déjà eu la visite d'un émissaire."

    menu :
        "Compatir":
            e "Je regrette. Ces gens étaient innocents. Harald avait pourtant dit qu'il ne voulait pas lancer d'attaques au hasard..."
            o "Merci. Je ne pense pas qu'il s'agisse d'attaques aveugles. Le roi a décidé de tuer des innocents pour nous faire sortir de nos cachettes et provoquer le rejet du peuple."
            m "Le roi aurait trahi sa parole, Einar ?"
            e "Ce n'est pas dans ses habitudes. Mais il y a peut-être été poussé. Ces massacres ne devraient pas avoir lieu. Je regrette sincèrement d'avoir amené la mort dans mon sillage."
            m "..."
            o "Vous êtes quelqu'un de juste, Einar. Vous n'êtes pas responsable de ce qui se produit."

        "Ne rien dire":
            e "..."
            o "Votre silence vous honore. Je comprends que vous ne vouliez pas prendre parti, votre position est délicate."

        "Se montrer heureux":
            e "Harald est à ma recherche. Bientôt, je serai libre. Ces massacres ne sont que les signes annonciateurs de ma libération."
            o "J'ai cru que vous étiez quelqu'un de juste. Je me trompais probablement. Vous me dégoûtez."

    m "Le roi ne risque pas d'arriver ici sous peu ?"
    o "Non, tout a été prévu. Hier, j'ai demandé à mes hommes d'accomplir deux choses : la première était de tenter d'assassiner l'ami du roi dans son propre château, l'évêque Patrick d'Edimbourg."
    o "La seconde était de brûler les navires par lesquelles les troupes vikings sont arrivées."
    o "L'assassinat aura lieu ce soir. Quant à l'incendie des navires, il aura eu lieu d'ici deux jours. Les délais sont très courts, mais cela devrait obliger Harald à reculer pour quelques temps."
    e "Il va vouloir consolider ses forces au château. Votre assaut n'en sera que plus difficile."
    o "Je n'avais pas le choix ! Sans ces décisions, les troupes du roi seraient arrivées ici après-demain au plus tard."
    o "Nous allons vous laisser. Reposez-vous."
    m "..."

    jump interieur_maison_village_4

#Sequence 4
label interieur_maison_village_4:
    scene bg house2_jour with dissolve

    $ libre_ask = False
    $ trahir_talk = False
    $ decevoir_moira = ""

    "Deux semaines plus tard..."

    "*Moira arrive dans la chambre, un couteau à la main.*"
    m "Bonjour, Einar."

    menu menu_moira_couteau:
        "Ne rien dire" if libre_ask == False:
            e "..."

        "Je suis libre ?" if libre_ask == False:
            e "Tu vas me libérer ?"
            m "Non. Je vais accomplir ce que mon père aurait dû faire depuis longtemps..."
            e "Au secours ! A moi !"
            $ libre_ask = True

        "Appeler des secours":
            e "À l'aide ! Elle va me saigner !"
            m "Mais non ! Calme toi. Je n'ai pas prévu de saigner qui que ce soit aujourd'hui !"

        "Humour":
            e "Mmmh... Notre relation manquait un peu de piment. Des accessoires ne seront pas de trop..."
            m "Ne dis pas de choses pareilles ! " #elle sourit

        "Inquiet":
            e "Alors c'est la fin ? Pourquoi aujourd'hui ? Pourquoi m'avoir soigné pendant toutes ces semaines ?"
            e "Ça n'a pas de sens !"

    if libre_ask:
        m "Ha ha ha, je viens bien te libérer, idiot ! Je n'ai aucune intention de te faire mal. Pour le moment !"

    m "Mon père a demandé à ce qu'on te rende ta liberté de mouvement. Il a dit que tu devais te dégourdir un peu les jambes : il ne faudrait pas que tu sois affaibli pour les combats à venir."
    e "Je n'ai pas vu l'extérieur depuis un mois..."
    m "Sortir te fera du bien ! Tu es encore plus pâle qu'au moment où tu es arrivé ici."

    menu:
        "Il y a un piège ?":
            e "Où est le piège ? Ça me semble trop beau..."
            m "Il n'y a pas de piège !"

        "Humour":
            e "Je suis déçu qu'il ne s'agisse pas d'un \"jeu\"... Tu ne veux pas me torturer un peu ?"
            m "Arrête, ça devient gênant !" #elle sourit

        "Craintes d'Ogma ?":
            e "Ton père ne se méfie pas ? Je pourrais m'échapper..."

    m "Mon père a choisi de te faire confiance. Tu pourras aller dehors, mais tu ne sortiras pas du village à moins de recevoir une autorisation directe. Et tu devras être accompagné en permanence !"
    m "Je suis heureuse de voir que ton état s'est bien amélioré. Je ne te cache pas que j'ai eu des doutes au début !"
    e "C'est rassurant..."
    m "D'ici peu de temps, tu seras complètement remis."

    menu :

        "Parler de trahir Harald":
            e "Et je serai tenu de trahir mon roi à ce moment là..."
            m "Oui... Tu as fait une promesse Einar. Nous comptons tous sur toi."
            e "..."
            m "Je me demande... Que comptes-tu faire après avoir tenu ta promesse ? Après avoir trahi Harald ?"
            $ trahir_talk = True

        "Grâce à Moira":
            e "Grâce à toi, Moira !"
            m "..." # elle sourit
            m "Je n'ai fait qu'une partie du travail. Tu es solide ! Ton corps à largement participé à l'efficacité de mes soins."

        "Ne rien dire":
            e "..."
            m "C'est tout ? Je m'attendais à des remerciements, à de l'enthousiasme ! Tu n'as pas envie d'aller dehors ?"
            e "Si, si..."

        "Sortir ?":
            e "On peut sortir maintenant ? La lumière du jour me manque."
            m "Bien sûr ! Reste près de moi." # elle sourit


    if trahir_talk:
        menu:

            "Arrêter d'être soldat":

                e "J'abandonnerai la carrière militaire. Je rentrerai en Norvège. J'en ai assez de servir les autres."
                e "On m'a promit des récompenses, des terres. Je n'ai rien eu de tout ça. Seulement la mort de mes compagnons. Et j'ai été estropié ! Passé un certain temps, la gloire ne suffit plus."

                $ decevoir_moira = "partir"

            "Aller dans une région plus chaude":
                e "Je partirai dans une région plus chaude. La méditerranée, peut-être. Je n'ai plus ma place auprès du roi, et je ne veux pas rester ici."
                e "L'éloignement est sûrement ma seule option : autant aller sous de meilleures latitudes."
                $ decevoir_moira = "partir"

            "Rester ici":
                e "Je vais rester ici. Je n'ai plus ma place en Norvège ni ailleurs. Harald me traquera partout où il le pourra. Je suppose que mon seul abri sera l'Ecosse."
                m "Si tu réussis, nous serons heureux de te compter parmi nous. Allez, il est temps de sortir !"

            "Ne sais pas":
                e "Je ne sais pas. J'ai besoin de temps pour y réfléchir..."
                m "Je comprends."
                $ decevoir_moira = "rien"

        if decevoir_moira == "partir":
            m "Oh... Tu pourrais rester ici ? Je pense que les gens accepteraient ta présence si tu participais à la vie du village."
            e "Je ne sais pas..."
            "*Moira est visiblement déçue.*"
            m "Suis-moi, je vais te montrer l'extérieur."

        elif decevoir_moira == "rien":
            m "J'espère que tu trouveras vite la réponse. Une fois que tu seras parti pour le château, tu seras au pied du mur..."
            e "Qu'est-ce que tu voudrais, toi ?"
            m "Ce n'est pas à moi de te dire ce que tu dois faire. J'aimerais juste savoir que tu es en sécurité. Le roi voudra se venger de toi."
            e "Où pourrais-je aller ? Harald domine le monde."
            m "Tu pourrais rester ici. Tu vivrais avec nous..."
            e "..."
            m "Je en veux pas te gêner, excuse-moi. Allez, il est temps de sortir !"

        else:
            "Le visage de Moira s'illumine et elle se fend d'un sourire discret"

    m "Viens !"
    "*Moira entraîne Einar a l'extérieur en lui tenant la main*"
    jump village_2

#Sequence 5
label village_2:
    scene bg village2_jour with dissolve

    vm "... et il faudra que tu penses à rentrer les bêtes plus tôt !"
    vm "Mamie ! J'ai trouvé un caillou qui brille !"

    "*Les villageois remarquent à peine la présence d'Einar.*"

    menu :
        "Être sarcastique":
            e "Pas d'applaudissements ? Pas d'ovation populaire ? C'est ainsi que le bon peuple accueille le héros qui doit le libérer du joug du terrible roi-empereur ?"
            m "Ha ha ha ! Ne soit pas trop exigeant ! Tu auras un accueil princier une fois que tu auras fait partir Harald !"
            e "Des encouragements auraient été enthousiasmants."

        "Ne rien dire":
            e "..."
            m "On dirait que voir l'extérieur et le village ne te fait pas plus d'effet que ça... J'imagine que tu ne réalises pas vraiment que tu as recouvré une partie de ta liberté."
            e "C'est sûrement ça..."

        "Être agressif":
            e "Les paysans n'ont pas changé depuis la dernière fois. Mêmes odeurs, mêmes têtes d'abrutis consanguins."
            m "Ces gens sont ma famille et mes amis. Un peu de reconnaissance pour ceux qui t'ont soigné, nourri et abrité pendant tout ce temps ne serait pas de trop."
            e "Je n'ai vu qu'une seule personne me soigner, et c'était toi."
            m "Peut-être. Mais ta nourriture venait bien de ces gens. Et les herbes et remèdes que je t'ai administré m'ont été conseillés par le vieux Murray."
            m "Tu dois quelque chose à chacune de ces personnes."
            e "Tu salueras le vieux Murray de ma part, alors..."

        "Où est Ogma ?":
            e "Ogma n'est pas ici ?"
            m "Non, mon père est parti hier soir du village."
            e "Pourquoi ?"
            m "Je ne sais pas vraiment... Je crois qu'il est parti rencontrer les gens de Kircaldy."
            e "Mmmh..."

    m "..."
    m "Je vais te faire visiter Perth. Nous allons d'abord voir Fenella, elle a hâte de te rencontrer depuis qu'elle t'a vu l'autre jour."
    e "Fenella ? La dernière fois, c'était une grosse femme rougeaude qui sentait l'ail. Il s'agit de cette Fenella ?"
    m "Ha ha, oui ! Et je crois bien que tu lui plaît beaucoup ! Elle a perdu son mari il y a quelques années. Il te ressemblait un peu, je crois."
    e "La journée va être longue..."

    jump village_3

#Sequence 6
label village_3:
    scene bg village2_crepuscule with dissolve

    $ einar_raler = False

    m "Alors ? Qu'as-tu pensé de cette première sortie ? Tu as apprécié ?"

    menu :

        "Besoin de bouger":
            e "Oui. Je commençais à être sérieusement engourdi ! Le sensation de l'herbe sous mes pieds... Ça me manquait !"
            m "J'imagine ! Des tas de choses ont dû te manquer pendant que tu étais enfermé ici..."

        "Agréable compagnie":
            e "Oui. Cette sortie est agréable, surtout aussi bien accompagné."
            m "..." #elle sourit
            m "Moi aussi, j'ai apprécié de passer du temps avec toi."

        "Désagréable":
            e "Pas vraiment. Je n'aimais déjà pas l'Ecosse quand j'y ai accosté, et mon opinion n'a toujours pas changé."
            e "D'ailleurs, je crois que personne n'était heureux de venir ici à part Logan."
            e "Et quand je dis heureux, c'est exagéré."
            e "Je pense que l'Ecosse m'insupporte parce qu'elle ressemble beaucoup à la Norvège, tout en n'y étant pas égale."
            e "Ah, si je pouvais retourner là-bas, je..."
            $ einar_raler = True

        "Se plaindre":
            e "Non. Mes blessures me lancent. Et le repas chez Fenella était un enfer."
            m "Tu n'as pas aimé les oatcakes ?"
            e "Non. Cette saloperie était plus sèche que l'Anatolie ! J'ai cru m'étouffer !"
            m "Et le haggis ? Je suis sûre que tu as aimé !"
            e "Pas vraiment."
            m "Pourtant, quand je t'en ai donné alors que tu étais attaché, tu avais l'air d'adorer ça."
            e "Tu les préparais mieux."
            m "Ils étaient préparés par Fenella."
            e "..."
            e "A vrai dire, la seule chose que j'ai apprécié était cette eau de vie que le vieux Murray m'a fait goûter."
            m "Ah ? C'est drôle, c'est la seule chose que je déteste ! L'odeur, le goût..."
            e "Avec quoi a-t-il dit que c'était fabriqué ?"
            m "De l'eau de source et des céréales, de l'orge je crois. C'est son vieux cousin Campbell qui lui en a donné un tonnelet."
            e "Une fois toute cette histoire terminée, j'irai chercher ce fameux cousin ! J'aimerais lui acheter un peu de sa production."
            m "Finalement, cette journée était plutôt agréable !"
            e "Non, je persiste. J'ai detesté le..."

            $ einar_raler = True

    if einar_raler:
        m "Arrête de râler ! Tu auras beau dire ce que tu veux, j'ai bien vu que tu avais apprécié ce que je t'ai montré. "

    m "Avant de te ramener à la maison, j'aimerais te montrer une dernière chose. C'est un endroit que j'aime beaucoup."
    "*Moira prend Einar par la main et l'entraîne derrière elle, sortant discrètement du village.*"


    jump foret_3

#Sequence 7
label foret_3:
    scene bg forest_crepuscule with dissolve

    menu :
        "Destination ?":
            e "Où allons-nous?"

        "Et l'ordre d'Ogma ?":
            e "Et les instructions de ton père ? Je croyais que je n'avais pas le droit de sortir, sauf autorisation spéciale."

        "Être sarcastique":
            e "C'est amusant, ça me rappelle un mauvais épisode de ma vie. Des rebelles écossais attaquaient mes hommes par surprise dans une forêt et..."

    "*Moira demande à EInar de se taire, en mettant un doigt sur sa bouche.*"
    m "Chuuut..."

    jump paradis_foret_1

#Sequence 8
label paradis_foret_1:
    scene bg little_heaven with dissolve

    $ moira_dead = False

    menu :
        "Quel est cet endroit ?":
            e "Où sommes-nous ?"

        "Ne rien dire":
            e "..."

        "Endroit magnifique":
            e "C'est un très bel endroit. Est-ce que..."


        "*Moira pousse doucement Einar contre un arbre.*"
        "*Elle recule de quelques pas, puis se retourne.*"
        "*Elle se dénude lentement devant Einar, sans le regarder.*"

    menu :

        "Tuer Moira":
            e "(Je n'aurai pas deux occasions comme celle là. Je dois rentrer au château et assurer mes arrières.)"
            "*Einar approche silencieusement dans le dos de Moira, puis plaque ses mains autour du cou de la jeune femme.*"
            "*Elle se débat, comprenant qu'elle vient d'être trahie. Sa respiration devient de plus en plus sifflante.*"
            "*Son visage devient violacé et elle se convulse, avant de tomber au sol, inerte.*"
            e "Il est temps pour moi de retrouver les miens."
            $ moira_dead = True
            jump cote_2

        "S'enfuir":
            e "(C'est une occasion en or de s'enfuir.)"
            "*Sans faire craquer la moindre brindille, Einar abandonne Moira au milieu de la forêt, s'éclipsant rapidement sous les frondaisons.*"
            m "Einar ? Einar ?"
            jump cote_2

        "La regarder":
            e "(Comme elle est belle...)"
            "*Moira s'approche sans bruit d'Einar, et commence à lui ôter ses vêtements.*"
            e "Tu..."
            m "Ne dis rien."
            "*Elle embrasse doucement Einar et commence à l'enlacer.*"
            "*Les mains du guerrier parcourent le corps de la jeune femme et ressentent la douceur de sa peau, parfaite.*"
            "..."
            jump village_4

#Sequence 9
label village_4:
    scene bg village2_jour with dissolve

    "*Le lendemain...*"
    o "Vous voilà prêt à partir, Einar."
    e "Je pense être prêt, oui. Retrouver mes affaires me fait du bien."
    o "Avant de vous souhaiter bonne route, je veux vous rappeler quelque chose. Vous nous avez fait une promesse."
    o "Nous vous avons soigné, nous nous sommes occupé de vous. Vous nous êtes redevable. Remplissez votre part du marché."
    o "Lorsque l'assaut aura commencé, je mènerai mes hommes au combat. Lorsque vous entendra deux coups de cor successifs, vous ouvrirez le pont-levis du château."

    menu:

        "Tenir sa promesse":
            e "Je sais ce que j'ai à faire. Je ne pense qu'à ça depuis plus d'un mois."

        "Tenir sa promesse à contrecoeur":
            e "Je vous suis reconnaissant pour tout ce que vous avez fait. J'accomplirai ma promesse, même si ce n'est pas de gaieté de coeur."

        "Acquiescer":
            e "Très bien."

    m "Tu as donné ta parole à mon père. Je considère que tu m'as également donné ta parole. S'il te plaît, ne me déçois pas..."
    "*Moira s'approche d'Einar.*"

    menu :

        "L'embrasser":
            "*Einar embrasse doucement Moira en caressant son visage*"

        "La serrer contre soi et la rassurer":
            "*Einar saisit Moira par les hanches et l'attire contre lui, puis l'enlace.*"
            e "Ne t'inquiète pas. Je reviendrai."

        "L'ignorer":
            "*Einar se retourne et, sans un regard pour la jeune femme, commence à s'éloigner."

    jump sentier_foret_1


#Sequence 10
label sentier_foret_1:
    scene bg sentier_jour with dissolve
    "..."
    "(Tout ce temps passé à Perth avec ces gens, avec Moira... Ils ont été bons pour moi. Mais je ne peux pas oublier le massacre, l'embuscade, Logan. Quoi qu'il arrive, je devrai trahir l'une des paroles que j'ai donné.)"

    menu :
        "Fidélité à Harald":
            e "(Harald est mon seigneur et celui de tout le monde connu, y comprit les rebelles. Je lui dois tout depuis de très nombreuses années. Le trahir est impensable.)"
        "Penser aux terre promises":
            e "(Le roi m'a fait miroiter des terres et des richesses depuis si longtemps... Sans jamais récompenser mes efforts à leur juste valeur. Pourquoi respecter mes engagements pour un roi qui ne respecte pas les siens ?)"
        "Oppression des écossais":
            e "(Ces gens vivent dans la pauvreté et n'ont fait que se défendre face à un oppresseur. Ils m'ont sauvé. Mais le meurtre lâche de mes hommes et de Logan...)"
            e "(Tout ceci n'a été qu'un enchaînement malheureux d'événements qui n'arrangent personne. Le seul vrai coupable, c'était l'intendant Clyde Montgomery. Et il est mort.)"

    jump foret_5

label foret_5:
    scene bg forest_night with dissolve

    "(Moira a fait beaucoup pour moi, quoi qu'elle en dise. Je n'avais pas rencontré une aussi bonne personne depuis longtemps...)"

    menu:
        "Reconnaissant":
            e "(Elle s'est occupée de moi pendant plus d'un mois, sans jamais se montrer lasse ni désagréable. Je lui dois beaucoup. Elle s'est attachée à moi. La décevoir serait terrible. )"
        "Ogma le lui avait demandé":
            e "(Elle ne s'est occupée de moi que parce que son père le lui avait demandé. Je me demande si notre petite escapade en forêt était aussi une idée de son père...)"
        "Rien qu'une amourette":
            e "(J'ai bien profité d'elle. Elle a été attentionnée avec moi, bien que naïve. Mais ce n'est pas la première femme que je rencontre... Cette petite histoire ne représente que peu de choses face aux engagements d'un huscarl.)"

    jump cote_1

#Sequence 11
label cote_1:
    scene bg cote1 with dissolve

    "(Les événements à venir risquent de bouleverser l'équilibre du monde... Est-ce que la liberté d'un petit nombre de paysans peut prévaloir sur le futur de peuples entiers ?)"

    menu :

        "Chute d'un empire":
            e "(Trahir Harald entraînera la mort d'un nombre incalculable d'hommes et de femmes. Le pouvoir de Harald vacillera en même temps que la stabilité politique du plus grand Empire connu.)"
            e "(Ce sera la porte ouverte à toutes les guerres, et des petits seigneurs ne tarderont pas à se comporter en vautours en se nourrissant sur la carcasse de l'empire décadent...)"
        "Je serai un paria":
            e "(En trahissant Harald, je m'expose à des représailles incessantes. Je serai traqué partout dans l'Empire. Mon seul abri sera l'Ecosse. D'un autre côté, je serai enfin suffisament riche pour avoir la vie que mon roi m'a promise depuis déjà longtemps... Pourvu qu'Ogma respecte sa parole, lui !)"
        "Il en va de ma vie":
            e "(Je n'ai pas d'autre choix que de faillir à ma promesse envers les rebelles. Ma vie en dépend, ainsi que celle de beaucoup d'autres. Tant pis pour la liberté de quelques paysans. Mais qu'arrivera-t-il à Moira ?)"

    jump cote_2

#Acte 3

#Sequence 1
label cote_2:
    scene bg mer with dissolve

    show einar serious at center with dissolve

    e "Hummmm me voilà tout près du chateau"
    e "Que vais-je faire?"
    e "Trahir mon roi ? Non impossible, je suis à ses côtés depuis bien longtemps"
    e "Mais d'un autre côté, celà fait un moment qu'il m'a promit des terre"
    e "Et jusquà aujourd'hui, je les attends toujours."
    e "hummm, j'attends d'être là-bas avant de prendre une décision"
    jump exterieur_chateau_1

#Sequence 2
label exterieur_chateau_1:

    scene bg pont_levis with dissolve

    show einar serious with moveinleft
    show garde_chateau normal at right with dissolve

    e "Me voici enfin arrivé au chateau"
    e "(Devant le pont-levis, deux gardes me font obstruciton)"

    gc "Je te reconnais, Einar, çà Harald ne croyait plus en ton retour"
    gc "Qui plus est, tu es tout seul"
    gc "Comment ça se fait ?"

    menu :
        "Que dois-je dire"

        "Pousse-toi":
            e"Écarte-toi, Geir! Je dois parler au roi immédiatement"
        "Explications vagues":
            e "Il m'est arrivé toutes sorte de chose que toi même tu ne comprendrais pas"
        "Menacer":
            e "Laisse-moi passer, andouille. Je fais partie de cette armée depuis plus longtemps que toi. Et je suis huscarl !"

    gc "D'accord, entre"

    hide garde_chateau with dissolve

    jump cours_chateau_1

#Sequence 3
label cours_chateau_1:

    scene bg cours_chateau with dissolve

    $ retour_silence_1 = False
    $ soupcon_harald_1 = False
    $ mentir_harald_1 = False
    $ interpose_bucher = False

    show einar serious at center with dissolve

    e "Me voilà enfin entré dans le chateau"
    e "Harald est en train de discuter avec un aute huscarl"
    e "Il m'a vu, se dirige vers moi"
    e "J'espère qu'il va être doux"

    show einar serious at left
    show harald normal at right

    menu:
        "Que devrais-je lui dire"

        "Content d'être rentré":
            e "Quel plaisir de vous retrouver, mon roi !"

            h "Tout le plaisir est pour moi, je croyais ne plus revoir un des mes meilleurs huscarls"

        "Peur de ne pas revenir":
            e "J'ai bien cru ne jamais revenir"

            h "Eh bien après tous ce temps, on te croyais mort"
            h "C'est pour celà que j'ai envoyé quelques expéditions punitive afin de te venger"

            e "Il ne fallait pas, ce n'est que trop d'honneur"

        "Ne rien dire":
            e "..."
            h "Je suppose que tu dois être fatigué depuis tout ce temps"

    h "Mais dis-moi, qu'est-ce qui t'est arrivé?"
    h"Et l'escorte qui t'accompagnais ?"
    h"Logan n'est pas là non plus"
    h"Mais bon sang, raconte-moi tout !"

    menu:
        "Que devrais-je dire ?"

        "Dire ne rien savoir":
            e "Je ne sais pas. J'ai été assommé. A mon réveil, il n'y avait plus personne et j'étais abandonné au fond d'un fossé."
            h"Admettons mais qui t'a soigné ?"
            jump menu_assome_cours_chateau

        "Raconter l'embuscade":
        #modifaction pour indiquer le lieu par la suite
            e "Il nous prit au dépourvu, le soir dans la forêt en continuant vers le nord"
            h"Admettons mais qui t'a soigné ?"

            jump menu_embusscade_ou_silence_cours_chateau

        "Ne rien dire":
            h"Eh bien, je t'ai connu plus bavard"
            h"Parles et nous pourrons venger les morts"

            $ retour_silence_1 = True

            jump menu_embusscade_ou_silence_cours_chateau


    menu menu_assome_cours_chateau:

        "Je me suis débrouillé":
            e "Je me suis remis, lentement mais surement, dans la nature."
            $ soupcon_harald_1 = True

        "Aide":
            e "J'ai été soigné par un vieux paysan."

    menu menu_embusscade_ou_silence_cours_chateau:

        "Village et Moira":
            e "J'ai été aidé par un village écossais"
            e "Un femme du non de Moira m'a soigné"
            e "J'ai fini par m'enfuir"

        "Aide":
            e "J'ai été soigné par un vieux paysan."

        "Perte de mémoire" if retour_silence_1:
            e "Tout ce dont je me souviens, c'est l'attaque et que j'ai été bléssé"
            e "Après, tout es flou"
            e "Je me suis réveillé il y a peu et mes blessures étaient soignés"
            $ soupcon_harald_1 = True

    "Harald se mon soupconeux"

    h "J'espère que tout ce que tu me dis est vrai"
    h "Parce que tu sais très bien ce qu'il en coute de me trahir"
    h "Mais j'espère pouvoir te faire confiance mon ami"

    menu :
        "C'est le moment ou jamais de dire la vérité"
        "Dire vérité":
            e "Mon Roi, j'ai été recceuilli par les sauvages uniquement pour me convaincre de vous trahir"
            e "Il m'ont forcé à accepter ce pacte"
            e "Mais au fond de moi, je vous ai toujours été fidèle et j'attendais patiemment le jour où je pouvais rentrer pour tout vous dévoiler"
            e "Ogma, chef de l'armée rebelle, veut que je baisse le pont-levis et que je prenne votre hache pour vous affaiblir "
        "Fidèle (mentir)":
            e "Nul ne vous est plus fidèle que moi !"
            $ mentir_harald_1 = True
        "Menti aux rebelles (mentir)":
            e "J'ai rusé en pactisant avec les rebelles uniquement dans le but de revenir à votre service"
            $ mentir_harald_1 = True

    if mentir_harald_1:
        h "Je te remercie Einar pour m'avoir dévoilé leur perfide plan"
        h "Grâce à toi, nous allons pouvoir nous pouvoir nous préparer et réduire la rebellion à néant une bonne fois pour toute"
        h "Tu devrais rejoindre les autres soldats pour te préparé à les acceuillir"

        e "Bien mon Roi"
    else:
        e "Bon j'avoue, je sèche un peu là pour le coup"

        h "J'ai eu des doutes sur toi"
        h "Ne me fait plus jamais peur comme ça"
        h "Les autres vont être content de ton retour"
        h "Vas les rejoindre dans la salle de banquet"

        e "Bien mon Roi"

    "Einar se dirige vers la salle de banquet et vois L'evêque Patrick juger 3 écossais qui sont déjà sur le bûcher"

    hide einar
    hide harald

    show patrick normal at center with dissolve



    p "Que Dieu, est-pitié de vous! Les flammes purificatrices vont laver tous vos pêchés"
    p "Deus propitius tibi!"

    show patrick normal at left
    show prisonnier normal at right with dissolve

    pe3 "Non arretez! Je suis enceinte!"
    pe3 "Même si vous me concidérez comme coupable, vous allez tuer un innocent"

    p "Je n'ai que faire de tes mensonges femme!"
    p "Tout ce que tu veux, c'est m'amener vers le diable"

    hide prisonnier
    show einar normal at left with dissolve
    show patrick normal at right

    menu:
        "(Que devrais-je faire ?)"

        "Arrêter le massacre":
            e "Stop! arretez-tout, ce ne sont que de simples paysans"

            p "Mais dis-moi, Einar, tu es porté disparu pendant presque un mois"
            p "Et te voilà en pleine forme, à défendre ces hérétiques."
            p "Qu'est-ce qui te fait dire qu'ils sont innocents ?"

            $ interpose_bucher = True

            jump menu_sauver_rebelle_cours_chateau

        "Ne rien dire":
            e "..."
        "Brûlez-les":
            e "Vous avez raisons Monseigneur, brûlez-les!"
            e "Brûlez cette racaille"

    if interpose_bucher:


        menu menu_sauver_rebelle_cours_chateau:
            "Parler du village":
                e "Je ne les ai pas vu, lorsque j'étais dans le village"
                e "Ils ne peuvent donc pas être avec les rebelles que nous recherchons"

                if mentir_harald_1 == False and soupcon_harald_1 == False:
                    $ soupcon_harald_1 = True

            "Ils ont l'air innoffencifs":
                e "Je ne sais rien d'eux mais ils n'ont pas l'air méchant"
                e "De plus, je pense qu'une future mère ne mettrait pas la vie de son enfant en danger"

        p "Ne t'interpose pas avec la volonté de Dieu"
        p "Sinon je vais finir par croire que tu es avec eux"
        p "Et tu as sous les yeux le châtiment que nous réservons au traitres!"

        e "Pardonnez-moi pas Monseigneur, je ne v...."

        p "Tu ne voulais pas quoi ?"
        p "Intérompre ma divine mission ?"
        p "Déguerpis avant que je pense que tu sois avec ses hérétiques"

    p "Amenez les torches et faite les bruler"

    pe3 "Non pas ça"
    pe1 "Nonnnnnn"
    pe2 "Arggggg"

    "Pendant que les condamnés sont en train de brûler, Einar regarde autour de lui et peut remarque que certain soldats se réjouissent de voir souffrir des hérétiques"
    "Mais d'autres sont mal à l'aise dont un particulèrement qui semble être sur le point de pleurer"
    "Einar se dirige vers lui"

    #Variable
    $ reponse_reconfort = ""

    menu :
        "Est-ce que j'essaye de lui remonter le moral ou pas"

        "Une bande de porc":
            e "Ha, souris un peu, gamin ! Ecoute leur graisse bouillir, à ces porcs !"
            $ reponse_reconfort = "pleurer"
        "Pas besoin de les pleurer":
            e "Ne pleure pas ces parasites, ils ne le méritent pas."
            $ reponse_reconfort = "pleurer"
        "Tu es impuissant":
            e "Tu n'aurais rien pu faire. L'évêque est un malade sanguinaire."
            $ reponse_reconfort = "larme_aux_yeux"
        "Ne rien dire":
            e "..."
            $ reponse_reconfort = "larme_aux_yeux"
        "L'évêque peut se tromper":
            e "L'évêque peut se tromper, mais pas le Seigneur. S'ils étaient Justes, les condamnés iront au paradis."
            $ reponse_reconfort = "rassure"

    if reponse_reconfort == "pleurer":
        "Le jeune soldat pleure sans se cacher"
    elif reponse_reconfort == "larme_aux_yeux":
        "Le jeune soldat ne change pas d'état"
    else:
        "Le jeune soldat semble rassuré"

    jump cours_chateau_2

#Sequence 4
label cours_chateau_2:

    "Un garde avertit depuis les remparts qu'une horde rebelle vient d'émerger des bois, de l'autre côté de la plaine. Un homme est à leur tête, et porte des peintures bleues. Les rebelles sont plusieurs centaines."
    "Harald demande à ses hommes de se tenir à la grande porte, prêts à la défendre et à empêcher quiconque de pénétrer l'enceinte. Le roi disparaît dans le donjon et va s'équiper pour la bataille."

    jump interieur_grande_porte_chateau_1

#Sequence 5
label interieur_grande_porte_chateau_1:

    "Einar est posté à proximité du système d'ouverture des portes."
    "La horde progresse en courant à travers la plaine. Lorsque les rebelles ne sont plus qu'à une centaine de mètres, un double son de cor retentit : le signal convenu avec Ogma pour ouvrir la porte."

    menu:
        "Dois-je baisser le pont-levis ?"
        "Le baisser":
            if soupcon_harald_1:
                jump bad_ending_3
            else:
                jump pont_levis_baisse

        "Laisser fermer":
            if soupcon_harald_1:
                jump soupcon_harald_defendre_porte
            else:
                jump harald_defendre_porte


#Baisser pont-levis
label pont_levis_baisse:

    "Le pont s'abaisse brutalement, laissant le champ libre aux rebelles pour entrer."
    "Une volée de flèches abat une partie des rebelles qui foncent vers le pont abaissé."
    "Les soldats proches se tournent vers Einar en l'insultant de traître, et s'apprêtent à le massacrer"

    menu:
        "Que dois-je leurs dire ?"

        "Reculez !":
            e "Arrière ! Je vous ferai rendre gorge !"
        "Tactique du roi":
            e "C'était une tactique imaginée par notre roi !"
        "Venez, je vous attends !":
            e "Tuez-moi, chiens. Mieux vaut être un traître qu'un oppresseur."
        "Ne rien dire":
            e "..."

    "Au même moment, la horde rebelle pénètre l'enceinte, ce qui détourne l'attention des soldats qui attaquaient Einar."

    "La bataille commence. La horde avance en une masse compacte et nombre de rebelles succombent sous les flèches des vikings. Le gros des forces parvient à franchir le pont-levis et la masse rebelle déferle dans l'enceinte, ravageant tout sur son passage."

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
