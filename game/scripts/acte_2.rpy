#Acte 2
#Sequence 1
label interieur_maison_village_1:
    hide einar
    hide ogma
    hide re

    $ menu_choice_1 = True
    $ menu_choice_2 = True
    $ menu_choice_3 = True
    $ menu_choice_4 = True
    $ menu_choice_5 = True

    play ambiance home

    scene bg house2_jour with dissolve

    $ critique_ogma = False

    "Einar émerge du sommeil..."
    show einar debout_normal_mid at left with dissolve
    e "Je suis entravé ? Huuugh..."
    show moira debout_normal_mid at right with dissolve

    menu menu_rencontre_moira_blesse:
        "Moira ?" if moira_met and moira_name_know and menu_choice_1:
            e "... Moira ?"
            m "Vous vous rappelez de moi ?"
            e "Oui. Tu étais à Perth."
            show moira debout_determine_mid at right
            m "Ne me tutoyez pas, s'il vous plaît. J'étais bien à Perth quand vous êtes arrivés pour menacer nos anciens et terroriser nos enfants."
            $ menu_choice_1 = False
            jump menu_rencontre_moira_blesse

        "Toi ?" if moira_met and moira_name_know == False and menu_choice_1:
            e "Toi ?"
            ve "Vous vous rappelez de moi ?"
            e "Oui. Tu étais à Perth."
            show moira debout_determine_mid at right
            m "Ne me tutoyez pas, s'il vous plaît. Je m'appelle Moira. J'étais bien à Perth quand vous êtes arrivés pour menacer nos anciens et terroriser nos enfants."
            $ menu_choice_1 = False
            jump menu_rencontre_moira_blesse

        "Qui es-tu ?" if menu_choice_2:
            e "Qui es-tu ? Je t'ai déjà rencontré ?"
            m "Je suis Moira, fille d'Ogma. Celui que l'on surnomme \"Le Hurleur\"."
            m "J'étais à Perth lorsque vous êtes arrivés pour menacer nos anciens et terroriser nos enfants."
            e "J'aurais probablement dû t'accorder plus d'attention..."
            show moira debout_determine_mid at right
            m "Ne me tutoyez pas."
            $ menu_choice_2 = False
            jump menu_rencontre_moira_blesse

        "Où sommes-nous ?" if menu_choice_3:
            e "Où sommes-nous ?"
            m "Nous sommes à Perth. Cette maison appartient à mon père."
            show moira debout_determine_mid at right
            m "Vous devriez vous habituer. Vous allez passer un certain temps ici."
            e "Pourquoi ?"
            m "Vos blessures sont graves. Une infection a déjà commencé à attaquer votre cuisse. Il vous faudra plus d'un mois pour vous remettre."
            $ menu_choice_3 = False
            jump menu_rencontre_moira_blesse

        "Arrière ! Laisse-moi !":
            show einar debout_effraye_mid at left
            e "Laisse-moi tranquille ! Où est Ogma ? Je veux sortir d'ici !"
            m "Du calme, du calme."
            m "Je n'ai aucune intention de vous faire du mal."
            show einar debout_normal_mid at left

        "La situation est assez... plaisante !":
            show einar debout_souriant_mid at left
            e "La situation est assez... satisfaisante. Je n'ai encore jamais été pris au piège par une jolie jeune fille comme ..."
            show moira debout_furieux_mid at right
            " Moira s'approche et assène un violent coup de pied dans le genou d'Einar, sans qu'il ne puisse se défendre."
            e "Aaargh !"
            m "A l'avenir, vous éviterez ce genre de... choses. Soyez correct avec moi et je serai correcte avec vous."
            show moira debout_normal_mid at right

    "Moira broie quelque chose avec un pilon"

    menu:

        "Que faites-vous ?":
            e "Qu'est ce que c'est ? Qu'est-ce que vous faites ?"
            m "Je broie des plantes pour vous."
            e "Pour moi ?"
            m "Oui ! C'est du millepertuis, mélangé avec d'autres herbes."

        "Ne rien dire":
            e "..."
            m " Vous pouvez parler, j'ai le droit de vous répondre."
            e "..."
            show moira debout_determine_mid at right
            m "J'imagine que vous ne dites rien par fierté ? Ne soyez pas idiot. Vous vous doutez que ce que je prépare vous est destiné !"
            show moira debout_normal_mid at right
            show einar debout_normal_mid at left
            e "Qu'est-ce que c'est ?"

        "J'ai encore toutes mes dents, merci":
            show einar debout_souriant_mid at left
            e "J'ai encore mes dents, je n'ai pas besoin que l'on broie ma nourriture."
            show moira debout_souriant_mid at right
            m "Ce n'est pas de la nourriture !"
            show einar debout_normal_mid at left

        "Je n'ai pas faim":
            e "Je n'ai pas faim, merci."
            show moira debout_souriant_mid at right
            m "Ce n'est pas de la nourriture !"

    m "Je vous prépare un onguent, pour l'infection de votre cuisse."
    e "Un onguent ?"
    m "Soyez rassuré : c'est un ancien qui m'a donné les plantes, et il ne se trompe jamais !"
    e "Mmmh..."
    m "C'est mon père qui m'a demandé de vous soigner. Quand vous le verrez, essayez de vous montrer reconnaissant."

    menu :
        "Merci":
            show einar debout_souriant_mid at left
            e "Merci. Je ne m'attendais pas à être soigné ici."
            show moira debout_normal_mid at right
            m "Ce n'est pas moi que vous devez remercier, je ne fais que suivre les instructions de mon père."

        "Ne rien dire":
            show einar debout_determine_mid at left
            e "..."
            show moira debout_determine_mid at right
            m "..."

        "Je n'ai pas besoin des soins d'une rebelle !":
            show einar debout_contrarie_mid at left
            e "Je n'ai pas besoin des soins d'une rebelle. J'ai supporté des blessures plus terribles sans être soigné !"
            show moira debout_determine_mid at right
            m "Vous êtes ridicule. Vous voulez que je vous laisse comme ça ? Dès ce soir vous serez tremblant de fièvre, et demain vous serez déjà mourant."
            m "Mais allez- y ! Allez vous promener dehors ! Ah, j'oublais, vous n'en avez pas le droit et vous êtes entravé."
            m "Laissez-moi faire ce qu'on m'a demandé. J'essaie de ne pas être désagréable, faites en autant."

    "..."
    hide einar with dissolve
    show ogma debout_normal_mid at center with dissolve
    o "Alors ? Comment va le prisonnier ?"
    show moira debout_normal_mid at right
    m "Plutôt bien ! Il a une infection à la jambe mais le vieux Murray m'a donné des plantes pour le soigner. D'ici une semaine, l'infection sera passée."
    o "Et l'épaule ?"
    m "La cicatrisation commence à peine, la blessure était profonde. Le vieux m'a aidé à extraire la tête de la flèche de son épaule, j'ai bien cru qu'il allait se vider de tout son sang !"
    show einar debout_normal_mid at left with dissolve
    e "Je ..."
    show ogma debout_determine_mid at center
    o "Tais-toi. Moira, finis les soins et rejoins moi dehors."
    hide ogma with dissolve


    menu :
        "Il a un problème avec moi ?":
            show einar debout_normal_mid at left
            e "Il a une dent contre moi ?"
            m "Pas contre vous en particulier, non."

        "J'aurais dû mourir...":
            show einar debout_attriste_mid at left
            e "J'aurais mieux fait de mourir avec les autres."
            m "Estimez-vous heureux d'être en vie. Il voulait tous vous tuer."
            show einar debout_normal_mid at left
            e "Pourquoi cette colère contre nous ?"

        "Quel salopard !":
            show einar debout_furieux_mid at left
            e "Quel enfoiré ! Il ne m'a même pas adressé la parole !"
            $ critique_ogma = True

        "Il doit avoir honte de s'adresser au survivant d'un assassinat lâche !":
            show einar debout_determine_mid at left
            e "A sa place, moi aussi j'aurais honte de m'adresser au chef d'une troupe assassinée lâchement au détour d'un sentier obscur. Bandits de grands chemins !"
            $ critique_ogma = True

    if critique_ogma:
        show moira debout_furieux_mid at right
        "Moira gifle Einar"
        m "C'est la dernière fois que vous manquez de respect à mon père. Ou bien vous irez vous faire voir dans l'enclos des boucs."

        menu :
            "Ne rien dire":
                show einar debout_normal_mid at left
                e "..."
                show moira debout_normal_mid at right
                m "Je n'agis pas par caprice, si c'est ce que vous pensez. Vous nous devez plusieurs vies."
                e "Plusieurs vies ?"
                m "La votre, dans un premier temps."
                e "Et ?"
                m "Et celle de Kennocha, ma mère."

            "Je vous demande pardon":
                show einar debout_contrarie_mid at left
                e "Excusez-moi."
                show moira debout_normal_mid at right
                m "N'en parlons plus."
                show einar debout_normal_mid at left
                e "..."
                m "Je n'agis pas par caprice, si c'est ce que vous pensez. Vous nous devez plusieurs vies."
                e "Plusieurs vies ?"
                m "La votre, dans un premier temps."
                e "Et ?"
                show moira debout_determine_mid at right
                m "Et celle de Kennocha, ma mère."

            "Vous n'avez pas d'ordres à me donner":
                show einar debout_determine_mid at left
                e "Je n'ai pas d'ordres à recevoir d'une fifille à papa."
                show moira debout_furieux_mid at right
                " Moira gifle Einar à nouveau, sur l'autre joue."
                m "J'ai omis de préciser que vous me deviez aussi le respect."
                show einar debout_determine_mid at left
                show moira debout_determine_mid at right
                m "Je n'agis pas par caprice, si c'est ce que vous pensez. Vous nous devez plusieurs vies."
                e "Plusieurs vies ?"
                m "La votre, dans un premier temps."
                e "Et ?"
                m "Et celle de Kennocha, ma mère."

    show moira debout_normal_mid at right
    m "J'imagine que si le roi est venu en Ecosse, c'est pour punir ceux qui ont tué son intendant ?"
    show einar debout_normal_mid at left
    e "Oui."
    m "Savez vous seulement pourquoi nous l'avons tué ? Je suis certaine que la question ne vous a même pas effleuré."
    e "Le roi nous a demandé de mater la rébellion et de venger l'intendant Montgomery. Le reste ne nous regarde pas."
    show moira debout_furieux_mid at right
    m "Montgomery méritait de mourir !"
    show einar debout_determine_mid at left
    e "Qu'est-ce qui vous a donné le droit de le tuer ?"
    show moira debout_attriste_mid at right
    m "Il a tué ma mère, Kennocha."
    e "..."
    show moira debout_determine_mid at right
    m "Clyde Montgomery n'était pas intendant. C'était un porc, doublé d'un tortionnaire ! Il saignait l'Ecosse à blanc ! Il exigeait de nous plus que ce que nous avions !"

    if short_version == False:
        e "Quel rapport avec votre mère ?"
        show moira debout_normal_mid at right

    m "Un matin, l'intendant est arrivé accompagné de ses sous-fifres. Il a exigé qu'on lui donne immédiatement l'impôt ainsi que de la nourriture pour ses hommes."

    if short_version == False:
        m "Nous avons rassemblé tout ce que nous pouvions et le leur avons donné. Il ne nous restait presque rien."

    m "Montgomery n'était pas satisfait, et il a demandé à ses gardes de fouiller nos maisons."
    m "Ils ont découvert une réserve de nourriture que ma mère avait dissimulé."
    show moira debout_attriste_mid at right
    m "Sans rien dire, Montgomery s'est approché de ma mère et l'a tuée devant tout le village, sur la place."

    if short_version == False:
        show einar debout_normal_mid at left
        m "\"Ne me cachez rien, jamais.\" J'entends encore sa voix. Tous ceux qui ont essayé de sauver ma mère ont été passés à tabac, personne n'a pu faire quoi que ce soit."
        show einar debout_determine_mid at left
        e "Où étiez-vous ? Où était votre père ?"
        show moira debout_determine_mid at right
        m "J'étais parmi ceux que les gardes ont frappé. Quand j'ai vu ma mère tomber, j'ai voulu me jeter sur l'intendant. Je n'ai même pas pu passer ses gardes."
        m "Quand mon père est revenu, il a franchi le cercle que formaient les gens du village. Personne ne parlait. Il revenait de la rivière avec quelques prises du matin."
        show moira debout_attriste_mid at right
        m "A ce moment là, Montgomery était déjà parti. Mon père a retrouvé ma mère allongée dans la boue et dans son sang, devant tout le monde."
        show moira debout_determine_mid at right

    m "La suite, vous la connaissez."
    e "Alors c'est Ogma lui-même qui a assassiné l'intendant..."

    if short_version == False:
        m "Oui. Et je l'y ai aidé. Le garde qui m'avait frappé, je lui ai tranché la gorge. Il pleurait."
        e "..."

    m "Mon père n'est pas une mauvaise personne. Il a tué l'intendant de plein droit."
    e "..."
    e "Pourquoi toutes ces révélations ?"
    show moira debout_normal_mid at right
    m "J'estime que vous avez le droit de savoir pourquoi vos hommes sont morts, et pourquoi vous allez trahir le roi."
    m "Je vais vous laisser. Je reviendrai demain changer vos bandages."

    if short_version:
        jump interieur_maison_village_4
    else:
        jump interieur_maison_village_2

#Sequence 2
label interieur_maison_village_2:
    scene bg house2_night with dissolve
    "Quelques jours plus tard..."

    show moira debout_souriant_mid at right
    m "Bonjour ! Je viens changer vos bandages."
    show einar debout_normal_mid at left
    e "Bonjour."

    menu:

        "Appelle moi Einar":
            e "Après ces quelques jours passés ensemble, plus la peine de me parler comme à un étranger. Appelez moi-Einar."
            show moira debout_normal_mid at right
            m "Alors parle moi comme à une bonne connaissance."
            show moira debout_normal_close at right with dissolve
            show einar debout_souriant_close at left with dissolve
            e "Très bien, Moira."
            show moira debout_souriant_close at right

        "Merci pour tout":
            e "Merci."
            show moira debout_normal_mid at right
            m "Pour ?"
            e "Les soins, les bandages, tout."
            show moira debout_souriant_mid at right
            m "Vous n'allez pas me remercier à chaque fois que je viens m'occuper de vous ! "
            e "Je vous suis redevable !"
            show moira debout_determine_mid at right
            m "..."
            e "Oui ?"
            m "Je suis lasse de devoir m'adresser à vous comme à un prisonnier."
            e "Alors appelez moi Einar."
            show moira debout_normal_mid at right
            m "Adressez-vous à moi comme à une bonne connaissance."
            show einar debout_souriant_close at left with dissolve
            show moira debout_normal_close at right with dissolve
            e "Très bien ! Alors voilà : je te remercie pour tes soins, Moira !"
            show moira debout_normal_mid at right
            m "C'est mieux comme ça..."
            show einar debout_determine_close at left
            e "Quelque chose ne va pas ?"
            show moira debout_souriant_close at right
            m "Non, tout va très bien, au contraire !"
            e "Tu en es certaine ?"
            show moira debout_normal_close at right
            m "Oui ! Ça va te sembler bizarre, mais j'apprécie ces moments."
            show einar debout_normal_close at left
            e "De quoi tu parles ?"
            m "Les moments où je te soigne. Pendant ce temps, je ne pense pas au reste. Ça me change les idées !"
            show einar debout_souriant_close at left
            e "Tu te distrais en changeant les bandages souillés d'un prisonnier de guerre ?"
            show moira debout_souriant_close at right
            m "Je préfère encore ça plutôt que de m'occuper des bêtes, bien que ce ne soit pas si différent !"
            show moira debout_normal_close at right
            show einar debout_normal_close at left

        "Ce n'est pas la peine d'insister, je ne suis toujours pas interessé ":
            show einar debout_souriant_mid at left
            e "Pas la peine d'insister : je ne suis toujours pas interessé !"
            show moira debout_souriant_mid at right
            m "Ne soit pas idiot !"
            show moira debout_normal_close at right with dissolve
            show einar debout_normal_close at left with dissolve
            e "Tiens ? On se tutoie maintenant ?"
            m "Oui. J'en ai assez de devoir te parler comme à un étranger."
            show einar debout_souriant_close at left with dissolve
            e "Ça me va !"

    " Les bandages d'Einar sont remplacés."
    m "Je vais te laisser, c'est tout pour aujourd'hui."
    show einar debout_souriant_close at left
    e "A demain ?"
    show moira debout_normal_close at right with dissolve
    m "A demain."
    hide einar
    hide moira
    with dissolve
    jump interieur_maison_village_3

#Sequence 3
label interieur_maison_village_3:
    scene bg house2_jour with dissolve
    show ogma debout_souriant_mid at center with dissolve
    show moira debout_souriant_mid at right with dissolve
    "Quelques semaines plus tard..."
    o "... je la voyait se débattre comme jamais une truite ne s'était débattue ! Je tire sur la ligne en essayant de la remonter, mais ce foutu poisson passe derrière un rocher : la ligne casse !"
    m "A ce moment là je saute dans la rivière depuis la berge !"
    o "Ta mère était folle ! Elle était persuadée que tu allais te noyer ! L'eau était vive et glacée, c'était au début du printemps."
    m "Et j'ai bien cru me noyer aussi !"
    o "On ne voyait plus que tes cheveux hors de l'eau ! Tu as dérivé sur une vingtaine de mètres, et puis tu as levé tes bras hors de l'eau !"
    m "Je tenais la truite au-dessus de moi ! Elle était énorme !"
    o "Pas si grosse que ça, mais tu étais à peine plus grande qu'elle, ha ha !"
    show ogma debout_normal_mid at center
    o "Ensuite ta mère t'a sortie de l'eau. Tu étais toute bleue, mais tu ne voulais pas lâcher le poisson ! On t'a ramenée à la maison et tu n'as lâché la truite qu'une fois rentrée !"
    show moira debout_attriste_mid at right
    m "J'aimerais retourner pêcher..."
    o "Pas pour le moment. Nous avons des choses à régler d'abord..."
    show einar debout_attriste_mid at left with dissolve
    e "Logan aussi était un bon pêcheur..."
    o "D'où venait-il ?"
    show einar debout_determine_mid at left
    e "D'Aberdeen, loin au nord."
    o "Je n'y suis jamais allé... Et vous Einar, vous n'avez rien à raconter ? D'où venez-vous ?"

    show moira debout_normal_mid at right with dissolve

    menu :
        "Ça ne vous regarde pas !":
            show einar debout_contrarie_mid at left
            e "Ça ne vous regarde pas, salopard. Vous avez tué mes hommes et Logan."
            show moira debout_furieux_mid at right
            m "Einar !"
            "Moira lève la main et s'apprête à gifler Einar. Ogma l'interromp en saisissant son bras au vol."
            show ogma debout_contrarie_mid at center
            o "Non... Laisse-le dire. Il n'a pas tort. J'ai tué ses amis."
            m "Mais il t'a insulté !"
            o "Il n'est pas responsable de grand chose dans cette histoire. Il a suivi les ordres de son roi."
            show moira debout_contrarie_mid at right
            m "..."
            e "..."

        "Je viens de Norvège...":
            show einar debout_attriste_mid at left
            e "Je viens de Norvège. Le pays me manque..."
            show moira debout_normal_mid at right
            m "A quoi ça ressemble, la Norvège ?"
            show einar debout_normal_mid at left
            e "Ce n'est pas si différent de l'Ecosse. Nous avons le même climat, peut être un peu plus froid. Et il y a de grands fjords."
            show ogma debout_normal_mid at center
            o "Des fjords ?"
            show einar debout_souriant_mid at left
            e "Des rivières et des fleuves encaissés dans des vallées. C'est très beau."
            m "J'imagine..."
            e "Lorsqu'on va loin au nord, la nuit, on peut voir de grandes lumières vertes ou rouges dans le ciel. Certains disent que sont des hommages divins pour les héros morts au combat."
            m "J'aimerais beaucoup voir ça, un jour..."
            show moira debout_souriant_mid at right
            m "Tu as une femme, là-bas ? Une famille ?"
            show einar debout_normal_mid at left
            e "Non. Je n'ai plus personne."

        "Je ne veux pas en parler":
            show einar debout_contrarie_mid at left
            e "Je ne souhaite pas en parler."
            show ogma debout_normal_mid at center
            o "Je comprends."
            show moira debout_normal_mid at right
            m "..."

    hide einar
    hide moira
    with dissolve
    show ve debout_effrayes_mid at right with dissolve
    ve "Ogma !"
    show ogma debout_contrarie_mid at center
    o "Fenella ? Quelque chose ne va pas ?"
    show ve debout_craintifs_mid at right
    ve "Dunfermline a brûlé ce matin !"
    show ogma debout_attriste_mid at center
    o "Le roi... Je ne suis pas surpris."
    hide ve with dissolve
    show einar debout_normal_mid at left with dissolve
    e "Vous n'avez pas vraiment l'air affecté par la nouvelle."
    show moira debout_attriste_mid at right with dissolve
    m "Stirling et Falkirk ont déjà été rasée il y a quelques jours. Le roi est en marche."
    show ogma debout_determine_mid at center
    o "Depuis que vous avez été capturé, Harald n'a pas cessé de vous chercher. Nous avons déjà eu la visite d'un émissaire."

    menu :
        "Je suis désolé pour les innocents":
            show einar debout_attriste_mid at left
            e "Je regrette. Ces gens étaient innocents. Harald avait pourtant dit qu'il ne voulait pas lancer d'attaques au hasard..."
            show ogma debout_normal_mid at center
            o "Merci. Je ne pense pas qu'il s'agisse d'attaques aveugles. Le roi a décidé de tuer des innocents pour nous faire sortir de nos cachettes et provoquer le rejet du peuple."
            show moira debout_normal_mid at right
            m "Le roi aurait trahi sa parole, Einar ?"
            show einar debout_contrarie_mid at left
            e "Ce n'est pas dans ses habitudes. Mais il y a peut-être été poussé. Ces massacres ne devraient pas avoir lieu. Je regrette sincèrement d'avoir amené la mort dans mon sillage."
            m "..."
            show ogma debout_normal_mid at center
            o "Vous êtes quelqu'un de juste, Einar. Vous n'êtes pas responsable de ce qui se produit."

        "Ne rien dire":
            e "..."
            show ogma debout_normal_mid at center
            o "Votre silence vous honore. Je comprends que vous ne vouliez pas prendre parti, votre position est délicate."

        "Je serai bientôt libre !":
            show einar debout_souriant_mid at left
            e "Harald est à ma recherche. Bientôt, je serai libre. Ces massacres ne sont que les signes annonciateurs de ma libération."
            show ogma debout_contrarie_mid at center
            o "J'ai cru que vous étiez quelqu'un de juste. Je me trompais probablement. Vous me dégoûtez."

    show moira debout_determine_mid at right
    m "Le roi ne risque pas d'arriver ici sous peu ?"
    show einar debout_normal_mid at left
    show ogma debout_determine_mid at center
    o "Non, tout a été prévu. Hier, j'ai demandé à mes hommes d'accomplir deux choses : la première était de tenter d'assassiner l'ami du roi dans son propre château, l'évêque Patrick d'Edimbourg."
    o "La seconde était de brûler les navires par lesquelles les troupes vikings sont arrivées."
    o "L'assassinat aura lieu ce soir. Quant à l'incendie des navires, il aura eu lieu d'ici deux jours. Les délais sont très courts, mais cela devrait obliger Harald à reculer pour quelques temps."
    show einar debout_determine_mid at left
    e "Il va vouloir consolider ses forces au château. Votre assaut n'en sera que plus difficile."
    o "Je n'avais pas le choix ! Sans ces décisions, les troupes du roi seraient arrivées ici après-demain au plus tard."
    show ogma debout_normal_mid at center
    o "Nous allons vous laisser. Reposez-vous."
    show moira debout_normal_mid at right
    m "..."

    hide einar
    hide moira
    hide ogma
    with dissolve
    jump interieur_maison_village_4

#Sequence 4
label interieur_maison_village_4:

    scene bg house2_jour with dissolve

    if short_version:
        #Narration

    $ libre_ask = False
    $ trahir_talk = False
    $ decevoir_moira = ""

    "Deux semaines plus tard..."

    "Moira arrive dans la chambre, un couteau à la main."
    show moira debout_normal_close at right with dissolve
    show einar debout_normal_close at left with dissolve
    m "Bonjour, Einar."

    menu menu_moira_couteau:
        "Ne rien dire" if libre_ask == False:
            e "..."

        "Je suis libre ?" if libre_ask == False:
            e "Tu vas me libérer ?"
            show moira debout_determine_close at right
            m "Non. Je vais accomplir ce que mon père aurait dû faire depuis longtemps..."
            show einar debout_effraye_close at left
            e "Au secours ! A moi !"
            $ libre_ask = True

        "Au secours !":
            show einar debout_effraye_close at left
            e "À l'aide ! Elle va me saigner !"
            show moira debout_souriant_close at right
            m "Mais non ! Calme toi. Je n'ai pas prévu de saigner qui que ce soit aujourd'hui !"

        "Mmmh... J'aime ce genre d'accessoires":
            show einar debout_souriant_close at left
            e "Mmmh... Notre relation manquait un peu de piment. Des accessoires ne seront pas de trop..."
            show moira debout_souriant_close at right
            m "Ne dis pas de choses pareilles ! " #elle sourit

        "Pourquoi me tuer maintenant ?":
            show einar debout_attriste_close at left
            e "Alors c'est la fin ? Pourquoi aujourd'hui ? Pourquoi m'avoir soigné pendant toutes ces semaines ?"
            e "Ça n'a pas de sens !"
            $ libre_ask = True

    if libre_ask:
        show moira debout_souriant_close at right
        m "Ha ha ha, je viens bien te libérer, idiot ! Je n'ai aucune intention de te faire mal. Pour le moment !"

    show moira debout_normal_close at right
    m "Mon père a demandé à ce qu'on te rende ta liberté de mouvement. Il a dit que tu devais te dégourdir un peu les jambes : il ne faudrait pas que tu sois affaibli pour les combats à venir."
    show einar debout_contrarie_close at left
    e "Je n'ai pas vu l'extérieur depuis un mois..."
    show moira debout_souriant_close at right
    m "Sortir te fera du bien ! Tu es encore plus pâle qu'au moment où tu es arrivé ici."

    menu:
        "Il y a un piège ?":
            show einar debout_contrarie_close at left
            e "Où est le piège ? Ça me semble trop beau..."
            show moira debout_souriant_close at right
            m "Il n'y a pas de piège !"

        "Tu ne veux pas me torturer un peu ?":
            show einar debout_souriant_close at left
            e "Je suis déçu qu'il ne s'agisse pas d'un \"jeu\"... Tu ne veux pas me torturer un peu ?"
            show moira debout_souriant_close at right
            m "Arrête, ça devient gênant !" #elle sourit

        "Vous n'avez pas peur que je m'échappe ?":
            show einar debout_normal_close at left
            e "Ton père ne se méfie pas ? Je pourrais m'échapper..."

    show moira debout_normal_close at right
    m "Mon père a choisi de te faire confiance. Tu pourras aller dehors, mais tu ne sortiras pas du village à moins de recevoir une autorisation directe. Et tu devras être accompagné en permanence !"
    show moira debout_souriant_close at right
    m "Je suis heureuse de voir que ton état s'est bien amélioré. Je ne te cache pas que j'ai eu des doutes au début !"
    show einar debout_normal_close at left
    e "C'est rassurant..."
    m "D'ici peu de temps, tu seras complètement remis."

    menu :

        "Et je devrai trahir Harald...":
            show einar debout_contrarie_close at left
            e "Et je serai tenu de trahir mon roi à ce moment là..."
            show moira debout_contrarie_close at right
            m "Oui... Tu as fait une promesse Einar. Nous comptons tous sur toi."
            e "..."
            show moira debout_normal_close at right
            m "Je me demande... Que comptes-tu faire après avoir tenu ta promesse ? Après avoir trahi Harald ?"
            $ trahir_talk = True

        "Grâce à toi":
            show einar debout_souriant_close at left
            e "Grâce à toi, Moira !"
            show moira debout_souriant_close at right
            m "..." # elle sourit
            m "Je n'ai fait qu'une partie du travail. Tu es solide ! Ton corps à largement participé à l'efficacité de mes soins."

        "Ne rien dire":
            show einar debout_determine_close at left
            e "..."
            show moira debout_souriant_close at right
            m "C'est tout ? Je m'attendais à des remerciements, à de l'enthousiasme ! Tu n'as pas envie d'aller dehors ?"
            show einar debout_normal_close at left
            e "Si, si..."

        "Je peux sortir ?":
            show einar debout_normal_close at left
            e "On peut sortir maintenant ? La lumière du jour me manque."
            show moira debout_souriant_close at right
            m "Bien sûr ! Reste près de moi." # elle sourit


    if trahir_talk:
        menu:

            "J'arrêterai d'être soldat":
                show einar debout_normal_close at left
                e "J'abandonnerai la carrière militaire. Je rentrerai en Norvège. J'en ai assez de servir les autres."
                e "On m'a promit des récompenses, des terres. Je n'ai rien eu de tout ça. Seulement la mort de mes compagnons. Et j'ai été estropié ! Passé un certain temps, la gloire ne suffit plus."

                $ decevoir_moira = "partir"

            "J'irai dans une région plus chaude":
                show einar debout_normal_close at left
                e "Je partirai dans une région plus chaude. La méditerranée, peut-être. Je n'ai plus ma place auprès du roi, et je ne veux pas rester ici."
                e "L'éloignement est sûrement ma seule option : autant aller sous de meilleures latitudes."
                $ decevoir_moira = "partir"

            "Je resterai ici":
                show einar debout_normal_close at left
                e "Je vais rester ici. Je n'ai plus ma place en Norvège ni ailleurs. Harald me traquera partout où il le pourra. Je suppose que mon seul abri sera l'Ecosse."
                show moira debout_souriant_close at right
                m "Si tu réussis, nous serons heureux de te compter parmi nous. Allez, il est temps de sortir !"

            "Je ne sais pas":
                show einar debout_normal_close at left
                e "Je ne sais pas. J'ai besoin de temps pour y réfléchir..."
                m "Je comprends."
                $ decevoir_moira = "rien"

        if decevoir_moira == "partir":
            show moira debout_normal_close at right
            m "Oh... Tu pourrais rester ici ? Je pense que les gens accepteraient ta présence si tu participais à la vie du village."
            show einar debout_normal_close at left
            e "Je ne sais pas..."
            show moira debout_attriste_close at right
            m "Suis-moi, je vais te montrer l'extérieur."

        elif decevoir_moira == "rien":
            show moira debout_normal_close at right
            m "J'espère que tu trouveras vite la réponse. Une fois que tu seras parti pour le château, tu seras au pied du mur..."
            show einar debout_normal_close at left
            e "Qu'est-ce que tu voudrais, toi ?"
            show moira debout_normal_close at right
            m "Ce n'est pas à moi de te dire ce que tu dois faire. J'aimerais juste savoir que tu es en sécurité. Le roi voudra se venger de toi."
            e "Où pourrais-je aller ? Harald domine le monde."
            m "Tu pourrais rester ici. Tu vivrais avec nous..."
            e "..."
            show moira debout_souriant_close at right
            m "Je ne veux pas te gêner, excuse-moi. Allez, il est temps de sortir !"

        else:
            show moira debout_souriant_close at right

    m "Viens !"
    hide einar
    hide moira
    with dissolve
    "Moira entraîne Einar a l'extérieur en lui tenant la main"

    if short_version:
        jump village_3
    else:
        jump village_2

#Sequence 5
label village_2:

    play ambiance village

    scene bg village with dissolve

    show ve debout_normaux_mid at center with dissolve

    ve "... et il faudra que tu penses à rentrer les bêtes plus tôt !"
    ve "Mamie ! J'ai trouvé un caillou qui brille !"

    "Les villageois remarquent à peine la présence d'Einar."
    hide ve with dissolve

    show einar debout_normal_mid at left with dissolve
    show moira debout_normal_mid at right with dissolve

    menu :
        "Pas d'ovation populaire ?":
            show einar debout_souriant_mid at left
            e "Pas d'applaudissements ? Pas d'ovation populaire ? C'est ainsi que le bon peuple accueille le héros qui doit le libérer du joug du terrible roi-empereur ?"
            show moira debout_souriant_mid at right
            m "Ha ha ha ! Ne soit pas trop exigeant ! Tu auras un accueil princier une fois que tu auras fait partir Harald !"
            e "Des encouragements auraient été enthousiasmants."

        "Ne rien dire":
            show einar debout_normal_mid at left
            e "..."
            show moira debout_normal_mid at right
            m "On dirait que voir l'extérieur et le village ne te fait pas plus d'effet que ça... J'imagine que tu ne réalises pas vraiment que tu as recouvré une partie de ta liberté."
            e "C'est sûrement ça..."

        "Ces paysans puent toujours autant":
            show einar debout_determine_mid at left
            e "Les paysans n'ont pas changé depuis la dernière fois. Mêmes odeurs, mêmes têtes d'abrutis consanguins."
            show moira debout_determine_mid at right
            m "Ces gens sont ma famille et mes amis. Un peu de reconnaissance pour ceux qui t'ont soigné, nourri et abrité pendant tout ce temps ne serait pas de trop."
            show einar debout_normal_mid at left
            e "Je n'ai vu qu'une seule personne me soigner, et c'était toi."
            m "Peut-être. Mais ta nourriture venait bien de ces gens. Et les herbes et remèdes que je t'ai administré m'ont été conseillés par le vieux Murray."
            m "Tu dois quelque chose à chacune de ces personnes."
            e "Tu salueras le vieux Murray de ma part, alors..."

        "Où est Ogma ?":
            show einar debout_normal_mid at left
            e "Ogma n'est pas ici ?"
            show moira debout_normal_mid at right
            m "Non, mon père est parti hier soir du village."
            e "Pourquoi ?"
            m "Je ne sais pas vraiment... Je crois qu'il est parti rencontrer les gens de Kircaldy."
            show einar debout_determine_mid at left
            e "Mmmh..."

    show moira debout_normal_mid at right
    show einar debout_normal_mid at left
    m "..."
    m "Je vais te faire visiter Perth. Nous allons d'abord voir Fenella, elle a hâte de te rencontrer depuis qu'elle t'a vu l'autre jour."
    show einar debout_effraye_mid at left
    e "Fenella ? La dernière fois, c'était une grosse femme rougeaude qui sentait l'ail. Il s'agit de cette Fenella ?"
    show moira debout_souriant_mid at right
    m "Ha ha, oui ! Et je crois bien que tu lui plaît beaucoup ! Elle a perdu son mari il y a quelques années. Il te ressemblait un peu, je crois."
    show einar debout_contrarie_mid at left
    e "La journée va être longue..."

    jump village_3

#Sequence 6
label village_3:

    scene bg village2_crepuscule with dissolve

    if short_version:
        #Narration

    $ einar_raler = False

    "Le soir, Moira s'apprête à ramener Einar dans sa \"cellule\"."

    show einar debout_normal_mid at left
    show moira debout_normal_mid at right

    m "Alors ? Qu'as-tu pensé de cette première sortie ? Tu as apprécié ?"

    menu :

        "J'avais besoin de bouger":
            show einar debout_souriant_mid at left
            e "Oui. Je commençais à être sérieusement engourdi ! Le sensation de l'herbe sous mes pieds... Ça me manquait !"
            show moira debout_souriant_mid at right
            m "J'imagine ! Des tas de choses ont dû te manquer pendant que tu étais enfermé ici..."

        "Oui, surtout en si bonne compagnie":
            show einar debout_souriant_mid at left
            e "Oui. Cette sortie est agréable, surtout aussi bien accompagné."
            show moira debout_souriant_mid at right
            m "..." #elle sourit
            m "Moi aussi, j'ai apprécié de passer du temps avec toi."

        "Non. Je déteste l'Ecosse !":
            show einar debout_contrarie_mid at left
            e "Pas vraiment. Je n'aimais déjà pas l'Ecosse quand j'y ai accosté, et mon opinion n'a toujours pas changé."
            e "D'ailleurs, je crois que personne n'était heureux de venir ici à part Logan."
            e "Et quand je dis heureux, c'est exagéré."
            e "Je pense que l'Ecosse m'insupporte parce qu'elle ressemble beaucoup à la Norvège, tout en n'y étant pas égale."
            e "Ah, si je pouvais retourner là-bas, je..."
            $ einar_raler = True

        "J'ai mal, le repas était mauvais, Fenella pue...":
            show einar debout_contrarie_mid at left
            e "Non. Mes blessures me lancent. Et le repas chez Fenella était un enfer."
            m "Tu n'as pas aimé les oatcakes ?"
            e "Non. Cette saloperie était plus sèche que l'Anatolie ! J'ai cru m'étouffer !"
            m "Et le haggis ? Je suis sûre que tu as aimé !"
            e "Pas vraiment."
            m "Pourtant, quand je t'en ai donné alors que tu étais attaché, tu avais l'air d'adorer ça."
            e "Tu les préparais mieux."
            m "Ils étaient préparés par Fenella."
            show einar debout_determine_mid at left
            show moira debout_souriant_mid at right
            e "..."
            show einar debout_normal_mid at left
            e "A vrai dire, la seule chose que j'ai apprécié était cette eau de vie que le vieux Murray m'a fait goûter."
            show moira debout_normal_mid at right
            m "Ah ? C'est drôle, c'est la seule chose que je déteste ! L'odeur, le goût..."
            e "Avec quoi a-t-il dit que c'était fabriqué ?"
            m "De l'eau de source et des céréales, de l'orge je crois. C'est son vieux cousin Campbell qui lui en a donné un tonnelet."
            show einar debout_souriant_mid at left
            e "Une fois toute cette histoire terminée, j'irai chercher ce fameux cousin ! J'aimerais lui acheter un peu de sa production."
            show moira debout_souriant_mid at right
            m "Finalement, cette journée était plutôt agréable !"
            show einar debout_determine_mid at left
            e "Non, je persiste. J'ai detesté le..."

            $ einar_raler = True

    if einar_raler:
        show moira debout_souriant_mid at right
        m "Arrête de râler ! Tu auras beau dire ce que tu veux, j'ai bien vu que tu avais apprécié ce que je t'ai montré. "

    show moira debout_souriant_mid at right
    m "Avant de te ramener à la maison, j'aimerais te montrer une dernière chose. C'est un endroit que j'aime beaucoup."
    "Moira prend Einar par la main et l'entraîne derrière elle, sortant discrètement du village."
    hide einar
    hide moira
    with dissolve

    jump foret_3

#Sequence 7
label foret_3:

    play ambiance wood

    scene bg forest_crepuscule with dissolve

    show einar debout_normal_mid at left with dissolve
    show moira debout_normal_mid at right with dissolve

    menu :
        "Où allons-nous ?":
            e "Où allons-nous?"

        "Et l'ordre d'Ogma ?":
            e "Et les instructions de ton père ? Je croyais que je n'avais pas le droit de sortir, sauf autorisation spéciale."

        "Ça me rappelle vaguement une embuscade...":
            show einar debout_determine_mid at left
            e "C'est amusant, ça me rappelle un mauvais épisode de ma vie. Des rebelles écossais attaquaient mes hommes par surprise dans une forêt et..."

    "Moira demande à Einar de se taire, en mettant un doigt sur sa bouche."
    show moira debout_souriant_mid at right
    m "Chuuut..."

    hide einar
    hide moira
    with dissolve

    jump paradis_foret_1

#Sequence 8
label paradis_foret_1:

    play music romance
    play ambiance magnificente_wood

    scene bg little_heaven with dissolve

    show einar debout_normal_mid at left
    show moira debout_normal_mid at right
    with dissolve

    $ moira_dead = False
    $ premier_refus_moira_foret_4 = False

    menu :
        "Quel est cet endroit ?":
            e "Où sommes-nous ?"

        "Ne rien dire":
            e "..."

        "C'est magnifique":
            e "C'est un très bel endroit. Est-ce que..."

    show moira debout_souriant_mid at right
    "Moira pousse doucement Einar contre un arbre."
    "Elle recule de quelques pas, puis se retourne."
    hide moira with dissolve
    "Elle se dénude lentement devant Einar, sans le regarder."
    show moira nue_normal_mid at right with dissolve

    menu :

        "C'est l'occasion de me débarrasser d'elle et de foutre le camp ! (Tuer Moira)":
            stop music
            e "(Je n'aurai pas deux occasions comme celle là. Je dois rentrer au château et assurer mes arrières.)"
            "Einar approche silencieusement dans le dos de Moira, puis plaque ses mains autour du cou de la jeune femme."
            show einar debout_determine_close at left
            show moira nue_effraye_close at right
            "Elle se débat, comprenant qu'elle vient d'être trahie. Sa respiration devient de plus en plus sifflante."
            "Son visage devient violacé et elle se convulse, avant de tomber au sol, inerte."
            hide moira with dissolve
            show einar debout_souriant_close at left
            e "Il est temps pour moi de retrouver les miens."
            $ moira_dead = True
            jump cote_2

        "C'est une occasion en or de s'enfuir (Fuir)":
            "Sans faire craquer la moindre brindille, Einar abandonne Moira au milieu de la forêt, s'éclipsant rapidement sous les frondaisons."
            hide einar with dissolve
            "..."
            show moira nue_normal_mid at right
            m "Einar ? Einar ?"
            $ premier_refus_moira_foret_4 = True
            jump cote_2

        "La regarder (Profiter du moment)":
            show moira nue_souriant_close at right
            show einar debout_normal_close at left
            "Moira s'approche sans bruit d'Einar, et commence à lui ôter ses vêtements."
            e "Tu..."
            m "Ne dis rien."
            show einar debout_souriant_close at left
            "Elle embrasse doucement Einar et commence à l'enlacer."
            "Les mains du guerrier parcourent le corps de la jeune femme et ressentent la douceur de sa peau, parfaite."
            "..."
            stop music
            jump village_4

    hide moira
    hide einar
    with dissolve

#Sequence 9
label village_4:

    play ambiance village

    scene bg village with dissolve

    "Le lendemain..."

    show ogma debout_normal_mid at right with dissolve
    o "Vous voilà prêt à partir, Einar."
    show einar debout_normal_mid at left with dissolve
    e "Je pense être prêt, oui. Mon matériel m'avait manqué !"
    show ogma debout_determine_mid at right
    o "Avant de vous souhaiter bonne route, je veux vous rappeler quelque chose. Vous nous avez fait une promesse."
    o "Nous vous avons soigné, nous nous sommes occupé de vous. Vous nous êtes redevable. Remplissez votre part du marché."
    o "Lorsque l'assaut aura commencé, je mènerai mes hommes au combat. Lorsque vous entendrez deux coups de cor successifs, vous ouvrirez le pont-levis du château."

    menu:

        "Je tiendrai ma promesse":
            show einar debout_normal_mid at left
            e "Je sais ce que j'ai à faire. Je ne pense qu'à ça depuis plus d'un mois."

        "Je n'ai pas le choix : je vais faire ce que vous voulez":
            show einar debout_determine_mid at left
            e "Je vous suis reconnaissant pour tout ce que vous avez fait. J'accomplirai ma promesse, même si ce n'est pas de gaieté de coeur."

        "Oui.":
            show einar debout_determine_mid at left
            e "Très bien."
    hide ogma with dissolve
    show moira debout_normal_mid at right with dissolve
    m "Tu as donné ta parole à mon père. S'il te plaît, ne me déçois pas..."
    "Moira s'approche d'Einar."

    menu :

        "(L'embrasser)":
            hide einar
            hide ogma
            hide moira
            show einar debout_souriant_close at left with dissolve
            show moira debout_souriant_close at right with dissolve
            "Einar embrasse doucement Moira en caressant son visage"

        "Je reviendrai, ne t'inquiète pas":
            hide einar
            hide ogma
            hide moira
            show einar debout_souriant_close at left with dissolve
            show moira debout_souriant_close at right with dissolve
            "Einar saisit Moira par les hanches et l'attire contre lui, puis l'enlace."
            e "Ne t'inquiète pas. Je reviendrai."

        "(L'ignorer)":
            hide ogma with dissolve
            hide moira with dissolve
            "Einar se retourne et, sans un regard pour la jeune femme, commence à s'éloigner."
            hide einar with dissolve


    hide moira
    hide einar
    with dissolve

    if short_version:
        jump cote_2
    else:
        jump sentier_foret_1

#Sequence 10
label sentier_foret_1:

    play ambiance wood

    scene bg sentier_jour with dissolve
    "Chemin faisant, Einar tente de remettre en perspective les événements récents et leurs implications..."
    show einar debout_normal_close with dissolve
    e "(Tout ce temps passé à Perth avec ces gens, avec Moira... Ils ont été bons pour moi. Mais je ne peux pas oublier le massacre, l'embuscade, Logan. Quoi qu'il arrive, je devrai trahir l'une des paroles que j'ai donné.)"

    menu :
        "Harald mérite ma fidélité":
            e "(Harald est mon seigneur et celui de tout le monde connu, y comprit les rebelles. Je lui dois tout depuis de très nombreuses années. Le trahir est impensable.)"
        "Harald ne m'a jamais offert les récompenses promises":
            e "(Le roi m'a fait miroiter des terres et des richesses depuis si longtemps... Sans jamais récompenser mes efforts à leur juste valeur. Pourquoi respecter mes engagements pour un roi qui ne respecte pas les siens ?)"
        "L'oppression des écossais est révoltante":
            e "(Ces gens vivent dans la pauvreté et n'ont fait que se défendre face à un oppresseur. Ils m'ont sauvé. Mais le meurtre lâche de mes hommes et de Logan...)"
            e "(Tout ceci n'a été qu'un enchaînement malheureux d'événements qui n'arrangent personne. Le seul vrai coupable, c'était l'intendant Clyde Montgomery. Et il est mort.)"
    hide einar with dissolve
    jump foret_5

label foret_5:
    scene bg forest_night with dissolve
    "Sans y prêter attention, Einar se rapproche peu à peu de Dunbar, toujours absorbé par ses pensées."
    show einar debout_normal_close with dissolve
    "(Moira a fait beaucoup pour moi, quoi qu'elle en dise. Je n'avais pas rencontré une aussi bonne personne depuis longtemps...)"

    menu:
        "Je dois beaucoup à Moira":
            e "(Elle s'est occupée de moi pendant plus d'un mois, sans jamais se montrer lasse ni désagréable. Je lui dois beaucoup. Elle s'est attachée à moi. La décevoir serait terrible. )"
        "Elle n'a agit que sur les ordres de son père":
            e "(Elle ne s'est occupée de moi que parce que son père le lui avait demandé. Je me demande si notre petite escapade en forêt était aussi une idée de son père...)"
        "Ce n'était qu'une amourette":
            e "(J'ai bien profité d'elle. Elle a été attentionnée avec moi, bien que naïve. Mais ce n'est pas la première femme que je rencontre... Cette petite histoire ne représente que peu de choses face aux engagements d'un huscarl.)"

    hide einar with dissolve
    jump cote_1

#Sequence 11
label cote_1:

    play ambiance coast

    scene bg plaine_cotière_matin with dissolve
    "A quelques heures de marche de Dunbar..."
    show einar debout_determine_close with dissolve
    e "(Les événements à venir risquent de bouleverser l'équilibre du monde... Est-ce que la liberté d'un petit nombre de paysans peut prévaloir sur le futur de peuples entiers ?)"

    menu :

        "Trahir Harald risque d'entraîner la chute de l'empire":
            e "(Trahir Harald entraînera la mort d'un nombre incalculable d'hommes et de femmes. Le pouvoir de Harald vacillera en même temps que la stabilité politique du plus grand Empire connu.)"
            e "(Ce sera la porte ouverte à toutes les guerres, et des petits seigneurs ne tarderont pas à se comporter en vautours en se nourrissant sur la carcasse de l'empire décadent...)"
        "En trahissant Harald, je serai coincé en Ecosse":
            e "(En trahissant Harald, je m'expose à des représailles incessantes. Je serai traqué partout dans l'Empire. Mon seul abri sera l'Ecosse. D'un autre côté, je serai enfin suffisament riche pour avoir la vie que mon roi m'a promise depuis déjà longtemps... Pourvu qu'Ogma respecte sa parole, lui !)"
        "Je dois abandonner les écossais, pour ma propre survie":
            e "(Je n'ai pas d'autre choix que de faillir à ma promesse envers les rebelles. Ma vie en dépend, ainsi que celle de beaucoup d'autres. Tant pis pour la liberté de quelques paysans. Mais qu'arrivera-t-il à Moira ?)"

    hide einar with dissolve
    jump cote_2
