from kivy.config import Config

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

from kivymd.app import MDApp
from kivy.lang import Builder

navigation_helper = """
MDScreenManager:
    id: master_manager

    MDScreen:
        name: "menu"
        MDBoxLayout:
            orientation: 'vertical'
            MDTopAppBar:
                title: "Dashboard Aprende"
            Widget:
            MDTopAppBar:
                title: "luisfrancistaekabel"

        MDFloatLayout:
            MDRaisedButton:
                text: "APRENDE HTML"
                pos_hint: {"center_x": .5, "center_y": .7 }
                on_release: master_manager.current = "aprendehtml"

        MDFloatLayout:
            MDRaisedButton:
                text: "APRENDE CSS"
                pos_hint: {"center_x": .5, "center_y": .6}
                on_release: master_manager.current = "aprendecss"

        MDFloatLayout:
            MDRaisedButton:
                text: "APRENDE JAVASCRIPT"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_release: master_manager.current = "aprendejavascript"

        MDFloatLayout:
            MDRaisedButton:
                text: "APRENDE PHP"
                pos_hint: {"center_x": .5, "center_y": .4}
                on_release: master_manager.current = "aprendephp"

        MDFloatLayout:
            MDRaisedButton:
                text: "APRENDE PYTHON"
                pos_hint: {"center_x": .5, "center_y": .3}
                on_release: master_manager.current = "aprendepython"

    # ==================== HTML SCREEN ====================
    MDScreen:
        name: "aprendehtml"
        MDNavigationLayout:
            MDScreenManager:
                id: html_screen_manager
                MDScreen:
                    name: "introdusaunhtml"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Introdusaun Html"
                            left_action_items: [['menu', lambda x: html_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"

                                   
                                MDLabel:
                                    text: "Istória no Introdusaun ba HTML"
                                    font_style: "H6"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "center"
                                    bold: True
                                
                                MDLabel:
                                    text: "Ita sei koalia uituan kona ba html  atu nune'e ita bele  konhese diak liu tan saida mak html, no oinsa mak uza html hodi bele hatene klaru liu tan."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                
                                MDLabel:
                                    text: "Html fasil atu uza no nia laos linguajem programasaun maibe linguajem markasaun ou babain iha english ema bolu markup languange"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                
                                MDLabel:
                                    text: "Html halo husi senhora ida naran Tim berners iha tinan 1991 no nia foto mak iha kraik nee."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "timbernes.jpg"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True
                             
                                
                                MDLabel:
                                    text: "html refere halo iha tinan 1991 no nia sei uza hela iha nia office rasik neebe lokazaliza iha Suica office refere hanaran CERN"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                
                                MDLabel:
                                    text: "No husi  ida ne'e ita bele hatene  katak ona html nia kria dahuluk agora ita ba fale sa tinan los mak html fo sai publiku"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                
                                MDLabel:
                                    text: "Iha tinan 1993, HTML foin fó sai ofisialmente ba públiku, maibe molok nia fo sai ba publiku iha tinan 1992 Tim Berners sei teste oinsa mak ema hotu iha mundu uza."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                
                                MDLabel:
                                    text: "Ho ida ne'e Tim Berners kraik https ( hypertext trasnfere protocol secured ) no http ( hypetertext transfer protocol) atu nunee ema hotu bele asseu laos deit local maibe iha mundu tomak"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                
                                MDLabel:
                                    text: "Iha momentu neba TIm berners fo sai katak html limitadu tebes ba iha nia feature sira ka nia ajuda sytax atu fo sai buat ruma ho ida ne'e mak developer seluk  komesa dezenvolve to era dadaun ne'e to Html nia versaun prezente agora mak Html 5"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "No atu hakerek html mak ita presiza editor aplikasaun ida ne'ebe mak hanesan visual studio code ita boot sira bele ba dowload rasik iha ita boot sira nia laptop ou pc"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Depois de  dowload bele ba halo folder depois mak ba iha visual studio code buti iha file no open folder pois buka iha ita nia folder nebe mak ita kriak konforme ita nia folder nebe halo ne naran saida"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Hotu ida maka ita bele hare iha baze html depois hakerek  coding hotu keta haluha mos halo file dahuluk nebe  tau lisaun dahuluk ho  nia pontu depois hakerek nia file.html"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                     
                MDScreen:
                    name: "bazehtml"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Baze Html"
                            left_action_items: [['menu', lambda x: html_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Baze Html atu hatene oinsa hakerek html "
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                
                                MDLabel:
                                    text: "Tuir mai hau sei koalia uluk html uza tag, no tag ne kompustu husi aspas meik rua no no loke ho aspas meik ho nia code iha laran iha aspas meik nia laran mak kode html nia no bainhira taka aspas ne iha tan sorin liu ba ita sei hare iha imagen kraik ne"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "bazehtml.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True
                                
                                MDLabel:
                                    text: "ita hanesa html loke iha aspas meik no nia tag taka mos iha mak aspas meik tau tan ho bara kleuk ne mak taka tag atu hatete katak ne'e mak nia ikus no rohan"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "agora ita boot sira bele hare nia rezultadu ona liu husi ita boot ba file nebe ita kria ona hanesan iha introdusuan no klik ba bele hili  browser saida saida  deit n o nia sei fo sai rezultadu hanesan neba"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                Image:
                                    source: "rezultadubazehtml.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True
                MDScreen:
                    name: "headinghtml"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Heading Html"
                            left_action_items: [['menu', lambda x: html_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Heading Html - H1 to H6"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                
                                MDLabel:
                                    text: "Heading utiliza ba hakerek titulu no subtopiku sira heading to heading da neen pois mak ita boot hare nia rezultadu mak ita komprende, no heading importante tebes iha website ida nia laran"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                MDLabel:
                                    text: "Heading babain ema uza ba iha footern no header nebe ita sei aprende iha materia  ikus liu"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                MDLabel:
                                    text: "No ita boot sira keta haluha katak code html nian sempre hakerek iha body laran  ka nia code html sira"
                                    size_hint_y: None
                                    height: self.texture_size[1]

                                Image:
                                    source: "heading.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                                
                                MDLabel:
                                    text: "run no sei sai hanesan rezultadu iha kraik nee keta haluha run ou loke  ne hau fo sai tiha ona iha materia anterior"
                                    size_hint_y: None
                                    height: self.texture_size[1]

                                Image:
                                    source: "rezultaduheading.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "paragrafuhtml"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Paragrafu Html"
                            left_action_items: [['menu', lambda x: html_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Paragrafu Html uza tag <p>"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                
                                MDLabel:
                                    text: "paragrafu hodi hakerek testu ruma hanesan babain ema hotu hotu hatene kona ba paragrafu"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                
                                MDLabel:
                                    text: "Tuir mai ita boot sira bele hare paragrafu nia code iha imagem kraik"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "paragrafu.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True
                                
                                MDLabel:
                                    text: "No bainhira run ona mak ita boot sira sei hetan rezultadu hanesan imagen kraik refere"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "rezultaduparagrafu.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "formatuhtml"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Formatu Html"
                            left_action_items: [['menu', lambda x: html_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Formatu Html: bold, italic, underline"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                
                                MDLabel:
                                    text: "Ida ne'e modelu letra sira nebe html halo balun sai hanesan iha word sira tuir mai ita hare nia code iha kraik"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "formatu.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True
                                
                                MDLabel:
                                    text: "No nia rezultadu mak hanesan imagen iha kraik ne'e"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "rezultaduformatuhtml.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True
                MDScreen:
                    name: "linkhtml"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Link Html"
                            left_action_items: [['menu', lambda x: html_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Link Html uza tag <a href>"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                
                                MDLabel:
                                    text: "Link ida nee ita halo koneksaun fale ba iha website seluk "
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                
                                MDLabel:
                                    text: "No bele hare nia code iha kraik keta haluha nafatin kria  file  no hakerek  code iha iha body nian hanesan hau fo sai tiha ona iha  code anterior"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "linkhtml.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True
                                
                                MDLabel:
                                    text: "Bele run ona no nia klik letra refere ba iha google "
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                MDScreen:
                    name: "imagehtml"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Imagen Html"
                            left_action_items: [['menu', lambda x: html_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Imagen Html uza tag <img>"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                
                                MDLabel:
                                    text: "Tag <img> uza hodi hatudu imagen iha pájina web, uza atributu 'src' hodi foti file imagen."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "No mos image refere keta haluha tau hamutuk iha folder ida nebe ita boot  niaf code html  file rai ba ne"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                Image:
                                    source: "atributu.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "listahtml"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Lista Html"
                            left_action_items: [['menu', lambda x: html_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Lista Html: ul, ol, li"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                
                                MDLabel:
                                    text: "Iha HTML iha lista oin rua: Ordered List <ol> no Unordered List <ul>."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "lista.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True
                                
                                MDLabel:
                                    text: "Rezultadu husi kodigu iha leten mak hanesan tuir mai ne'e:"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "rezultadulistahtml.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "komentariuhtml"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Komentariu Html"
                            left_action_items: [['menu', lambda x: html_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Komentariu Html: <!-- comment -->"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                
                                MDLabel:
                                    text: "Komentariu uza hodi tau nota iha kodigu laran ne'ebé sei la mosu iha browser."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "komentariu.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True
                                
                                MDLabel:
                                    text: "Rezultadu (komentariu sei la mosu):"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                               
                MDScreen:
                    name: "bazeatributhtml"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Baze Atributu Html"
                            left_action_items: [['menu', lambda x: html_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Atributu Html: id, class, style"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                
                                MDLabel:
                                    text: "Atributu fó informasaun adisional ba elementu HTML nian. nebe mak molok hakerek toolpi nain hanesan mos iha video nian nebe source no src mak atributu hodi aumenta deit funsaun iha tag nia laran"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "atributu.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True
                MDScreen:
                    name: "form"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Form Html"
                            left_action_items: [['menu', lambda x: html_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'                 
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Form Html uza tag <form>"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Ihane'e kona ba oinsa mak atu halo formulariu website nian ita bele hakerek  code iha kraik nee no koko hare nia rezultadu rasik"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                Image:
                                    source: "form.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True
                MDScreen:
                    name: "tipuinputhtml"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Tipu Input Html"
                            left_action_items: [['menu', lambda x: html_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Tipu Input: text, email, password, number"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "iha ne'e hanesan ho form nebe liu tiha ona maibe atu esplika uituan deit katak tipu input hrmln nia mak kotak mamuk sira nee ho nia kategoria oinoin"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                Image:
                                    source: "form.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "textareahtml"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Textarea Html"
                            left_action_items: [['menu', lambda x: html_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"

                                MDLabel:
                                    text: "Textarea uza tag <textarea>"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Textarea  atu hakerek iha laran ou babaine  ema ba halo komentariu nia laran"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                Image:
                                    source: "form.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "butaunhtml"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Butaun Html"
                            left_action_items: [['menu', lambda x: html_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Butaun uza tag <button>"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Butaun nia mak atu halo butaun sira ita boot sira bele troka link iha laran maibe tan aplikasaun ne fo sai ba ema sira beginner ou foin aprende depoi mak ita sei aumenta tan materia bainhira tempu iha, no butaun code mak iha kraik   button type refere"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                Image:
                                    source: "form.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "multimediahtml"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Multimedia Html"
                            left_action_items: [['menu', lambda x: html_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Multimedia: video, audio, embed"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Multimedia atu fo sai video keta haluha bainhira atu tau video  nian naran iha source src nina video tenki hatama hamutuk ba folder ida nia laran ka fila nia laran"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                Image:
                                    source: "multimedia.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "semantichtml"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Semantic Html"
                            left_action_items: [['menu', lambda x: html_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Semantic: header, nav, main, footer"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                
                                MDLabel:
                                    text: "Semantic HTML mak prátika ida hodi uza tag HTML ne'ebé fó informasaun loloos kona-ba konteúdu iha laran, nune'e browser no masin buka-fatin hanesan Google bele komprende estrutura website nian ho di'ak liu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Antes ne'e ema uza de'it 'div' ba buat hotu, maibé ho HTML5, ita iha tag hanesan <header> hodi define parte leten husi website ne'ebé baibain rai logo no menu navigasaun nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Tag <nav> kria espesiál hodi rai ligasaun ka 'links' navigasaun nian, ne'ebé ajuda tebes 'screen readers' hodi fó hatene ba ema ne'ebé labele hare katak parte ida ne'e mak menu ba website nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ba konteúdu prinsipál, ita uza tag <main>, ne'ebé hatudu ba sistema sira katak informasaun ne'ebé importante liu iha pájina ida laran tur iha ne'ebá, la'ós iha 'sidebar' ka 'footer'."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Tag <article> uza hodi kobre konteúdu ida ne'ebé bele moris mesak, hanesan kapa livru ida, notísia ida, ka 'post' husi blog, nune'e fasilitu tebes atu fahe ka 'distribute' ba fatin seluk."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Enkuantu <section> uza hodi separa tópiku sira ne'ebé la hanesan iha pájina ida laran, hanesan parte 'Kona-ba Ami', 'Servisu', no 'Kontaktu' hodi kria organizasaun ne'ebé moos."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Tag <aside> útil tebes hodi rai informasaun sekundáriu ne'ebé iha relasaun uitoan de'it ho konteúdu prinsipál, baibain ema uza ba 'sidebar', publisidade, ka ligasaun ba artigu sira seluk."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Iha parte kraik liu, ita iha <footer> ne'ebé rai informasaun hanesan 'copyright', ligasaun ba média sosiál, no informasaun legál sira seluk ne'ebé presiza mosu iha rohan."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Uza Semantic HTML halo ita-nia kódigu sai fásil liu ba dezenvolvedór seluk hodi lee no edita, tanba sira bele hatene kedas funsaun husi parte ida-idak lahó presiza buka-tuir 'class' ka 'id'."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Mestre ba Semantic HTML mak xave hodi kria website ne'ebé profesonál no iha SEO ne'ebé aas, tanba Google gosta tebes website ne'ebé estrutura ninia informasaun ho lójika no sentidu ne'ebé klaru."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "semantichtml.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

            MDNavigationDrawer:
                id: html_nav_drawer
                radius: (0, 16, 16, 0)
                MDNavigationDrawerMenu:
                    MDNavigationDrawerHeader:
                        title: "Luis App"
                        text: "Projetu Indpendente"
                        spacing: "4dp"
                        padding: "16dp", 0, 0, "16dp"

                    MDNavigationDrawerItem:
                        text: "Introdusaun Html"
                        on_release:
                            html_screen_manager.current = "introdusaunhtml"
                            html_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Baze Html"
                        on_release:
                            html_screen_manager.current = "bazehtml"
                            html_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Heading Html"
                        on_release:
                            html_screen_manager.current = "headinghtml"
                            html_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Paragrfu Html"
                        on_release:
                            html_screen_manager.current = "paragrafuhtml"
                            html_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Formatu Html"
                        on_release:
                            html_screen_manager.current = "formatuhtml"
                            html_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Link Html"
                        on_release:
                            html_screen_manager.current = "linkhtml"
                            html_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Imagen Html"
                        on_release:
                            html_screen_manager.current = "imagehtml"
                            html_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Lista Html"
                        on_release:
                            html_screen_manager.current = "listahtml"
                            html_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Komentariu Html"
                        on_release:
                            html_screen_manager.current = "komentariuhtml"
                            html_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Baze Atributu Html"
                        on_release:
                            html_screen_manager.current = "bazeatributhtml"
                            html_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Form Html"
                        on_release:
                            html_screen_manager.current = "form"
                            html_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Tipu Input Html"
                        on_release:
                            html_screen_manager.current = "tipuinputhtml"
                            html_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Textarea Html"
                        on_release:
                            html_screen_manager.current = "textareahtml"
                            html_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Butaun Html"
                        on_release:
                            html_screen_manager.current = "butaunhtml"
                            html_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Multimedia Html"
                        on_release:
                            html_screen_manager.current = "multimediahtml"
                            html_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Semantic Html"
                        on_release:
                            html_screen_manager.current = "semantichtml"
                            html_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        icon: "logout"
                        text: "Sai"
                        on_release:
                            master_manager.current = "menu"
                            html_nav_drawer.set_state("close")

    # ==================== CSS SCREEN ====================
    MDScreen:
        name: "aprendecss"
        MDNavigationLayout:
            MDScreenManager:
                id: css_screen_manager
                MDScreen:
                    name: "introdusauncss"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Introdusaun CSS"
                            left_action_items: [['menu', lambda x: css_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "CSS katak Cascading Style Sheets no nia mak linguajen padraun ne'ebé uza hodi kria dezañu vizuál ba website hotu-hotu iha mundu tomak hodi nune'e bele kria kór no mós layout ne'ebé furak."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Håkon Wium Lie mak ema primeiru ne'ebé propoza kbiit CSS nian iha tinan 1994 hodi rezolve problema boot iha tempu ne'ebá ne'ebé HTML de'it la bele ona kontrola dezañu ho fasil no simples."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Antes CSS mosu programadór sira tenke hakerek kódigu barak tebes iha HTML laran de'it hodi muda kór letra nian maibé ho CSS ita bele kontrola pájina barak dala ida de'it husi arkivu ida."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Bert Bos mós iha parte importante tebes hodi dezenvolve padraun CSS nian hamutuk ho Håkon hodi nune'e sira na'in rua bele kria sistema ne'ebé lójiku tebes ba dezenvolvimentu web modernu nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "CSS 1 sai rekomendasaun ofisiál husi organizasaun W3C iha Dezembru 1996 no foka liu ba propriedade báziku sira hanesan font-family no kór no mós distánsia uitoan entre elementu sira nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Iha tinan 1998 CSS 2 mosu hodi lori mudansa boot tebes tanba nia suporta ona pozisaun elementu nian hanesan absolute no relative ne'ebé ajuda tebes programadór sira atu kria layout kompleksu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "CSS 3 ne'ebé foin mosu iha tinan 1999 hodi fahe ba módulu oioin mak lori funsaun foun hanesan border-radius hodi halo kantu kaba'as no shadow hodi halo dezañu sira ne'e sai hanesan iha kbiit 3D."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Benefísiu boot husi uza CSS mak nia bele kria website ne'ebé responsivu katak website ida de'it bele nakloke ho kapa'as tebes maske uza telemóvel ne'ebé ki'ik ka komputadór ne'ebé boot tebes."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ohin loron CSS la'ós de'it kona-ba kór no fonte maibé mós kona-ba animasaun ne'ebé kapa'as no tranzisaun ne'ebé halo esperiénsia uza website nian sai interativu liu ba vizitante sira ne'ebé mai."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Aprende CSS mak pasu importante segundu ba ema hotu-hotu ne'ebé hakarak sai dezenvolvedór web profisionál tanba la iha website ida iha mundu ne'e ne'ebé bele moris ho dezañu di'ak lahó kbiit CSS."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                    
                                Image:
                                    source: "cssintrodusan.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "komprensauncss"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Komprensaun CSS"
                            left_action_items: [['menu', lambda x: css_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Komprensaun baze kona-ba CSS."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "CSS mak lian dezañu ida ne'ebé ita uza hodi fó kór, forma, no layout ba elementu HTML hotu-hotu nune'e website la'ós de'it hatudu testu mutin no metan maibé sai furak hodi dada uza-na'in sira-nia matan hodi sente kmanek bainhira asesu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Konceitu 'Cascading' iha CSS katak regra sira ne'ebé ita hakerek iha leten bele tun ba elementu sira iha kraik, maibé ita mós bele troka fali regra sira-ne'e bazeia ba 'specificity' ka prioridade hodi kontrola dezañu ho detalladu tebes."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Iha CSS ita uza 'Selector' hodi hili elementu HTML ida ne'ebé mak ita hakarak kria dezañu, depois ita tau 'Property' hanesan 'color' ka 'font-size' no fó 'Value' ba sira nune'e ita bele kria estilu ne'ebé úniku ba kada parte husi website."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "CSS permite ita hodi separa kódigu konteúdu husi kódigu dezañu, ne'ebé katak ita bele troka vizuál husi website ida tomak ho lalais tebes de'it liuhusi troka file CSS ida, lahó presiza mexe fali iha kódigu HTML ne'ebé barak."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Aprende CSS ho didi'ak mak xave hodi kria website ne'ebé 'Responsive', katak dezañu ne'e bele muda an mesak hodi sai kapa'as nafatin maske uza-na'in loke husi telemóvel, tablet, ka komputadór ne'ebé iha ekrán boot."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                MDScreen:
                    name: "syntaxcss"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Syntax CSS"
                            left_action_items: [['menu', lambda x: css_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "CSS Syntax: selector { property: value; }"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Syntax CSS nian mak regra ida ne'ebé ita tenke tuir hodi fó hatene ba browser oinsá atu fó kór ka dezañu ba elementu HTML ida ne'ebé ita hili ona."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Estrutura báziku husi syntax CSS nian mak Selector hamutuk ho Declaration Block ne'ebé kompostu husi Property no mós Value ne'ebé ita hakarak uza."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Selector mak parte ne'ebé ita uza hodi hili elementu HTML saida mak ita hakarak fó dezañu hanesan h1 ka p ka bele mós uza class no id ba elementu sira."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Declaration Block mak parte ne'ebé ita rai iha bracket laran ne'ebé komesa ho de'it sinal bracket nakloke no taka hodi kobre regra hotu ne'ebé ita tau."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Property mak kbiit ka atributu ne'ebé ita hakarak muda husi elementu HTML nian hanesan color hodi muda kór ka font-size hodi muda letra nia boot."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Value mak valór ne'ebé ita fó ba property ida ne'ebé ita hili ona hanesan kór mean ka númeru pixel balu hodi nune'e browser bele hatene lójika dezañu nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ita tenke uza de'it sinal colon hodi separa property ho value no mós uza sinal semicolon iha parte ikus hodi taka regra ida nune'e bele hatama tan regra seluk."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ezemplu simples husi syntax CSS mak hanesan h1 ne'ebé ita fó kór azul ho kódigu h1 { color: blue; } ne'ebé h1 mak selector no color mak nia property nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ho uza syntax ne'ebé loos ita bele kria dezañu barak tebes ba website ida hodi halo nia sai furak liu no fasil ba vizitante sira atu lee konteúdu sira ne'ebé iha."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Keta haluha katak CSS mós sensitivu tebes ba sinal sira ne'e nune'e se ita haluha de'it semicolon ida mós bele halo dezañu tomak iha website laran la mós."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "csssyntax.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "selectorcss"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Selector CSS"
                            left_action_items: [['menu', lambda x: css_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "CSS Selectors: element, class, id, universal"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Selector CSS mak instrumentu ne'ebé boot tebes nia kbiit tanba nia funsaun la'ós de'it atu hili elementu ida maibé atu kria relasaun vizuál ne'ebé organizadu entre kódigu HTML ne'ebé ita hakerek ho dezañu ne'ebé ita-nia user sira sei haree iha ekrán."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Descendant Selector mak kbiit ida ne'ebé permite ita hili elementu ida ne'ebé moris iha elementu seluk nia laran hanesan se ita hakarak fó kór ba de'it letra ne'ebé iha div laran maibé la fó impaktu ba letra sira ne'ebé iha div nia li'ur."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Child Selector ne'ebé uza sinal boot liu ka '>' mak kbiit ne'ebé espesífiku liu descendant selector tanba nia hili de'it elementu ne'ebé sai oan diretu husi nia inan nune'e dezañu ne'e la bele monu ba bei-oan sira seluk iha laran."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Adjacent Sibling Selector ne'ebé uza sinal 'plus' ka '+' serve hodi hili elementu ida ne'ebé tuir kedas elementu seluk iha nia sorin nune'e ita bele kria dezañu espesiál ba parágrafu primeiru ne'ebé mosu depois de títulu h1."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "General Sibling Selector ne'ebé uza sinal 'tilde' ka '~' ajuda ita hili elementu hotu-hotu ne'ebé iha nivel hanesan ho elementu ida ne'ebé ita hili maske sira la tuir malu kedas iha kódigu laran maibé sira sei iha inan-aman ne'ebé hanesan."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Pseudo-element Selector ne'ebé uza pontu rua dala rua hanesan '::before' ka '::after' mak kbiit ida ne'ebé kmanek tebes tanba nia permite ita hatama konteúdu vizuál foun ka dezañu ba elementu ida nia oin ka nia kotuk lahó presiza mexe kódigu HTML."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Selector :nth-child() mak kbiit matemátika ida ne'ebé permite ita hili elementu sira bazeia ba sira-nia númeru ka orden hanesan hili de'it liña ne'ebé ho númeru pár ka númeru impar de'it iha tabela ida nia laran hodi kria kór ne'ebé seluk-seluk."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Kbiit husi Specificity iha CSS determina katak selector ida ne'ebé mak 'todan' liu nune'e se ita iha kódigu rua ne'ebé kontradis de'it mós browser sei hili ida ne'ebé iha pontu aas liu hanesan ID ne'ebé sempre manán class no element selector."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Aprende hodi uza Selector ne'ebé efisiente mós bele ajuda website nia performansa tanba browser sei la gasta tempu barak hodi buka-tuir elementu ida-idak se ita hakerek ita-nia selector sira ne'ebé simples no la naruk liu to'o susar atu lee."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ikus liu mak prátika mak xave importante tanba uza selector oioin iha projetu reál hanesan ita-nia aplikasaun 'Dashboard Aprende' ne'e sei halo ita-nia matenek ba CSS aumenta ba beibeik to'o ita sai mestre ne'ebé bele kria buat kmanek oioin."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                MDScreen:
                    name: "korcss"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Kor CSS"
                            left_action_items: [['menu', lambda x: css_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "CSS Colors: name, hex, rgb, rgba"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Kór iha CSS mak elementu vizuál ne'ebé importante tebes tanba nia bele fó moris ba website ida no mós bele fó influénsia ba sentimentu vizitante sira nian bainhira sira haree ita-nia dezañu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ita bele fó kór uza de'it naran kór nian ne'ebé simples hanesan red ka blue ka tomato ne'ebé fasil ba ita atu hanoin maibé kbiit ne'e limitadu uitoan tanba naran kór nian iha de'it kór hamutuk atus ida resin."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Hexadecimal ka Hex Code mak kódigu ne'ebé uza sinal hashtag ho letra no númeru ne'ebé kobre kór millaun ba millaun hodi nune'e ita bele hili kór ne'ebé espesífiku tebes tuir ita-nia hakarak."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "RGB katak Red Green no Blue ne'ebé uza valór númeru husi zero to'o duzentus sinkuenta i sinku hodi kahur kór fundamentál sira ne'e to'o mosu fali kór foun ne'ebé ita presiza iha ita-nia dezañu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "RGBA mak evolusaun husi RGB ne'ebé aumenta tan kbiit 'Alpha' hodi nune'e ita bele kria kór ne'ebé transparentu uitoan ka transparentu tebes hodi haree buat ne'ebé iha kór ne'e nia kotuk."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "HSL katak Hue Saturation no Lightness ne'ebé fó dalan foun mai ita hodi hili kór bazeia ba nia 'angle' iha roda kór nian hamutuk ho nia kbiit kór nian no mós nia naroman ka nakukun."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Background-color mak propriedade ne'ebé ita uza hodi fó kór ba kotuk husi elementu ida nune'e ita bele separa seksaun ida ho seksaun seluk iha ita-nia website hodi halo nia haree ba organizadu liu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Propriedade 'color' uza de'it hodi fó kór ba testu ka letra sira nune'e ita tenke kuidadu hodi hili kór ne'ebé la halo matan moras bainhira vizitante sira lee testu sira ne'ebé naruk tebes."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Uza kór ne'ebé iha kontraste di'ak mak xave importante ba asisibilidade nune'e ema hotu maske sira-nia matan la haree di'ak mós bele lee nafatin informasaun ne'ebé ita tau iha website laran."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ita mós bele uza Gradient hodi kahur kór rua ka liu dala ida de'it hodi mosu kór ne'ebé suli husi parte ida ba parte seluk ne'ebé halo dezañu website modernu nian sai kapa'as liu no profesonál."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ikus liu mak aprende oinsá uza kór ne'ebé loos iha CSS sei ajuda tebes ita hodi kria 'brand identity' ne'ebé forte ba ita-nia projetu sira hanesan aplikasaun Pi ne'e ne'ebé uza kór mean kapa'as iha leten."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "csskor.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "backgroundcss"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Background CSS"
                            left_action_items: [['menu', lambda x: css_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "CSS Background: color, image, repeat, position"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Uza background-image la'ós de'it kona-ba hatama imajen simples ida maibé ita bele mós kahur imajen oioin dala ida de'it uza kbiit multiple backgrounds nune'e ita bele tau mós dezañu 'overlay' ho kór transparante iha imajen nia leten hodi halo testu sira ne'ebé iha leten sai naroman liu no fasil ba ema hotu hodi lee konteúdu sira ne'ebé importante iha website laran."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Background-position mak ferramenta ida ne'ebé poderozu tebes tanba permite dezenvolvedór sira atu foka ba parte imajen nian ne'ebé kapa'as liu hanesan 'center' ka 'top right' hodi nune'e maske ekrán telemóvel nian ki'ik mós parte importante husi imajen ne'e la bele lakon ka tesi tiha nune'e esperiénsia uza-na'in nian nafatin mantein kualidade ne'ebé aas tebes."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "cssbg.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "textstylingcss"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Text Styling CSS"
                            left_action_items: [['menu', lambda x: css_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "CSS Text: font-size, font-family, color, text-align"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Propriedade text-shadow mak dalan ida ne'ebé kmanek tebes hodi kria dimensaun ba letra sira nune'e sira haree ba hanesan 'pop out' ka mosu sai husi ekrán laran ne'ebé ajuda tebes vizitante sira hodi foka sira-nia matan ba títulu importante sira no mós bele uza hodi kria efetu 'glow' ne'ebé modernu tebes ba dezañu website ne'ebé uza kór nakukun ka dark mode."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Letter-spacing no word-spacing mak detalhe ki'ik sira ne'ebé dala barak ema haluha maibé nia kbiit boot tebes hodi muda 'feel' husi dezañu ida tanba aumenta espasu uitoan entre letra sira bele halo website ne'e haree ba luxu liu no elegante liu enkuantu letra sira ne'ebé namtikit malu liu bele halo ema sente laran-todan bainhira foin foti telemóvel hodi loke pájina ne'e."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "csstextstyling.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "boxmodelcss"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Box Model CSS"
                            left_action_items: [['menu', lambda x: css_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "CSS Box Model: margin, border, padding, content"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Iha konseitu Box Model ita tenke komprende didi'ak oinsá padding servisu hamutuk ho background-color tanba kór ne'ebé ita fó ba elementu ida sei kobre mós área padding nian maibé la kobre área margin nian nune'e se ita sala uza propriedade rua ne'e ita-nia dezañu sei haree ba runguranga no la tuir regra vizuál ne'ebé loos iha dezenvolvimentu front-end modernu nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Outline mós importante maibé nia la hanesan ho border tanba outline la foti fatin iha box model nian laran nune'e nia la muda pozisaun elementu sira seluk ne'ebé iha nia sorin ne'ebé di'ak tebes hodi uza hanesan sinal vizuál bainhira ema ida hili elementu ruma uza de'it 'keyboard' hodi nune'e website ne'e sai asisivel liu ba ema ho kbiit limitadu sira."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "cssboxmodel.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "borderstylecss"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Border Style CSS"
                            left_action_items: [['menu', lambda x: css_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "CSS Border: style, width, color, radius"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "CSS Border mak hanesan ninin ka 'frame' ne'ebé ita tau hale'u elementu HTML ida hodi separa nia husi elementu sira seluk, ne'ebé ajuda tebes hodi kria estrutura vizuál ne'ebé klaru."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ita bele determina 'border-style' oioin hanesan 'solid' ba liña loos, 'dashed' ba liña kiska-riska, ka 'dotted' ba pontu-pontu hodi fó karakterístika úniku ba ita-nia dezañu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Propriedade 'border-width' kontrola naruk ka mahar husi liña border nian, enkuantu 'border-color' permite ita hodi fó kór ne'ebé mós bele uza kódigu HEX ka RGBA ba dezañu ne'ebé modernu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Atu kria dezañu ne'ebé 'smooth' ka mamar, ita uza 'border-radius' hodi halo ninin sira-ne'e sai kabuar, ne'ebé baibain ema uza hodi kria butaun ka imajen ne'ebé sirkulár."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ita mós bele kria border ba ninin ida de'it, hanesan 'border-bottom' de'it hodi kria liña iha testu okos, ne'ebé halo dezañu website nian sai elegante liu lahó presiza uza kór barak liu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "cssborderstyle.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "displaycss"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Display Property CSS"
                            left_action_items: [['menu', lambda x: css_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "CSS Display: block, inline, inline-block, none"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Uza display: grid mak mudansa boot liu iha istória CSS nian tanba nia permite ita kria layout ne'ebé iha koluna no linha ne'ebé kompleksu tebes lahó presiza kódigu barak nune'e ita bele kontrola espasu tomak iha ekrán laran ho lójika ne'ebé simples tebes ne'ebé uluk ema sira gasta tempu barak hodi kria uza de'it kbiit 'float' ne'ebé dala barak halo ulun-moras."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Position: sticky mak kbiit ne'ebé haree ba hanesan májika tanba nia sei hela de'it iha nia fatin normál to'o bainhira ita *scroll* liu nia mak nia sei 'tikit' fali iha ekrán nia leten ne'ebé kapa'as tebes hodi uza ba títulu seksaun ida-idak nune'e vizitante sira sempre hatene sira iha ne'ebé maske konteúdu iha pájina laran naruk tebes to'o ba okos."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "cssdisplay.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "pozisauncss"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Pozisaun CSS"
                            left_action_items: [['menu', lambda x: css_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "CSS Position: static, relative, absolute, fixed, sticky"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "CSS Position mak kbiit ida ne'ebé permite ita hodi determina loloos iha ne'ebé mak elementu HTML ida tenke mosu iha ekrán laran, nune'e ita bele kria layout ne'ebé kompleksu liu duke tuir de'it orden baibain."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Position 'static' mak valór padraun ba elementu hotu-hotu, iha ne'ebé sira sei tuir de'it 'flow' baibain husi dokumentu HTML nian no la simu influénsia husi propriedade hanesan top, bottom, left, ka right."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Position 'relative' permite ita hodi muda uitoan elementu ida nia fatin husi nia pozisaun originál lahó mexe elementu sira seluk ne'ebé hale'u nia, nune'e nia sai hanesan baze di'ak ida antes ita uza pozisaun absolute."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Position 'absolute' kmanek tebes tanba nia hasai elementu husi 'flow' baibain no tau nia bazeia ba parent ne'ebé iha pozisaun relative, nune'e ita bele tau elementu ida iha leten loos husi elementu seluk ho livre."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ho 'absolute', ita bele uza propriedade top ka left ho valór 'pixel' hodi determina ho loloos distánsia elementu nian husi ninin ekrán nian, ne'ebé ajuda tebes hodi kria dezañu ne'ebé presiza presizaun aas."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Position 'fixed' sei halo elementu ida 'metin' hela de'it iha ekrán laran maske ita 'scroll' pájina ne'e ba leten ka kraik, ne'ebé baibain ita uza hodi kria 'navigation bar' ka butaun 'chat' ne'ebé la bele lakon husi vizaun."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Position 'sticky' mak kombinasaun entre relative no fixed, iha ne'ebé elementu sei la'o tuir 'scroll' baibain to'o nia kona ninin ekrán nian, foin nia sei 'metin' iha ne'ebá hodi la bele sai husi uza-na'in sira-nia matan."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Importante tebes hodi kria 'Z-index' hamutuk ho pozisaun sira-ne'e tanba nia mak determina sé mak tenke iha oin no sé mak tenke iha kotuk bainhira elementu barak 'tumpuk' malu iha fatin ida de'it."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Uza pozisaun ne'ebé loos sei evita 'layout' ne'ebé runguranga, espesiálmente bainhira ita kria dezañu ne'ebé 'responsive' hodi nune'e elementu sira la bele 'soke' malu bainhira loke husi telemóvel ne'ebé ekrán ki'ik."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Mestre ba CSS Position mak pasu boot ida hodi sai dezenvolvedór 'Front-end' ne'ebé kapa'as, tanba kbiit hodi jere estrutura vizuál mak buat ne'ebé halo diferensa entre website baibain no website ne'ebé dezañu elegante."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                
                                Image:
                                    source: "pozisauncss.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "flexboxcss"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Flexbox CSS"
                            left_action_items: [['menu', lambda x: css_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "CSS Flexbox: display flex, justify-content, align-items"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "CSS Flexbox mak modelu layout ida ne'ebé permite elementu sira iha kontentór ida nia laran atu muda sira-nia luan no aas mesak de'it hodi nune'e bele foti espasu ne'ebé iha ho efisiente tebes hodi prevene ekrán mamuk ne'ebé haree ba la profesonál iha kualker dezenu website modernu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Uza justify-content: center hamutuk ho align-items: center mak dalan ne'ebé kmanek liu hodi tau buat hotu iha klaran loos husi ekrán laran lahó presiza kalkula númeru pixel sira ne'ebé halo ulun-moras tanba Flexbox sei rezolve problema ida ne'e mesak de'it hodi fó rezultadu ne'ebé simetriku."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Flex-wrap mak propriedade ida ne'ebé esensiál tebes bainhira ita kria dezañu responsivu tanba nia fó dalan ba elementu sira hodi monu ba liña foun bainhira ekrán telemóvel nian sai kikit liu hodi nune'e konteúdu sira la bele soke malu ka sai husi limitasaun vizuál ne'ebé ita determina ona."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "cssflexbox.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "gridlayoutcss"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Grid Layout CSS"
                            left_action_items: [['menu', lambda x: css_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "CSS Grid: display grid, grid-template-columns, grid-gap"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "CSS Grid Layout mak kbiit ne'ebé poderozu liu iha mundu front-end tanba nia permite dezenvolvedór sira atu kria sistema koluna no liña ne'ebé kompleksu tebes hodi kontrola dezañu husi parte rua dala ida de'it ne'ebé uluk susar tebes atu halo uza de'it kódigu CSS báziku ka uza de'it kbiit Flexbox nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Uza grid-template-columns ho kódigu 'repeat(auto-fit, minmax(200px, 1fr))' mak májika ida ne'ebé sei kria kapa dezañu ne'ebé muda an mesak tuir boot ekrán nian hodi nune'e ita-nia website sempre haree ba kmanek maske loke husi telemóvel ki'ik ka monitor komputadór ne'ebé boot tebes."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Grid-gap mak kbiit ne'ebé simples maibé kapa'as tebes hodi fó espasu ne'ebé hanesan entre elementu hotu-hotu iha grid laran lahó presiza uza margin ba elementu ida-idak nune'e ita-nia kódigu sai moos liu no fásil ba ema seluk hodi lee no komprende lójika dezañu ne'ebé ita kria ona iha projetu ne'e."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "cssgridlayout.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

            MDNavigationDrawer:
                id: css_nav_drawer
                radius: (0, 16, 16, 0)
                MDNavigationDrawerMenu:
                    MDNavigationDrawerHeader:
                        title: "Luis App"
                        text: "Projetu Indpendente"
                        spacing: "4dp"
                        padding: "16dp", 0, 0, "16dp"

                    MDNavigationDrawerItem:
                        text: "Introdusaun Css"
                        on_release:
                            css_screen_manager.current = "introdusauncss"
                            css_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Komprensaun Css"
                        on_release:
                            css_screen_manager.current = "komprensauncss"
                            css_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Syntax Css"
                        on_release:
                            css_screen_manager.current = "syntaxcss"
                            css_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Selector Css"
                        on_release:
                            css_screen_manager.current = "selectorcss"
                            css_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Kor Css"
                        on_release:
                            css_screen_manager.current = "korcss"
                            css_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Background Css"
                        on_release:
                            css_screen_manager.current = "backgroundcss"
                            css_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Text Styling Css"
                        on_release:
                            css_screen_manager.current = "textstylingcss"
                            css_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Box Model Css"
                        on_release:
                            css_screen_manager.current = "boxmodelcss"
                            css_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Border Style Css"
                        on_release:
                            css_screen_manager.current = "borderstylecss"
                            css_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Display Property Css"
                        on_release:
                            css_screen_manager.current = "displaycss"
                            css_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Pozisaun Css"
                        on_release:
                            css_screen_manager.current = "pozisauncss"
                            css_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Flex Box Css"
                        on_release:
                            css_screen_manager.current = "flexboxcss"
                            css_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "GridLayout"
                        on_release:
                            css_screen_manager.current = "gridlayoutcss"
                            css_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        icon: "logout"
                        text: "Sai"
                        on_release:
                            master_manager.current = "menu"
                            css_nav_drawer.set_state("close")

    # ==================== JAVASCRIPT SCREEN ====================
    MDScreen:
        name: "aprendejavascript"
        MDNavigationLayout:
            MDScreenManager:
                id: js_screen_manager
                MDScreen:
                    name: "introdusaunjs"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Introdusaun Javascript"
                            left_action_items: [['menu', lambda x: js_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "JavaScript mak linguajen programasaun ne'ebé uza hodi halo web interaktivu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "JavaScript mak lian programasaun ne'ebé sai hanesan kbiit boot ba mundu interativu iha internet laran tanba lahó JavaScript website sira sei sai de'it hanesan dokumentu statiku ne'ebé la bele fó resposta ba buat ne'ebé uza-na'in sira halo nune'e lian ne'e importante tebes ba dezenvolvimentu web modernu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Brendan Eich mak ema ne'ebé kria JavaScript iha tinan mil novesentos noventa i sinku de'it iha loron sanulu nia laran bainhira nia serbisu iha Netscape hodi fó kbiit foun ba browser sira nune'e bele kria dezañu ne'ebé dinámiku liu no la'ós de'it hatudu testu ho imajen ne'ebé mate de'it."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Diferensa boot entre JavaScript ho lian programasaun seluk mak nia bele la'o kedas iha browser laran lahó presiza instala programa todan sira seluk nune'e kualker ema ne'ebé iha kbiit de'it atu loke internet bele mós kria kódigu ne'ebé kmanek hodi kontrola buat hotu ne'ebé mosu iha sira-nia ekrán laran."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "JavaScript uza konseitu 'Client-Side Scripting' ne'ebé katak lójika hotu-hotu ne'ebé ita hakerek sei la'o iha uza-na'in sira-nia komputadór rasik nune'e fó rezultadu ne'ebé lalais tebes tanba la presiza hein resposta husi server ne'ebé dook bainhira ita klika de'it butaun ida ka muda kór."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Maske iha de'it naran 'Java' iha oin maibé ita tenke hatene katak JavaScript ho Java mak buat rua ne'ebé lahanesan duni tanba sira iha lójika no funsaun ne'ebé diferente tebes hanesan de'it kbiit husi karreta ho aviaun ne'ebé iha naran hanesan uitoan maibé la'o iha fatin ne'ebé ketak-ketak."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Evolusaun JavaScript nian liuhusi ECMAScript fó kbiit foun ba beibeik mai ita dezenvolvedór sira hodi kria kódigu ne'ebé seguru liu no mós kmaan liu hodi nune'e aplikasaun sira ne'ebé ita halo bele la'o ho kualidade ne'ebé aas tebes maske uza de'it telemóvel ne'ebé iha kbiit limitadu tebes."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Kbiit husi JavaScript la'ós de'it limite ba website de'it tanba ho teknolojia foun hanesan Node.js ita bele mós uza JavaScript hodi kria sistema iha server-side no mós kria aplikasaun ba telemóvel ka joga sira ne'ebé kompleksu tebes ne'ebé halo lian ne'e sai populár liu iha mundu tomak."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Aprende JavaScript mak pasu primeiru hodi komprende oinsá mundu dijitál ne'e serbisu tanba lójika sira ne'ebé ita aprende iha ne'e hanesan 'Variables', 'Data Types', no 'Functions' sei ajuda tebes ita hodi aprende lian programasaun seluk ho fasil liu tanba fundamentu lójika nian ne'ebé hanesan."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                    

                MDScreen:
                    name: "operatorjs"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Operator Javascript"
                            left_action_items: [['menu', lambda x: js_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                MDLabel:
                                    text: "JS Operators: +, -, *, /, %, ==, ===, !=, !=="
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Iha opertor ne'e mak sai hanesan matematik nian iha website coding laran ita boot sira bele hare iha coding kraik ne'e"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "JavaScript operators mak ferramenta fundamentál ne'ebé ita uza hodi manipula valór husi variável sira nune'e ita bele halo operasaun matemátika, komparasaun lójika, no mós atribuisaun dadus ne'ebé importante tebes ba funsionamentu husi kualker algorithm ne'ebé ita kria ona."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Uza arithmetic operators hanesan adisaun, subtraun, multiplikasaun, no divizaun permite ita-nia kódigu hodi suru númeru sira ho lalais tebes hodi rezolve kualker problema matemátika ne'ebé mosu iha ita-nia aplikasaun dashboard aprende nian ne'e."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Assignment operators hanesan '=' ka '+=' serve hodi rai valór foun ba variável ida ne'ebé fó dalan mai ita hodi atualiza informasaun sira iha memória laran bainhira programa ne'e la'o hela hodi nune'e ita bele jere estatutu husi aplikasaun ne'e ho kapa'as."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Comparison operators hanesan '==' no '===' mak importante tebes hodi teste se valór rua hanesan ka lae ne'ebé ajuda tebes iha foti desizaun nune'e ita bele garante katak kódigu sei foti de'it dalan ne'ebé loos bainhira kondisaun sira ne'e kumpri ona."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Logical operators hanesan AND, OR, no NOT fó kbiit mai ita hodi kahur kondisaun barak dala ida de'it nune'e ita-nia lójika bele sai kompleksu liu hodi kontrola fluxu husi aplikasaun ne'ebé ita dezenvolve hela ho kbiit JavaScript nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Modulus operator '%' mak kbiit ida ne'ebé dala barak ema haluha maibé nia útil tebes hodi buka restu husi divizaun ida ne'ebé fásil tebes atu uza hodi determina se númeru ida mak par ka impar iha lójika programasaun nian laran."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Exponentiation operator '**' ne'ebé foin mosu iha versaun foun JavaScript nian fó dalan mai ita hodi hasae númeru ida ba nia poténsia ho kódigu ne'ebé simples liu no fásil atu lee duke uza fali funsaun husi Math.pow ne'ebé uluk ita uza."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Unary operators hanesan increment '++' no decrement '--' mak dalan ne'ebé lalais liu hodi aumenta ka hamenus valór númeru nian ho ida de'it ne'ebé ita uza barak tebes iha laran loops hodi kontrola repetisaun sira ne'ebé ita kria."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ternary operator mak dalan badak ida hodi hakerek lójika if-else nune'e ita-nia kódigu bele sai moos liu no elegante liu bainhira ita presiza de'it foti desizaun simples bazeia ba kondisaun ida ne'ebé ita fó sai tiha ona iha liña ida de'it."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Aprende operators hotu-hotu iha JavaScript sei fó fundamentu ne'ebé forte tebes ba ita hodi sai programadór ne'ebé di'ak tanba lójika hotu-hotu ne'ebé ita kria sempre depende ba oinsá ita jere no manipula dadus sira-ne'e ho didi'ak tebes."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "operatorbazikujs.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "conditionaljs"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Conditional Javascript"
                            left_action_items: [['menu', lambda x: js_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                MDLabel:
                                    text: "JS Conditionals: if, else, else if, switch"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "ida nee hanesan hatudu kondisaun karik no la karik ou munking nian ou troka hanesan esplika ho script testu verbal nian"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Antonio nia tinan 30 se antonio tinan 30 entaun nia boot ona ou adultu se lae troka switch ou else nian mak Antonio laos tinan 30 maibe 12 entaun nia sei inosenete"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Lójika Conditional mak kapasidade husi kódigu JavaScript ida hodi foti desizaun bazeia ba faktu ne'ebé mosu nune'e aplikasaun ne'e la'ós de'it robó maibé bele hatene oinsá atu fó resposta ne'ebé loos ba uza-na'in."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Instruaun 'if' mak baze fundamental husi desizaun hotu-hotu iha ne'ebé kódigu iha nia laran sei la'o de'it se kondisaun ne'ebé ita fó mak loos ka 'true' nune'e ita bele kontrola fluxu husi programa ne'e ho didi'ak."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Uza 'else' permite ita hodi kria kbiit alternativu ida nune'e se kondisaun 'if' nian sala kódigu seluk sei la'o nafatin hodi garante katak aplikasaun ne'e la mate de'it bainhira uza-na'in hatama dadus ne'ebé sala."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "'else if' fó dalan mai ita hodi halo teste ba kondisaun oioin ne'ebé ketak-ketak nune'e ita bele kria lójika ne'ebé kle'an liu hodi jere kazu barak ne'ebé bele mosu iha mundu reál nia laran ho fasil tebes."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Switch statement mak opsaun ne'ebé kapa'as tebes hodi troka 'if-else' ne'ebé naruk demais tanba nia bele haree ba valór ida de'it hodi hili kazu ne'ebé loos ne'ebé halo kódigu ne'e moos liu no fásil ba manutensaun."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ita mós tenke komprende konseitu 'truthy' no 'falsy' iha JavaScript tanba iha valór balu ne'ebé la'ós de'it boolean maibé bele konsidera hanesan sala hanesan númeru zero ka testu mamuk ne'ebé bele lori ita ba sala."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Nested conditionals mak bainhira ita tau 'if' ida iha 'if' seluk nia laran ne'ebé permite ita hodi kria regra ne'ebé espesífiku tebes maske ita tenke kuidadu hodi kódigu ne'e la sai 'spaghetti' ne'ebé susar atu lee."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Uza conditionals hamutuk ho input husi uza-na'in mak xave hodi kria sistema validasaun hanesan formuláriu login ne'ebé bele hatene se naran-segredu loos ka sala hodi proteje informasaun privadu sira."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                Image:
                                    source: "conditionaljss.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "arrayjs"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Array Javascript"
                            left_action_items: [['menu', lambda x: js_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                MDLabel:
                                    text: "JS Arrays: let arr = [1, 2, 3]; push, pop, shift, unshift"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Ida nee hanesa lista ida ba iha notifikasi babain pop up mak notifikasaun sira bele hakerek code iha kraik "
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "arrayjs.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True
                                MDLabel:
                                    text: "Array iha JavaScript mak hanesan kestaun ida ne'ebé ita bele uza hodi rai informasaun barak ho tipu dadus ne'ebé oioin iha fatin ida de'it nune'e ita bele jere lista sasán ka naran sira ho organizadu liu no lalais liu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ita bele asesu ba elementu ida-idak iha array nia laran uza nia índise ne'ebé sempre komesa husi númeru zero nune'e ita bele foti informasaun ne'ebé ita presiza ho presiza tebes maske iha dadus rihun ba rihun iha laran."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Metódu '.push()' mak dalan ne'ebé populár liu hodi hatama dadus foun ba parte ikun liu husi array ida ne'ebé fó kbiit mai ita hodi kria lista ne'ebé dinámiku tebes ne'ebé bele aumenta ba nafatin tuir ita-nia hakarak."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Enkuantu '.pop()' serve hodi hasai fali elementu ikun liu husi array nian ne'ebé ajuda tebes hodi jere memória no mós hamoos informasaun ne'ebé ita la presiza ona iha ita-nia sistema laran ho de'it kódigu ne'ebé badak."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Propriedade '.length' fó hatene mai ita ho presiza tebes katak hira mak totál elementu ne'ebé iha array ida nia laran nune'e ita bele kontrola lójika repetisaun nian hodi la bele sai husi limitasaun dadus nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Metódu '.shift()' no '.unshift()' serve hodi manipula dadus iha parte oin husi array nian ne'ebé fó flexibilidade liután mai ita hodi jere fila informasaun sira nian maske lójika ne'e todan uitoan ba performance."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ita mós bele uza '.splice()' hodi hasai ka hatama elementu foun iha klaran husi array ida ne'ebé fó kbiit boot tebes hodi edita lista sira ne'ebé ita iha ona lahó presiza kria fali array foun ida ne'ebé foti fatin barak."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Metódu modernu hanesan '.forEach()' fó dalan mai ita hodi uza repetisaun ho kmanek liu hodi vizualiza dadus ida-idak husi array nian ba ekrán laran nune'e ita bele kria interface ne'ebé interativu tebes ba uza-na'in sira."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Array multidimensionál mak array ne'ebé iha array seluk iha nia laran ne'ebé ita uza hodi rai dadus ne'ebé iha forma hanesan tabela ka matrix ne'ebé importante tebes ba dezenvolvimentu joga ka lójika ne'ebé naruk."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Mestre ba Arrays mak mestre ba JavaScript tanba kbiit hodi jere lista informasaun mak buat ne'ebé halo diferensa boot entre programadór inisiante ho ida ne'ebé profisionál ona iha mundu dezenvolvimentu nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                MDScreen:
                    name: "loopsjs"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Loops Javascript"
                            left_action_items: [['menu', lambda x: js_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                MDLabel:
                                    text: "JS Loops: for, while, do...while, for...of, for...in"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "loop katak nia repet ou fila fila ho ida ne'e nia automatiku fila fale hanesan nia bele repete 1 to dala 100 no 100 dala 100 no mos nia bele loop hakerek 1 to 100"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Loops mak kbiit ne'ebé permite kódigu JavaScript hodi repete asaun ida dala barak ho automátiku nune'e ita la presiza kolen hodi hakerek kódigu ne'ebé hanesan dala atus ba atus iha ita-nia file laran."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "'For loop' mak modelu repetisaun ne'ebé populár liu tanba nia iha estrutura ne'ebé kompletu hodi determina iha ne'ebé mak komesa, saida mak kondisaun hodi para, no oinsá mak atu muda valór repetisaun nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Uza 'while loop' di'ak tebes bainhira ita la hatene loloos katak repetisaun ne'e tenke la'o dala hira maibé ita de'it hatene kondisaun saida mak tenke kumpri hodi nune'e repetisaun ne'e bele para ho di'ak."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "'Do-while loop' kmanek uitoan tanba nia sei la'o kódigu iha nia laran dala ida uluk antes nia haree ba kondisaun ne'e loos ka sala nune'e garante katak pelumenus asaun ida mosu duni iha ekrán laran."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "'For...of' loop mak dalan modernu hodi lee elementu hotu husi array ida ho kmanek tebes lahó presiza uza índise númeru nune'e kódigu sai moos liu no fásil tebes ba ema seluk hodi lee fali ita-nia lójika."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Uza 'break' iha loops laran fó dalan mai ita hodi sai kedas husi repetisaun ida se kondisaun ruma kumpri ona nune'e ita bele poupa enerjia komputadór nian hodi la gasta tempu ba buat ne'ebé ita hetan ona."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "'Continue' serve hodi 'pula' ka hakat liu repetisaun ida ne'ebé la'o hela hodi kontinua fali ba repetisaun tuir mai ne'ebé ajuda tebes hodi filtra dadus ne'ebé ita la presiza hatudu ba uza-na'in sira."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Infinite loop mak buat ne'ebé perigozu tebes tanba nia bele halo telemóvel ka komputadór 'hang' ka mate de'it tanba kódigu ne'e la para de'it hodi gasta memória hotu nune'e ita tenke kuidadu tebes hodi kria kondisaun."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Loops mak xave hodi kria 'rendering' ba lista dadus ne'ebé naruk tebes iha website laran hanesan hatudu post sira husi kualker média sosiál ne'ebé suli ba nafatin bainhira ita *scroll* ba okos ho kmaan."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Aprende lójika repetisaun ne'e sei halo ita sai programadór ne'ebé efisiente tebes tanba ita bele haruka komputadór hodi serbisu todan ba ita ho de'it kódigu balu ne'ebé kmanek no matenek tebes."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "loopjs.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

            MDNavigationDrawer:
                id: js_nav_drawer
                radius: (0, 16, 16, 0)
                MDNavigationDrawerMenu:
                    MDNavigationDrawerHeader:
                        title: "Luis App"
                        text: "Projetu Indpendente"
                        spacing: "4dp"
                        padding: "16dp", 0, 0, "16dp"

                    MDNavigationDrawerItem:
                        text: "Introdusaun Js"
                        on_release:
                            js_screen_manager.current = "introdusaunjs"
                            js_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Operator Baziku Js"
                        on_release:
                            js_screen_manager.current = "operatorjs"
                            js_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Conditional Js"
                        on_release:
                            js_screen_manager.current = "conditionaljs"
                            js_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Array Js"
                        on_release:
                            js_screen_manager.current = "arrayjs"
                            js_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Loops Js"
                        on_release:
                            js_screen_manager.current = "loopsjs"
                            js_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        icon: "logout"
                        text: "Sai"
                        on_release:
                            master_manager.current = "menu"
                            js_nav_drawer.set_state("close")

    # ==================== PHP SCREEN ====================
    MDScreen:
        name: "aprendephp"
        MDNavigationLayout:
            MDScreenManager:
                id: php_screen_manager
                MDScreen:
                    name: "introdusaunphp"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Introdusaun PHP"
                            left_action_items: [['menu', lambda x: php_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "PHP mak linguajen programasaun ba servidor (server-side)."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "PHP mak lian programasaun ne'ebé kria husi Rasmus Lerdorf, dezenvolvedór ida husi kantu Olanda-Kanadá ne'ebé iha tinan mil novesentos sianulu resin haat dezenvolve sistema ida ne'e hodi jere de'it nia pájina pesoál ka 'Personal Home Page' nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Iha inísiu, Rasmus kria PHP uza lian programasaun 'C' hodi bele fó kbiit ba nia de'it atu bele komunika ho 'web forms' no 'database' nune'e nia bele hatene sé mak vizita nia website no mós foti dadus sira ne'ebé vizitante sira haruka ba nia."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Rasmus Lerdorf la'ós mesak hodi halo PHP sai boot, tanba iha tinan mil novesentos sianulu resin hitu, dezenvolvedór na'in rua seluk ne'ebé naran Zeev Suraski no Andi Gutmans foti fali kódigu husi Rasmus hodi hakerek fali husi hun to'o rohan ne'ebé ita koñese ho naran PHP 3."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Mudansa husi Zeev no Andi mak sai hanesan xave boot ne'ebé transforma PHP husi ferramenta simples ida ba lian programasaun ne'ebé kompletu no poderozu tebes hodi kria website sira ne'ebé dinámiku tebes ne'ebé ita uza to'o ohin loron iha mundu dijitál."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Naran PHP ne'e rasik iha nia istória laran mós muda ona husi 'Personal Home Page' ba 'PHP: Hypertext Preprocessor' ne'ebé mak abreviasaun rekursivu ida ne'ebé hatudu katak PHP agora foka liu ba oinsá prosesu testu sira iha server laran antes hatudu ba ekrán."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Iha tinan rihun rua, PHP 4 fó sai ho teknolojia foun ne'ebé naran 'Zend Engine' ne'ebé halo PHP sai lalais liu no bele jere aplikasaun web ne'ebé boot tebes nune'e kumpañia sira mós komesa konfia no uza lian ida ne'e ba sira-nia negósiu online."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Istória PHP nian kontinua sai furak ho PHP 5 ne'ebé lori kbiit 'Object-Oriented Programming' ne'ebé kompletu liu hodi nune'e dezenvolvedór sira bele kria kódigu ne'ebé profesonál liu, organizadu liu, no mós seguru liu hodi proteje dadus uza-na'in sira nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Buat ne'ebé úniku iha PHP mak versaun PHP 6 nunka fó sai ofisialmente ba públiku tanba dezafiu tékniku ne'ebé boot tebes, nune'e komunidade deside hodi 'salta' kedas ba PHP 7 ne'ebé lori mudansa boot tebes iha parte performance no kualidade kódigu nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ohin loron, PHP ona iha versaun 8 ne'ebé iha teknolojia 'JIT compilation' ne'ebé permite aplikasaun sira la'o ho kbiit ne'ebé lalais tebes hanesan lian programasaun seluk ne'ebé ita uza ba dezenvolve software sira ne'ebé kompleksu tebes iha mundu tomak."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ikus liu mak PHP nia istória ne'e prova katak lian ida ne'ebé kmanek no fásil ba ema inisiante sira hodi aprende sei nafatin sai teknolojia xave ba futuru internet nian tanba nia komunidade ne'ebé boot no nafatin dezenvolve an hodi tuir nesesidade tempu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                MDScreen:
                    name: "syntaxphp"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Syntax PHP"
                            left_action_items: [['menu', lambda x: php_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "PHP Syntax: <?php ... ?> hodi hakerek kodigu PHP."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Pasu primeiru mak ita tenke download no instala XAMPP husi website ofisiál Apache Friends tanba programa ne'e mak hanesan 'paket kompletu' ida ne'ebé lori ona Apache Server, MySQL, no PHP dala ida de'it nune'e ita la presiza instala sira ida-idak ketak-ketak ne'ebé komplikadu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Depois de instala tiha, ita tenke loke 'XAMPP Control Panel' no klika butaun 'Start' ba Apache hodi nune'e ita-nia komputadór bele transforma an sai hanesan 'Local Server' ida ne'ebé prontu ona hodi prosesu kódigu PHP hotu-hotu ne'ebé ita sei hakerek."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Fatin ne'ebé importante liu iha XAMPP mak folder 'htdocs' ne'ebé baibain hela iha laran 'C:/xampp/htdocs' tanba ne'e mak 'fuan' husi server nian, iha ne'ebé kualker file ka folder ne'ebé ita tau iha laran mak browser bele haree no loke de'it."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ba ema beginner, di'ak liu kria folder foun ida iha laran 'htdocs' ho naran ne'ebé simples hanesan 'meu_projetu' hodi nune'e ita-nia file sira la kahur malu ho file default sira seluk no ita bele organiza ita-nia serbisu hotu ho moos no kapa'as."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Iha folder foun ne'e nia laran, kria file ida ho naran 'index.php' uza text editor hanesan VS Code tanba naran 'index' ne'e mak espesiál tebes, server sei buka no loke file ne'e uluk fali antes file sira seluk bainhira ita loke folder ne'e iha browser."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Keta haluha katak file PHP tenke remata ho estensaun '.php', la'ós '.html' ka '.txt', tanba se estensaun sala server sei la bele rekoñese lójika PHP ne'ebé iha laran no sei hatudu de'it testu baibain lahó prosesu kódigu sira ne'ebé ita halo."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Hakerek kódigu simples hanesan '<?php echo 'Ola Mundu'; ?>' iha laran hodi teste, depois loke browser hanesan Chrome ka Firefox no hakerek 'localhost/meu_projetu' iha address bar hodi nune'e browser bele haruka pedidu ba Apache hodi hatudu rezultadu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Se ita hakerek 'localhost' de'it, ne'e katak ita ko'alia hela ho ita-nia komputadór rasik nia 'ip address' lokal nian, no Apache sei hatudu kedas konteúdu hotu ne'ebé ita rai hela iha folder 'htdocs' ne'ebé ita foin kria tiha ona ne'ebá."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Bainhira ita halo mudansa iha kódigu, ita presiza de'it 'Refresh' pájina iha browser hodi haree rezultadu foun, nune'e ita bele aprende ho lalais tebes oinsá kódigu PHP nian troka konteúdu website nian ho dinámiku tebes tuir ita-nia hakarak."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ikus liu mak prátika mak xave importante, kontinua kria file foun no kria folder foun hodi aumenta ita-nia kbiit, tanba mestre ba PHP komesa husi buat ki'ik sira hanesan prepara XAMPP no kria file 'Hello World' ne'ebé ita foin halo ohin."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                MDScreen:
                    name: "variablephp"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Variable PHP"
                            left_action_items: [['menu', lambda x: php_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "PHP Variables: $name = 'value'; uza $ hodi declara variable."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Pasu primeiru ne'ebé ita tenke halo mak download no instala XAMPP husi website ofisiál Apache Friends tanba programa ne'e mak hanesan 'paket kompletu' ida ne'ebé lori ona Apache Server, MySQL, no PHP dala ida de'it nune'e ita la presiza instala sira ida-idak ketak-ketak."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Depois de instala tiha, ita tenke loke 'XAMPP Control Panel' husi ita-nia komputadór no klika butaun 'Start' ba Apache hodi nune'e ita-nia komputadór bele transforma an sai hanesan 'Local Server' ida ne'ebé prontu ona hodi prosesu kódigu PHP hotu-hotu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ita tenke hatene katak fatin ne'ebé importante liu iha XAMPP mak folder 'htdocs' ne'ebé baibain hela iha 'C:/xampp/htdocs' tanba ne'e mak 'fuan' husi server nian, iha ne'ebé kualker file ka folder ne'ebé ita tau iha laran mak browser bele haree no loke de'it."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ba ema ne'ebé foin aprende, di'ak liu kria folder foun ida iha laran 'htdocs' ho naran ne'ebé simples hanesan 'aprendende_php' hodi nune'e ita-nia file sira la kahur malu ho file default sira seluk no ita bele organiza ita-nia projetu hotu ho moos."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Iha folder foun ne'e nia laran, ita kria file ida ho naran 'index.php' uza text editor hanesan VS Code tanba naran 'index' ne'e mak espesiál tebes, server sei buka no loke file ne'e uluk fali antes file sira seluk bainhira ita loke folder ne'e iha browser."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Keta haluha katak file PHP tenke remata ho estensaun '.php', la'ós '.html' ka '.txt', tanba se estensaun sala server sei la bele rekoñese lójika PHP ne'ebé iha laran no sei hatudu de'it testu baibain lahó prosesu kódigu sira ne'ebé ita halo."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Hakerek kódigu simples hanesan '<?php echo 'Ola Mundu'; ?>' iha laran hodi teste, depois loke browser hanesan Chrome ka Firefox no hakerek 'localhost/aprendende_php' iha address bar hodi nune'e browser bele haruka pedidu ba Apache hodi hatudu rezultadu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Bainhira ita hakerek 'localhost' iha browser, ne'e katak ita ko'alia hela ho ita-nia komputadór rasik nia 'IP Address' lokal nian, no Apache sei hatudu kedas konteúdu hotu ne'ebé ita rai hela iha folder 'htdocs' ne'ebé ita foin kria tiha ona ne'ebá."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Sempre kuidadu hodi la bele taka XAMPP Control Panel bainhira ita sei hakerek hela kódigu, tanba se Apache 'Stop' tiha, browser sei la bele loke ita-nia file PHP no sei hatudu de'it error 'Site can't be reached' ne'ebé dala barak halo ema beginner sira tauk."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ikus liu mak prátika mak xave importante, kontinua kria file foun no kria folder foun hodi aumenta ita-nia kbiit, tanba mestre ba PHP komesa husi buat ki'ik sira hanesan prepara ambiente XAMPP no kria file 'Hello World' ne'ebé kmanek."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                MDScreen:
                    name: "tipudataphp"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Tipu Data PHP"
                            left_action_items: [['menu', lambda x: php_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "PHP Data Types: string, integer, float, boolean, array, object, null"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Tipu dadus mak kategoria husi informasaun ne'ebé variável ida bele rai, no iha PHP ida ne'e importante tebes tanba maske PHP bele determina mesak nia tipu, ita nu'udar programadór tenke komprende kbiit husi ida-idak nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "String mak tipu dadus ne'ebé ita uza hodi rai testu ka karaktér sira, hanesan naran uza-na'in ka hela-fatin, ne'ebé ita tenke tau iha laran aspas rua ka aspas ida nune'e PHP bele hatene katak ne'e mak testu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Integer mak númeru tomak ne'ebé la iha pontu dezimál ka vírgula, hanesan tinan ka kuantidade sasán nian, ne'ebé ita bele uza hodi halo kalkulasaun matemátika ne'ebé presiza tebes iha ita-nia lógika aplikasaun nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Float ka Double mak tipu dadus ba númeru ne'ebé iha pontu dezimál, ne'ebé ita uza hodi rai valór sira ne'ebé presiza detalhe boot hanesan folin osan, todan sasán nian, ka koordenada lokasaun nian ho presiza tebes."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Boolean mak tipu dadus ne'ebé simples liu maibé poderozu tebes tanba nia iha de'it valór rua mak 'True' ka 'False', ne'ebé sai hanesan fuan ba lógika foti desizaun nian iha ita-nia kódigu hotu-hotu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Array mak tipu dadus ida ne'ebé permite ita hodi rai valór barak iha variável ida de'it, ne'ebé ajuda ita hodi organiza lista informasaun sira ne'ebé iha relasaun ba malu nune'e ita-nia kódigu la sai runguranga."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Object mak tipu dadus ne'ebé rai dadus no mós informasaun oinsá atu prosesu dadus sira-ne'e bazeia ba 'Class' ne'ebé ita kria ona, ne'ebé lori ita ba konseitu programasaun profesonál hanesan Object Oriented Programming."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "NULL mak valór espesiál ida ne'ebé hatudu katak variável ida la iha valór ka mamuk loloos, ne'ebé útil tebes hodi hamoos variável ruma ka hodi teste se dadus ruma mai duni husi 'database' ka lae."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ita bele uza funsaun 'var_dump()' hodi haree loloos variável ida nia tipu dadus no mós nia valór, ne'ebé ajuda tebes dezenvolvedór sira hodi kria 'debugging' ka buka-tuir error bainhira kódigu la la'o tuir planu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Mestre ba tipu dadus mak xave hodi jere memória komputadór nian ho di'ak, tanba maske PHP matenek hodi troka tipu dadus ho automátiku, ita-nia kbiit hodi uza tipu dadus ne'ebé loos sei halo aplikasaun la'o lalais liu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                MDScreen:
                    name: "constantaphp"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Constanta PHP"
                            left_action_items: [['menu', lambda x: php_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "PHP Constants: define('NAME', 'value'); la muda durante execusaun."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Konstante mak fatin hodi rai informasaun ne'ebé nia valór sei la muda duni durante programa ne'e la'o, nune'e nia hanesan fatin rai-sasán ne'ebé ita xave metin tiha ona hodi ema ida la bele mai troka fali nia konteúdu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Diferensa ida ne'ebé boot tebes husi variável mak konstante la uza sinal osan-mean '$' iha oin, nune'e PHP bele hatene kedas katak ida ne'e mak buat ne'ebé permanente no la'ós variável baibain ne'ebé ita uza loron-loron."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Hodi kria konstante ida, ita uza funsaun 'define()' ne'ebé simu parámeter rua, mak naran konstante nian no mós nia valór, ka ita bele mós uza 'const' keyword ne'ebé mak dalan modernu liu hodi define buat ne'ebé statiku."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Konstante iha kbiit 'Global' husi hun to'o rohan, ne'ebé katak bainhira ita kria tiha ona konstante ida iha parte leten, ita bele uza fali nia valór iha kualker fatin iha kódigu laran lahó presiza kria fali ka bolu fali."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Baibain dezenvolvedór sira hakerek naran konstante uza letra boot hotu (UPPERCASE) hodi nune'e fásil ba ita hodi distinge entre variabel baibain ho konstante bainhira ita lee fali kódigu ne'ebé naruk tebes iha futuru."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ita uza konstante hodi rai informasaun ne'ebé sempre hanesan, hanesan naran 'database', 'base_url' husi website, ka folin 'PI' iha matemátika ne'ebé ita hatene katak nia folin sei nunka muda durante aplikasaun ne'e moris."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "PHP mós iha buat ne'ebé ita bolu dehan 'Magic Constants' ne'ebé komesa no remata ho 'underscore' rua, hanesan '__LINE__' hodi hatene liña kódigu nian ka '__FILE__' hodi hatene dalan loloos husi file ne'ebé ita loke hela."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Se ita koko hodi muda valór konstante ida depois de ita define tiha ona, PHP sei fó sai 'Error' tanba lójika husi konstante mak nia labele simu fali valór foun, ne'ebé ajuda tebes hodi proteje dadus importante sira."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Konstante mós bele rai dadus 'Array' bazeia ba versaun PHP foun nian, nune'e ita bele kria lista sasán ne'ebé permanete hodi uza iha sistema tomak lahó tauk katak parte kódigu seluk sei mai troka lista ne'ebé ita iha."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Aprende uza konstante ho didi'ak mak pasu ida hodi kria kódigu ne'ebé seguru no profesonál liu, tanba ita komesa hatene ona oinsá separa dadus ne'ebé bele muda no dadus ne'ebé tenke metin nafatin ba ita-nia sistema."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                MDScreen:
                    name: "operatorphp"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Operator PHP"
                            left_action_items: [['menu', lambda x: php_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "PHP Operators: +, -, *, /, ., ==, ===, &&, ||"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Arithmetic Operators mak operator ne'ebé ita uza hodi hala'o kalkulasaun matemátika báziku hanesan moin (+), menus (-), fali (*), no fahe (/) hodi nune'e ita-nia aplikasaun bele suru buat hotu ne'ebé ita presiza ho lalais."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Modulus operator ne'ebé uza símbolu porsentu (%) mak buat ne'ebé úniku tebes tanba nia la'ós fó rezultadu fahe nian maibé nia fó restu husi fahe nian, ne'ebé útil tebes hodi deteta númeru par ka impar iha lójika programa nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Assignment Operators hanesan sinal hanesan (=) ita uza hodi fó valór ba variável ida, maibé ita mós bele kahur nia ho operasaun seluk hanesan (+=) hodi aumenta valór foun ba valór ne'ebé iha ona lahó hakerek fali variável nia naran."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Comparison Operators mak ferramenta hodi kompara buat rua, hanesan (==) hodi haree se valór sira hanesan ka (!=) hodi haree se sira la hanesan, ne'ebé sai hanesan xave boot hodi determina dalan ne'ebé programa sei foti."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Identical operator (===) mak operadór ne'ebé estritu liu tanba nia la'ós de'it kompara valór maibé nia kompara mós tipu dadus, nune'e númeru 5 sei la hanesan ho testu '5' hodi nune'e ita-nia kódigu sai seguru liu husi error."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Increment no Decrement operators (++) no (--) mak dalan badak hodi aumenta ka hamenus valór ida husi variável, ne'ebé baibain ita uza barak tebes iha 'loops' laran hodi kontrola dala hira mak kódigu ida tenke repete an."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Logical Operators hanesan AND (&&), OR (||), no NOT (!) permite ita hodi kahur kondisaun barak sai ida de'it, nune'e ita bele kria lójika ne'ebé kompleksu hanesan 'se naran-uiza loos NO naran-segredu mós loos' foin bele tama."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "String Operators uza pontu (.) hodi halo 'concatenation' ka liga testu rua sai ida de'it, ne'ebé permite ita hodi kria fraze ne'ebé dinámiku tebes bazeia ba dadus ne'ebé foti husi uza-na'in ka husi database laran."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Operator Precedence mak regra ne'ebé PHP uza hodi determina ida ne'ebé mak tenke suru uluk, hanesan fali (*) no fahe (/) sempre manán moin (+) no menus (-), nune'e ita tenke kuidadu hodi uza parenteze () se hakarak muda regra ne'e."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Aprende operator sira ne'e ho didi'ak mak fundamentu hodi sai programadór ne'ebé matenek tanba kbiit hodi manipula dadus no foti desizaun lójika hotu-hotu depende ba oinsá ita uza operator sira ne'e iha kódigu laran."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                MDScreen:
                    name: "conditionalphp"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Conditional PHP"
                            left_action_items: [['menu', lambda x: php_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "PHP Conditionals: if, else, elseif, switch"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Conditional statements mak hanesan fuan husi lójika programasaun nian tanba nia permite programa hodi foti desizaun bazeia ba kondisaun ruma ne'ebé ita fó, hanesan de'it ita-nia moris loron-loron nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Instruaun 'if' mak forma simples liu husi kondisionál, iha ne'ebé kódigu ida sei la'o de'it SE kondisaun ne'ebé ita fó mak loos ka 'True', se lae PHP sei hakat de'it kódigu ne'e lahó halo buat ruma."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Uza 'else' permite ita hodi fó opsaun seluk bainhira kondisaun 'if' nian la loos, nune'e ita bele kria lójika ida ne'ebé kobre situasaun rua hanesan 'se natoon tinan bele tama, se lae tenke fila ba uma'."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Bainhira ita iha kondisaun barak ne'ebé ita hakarak teste, ita bele uza 'elseif' hodi kria korente desizaun nian ne'ebé naruk to'o ita hetan resposta ne'ebé loos ba problema ne'ebé ita hasoru iha kódigu laran."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Operadór lójika hanesan AND (&&) no OR (||) bele uza hamutuk iha 'if' laran hodi kria kondisaun ne'ebé kompleksu liu, hanesan teste se uza-na'in iha duni 'username' NO mós 'password' ne'ebé loos dala ida de'it."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "'Switch statement' mak dalan ida ne'ebé organizadu liu hodi kompara variável ida ho valór barak ne'ebé diferente, ne'ebé di'ak liu uza 'switch' duke hakerek 'if-elseif' barak demais ne'ebé halo kódigu susar atu lee."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Iha 'switch' laran, ita uza 'case' hodi define valór ida-idak no keta haluha uza 'break' hodi fó hatene ba PHP katak nia tenke sai ona husi 'switch' ne'e bainhira nia hetan ona resposta ne'ebé loloos."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Kondisaun 'default' iha switch laran serbisu hanesan 'else' iha 'if' nian, katak nia sei la'o de'it bainhira 'case' hotu-hotu ne'ebé ita kria la iha ida mak tuir valór ne'ebé ita buka hela iha sistema laran."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ita mós bele uza 'Ternary Operator' ne'ebé uza símbolu (?) no (:) hodi hakerek kondisaun 'if-else' simples iha liña ida de'it, ne'ebé ajuda tebes hodi halo ita-nia kódigu sai badak no elegante liu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Mestre ba kondisionál mak xave hodi kria aplikasaun ne'ebé dinámiku no interativu, tanba kbiit hodi responde ba situasaun oioin mak buat ne'ebé halo programa komputadór ida sai util ba uza-na'in sira."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                MDScreen:
                    name: "loopphp"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Loop PHP"
                            left_action_items: [['menu', lambda x: php_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "PHP Loops: for, while, do...while, foreach"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Loop mak konseitu programasaun ida ne'ebé permite ita hodi ezekuta bloku kódigu ida dala barak nune'e ita bele poupa tempu no enerjia hodi la presiza hakerek kódigu ne'ebé hanesan ba dala atus ba rihun."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Loop 'while' sei kontinua repete kódigu iha nia laran enkuantu kondisaun ne'ebé ita fó mak nafatin loos ka 'True', nune'e nia di'ak tebes uza bainhira ita la hatene loloos dala hira mak kódigu ne'e tenke repete."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Diferensa entre 'while' ho 'do...while' mak 'do...while' sei ezekuta kódigu iha laran ba dala primeiru duni antes nia ba teste kondisaun, nune'e ita bele garante katak kódigu ne'e sei la'ó pelumenus dala ida."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Loop 'for' mak loop ne'ebé populár liu tanba nia rai 'initialization', 'condition', no 'increment' iha liña ida de'it, ne'ebé halo kódigu sai organizadu liu bainhira ita hatene loloos dala hira mak ita hakarak repete kódigu ne'e."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Iha loop 'for' laran, ita uza 'counter' ida hodi foti kontajen nune'e ita bele asesu ba elementu sira husi lista ida bazeia ba sira-nia 'index' husi zero to'o rohan ne'ebé ita determina ona."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Loop 'foreach' kria espesiál de'it hodi uza ho 'Arrays', iha ne'ebé nia sei la'ó hodi foti valór ida-idak husi lista laran hodi ita bele prosesu lahó presiza jere 'counter' ka númeru 'index' nian ho liman."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Uza 'foreach' mak dalan ne'ebé seguru liu hodi lee dadus husi 'database' ne'ebé baibain mai iha forma lista, tanba nia sei para mesak de'it bainhira dadus hotu-hotu iha lista laran remata ona nia lee."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Instruaun 'break' bele uza iha loop kualker ida nia laran hodi haruka PHP hodi para kedas prosesu repetisaun maske kondisaun seidauk remata, ne'ebé útil tebes hodi poupa memória bainhira ita hetan ona buat ne'ebé ita buka."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Enkuantu 'continue' sei hakat de'it repetisaun ida ne'ebé la'o hela hodi kontinua fali ba repetisaun tuir mai, ne'ebé di'ak tebes uza bainhira ita hakarak hakat tiha dadus balu ne'ebé la tuir kitéria ne'ebé ita hakarak."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Kuidadu ho 'Infinite Loop' ne'ebé mosu bainhira kondisaun loop nian nafatin loos no nunka sai sala, tanba ida ne'e bele halo server 'hang' ka mate tanba gasta memória hotu hodi repete kódigu ne'ebé nunka para."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
            MDNavigationDrawer:
                id: php_nav_drawer
                radius: (0, 16, 16, 0)
                MDNavigationDrawerMenu:
                    MDNavigationDrawerHeader:
                        title: "Luis App"
                        text: "Projetu Indpendente"
                        spacing: "4dp"
                        padding: "16dp", 0, 0, "16dp"

                    MDNavigationDrawerItem:
                        text: "Introdusaun Php"
                        on_release:
                            php_screen_manager.current = "introdusaunphp"
                            php_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Syntax Php"
                        on_release:
                            php_screen_manager.current = "syntaxphp"
                            php_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Variable Php"
                        on_release:
                            php_screen_manager.current = "variablephp"
                            php_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Tipu Data Php"
                        on_release:
                            php_screen_manager.current = "tipudataphp"
                            php_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Constanta Php"
                        on_release:
                            php_screen_manager.current = "constantaphp"
                            php_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Operator Php"
                        on_release:
                            php_screen_manager.current = "operatorphp"
                            php_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Conditional Php"
                        on_release:
                            php_screen_manager.current = "conditionalphp"
                            php_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Loop Php"
                        on_release:
                            php_screen_manager.current = "loopphp"
                            php_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        icon: "logout"
                        text: "Sai"
                        on_release:
                            master_manager.current = "menu"
                            php_nav_drawer.set_state("close")

    # ==================== PYTHON SCREEN ====================
    MDScreen:
        name: "aprendepython"
        MDNavigationLayout:
            MDScreenManager:
                id: python_screen_manager
                MDScreen:
                    name: "introdusaunpython"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Introdusaun Python"
                            left_action_items: [['menu', lambda x: python_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Python mak linguajen programasaun ne'ebé fasil aprende no poderoso."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Python kria husi programadór naran Guido van Rossum iha tinan 1989 iha Olanda, no nia sai hanesan lian programasaun ne'ebé ohin loron ema uza barak liu iha mundu tanba ninia kbiit ne'ebé boot tebes."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Naran Python ne'e rasik la'ós foti husi kobra Python nian, maibé Guido foti naran ne'e husi grup komedi favoritu ida iha TV naran 'Monty Python’s Flying Circus' hodi hatudu katak lian ne'e tenke kmaan no diverte."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Objetivu primeiru husi kria Python mak hodi halo lian programasaun ida ne'ebé fásil tebes atu lee husi ema, nune'e kódigu sira ne'ebé ita hakerek la presiza komplikadu hanesan lian programasaun sira seluk iha tempu ne'ebá."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Python foin ofisialmente fó sai ba públiku iha tinan 1991 ho versaun 0.9.0, iha ne'ebé nia lori ona konseitu foun hanesan 'classes' no 'exception handling' ne'ebé ajuda programadór sira hodi jere error ho di'ak."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Iha tinan 2000, Python versaun 2.0 mosu hodi lori kbiit foun hanesan 'list comprehensions' no sistema 'garbage collection' ne'ebé ajuda hamoos memória automátiku nune'e aplikasaun la'o ho kmaan liu tan."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Mudansa boot liu akontese iha tinan 2008 bainhira Python 3.0 fó sai, iha ne'ebé sira halo 're-design' ba lian ne'e tomak hodi hamoos kódigu sira ne'ebé la importante ona maske ida ne'e halo kódigu husi versaun 2 la la'o iha versaun 3."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Filozofia husi Python mak 'The Zen of Python', ne'ebé hanorin katak 'Beautifull is better than ugly' no 'Simple is better than complex', halo lian ne'e sai kapa'as tebes ba ema ne'ebé foin mak aprende kódigu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ohin loron, Python la'ós de'it ba kria website simples, maibé nia sai hanesan instrumentu xave iha mundu Artificial Intelligence (AI), Data Science, no mós dezenvolvimentu aplikasaun mobile hanesan Kivy ne'ebé ita uza hela ne'e."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Aprende Python katak ita prepara an hodi tama ba mundu teknolozia modernu, tanba ho ninia komunidade ne'ebé boot tebes iha mundu tomak, ita sei nunka mesak bainhira hasoru problema tékniku ruma iha dalan klaran."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"MDLabel:
                                    text: "Python kria husi programadór naran Guido van Rossum iha tinan 1989 iha Olanda, no nia sai hanesan lian programasaun ne'ebé ohin loron ema uza barak liu iha mundu tanba ninia kbiit ne'ebé boot tebes."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Naran Python ne'e rasik la'ós foti husi kobra Python nian, maibé Guido foti naran ne'e husi grup komedi favoritu ida iha TV naran 'Monty Python’s Flying Circus' hodi hatudu katak lian ne'e tenke kmaan no diverte."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Objetivu primeiru husi kria Python mak hodi halo lian programasaun ida ne'ebé fásil tebes atu lee husi ema, nune'e kódigu sira ne'ebé ita hakerek la presiza komplikadu hanesan lian programasaun sira seluk iha tempu ne'ebá."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Python foin ofisialmente fó sai ba públiku iha tinan 1991 ho versaun 0.9.0, iha ne'ebé nia lori ona konseitu foun hanesan 'classes' no 'exception handling' ne'ebé ajuda programadór sira hodi jere error ho di'ak."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Iha tinan 2000, Python versaun 2.0 mosu hodi lori kbiit foun hanesan 'list comprehensions' no sistema 'garbage collection' ne'ebé ajuda hamoos memória automátiku nune'e aplikasaun la'o ho kmaan liu tan."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Mudansa boot liu akontese iha tinan 2008 bainhira Python 3.0 fó sai, iha ne'ebé sira halo 're-design' ba lian ne'e tomak hodi hamoos kódigu sira ne'ebé la importante ona maske ida ne'e halo kódigu husi versaun 2 la la'o iha versaun 3."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Filozofia husi Python mak 'The Zen of Python', ne'ebé hanorin katak 'Beautifull is better than ugly' no 'Simple is better than complex', halo lian ne'e sai kapa'as tebes ba ema ne'ebé foin mak aprende kódigu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ohin loron, Python la'ós de'it ba kria website simples, maibé nia sai hanesan instrumentu xave iha mundu Artificial Intelligence (AI), Data Science, no mós dezenvolvimentu aplikasaun mobile hanesan Kivy ne'ebé ita uza hela ne'e."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Aprende Python katak ita prepara an hodi tama ba mundu teknolozia modernu, tanba ho ninia komunidade ne'ebé boot tebes iha mundu tomak, ita sei nunka mesak bainhira hasoru problema tékniku ruma iha dalan klaran."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "syntaxpython.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "syntaxpython"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Syntax Python"
                            left_action_items: [['menu', lambda x: python_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Python Syntax uza indentasaun (spaces) la presiza {} ou ;"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Sintakse Python nian kria espesiál tebes hodi sai fásil ba ema hotu hodi lee no komprende, iha ne'ebé nia uza lian Inglés baibain hodi nune'e ita sente hanesan lee hela livru ida duke lee kódigu komputadór ne'ebé nakali."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Karakterístika boot liu husi Python mak 'Indentation' ka uza espasu hodi define bloku kódigu, nune'e ita la presiza uza 'curly braces' {} hanesan iha PHP ka Java hodi hatene kódigu ne'ebé mak pertense ba 'if' ka 'loop'."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Se ita-nia indatasaun ka espasu iha oin la hanesan, Python sei fó sai 'IndentationError', regra ne'e obriga programadór hotu hodi hakerek kódigu ne'ebé moos, organizadu, no kapa'as atu lee husi ema seluk."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Iha Python, ita la presiza uza titik-koma (;) iha rohan husi kódigu ida-idak, tanba Python hatene katak liña foun katak instruaun foun ida ona, ne'ebé halo ita-nia kódigu sai badak no la runguranga ho símbolu sira."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Python mak lian ne'ebé 'Case Sensitive', ne'ebé katak variável ho naran 'Kódigu' sei la hanesan ho 'kódigu', nune'e ita presiza kuidadu tebes bainhira hakerek naran variável sira hodi la kria error ne'ebé konfuzu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Hodi kria komentáriu ne'ebé Python sei la ezekuta, ita uza de'it símbolu 'hash' (#) iha oin, ne'ebé útil tebes hodi fó esplikasaun ba ita-nia kódigu nune'e ita la haluha lójika saida mak ita kria hela iha ne'ebá."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Python uza 'newline' hodi remata komandu ida, maibé se ita hakarak hakerek komandu ida ne'ebé naruk tebes iha liña barak, ita bele uza 'backslash' (\) hodi fó hatene ba Python katak kódigu ne'e seidauk remata."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Dalan ne'ebé Python kria 'function' uza keyword 'def' tuir ho naran funsaun nian no paréntese (), ne'ebé hatudu katak Python foka tebes ba simplicidade hodi nune'e dezenvolvedór sira bele foka liu ba lójika duke ba regra hakerek nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ita mós bele uza aspas ida (' ') ka aspas rua (\" \") hodi kria 'String', ne'ebé fó liberdade mai ita hodi uza símbolu sira iha laran lahó problema, buat ne'ebé hatudu fleksibilidade boot husi lian programasaun ida ne'e."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Aprende sintakse Python mak fundamentu importante tebes, tanba ho kódigu ne'ebé simples no moos, ita bele kria aplikasaun ne'ebé poderozu tebes husi sistema dezañu vizuál to'o ba inteligénsia artifisiál ne'ebé kompleksu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "syntaxpython.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "variablepython"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Variable Python"
                            left_action_items: [['menu', lambda x: python_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Python Variables: x = 5, name = 'Luis' (la presiza declara tipu)"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "variabelpython.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True
                                MDLabel:
                                    text: "Variável iha Python mak hanesan fatin rai-sasán ka 'container' ida ne'ebé ita uza hodi rai valór sira, nune'e ita bele bolu fali no uza fali informasaun ne'ebé rai ona iha fatin seluk iha ita-nia kódigu laran."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Python uza sistema 'Dynamic Typing', ne'ebé katak ita la presiza declara tipu dadus hanesan 'int' ka 'string' antes uza variável ida, tanba Python sei deteta mesak de'it bazeia ba buat ne'ebé ita hakerek."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Hodi kria variável ida, ita uza de'it naran variável nian tuir ho sinal hanesan (=) no fó nia valór,ne'ebé simples tebes no halo ita-nia kódigu sai badak no kapa'as."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Naran variável nian tenke komesa ho letra ka 'underscore' (_) no la bele komesa ho númeru, nune'e mós Python la permite ita uza símbolu espesiál hanesan @, $, ka % iha naran variável nia laran."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Python permite ita hodi fó valór ba variável barak dala ida de'it iha liña ida, hanesan 'x, y, z = 1, 2, 3', ne'ebé útil tebes hodi organiza ita-nia dadus ho lalais lahó presiza hakerek liña foun barak."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ita bele muda fali tipu dadus husi variável ida kualker tempu, hanesan husi númeru ba testu, buat ne'ebé hatudu katak Python fó liberdade boot mai ita hodi kria lójika ne'ebé fleksível tebes bazeia ba nesesidade."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Variável sira iha Python mós iha 'Scope' ka kbiit, iha ne'ebé variável ne'ebé kria iha funsaun nia laran ita bolu 'local variable' no sira ne'ebé kria iha li'ur ita bolu 'global variable' ne'ebé bele asesu husi ne'ebé de'it."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ita uza 'naming convention' hanesan 'snake_case' (naran_uiza_nain) hodi hakerek naran variável ne'ebé iha liafuan barak, nune'e ita-nia kódigu sai padraun no fásil ba dezenvolvedór seluk hodi lee no komprende."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Kuidadu hodi la uza 'keywords' husi Python hanesan 'if', 'else', ka 'while' nu'udar naran variável, tanba liafuan sira-ne'e Python rezerva ona hodi hala'o nia funsaun lójika rasik iha sistema laran."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Mestre ba oinsá jere variável mak pasu primeiru hodi kria kódigu ne'ebé efisiente, tanba variável mak sai hanesan rai-hun ba buat hotu ne'ebé ita sei halo iha dezenvolvimentu aplikasaun matenek sira iha futuru."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                MDScreen:
                    name: "datatipupython"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Data Tipu Python"
                            left_action_items: [['menu', lambda x: python_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Python Types: str, int, float, bool, list, tuple, dict, set"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "datatipupython.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True
                                MDLabel:
                                    text: "Data Tipu ka tipu dadus mak kategoria husi informasaun ne'ebé Python bele rekoñese no jere, iha ne'ebé kada tipu iha ninia karakterístika rasik hodi ajuda ita kria lógika ne'ebé loos."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "String (str) mak tipu dadus ba testu ne'ebé ita tau iha aspas laran, ne'ebé ita uza hodi rai naran, hela-fatin, ka kualker informasaun ne'ebé bazeia ba karaktér alfabetu nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Integer (int) mak númeru tomak ne'ebé la iha pontu dezimál, enkuantu Float mak númeru ne'ebé iha pontu dezimál, ne'ebé importante tebes ba kalkulasaun ne'ebé presiza presizaun aas."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Boolean (bool) mak tipu dadus ne'ebé simples liu tanba nia iha de'it valór rua: True ka False, ne'ebé sai hanesan baze ba foti desizaun hotu-hotu iha ita-nia kódigu laran."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "List mak koleksaun dadus ne'ebé ita bele muda (mutable) no organiza tuir orden, iha ne'ebé ita bele kahur tipu dadus oioin iha laran uza paréntese kuadradu [ ], ne'ebé fleksível tebes."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Tuple mak hanesan ho List maibé nia 'immutable', katak bainhira ita kria tiha ona, ita la bele troka tan nia valór, nune'e nia seguru liu hodi rai dadus ne'ebé tenke permanente nafatin."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Dictionary (dict) mak koleksaun ne'ebé la iha orden maibé uza sistema 'key:value', ne'ebé permite ita hodi rai informasaun ne'ebé iha relasaun, hanesan rai naran ema nian hamutuk ho nia tinan."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Set mak koleksaun ne'ebé la iha orden no la simu elementu ne'ebé hanesan ka 'duplicate', ne'ebé ajuda tebes hodi hamoos dadus ne'ebé dupla hodi nune'e ita-nia lista sai úniku de'it."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ita bele uza funsaun 'type()' hodi check loloos variabel ida nia tipu dadus saida, ne'ebé ajuda tebes bainhira ita halo 'debugging' ba kódigu ne'ebé ita dezenvolve hela."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Komprende tipu dadus sira-ne'e hotu mak xave hodi jere memória ho di'ak, tanba bazeia ba tipu dadus ne'ebé ita hili, Python sei jere ninia prosesu ho dalan ne'ebé efisiente liu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                MDScreen:
                    name: "numberpython"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Number Python"
                            left_action_items: [['menu', lambda x: python_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Python Numbers: int, float, complex"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Python iha tipu númeru oioin ne'ebé permite ita hodi halo kalkulasaun ho lalais, iha ne'ebé tipu sira-ne'e kria ona hodi jere memória ho efisiente bazeia ba valór númeru nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Tipu 'int' ka Integer mak númeru tomak ne'ebé bele pozitivu ka negativu lahó pontu dezimál, no Python permite ita hodi rai númeru ne'ebé boot tebes lahó limite memória ne'ebé restritu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Tipu 'float' mak númeru ne'ebé iha pontu dezimál ida ka liu, ne'ebé ita uza ba buat ne'ebé presiza presizaun hanesan osan, sasukat, ka rezultadu husi divizaun ne'ebé la'ós númeru tomak."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Python mós suporta númeru 'complex' ne'ebé uza letra 'j' nu'udar parte imajináriu, buat ida ne'ebé útil tebes ba fízika ka injeñaria ne'ebé presiza halo kalkulasaun kompleksu tebes."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Operadór aritmétika hanesan adisaun (+), subtraksaun (-), no multiplikasaun (*) serbisu hanesan baibain, maibé Python iha mós operadór úniku hanesan 'exponentiation' (**) hodi kria númeru pangkat."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Operadór 'floor division' (//) sei fahe númeru no hasai ninia pontu dezimál hodi fó rezultadu númeru tomak de'it, ne'ebé ajuda tebes bainhira ita presiza rezultadu ne'ebé simples."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Operadór 'modulus' (%) sei fó rezultadu husi restu divizaun nian, ne'ebé ita uza barak hodi buka-hatene se númeru ida mak númeru par ka ganjil iha ita-nia lójika programa nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ita bele uza funsaun 'round()' hodi halo arredondamentu ba númeru float ba númeru tomak ne'ebé besik liu, nune'e ita-nia rezultadu kalkulasaun sai moos no fásil atu lee."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Python iha mós funsaun hanesan 'abs()' hodi foti valór absolutu (pozitivu nafatin) no funsaun 'max()' ka 'min()' hodi buka valór ne'ebé boot liu ka ki'ik liu husi lista númeru nian."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Mestre ba oinsá Python jere númeru mak fundasaun ba 'data science' no 'machine learning', tanba algoritmu hotu-hotu ne'ebé matenek iha futuru sei bazeia ba kalkulasaun númeru sira-ne'e."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "numberpython.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True
                                
                                

                MDScreen:
                    name: "stringpython"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "String Python"
                            left_action_items: [['menu', lambda x: python_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Python Strings"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "String mak koleksaun husi karaktér sira ne'ebé ita tau iha aspas laran, no iha Python ita bele uza aspas ida (' ') ka aspas rua (\" \") hodi kria testu ne'ebé ita hakarak."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Konkatenasaun mak prosesu hodi liga String rua ka liu sai ida de'it uza sinal moin (+), ne'ebé permite ita hodi kria fraze ne'ebé kompletu husi variável oioin ne'ebé ita iha."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Python iha buat kapa'as ida naran 'f-strings', iha ne'ebé ita tau letra 'f' iha aspas oin hodi bele hatama variável loloos iha fraze laran uza 'curly braces' {}, halo kódigu sai moos liu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Funsaun 'len()' uza hodi suru karaktér hira mak iha String ida nia laran, inklui espasu, ne'ebé útil tebes hodi limita naruk husi 'username' ka 'password' ne'ebé uza-na'in sira hatama."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Metode 'upper()' no 'lower()' uza hodi muda String tomak ba letra boot ka letra ki'ik ho lalais, ne'ebé ajuda tebes hodi foti desizaun bainhira ita la hatene uza-na'in hakerek ho letra saida."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Metode 'strip()' serbisu hodi hamoos espasu mamuk ne'ebé la importante iha String nia oin no kotuk, nune'e dadus ne'ebé ita rai iha 'database' sai moos no la iha error tanba espasu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ita bele troka testu balu iha String laran uza 'replace()', hanesan troka liafuan 'Python' ba 'Java', ne'ebé fó kbiit mai ita hodi halo edisaun ba testu barak dala ida de'it."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Python permite 'String Slicing', katak ita bele foti de'it parte balu husi testu uza 'index' hanesan '[2:5]', ne'ebé hanesan ita tesi String ne'e hodi foti de'it buat ne'ebé ita presiza."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Hodi rai testu ne'ebé naruk tebes iha liña barak, ita bele uza aspas tolu nune'e Python sei rai formatu testu ne'e natoon de'it hanesan saida mak ita hakerek."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Mestre ba manipulasaun String mak xave hodi jere informasaun iha aplikasaun, tanba testu mak dalan prinsipál ne'ebé ita uza hodi komunika ho uza-na'in sira iha mundu dijitál."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "stringpython.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "conditionalpython"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Conditional Python"
                            left_action_items: [['menu', lambda x: python_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Python Conditionals: if, elif, else"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Kondisionál iha Python mak mekanizmu ne'ebé permite ita-nia programa hodi foti desizaun mesak bazeia ba kondisaun ne'ebé ita fó, nune'e kódigu ne'e bele sai 'matenek' hodi responde ba situasaun oioin."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Instruaun 'if' mak baze primeiru, iha ne'ebé Python sei check se kondisaun ida mak loos (True), foin nia ezekuta kódigu ne'ebé ita tau ho indentasaun iha nia okos hodi la'o tuir planu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Python la uza 'curly braces' {}, nune'e uza de'it 'colon' (:) iha rohan husi 'if' hodi hatudu katak kódigu ne'ebé tuir mai ho espasu (indentation) mak parte husi kondisaun ne'ebé ita kria."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Se kondisaun 'if' nian mak sala (False), ita bele uza 'else' hodi fó dalan seluk ba programa, nune'e ita-nia aplikasaun sempre iha resposta maske kondisaun primeiru ne'e la moris."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Diferensa boot ida husi PHP mak Python uza 'elif' (abreviasaun husi else if) hodi check kondisaun barak tumpuk malu, ne'ebé halo kódigu sai badak liu no fásil liu ba ema hodi lee."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Operadór komparasaun hanesan (==) ba hanesan, (!=) ba la hanesan, no mós boot liu (>) ka ki'ik liu (<) mak sai hanesan instrumentu prinsipál hodi kria kondisaun sira-ne'e hotu iha laran."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ita mós bele kahur kondisaun barak dala ida de'it uza operadór lójika 'and', 'or', no 'not', ne'ebé hakerek uza liafuan loloos nune'e ita sente hanesan ko'alia hela lian Inglés baibain."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Python mós iha 'Nested If', katak ita bele hatama tan 'if' ida iha 'if' seluk nia laran hodi kria lójika ne'ebé kle'an liu, maibé ita tenke kuidadu ho indentasaun nune'e la kria konfusaun."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Uza 'Short Hand If' permite ita hodi hakerek kondisaun simples iha liña ida de'it, ne'ebé ajuda tebes hodi halo kódigu Python sai elegante no 'Pythonic' tebes tuir ninia filozofia rasik."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Komprende kondisionál mak xave hodi jere fluxo aplikasaun nian, tanba kbiit hodi responde ba dadus uza-na'in nian mak buat ne'ebé halo diferensa entre kódigu mate no programa ne'ebé interativu."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "conditionalpython.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

                MDScreen:
                    name: "loopython"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: "Loop Python"
                            left_action_items: [['menu', lambda x: python_nav_drawer.set_state("open")]]
                        ScrollView:
                            do_scroll_x: False
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: "16dp"
                                spacing: "12dp"
                                
                                MDLabel:
                                    text: "Python Loops: for, while"
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                MDLabel:
                                    text: "Loop iha Python mak ferramenta ida ne'ebé permite ita hodi repete bloku kódigu ida dala barak, ne'ebé ajuda tebes hodi jere dadus barak lahó presiza hakerek kódigu ne'ebé hanesan dala barak."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Loop 'for' iha Python úniku tebes tanba nia la uza de'it númeru hodi suru, maibé nia la'o hodi foti elementu ida-idak husi 'sequence' hanesan List, Tuple, ka String hodi prosesu ho fasil."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Ita uza funsaun 'range()' hamutuk ho loop 'for' bainhira ita hakarak repete kódigu ba dala hira ne'ebé ita determina ona, nune'e Python hatene loloos horain mak nia tenke komesa no para."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Loop 'while' sei kontinua la'o enkuantu kondisaun ne'ebé ita fó nafatin loos (True), no nia sei para mesak bainhira kondisaun ne'e sai sala (False), nune'e ita bele kontrola prosesu ne'ebé naruk."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Diferensa boot ida husi PHP mak Python la iha loop 'do...while', maibé ita bele kria lójika ne'ebé hanesan uza 'while True' hamutuk ho kondisaun 'if' no 'break' iha nia laran."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Instruaun 'break' permite ita hodi para loop ida maske ninia kondisaun seidauk remata, ne'ebé útil tebes bainhira ita hetan ona buat ne'ebé ita buka iha lista dadus ne'ebé boot tebes laran."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Instruaun 'continue' uza hodi hakat repetisaun ida ne'ebé la'o hela no kontinua fali ba repetisaun tuir mai, nune'e ita bele hili de'it dadus ne'ebé ita hakarak prosesu no husik sira seluk."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Python iha mós kbiit ida naran 'Nested Loops', katak ita bele tau loop ida iha loop seluk nia laran, ne'ebé baibain ema uza hodi jere dadus ne'ebé kompleksu hanesan tabela ka matris."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Kbiit kapa'as ida husi Python mak 'else' iha loop nia rohan, ne'ebé kódigu ne'e sei la'o de'it bainhira loop ne'e remata loloos lahó 'break', buat ida ne'ebé lian programasaun seluk barak la iha."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"

                                MDLabel:
                                    text: "Mestre ba loop mak fundamentu hodi kria algoritmu ne'ebé efisiente, tanba kbiit hodi jere repetisaun mak buat ne'ebé halo komputadór ida bele halo serbisu ne'ebé ema labele halo ho lalais."
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    halign: "left"
                                Image:
                                    source: "looppython.png"
                                    size_hint_y: None
                                    height: (self.width / self.image_ratio) if self.image_ratio > 0 else "200dp"
                                    allow_stretch: True
                                    keep_ratio: True

            MDNavigationDrawer:
                id: python_nav_drawer
                radius: (0, 16, 16, 0)
                MDNavigationDrawerMenu:
                    MDNavigationDrawerHeader:
                        title: "Luis App"
                        text: "Projetu Indpendente"
                        spacing: "4dp"
                        padding: "16dp", 0, 0, "16dp"

                    MDNavigationDrawerItem:
                        text: "Introdusaun Python"
                        on_release:
                            python_screen_manager.current = "introdusaunpython"
                            python_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Syntax Python"
                        on_release:
                            python_screen_manager.current = "syntaxpython"
                            python_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Variabel Python"
                        on_release:
                            python_screen_manager.current = "variablepython"
                            python_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Data Tipu Python"
                        on_release:
                            python_screen_manager.current = "datatipupython"
                            python_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Number Python"
                        on_release:
                            python_screen_manager.current = "numberpython"
                            python_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "String Python"
                        on_release:
                            python_screen_manager.current = "stringpython"
                            python_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Conditional Python"
                        on_release:
                            python_screen_manager.current = "conditionalpython"
                            python_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        text: "Loop Python"
                        on_release:
                            python_screen_manager.current = "loopython"
                            python_nav_drawer.set_state("close")

                    MDNavigationDrawerItem:
                        icon: "logout"
                        text: "Sai"
                        on_release:
                            master_manager.current = "menu"
                            python_nav_drawer.set_state("close")
"""


class PiApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        return Builder.load_string(navigation_helper)


if __name__ == "__main__":
    PiApp().run()
