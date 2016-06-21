# Vous pouvez placer le script de votre jeu dans ce fichier.

init :
    $ checkpoint = ""

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
#Image représentant les personnages

##Einar
define e = Character('Einar', color="#e74c3c", image="einar")

image side einar = "einar/einar_portrait.png"

#Debout

#mid
image einar debout_normal_mid = "einar/debout/einar_debout_normal_mid.png"
image einar debout_souriant_mid = "einar/debout/einar_debout_souriant_mid.png"
image einar debout_furieux_mid = "einar/debout/einar_debout_furieux_mid.png"
image einar debout_attriste_mid = "einar/debout/einar_debout_attriste_mid.png"
image einar debout_blesse_mid = "einar/debout/einar_debout_blesse_mid.png"
image einar debout_contrarie_mid = "einar/debout/einar_debout_contrarie_mid.png"
image einar debout_effraye_mid = "einar/debout/einar_debout_effraye_mid.png"
image einar debout_determine_mid = "einar/debout/einar_debout_determine_mid.png"

#close
image einar debout_normal_close = "einar/debout/einar_debout_normal_close.png"
image einar debout_souriant_close = "einar/debout/einar_debout_souriant_close.png"
image einar debout_furieux_close = "einar/debout/einar_debout_furieux_close.png"
image einar debout_attriste_close = "einar/debout/einar_debout_attriste_close.png"
image einar debout_blesse_close = "einar/debout/einar_debout_blesse_close.png"
image einar debout_contrarie_close = "einar/debout/einar_debout_contrarie_close.png"
image einar debout_effraye_close = "einar/debout/einar_debout_effraye_close.png"
image einar debout_determine_close = "einar/debout/einar_debout_determine_close.png"

#flip
image einar debout_determine_mid_flip = im.Flip("einar/debout/einar_debout_determine_mid.png", horizontal = True)
image einar debout_attriste_mid_flip = im.Flip("einar/debout/einar_debout_attriste_mid.png", horizontal = True)
image einar debout_normal_mid_flip = im.Flip("einar/debout/einar_debout_normal_mid.png", horizontal = True)
image einar debout_furieux_mid_flip = im.Flip("einar/debout/einar_debout_furieux_mid.png", horizontal = True)

image einar debout_determine_close_flip = im.Flip("einar/debout/einar_debout_determine_close.png", horizontal = True)
image einar debout_attriste_close_flip = im.Flip("einar/debout/einar_debout_attriste_close.png", horizontal = True)
image einar debout_normal_close_flip = im.Flip("einar/debout/einar_debout_normal_close.png", horizontal = True)
image einar debout_furieux_close_flip = im.Flip("einar/debout/einar_debout_furieux_close.png", horizontal = True)

#Combat

#mid
image einar combat_normal_mid = "einar/combat/einar_combat_normal_mid.png"
image einar combat_furieux_mid = "einar/combat/einar_combat_furieux_mid.png"
image einar combat_blesse_mid = "einar/combat/einar_combat_blesse_mid.png"
image einar combat_determine_mid = "einar/combat/einar_combat_determine_mid.png"

#close
image einar combat_normal_close = "einar/combat/einar_combat_normal_close.png"
image einar combat_furieux_close = "einar/combat/einar_combat_furieux_close.png"
image einar combat_blesse_close = "einar/combat/einar_combat_blesse_close.png"
image einar combat_determine_close = "einar/combat/einar_combat_determine_close.png"


#Combat Hache

#mid
image einar combat_hache_normal_mid = "einar/combat_hache/einar_combat_hache_normal_mid.png"
image einar combat_hache_furieux_mid = "einar/combat_hache/einar_combat_hache_furieux_mid.png"
image einar combat_hache_determine_mid = "einar/combat_hache/einar_combat_hache_determine_mid.png"

#close
image einar combat_hache_normal_close = "einar/combat_hache/einar_combat_hache_normal_close.png"
image einar combat_hache_furieux_close = "einar/combat_hache/einar_combat_hache_furieux_close.png"
image einar combat_hache_determine_close = "einar/combat_hache/einar_combat_hache_determine_close.png"

#combat
image einar combat_normal_mid_flip = im.Flip("einar/combat/einar_combat_normal_mid.png", horizontal = True)
image einar combat_determine_mid_flip = im.Flip("einar/combat/einar_combat_determine_mid.png", horizontal = True)
image einar combat_furieux_mid_flip = im.Flip("einar/combat/einar_combat_furieux_mid.png", horizontal = True)
image einar combat_blesse_mid_flip = im.Flip("einar/combat/einar_combat_blesse_mid.png", horizontal = True)

#combat hache
image einar combat_hache_normal_mid_flip = im.Flip("einar/combat_hache/einar_combat_hache_normal_mid.png", horizontal = True)

#Prisonnier
#mid
image einar prisonnier_attriste_mid = "einar/prisonnier/einar_prisonnier_attriste_mid.png"
image einar prisonnier_blesse_mid = "einar/prisonnier/einar_prisonnier_blesse_mid.png"
image einar prisonnier_contrarie_mid = "einar/prisonnier/einar_prisonnier_contrarie_mid.png"
image einar prisonnier_determine_mid = "einar/prisonnier/einar_prisonnier_determine_mid.png"
image einar prisonnier_effraye_mid = "einar/prisonnier/einar_prisonnier_effraye_mid.png"
image einar prisonnier_furieux_mid = "einar/prisonnier/einar_prisonnier_furieux_mid.png"
image einar prisonnier_normal_mid = "einar/prisonnier/einar_prisonnier_normal_mid.png"
image einar prisonnier_souriant_mid = "einar/prisonnier/einar_prisonnier_souriant_mid.png"

#close
image einar prisonnier_attriste_close = "einar/prisonnier/einar_prisonnier_attriste_close.png"
image einar prisonnier_blesse_close = "einar/prisonnier/einar_prisonnier_blesse_close.png"
image einar prisonnier_contrarie_close = "einar/prisonnier/einar_prisonnier_contrarie_close.png"
image einar prisonnier_determine_close = "einar/prisonnier/einar_prisonnier_determine_close.png"
image einar prisonnier_effraye_close = "einar/prisonnier/einar_prisonnier_effraye_close.png"
image einar prisonnier_furieux_close = "einar/prisonnier/einar_prisonnier_furieux_close.png"
image einar prisonnier_normal_close = "einar/prisonnier/einar_prisonnier_normal_close.png"
image einar prisonnier_souriant_close = "einar/prisonnier/einar_prisonnier_souriant_close.png"

#flip
image einar prisonnier_attriste_mid_flip = im.Flip("einar/prisonnier/einar_prisonnier_attriste_mid.png", horizontal = True)
image einar prisonnier_blesse_mid_flip = im.Flip("einar/prisonnier/einar_prisonnier_blesse_mid.png", horizontal = True)
image einar prisonnier_contrarie_mid_flip = im.Flip("einar/prisonnier/einar_prisonnier_contrarie_mid.png", horizontal = True)
image einar prisonnier_determine_mid_flip = im.Flip("einar/prisonnier/einar_prisonnier_determine_mid.png", horizontal = True)
image einar prisonnier_effraye_mid_flip = im.Flip("einar/prisonnier/einar_prisonnier_effraye_mid.png", horizontal = True)
image einar prisonnier_furieux_mid_flip = im.Flip("einar/prisonnier/einar_prisonnier_furieux_mid.png", horizontal = True)
image einar prisonnier_normal_mid_flip = im.Flip("einar/prisonnier/einar_prisonnier_normal_mid.png", horizontal = True)
image einar prisonnier_souriant_mid_flip = im.Flip("einar/prisonnier/einar_prisonnier_souriant_mid.png", horizontal = True)

image einar prisonnier_attriste_close_flip = im.Flip("einar/prisonnier/einar_prisonnier_attriste_close.png", horizontal = True)
image einar prisonnier_blesse_close_flip = im.Flip("einar/prisonnier/einar_prisonnier_blesse_close.png", horizontal = True)
image einar prisonnier_contrarie_close_flip = im.Flip("einar/prisonnier/einar_prisonnier_contrarie_close.png", horizontal = True)
image einar prisonnier_determine_close_flip = im.Flip("einar/prisonnier/einar_prisonnier_determine_close.png", horizontal = True)
image einar prisonnier_effraye_close_flip = im.Flip("einar/prisonnier/einar_prisonnier_effraye_close.png", horizontal = True)
image einar prisonnier_furieux_close_flip = im.Flip("einar/prisonnier/einar_prisonnier_furieux_close.png", horizontal = True)
image einar prisonnier_normal_close_flip = im.Flip("einar/prisonnier/einar_prisonnier_normal_close.png", horizontal = True)
image einar prisonnier_souriant_close_flip = im.Flip("einar/prisonnier/einar_prisonnier_souriant_close.png", horizontal = True)

#Général
image einar general_determine = "einar/general/einar_general_determine.png"
image einar general_determine_mid = "einar/general/einar_general_determine_mid.png"
image einar general_determine_close = "einar/general/einar_general_determine_close.png"


##Logan
define l = Character('Logan', color="#f1c40f", image="logan")

image side logan = "logan/logan_portrait.png"

#Debout

image logan debout_normal_mid = "logan/debout/logan_debout_normal_mid.png"
image logan debout_souriant_mid = "logan/debout/logan_debout_souriant_mid.png"
image logan debout_attriste_mid = "logan/debout/logan_debout_attriste_mid.png"
image logan debout_contrarie_mid = "logan/debout/logan_debout_contrarie_mid.png"
image logan debout_determine_mid = "logan/debout/logan_debout_determine_mid.png"

image logan debout_normal_close = "logan/debout/logan_debout_normal_close.png"
image logan debout_souriant_close = "logan/debout/logan_debout_souriant_close.png"
image logan debout_contrarie_close = "logan/debout/logan_debout_contrarie_close.png"
image logan debout_attriste_close = "logan/debout/logan_debout_attriste_close.png"
image logan debout_determine_close = "logan/debout/logan_debout_determine_close.png"

#Flip
#Mid
image logan debout_normal_mid_flip = im.Flip("logan/debout/logan_debout_normal_mid.png", horizontal = True)
image logan debout_souriant_mid_flip = im.Flip("logan/debout/logan_debout_souriant_mid.png", horizontal = True)
image logan debout_attriste_mid_flip = im.Flip("logan/debout/logan_debout_attriste_mid.png", horizontal = True)
image logan debout_contrarie_mid_flip = im.Flip("logan/debout/logan_debout_contrarie_mid.png", horizontal = True)
image logan debout_determine_mid_flip = im.Flip("logan/debout/logan_debout_determine_mid.png", horizontal = True)

#Close
image logan debout_normal_close_flip = im.Flip("logan/debout/logan_debout_normal_close.png", horizontal = True)
image logan debout_souriant_close_flip = im.Flip("logan/debout/logan_debout_souriant_close.png", horizontal = True)
image logan debout_contrarie_close_flip = im.Flip("logan/debout/logan_debout_contrarie_close.png", horizontal = True)
image logan debout_attriste_close_flip = im.Flip("logan/debout/logan_debout_attriste_close.png", horizontal = True)
image logan debout_determine_close_flip = im.Flip("logan/debout/logan_debout_determine_close.png", horizontal = True)

#Combat

#mid
image logan combat_normal_mid = "logan/combat/logan_combat_normal_mid.png"
image logan combat_blesse_mid = "logan/combat/logan_combat_blesse_mid.png"
image logan combat_determine_mid = "logan/combat/logan_combat_determine_mid.png"

#close
image logan combat_normal_close = "logan/combat/logan_combat_normal_close.png"
image logan combat_blesse_close = "logan/combat/logan_combat_blesse_close.png"
image logan combat_determine_close = "logan/combat/logan_combat_determine_close.png"

#Flip
#mid
image logan combat_normal_mid_flip = im.Flip("logan/combat/logan_combat_normal_mid.png", horizontal = True)
image logan combat_blesse_mid_flip = im.Flip("logan/combat/logan_combat_blesse_mid.png", horizontal = True)
image logan combat_determine_mid_flip = im.Flip("logan/combat/logan_combat_determine_mid.png", horizontal = True)

#close
image logan combat_normal_close_flip = im.Flip("logan/combat/logan_combat_normal_close.png", horizontal = True)
image logan combat_blesse_close_flip = im.Flip("logan/combat/logan_combat_blesse_close.png", horizontal = True)
image logan combat_determine_close_flip = im.Flip("logan/combat/logan_combat_determine_close.png", horizontal = True)

##Harald
define h = Character('Harald', color="#3498db", image="harald")

image side harald = "harald/harald_portrait.png"

image harald debout_normal_mid = "harald/debout/harald_debout_normal_mid.png"
image harald debout_furieux_mid = "harald/debout/harald_debout_furieux_mid.png"
image harald debout_contrarie_mid = "harald/debout/harald_debout_contrarie_mid.png"
image harald debout_determine_mid = "harald/debout/harald_debout_determine_mid.png"
image harald debout_sceptique_mid = "harald/debout/harald_debout_sceptique_mid.png"

image harald debout_normal_close = "harald/debout/harald_debout_normal_close.png"
image harald debout_furieux_close = "harald/debout/harald_debout_furieux_close.png"
image harald debout_contrarie_close = "harald/debout/harald_debout_contrarie_close.png"
image harald debout_determine_close = "harald/debout/harald_debout_determine_close.png"
image harald debout_sceptique_close = "harald/debout/harald_debout_sceptique_close.png"

#Combat Hache

#mid
image harald combat_hache_normal_mid = "harald/combat_hache/harald_combat_hache_normal_mid.png"
image harald combat_hache_furieux_mid = "harald/combat_hache/harald_combat_hache_furieux_mid.png"
image harald combat_hache_determine_mid = "harald/combat_hache/harald_combat_hache_determine_mid.png"

#close
image harald combat_hache_normal_close = "harald/combat_hache/harald_combat_hache_normal_close.png"
image harald combat_hache_furieux_close = "harald/combat_hache/harald_combat_hache_furieux_close.png"
image harald combat_hache_determine_close = "harald/combat_hache/harald_combat_hache_determine_close.png"

#Combat

#mid
image harald combat_normal_mid = "harald/combat/harald_combat_normal_mid.png"
image harald combat_furieux_mid = "harald/combat/harald_combat_furieux_mid.png"
image harald combat_blesse_mid = "harald/combat/harald_combat_blesse_mid.png"
image harald combat_determine_mid = "harald/combat/harald_combat_determine_mid.png"

#close
image harald combat_normal_close = "harald/combat/harald_combat_normal_close.png"
image harald combat_furieux_close = "harald/combat/harald_combat_furieux_close.png"
image harald combat_blesse_close = "harald/combat/harald_combat_blesse_close.png"
image harald combat_determine_close = "harald/combat/harald_combat_determine_close.png"

#Flip
image harald debout_normal_mid_flip = im.Flip("harald/debout/harald_debout_normal_mid.png", horizontal = True)
image harald debout_furieux_mid_flip = im.Flip("harald/debout/harald_debout_furieux_mid.png", horizontal = True)
image harald debout_contrarie_mid_flip = im.Flip("harald/debout/harald_debout_contrarie_mid.png", horizontal = True)
image harald debout_determine_mid_flip = im.Flip("harald/debout/harald_debout_determine_mid.png", horizontal = True)

image harald debout_normal_close_flip = im.Flip("harald/debout/harald_debout_normal_close.png", horizontal = True)
image harald debout_furieux_close_flip = im.Flip("harald/debout/harald_debout_furieux_close.png", horizontal = True)
image harald debout_contrarie_close_flip = im.Flip("harald/debout/harald_debout_contrarie_close.png", horizontal = True)
image harald debout_determine_close_flip = im.Flip("harald/debout/harald_debout_determine_close.png", horizontal = True)

#combat hache
#mid
image harald combat_hache_normal_mid_flip = im.Flip("harald/combat_hache/harald_combat_hache_normal_mid.png", horizontal = True)
image harald combat_hache_furieux_mid_flip = im.Flip("harald/combat_hache/harald_combat_hache_furieux_mid.png", horizontal = True)
image harald combat_hache_determine_mid_flip = im.Flip("harald/combat_hache/harald_combat_hache_determine_mid.png", horizontal = True)

#close
image harald combat_hache_normal_close_flip = im.Flip("harald/combat_hache/harald_combat_hache_normal_close.png", horizontal = True)
image harald combat_hache_furieux_close_flip = im.Flip("harald/combat_hache/harald_combat_hache_furieux_close.png", horizontal = True)
image harald combat_hache_determine_close_flip = im.Flip("harald/combat_hache/harald_combat_hache_determine_close.png", horizontal = True)

#combat
#mid
image harald combat_normal_mid_flip = im.Flip("harald/combat/harald_combat_normal_mid.png", horizontal = True)
image harald combat_furieux_mid_flip = im.Flip("harald/combat/harald_combat_furieux_mid.png", horizontal = True)
image harald combat_blesse_mid_flip = im.Flip("harald/combat/harald_combat_blesse_mid.png", horizontal = True)
image harald combat_determine_mid_flip = im.Flip("harald/combat/harald_combat_determine_mid.png", horizontal = True)

#close
image harald combat_normal_close_flip = im.Flip("harald/combat/harald_combat_normal_close.png", horizontal = True)
image harald combat_furieux_close_flip = im.Flip("harald/combat/harald_combat_furieux_close.png", horizontal = True)
image harald combat_blesse_close_flip = im.Flip("harald/combat/harald_combat_blesse_close.png", horizontal = True)
image harald combat_determine_close_flip = im.Flip("harald/combat/harald_combat_determine_close.png", horizontal = True)

##Huscarls
define hu = Character("Huscarls")

#Debout

image huscarls debout_normal_mid = "huscarls/debout/huscarls_debout_normaux_mid.png"
image huscarls debout_rire_mid = "huscarls/debout/huscarls_debout_rire_mid.png"

image huscarls debout_normal_close = "huscarls/debout/huscarls_debout_normaux_close.png"
image huscarls debout_rire_close = "huscarls/debout/huscarls_debout_rire_close.png"

#Combat

#mid
image huscarls combat_normal_mid = "huscarls/combat/huscarls_combat_normaux_mid.png"
image huscarls combat_enthousiaste_mid = "huscarls/combat/huscarls_combat_enthousiaste_mid.png"
image huscarls combat_furieux_mid = "huscarls/combat/huscarls_combat_furieux_mid.png"
image huscarls combat_inquiet_mid = "huscarls/combat/huscarls_combat_inquiets_mid.png"

#close
image huscarls combat_normal_close = "huscarls/combat/huscarls_combat_normaux_close.png"
image huscarls combat_enthousiaste_close = "huscarls/combat/huscarls_combat_enthousiaste_close.png"
image huscarls combat_furieux_close = "huscarls/combat/huscarls_combat_furieux_close.png"
image huscarls combat_inquiet_close = "huscarls/combat/huscarls_combat_inquiets_close.png"

##moira
define m = Character("moira", image="moira")

# image side moira = "moira/moira_portrait.png"

#Debout
# image moira debout_normal = "moira/debout/moira_debout_normaux.png"
# image moira debout_rire = "moira/debout/moira_debout_rire.png"
#
# image moira debout_normal_mid = "moira/debout/moira_debout_normaux_mid.png"
# image moira debout_rire_mid = "moira/debout/moira_debout_rire_mid.png"
#
# image moira debout_normal_close = "moira/debout/moira_debout_normaux_close.png"
# image moira debout_rire_close = "moira/debout/moira_debout_rire_close.png"
#

##Garde / Guerriers Vikings / Jeune Guerrier Viking
define gv = Character('Guerriers Vikings', color="#e67e22", image="guerriers_vikings")

# image side guerriers_vikings = "guerriers_vikings/guerriers_vikings_portrait.png"


define gc = Character("Garde du Château", image="guerriers_vikings")

# image side guerriers_vikings = "guerriers_vikings/guerriers_vikings_portrait.png"


define jgv = Character("Jeune Guerrier Viking", image="jeune_viking")

# image side guerriers_vikings = "jeune_viking/jeune_viking_portrait.png"

#Debout

image gv debout_normaux_mid = "guerriers_vikings/debout/gv_debout_normaux_mid.png"
image gv debout_enthousiaste_mid = "guerriers_vikings/debout/gv_debout_enthousiastes_mid.png"
image gv debout_furieux_mid = "guerriers_vikings/debout/gv_debout_furieux_mid.png"
image gv debout_rire_mid = "guerriers_vikings/debout/gv_debout_rire_mid.png"
image gv debout_contrarie_mid = "guerriers_vikings/debout/gv_debout_contraries_mid.png"
image gv debout_determines_mid = "guerriers_vikings/debout/gv_debout_determines_mid.png"

image gv debout_normaux_close = "guerriers_vikings/debout/gv_debout_normaux_close.png"
image gv debout_enthousiaste_close = "guerriers_vikings/debout/gv_debout_enthousiastes_close.png"
image gv debout_furieux_close = "guerriers_vikings/debout/gv_debout_furieux_close.png"
image gv debout_rire_close = "guerriers_vikings/debout/gv_debout_rire_close.png"
image gv debout_contrarie_close = "guerriers_vikings/debout/gv_debout_contraries_close.png"
image gv debout_determines_close = "guerriers_vikings/debout/gv_debout_determines_close.png"

image gv debout_normaux_mid_flip = im.Flip("guerriers_vikings/debout/gv_debout_normaux_mid.png", horizontal = True)
image gv debout_enthousiaste_mid_flip = im.Flip("guerriers_vikings/debout/gv_debout_enthousiastes_mid.png", horizontal = True)
image gv debout_furieux_mid_flip = im.Flip("guerriers_vikings/debout/gv_debout_furieux_mid.png", horizontal = True)
image gv debout_rire_mid_flip = im.Flip("guerriers_vikings/debout/gv_debout_rire_mid.png", horizontal = True)
image gv debout_contrarie_mid_flip = im.Flip("guerriers_vikings/debout/gv_debout_contraries_mid.png", horizontal = True)
image gv debout_determines_mid_flip = im.Flip("guerriers_vikings/debout/gv_debout_determines_mid.png", horizontal = True)

#Combat

#mid
image gv combat_normal_mid = "guerriers_vikings/combat/gv_combat_normaux_mid.png"
image gv combat_blesses_mid = "guerriers_vikings/combat/gv_combat_blesses_mid.png"

#close
image gv combat_normal_close = "guerriers_vikings/combat/gv_combat_normaux_close.png"
image gv combat_blesses_close = "guerriers_vikings/combat/gv_combat_blesses_close.png"

#Jeune Guerrier Viking

image jgv debout_normal_mid = "jeune_viking/debout/jgv_debout_normal_mid.png"
image jgv debout_pleurant_mid = "jeune_viking/debout/jgv_debout_pleurant_mid.png"

image jgv debout_normal_close = "jeune_viking/debout/jgv_debout_normal_close.png"
image jgv debout_pleurant_close = "jeune_viking/debout/jgv_debout_pleurant_close.png"

##Ogma
define o = Character('Ogma', color="#d35400", image="ogma")

image side ogma = "ogma/ogma_portrait.png"

#Debout

#mid
image ogma debout_normal_mid = "ogma/debout/ogma_debout_normal_mid.png"
image ogma debout_souriant_mid = "ogma/debout/ogma_debout_souriant_mid.png"
image ogma debout_furieux_mid = "ogma/debout/ogma_debout_furieux_mid.png"
image ogma debout_attriste_mid = "ogma/debout/ogma_debout_attriste_mid.png"
image ogma debout_contrarie_mid = "ogma/debout/ogma_debout_contrarie_mid.png"
image ogma debout_determine_mid = "ogma/debout/ogma_debout_determine_mid.png"

#close
image ogma debout_normal_close = "ogma/debout/ogma_debout_normal_close.png"
image ogma debout_souriant_close = "ogma/debout/ogma_debout_souriant_close.png"
image ogma debout_furieux_close = "ogma/debout/ogma_debout_furieux_close.png"
image ogma debout_attriste_close = "ogma/debout/ogma_debout_attriste_close.png"
image ogma debout_contrarie_close = "ogma/debout/ogma_debout_contrarie_close.png"
image ogma debout_determine_close = "ogma/debout/ogma_debout_determine_close.png"

#Flip
image ogma debout_normal_mid_flip = im.Flip("ogma/debout/ogma_debout_normal_mid.png", horizontal = True)
image ogma debout_souriant_mid_flip = im.Flip("ogma/debout/ogma_debout_normal_mid.png", horizontal = True)
image ogma debout_furieux_mid_flip = im.Flip("ogma/debout/ogma_debout_normal_mid.png", horizontal = True)
image ogma debout_attriste_mid_flip = im.Flip("ogma/debout/ogma_debout_normal_mid.png", horizontal = True)
image ogma debout_contrarie_mid_flip = im.Flip("ogma/debout/ogma_debout_normal_mid.png", horizontal = True)
image ogma debout_determine_mid_flip = im.Flip("ogma/debout/ogma_debout_normal_mid.png", horizontal = True)


#Combat

#mid
image ogma combat_normal_mid = "ogma/combat/ogma_combat_normal_mid.png"
image ogma combat_furieux_mid = "ogma/combat/ogma_combat_furieux_mid.png"
image ogma combat_contrarie_mid = "ogma/combat/ogma_combat_contrarie_mid.png"
image ogma combat_determine_mid = "ogma/combat/ogma_combat_determine_mid.png"
image ogma combat_surpris_mid = "ogma/combat/ogma_combat_surpris_mid.png"

#close
image ogma combat_normal_close = "ogma/combat/ogma_combat_normal_close.png"
image ogma combat_furieux_close = "ogma/combat/ogma_combat_furieux_close.png"
image ogma combat_contrarie_close = "ogma/combat/ogma_combat_contrarie_close.png"
image ogma combat_determine_close = "ogma/combat/ogma_combat_determine_close.png"
image ogma combat_surpris_close = "ogma/combat/ogma_combat_surpris_close.png"

#flip
image ogma combat_normal_mid_flip = im.Flip("ogma/combat/ogma_combat_normal_mid.png", horizontal = True)
image ogma combat_determine_mid_flip = im.Flip("ogma/combat/ogma_combat_determine_mid.png", horizontal = True)
image ogma combat_furieux_mid_flip = im.Flip("ogma/combat/ogma_combat_furieux_mid.png", horizontal = True)
image ogma combat_contrarie_mid_flip = im.Flip("ogma/combat/ogma_combat_contrarie_mid.png", horizontal = True)
image ogma combat_surpris_mid_flip = im.Flip("ogma/combat/ogma_combat_surpris_mid.png", horizontal = True)

#Combat Hache

#mid
image ogma combat_hache_brandir_mid = "ogma/combat_hache/ogma_combat_hache_brandir_mid.png"
image ogma combat_hache_determine_mid = "ogma/combat_hache/ogma_combat_hache_determine_mid.png"

#close
image ogma combat_hache_brandir_close = "ogma/combat_hache/ogma_combat_hache_brandir_close.png"
image ogma combat_hache_determine_close = "ogma/combat_hache/ogma_combat_hache_determine_close.png"

##Moira
define m = Character("Moira", color = "#f00", image="moira")

# image side moira = "moira/moira_portrait.png"

#Debout

image moira debout_normal_mid = "moira/debout/moira_debout_normal_mid.png"
image moira debout_souriant_mid = "moira/debout/moira_debout_souriant_mid.png"
image moira debout_furieux_mid = "moira/debout/moira_debout_furieux_mid.png"
image moira debout_attriste_mid = "moira/debout/moira_debout_attriste_mid.png"
image moira debout_contrarie_mid = "moira/debout/moira_debout_contrarie_mid.png"
image moira debout_effraye_mid = "moira/debout/moira_debout_effraye_mid.png"
image moira debout_determine_mid = "moira/debout/moira_debout_determine_mid.png"

image moira debout_normal_close = "moira/debout/moira_debout_normal_close.png"
image moira debout_souriant_close = "moira/debout/moira_debout_souriant_close.png"
image moira debout_furieux_close = "moira/debout/moira_debout_furieux_close.png"
image moira debout_attriste_close = "moira/debout/moira_debout_attriste_close.png"
image moira debout_contrarie_close = "moira/debout/moira_debout_contrarie_close.png"
image moira debout_effraye_close = "moira/debout/moira_debout_effraye_close.png"
image moira debout_determine_close = "moira/debout/moira_debout_determine_close.png"

#Flip
image moira debout_normal_mid_flip = im.Flip("moira/debout/moira_debout_normal_mid.png", horizontal = True)
image moira debout_souriant_mid_flip = im.Flip("moira/debout/moira_debout_souriant_mid.png", horizontal = True)
image moira debout_furieux_mid_flip = im.Flip("moira/debout/moira_debout_furieux_mid.png", horizontal = True)
image moira debout_attriste_mid_flip = im.Flip("moira/debout/moira_debout_attriste_mid.png", horizontal = True)
image moira debout_contrarie_mid_flip = im.Flip("moira/debout/moira_debout_contrarie_mid.png", horizontal = True)
image moira debout_effraye_mid_flip = im.Flip("moira/debout/moira_debout_effraye_mid.png", horizontal = True)
image moira debout_determine_mid_flip = im.Flip("moira/debout/moira_debout_determine_mid.png", horizontal = True)

image moira debout_normal_close_flip = im.Flip("moira/debout/moira_debout_normal_close.png", horizontal = True)
image moira debout_souriant_close_flip = im.Flip("moira/debout/moira_debout_souriant_close.png", horizontal = True)
image moira debout_furieux_close_flip = im.Flip("moira/debout/moira_debout_furieux_close.png", horizontal = True)
image moira debout_attriste_close_flip = im.Flip("moira/debout/moira_debout_attriste_close.png", horizontal = True)
image moira debout_contrarie_close_flip = im.Flip("moira/debout/moira_debout_contrarie_close.png", horizontal = True)
image moira debout_effraye_close_flip = im.Flip("moira/debout/moira_debout_effraye_close.png", horizontal = True)
image moira debout_determine_close_flip = im.Flip("moira/debout/moira_debout_determine_close.png", horizontal = True)

image moira nue_normal_mid_flip = im.Flip("moira/nue/moira_nue_normale_mid.png", horizontal = True)
image moira nue_souriant_mid_flip = im.Flip("moira/nue/moira_nue_souriant_mid.png", horizontal = True)
image moira nue_effraye_mid_flip = im.Flip("moira/nue/moira_nue_effraye_mid.png", horizontal = True)

image moira nue_normal_close_flip = im.Flip("moira/nue/moira_nue_normale_close.png", horizontal = True)
image moira nue_souriant_close_flip = im.Flip("moira/nue/moira_nue_souriant_close.png", horizontal = True)
image moira nue_effraye_close_flip = im.Flip("moira/nue/moira_nue_effraye_close.png", horizontal = True)


#nude

image moira nue_normal_mid = "moira/nue/moira_nue_normale_mid.png"
image moira nue_souriant_mid = "moira/nue/moira_nue_souriant_mid.png"
image moira nue_effraye_mid = "moira/nue/moira_nue_effraye_mid.png"

image moira nue_normal_close = "moira/nue/moira_nue_normale_close.png"
image moira nue_souriant_close = "moira/nue/moira_nue_souriant_close.png"
image moira nue_effraye_close = "moira/nue/moira_nue_effraye_close.png"

#Attache

#mid
image moira attache_determine_mid = "moira/buchet/moira_attache_determine_mid.png"
image moira attache_furieuse_mid = "moira/buchet/moira_attache_furieuse_mid.png"

#close
image moira attache_determine_close = "moira/buchet/moira_attache_determine_close.png"
image moira attache_furieuse_close = "moira/buchet/moira_attache_furieuse_close.png"

##Rebelles ecossais
define ge = Character('rebelles écossais', color="#f39c12", image="rebelles_ecossais")

# image side rebelles_ecossais = "rebelles_ecossais/rebelles_ecossais_portrait.png"

#Debout
image re debout_normaux_mid = "rebelles_ecossais/debout/re_debout_normaux_mid.png"
image re debout_normaux_close = "rebelles_ecossais/debout/re_debout_normaux_close.png"

#Combat
#mid
image re combat_normal_mid = "rebelles_ecossais/combat/re_combat_normaux_mid.png"
image re combat_furieux_mid = "rebelles_ecossais/combat/re_combat_furieux_mid.png"

#close
image re combat_normal_close = "rebelles_ecossais/combat/re_combat_normaux_close.png"
image re combat_furieux_close = "rebelles_ecossais/combat/re_combat_furieux_close.png"

#Flip
image re debout_normal_mid_flip = im.Flip("rebelles_ecossais/debout/re_debout_normaux_mid.png", horizontal = True)
image re debout_normal_close_flip = im.Flip("rebelles_ecossais/debout/re_debout_normaux_close.png", horizontal = True)

#Combat
#mid
image re combat_normal_mid_flip= im.Flip("rebelles_ecossais/combat/re_combat_normaux_mid.png", horizontal = True)
image re combat_furieux_mid_flip = im.Flip("rebelles_ecossais/combat/re_combat_furieux_mid.png", horizontal = True)

#close
image re combat_normal_close_flip = im.Flip("rebelles_ecossais/combat/re_combat_normaux_close.png", horizontal = True)
image re combat_furieux_close_flip = im.Flip("rebelles_ecossais/combat/re_combat_furieux_close.png", horizontal = True)


##Villageois / prisonniers
define ve = Character('{color=#3498db}Villageois{/color}', color="#3498db", image="villageois")

# image side villageois = "villageois/villageois_portrait.png"

define pe1 = Character("Prisonnier écossais 1", image="villageois_ecossais")
define pe2 = Character("Prisonnier écossais 2", image="villageois_ecossais")
define pe3 = Character("Prisonnière écossaise 1", image="villageois_ecossais")

# image side villageois_ecossais = "villageois_ecossais/villageois_ecossais_portrait.png"

#Debout

image ve debout_normaux_mid = "villageois_ecossais/debout/ve_debout_normaux_mid.png"
image ve debout_craintifs_mid = "villageois_ecossais/debout/ve_debout_craintifs_mid.png"
image ve debout_effrayes_mid = "villageois_ecossais/debout/ve_debout_effrayes_mid.png"

image ve debout_normaux_close = "villageois_ecossais/debout/ve_debout_normaux_close.png"
image ve debout_craintifs_close = "villageois_ecossais/debout/ve_debout_craintifs_close.png"
image ve debout_effrayes_close = "villageois_ecossais/debout/ve_debout_effrayes_close.png"

#Buchet
image ve buchet_normaux_mid = "villageois_ecossais/buchet/ve_buchet_effrayes_mid.png"
image ve buchet_pleurent_mid = "villageois_ecossais/buchet/ve_buchet_pleurent_mid.png"

image ve buchet_normaux_close = "villageois_ecossais/buchet/ve_buchet_effrayes_close.png"
image ve buchet_pleurent_close = "villageois_ecossais/buchet/ve_buchet_pleurent_close.png"

##Patrick
define p = Character("Patrick", image="patrick")

# image side patrick = "patrick/patrick_portrait.png"

image patrick debout_normal_mid = "patrick/debout/patrick_debout_normal_mid.png"

image patrick debout_normal_close = "patrick/debout/patrick_debout_normal_close.png"

#Flip
image patrick debout_normal_mid_flip = im.Flip("patrick/debout/patrick_debout_normal_mid.png", horizontal = True)

image patrick debout_normal_close_flip = im.Flip("patrick/debout/patrick_debout_normal_close.png", horizontal = True)

#Scene

##Forest
#forest
image bg forest = "scenes/foretWestruther_ext_jour_foret.jpg"
image bg forest_night = "scenes/foretWestruther_ext_nuit_foret.png"
image bg forest_crepuscule = "scenes/foretWestruther_ext_aube_foret.png"
image bg little_heaven = "scenes/foretWestruther_ext_matin_paradis.png"

#sentier
image bg sentier_jour = "scenes/foretWestruther_ext_matin_sentier.png"

#Village
#exterior
image bg village = "scenes/perth_ext_jour_village.png"
image bg village_crepuscule = "scenes/perth_ext_crepuscule_village.png"
#ogma house
image bg house = "scenes/perth_int_jour_maison.png"
image bg house2_jour = "scenes/perth_int_jour_maison.png"
image bg house2_night = "scenes/perth_int_nuit_maison.png"
image bg house2_aube = "scenes/perth_int_jour_maison.png"

##Plaine cotière
image bg plaine_cotière_matin = "scenes/plaine_ext_matin_plaineCotiere.png"
image bg plaine_cotiere_crepuscule = "scenes/plaine_ext_crepuscule_plaineCotiere.png."
image bg plaine_chateau_matin = "scenes/plaine_ext_matin_plaineChateau.png"
image bg plaine_chateau_crepuscule = "scenes/plaine_ext_crepuscule_plaineCotiereChateau.png"

#plaine
image bg plaine_plaine_matin = "scenes/plaine_ext_matin_plaine.png"
image bg plaine_plaine_crepuscule = "scenes/plaine_ext_crepuscule_plaine.png"

##Chateau
#pont-levis
image bg pont_levis = "scenes/pont_levis.jpg"
#porte chateau
image bg chateau_porte = "scenes/chateauDunbar_ext_jour_porte.png"
image bg chateau_porte_crepuscule = "scenes/chateauDunbar_ext_crepuscule_porte.png"
image bg chateau_porte_interieur_crepuscule = "scenes/chateauDunbar_ext_crepuscule_porte.png"
#remparts
image bg chateau_rempart_crepuscule = "scenes/chateauDunbar_ext_crepuscule_remparts.jpg"
image bg chateau_rempart_jour = "scenes/chateauDunbar_ext_jour_remparts.jpg"
#cour chateau
image bg cour_chateau = "scenes/chateauDunbar_ext_jour_cour.png"
image bg cour_chateau_crepuscule = "scenes/chateauDunbar_ext_crepuscule_cour.png"
#couloirs
image bg chateau_couloir_crepuscule = "scenes/chateauDunbar_int_crepuscule_couloir.png"
#chambre Harald
image bg chateau_chambre_nuit = "scenes/chateauDunbar_int_nuit_chambreHarald.png"
#Salle banquet
image bg chateau_banquet = "scenes/chateauDunbar_int_salleBanque.png"

#Fond uni
image bg black = "#000"

#VFX

image vfx_flame_1 flame = "vfx/flame.png"
image vfx_flame_2 flame = "vfx/flame.png"
image vfx_flame_3 flame = "vfx/flame.png"

# sounds

#musics
define audio.nature = "sounds/musics/music_travelling_in_nature.mp3"
define audio.romance ="sounds/musics/music_romance.mp3"
define audio.weird_village = "sounds/musics/music_village_weird.mp3"
define audio.slaughter = "sounds/musics/music_drama_slaughter.mp3"
#define audio.drama_slaughter = "sounds/musics/music_drama_slaughter.wav"

#SFX
define audio.blade_1 = "sounds/sfx/SFX_Blade1.mp3"
define audio.blade_2 = "sounds/sfx/SFX_Blade2.mp3"
define audio.war_horn = "sounds/sfx/SFX_WarHorn.mp3"
define audio.double_horn = "sounds/sfx/SFX_Double_WarHorn.mp3"
define audio.drawbrigde = "sounds/sfx/SFX_Drawbridge_Down.mp3"
define audio.hurt_man_1 = "sounds/sfx/SFX_Hurt_Man.mp3"
define audio.hurt_man_2 = "sounds/sfx/SFX_Hurt_Man2.mp3"
define audio.hurt_man_3 = "sounds/sfx/SFX_Hurt_Man3.mp3"

#ambiance
define audio.burning_dungeon = "sounds/ambiances/ambiance_burning_dungeonkeep.mp3"
define audio.coast = "sounds/ambiances/ambiance_coast.mp3"
define audio.fight = "sounds/ambiances/ambiance_fight.mp3"
define audio.magnificente_wood = "sounds/ambiances/ambiance_magnificent_woods.mp3"
define audio.home = "sounds/ambiances/ambiance_maison.mp3"
define audio.village = "sounds/ambiances/ambiance_village.mp3"
define audio.wood_night = "sounds/ambiances/ambiance_wood_night.mp3"
define audio.wood = "sounds/ambiances/ambiance_woods.mp3"

#transform
transform halfsize :
    zoom 0.5

transform shake:
        ease .06 yoffset 24
        ease .06 yoffset -24
        ease .05 yoffset 20
        ease .05 yoffset -20
        ease .04 yoffset 16
        ease .04 yoffset -16
        ease .03 yoffset 12
        ease .03 yoffset -12
        ease .02 yoffset 8
        ease .02 yoffset -8
        ease .01 yoffset 4
        ease .01 yoffset -4
        ease .01 yoffset 0

transform burn:
    ease 0.5 alpha 0.4
    ease 0.3 alpha 0.2
    ease 0.5 alpha 0.5
    ease 0.1 alpha 0.6
    ease 0.5 alpha 0.4
    ease 0.5 alpha 0.5
    repeat

transform ve_pos:
    xoffset 590

transform ogma_pos_left:
    xoffset -300

transform ogma_pos_right:
    xoffset 850

transform ogma_pos_reset:
    xoffset - 300

#Déclaration timer
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve

# Le jeu commence ici

label start:

    scene bg black

    if short_version:
        centered "C'est la version courte"
    else:
        centered "C'est la version longue"


    centered "En l'an 1038, Harald Sigurdsson de Norvège, garde varègue au service de l'impératrice de Constantinople, s'empare des Clous de la Sainte Croix à Jérusalem."

    centered "Les Clous donnent à Harald la force et l'immortalité. Le viking, convaincu d'être un élu divin, décide d'orner sa hache des Clous. Il créé ainsi une nouvelle relique : la Hache Sainte."

    centered "Revenu triomphalement en Norvège, il est couronné roi et entame de grandes campagnes militaires visant à christianiser le monde ainsi qu'à asseoir sa suprématie."

    centered "Armé de la Hache Sainte, Harald prend le contrôle de l'Europe, du Moyen-Orient et d'une partie de l'Asie et de l'Afrique. En 1080, Harald est devenu l'équivalent d'Alexandre le Grand : un roi-empereur, une légende vivante, un demi-dieu."

    centered "Nous sommes en 1082. Des paysans écossais ont tué Clyde Montgomery, l'intendant que Harald avait placé à la tête de l'Ecosse. Le roi-empereur a décidé de revenir mater cette petite rébellion et d’en faire un exemple."

    jump intro
