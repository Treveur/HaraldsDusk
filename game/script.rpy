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

#Moira
define m = Character("Moira", color = "#f00")

#Scene
image bg forest = "foret_cabane.jpg"
image bg village = "village.jpg"
image bg mer = "chateau_mer.jpg"

#Fond uni
image bg black = "#000"

# Déclarez les personnages utilisés dans le jeu.



define gv = Character('Guerriers Vikings', color="#e67e22")
define vm = Character('Villageois', color="#3498db")

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

    scene bg forest

    "Dans la forêt Westruther, au coeur de l'Ecosse, une troupe de vikings se dirige vers le chateau de Dunbar pour s'y installer et préparer l'expédition punitive visant à mater les rebelles."

    "A la tête de la cohorte, Harald, roi-empereur des vikings. Il a décidé de venir punir lui-même les insolents ayant osé défier son pouvoir."

    "A ses côtés marche une armée de cent vikings, guerriers et huscarls, impatients d'en découdre : cela fait déjà longtemps qu'ils ne se sont pas battus."

    "Einar est l'un des huscarls : un guerrier d'élite, chef militaire et garde personnel du roi."

    menu:
        "Parler à Harald":
            jump harald_choice
        "Parler à Logan":
            jump logan_choice
        "Ne rien dire":
            jump plaine_1

    show einar serious

label harald_choice:

    show einar serious

    e "Mon Roi, sommes-nous proches ?"

    show einar serious at left
    show harald normal at right with dissolve

    h "Nous n'en avons plus pour très longtemps. Une heure, tout au plus."

    menu menu_harald_choice_foret:
        "Quel est le plan ?":
            jump h_souvenir_bataille

        "Parler de la région":
            jump h_info_region

        "Se montrer enthousiaste":
            jump h_enthousiaste

        "Pourquoi tant de confiance ?":
            jump h_confiance

        "Est-il vraiment nécessaire de massacrer une bande paysans ?":
            jump h_innocents

        "Continuer silencieusement":
            jump plaine_1



label logan_choice :

    show einar serious

    e "Ça va, Logan ? Tu n'as pas desserré les dents depuis Newcastle. "

    show einar serious at left
    show logan fache at right with dissolve

    l "... Je n'ai pas revu l'Ecosse depuis plus de dix ans."

    e "Depuis tout ce temps passé en campagne, j'en avais oublié tes racines."

    l "Je me demande si Aberdeen a beaucoup changé."

    e "La nostalgie de la maison, hein ? Si tu veux, je peux peut-être glisser un mot au roi pour..."

    l "Non, merci. Je ne tiens pas à y retourner."

    menu menu_logan_choice_foret:
        "Se remémorer un bon souvenir":
            jump l_souvenir_bataille

        "Parler de la région":
            jump l_info_region

        "Se montrer enthousiaste":
            jump l_enthousiaste

        "Pourquoi Harald est-il si confiant ?":
            jump l_confiance

        "Est-il vraiment nécessaire de massacrer une bande de paysans ?":
            jump l_innocents

        "Continuer silencieusement":
            jump plaine_1


#Harald
label h_souvenir_bataille :
    e "Quelles sont les instructions, sire ? A quoi devons-nous nous préparer ?"

    h "Tout d'abord, nous allons atteindre le château de Dunbar. Là, l'évêque Patrick d'Edimbourg nous accueillera."

    h "Ensuite je détacherai un groupe d'éclaireurs. Je veux retrouver le village des rebelles le plus vite possible."

    h "Une fois le village retrouvé, j'aviserai. Mais ces foutus écossais n'apprécieront pas ce qui va leur arriver, tu peux me croire."


    jump menu_harald_choice_foret

label h_info_region :
    e "Qu'indiquent les cartes à propos de la région, sire ? Je n'ai pas eu le loisir de les consulter."

    h "Pas grand chose. Des plaines d'herbe rase, des rocailles abruptes, quelques forêts. Et surtout, la mer."

    h "Nous ne sommes encore que dans les Lowlands ; les Highlands sont plus au nord."

    h "La seule différence entre les deux est la quantité de rocaille. "

    e "La région a l'air inhospitalière..."

    h "Sauf pour les moutons. Il y a plus de moutons que d'hommes, par ici. Et quand je parle d'hommes, je suis encore trop élogieux. N'en déplaise à Logan."

    jump menu_harald_choice_foret

label h_enthousiaste :
    e "Sire, il me tarde de massacrer quelques paysans !"

    h "Ha ha ! Ne sois pas si hatif, Einar. Il ne s'agit pas de tuer tout ce qui bouge. Pas pour le moment. "

    e "Sauf votre respect, Sire, votre Hache nous a privé de nombreuses batailles. D'habitude, vos ennemis se rendent dès qu'ils la voient ! Alors un soulèvement paysan, c'est une chance inespérée !"

    h "Ton enthousiasme fait plaisir à voir !"

    jump menu_harald_choice_foret

label h_confiance :
    e "Mon roi, votre présence ici m'intrigue : pourquoi risquer votre vie dans une expedition de moindre importance ? Vous pourriez recevoir une flèche !"

    h "Je suis l'élu divin, Einar. Je porte une relique du Christ. La Hache me rend immortel. Une flèche me ferait rire, rien de plus."

    h "Harald Sigurdsson, roi-empereur des vikings, abattu par une flèche de paysan rebelle ! Ha ha !"

    e "Ha ! Les dirigeants du monde entier craindraient les paysans écossais !"

    jump menu_harald_choice_foret

label h_innocents :
    e "Mon Roi, est-il vraiment nécessaire de tuer des paysans ? Ne pensez-vous pas que de nombreux innocents risquent de perde la vie ?"

    h "Quelle mollesse de ta part, Einar ! Je suis surpris !"

    h "Il n'y a pas d'innocents sur ces terres. En tuant mon intendant, ils se sont attaqués à moi. Ils mourront tous pour l'exemple."

    h "J'ai un message à faire passer au reste du monde. La moindre rébellion entraînera une sanction immédiate, sans distinction."

    e "La mort."

    h "Exactement !"
    jump menu_harald_choice_foret

#Logan
label l_souvenir_bataille :
    e "Tu te souviens de la bataille de Wertheim ?"

    l "L'automne dernier ? Et comment ! Je revois encore les seins de la petite que j'avais attrapé ! J'ai passé une bonne nuit cette fois là !"

    l "Je ne me rappelle même pas de son nom. Dorthe, Dorothe, quelque chose comme ça. Le lendemain, sur le départ, elle a insisté pour que je l'emmène ! La garce ! Ha ha ! "

    e "Tu as toujours de la chance quand il s'agit de dégoter de belles filles. Même au milieu de nul part !"

    l "Remarque, ça fait un moment que je ne t'ai pas vu avec une fille. Pas une captive, rien ! Monsieur cherche le grand amour ? A moins qu'il ne soit plus du genre à embrasser les garçons ?"

    e "Ferme la, sale porc. Quand je passe du bon temps, j'aime que la fille ne sois pas entrain de se débattre."

    l "Chacun son truc !"

    jump menu_logan_choice_foret

label l_info_region :
    e "Tu reconnais la région ?"

    l "Pas vraiment. Aberdeen est bien plus loin au nord, je ne suis jamais venu jusqu'ici."

    l "Cela dit, je ne suis pas dépaysé. La différence entre ici et chez moi, ce sont les montagnes."

    l "Pour le reste, tout est identique : mêmes forêts, mêmes plaines herbeuses. Et la mer."

    l "Quant aux gens qui vivent ici, j'imagine qu'ils sont identiques à ceux d'Aberdeen."

    jump menu_logan_choice_foret

label l_enthousiaste :
    e "Ma hache me démange. Je fracasserais bien quelques crânes."

    l "Moi aussi ! Je ne supporte plus ces voyages interminables. Deux mois que nous n'avons pas combattu ! Et plus d'un an depuis la dernière vraie bataille. Il est grand temps de nous dégourdir un peu !"

    e "Tuer des écossais ne te posera pas de problème ?"

    l "Je n'aurai pas plus de problèmes que toi. Ces gens sont des inconnus, et ils ont tué l'un des vassaux de notre roi. C'est une motivation amplement suffisante pour trancher la tête de quelques compatriotes."

    jump menu_logan_choice_foret

label l_confiance :
    e "Le roi me paraît bien confiant."

    l "Et pourquoi ne le serait-il pas ? Il est le plus grand souverain que le monde connaisse. Il porte une Hache Sainte incrustée des Clous de la Sainte Croix."

    l "Il est immortel et invincible. Une armée de vétérans marche avec lui. S'il y a bien une personne sur cette terre qui puisse avoir confiance en lui-même, c'est notre roi."

    jump menu_logan_choice_foret

label l_innocents :
    e "Je me demande si le massacre de paysans innocents est justifié."

    l "Tu te poses beaucoup de questions. Si notre roi nous le demande, nous le faisons."

    l "Et à titre personnel, tuer des paysans ne me pose aucun problème. C'est un message que nous envoyons à tous les rebelles potentiels : trahissez Harald, et vous verrez vos familles mourir."

    jump menu_logan_choice_foret


#Sequence 2
label plaine_1 :

    scene bg mer

    h "Ha ! Dunbar, enfin. Un bon repas nous attend."

    e "Dois-je envoyer un émissaire annoncer notre arrivée ?"

    h "Non. Je compte sur toi pour autre chose."

    e "Autre chose ?"

    h "Pas de repas pour toi, hélas. J'ai besoin d'envoyer un groupe de reconnaissance à l'avant de l'armée, afin de débusquer le village rebelle."

    h "Je compte sur toi pour diriger la troupe. Tu es un bon meneur d'hommes, et ton expérience du pistage te permettra de trouver les rebelles. Ça ne fait aucun doute !"

    menu menu_harald_eclaireur_foret_1:
        "Je refuse cette responsabilité":
            jump h_refus_village
        "Pourquoi ?":
            jump h_demande_information
        "A quel dangers dois-je m'attendre ??":
            jump h_demande_nb_detachement
        "J'accepte":
            jump h_accepter
        "Avec grand plaisir !":
            jump h_accepter_fayot

label h_refus_village :
    e "Mon roi, je me vois dans l'obligation de refuser cette responsabilité."

    h "Pardon ? C'est un ordre, Einar. Pas une proposition. Ton attitude est décevante."

    e "Pardonnez-moi, sire. "

    jump menu_harald_eclaireur_foret_1

label h_demande_information :

    e "Pourquoi dois-je mener ce groupe de reconnaissance ?"

    h "Parce que je te le demande. Comme je te l'ai dit, je suis convaincu que tes qualités te permettront de mener à bien cette mission mieux que quiconque."

    h "Cette reconnaissance est très importante : elle me permettra de cibler précisément le village à châtier. Nous gagnerons un temps précieux et nous épargnerons les villages n'ayant aucun rapport avec cette rébellion."

    jump menu_harald_eclaireur_foret_1

label h_demande_nb_detachement :

    e "Sire, quels sont les dangers de cette mission ? A quoi dois-je m'attendre ?"

    h "Il n'y a aucun danger. Dans le pire des cas, tu pourrais te faire insulter par une bande de villageois chétifs. Tu mènes un groupe de guerriers vikings. Tu es un huscarl. Rien ne va te résister."

    jump menu_harald_eclaireur_foret_1

label h_accepter :

    e "J'accepte cette mission."

    h "Et j'en suis satisfait. Part dès maintenant : il n'y a pas de temps à perdre. Tu atteindras les premiers villages des Highlands avant la nuit."

    e "Fort bien. "

    jump logan_aide

label h_accepter_fayot :

    e "Comme il vous plaira, mon roi. C'est un grand honneur que vous me faites ! "

    h "Cesse tes flagorneries et part sans tarder."

    jump logan_aide

label logan_aide :

    l "Einar, je t'accompagne ! Mes connaissances de la région ne seront pas de trop, et la vue d'un écossais parmi les vikings rassurera peut-être les villageois. "

    menu:
        "Merci Logan !":
            jump e_reconnaissant
        "Je regrette, mais non.":
            jump e_refus
        "Très bien, puisque tu insistes...":
            jump e_contrecoeur


label e_reconnaissant :

    e "Merci beaucoup Logan. Je suis heureux de pouvoir compter sur toi !"

    l "J'aurais préféré manger à la table du roi ce soir, mais j'avais peur que tu te perdes en forêt !"

    h "Ne vous inquiétez pas. Vous aurez tout les deux de quoi boire et manger une fois revenus ! Maintenant, partez !"

    jump plaine_2

label e_refus :
    e "Non, je refuse. Je n'ai pas besoin de toi, Logan. C'est une mission de reconnaissance : moins nous sommes, mieux c'est."

    l "..."

    h "Ton ingratitude est exaspérante, Einar. Logan t'accompagnera, que tu le veuilles ou non. C'est un ordre !"

    l "Sire, vous..."

    h "Silence. Partez maintenant, ne perdez pas de temps."

    jump plaine_2

label e_contrecoeur :

    e "Très bien... Viens, mais tais-toi. J'en ai assez de voyager à travers tout le continent. Nous accomplissons notre devoir et nous rentrons au château. Arrange-toi pour ne pas me déranger."

    l "Moi aussi, j'aime voyager dans une ambiance chaleureuse !"

    h "Parfait. Je suis certain que Logan saura se montrer utile. Partez, et ne revenez qu'après avoir trouvé les rebelles !"

    jump plaine_2

#Sequence 3
label plaine_2:

    e "Bon les gars, j'ai quelque chose à vous dire"

    menu:
        "Mettre en garde" :
            jump e_mettre_en_garde
        "On s'en branle" :
            jump e_ininteret_mission
        "Motiver les troupes" :
            jump e_motiver_troupe_plaine_2
        "Logan, t'es qu'un PD" :
            jump e_chambrer_logan_plaine_2
        "Bon, les gars, c'est moi qui vous l'dit, descendez d'un étage dans votre tête" :
            jump e_jouer_chef

label e_mettre_en_garde:

    e "Bon faite gaffe"

    gv "ok"

    jump foret_1

label e_ininteret_mission:

    e "A vrai dire, j'en ai rien à faire de cette mission"

    l "Comment oses-tu ?"

    gv "Ouai, c'est pas cool"

    jump foret_1

label e_motiver_troupe_plaine_2:

    e "On va tous les défoncer!"

    gv "Ahou ahou"

    jump foret_1

label e_chambrer_logan_plaine_2:

    e "Logan, t'es vraiment qu'un PD"

    l "Mais euh"

    gv "hahahahah"

    jump foret_1

label e_jouer_chef:

    e "Bon pour cette mission, c'est moi qui commande alors pas de connerie"

    e "Sinon, c'est moi qui encule"

    gv "Ohhhh. :("

    jump foret_1

#Scequence 4
label foret_1:

    e "Bon les gars"

    menu:
        "Se montrer impatient de rentrer en Norvège":
            jump e_impatient_norvege
        "Se moquer de  gens de la région" :
            jump e_se_moquer_foret_1
        "Impatient de terminer la misison" :
            jump e_impatient_mision_foret_1
        "Allez les gars, on se bouge le cul" :
            jump e_motiver_troupe_foret_1
        "Chambrer Logan" :
            jump e_chambrer_logan_foret_1
        "Demander à Logan ce qu'il pense de la mission" :
            jump e_avis_logan_mission_foret_1

label e_impatient_norvege:

    e "Plus le temps passe, plus la Norvège me manque"

    gv "Ouai, moi aussi maggle"

    menu:
        "Je suis préssé de recevoir mes terres promises rapidement":
            jump e_espoir_terre_norvege_foret_1
        "Fermez-là bande de bolosse":
            jump e_ordre_taire_guerrier_foret_1

label e_se_moquer_foret_1:

    e "quel bande de pequenot!"

    jump village_1

label e_impatient_mision_foret_1:

    e "je suis impatient de terminer cette mission"

    jump village_1

label e_motiver_troupe_foret_1:

    e "Allez les gars, on se motive"

    jump village_1

label e_chambrer_logan_foret_1:

    e "Logan, t'es qu'un pd"

    jump village_1

label e_avis_logan_mission_foret_1:

    e "Hey Loggy, que penses-ty de cette mission"

    l "Bah tu sais moi je suis un pe con con"

    menu:
        "Pourquoi as-tu décidé de m'accompagné ?":
            jump e_pourquoi_logan_accompagne_foret_1
        "Thx bro, d'être venu":
            jump e_reconnaissant_logan_foret_1
        "Tu aurais du rester avec Harald":
            jump e_rester_haral_foret_1

label e_espoir_terre_norvege_foret_1:

    e "Snif, je veux rentrer"
    jump village_1

label e_ordre_taire_guerrier_foret_1:

    e "OHhhhhhhhhhhh fermez-vos gueule de gogole"

    gv "Oui maître"

    jump village_1

label e_pourquoi_logan_accompagne_foret_1:

    e "Pour m'a tu accompagné"

    l "Parce que tu es mon bro"

    jump village_1

label e_reconnaissant_logan_foret_1:

    e "Je remercie de m'avoir accompagné"

    l "C'est normal, il faut bien se serrer les coudes et bien plus ;)"

    jump village_1

label e_rester_haral_foret_1:

    e "Tu aurais du rester avec Harald! Abruti!"

    l "Et pourquoi donc ?"

    menu:
        "Je n'ai pas envie de mettre ta vie en danger":
            jump e_attention_logan_foret_1
        "Pas besoin d'un boulet":
            jump e_poids_logan_foret_1

label e_attention_logan_foret_1:

    e "C'est parce que je n'ai pas envie de mettre ta vie en jeu"

    l "Nous sommes des guerriers, bon sans de bois"

    jump village_1

label e_poids_logan_foret_1:

    e "Tu vas me gêner tout le long de la mission"

    l "Sympa l'ami..."

    jump village_1

#Scequence 5
#Scene 1
label village_1:

    show bg village

    e "bon les gars, nous sommes arrivé au village"

    menu:
        "Massacrez-les tous!!!!":
            jump e_massacre_village_1
        "Demander des infomation sur les rebelles":
            jump e_demander_information_village_1
        "Fouiller le village!":
            jump e_fouiller_village_1
        "Chercher soi-même dans le village":
            call e_fouiller_village_1 pass (einarFouille = True)

label e_massacre_village_1:

    gv "yeah, buttons tlm"


    call choix_retour_village_1 pass (massacre = True)

label e_demander_information_village_1:

    e "Avez vous des information sur les rebelles ?"

    vm "On ne sait rien, promis juré craché!"

    menu:
        "Tuer un Villageois afin de les forcer à parler":
            jump e_tuer_villageois_village_1

        "Hausser le ton":
            jump e_intimider_villageois_village_1

label e_fouiller_village_1(einarFouille = False):

    $ already_talk = False

    if einarFouille:
        e "Bande d'andouille, c'est moi qui fouille"

        "Entre dans une maison"

        e "Eh madmoiselle, vous'tes bien bonne"

    else:
        e "Fouillez bande de chien galleux"

        gv "Yeahhhhhhh"

        gv "Hey, Einar vient voir ça"

        e "Mais que ce passe-t-il ?"

        gv "Regarde c'est Natalie et nous, nous sommes les méchants"

        e "Mais qui voilà"


    menu menu_maison_1:
        "Hey la meuf, c'est quoi ton nom? File moi ton 06":
            jump e_nom_villageoise_maison_1
        "Pourquoi t'fais la tepu à rester caché?":
            jump e_cache_villageoise_maison_1
        "Aurais-tu des info ou un mail pour joindre les rebelles? ":
            jump e_info_rebelle_maison_1
        #Si Einar à déjà parlé une fois à Moira
        "Tuer la villageoise" if already_talk:
            jump e_tuer_moira_maison_1
        "La laisser partir" if already_talk:
            jump e_villagoise_partir_maison_1

label e_tuer_villageois_village_1:

    e "Toi approche"

    vm "Mais euh"

    e "Plus près"

    vm "C'est que vous savez..."

    e "Chabite, non je déconne, tu vas crever"

    call choix_retour_village_1 pass (massacre = True)

label e_intimider_villageois_village_1:
    e "Si vous ne dites rien, je vais finir par me facher et bouder !"

    vm "Mais je vous jure, je n'en sais rien"

    e "Ouin"

    jump choix_retour_village_1

#Scequence 6 (alternative)
label e_nom_villageoise_maison_1:
    e "Hey siva, dis-moi ton nom la bonnase"

    vm "Tu me parle pas comme ça ! Et je m'appelle Moira"

    e "Une belle histoire"

    $ already_talk = True

    jump menu_maison_1

label e_cache_villageoise_maison_1:
    e "Pourquoi n'es-tu pas avec les autres?"

    vm "Parce que je suis trop une bonnasse pour vous"

    e "Hannnnnn"

    $ already_talk = True

    jump menu_maison_1

label e_info_rebelle_maison_1:
    e "Aurais-tu des infos sur les rebelles ?"

    vm "Non"

    $ already_talk = True

    jump menu_maison_2

label e_tuer_moira_maison_1:

    e "Dommage pour toi, je vais te tuer"

    vm "oh je me meure"

    e "Alors vous allez parler bande de bolosse"

    l "Oh je suis outré"

    jump e_massacre_village_1

label e_villagoise_partir_maison_1:
    e "Va et que je ne te revois plus"

    vm "Oh merci mon seigneur"

    jump choix_retour_village_1
#fin Scequence 6

label choix_retour_village_1(massacre = False):

    if massacre:
        e "J'espère que ça leur servira de leçon"
    else:
        e "Ils vont rien nous apprendre de plus, tirons-nous"

    e "Bon ou allons nous continuer ?"

    if massacre:
        menu:
            "Rentrer au Chateau de Dunbar":
                call massacre_foret_2 pass (lieu = "chateau")
            "Poursuivre vers le nord":
                call massacre_foret_2 pass (lieu = "nord")
    else:
        menu:
            "Rentrer au Chateau de Dunbar":
                call foret_2 pass (lieu = "chateau")
            "Poursuivre vers le nord":
                call foret_2 pass (lieu = "nord")

#Scequence 7
label foret_2(lieu):

    if lieu == "chateau":

        "Sur le chemin du retour"
    else:
        "En poursuivant vers le nord"

    e "Bon les gars"

    menu:
        "Mettre en garde":
            call attaque_massacre_einar_sauf_foret_2 pass (message = "attentif")
        "Déçu par la mission":
            call attaque_massacre_einar_sauf_foret_2 pass (message = "deception")
        "attitude villageois":
            call attaque_massacre_einar_sauf_foret_2 pass (message = "attitude")
        "Chambrer Logan":
            call attaque_massacre_einar_sauf_foret_2 pass (message = "chambre_logan")

label attaque_massacre_einar_sauf_foret_2(message):

    if message == "attentif":
        e "Faites-attention, j'ai la nette impression que nous sommes oberservé!"

        gv "Bof rien ne peut nous atteindre"

    elif message == "deception":

        e "Ce n'était que du menu fretin, je vais me plaindre auprès d'Harald une fois rentré"

    elif message == "attitude":
        e "Ils avaient l'air de cacher quelque chose"

        menu :
            "Craindre un piège":
                jump menu_avertissement_villageois
            "Ils ont surrement eu peur de notre prestence":
                e "Ils ont fait dans leur pantalon"
            "Ce n'était qu'une bande de congénitaux":
                e "Ce n'était que des ch'ti"

        menu menu_avertissement_villageois:
            "Mettre en garde":
                call attaque_massacre_einar_sauf_foret_2 pass (message = "attentif")
            "Garder ses craintes pour soi":
                e "(Ne pas faire par de ses craintes)"

    else:
        e "logan, t'es qu'un PD"


    o "Vous allez payer pour ce que vous avez fait au villageois"

    o "Venez que je vous bute sales enculés"

    e "Salaud! Viens ici que je te bute enculé"

    "Einar tombe à terre un flèche dans l'épaule"

    "Il recoit un épieux dans la jambe"

    e "Aieuhhhh"

    "Logan tombe et est égorgé au sol"

    "Einar recoit du sang de la tafiolle sur le visage"

    e "Comment as-tu osé ? Espèce de **** **** de ***"

    "Une grosse masse de muscle s'approche de Einar"

    menu:
        "Qui est tu ?":
            jump e_demande_nom_foret_2
        "Non ne me tue pas, je te donnerai un sandwitch à la fraise":
            jump e_implore_pitie_foret_2
        "Menacer le lourdeau":
            jump e_menace_foret_2

#Fin alternative n°1
label massacre_foret_2(lieu):

    if lieu == "chateau":

        "Sur le chemin du retour"
    else:
        "En poursuivant vers le nord"

    e "Bon les gars"

    menu:
        "Mettre en garde":
            call attaque_massacre_foret_2 pass (message = "attentif")
        "Déçu par la mission":
            call attaque_massacre_foret_2 pass (message = "deception")
        "Se moquer des villageois":
            call attaque_massacre_foret_2 pass (message = "moquerie")
        "Chambrer Logan":
            call attaque_massacre_foret_2 pass (message = "chambre_logan")

label attaque_massacre_foret_2(message):

    if message == "attentif":
        e "Faites-attention, j'ai la nette impression que nous sommes oberservé!"

        gv "Bof rien ne peut nous atteindre"

    elif message == "deception":

        e "Ce n'était que du menu fretin, je vais me plaindre auprès d'Harald une fois rentré"

    elif message == "moquerie":
        e "Les bolosses, ça craquait sous ma hache"

    else:
        e "logan, t'es qu'un PD"

    o "Vous allez payer pour ce que vous avez fait au villageois"

    o "Venez que je vous bute sales enculés"

    e "Salaud! Viens ici que je te bute enculé"

    "Einar tombe à terre un flèche dans l'épaule"

    e "Aieuhhhh"

    "Logan tombe et est égorgé au sol"

    "Einar recoit du sang de la tafiolle sur le visage"

    e "Comment as-tu osé ? Espèce de **** **** de ***"

    "Une grosse masse de muscle s'approche de Einar"

    menu:
        "Qui est tu ?":
            call e_demande_nom_foret_2 pass (bad_ending = true)
        "Non ne me tue pas, je te donnerai un sandwitch à la fraise":
            call e_implore_pitie_foret_2 pass (bad_ending = true)
        "Menacer le lourdeau":
            call e_menace_foret_2 pass (bad_ending = true)


label e_demande_nom_foret_2(bad_ending = False):

    e "Mais qui es-tu donc ?"

    if bad_ending:
        o "Tu ne le saura jamais"
        jump bad_ending_1
    else:
        o "Tu le saura bien assez tôt"

label e_implore_pitie_foret_2(bad_ending = False):

    e "Par pitié, ne me tue pas"

    if bad_ending:
        o "Comtpe là dessus et bois de l'eau"
        jump bad_ending_1
    else:
        o "Suprise Motherfucker. Tu y as cru ?"

label e_menace_foret_2(bad_ending = False):

    e "Si tu me tues Harald, arriva pour tous vous buter"

    if bad_ending:
        o "Hasta la vista bady!"
        jump bad_ending_1
    else:
        "nope"



#Ending
label bad_ending_1:

    "Einar se fait tuer comme une merde parce qu'il n'a pas eu l'intelligence de réfléchir"

    "Et oui, il faut réfléchir"

    return
