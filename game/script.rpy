# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
#Image représentant les personnages
#Einar
define e = Character('Einar', color="#e74c3c")

#Debout
image einar debout_normal = "einar_debout_nomal.png"
#image einar debout_souriant = "einar_debout_souriant.png"
#image einar debout_furieux = "einar_debout_furieux.png"
#image einar debout_attriste = "einar_debout_attriste.png"
#image einar debout_blesse = "einar_debout_blesse.png"
#image einar debout_contratrie = "einar_debout_contratrie.png"
#image einar debout_effraye = "einar_debout_effraye.png"
#image einar debout_determine = "einar_debout_determine.png"

#Combat
#image einar combat_normal = "einar_combat_normal.png"
#image einar combat_furieux = "einar_combat_furieux.png"
#image einar combat_blesse = "einar_combat_blesse.png"
#image einar combat_determine = "einar_debout_determine.png"

#Attaché
#image einar attache_normal = "einar_attache_nomal.png"
#image einar attache_souriant = "einar_attache_souriant.png"
#image einar attache_furieux = "einar_attache_furieux.png"
#image einar attache_attriste = "einar_attache_attriste.png"
#image einar attache_effraye = "einar_attache_effraye.png"
#image einar attache_determine = "einar_debout_determine.png"

#Général
#image einar general_determine = "einar_general_determine.png"

#Logan
define l = Character('Logan', color="#f1c40f")

#Debout
image logan debout_normal = "logan_debout_nomal.png"
#image logan debout_souriant = "logan_debout_souriant.png"
#image logan debout_attriste = "logan_debout_attriste.png"
#image logan debout_contratrie = "logan_debout_contratrie.png"
#image logan debout_determine = "logan_debout_determine.png"

#Combat
#image logan combat_normal = "logan_combat_normal.png"
#image logan combat_furieux = "logan_combat_furieux.png"
#image logan combat_blesse = "logan_combat_blesse.png"
#image logan combat_contratrie = "logan_combat_contratrie.png"
#image logan combat_determine = "logan_debout_determine.png"

#Harald
define h = Character('Harald', color="#3498db")
image harald debout_normal = "harald_debout_nomal.png"
#image harald debout_furieux = "harald_debout_furieux.png"
#image harald debout_blesse = "harald_debout_blesse.png"
#image harald debout_contratrie = "harald_debout_contratrie.png"
#image harald debout_determine = "harald_debout_determine.png"

#Combat Hache
#image harald combat_hache_normal = "harald_combat_hache_normal.png"
#image harald combat_hache_furieux = "harald_combat_hache_furieux.png"
#image harald combat_hache_blesse = "harald_combat_hache_blesse.png"
#image harald combat_hache_contratrie = "harald_combat_hache_contratrie.png"
#image harald combat_hache_determine = "harald_combat_hache_determine.png"

#Combat
#image harald combat_normal = "harald_combat_normal.png"
#image harald combat_furieux = "harald_combat_furieux.png"
#image harald combat_blesse = "harald_combat_blesse.png"
#image harald combat_contratrie = "harald_combat_contratrie.png"
#image harald combat_determine = "harald_debout_determine.png"

#Ogma
define o = Character('Ogma', color="#d35400")
image ogma normal = "ogma.png"

#Moira
define m = Character("Moira", color = "#f00")

#Debout
image moira debout_normal = "moira_debout_nomal.png"
#image moira debout_souriant = "moira_debout_souriant.png"
#image moira debout_furieux = "moira_debout_furieux.png"
#image moira debout_attriste = "moira_debout_attriste.png"
#image moira debout_blesse = "moira_debout_blesse.png"
#image moira debout_contratrie = "moira_debout_contratrie.png"
#image moira debout_effraye = "moira_debout_effraye.png"
#image moira debout_determine = "moira_debout_determine.png"

#nude
#image moira nue_normal = "moira_nue_nomal.png"
#image moira nue_souriant = "moira_nue_souriant.png"
#image moira nue_effraye = "moira_nue_effraye.png"

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
