# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Bienvenido, skill chidoris listas?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class AnimalmarIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AnimalmarIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["mar"].value
        if consola_name == "delfin":
            consola_datos = " El delfin el el animal maritimo mas inteligente."
            
        if consola_name == "ballena":
            consola_datos = " es uno de los animales maritimos mas grande del mar."
            
        if consola_name == "nemo":
            consola_datos = " es el pescadito que se perdio."            
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class AnimalTerrestreIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AnimalTerrestreIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["terrestre"].value
        if consola_name == "iguana":
            consola_datos = " son muy latosas y mas con sus ruidos pero al final caen bien."
            
        if consola_name == "serpiente":
            consola_datos = " es muy temida pero la verdad y tiene miedo de la gente."
            
        if consola_name == "tigre":
            consola_datos = " el mayor miedo de las gacelas y el rey de los animales terrestres."            
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class AnimalesaereosIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AnimalesaereosIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["aereos"].value
        if consola_name == "paloma":
            consola_datos = " Pueden haber distintos tipos de paloma pero las palomas blancas dicen que es la paz."
            
        if consola_name == "agila":
            consola_datos = " uno de las mejores aves y el rey de todas."
            
        if consola_name == "pelicano":
            consola_datos = " el pelicano se alimenta de nemo."            
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SelvaanimalIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SelvaanimalIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["selva"].value
        if consola_name == "tigre":
            consola_datos = " es una de las especies??? de la subfamilia de los panterinos (familia Felidae) pertenecientes al g??nero Panthera."
            
        if consola_name == "pantera":
            consola_datos = " es jefe de wakanda, wakanda forever."
            
        if consola_name == "mono":
            consola_datos = " mucho ojo, yo vi planeta de los simios."            
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class insectosIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("insectosIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["insecto"].value
        if consola_name == "cucaracha":
            consola_datos = " insecto que se alimenta de sobras muertas o vivas, su morpologia esta muy rara."
            
        if consola_name == "mosca":
            consola_datos = " el peor insecto que dudo creear dios."
            
        if consola_name == "mosquito":
            consola_datos = " te pica en la noche y te saca sangre."            
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class generorockInten(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("generorockInten")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["rock"].value
        if consola_name == "muse":
            consola_datos = " Muse es una banda de rock alternativo originaria de la ciudad de Teignmouth, Devon (Inglaterra) formada en 1994 por Matthew Bellamy"
            
        if consola_name == "the beatles":
            consola_datos = " The Beatles fue un grupo musical de la d??cada de 1960 que revolucion??, no solamente el rock ingl??s sino la forma de hacer m??sica en general."
            
        if consola_name == "red hot":
            consola_datos = " Red Hot Chili Peppers es un grupo de California fundado en 1983 que combina funk y rock."            
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class generorapIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("generorapIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["rap"].value
        if consola_name == "aleman":
            consola_datos = " nacido en los cabos empezo a ser musica a los 14 a??os y es un gran exponente."
            
        if consola_name == "santa fe klan":
            consola_datos = "  es un rapero, cantante, y compositor mexicano, que incorpora a su producci??n musical g??neros como la cumbia??? y el rap mexicano."
            
        if consola_name == "cartel de santa":
            consola_datos = " es una banda mexicana de rap creada en la ciudad de Santa Catarina, Nuevo Le??n, M??xico. El grupo comenz?? sus actividades en el a??o 1999 bajo distintos nombres y miembros antes de tomar su nombre y alineaci??n definitivos."            
            
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class generojazzIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("generojazzIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["jazz"].value
        if consola_name == " coltrane":
            consola_datos = " John Coltrane (Hamlet, Carolina del Norte, 23 de septiembre de 1926 - Nueva York, 17 de julio de 1967)."
            
        if consola_name == "norah":
            consola_datos = " Geethali Norah Jones Shankar (30 de marzo de 1979), conocida como Norah Jones, es una cantante y pianista estadounidense de jazz y m??sica pop."
            
        if consola_name == "miles davis":
            consola_datos = " Miles Dewey Davis III, conocido art??sticamente como Miles Davis, (Alton, 26 de mayo de 1926."
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class generohiphopIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("generohiphopIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["hiphop"].value
        if consola_name == "mod def":
            consola_datos = " Definido inicialmente como uno de los artistas m??s prometedores de inicios de los 90, MOS Def ampli?? sus miras en los a??os siguientes"
            
        if consola_name == "mf doom":
            consola_datos = " Daniel Dumile (9 de enero de 1971 Londres Reino Unido - 31 de octubre de 2020 Londres Reino Unido) fue un rapero Brit??nico-Estadounidense."
            
        if consola_name == "mad villan":
            consola_datos = " Es un grupo americano de hip-hop formado por el MC DOOM y productor Madlib. Debutaron en 2004 con el ??lbum Madvillainy ."
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class razaperroIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("razaperroIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["raza"].value
        if consola_name == "schnauzer":
            consola_datos = " Peque??o, alegre, leal y barbudo es el schnauzer miniatura o zwergschnauzer. "
            
        if consola_name == "cavalier":
            consola_datos = " La raza de perro Cavalier King Charles spaniel es conocida por su aparici??n m??ltiples pel??culas, as?? mismo, tambi??n se populariz?? gracias a las celebridades que lo eligieron como perro de compa????a, tales como Coco Chanel, Oscar Wilde o Frank Sinatra."
            
        if consola_name == "cocker ingles":
            consola_datos = " El cocker spaniel ingl??s es un perro muy inteligente, juguet??n y sociable."
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class marcacelIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("marcacelIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["marcacelular"].value
        if consola_name == "iphone":
            consola_datos = " Phone es una l??nea de tel??fonos inteligentes de alta gama dise??ada y comercializada por Apple Inc. "
            
        if consola_name == "samsung":
            consola_datos = " Samsung (en hangul, ??????; en hanja, ??????) es un conglomerado de empresas multinacionales con sede en Se??l, Corea del Sur."
            
        if consola_name == "redmi":
            consola_datos = " Redmi es una submarca encargada de la l??nea de tel??fonos inteligentes de gama media, as?? como diversos accesorios dise??ados y comercializados por Xiaomi."
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class MarcapcIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MarcapcIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["marcapc"].value
        if consola_name == "msi":
            consola_datos = " Todos los ordenadores MSI se encuentran en esta selecci??n de PC de sobremesa especializados en Gaming.  "
            
        if consola_name == "asus":
            consola_datos = " ASUSTeK Computer, Inc. (en chino: ??????????????????????????????), conocida simplemente como ASUS ???pronunciado habitualmente con fon??tica inglesa ??ei-sus?????, es una corporaci??n multinacional de hardware, electr??nica y rob??tica??? con sede en Taip??i, Taiw??n, en el Distrito de Beitou."
            
        if consola_name == "lenovo":
            consola_datos = " Lenovo Group, Ltd.??? (en chino: ????????????, en pinyin: Li??nxi??ng j??tu??n), abreviado simplemente como Lenovo,??? es una compa????a multinacional china de tecnolog??a, con sede central en Pek??n, China. "
        
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class MarcatennisIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MarcatennisIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["marcatennis"].value
        if consola_name == "nike":
            consola_datos = " Es una empresa multinacional estadounidense dedicada al dise??o, desarrollo, fabricaci??n y comercializaci??n de equipamiento deportivo. "
            
        if consola_name == "adidas":
            consola_datos = " Estilizado adidas, con min??sculas, desde 1949)??? es una compa????a multinacional alemana fundada en 1949, con sede en Herzogenaurach, ciudad ubicada en Baviera. "
        if consola_name == "charly":
            consola_datos = " Es una compa????a mexicana que se dedica al dise??o, desarrollo, fabricaci??n y comercializaci??n de calzado, ropa deportiva y otros productos."
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class lacucaracha(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("lacucaracha")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["cucaracha"].value
        if consola_name == "cucaracha":
            consola_datos = " la cucaracha, ya no puede caminar, porque no tiene, porque le falta, marihuana que fumar. Ya se van los carrancistas, ya se van por el alambre, porque dicen los villistas, que se estar??n muriendo de hambre."
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class generoreggetonIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("generoreggetonIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["reggeton"].value
        if consola_name == "bad bunny":
            consola_datos = " Benito Antonio Mart??nez Ocasio, mejor conocido como Bad Bunny, es un rapero y compositor puertorrique??o de trap, rap y hip-hop en espa??ol. "
            
        if consola_name == "dady yankee":
            consola_datos = " Raymond Luis Ayala Rodr??guez (n. R??o Piedras, Puerto Rico, 3 de febrero de 1977), conocido art??sticamente como Daddy Yankee,. "
        if consola_name == "pit bull":
            consola_datos = " Hay varios artistas con este nombre. Armando Christian P??rez (Miami, Forida, Estados Unidos, 15 de enero de 1981) Sus padres, pertenecientes."
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class larachamaslinadaIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("larachamaslinadaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["lanochemas"].value
        if consola_name == "racha":
            consola_datos = "  Y te ped?? el perd??n que yo nunca concedo Te confes?? que no consegu?? remplazarte Y te dej?? en la alcoba despu??s de besarte Tus besos eran soles, mis manos pu??ales Tu sonrisa y la m??a se dijeron te quiero Y brotaron las frases poco tradicionales En una mujer libre y un hombre soltero Y esa fue la noche m??s linda del mundo Aunque nos durara tan solo un segundo Mas no me arrepiento, porque aquel momento Lo llevo grabado en mi pensamiento. "
            
        if consola_name == "noche":
            consola_datos = "  Y te ped?? el perd??n que yo nunca concedo Te confes?? que no consegu?? remplazarte Y te dej?? en la alcoba despu??s de besarte Tus besos eran soles, mis manos pu??ales Tu sonrisa y la m??a se dijeron te quiero Y brotaron las frases poco tradicionales En una mujer libre y un hombre soltero Y esa fue la noche m??s linda del mundo Aunque nos durara tan solo un segundo Mas no me arrepiento, porque aquel momento Lo llevo grabado en mi pensamiento. "
        if consola_name == "pit bull":
            consola_datos = " Hay varios artistas con este nombre. Armando Christian P??rez (Miami, Forida, Estados Unidos, 15 de enero de 1981) Sus padres, pertenecientes."
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class EntretenimientoIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("EntretenimientoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["streaming"].value
        if consola_name == "netflix":
            consola_datos = "   Netflix, Inc. es una empresa de entretenimiento y una plataforma de streaming estadounidense. Ubicada en Los Gatos (California), la compa????a fue fundada el 29 de agosto de 1997 y un a??o despu??s comenz?? su actividad, ofreciendo un servicio de alquiler de DVD a trav??s del correo postal.??? "
            
        if consola_name == "youtube":
            consola_datos = "  YouTube (pronunciado [??u??tub]) es un sitio web de origen estadounidense dedicado a compartir videos. Presenta una variedad de clips de pel??culas, programas de televisi??n y v??deos musicales, as?? como contenidos amateur como videoblogs y YouTube Gaming.  "
        if consola_name == "cuevana":
            consola_datos = " Cuevana es un sitio web argentino dedicado a la distribuci??n de producciones de cine y televisi??n a trav??s de la web.??? "
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class ReconocimientoterrorIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ReconocimientoterrorIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["peliterror"].value
        if consola_name == "el resplandor":
            consola_datos = "  Ese genio indiscutible llamado Stanley Kubrick domin?? todos y cada uno de los g??neros que abord?? a lo largo de su carrera. No es de extra??ar dado su excepcional talento que su incursi??n en el terror diese como resultado una obra maestra como lo es 'El resplandor'.??? "
            
        if consola_name == "halloween":
            consola_datos = "  Rodando en unos 20 d??as y con una limitaci??n de recursos m??s que obvia ???ten??an que recoger reutilizar hasta las hojas que aparec??an en el suelo de la calle entre plano y plano???, el maestro John Howard Carpenter revolucion?? el terror sentando c??tedra y marcando un antes y un despu??s en el subg??nero del slasher con este cl??sico de culto imperecedero.  "
        if consola_name == "la cosa":
            consola_datos = " Aunque mi obra predilecta de John Carpenter sea la genial 'En la boca del miedo', he de reconocer que el master of horror toc?? techo en 1982 con este remake de 'El enigma de otro mundo', que dirigi?? su idolatrado Howard Hawks en 1951. ??? "
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class RecomendacioncomendiaIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RecomendacioncomendiaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["comedia"].value
        if consola_name == "la otra missy":
            consola_datos = "  Esta divertida pel??cula estadounidense de Netflix es protagonizada por David Spade, como Tim Morris y Lauren Lapkus, como Melissa. Todo comienza cuando Tim conoce a la mujer de sus sue??os y est?? dispuesto a dar el siguiente paso invit??ndola al retiro de su empresa, pero por una confusi??n invita a la Melissa equivocada que conoci?? en su peor cita a ciegas.??? "
            
        if consola_name == "pasante de moda":
            consola_datos = " Protagonizada por Robert De Niro y Anne Hathaway, esta comedia dram??tica nos deja de lecci??n muchas cosas. Jules Austin es una mujer exitosa de una empresa de moda en l??nea, que debe contratar como proyecto laboral a una persona de la tercera edad para ser practicante. "
        if consola_name == "quienes son los miller":
            consola_datos = " Trata sobre un peque??o traficante de drogas que convence a sus vecinos para crear una familia falsa, despu??s de que un grupo de ladrones les roba el dinero de sus ventas y su jefe lo obliga a contrabandear droga desde M??xico.??? "
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class recomendacionsuspensoIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("recomendacionsuspensoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["suspenso"].value
        if consola_name == "multiple":
            consola_datos = "  Nunca nos cansaremos de ver a James McAvoy surfeando a trav??s de las muchas personalidades de este inquietante personaje en el centro de 'M??ltiple' de M??? "
            
        if consola_name == "codigo enperador":
            consola_datos = " Luis Tosar lidera el reparto de esta intriga patria basada en hechos reales y cargada de giros y sorpresas.  "
        if consola_name == "el perfume":
            consola_datos = " Basada en la famosa novela de Patrick S??skind y rodada parcialmente en Barcelona, 'El Perfume' es una perturbadora historia ambientada en la Francia del siglo XVIII y no apta para est??magos sensibles. "
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class MarcadeaireIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MarcadeaireIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["ac"].value
        if consola_name == "green":
            consola_datos = "  El aire acondicionado GREE aterriz?? en Espa??a hace ya varios a??os. Desconocido por muchos, GREE es la mayor empresa de aire acondicionado de todo el mundo ya que integra todo el ciclo de vida de cualquier producto: I+D (Innovaci??n y desarrollo), fabricaci??n propia, comercializaci??n y un excelente servicio postventa.??? "
            
        if consola_name == "mirage":
            consola_datos = " Somos la principal marca mexicana de aires acondicionados tipo minisplit, l??der nacional en ventas. Ampliamos nuestra gama de productos introduciendo componentes de LINEA BLANCA que integran los mismos est??ndares de eficiencia en ahorro energ??tico logrados con nuestros dise??os exclusivos, los modelos de la linea MAGNUM.  "
        if consola_name == "samsung":
            consola_datos = " Los aires acondicionados Samsung a trav??s del modo WindFree??? dispersa el aire de manera homog??nea y evita las corrientes directas. De esta manera, te proteges y cuidas a las personas que te importan. MITO: Dormir con el aire acondicionado encendido puede provocar un resfriado. "
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class marcatermosIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("marcatermosIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["termo"].value
        if consola_name == "flintronic":
            consola_datos = "  Un econ??mico recipiente t??rmico que te informa de la temperatura de su interior y dispone de filtro para caf?? o t??.??? "
            
        if consola_name == "matraz":
            consola_datos = "  Esta taza de viaje ha sido dise??ada para encajar a la perfecci??n en los soportes para coche sin derramar ni una gota.  "
        if consola_name == "termo milu":
            consola_datos = " Pensado para rellenarlo directamente bajo el surtidor de las cafeteras. "
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class marcagraficaIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("marcagraficaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["grafica"].value
        if consola_name == "nvidia":
            consola_datos = "  Nvidia surgi?? en los a??os 90 como uno de los muchos competidores en gr??ficos para PC, junto con 3DFX y ATI. Si bien las guerras de GPU de los a??os 90 fueron un momento interesante, dieron lugar a muchas adquisiciones y quiebras hasta que solo quedaron dos competidores: Nvidia y ATI.??? "
            
        if consola_name == "radeon":
            consola_datos = "  Radeon comenz?? como una marca ATI, no como una marca AMD. ATI, o Array Technology Inc., fue el principal rival de Nvidia en el espacio de gr??ficos para PC desde los a??os 90 hasta mediados de los 2000.  "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class CarrosawdIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CarrosawdIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["awd"].value
        if consola_name == "audi tt":
            consola_datos = " es el deportivo m??s peque??o de Audi que cuenta con sistema de tracci??n total. Mucha gente incluso lo llama un mini supercoche. Su precio arranca desde USD 43,950 y se ofrece con una gran variedad de opciones.??? "
            
        if consola_name == "dodge charger":
            consola_datos = " posee un sistema de tracci??n a las cuatro ruedas y s??lo emplea un motor V6 que entrega una capacidad de 305 hp. Su caja de cambios autom??tica ZF de 8 velocidades ayuda a brindar al propietario una experiencia de conducci??n extremadamente incre??ble.  "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Carroallterren(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("Carroallterren")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["allterren"].value
        if consola_name == "max v8":
            consola_datos = " Mel Gibson conduce el famoso negro 'V8 Interceptor', un coche de polic??a sobre la base de un Ford Falcon XB GT Coupe para localizar a la banda que mat?? a su familia. "
            
        if consola_name == "honda mxv750":
            consola_datos = " Las NXR ganaron el Dakar de 1986 a 1989 de forma consecutiva y es, sin duda, la abuela de las motos de los rallies raid de hoy.  "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Marcaaudifonos(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("Marcaaudifonos")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["audifonos"].value
        if consola_name == "jbl":
            consola_datos = " Creamos experiencias de audio inolvidables que amplifican cualquier momento. Donde quiera que est??s y cuando quieras escuchar, nuestra incomparable colecci??n de altavoces y auriculares ofrecen una experiencia incre??ble de audio envolvente."
        if consola_name == "sonny":
            consola_datos = " Estos son tipo cerrado, din??mico y de c??pula, lo que te da una buena reproducci??n del sonido y te aleja del ruido externo. Adem??s su respuesta de frecuencia es 10 a 24,000 Hz, lo que te permite escuchar gran rango de sonidos.   "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class FreestyleIntent(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FreestyleIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["liric"].value
        if consola_name == "wos":
            consola_datos = " Valent??n Oliva M??naco (Buenos Aires, 23 de enero de 1998), conocido art??sticamente como Wos (estilizado como WOS o WOS DS3), es un rapero, rapero de estilo libre, cantante y actor argentino. "
        if consola_name == "aczino":
            consola_datos = " Mauricio Hern??ndez Gonz??lez, mejor conocido como Aczino o Mau, es un rapero y freestyler procedente de la ciudad de Nezahualc??yotl ubicado en el pa??s de M??xico, siendo 4 veces campe??n nacional de Red Bull, pues ganar??a la Red Bull Nacional Colombia 2012 y la Red Bull Nacional M??xico   "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Estados(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("Estados")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["mejorEstado"].value
        if consola_name == "monterrey":
            consola_datos = " Monterrey es la capital y ciudad m??s poblada del estado mexicano de Nuevo Le??n, adem??s de la cabecera del municipio del mismo nombre.  "
        if consola_name == "queretaro":
            consola_datos = " oficialmente el Estado Libre y Soberano de Quer??taro, es uno de los treinta y un estados que, junto con la Ciudad de M??xico, forman M??xico.??????    "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class canaltele(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("canaltele")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["canales"].value
        if consola_name == "7":
            consola_datos = " Canal de las estrellas donde puedes encontrar novelas y deportes.  "
        if consola_name == "5":
            consola_datos = " Canal 5 uno de los mejores canales de entretenimiento.  "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class carroslentos(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("carroslentos")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["peorcarro"].value
        if consola_name == "lincon continental":
            consola_datos = " El unico valor que tiene este carro es por lo viejo, ya que por seguridad y motor muy malos.  "
        if consola_name == "cadilac coupe":
            consola_datos = " El unico valor que tiene este carro es por lo viejo, ya que por seguridad y motor muy malos.  "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Banda(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("Banda")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["cancionbanda"].value
        if consola_name == "ricardo":
            consola_datos = " la que con su risa me dejo sin habla.  "
        if consola_name == "cadilac coupe":
            consola_datos = " El unico valor que tiene este carro es por lo viejo, ya que por seguridad y motor muy malos.  "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class divisas(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("divisas")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["totaldivisas"].value
        if consola_name == "dlls":
            consola_datos = " cambio 18.23 pesos "
        if consola_name == "eur":
            consola_datos = " cambio 19.98 pesos.  "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class marcavaper(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("marcavaper")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["vaper"].value
        if consola_name == "vaporesso":
            consola_datos = " son uno de los calidad, precio por su rendimiento y resistencias."
        if consola_name == "smok":
            consola_datos = " marca estadounidense muy recomendada por su calidad.  "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class marcayogurt(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("marcayogurt")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["yogurt"].value
        if consola_name == "oikos":
            consola_datos = " marca estado unidense con poca saturacion de grasas y muy delicioso."
        if consola_name == "griego":
            consola_datos = " marca de yogurt natural, zero azucar con una textura inigualable.  "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#class Ganamundial(AbstractRequestHandler):
   # """Handler Generos intent."""
   # def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        #return ask_utils.is_intent_name("Ganamundial")(handler_input)

   # def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
      #9   if consola_name == "brasil":
    #        consola_datos = " probabilidad de ganar mundial 85%"
        #if consola_name == "mexico":
         #   consola_datos = " probabilidad de ganar mundial 55%  "
        #if consola_name == "argentina":
        #consola_datos = " probabilidad de ganar mundial 95%  "
            
        #speak_output = "  " + consola_name + consola_datos

        #return (
            #handler_input.response_builder
             #   .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
           #     .response
       # )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Comediantesmexicanos(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("Comediantesmexicanos")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["comediantemex"].value
        if consola_name == "sofia ni??a":
            consola_datos = " Comenz?? como actriz y artista clown hasta que incursion?? en el mundo de la comedia a trav??s de los shows de micr??fono abierto. "
        if consola_name == "roberto flores":
            consola_datos = " inici?? sus primeros pasos en el mundo de la comedia a trav??s del stand up y en especiales televisivos en Comedy Central, haci??ndolo uno de los rostros m??s conocidos y queridos de la industria. "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Comediantesusa(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("Comediantesusa")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["Comediausa"].value
        if consola_name == "jerry":
            consola_datos = " Comediante, actor y escritor, gana mas de 41 millones de dolares al a??o. "
        if consola_name == "kevin hart":
            consola_datos = "  El comediante y actor de estados unidos genero una fortuna desde el a??o 18 de junio del 2019. "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class escuelaprimaria(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("escuelaprimaria")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["primaria"].value
        if consola_name == "primaria lampar":
            consola_datos = " Muy buena escuela donde los sue??os se hacen realidad. "
        if consola_name == "frida khalo":
            consola_datos = " Escuela de los cabos con una buena infrestructura. "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class jugadoresargentinos(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("jugadoresargentinos")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["argentinos"].value
        if consola_name == "messi":
            consola_datos = " Jugador que no es de este planeta. "
        if consola_name == "lautaro":
            consola_datos = " jugador muy joven, futura promexa argentina. "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class jugadoresportugal(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("jugadoresportugal")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["portugal"].value
        if consola_name == "cristiano":
            consola_datos = " Jugador que no es de este planeta. "
        if consola_name == "pepe":
            consola_datos = " juega de defensa, tiene muchos a??os jugando con la selecion. "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class jugadoresbelgica(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("jugadoresbelgica")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["belgica"].value
        if consola_name == "bruyna":
            consola_datos = " con una derecha privilegida con mucha tecnica y espectacular tiro. "
        if consola_name == "hazard":
            consola_datos = " uno de los mejores delanteros con un ritmo inigualable. "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class jugadoresfrances(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("jugadoresfrances")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["francia"].value
        if consola_name == "mbape":
            consola_datos = " uno de las mejores promesas de estos a??os con una corrida exagerada. "
        if consola_name == "dembele":
            consola_datos = " esta recuperando su nivel y uno de los mejores exponentes franceses. "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class jugadoresmexicanos(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("jugadoresmexicanos")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["mexico"].value
        if consola_name == "lozano":
            consola_datos = " uno de las mejores promesas de estos a??os con una corrida exagerada. "
        if consola_name == "vega":
            consola_datos = " uno de los mejores jugadores mexicanos. "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class jugadoresespana(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("jugadoresespana")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["espana"].value
        if consola_name == "gavi":
            consola_datos = " uno de las mejores promesas de estos a??os, jugador de barcelona. "
        if consola_name == "busque":
            consola_datos = " muy buen medio campista con muchos a??os de experiencia. "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class jugadorescostarica(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("jugadorescostarica")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["costarica"].value
        if consola_name == "navas":
            consola_datos = " el mejor exponente de costa rica. "
        if consola_name == "busque":
            consola_datos = " muy buen medio campista con muchos a??os de experiencia. "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class marcataladro(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("marcataladro")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["taladros"].value
        if consola_name == "milwakeer":
            consola_datos = " Marca de taladros enfocado a su uso cotidiano, con una alto rendimiento en los trabajos mas fuertes. "
        if consola_name == "makita":
            consola_datos = " Marca de taladros enfocado a su uso cotidiano, con una alto rendimiento en los trabajos mas fuertes. "
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class marcacervezas(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("marcacervezas")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["cervezass"].value
        if consola_name == "ale":
            consola_datos = " Las ale, al rev??s que las lagers, son de fermentaci??n alta, es decir  que la fermentaci??n se produce en la superficie del fermentador. Se suele fermentar a temperaturas que rondan los 19 grados durante periodos cortos que van de 5 a 7 d??as (seguidos a menudo de una segunda fermentaci??n que tiene como objetivo reducir la turbidez de la cerveza). Suele tratarse de cervezas hechas con bastante cantidad de l??pulo y contenido alcoh??lico elevado. Insisto, esto son rasgos generales dado que como ya hemos explicado una cerveza ale es simplemente una cerveza fermentada con levadura ale y se puede hacer m??s o menos fuerte en funci??n de la cantidad de l??pulo y de malta que se a??ada. "
        if consola_name == "de trigo":
            consola_datos = " Son toda una categor??a en s??, y son especialmente importantes en Alemania. Est??n hechas total o parcialmente con malta de trigo, son claras de color y de baja graduaci??n. Se fermentan con levadura ale. La m??s conocida, la cerveza blanca, la weisse beer, que hace las delicias del Oktober Fest en Munich y que tiene una variante tambi??n maravillosa en Berl??n."
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class marcapila(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("marcapila")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["pilas"].value
        if consola_name == "panasonic":
            consola_datos = " su capacidad es de 1500 amps y su tiempo de vida son 5 horas. "
        if consola_name == "sonny":
            consola_datos = " su capacidad es de 1500 amps y su tiempo de vida son 9 horas."
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class tiponavegador(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("tiponavegador")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["navegador"].value
        if consola_name == "internet explorer":
            consola_datos = " Creado por Microsoft a mediados del a??o 1995, naci?? como Microsoft Internet Explorer, posteriormente Windows Internet Explore, hasta que gano popularidad como Internet Explorer nombre con el que se acu???? en el mercado digital y con el cual paso a la posteridad. "
        if consola_name == "crome":
            consola_datos = " Es uno de los navegadores webs m??s seguros, ligeros y r??pidos, creado por el gigante de Google, es de software privado, por lo que sus modificaciones solo pertenecen al propietario, no pudiendo ning??n usuario acceder a sus datos principales, ya que son de exclusividad del desarrollador."
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class marcaestereo(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("marcaestereo")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["estereo"].value
        if consola_name == "sonny":
            consola_datos = " bocinas de 15 whats y bajo de 10 pulgadas con una tolerancia a 30 whats. "
        if consola_name == "jbl":
            consola_datos = "  bocinas de 15 whats y bajo de 10 pulgadas con una tolerancia a 30 whats."
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class cancionaleman(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("cancionaleman")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["aleman"].value
        if consola_name == "aleman":
            consola_datos = " como le haces pa' rimar la verdad no lo se tengo una pin-- imaginacion que pueda crear. "
        if consola_name == "jbl":
            consola_datos = "  bocinas de 15 whats y bajo de 10 pulgadas con una tolerancia a 30 whats."
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class cancionloshombreg(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("cancionloshombreg")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["hombreg"].value
        if consola_name == "chica":
            consola_datos = " O te arrepentiras con mi polvo pica pica, sufreeeeeeeeee mamooooooooooooooooooooooooooooon de vulveme a mi chicaaaaaaaaa o te retorceras con mi polvo picapica.. "
        if consola_name == "jbl":
            consola_datos = "  bocinas de 15 whats y bajo de 10 pulgadas con una tolerancia a 30 whats."
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class blockesmaicra(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("blockesmaicra")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["bloquesminecraft"].value
        if consola_name == "mena de diamantes":
            consola_datos = " bloque de adquisicion de diamantes"
        if consola_name == "mena de oro":
            consola_datos = "  bloque de adquisicion de oro."
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class pokemontipoagua(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("pokemontipoagua")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["agua"].value
        if consola_name == "psyduck":
            consola_datos = " sideduck side dok"
        if consola_name == "squirtle":
            consola_datos = "  skuarel skuerel skuerel."
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class pokemontipotierra(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("pokemontipotierra")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["tierra"].value
        if consola_name == "caterpie":
            consola_datos = " pokemon tipo tierra para protegerse, despide un hedor horrible por las antenas con el que repele a sus enemigos."
        if consola_name == "metapod":
            consola_datos = "  pokemon tipo tierra, como en este estado solo puede endurecer su coraza, permanece inm??vil a la espera de evolucionar."
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class pokemontipofantasma(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("pokemontipofantasma")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["fantasma"].value
        if consola_name == "gastly":
            consola_datos = " Naci?? a partir de gases venenosos que asfixiar??an a cualquiera que se viera envuelto en ellos."
        if consola_name == "gengar":
            consola_datos = "  Las noches de luna llena, a este Pok??mon le gusta imitar las sombras de la gente y burlarse de sus miedos."
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class pokemontipohielo(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("pokemontipohielo")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["hielo"].value
        if consola_name == "dewgong":
            consola_datos = " Su cuerpo es blanco como la nieve. Puede nadar pl??cidamente en mares g??lidos gracias a su resistencia al fr??o."
        if consola_name == "cloyter":
            consola_datos = " La concha que lo cubre es extremadamente dura, hasta el punto de que ni siquiera una bomba puede destrozarla. Solo se abre cuando ataca."
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class pokemontiporoca(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("pokemontiporoca")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["roca"].value
        if consola_name == "onix":
            consola_datos = " Al abrirse paso bajo tierra, va absorbiendo todo lo que encuentra. Eso hace que su cuerpo sea as?? de s??lido."
        if consola_name == "geodude":
            consola_datos = " Se suele encontrar en senderos de monta??a y sitios parecidos. Conviene andar con cuidado para no pisarlo sin querer y provocar su enfado."
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class pokemontipohierro(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("pokemontipohierro")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["hierro"].value
        if consola_name == "steelix":
            consola_datos = " Seg??n dicen, si un Onix vive m??s de 100 a??os, su cuerpo adquiere una composici??n que recuerda a la de los diamantes."
        if consola_name == "aron":
            consola_datos = " Se alimenta de minerales de hierro o, en ocasiones, de v??as de tren para producir la coraza de acero que le protege el cuerpo."
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class terminamos(AbstractRequestHandler):
    """Handler Generos intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("terminamos")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        consola_name = handler_input.request_envelope.request.intent.slots["diego"].value
        if consola_name == "diego":
            consola_datos = " Despues de tanto tiempo, e terminado, gracias por su atencion, GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG."
        if consola_name == "aron":
            consola_datos = " Se alimenta de minerales de hierro o, en ocasiones, de v??as de tren para producir la coraza de acero que le protege el cuerpo."
            
        speak_output = "  " + consola_name + consola_datos

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(AnimalmarIntent())
sb.add_request_handler(AnimalTerrestreIntent())
sb.add_request_handler(AnimalesaereosIntent())
sb.add_request_handler(SelvaanimalIntent())
sb.add_request_handler(insectosIntent())
sb.add_request_handler(generorockInten())
sb.add_request_handler(generorapIntent())
sb.add_request_handler(generojazzIntent())
sb.add_request_handler(razaperroIntent())
sb.add_request_handler(marcacelIntent())
sb.add_request_handler(MarcapcIntent())
sb.add_request_handler(MarcatennisIntent())
sb.add_request_handler(lacucaracha())
sb.add_request_handler(generoreggetonIntent())
sb.add_request_handler(larachamaslinadaIntent())
sb.add_request_handler(EntretenimientoIntent())
sb.add_request_handler(ReconocimientoterrorIntent())
sb.add_request_handler(RecomendacioncomendiaIntent())
sb.add_request_handler(recomendacionsuspensoIntent())
sb.add_request_handler(MarcadeaireIntent())
sb.add_request_handler(marcatermosIntent())
sb.add_request_handler(marcagraficaIntent())
sb.add_request_handler(CarrosawdIntent())
sb.add_request_handler(Carroallterren())
sb.add_request_handler(Marcaaudifonos())
sb.add_request_handler(FreestyleIntent())
sb.add_request_handler(Estados())
sb.add_request_handler(canaltele())
sb.add_request_handler(carroslentos())
sb.add_request_handler(Banda())
sb.add_request_handler(divisas())
sb.add_request_handler(marcavaper())
sb.add_request_handler(marcayogurt())
#sb.add_request_handler(Ganamundial())
sb.add_request_handler(Comediantesmexicanos())
sb.add_request_handler(Comediantesusa())
sb.add_request_handler(escuelaprimaria())
sb.add_request_handler(jugadoresargentinos())
sb.add_request_handler(jugadoresportugal())
sb.add_request_handler(jugadoresbelgica())
sb.add_request_handler(jugadoresfrances())
sb.add_request_handler(jugadoresmexicanos())
sb.add_request_handler(jugadoresespana())
sb.add_request_handler(jugadorescostarica())
sb.add_request_handler(marcataladro())
sb.add_request_handler(marcacervezas())
sb.add_request_handler(marcapila())
sb.add_request_handler(tiponavegador())
sb.add_request_handler(marcaestereo())
sb.add_request_handler(cancionaleman())
sb.add_request_handler(cancionloshombreg())
sb.add_request_handler(blockesmaicra())
sb.add_request_handler(pokemontipoagua())
sb.add_request_handler(pokemontipotierra())
sb.add_request_handler(pokemontipofantasma())
sb.add_request_handler(pokemontipohielo())
sb.add_request_handler(pokemontiporoca())
sb.add_request_handler(pokemontipohierro())
sb.add_request_handler(terminamos())

sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()