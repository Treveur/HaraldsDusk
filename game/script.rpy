# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
#Image représentant les personnages

init -1500 python:

    class StartL(Action, DictEquality):
        """
         :doc: menu_action

         Causes Ren'Py to jump out of the menu context to the named
         label. The main use of this is to start a new game from the
         main menu. Common uses are:

         * Start() - Start at the start label.
         * Start("foo") - Start at the "foo" label.
         """

        def __init__(self, label="start_l"):
            self.label = label

        def __call__(self):
            renpy.jump_out_of_context(self.label)

    class StartS(Action, DictEquality):
        """
         :doc: menu_action

         Causes Ren'Py to jump out of the menu context to the named
         label. The main use of this is to start a new game from the
         main menu. Common uses are:

         * Start() - Start at the start label.
         * Start("foo") - Start at the "foo" label.
         """

        def __init__(self, label="start_s"):
            self.label = label

        def __call__(self):
            renpy.jump_out_of_context(self.label)


##Einar
define e = Character('Einar', color="#e74c3c")

#Debout
image einar debout_normal = "einar/debout/einar_debout_normal.png"
image einar debout_souriant = "einar/debout/einar_debout_souriant.png"
image einar debout_furieux = "einar/debout/einar_debout_furieux.png"
image einar debout_attriste = "einar/debout/einar_debout_attriste.png"
image einar debout_blesse = "einar/debout/einar_debout_blesse.png"
image einar debout_contrarie = "einar/debout/einar_debout_contrarie.png"
image einar debout_effraye = "einar/debout/einar_debout_effraye.png"
image einar debout_determine = "einar/debout/einar_debout_determine.png"

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


#Combat
image einar combat_normal = "einar/combat/einar_combat_normal.png"
image einar combat_furieux = "einar/combat/einar_combat_furieux.png"
image einar combat_blesse = "einar/combat/einar_combat_blesse.png"
image einar combat_determine = "einar/combat/einar_combat_determine.png"

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

#Combat
image einar combat_hache_normal = "einar/combat_hache/einar_combat_hache_normal.png"
image einar combat_hache_furieux = "einar/combat_hache/einar_combat_hache_furieux.png"
image einar combat_hache_determine = "einar/combat_hache/einar_combat_hache_determine.png"

#mid
image einar combat_hache_normal_mid = "einar/combat_hache/einar_combat_hache_normal_mid.png"
image einar combat_hache_furieux_mid = "einar/combat_hache/einar_combat_hache_furieux_mid.png"
image einar combat_hache_determine_mid = "einar/combat_hache/einar_combat_hache_determine_mid.png"

#close
image einar combat_hache_normal_close = "einar/combat_hache/einar_combat_hache_normal_close.png"
image einar combat_hache_furieux_close = "einar/combat_hache/einar_combat_hache_furieux_close.png"
image einar combat_hache_determine_close = "einar/combat_hache/einar_combat_hache_determine_close.png"

#Général
image einar general_determine = "einar/general/einar_general_determine.png"
image einar general_determine_mid = "einar/general/einar_general_determine_mid.png"
image einar general_determine_close = "einar/general/einar_general_determine_close.png"


##Logan
define l = Character('Logan', color="#f1c40f")

#Debout
image logan debout_normal = "logan/debout/logan_debout_normal.png"
image logan debout_souriant = "logan/debout/logan_debout_souriant.png"
image logan debout_attriste = "logan/debout/logan_debout_attriste.png"
image logan debout_contrarie = "logan/debout/logan_debout_contrarie.png"
image logan debout_determine = "logan/debout/logan_debout_determine.png"

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
image logan debout_souriant_flip_mid = im.Flip("logan/debout/logan_debout_souriant_mid.png", horizontal = True)

#Combat
image logan combat_normal = "logan/combat/logan_combat_normal.png"
image logan combat_blesse = "logan/combat/logan_combat_blesse.png"
image logan combat_determine = "logan/combat/logan_combat_determine.png"

#mid
image logan combat_normal_mid = "logan/combat/logan_combat_normal_mid.png"
image logan combat_blesse_mid = "logan/combat/logan_combat_blesse_mid.png"
image logan combat_determine_mid = "logan/combat/logan_combat_determine_mid.png"

#close
image logan combat_normal_close = "logan/combat/logan_combat_normal_close.png"
image logan combat_blesse_close = "logan/combat/logan_combat_blesse_close.png"
image logan combat_determine_close = "logan/combat/logan_combat_determine_close.png"

##Harald
define h = Character('Harald', color="#3498db")

image harald debout_normal = "harald/debout/harald_debout_normal.png"
image harald debout_furieux = "harald/debout/harald_debout_furieux.png"
#image harald debout_blesse = "harald/noraml/harald_debout_blesse.png"
image harald debout_contrarie = "harald/debout/harald_debout_contrarie.png"
image harald debout_determine = "harald/debout/harald_debout_determine.png"

image harald debout_normal_mid = "harald/debout/harald_debout_normal_mid.png"
image harald debout_furieux_mid = "harald/debout/harald_debout_furieux_mid.png"
image harald debout_contrarie_mid = "harald/debout/harald_debout_contrarie_mid.png"
image harald debout_determine_mid = "harald/debout/harald_debout_determine_mid.png"

image harald debout_normal_close = "harald/debout/harald_debout_normal_close.png"
image harald debout_furieux_close = "harald/debout/harald_debout_furieux_close.png"
image harald debout_contrarie_close = "harald/debout/harald_debout_contrarie_close.png"
image harald debout_determine_close = "harald/debout/harald_debout_determine_close.png"

#Combat Hache
image harald combat_hache_normal = "harald/combat_hache/harald_combat_hache_normal.png"
image harald combat_hache_furieux = "harald/combat_hache/harald_combat_hache_furieux.png"
#image harald combat_hache_contrarie = "harald/combat_hache/harald_combat_hache_contrarie.png"
image harald combat_hache_determine = "harald/combat_hache/harald_combat_hache_determine.png"

#mid
image harald combat_hache_normal_mid = "harald/combat_hache/harald_combat_hache_normal_mid.png"
image harald combat_hache_furieux_mid = "harald/combat_hache/harald_combat_hache_furieux_mid.png"
#image harald combat_hache_contrarie_mid = "harald/combat_hache/harald_combat_hache_contrarie_mid.png"
image harald combat_hache_determine_mid = "harald/combat_hache/harald_combat_hache_determine_mid.png"

#close
image harald combat_hache_normal_close = "harald/combat_hache/harald_combat_hache_normal_close.png"
image harald combat_hache_furieux_close = "harald/combat_hache/harald_combat_hache_furieux_close.png"
#image harald combat_hache_contrarie_close = "harald/combat_hache/harald_combat_hache_contrarie_close.png"
image harald combat_hache_determine_close = "harald/combat_hache/harald_combat_hache_determine_close.png"

#Combat
image harald combat_normal = "harald/combat/harald_combat_normal.png"
image harald combat_furieux = "harald/combat/harald_combat_furieux.png"
image harald combat_blesse = "harald/combat/harald_combat_blesse.png"
#image harald combat_contrarie = "harald/combat/harald_combat_contrarie.png"
image harald combat_determine = "harald/combat/harald_combat_determine.png"

#mid
image harald combat_normal_mid = "harald/combat/harald_combat_normal_mid.png"
image harald combat_furieux_mid = "harald/combat/harald_combat_furieux_mid.png"
image harald combat_blesse_mid = "harald/combat/harald_combat_blesse_mid.png"
#image harald combat_contrarie_mid = "harald/combat/harald_combat_contrarie_mid.png"
image harald combat_determine_mid = "harald/combat/harald_combat_determine_mid.png"

#close
image harald combat_normal_close = "harald/combat/harald_combat_normal_close.png"
image harald combat_furieux_close = "harald/combat/harald_combat_furieux_close.png"
image harald combat_blesse_close = "harald/combat/harald_combat_blesse_close.png"
#image harald combat_contrarie_close = "harald/combat/harald_combat_contrarie_close.png"
image harald combat_determine_close = "harald/combat/harald_combat_determine_close.png"

##Huscarls
define hu = Character("Huscarls")
#Debout
image huscarls debout_normal = "huscarls/debout/huscarls_debout_normaux.png"
image huscarls debout_rire = "huscarls/debout/huscarls_debout_rire.png"

image huscarls debout_normal_mid = "huscarls/debout/huscarls_debout_normaux_mid.png"
image huscarls debout_rire_mid = "huscarls/debout/huscarls_debout_rire_mid.png"

image huscarls debout_normal_close = "huscarls/debout/huscarls_debout_normaux_close.png"
image huscarls debout_rire_close = "huscarls/debout/huscarls_debout_rire_close.png"

#Combat
image huscarls combat_normaux = "huscarls/combat/huscarls_combat_normaux.png"
image huscarls combat_enthousiaste = "huscarls/combat/huscarls_combat_enthousiaste.png"
image huscarls combat_furieux = "huscarls/combat/huscarls_combat_furieux.png"
image huscarls combat_inquiets = "huscarls/combat/huscarls_combat_inquiets.png"

#mid
image huscarls combat_normaux_mid = "huscarls/combat/huscarls_combat_normaux_mid.png"
image huscarls combat_enthousiaste_mid = "huscarls/combat/huscarls_combat_enthousiaste_mid.png"
image huscarls combat_furieux_mid = "huscarls/combat/huscarls_combat_furieux_mid.png"
image huscarls combat_inquiets_mid = "huscarls/combat/huscarls_combat_inquiets_mid.png"

#close
image huscarls combat_normaux_close = "huscarls/combat/huscarls_combat_normaux_close.png"
image huscarls combat_enthousiaste_close = "huscarls/combat/huscarls_combat_enthousiaste_close.png"
image huscarls combat_furieux_close = "huscarls/combat/huscarls_combat_furieux_close.png"
image huscarls combat_inquiets_close = "huscarls/combat/huscarls_combat_inquiets_close.png"

##Garde / Guerriers Vikings / Jeune Guerrier Viking
define gv = Character('Guerriers Vikings', color="#e67e22")
define gc = Character("Garde du Château")
define jgv = Character("Jeune Guerrier Viking")

#Debout
image gv debout_normaux = "guerriers_vikings/debout/gv_debout_normaux.png"
image gv debout_enthousiastes = "guerriers_vikings/debout/gv_debout_enthousiastes.png"
image gv debout_furieux = "guerriers_vikings/debout/gv_debout_furieux.png"
image gv debout_rire = "guerriers_vikings/debout/gv_debout_rire.png"
image gv debout_contraries = "guerriers_vikings/debout/gv_debout_contraries.png"
image gv debout_determines = "guerriers_vikings/debout/gv_debout_determines.png"

image gv debout_normaux_mid = "guerriers_vikings/debout/gv_debout_normaux_mid.png"
image gv debout_enthousiastes_mid = "guerriers_vikings/debout/gv_debout_enthousiastes_mid.png"
image gv debout_furieux_mid = "guerriers_vikings/debout/gv_debout_furieux_mid.png"
image gv debout_rire_mid = "guerriers_vikings/debout/gv_debout_rire_mid.png"
image gv debout_contraries_mid = "guerriers_vikings/debout/gv_debout_contraries_mid.png"
image gv debout_determines_mid = "guerriers_vikings/debout/gv_debout_determines_mid.png"

image gv debout_normaux_close = "guerriers_vikings/debout/gv_debout_normaux_close.png"
image gv debout_enthousiastes_close = "guerriers_vikings/debout/gv_debout_enthousiastes_close.png"
image gv debout_furieux_close = "guerriers_vikings/debout/gv_debout_furieux_close.png"
image gv debout_rire_close = "guerriers_vikings/debout/gv_debout_rire_close.png"
image gv debout_contraries_close = "guerriers_vikings/debout/gv_debout_contraries_close.png"
image gv debout_determines_close = "guerriers_vikings/debout/gv_debout_determines_close.png"

#Combat
image gv combat_normaux = "guerriers_vikings/combat/gv_combat_normaux.png"
image gv combat_blesses = "guerriers_vikings/combat/gv_combat_blesses.png"

#mid
image gv combat_normaux_mid = "guerriers_vikings/combat/gv_combat_normaux_mid.png"
image gv combat_blesses_mid = "guerriers_vikings/combat/gv_combat_blesses_mid.png"

#close
image gv combat_normaux_close = "guerriers_vikings/combat/gv_combat_normaux_close.png"
image gv combat_blesses_close = "guerriers_vikings/combat/gv_combat_blesses_close.png"

#Jeune Guerrier Viking
image jgv debout_normal = "jeune_viking/debout/jgv_debout_normal.png"
image jgv debout_pleurant = "jeune_viking/debout/jgv_debout_pleurant.png"

image jgv debout_normal_mid = "jeune_viking/debout/jgv_debout_normal_mid.png"
image jgv debout_pleurant_mid = "jeune_viking/debout/jgv_debout_pleurant_mid.png"

image jgv debout_normal_close = "jeune_viking/debout/jgv_debout_normal_close.png"
image jgv debout_pleurant_close = "jeune_viking/debout/jgv_debout_pleurant_close.png"

##Ogma
define o = Character('Ogma', color="#d35400")

#Debout
image ogma debout_normal = "ogma/debout/ogma_debout_normal.png"
image ogma debout_souriant = "ogma/debout/ogma_debout_souriant.png"
image ogma debout_furieux = "ogma/debout/ogma_debout_furieux.png"
image ogma debout_attriste = "ogma/debout/ogma_debout_attriste.png"
image ogma debout_contrarie = "ogma/debout/ogma_debout_contrarie.png"
image ogma debout_determine = "ogma/debout/ogma_debout_determine.png"

image ogma debout_normal_mid = "ogma/debout/ogma_debout_normal_mid.png"
image ogma debout_souriant_mid = "ogma/debout/ogma_debout_souriant_mid.png"
image ogma debout_furieux_mid = "ogma/debout/ogma_debout_furieux_mid.png"
image ogma debout_attriste_mid = "ogma/debout/ogma_debout_attriste_mid.png"
image ogma debout_contrarie_mid = "ogma/debout/ogma_debout_contrarie_mid.png"
image ogma debout_determine_mid = "ogma/debout/ogma_debout_determine_mid.png"

image ogma debout_normal_close = "ogma/debout/ogma_debout_normal_close.png"
image ogma debout_souriant_close = "ogma/debout/ogma_debout_souriant_close.png"
image ogma debout_furieux_close = "ogma/debout/ogma_debout_furieux_close.png"
image ogma debout_attriste_close = "ogma/debout/ogma_debout_attriste_close.png"
image ogma debout_contrarie_close = "ogma/debout/ogma_debout_contrarie_close.png"
image ogma debout_determine_close = "ogma/debout/ogma_debout_determine_close.png"

#Combat
image ogma combat_normal = "ogma/combat/ogma_combat_normal.png"
image ogma combat_furieux = "ogma/combat/ogma_combat_furieux.png"
image ogma combat_contrarie = "ogma/combat/ogma_combat_contrarie.png"
image ogma combat_determine = "ogma/combat/ogma_combat_determine.png"

#mid
image ogma combat_normal_mid = "ogma/combat/ogma_combat_normal_mid.png"
image ogma combat_furieux_mid = "ogma/combat/ogma_combat_furieux_mid.png"
image ogma combat_contrarie_mid = "ogma/combat/ogma_combat_contrarie_mid.png"
image ogma combat_determine_mid = "ogma/combat/ogma_combat_determine_mid.png"

#close
image ogma combat_normal_close = "ogma/combat/ogma_combat_normal_close.png"
image ogma combat_furieux_close = "ogma/combat/ogma_combat_furieux_close.png"
image ogma combat_contrarie_close = "ogma/combat/ogma_combat_contrarie_close.png"
image ogma combat_determine_close = "ogma/combat/ogma_combat_determine_close.png"

#Combat Hache
image ogma combat_hache_brandir = "ogma/combat_hache/ogma_combat_hache_brandir.png"
image ogma combat_hache_determine = "ogma/combat_hache/ogma_combat_hache_determine.png"

#mid
image ogma combat_hache_brandir_mid = "ogma/combat_hache/ogma_combat_hache_brandir_mid.png"
image ogma combat_hache_determine_mid = "ogma/combat_hache/ogma_combat_hache_determine_mid.png"

#close
image ogma combat_hache_brandir_close = "ogma/combat_hache/ogma_combat_hache_brandir_close.png"
image ogma combat_hache_determine_close = "ogma/combat_hache/ogma_combat_hache_determine_close.png"

##Moira
define m = Character("Moira", color = "#f00")

#Debout
image moira debout_normal = "moira/debout/moira_debout_normal.png"
image moira debout_souriant = "moira/debout/moira_debout_souriant.png"
image moira debout_furieux = "moira/debout/moira_debout_furieux.png"
image moira debout_attriste = "moira/debout/moira_debout_attriste.png"
image moira debout_contrarie = "moira/debout/moira_debout_contrarie.png"
image moira debout_effraye = "moira/debout/moira_debout_effraye.png"
image moira debout_determine = "moira/debout/moira_debout_determine.png"

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

#nude
image moira nue_normal = "moira/nue/moira_nue_normale.png"
image moira nue_souriant = "moira/nue/moira_nue_souriante.png"
image moira nue_effraye = "moira/nue/moira_nue_effrayee.png"

image moira nue_normal_mid = "moira/nue/moira_nue_normale_mid.png"
image moira nue_souriant_mid = "moira/nue/moira_nue_souriant_mid.png"
image moira nue_effraye_mid = "moira/nue/moira_nue_effraye_mid.png"

image moira nue_normal_close = "moira/nue/moira_nue_normale_close.png"
image moira nue_souriant_close = "moira/nue/moira_nue_souriant_close.png"
image moira nue_effraye_close = "moira/nue/moira_nue_effraye_close.png"

#Attache
image moira attache_determine = "moira/buchet/moira_attache_determine.png"
image moira attache_furieuse = "moira/buchet/moira_attache_furieuse.png"

#mid
image moira attache_determine_mid = "moira/buchet/moira_attache_determine_mid.png"
image moira attache_furieuse_mid = "moira/buchet/moira_attache_furieuse_mid.png"

#close
image moira attache_determine_close = "moira/buchet/moira_attache_determine_close.png"
image moira attache_furieuse_close = "moira/buchet/moira_attache_furieuse_close.png"

##Rebelles ecossais
define ge = Character('rebelles écossais', color="#f39c12")

#Debout
image re debout_normaux = "rebelles_ecossais/debout/re_debout_normaux.png"
image re debout_enthousiastes = "rebelles_ecossais/debout/re_debout_enthousiastes.png"
image re debout_inquiets = "rebelles_ecossais/debout/re_debout_inquiets.png"
image re debout_rire = "rebelles_ecossais/debout/re_debout_rire.png"

image re debout_normaux_mid = "rebelles_ecossais/debout/re_debout_normaux_mid.png"
image re debout_enthousiastes_mid = "rebelles_ecossais/debout/re_debout_enthousiastes_mid.png"
image re debout_inquiets_mid = "rebelles_ecossais/debout/re_debout_inquiets_mid.png"
image re debout_rire_mid = "rebelles_ecossais/debout/re_debout_rire_mid.png"

image re debout_normaux_close = "rebelles_ecossais/debout/re_debout_normaux_close.png"
image re debout_enthousiastes_close = "rebelles_ecossais/debout/re_debout_enthousiastes_close.png"
image re debout_inquiets_close = "rebelles_ecossais/debout/re_debout_inquiets_close.png"
image re debout_rire_close = "rebelles_ecossais/debout/re_debout_rire_close.png"

#Combat
image re combat_normaux = "rebelles_ecossais/combat/re_combat_normaux.png"
image re combat_blesse = "rebelles_ecossais/combat/re_combat_blesses.png"
image re combat_furieux = "rebelles_ecossais/combat/re_combat_furieux.png"

#mid
image re combat_normaux_mid = "rebelles_ecossais/combat/re_combat_normaux_mid.png"
image re combat_blesse_mid = "rebelles_ecossais/combat/re_combat_blesses_mid.png"
image re combat_furieux_mid = "rebelles_ecossais/combat/re_combat_furieux_mid.png"

#close
image re combat_normaux_close = "rebelles_ecossais/combat/re_combat_normaux_close.png"
image re combat_blesse_close = "rebelles_ecossais/combat/re_combat_blesses_close.png"
image re combat_furieux_close = "rebelles_ecossais/combat/re_combat_furieux_close.png"


##Villageois / prisonniers
define ve = Character('Villageois', color="#3498db")

define pe1 = Character("Prisonnier écossais 1")
define pe2 = Character("Prisonnier écossais 2")
define pe3 = Character("Prisonnière écossaise 1")

#Debout
image ve debout_normaux = "villageois_ecossais/debout/ve_debout_normaux.png"
image ve debout_craintifs = "villageois_ecossais/debout/ve_debout_craintifs.png"
image ve debout_effrayes = "villageois_ecossais/debout/ve_debout_effrayes.png"

image ve debout_normaux_mid = "villageois_ecossais/debout/ve_debout_normaux_mid.png"
image ve debout_craintifs_mid = "villageois_ecossais/debout/ve_debout_craintifs_mid.png"
image ve debout_effrayes_mid = "villageois_ecossais/debout/ve_debout_effrayes_mid.png"

image ve debout_normaux_close = "villageois_ecossais/debout/ve_debout_normaux_close.png"
image ve debout_craintifs_close = "villageois_ecossais/debout/ve_debout_craintifs_close.png"
image ve debout_effrayes_close = "villageois_ecossais/debout/ve_debout_effrayes_close.png"

#Buchet
image ve buchet_normaux = "villageois_ecossais/buchet/ve_buchet_effrayes.png"
image ve buchet_pleurent = "villageois_ecossais/buchet/ve_buchet_pleurent.png"

image ve buchet_normaux_mid = "villageois_ecossais/buchet/ve_buchet_effrayes_mid.png"
image ve buchet_pleurent_mid = "villageois_ecossais/buchet/ve_buchet_pleurent_mid.png"

image ve buchet_normaux_close = "villageois_ecossais/buchet/ve_buchet_effrayes_close.png"
image ve buchet_pleurent_close = "villageois_ecossais/buchet/ve_buchet_pleurent_close.png"

##Patrick
define p = Character("Patrick")
image patrick debout_normal = "patrick/debout/patrick_debout_normal.png"
image patrick debout_furieux = "patrick/debout/patrick_debout_furieux.png"

image patrick debout_normal_mid = "patrick/debout/patrick_debout_normal_mid.png"
image patrick debout_furieux_mid = "patrick/debout/patrick_debout_furieux_mid.png"

image patrick debout_normal_close = "patrick/debout/patrick_debout_normal_close.png"
image patrick debout_furieux_close = "patrick/debout/patrick_debout_furieux_close.png"

#Guerriers Asiatiques
#image ga combat_agressifs = "ga_combat_agressifs.png"

#Scene

##Forest
#forest
image bg forest = "scenes/foretWestruther_ext_jour_foret.jpg"
image bg forest_night = "scenes/foretWestruther_ext_nuit_foret.jpg"
image bg forest_crepuscule = "scenes/foretWestruther_ext_aube_foret.jpg"
image bg little_heaven = "scenes/foretWestruther_ext_matin_paradis.png"
#sentier
image bg sentier_jour = "scenes/foretWestruther_ext_matin_sentier.jpg"

#Village
#exterior
image bg village = "scenes/perth_ext_jour_village.png"
image bg village2_crepuscule = "scenes/perth_ext_jour_village.png"
#ogma house
image bg house = "scenes/perth_int_jour_maison.png"
image bg house2_jour = "scenes/perth_int_jour_maison.png"
image bg house2_night = "scenes/perth_int_nuit_maison.png"
image bg house2_aube = "scenes/perth_int_jour_maison.png"

##Plaine cotière
image bg plaine_cotière_matin = "scenes/plaine_ext_matin_plaineCotiere.jpg"
image bg plaine_chateau_matin = "scenes/plaine_ext_matin_plaineChateau.jpg"

#plaine
image bg plaine_plaine_matin = "scenes/plaine_ext_matin_plaine.jpg"

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
image bg chateau_couloir_crepuscule = "scenes/chateauDunbar_int_crepuscule_couloir.jpg"
#chambre Harald
image bg chateau_chambre_nuit = "scenes/chateauDunbar_int_nuit_chambreHarald.png"
#Salle banquet
image bg chateau_banquet = "scenes/chateauDunbar_int_salleBanque.jpg"

#Fond uni
image bg black = "#000"

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

label start_s:

    scene bg black

    centered "En l'an 1038, Harald Sigurdsson de Norvège, garde varègue au service de l'impératrice de Constantinople, s'empare des Clous de la Sainte Croix à Jérusalem."

    centered "Les Clous donnent à Harald la force et l'immortalité. Le viking, convaincu d'être un élu divin, décide d'orner sa hache des Clous. Il créé ainsi une nouvelle relique : la Hache Sainte."

    centered "Revenu triomphalement en Norvège, il est couronné roi et entame de grandes campagnes militaires visant à christianiser le monde ainsi qu'à asseoir sa suprématie."

    centered "Armé de la Hache Sainte, Harald prend le contrôle de l'Europe, du Moyen-Orient et d'une partie de l'Asie et de l'Afrique. En 1080, Harald est devenu l'équivalent d'Alexandre le Grand : un roi-empereur, une légende vivante, un demi-dieu."

    centered "Nous sommes en 1082. Des paysans écossais ont tué Clyde Montgomery, l'intendant que Harald avait placé à la tête de l'Ecosse. Le roi-empereur a décidé de revenir mater cette petite rébellion et d’en faire un exemple."

    jump introS

label start_l:

    scene bg black

    centered "En l'an 1038, Harald Sigurdsson de Norvège, garde varègue au service de l'impératrice de Constantinople, s'empare des Clous de la Sainte Croix à Jérusalem."

    centered "Les Clous donnent à Harald la force et l'immortalité. Le viking, convaincu d'être un élu divin, décide d'orner sa hache des Clous. Il créé ainsi une nouvelle relique : la Hache Sainte."

    centered "Revenu triomphalement en Norvège, il est couronné roi et entame de grandes campagnes militaires visant à christianiser le monde ainsi qu'à asseoir sa suprématie."

    centered "Armé de la Hache Sainte, Harald prend le contrôle de l'Europe, du Moyen-Orient et d'une partie de l'Asie et de l'Afrique. En 1080, Harald est devenu l'équivalent d'Alexandre le Grand : un roi-empereur, une légende vivante, un demi-dieu."

    centered "Nous sommes en 1082. Des paysans écossais ont tué Clyde Montgomery, l'intendant que Harald avait placé à la tête de l'Ecosse. Le roi-empereur a décidé de revenir mater cette petite rébellion et d’en faire un exemple."

    jump intro
