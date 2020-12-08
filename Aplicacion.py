#Developed by:

#Wembie.

#PASOS A SEGUIR!

#1. instalar "https://bootstrap.pypa.io/get-pip.py"
#2. correrlo
#3. tecla Windows + X -> abrir PowerShell COMO ADMIN
#4. colocar ->
#5. pip install pandas
#6. pip install openxmllib
#7. pip install openpyxl
#8. pip install validate_email

import marshal
import random as rd
import os
import pandas as pd
import os.path as path
import datetime
from os import remove
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
from email import encoders
from openpyxl.workbook import Workbook
from validate_email import validate_email

def mostrarTips():
  print("1. ¿Cómo puedo dormir mejor?")
  print("2. ¿Cómo puedo conseguir bienestar psicológico?")
  print("3. ¿Cómo puedo sentirme mejor en la cuarentena?")
  print("4. ¿Cómo puedo superar la depresion?")
  print("5. ¿Cómo puedo dejar de sentirme solo?")
  print("6. Comprar version PREMIUM")
  print("0. Salir")

def dormirMejor():
  print("""\n¿Qué es el sueño?
Cuando usted duerme está inconsciente, pero las funciones de su cerebro y cuerpo siguen activas. El sueño es un complejo proceso biológico que le ayuda a procesar información nueva, mantenerse saludable y a sentirse descansado.

Durante el sueño, su cerebro pasa por cinco fases diferentes: Etapa 1, 2, 3, 4 y sueño de movimientos oculares rápidos (MOR o REM en inglés). Diferentes cosas ocurren en cada etapa. Por ejemplo, usted pasa por distintos patrones de ondas cerebrales (patrones de actividad eléctrica en el cerebro) en cada una de ellas. Su respiración, ritmo cardiaco y temperatura puede ser más rápido o lento en ciertas etapas. Algunas fases del sueño pueden ayudarle a sentirse más descansado y con energía al día siguiente. Las distintas fases del sueño lo ayudan a:

Sentirse descansado y con energía al día siguiente
Aprender información, hacer reflexiones y formar recuerdos
Descansar el corazón y el sistema vascular
Liberar más hormona del crecimiento, que ayuda a los niños a crecer. También aumenta la masa muscular y la reparación de células y tejidos en niños y adultos
Liberar hormonas sexuales, que contribuyen a la pubertad y la fertilidad
Evitar enfermarse o a mejorarse cuando está enfermo, creando más citoquinas (hormonas que ayudan al sistema inmunitario a combatir varias infecciones)
¿Cuánto sueño necesito?
La cantidad de sueño que usted necesita depende de varios factores, incluyendo su edad, estilo de vida, estado de salud y si ha dormido lo suficiente. Las recomendaciones generales para dormir son:

Recién nacidos: 16-18 horas al día
Niños en edad preescolar: 11-12 horas al día
Niños en edad escolar: por lo menos 10 horas al día
Adolescentes: 9-10 horas al día
Adultos (incluyendo adultos mayores): 7-8 horas al día
Durante la pubertad, el reloj biológico de los adolescentes cambia y es más probable que se acuesten más tarde que los niños y adultos, y tienden a querer dormir más por la mañana. Esto está en conflicto con las tempraneras horas de inicio de muchas escuelas secundarias y ayuda a explicar por qué la mayoría de los adolescentes no duermen lo suficiente.

Algunas personas piensan que los adultos necesitan dormir menos a medida que envejecen, pero no hay evidencia que lo demuestre. Sin embargo, a medida que las personas envejecen tienden a dormir menos o a pasar menos tiempo en el sueño profundo y reparador. Las personas mayores también se despiertan más fácilmente.

Y no sólo la cantidad de horas de sueño que obtiene es lo que importa. La calidad del sueño también es importante.

Las personas cuyo sueño suele interrumpirse o acortarse pueden no pasar suficiente tiempo en las diferentes etapas del sueño.

Si tiene dudas sobre si consigue dormir lo suficiente, incluyendo sueño de calidad, pregúntese lo siguiente:

¿Tengo problemas para levantarme por la mañana?
¿Tengo problemas para concentrarme durante el día?
¿Estoy somnoliento durante el día?
Si respondió afirmativamente a estas tres preguntas, debería tratar de dormir mejor.

¿Cuáles son los efectos a la salud de no dormir lo suficiente?
El sueño es importante para la salud en general. Cuando no duerme lo suficiente (privación del sueño), puede sentirse cansado y afectar su rendimiento, incluyendo su capacidad de pensar con claridad, reaccionar rápidamente y formar recuerdos. Esto puede llevarlo a tomar malas decisiones y ponerse en situaciones de riesgo. Las personas que no duermen bien son más propensas a sufrir accidentes.

La privación del sueño también puede afectar su estado de ánimo, lo que causa:

Irritabilidad
Problemas en sus relaciones, especialmente para niños y adolescentes
Depresión
Ansiedad
También puede afectar su salud física. Los estudios muestran que no dormir lo suficiente o dormir mal aumenta el riesgo de:

Presión arterial alta
Enfermedad del corazón
Accidente cerebrovascular
Enfermedad del riñón
Obesidad
Diabetes tipo 2
No dormir lo suficiente puede afectar la liberación de las hormonas que lo ayudan a crear masa muscular, combatir infecciones y reparar células. Además, en los niños puede hacer que no liberen suficientes hormonas que los hacen crecer.

La privación del sueño aumenta el efecto del alcohol. Una persona con sueño que beba demasiado alcohol resultará más afectada que una persona bien descansada.

¿Cómo puedo dormir mejor?
Usted puede tomar medidas para mejorar sus hábitos de sueño. En primer lugar, asegúrese de que tenga suficiente tiempo para dormir. Con dormir lo suficiente cada noche, usted puede sentirse mejor y más productivo durante el día.

Para mejorar sus hábitos de sueño, también puede ayudar:

Irse a la cama y despertar a la misma hora todos los días
Evitar la cafeína, especialmente por la tarde y noche
Evitar la nicotina
Hacer ejercicio con regularidad, pero no demasiado tarde
Evitar las bebidas alcohólicas antes de acostarse
Evitar comidas y bebidas pesadas por la noche
No tomar siestas después de las 3 de la tarde
Relajarse antes de acostarse, por ejemplo, tomando un baño, leyendo o escuchando música suave
Mantener su dormitorio con una temperatura fresca
Deshacerse de distracciones como ruidos, luces brillantes y el televisor o computadora en el dormitorio. Además, no se sienta tentado de usar su teléfono o tableta justo antes de acostarse
Obtener suficiente sol durante el día
No se acueste en la cama despierto. Si no puede dormir por 20 minutos, levántese y haga algo relajante
Consulte a un médico si tiene problemas constantes para dormir. Usted puede tener un trastorno del sueño, como insomnio o apnea del sueño. En algunos casos, su médico puede sugerir usar medicamentos para dormir disponibles con o sin receta médica. En otros casos, puede solicitar un estudio del sueño para diagnosticar el problema
Si usted trabaja por turnos, puede ser aún más difícil dormir bien. Es probable que usted necesite:

Tomar siestas y aumentar la cantidad de tiempo disponible para dormir
Mantener las luces prendidas en su trabajo
Limitar los cambios de turno para permitir que su cuerpo se ajuste
Consumir cafeína sólo al comienzo de su turno
Remover las fuentes de sonido y luz durante su descanso diurno (por ejemplo, usar cortinas que bloqueen la luz)""")

def sentirMejor():
  print("""\n¿Qué es el bienestar psicológico?
El concepto de bienestar psicológico, así como el de felicidad, son nociones muy difíciles de definir o determinar de manera concisa. No obstante, podemos decir que en ambos casos de trata de conceptos abstractos que se caracterizan por ser estados subjetivos relacionados con una sensación de bienestar y satisfacción general.

Por supuesto, los motivos o causas que generan esta satisfacción son diferentes en cada una de las personas y se ciñen a las creencias individuales que posee cada individuo en relación a lo él mismo entiende por bienestar psicológico o por felicidad.

No obstante, aunque tal y como hemos mencionado cada persona se distingue por poseer concepciones distintas de los que es sentirse bien psicológicamente, existen una serie de puntos comunes sin los cuales este bienestar psicológico es mucho más difícil de alcanzar. Estas dimensiones fueron desarrolladas por la psicóloga de la Universidad de Pennsylvania, Carol Ryff, y se compone de los siguientes aspectos:

Autoaceptación.
Relaciones positivas.
Tener un propósito en la vida.
Crecimiento personal.
Autonomía.
Dominio del entorno.
Como podemos observar todos estos aspectos son susceptibles de ser trabajados y mejorados, por lo que conseguir el bienestar psicológico està al alcance de nuestra mano. Es necesario especificar que, obviamente, esto no siempre va a ser sencillo, puesto que pueden aparecer eventos o agentes externos que perturben este bienestar y que no podemos controlar.

No obstante, aunque no tengamos el control sobre estos agentes, sí podemos determinar y decidir cómo enfrentarnos a ellos y qué grado de consideración otorgarles, siendo esto lo que marcará la diferencia a la hora de mantener nuestro bienestar psicológico o no.

10 consejos para conseguir el bienestar psicológico
Como ya mencionamos al inicio del artículo somos los únicos responsables de gestionar nuestra felicidad y nuestro bienestar mental, lo que nos convierte en agentes activos capaces de mejorar nuestro estado psicológico.

A continuación veremos una serie de consejos o recomendaciones que podemos practicar para mejorar nuestra salud psicológica y emocional. Esto no significa que para conseguirlo debamos realizar todas y cada una de estas indicaciones, puesto que este bienestar psicológico es un concepto totalmente subjetivo, podremos escoger aquellas con las que nos sintamos más cómodos o nos identifiquemos más.

1. Aprender a controlar nuestros pensamientos y emociones
Podríamos decir que este primer punto se trata de una recomendación universal válida para todo tipo de personas independientemente de su carácter o personalidad.

Habitualmente, nuestros pensamientos tienden a estar acompañados de emociones que los convierten en experiencias positivas o negativas. Si aprendemos a controlar y gestionar eficazmente nuestros pensamientos y emociones conseguiremos la habilidad necesaria para mejorar nuestro bienestar psicológico, siendo este el primer paso y la base que facilite el resto de nuestro trabajo psicológico.

Para ello podemos recurrir a ejercicios de meditación tradicional, así como a la práctica de ejercicios de mindfulness, los cuales han demostrado ser eficaces para la consecución del control de nuestros pensamientos y el bienestar emocional.

Artículo relacionado: "Regulación emocional: así domamos nuestro estado de ánimo"
2. Dedicar un momento a sentirse agradecido
Habitualmente, tendemos a mantener una fijación excesiva en los problemas y situaciones negativas que experimentamos a lo largo del día. Por lo tanto, nos puede resultar particularmente útil dedicar unos pocos minutos al día a reflexionar acerca de las cosas que nos han pasado a lo largo de la jornada por las cuales podemos dar las gracias.

Aunque esto pueda resultar difícil al principio, con la práctica nos costará cada vez menos identificar pequeños detalles diarios por los cuales podemos sentirnos agradecidos y satisfechos. Este hábito nos reportará una serie de sensaciones de bienestar diarias que se pueden llegar a mantener a lo largo de la semana.

3. Poner en orden nuestra vida

El exceso de estrés que experimentamos a diario es uno de los grandes enemigos del bienestar psicológico, puesto que merma poco a poco nuestra sensación de bienestar y tiende a ir en aumento si no hacemos nada para remediarlo.

Para solucionarlo, nos será de gran utilidad llevar a cabo una organización eficaz de nuestras tareas a lo largo del día. Esto nos ayudará a disminuir el efecto de los imprevistos y a experimentar una sensación de control sobre nuestra vida.

4. Dormir bien
Las rutinas de sueño afectan directamente a nuestro estado de ánimo por lo que unos hábitos de sueño perjudiciales repercutirán de manera negativa en nuestro bienestar psicológico.

Por lo tanto, es esencial intentar mantener unas costumbres de sueño en las que realicemos las horas mínimas de sueño recomendadas, siempre con todas las luces apagadas e intentando disminuir todo aquello que interfiera en nuestro sueño, como ruidos externos o el sonido del teléfono móvil.

Quizás te interese: "10 principios básicos para una buena higiene del sueño"
5. Mejorar la alimentación y realizar ejercicio
Tal y como describe la expresión mens sana in corpore sano, cuidar nuestro cuerpo y encontrar un equilibrio nos ayudará a conseguir y mantener nuestro bienestar psicológico. Al contrario de lo que popularmente se cree, el significado original de la expresión está relacionada con la necesidad de tener una mente y un cuerpo sano para poder alcanzar el bienestar.

Para ello, es esencial mantener una dieta equilibrada que nos proporcione todo tipo de nutrientes, así como realizar ejercicio de manera regular, lo que nos ayudará a mantener nuestro organismo en forma y a facilitar el equilibrio emocional.

6. Entablar conversación con otras personas
Los seres humanos somos animales sociales, por lo que mantenernos cerca de otras personas suele repercutir positivamente en nuestro estado de ánimo. Dedicar un momento de nuestro día para entablar una conversación con alguien conocido y aumentar así nuestras relaciones sociales, nos generará una sensación de bienestar y satisfacción muy placentera.

7. Romper la monotonía
Aunque cierto grado de rutina y monotonía nos ofrecen una sensación de seguridad y control sobre nuestra vida que puede resultar beneficiosa, el exceso de esta no suele resultarnos tan agradable, pudiendo aparecer sensaciones como el hastío, frustración o tristeza.

Para compensarlo, podemos planificar o establecer pequeños cambios en nuestra rutina diaria que nos puedan resultar estimulantes, así como mantener nuestra mente abierta ante la posibilidad de probar o experimentar cosas nuevas que aporten un poco de vivacidad y dinamismo en nuestra vida.

8. Hacer algo por otra persona
En psicología, es de sobra conocido el efecto positivo que el hecho de ayudar a los demás ejerce sobre nuestro estado de ánimo y sobre nuestro bienestar psicológico. Hacer algo por alguien aumenta nuestros niveles de felicidad y satisfacción, así como aporta una sensación de utilidad y competencia, reduce los niveles de estrés y cómo no aporta algo bueno a la sociedad y al estado anímico de la otra persona.

9. Realizar actividades artísticas
No es necesario ser un prodigio artístico para beneficiarse de los efectos positivos que la realización de actividades artísticas tiene sobre nuestro estado de ánimo. El arte, manifestado de la forma que sea, aumenta nuestros niveles de dopamina y estimula ciertas zonas de nuestra corteza frontal que provocan sensaciones positivas y placenteras.

10. Estar en contacto con la naturaleza
Finalmente, son muchos los estudios que han relacionado el vivir o estar cerca de la naturaleza o las zonas verdes con mejores cotas de salud mental y de bienestar emocional.

La conexión con la naturaleza genera un impacto positivo en nuestro estado de ánimo. Además, el simple hecho de estar expuestos a la luz del sol nos ayuda a aumentar los niveles de vitamina D, la cual está relacionada directamente con la disminución de emociones negativas como la tristeza.""")

def sentirMejorCuarentena():
  print("""\n1. NOTA PARA TI MISMO: ESTÁS SALVANDO VIDAS

Quedarte en casa con la mentalidad de que lo haces para salvar vidas y que estás contribuyendo a detener el virus puede hacerte sentirte menos abrumado.
“En lugar de quedarse en casa por temor lo que te ayuda es el pensamiento de que te quedas para proteger a los demás y evitar que otros se contagien”, mencionó el doctor Caraza. 
Manos sosteniendo un letrero con el mensaje: "Quédate en casa, salva vidas"


2. EXPRESA TU SENTIR

Hablar de cómo te sientes con tu familia o roomies y escuchar cómo se sienten ellos es otro de los consejos del especialista para no sentirte tan abrumado.
“Analizar lo que nos está pasando, externar si me siento ansioso o preocupado con la gente cercana nos ayuda a que fluya mejor lo que hacemos”, señaló el doctor Caraza. 


3. ¿ASISTES A TERAPIA O QUIERES TOMAR UNA? BUSCA OPCIONES VIRTUALES

Si asistes a terapia de algún tipo busca cómo continuar las sesiones de manera virtual. También si necesitas que alguien te escuche puedes buscar especialistas que estén realizando terapias online.
Una opción para los miembros de la comunidad Tec es la línea TQueremos, donde hay asesoría psicológica disponible 24/7: 01800 813 9500. También a través de la app Orienta. 
Chica tomando terapia virtual a través de su tablet

 
4. ESCRIBE UN DIARIO

Si vives solo, estudias en otra ciudad o no eres de los que platican tan fácil sobre sus sentimientos, llevar un diario puede servirte para saber cómo te sientes y relajarte.
“Escribir ayuda a no solo tenerlo en mente. Plasmarlo y poder verlo es muy bueno y puede ayudarte a sentirte mejor”, indicó el especialista. 
Manos de un chico joven escribiendo un diario

 
5. CONOCE EL MUNDO SIN SALIR DE CASA

Visita sitios web en los que puedes recorrer museos del mundo de manera virtual o ver videoblogs sobre viajes y sitios turísticos.
El doctor Caraza también recomienda buscar sitios donde puedas leer libros de manera gratuita, tomar cursos en línea gratis e incluso ver conciertos en tiempo real.

 
6. CREA UN HORARIO PARA TU DÍA

El doctor Caraza afirma que armar una rutina para trabajar o estudiar desde casa, además de tener horarios para disfrutar en familia, ver películas o jugar videojuegos, puede hacer más fácil tu aislamiento.

 
7. MUEVE Y RELAJA TU CUERPO

Desde técnicas de respiración hasta ejercicio en casa y yoga son algunas de las actividades que pueden ayudarte a mantenerte relajado.
“Busca apps que te ayudan a meditar o te ponen ruido ambiental de fondo. Hay muchas opciones gratuitas en línea”, sugirió el especialista.
Madre e hijo realizando yoga desde casa

 
8. ¡KEEP CALM! TRATA DE NO CAER EN PÁNICO

Estar informados sobre el coronavirus y el COVID-19 es importante, pero el especialista menciona que si esto te causa ansiedad o temor es mejor reducir el tiempo que pasas frente a la pantalla o buscando noticias.
“Hay demasiada información en internet y muchas noticias pueden ser fake news. Mantente informado una o dos horas al día y sobre todo en sitios como el de la OMS o páginas como la del Tec y de otras instituciones formales”, puntualizó el doctor Caraza.""")

def superarDepresion():
  print("""Si estás deprimido, lo mejor es que hagas algo al respecto: las depresiones no se curan solas. Aparte de pedir ayuda a un médico o terapeuta, hay cinco cosas que puedes hacer para encontrarte mejor.

1. Ejercicio físico. Anda a paso ligero de 15 a 30 minutos cada día, o baila, corre o monta en bicicleta, si lo prefieres. A las personas deprimidas no les suele apetecer estar activas. Pero, de todos modos, oblígate a hacerlo (pídele a un amigo que te acompañe si lo necesitas para estar motivado). En cuanto hagas del ejercicio un hábito, no tardarás mucho en percibir un cambio positivo en tu estado de ánimo.
Aparte del ejercicio aeróbico, algunas posturas de yoga te pueden ayudar a aliviar los sentimientos depresivos. Prueba la postura del perro con la cabeza hacia abajo o la de piernas arriba contra la pared (puedes encontrar estas dos posturas en sitios de Internet sobre yoga). Hay otros dos aspectos del yoga: los ejercicios de respiración y la meditación, que también pueden ayudar a encontrarse mejor a la gente deprimida.

2. Cuídate alimentándote bien. La depresión puede afectar al apetito. Cuando están deprimidas, a algunas personas no les apetece nada comer, pero hay otras pueden comer demasiado. Si la depresión ha afectado a tus hábitos alimentarios, tendrás que tener muy presente la necesidad de alimentarte bien. La nutrición puede influir en el estado de ánimo y el nivel de energía de una persona. O sea que come abundante fruta y verdura y sigue un horario de comidas regular (aunque no tengas hambre, intenta comer algo ligero, como una pieza de fruta, para seguir adelante).

3. Identifica los problemas, pero no les des vueltas. Intenta identificar las circunstancias que han contribuido a tu depresión. Cuando sepas qué es lo que te ha hecho sentirte triste y decaído y por qué, habla sobre ello con un amigo que te aprecie. Hablar es una forma de dar rienda suelta a los sentimientos y de recibir algo de comprensión.
Una vez hayas aireado esos pensamientos y sentimientos, centra la atención en algo positivo. Actúa para solucionar tus problemas. Pide ayuda si la necesitas. Sentirse conectado con los amigos y la familia puede ayudar a aliviar los sentimientos depresivos. Y tú también puedes ayudarles a sentir que pueden hacer algo por ti en vez de limitarse a ver lo trise que estás.

4. Exprésate. Cuando una persona está deprimida, puede tener bloqueadas la creatividad y la capacidad para disfrutar de las cosas. Ejercita tu imaginación (pintando, dibujando, haciendo garabatos, cosiendo, escribiendo, bailando, componiendo música, etc.) y no sólo conseguirás que fluyan tus jugos creativos sino que es posible que también experimentes emociones positivas. Dedica tiempo a jugar con un amigo o con tu mascota o haz algo divertido a solas. Encuentra algo de qué reírte; como una comedia, por ejemplo. La risa ayuda a levantar el ánimo.

5. Intenta fijarte en el lado positivo de las cosas. La depresión repercute sobre los pensamientos de las personas, haciendo que todo parezca negro, desastroso, triste y negativo. Si la depresión te está haciendo fijarte solo en lo negativo, haz un esfuerzo para fijarte en las cosas buenas de la vida. Primero intenta identificar una cosa positiva, luego intenta buscar otra más. Considera tus puntos fuertes, tus dones y lo afortunado que eres. Y, sobre todo, no te olvides de tener paciencia contigo mismo. La depresión requiere tiempo para curarse.""")

def sentirseSolo():
  print("""Si te sientes solo cuando estás solo, quizás estés en mala compañía. —Jean Paul Sartre

Solo.
Ignorado.
Incomprendido.

Quizás sea porque has tenido un desengaño amoroso, has perdido un ser querido, o has sufrido una gran desilusión.

Puede que lleves tiempo sin pareja, que te hayan rechazado o puede que te sientas así incluso habiendo formado una gran una familia.

La cuestión es que te invade una sensación de tristeza difícil de explicar. Te sientes desconectado del mundo, como si todo lo que motiva a la gente fuera ajeno a ti y no le importaras a nadie.

Tu dolor te impide ver más allá de este momento de sufrimiento. Querrías compartir tu tristeza con alguien que pudiera entenderte, pero no hay nadie.

Si alguna vez te has sentido perdido, abandonado o sin alguien que te ame, seguramente sepas de lo que te hablo.

Me siento solo

Yo lo he vivido en varios momentos de mi vida. En algunos casos por una causa concreta, pero en otros simplemente me invadía la sensación de estar fuera de lugar, sin que nadie pudiera comprender mis pensamientos.

Si lo piensas, es paradójico. Da igual los amigos de Facebook que tengas. Hoy estamos más conectados que nunca, pero a la vez más aislados que en ningún otro tiempo. Es perfectamente posible tener 1.000 amigos en Facebook, 700 seguidores en Twitter y ni una sola persona a la que llamar para tomar algo por la noche.

Pero hay esperanza.

Dicen que la mejor forma de vencer a un enemigo es conociéndolo, así que me puse a investigar qué decía la ciencia al respecto. Por eso hoy te traigo este artículo donde descubrirás la cara amarga de la soledad, pero también las mejores herramientas psicológicas para romper sus cadenas y vivir una vida más libre.

¿Qué aprenderás en este artículo? [mostrar]

¿Qué es la soledad?
Empecemos por una sencilla definición.

La soledad es la circunstancia de estar sin compañía en algún lugar durante un determinado período de tiempo, ya sea por elección propia o circunstancias ajenas.

Sin embargo, el sentimiento de soledad es otra cosa totalmente distinta. No está relacionado con la compañía, ni el número de amigos, vida en pareja o familiares que tengas, sino en cómo te sientes respecto a todo eso.

Y cuando la soledad se prolonga, las emociones negativas pueden llegar a ser muy intensas.

Por qué el miedo a la soledad te deprime tanto
Nacemos solos y moriremos solos. Entonces, ¿por qué nos deprime tanto la soledad? ¿No se supone que deberíamos ser capaces de estar a gusto simplemente con nosotros mismos? ¿No sería eso maravilloso?

La respuesta a esa pregunta está en nuestra evolución como especie humana.

Estamos programados para estar en contacto. Todos los animales sociales saben que quedarse aislados reduce drásticamente sus probabilidades de sobrevivir y reproducirse, y por eso evitan la soledad (Cacioppo et al. 2015).

Sentirte solo es como una alarma anticuada. Tu cuerpo te avisa de que alejarte de la sociedad, de la gente que te ama, pone en peligro tu supervivencia y, aunque hoy en día ya no corras el riesgo de morir devorado por un tigre, no puedes hacer nada para evitarlo.

Frente esta situación, tu mente empieza a preparase para lo peor, identificando cualquier señal a tu alrededor como una posible amenaza.

Como tu cuerpo ha empezado a vivir bajo peligro constante, se crea una espada de doble filo. Porque lejos de motivarte a a salir, explorar y conocer gente nueva, el miedo provoca todo lo contrario.

Círculo de la soledad

Esta situación genera un estado similar a la depresión, hasta el punto en que puedes llegar a interpretar la soledad como dolor físico real (Matthews et al. 2016, Eisensberger et al. 2003).

Por si todo esto fuera poco, nuestra educación también ha reforzado estas creencias irracionales, por ejemplo dando por sentado que a cierta edad ya tenemos que habernos casado o formado una familia. De lo contrario parece que seamos bichos raros, y eso todavía añade más presión.

Pero recuerda: este círculo vicioso está solo en tu cabeza. Es un vestigio prehistórico que carece de sentido hoy en día. Cuanto más consciente seas de esto, antes podrás dejar de vivir la soledad como si fuera depresión.

La verdadera relación entre soledad y felicidad
Cuando terminé de estudiar mi carrera tuve la suerte de encontrar trabajo casi de inmediato. Se trataba de una buena oportunidad con grandes posibilidades de crecimiento.

Era joven y tenía ganas de comerme el mundo, y volqué todos mis esfuerzos en mi vida profesional. Me pasaba más de 12 horas diarias en la oficina y trabajaba la mayoría de fines de semana. Incluso la noche que cumplí 23 años elegí quedarme trabajando en casa de mi jefe para terminar un proyecto.

Un año después me había quedado completamente solo. Y fue una de las etapas más duras de mi vida.

Sin pareja ni amigos.

Me había olvidado de cultivar mis relaciones. Creí que mis amigos seguirían contando siempre conmigo, o que con mandarles de vez en cuando un mensaje ya sería suficiente.

Pero no es lo mismo.

¿Recuerdas la cantidad de amigos que tenías de pequeño? Durante la adolescencia las relaciones sociales ocupan el primer puesto en nuestra escala de valores, pero al hacernos adultos cuestiones como la carrera laboral o cuidar los hijos las relegan a un segundo plano.

Amigos íntimos edad

Eso es exactamente lo que me había pasado. Se me olvidó por completo que lo que más influye sobre nuestra felicidad son las relaciones sociales. Por mucho dinero, trabajo o fama que tengas, si te sientes solo seguirás siendo infeliz (Waldinger, 2002).

Y las redes sociales, en las que yo me había refugiado, no sirven. Miles de años de evolución nos han programado para las relaciones cara a cara, no para interactuar mediante mensajes de texto. Por eso las personas que dedican más de dos horas diarias a las redes sociales tienen el doble de posibilidades de sentirse solas (Primack et al. 2017).

Eso sin contar que ser espectadores de las vidas aparentemente felices de los demás nos hace sentir más desgraciados todavía, tal y como demostró un estudio (Kross et al. 2013).

En realidad no estás tan solo como crees
Sí, aunque sigamos colgando fotos sonrientes en el muro de Facebook, todos nos hemos sentido solos en algún momento de nuestra vida.

Se calcula que 1 de cada 10 personas se siente sola, y ese porcentaje aumenta hasta 1 de cada 3 en los mayores de 60 años (Griffin, 2010).

Incluso hay varios expertos que advierten que la próxima epidemia mundial es la soledad.

Personas sienten solas

Aunque sientas que todos los astros del universo se han conjurado contra ti y que nunca encontrarás alguien que te quiera o entienda, nadie escapa de sentirse solo. Nadie. De hecho, siempre recordaré la confesión que me hizo uno de mis mejores amigos cuando íbamos al instituto.

Él era el típico chico popular. Era divertido, valiente y siempre estaba rodeado de amigos, y todos nos moríamos de ganas de formar parte de su pandilla.

Pero una noche en la que bebió demasiado me reveló que a veces se sentía insoportablemente solo.

Me dijo que no se atrevía a explicarlo por miedo a romper su imagen carismática, pero que sentía que nadie le podía comprender, y que no sabía qué quería hacer en esta vida.

Ese día aprendí que el interior de las personas esconde muchas sorpresas. Y que puedes estar muy cerca de la gente, pero sentirte muy lejos.

Sentirte solo no es lo mismo que estar solo
Porque, en realidad, la soledad puede ser buena. Se ha demostrado que, en ese estado, el cerebro recupera capacidad de atención, motivación, creatividad y productividad.

Sin embargo, sentirse solo es otra historia. A largo plazo afecta tu salud mental, provoca depresión y supone mayor riesgo de mortalidad que la obesidad (Holt-Lundstad et al. 2015).

Entonces, ¿cuál es la diferencia entre estar solo y sentirte solo y deprimido?

La primera respuesta está en tus expectativas. En la distancia entre tus relaciones sociales reales y las que te gustaría tener. Si te gustaría poder compartir tus pensamientos con alguien pero no tienes nadie con quien hacerlo, te sentirás solo.

La segunda respuesta es cómo te sientes respecto a lo que sientes.

Dicho de otra forma, lo verdaderamente importante no es sentirte solo, sino cómo te sientes respecto a sentirte solo.

Lo importante no es cómo te sientes, sino cómo te sientes respecto lo que sientes.
HAZ CLICK PARA TWITTEAR
Puede costar de entender, pero si cuando te sientes solo lo interpretas como algo terrible, probablemente te deprimas. Si por el contrario lo interpretas como una oportunidad para reflexionar y conocerte mejor, probablemente no te afecte tanto.

No puedes evitar sentirte solo, especialmente si tus relaciones sociales no son las que te gustarían. Pero si te pasas el día diciéndote que eso es algo espantoso y que toda tu vida será horrible, caerás en la tristeza y depresión, sin poder salir de ese círculo vicioso.

Por fortuna, todas estas emociones negativas están provocadas por pensamientos. Y esto es una gran noticia, porque significa que tienes poder para cambiarlas.

5 señales de que tienes miedo a estar solo
El miedo a la soledad es tan fuerte que nos hace sentir que incapaces de valernos por nosotros mismos en este mundo. Que necesitamos tener alguien a nuestro lado para tirar adelante.

Lógicamente esto no es cierto, pero la falta de confianza en uno mismo y el miedo a quedarse sola es lo que encadena a mucha gente en relaciones tóxicas, cuando su pareja les hace bastante más daño que bien.

Entonces, si es posible autoengañarse por miedo, ¿qué señales pueden delatar que en el fondo de tu corazón te sientes solo?

La ciencia ha detectado varias, y algunas son sorprendentes.

1. A veces compras compulsivamente
¿Sabes por qué deseas tanto el nuevo iPhone o despilfarras dinero en ropa que luego no te pones?

En un estudio realizado en más de 2.500 voluntarios se comprobó que las personas que se sienten solas intentan llenar su vacío acumulando posesiones materiales (Pieters, 2013).

Aunque ir de compras te pueda subir el ánimo de forma temporal, esa sensación es fugaz. Varios estudios han demostrado comprar cosas no mejora tu felicidad a medio plazo: es mejor gastar el dinero en experiencias.

2. Estás enganchado a las series
¿Adicto a Juego de Tronos? Pues se ha demostrado que existe una correlación entre la sensación de soledad y la tendencia a abusar de las series de televisión (Sung, Kand & Lee, 2015).

Si disfrutas de sesiones maratonianas viendo series, ándate con cuidado. Quizás las estés usando como distracción para no enfrentarte a tus sentimientos reales.

3. Prefieres pasar calor
Resulta que asociamos la calidez de las relaciones sociales con el calor físico. Literalmente.

Un estudio de 2013 descubrió que las personas que se sienten solas acostumbran a darse duchas más largas y con agua más caliente, lo que les ayuda a sentirse mejor (Bargh & Shalev, 2013).

Según parece, no sentimos más aislados cuando tenemos frío, y más acompañados cuando tenemos calor. La razón probablemente tenga algo que ver con la calidez que nos transmitían nuestras primeras experiencias sociales, como los abrazos de nuestros padres o amigos.

4. Tus amigos también se sienten solos
Tus amigos pueden contagiarte un resfriado, ¿pero sabías que también pueden contagiarte su soledad?

Sentirse solo es contagioso, especialmente entre mujeres. De hecho, tienes un 52% más de probabilidades de sentirte solo si algún familiar o amigo íntimo también se siente así. (Cacioppo et al, 2009)

Contagio soledad

¿Por qué? Pues porque la gente deprimida puede comportarse de forma distante contigo, lo que conseguirá que te sientas más solo al haberles perdido.

5. Estás más irascible de lo normal
¿Últimamente estás de los nervios? ¿No soportas quedarte atrapado en los atascos o te irrita la antipatía de algunas personas?

Si es tu caso, quizás no sea cuestión de una mala racha. Quizás sea culpa de la soledad.

Sentirte solo te pone en modo de alerta frente nuevas amenazas. Por eso ciertos comportamientos te provocan tanto estrés (Cacioppo, Hawkley & Bertnson 2003).

¿Qué hacer cuando te sientes solo? 10 claves psicológicas
Si te sientes terriblemente solo de forma habitual, deja de compadecerte y empezar tomar cartas en el asunto.

Para superar la soledad definitivamente evita buscar consuelo por Internet, donde es fácil quedarse enganchado. En su lugar, debes aprender a cambiar tus perspectivas, mejorar tus habilidades sociales y ampliar tu círculo social. De lo contrario estarás dejando la puerta abierta a que la soledad vuelva otra vez (Masi et al. 2010).

A continuación encontrarás 10 estrategias psicológicas que te ayudarán a aceptar la soledad, mejorar tu ánimo y conectar con la gente.

1. Identifica la causa de tus sentimientos
¿Verdad que no te tomarías un medicamento antes de saber cuál es tu enfermedad?

Pues el primer error de la mayoría de gente que se siente sola es buscar la solución antes de dar con el problema.

Piensa en lo que significa para ti sentirte solo e intenta descubrir su causa. ¡Pero cuidado! La causa no es “Me siento solo porque no tengo pareja”. No. La causa es por qué no tener pareja te hace sentir solo.

Quizás sea porque crees que a tu edad ya deberías estar casado y eso te haga sentir fracasado, o porque te valoras poco y piensas que nadie será capaz de amarte jamás. Para encontrar el origen, simplemente hazte dos veces la pregunta ¿Por qué?

—Me siento solo. 

—¿Por qué te sientes solo?

—Porque no tengo amigos en quien apoyarme.

—¿Por qué no tener amigos en quien apoyarte te hace sentir solo?

Es difícil ser dolorosamente honesto con uno mismo, pero tener claro el motivo es fundamental para encontrar una dirección.

2. Acepta tus sentimientos y no luches contra ellos
Una vez ya tienes claro el origen de tu soledad, es el momento de reconciliarte con ella.

Te sientes solo y deprimido cuando interpretas pensamientos como “no tengo amigos”, “no puedo sincerarme con mi marido” o “no le importo a nadie” como algo horrible. Por lo tanto, la solución es no juzgarlos ni luchar contra ellos cuando te vuelvan a invadir, .

El motivo es que cuanto más te resistes a un pensamiento, más fuerte se hace. Es como intentar no pensar en un oso polar blanco: irremediablemente terminas pensando en ese maldito oso polar blanco (Wegner et al. 1987).

Pensamientos negativos

Sin embargo, cuanto más espacio le des a tus pensamientos negativos para existir, más rápidamente se marcharán. Porque dejarás de interpretarlos como una amenaza contra la que tienes que luchar.

Simplemente acéptalos y reconoce cómo te sientes: “Pensar que no tengo pareja me hace sentir solo”. Y ya está. Incluso puedes tratarlo como un amigo pesado que te está haciendo una visita sorpresa.

“Hola soledad, veo que has vuelto a visitarme” —y acógelo con resignación hasta que se marche.

3. Cuéntale a alguien cómo te sientes
La siguiente manera de aliviar tu soledad es contarle a alguien cómo te sientes. No en foros de Internet, sino cara a cara.

Piensa en algún amigo que te haya dado apoyo en el pasado o que simplemente estés a gusto con él y llámale. Puede ser difícil hacerlo cuando lleváis tiempo sin hablar, pero hazlo.

Quizás creas que se reirá, te compadecerá o le quitará importancia. Pero te aseguro que no va a ser así. Lo más probable es que empatice contigo, porque todo el mundo se ha sentido solo y perdido alguna vez.

Sincerarte con alguien y mostrarle tus verdaderos sentimientos os unirá más. Lo único que levanta sospechas y genera distanciamiento es intentar ocultar lo que sientes. (Sprecher, Treger & Wondra 2012)

4. Medita durante 15 minutos al día
Un estudio de 2012 descubrió que la meditación puede reducir los efectos perjudiciales de la soledad (Creswell et al. 2012).

En concreto, meditar 15 minutos al día durante 8 semanas redujo los pensamientos negativos asociados a la soledad en un 18% comparado con el grupo control.

Meditar soledad

Aprender a meditar no es difícil. No es necesario que leas ningún libro ni te apuntes a cursos. Solo tienes que entrenar tu mente para centrarse en el presente sin vagar entre el pasado y el futuro.

Simplemente ponte cómodo, cierra los ojos, y céntrate en tu respiración. Si empiezas a pensar en otra cosa, devuelve tu atención a la respiración, sin juzgar si lo has hecho bien o mal.

Y ya está. No es posible fracasar con la meditación, tan solo practícala y tu mente empezará a crear una nueva relación con la soledad. Una relación que te permitirá observarla sin miedo, de forma pacífica y tranquila.

5. Deja de leer autoayuda ahora mismo
Una vez leí una reflexión en el blog de la psicóloga Marina Díaz que me pareció muy acertada.

Según la psicología popular, cuando te sientes solo o deprimido es porque tienes baja autoestima.

En ese caso, lo que debes hacer es intentar aumentarla, ¿verdad?

Muchos creen eso. Y entonces empiezan a leer y leer libros de autoayuda para aprender a conocerse y quererse más.

Pero esta estrategia tiene un gran problema.

Imagínate que tu autoestima es un diamante. Lo guardas encima de una bandeja en tu casa, y lógicamente quieres que esté limpio y brillante.

Sin embargo en tu casa hay polvo. Cuando no es por culpa del viento es porque alguien entra con los pies sucios.

Como el diamante se ensucia constantemente, tú te dedicas obsesivamente a limpiarlo. Te pasas horas sacándole brillo, pero cuando te despistas le vuelven a caer motas de polvo encima.

Sin embargo, tu mente te dice que debes seguir limpiando el diamante, porque si está limpio entonces te sentirás bien, encontrarás amigos y solucionarás todos tus problemas.

Pero como lo único que haces es limpiar el diamante, no te queda tiempo para hacer amigos nuevos o hablar de tus problemas en pareja.

Tienes que elegir. O sales a vivir la vida y asumes que el diamante a veces va a estar sucio, o te quedas en casa limpiándolo.

Ese diamante es tu autoestima. Porque creemos que no somos capaces de hacer nada si no la tenemos siempre perfecta. Y por eso no hacemos nada.

“Necesito autoestima para no sentirme solo”. “Con más autoestima me respetarían más”. “Si tuviera autoestima no me afectaría lo que pensaran de mí”. Y un largo etcétera.

¿Te ha servido de algo dedicar todo ese  tiempo a limpiar el diamante? ¿No crees que te iría mejor si no te preocupase tanto mantenerlo impoluto y te dedicaras a hacer algo importante para ti?

6. Haz 30 minutos de ejercicio
Mente y cuerpo van unidos. Lo que le pasa a uno tiene consecuencias sobre el otro, y al revés.

La soledad también tiene efectos negativos sobre tu salud física. Pero solo 30 minutos de ejercicio durante tres días a la semana son suficientes para cambiar ese estado y empezar a recuperarte (Bartholomew, Morrison & Ciccolo, 2005)

Ejercicio soledad

No menosprecies la importancia que tiene el deporte sobre tu estado anímico. El ejercicio dispara tus pensamientos positivos al generar endorfinas (conocidas como las hormonas del bienestar), aumenta tu ritmo metabólico y te ayuda a sentirte más a gusto con tu propia imagen.

Si no haces deporte, olvídate de las otras nueve claves y empieza por aquí. El ejercicio quizás no elimine la causa de tu soledad, pero aliviará tus síntomas.

7. Conecta con gente a través de MeetUps
Relacionarte con gente te enseña que no estás tan solo en el universo. Te conecta con este mundo y te hace sentir parte de él, con sus mismos problemas e ilusiones.

¿Pero qué ocurre cuando no tienes amigos cerca? ¿Cómo puedes conocer gente nueva?

Te presento MeetUp.

MeetUp es una web donde se anuncian eventos y quedadas (las hay para ir en bicicleta o comentar libros, por ejemplo), y donde acostumbra a ir mucha gente sola.

Sé que no es fácil ir solo a un evento. La soledad puede aumentar tu ansiedad en situaciones sociales, así que te recomiendo una estrategia psicológica que suele funcionar bien: plantearte la situación como un juego poniéndote en la piel de otra persona. (Knowles et al. 2015)

Por ejemplo, podrías imaginarte que eres un relaciones públicas. ¿Cómo lo harías para saber si la gente del evento se lo está pasando bien?

8. Haz algo por los demás (aunque sea pequeño)
¿Sabías que cuando donas a la caridad se activa la misma región cerebral que cuando comes chocolate o tienes sexo? (Moll et al, 2006)

Dar te hará sentir mejor. En un estudio que sorprendería a muchos economistas, los participantes se dividieron aleatoriamente en 4 grupos.

Al primero se le dio 5 dólares a cada uno para que compraran algo para ellos. Al segundo se le dio 20 dólares para que hicieran lo mismo.
En el tercero, tenían que gastar los 5 dólares en comprar algo para otra persona, y en el último lo mismo con 20.
Los que gastaron 5 y 20 dólares en los demás terminaron sintiéndose mucho más felices y satisfechos que los que gastaron el dinero en ellos mismos. Pero lo que es más sorprendente es que los que regalaron 20 dólares no se sintieron mejor que los de 5 (Dunn, Aknin & Norton, 2008).

Dicho de otra forma, no es una cuestión de cuánto dar, sino simplemente dar.

Ayudar felicidad

Una de las mejores maneras de aliviar la soledad y dejar de pensar en ella es hacer algo por los demás. Únete a una ONG o dedica dos días al mes a hacerle compañía a una persona anciana; es muy difícil sentirte solo cuando estás ayudando a los pobres o los más necesitados. Y además te recompensa con inmensa gratitud.

9. Viaja solo para no sentirte solo
Cuanto más solo viajes, más acompañado vas a estar.

Es una paradoja, pero es así. Mucha gente no se atreve a viajar sola por varios miedos, especialmente el de no poder soportar la soledad. Pero la realidad es que van a estar solos muy poco tiempo.

Viajar en compañía puede ser mucho más solitario que viajar por tu cuenta. Te obliga a tener que relacionarte constantemente con tus compañeros para que no parezca que los estás dejando de lado. En estos casos es muy frecuente volver de viaje sin haber conocido a nadie.

Cuando viajas solo, la gente está más predispuesta a hablar contigo. Dejas de ser un grupo cerrado, con normas propias, y te conviertes en un viajero curioso. Sin darte cuenta, empezarás a conocer gente con historias sorprendentes, y eso te conectará de nuevo con el mundo.

Personalmente, en pocas ocasiones he pasado más de dos días sin compañía cuando he viajado solo. Si te alojas en hostales encontrarás un montón de gente (jóvenes y mayores) en tu misma situación, y en cuestión de minutos ya estarás haciendo nuevas amistades.

10. Adopta un perro
Si últimamente te sientes triste y deprimido quizás pienses que ahora no puedes sobrellevar más responsabilidades en tu vida. ¡Sólo te faltaría tener un perro!

Permíteme que discrepe rotundamente.

Yo no había mostrado ningún interés por estos seres peludos durante toda mi vida. Algunos me parecían bonitos, pero tener que pasearlos 3 veces al día se me antojaba una esclavitud excesiva.

Sin embargo hace poco he empezado a ver las ventajas que eso conlleva. Voy a citarte algunas:

Te obliga a moverte

Tener un perro supone seguir una rutina. Ya no puedes quedarte deprimido en la cama hasta las 12 de la mañana; tienes que levantarte para sacarlo a la calle y darle de comer.

Un perro añadirá rutina a tu vida. Y en los peores momentos, eso puede ser el primer paso hacia la recuperación.

Te ayuda a conocer gente

Los dueños de perros inician muchas más conversaciones entre ellos, así que aprovéchalo para conocer gente cuando sales a pasear tu mascota (Rogers, Hart & Boltz, 1993).

El motivo es que tener algo en común con otras personas nos vincula más a ellas y nos predispone para relacionarnos socialmente.

Te levanta el ánimo

Por si todo esto fuera poco, el simple hecho de acariciar tu perro durante 20 minutos es suficiente para aumentar en un 10% tus niveles de serotonina, conocida como la hormona de la felicidad (Beetz et al. 2012).

Mascota felicidad

Si te sientes solo, tener un perro no solo evitará que te abandones, sino que te abrirá las puertas a conocer más gente y a ver las cosas con más optimismo. Y si además lo adoptas estarás salvando una vida.

Conclusión: aprende a estar solo
En esta guía te he mostrado las principales estrategias científicas para reducir el terrible efecto de la soledad.

Sin embargo, recuerda que es normal que te sientas solo de vez en cuando. A todos nos ocurre.

Incluso aquellas personas que consideras más sociables o extrovertidas han pasado por la soledad. En algún momento u otro, todos nos hemos sentido (o nos sentiremos) incomprendidos, perdidos e ignorados.

No rechaces la soledad. No tienes que estar permanentemente contento y feliz, ni portarte como un valiente o ser el que siempre consuela a los demás. Tú también tienes derecho a sentirte triste de vez en cuando, porque esa reflexión te ayudará volver a coger impulso.

Sin embargo, no dejes que esta sensación se prolongue demasiado. De lo contrario, la depresión puede empezar a asomar la cabeza.

Para conseguirlo, aprende a luchar sin resistirte. Sentirte solo es un sentimiento, y no hay ningún sentimiento que dure para siempre. Si le dejas marchar en lugar de enfrentarte a él como si fuera a quedarse eternamente, terminará yéndose.

Una vez aprendas a convivir pacíficamente con la soledad, pon la primera piedra para que no tenga que regresar. Sal, haz ejercicio, crea rutinas y conecta con gente nueva. Descubrirás que tu círculo de soledad es tan pequeño como tú quieres que sea.""")

def opciones():
  print("\n0 -> Nunca")
  print("1 -> Varios dias")
  print("2 -> Mas de la mitad de los dias")
  print("3 -> Casi cada dia")

def tablaResultados(resultado, nombre):
  print(f"\n-> RESULTADOS: {resultado} <-\n")
  print("Menor a 13 -> No eres depresivo")
  print("Menor a 26 -> Eres un poco depresivo")
  print("Menor a 39 -> Eres medianamente depresivo")
  print("Mayor a 39 -> Eres depresivo\n")
  if resultado <= 13:
    print(f"{nombre} no eres depresivo")
    #Le aumentan mas cosas.. nose q mas equisde
  if resultado <= 26 and resultado >= 13 :
    print(f"{nombre} eres un poco depresivo")
    #Le aumentan mas cosas.. nose q mas equisde x2
  if resultado <= 39 and resultado >= 26 :
    print(f"{nombre} eres medianamente depresivo")
    #Le aumentan mas cosas.. nose q mas equisde x3
  if resultado > 39:
    print(f"{nombre} eres depresivo")
    #Le aumentan mas cosas.. nose q mas equisde x4

def diario():
    veces = 0
    entrada = {'nombre':[],'fecha':[],'animo':[]}
    while True:
        print("          Diario          \n__________________________")
        print("[1] Crear entrada\n[2] Ver entradas previas\n[3] Ver promedio de ánimo\n[0] terminar")
        try:
            p = int(input("Qué desea hacer?\n"))
        except:
            print("Entrada invalida.")
        if p >= 0 and p < 4 and (type(p) is int):
            if p == 1:
                crearE(veces, entrada)
                veces += 1
            elif p == 2:
                verE(entrada)
            elif p == 3:
                print(prom(entrada))
            elif p == 0:
                break
            else:
                print("Ingrese una opción válida")


        



def crearE(x:int, entrada : {}):
    entrada['nombre'].append(input("Ingrese su nombre completo:\n"))
    entrada['fecha'].append(datetime.datetime.now())
    entrada['animo'].append(int(input("Del 1 al 10 ¿Cómo se siente hoy?\n")))



def verE(entrada : {}):
    n, f, a, s = entrada['nombre'], entrada['fecha'], entrada['animo'], ""
    for i in range(len(n)):
        s = "Nombre: " + n[i] + " Fecha: "+ str(f[i]) + " Nivel de ánimo: " + str(a[i])
        print(s)
        
    
def prom(entrada) :
    ac = 0
    if len(entrada['animo']) > 0:
        for i in entrada['animo']:
            ac += i
        ac = ac / len(entrada['animo'])
        return "El promedio de sus entradas de ánimo es " + str(ac)
    else:
        return("No hay registros")
    
def teleDiagnostico():
  print("TEST PARA DEPRESION\n")
  nombre = input("Digita tu nombre: ")
  preguntas = ["Poco interés o alegría por hacer cosas",
               "Sensación de estar decaído/a, deprimido/a o desesperanzado/a",
               "Problemas para quedarse dormido/a, seguir durmiendo o dormir demasiado",
               "Sensación de cansancio o de tener poca energía",
               "Poco apetito o comer demasiado",
               "Sentirse mal consigo mismo/a; sentir que es un/a fracasado/a; o que ha decepcionado a su familia o a sí mismo/a",
               "Problemas para concentrarse en algo, como leer el periódico o ver televisión",
               "Moverse o hablar tan despacio que los demás pueden haberlo notado. O lo contrario, estar tan inquieto/a o agitado/a que se ha estado moviendo de un lado a otro más de lo habitual",
               "Pensamientos de que estaría mejor muerto/a o de querer hacerse daño de algún modo"]
  inicio = 0
  resultado = 0 #Mayor posible -> 54
  while inicio <= 8:
    print(f"\nPregunta {inicio + 1}: {preguntas[inicio]}")
    opcionPregunta = None
    opciones()
    while True:
      try:
        opcionPregunta = int(input("\nDigite el numero deseado: "))
      except ValueError:
        print("\nSolo se recibe numeros enteros")
      else:
        if opcionPregunta <= 3 and opcionPregunta >= 0:
          if opcionPregunta == 0: #NUNCA
            resultado += 0
          if opcionPregunta == 1: #VARIOS DIAS
            resultado += 1
          if opcionPregunta == 2: #MAS DE LA MITAD DE LOS DIAS
            resultado += 3
          if opcionPregunta == 3: #CASI CADA DIA
            resultado += 6
          break
        else:
          print("Numero invalido")
          print("Por favor digitelo nuevamente")
    inicio += 1
  tablaResultados(resultado, nombre)
def premium():
  link = "paypal.me/acostalopez"
  dinero = "$40 USD"
  while True:
    emailVerificado = None
    email = input("\nDigita tu email de PayPal: ")
    print("\nVerificando correo...")
    emailVerificado = validate_email(email)
    if emailVerificado is True:
      print("Email valido\n")
      break
    else:
      print("Email invalido\n")
  print(f"Envia {dinero} a {link}.\n")
  print("Pronto verificaremos el pago y con ello")
  print("Te enviaremos a tu correo la contraseña del plan premium")
  exit()

def gratis():
  print("\n1. Tips")
  print("2. Tele Diagnostico")
  print("3. Diario")
  print("0. Salir.")
 
  
def elegirTip():
  while True:
    mostrarTips()
    opcionElegirTip = None
    while True:
      try:
        opcionElegirTip = int(input("\nDigite el numero deseado: "))
      except ValueError:
        print("\nSolo se recibe numeros enteros")
      else:
        if opcionElegirTip <= 6 and opcionElegirTip >= 0:
          break
        else:
          print("Numero invalido")
          print("Por favor digitelo nuevamente")
    if opcionElegirTip == 1:
      dormirMejor()
    if opcionElegirTip == 2:
      sentirMejor()
    if opcionElegirTip == 3:
      sentirMejorCuarentena()
    if opcionElegirTip == 4:
      superarDepresion()
    if opcionElegirTip == 5:
      sentirseSolo()
    if opcionElegirTip == 6:
      premium()
    if opcionElegirTip == 0:
      break
  
def preguntarNumero(inicio, final, recuadro):
  while True:
    try:
      opcion = int(input(f"\nDigite el numero deseado {recuadro}: "))
      print("")
    except ValueError:
      print("\nSolo se recibe numeros enteros")
    else:
      if opcion >= inicio and opcion <= final:
        return opcion
      else:
        print("Numero invalido")
        print("Por favor digitelo nuevamente")
        
def enviarEmail(email, asunto):
  mensaje = MIMEMultipart("plain")
  mensaje["From"] = "medineerscolombia@gmail.com"
  mensaje["To"] = email
  mensaje["Subject"] = asunto
  adjunto = MIMEBase("application", "octect-stream")
  adjunto.set_payload(open("respuestaEncuesta.xlsx", "rb").read())
  encoders.encode_base64(adjunto)
  adjunto.add_header("content-Disposition", 'attachment; filename="respuestaEncuesta.xlsx"')
  mensaje.attach(adjunto)
  smtp = SMTP("smtp.gmail.com")
  smtp.starttls()
  smtp.login("medineerscolombia@gmail.com", "Medineers69XD")
  smtp.sendmail("medineerscolombia@gmail.com", email, mensaje.as_string())
  print("Correo Enviado Exitosamente")
  smtp.quit()
  
def nuevoUsuario():
  while True: 
    usuario = input("Digite su usuario: ")
    if len(usuario) > 5:
      break
    else:
      print("El usuario debe tener al menos mas de 5 caracteres")
  password = None
  mayuscula = 0
  minuscula = 0
  numero = 0
  espacio = 0
  while True:
    password = input("Digite su contraseña: ")
    if len(password) < 8:
      print("La contraseña debe tener al menos mas de 8 caracteres")
    else:
      for contenido in password:
        if contenido.islower() == True:
          minuscula += 1
        elif contenido.isupper() == True:
          mayuscula += 1
        elif contenido.isdigit() == True:
          numero += 1
        else:
          if contenido.isspace() == True:
            espacio += 1
      if minuscula >= 1:
        if mayuscula >= 1:
          if numero >= 1:
            if espacio >= 1:
              print("La contraseña no puede tener espacios en blanco")
            else:
              break
          else:
            print("La contraseña debe tener como minimo un caracter numerico")
        else:
          print("La contraseña debe tener como minimo un caracter en mayuscula")
      else:
        print("La contraseña debe tener como minimo un caracter en minuscula")
  if path.exists("usuarios"):
    ()
  else:
    os.mkdir("usuarios")
  archivo = open(f"usuarios/{usuario}", "w")
  archivo.write(usuario + "\n")
  archivo.write(password)
  archivo.close()  

def loguearse(usuario, password):
  if path.exists("usuarios"):
    ()
  else:
    os.mkdir("usuarios")
  listaArchivos = os.listdir("usuarios")
  if len(listaArchivos) > 0:
    if usuario in listaArchivos:
      archivo = open(f"usuarios/{usuario}", "r")
      verificacion = archivo.read().splitlines()
      if password in verificacion:
        print("\nTe has logueado con exito")
        return True
      else:
        print("\nContraseña incorrecta")
    else:
      print("\nUsuario incorrecto")
  else:
    print("\nNo hay usuarios en la base de datos")
    
def bienvenida():
  print("—————— SOFTWARE BY MEDINEERS ——————")
  print("")
  print("——————————— Bienvenid@ ————————————")
  print("——————————————— a —————————————————")
  print("——————————— Psycho 19 —————————————")

def cliente_o_empleado():
  print("\n1. Cliente")
  print("2. Empleado")
  print("0. Salir")
  
def gratis_o_premium():
  print("1. Version gratis")
  print("2. Version premium")
  print("0. Salir")  

def menuPrincipal():
  print("\n1. Iniciar sesion")
  print("2. Registrarse")
  print("0. Salir.")
  
def menu():
  print("\n1. Registrar paciente")
  print("2. Buscar paciente")
  print("3. Borrar paciente")
  print("4. Ver total pacientes")
  print("5. Borrar datos")
  print("0. Salir")

bienvenida()
SERVER_PASSWORD = "UserMedineers69" #tambien se pude hacer generando contraseña aleatoria y q se la envie al correo y la digite
PREMIUM_PASSWORD = ["asu98bp[gd.<:>?>;'[['[;]',", "AUIHYGVaksii2894537", "ALoPExxnujofgb25}{}{}#(&*^$(", "AHVZTC@648^&*@%#!(H", "WASDwasd123321!@#$%^&*()_++_)(*&^%$#@!"]
opcionPrincipal = None
while True:
  menuPrincipal()
  while True:
    try:
      opcionPrincipal = int(input("\nDigite el numero deseado [0,1,2]: "))
      print("")
    except ValueError:
      print("\nSolo se recibe numeros enteros")
    else:
      if opcionPrincipal >=0 and opcionPrincipal <= 2:
        break
      else:
        print("Numero invalido")
        print("Por favor digitelo nuevamente")
  if opcionPrincipal == 1:
    usuario = input("Digite su usuario: ")
    password = input("Digite su contraseña: ")
    if loguearse(usuario, password) is True:
      break
  if opcionPrincipal == 2:
    nuevoUsuario()
  if opcionPrincipal == 0:
    exit()
opcionCE = None
while True:
  cliente_o_empleado()
  try:
    opcionCE = int(input("\nDigite el numero deseado [0,1,2]: "))
    print("")
  except ValueError:
    print("\nSolo se recibe numeros enteros")
  else:
    if opcionCE >=0 and opcionCE <= 2:
      break
    else:
      print("Numero invalido")
      print("Por favor digitelo nuevamente")
if opcionCE == 1:
  gratis_o_premium()
  opcionGP = preguntarNumero( 0, 2, "[0,1,2]")
  if opcionGP == 1:
    print("___ VERSION GRATIS ___")
    while True:
      gratis()
      opcionGratis = preguntarNumero( 0, 3, "[0,1,2]")  
      if opcionGratis == 1:
        elegirTip()
      if opcionGratis == 2:
        teleDiagnostico()
      if opcionGratis == 3:
        diario()
      if opcionGratis == 0:
        break  
  if opcionGP == 2:
    while True:
      premiumPassword = input("Digite la contraseña del servidor: ")
      if premiumPassword in PREMIUM_PASSWORD:
        break
      elif intentos == 3:
        print("Contraseña incorrecta")
      elif intentos == 2:
        print("Contraseña incorrecta")
        print("El programa se cerrara la proxima vez que se equivoque")
      elif intentos == 1:
        exit()
      intentos -= 1
      print(f"Intentos restastes: {intentos}\n") 
    print("___ VERSION PREMIUM ___")
    nombre = input("Digita tu nombre completo: ")
    while True:
      emailVerificado = None
      email = input("Digita tu email: ")
      print("\nVerificando correo...")
      emailVerificado = validate_email(email)
      if emailVerificado is True:
        print("Email valido\n")
        break
      else:
        print("Email invalido\n")
    print("Acontinuacion te haremos 5 preguntas...\n")
    print("Por favor te pedimos contestarlas honestamente")
    print("Para que uno de nuestros asesores se ponga en")
    print("Contacto contigo via e-mail\n")
    estasSeguro = None
    while True:
      estasSeguro = input("Estas listo? [ Si / No ]: ")
      if estasSeguro == "Si" or estasSeguro == "sI" or estasSeguro == "SI" or estasSeguro == "si":
        break
      elif estasSeguro == "No" or estasSeguro == "nO" or estasSeguro == "NO" or estasSeguro == "no":
        salir = None
        while True:
          salir = input("Deseas salir ? [ Si / No ]: ")
          if salir == "Si" or salir == "sI" or salir == "SI" or salir == "si":
            exit()
          elif salir == "No" or salir == "nO" or salir == "NO" or salir == "no":
            break
          else:
            print("Caracter invalido")
            print("Por favor digitelo nuevamente")
      else:
        print("Caracter invalido")
        print("Por favor digitelo nuevamente")
    print("\nComencemos!!!\n")
    bancoPreguntas = ["Como te sientes hoy?", "Estas aburrido?", "Te has alimentado bien?", "Te ha afectado no salir?", "Que haces en tu tiempo libre?", "Has hecho deporte?", "Te llevas bien con las personas que viven bajo tu mismo techo?" ]
    bancoRespuestas = {}
    preguntas = []
    respuestas = []
    correoAsesores = ["wembie@javerianacali.edu.co", "juanjorestrepo@javerianacali.edu.co", "jmlopezriani@javerianacali.edu.co" , "danielagomez01@javerianacali.edu.co"]
    correo = correoAsesores[rd.randint(0,len(correoAsesores)-1)] 
    bancoRespuestas['email'] = email
    bancoRespuestas['nombre'] = nombre
    indice = 0  
    while indice < 5:
      preguntaAleatoria = rd.randint(0,len(bancoPreguntas)-1)
      if bancoPreguntas[preguntaAleatoria] not in preguntas:
        respuestaUsuario = input(f"{bancoPreguntas[preguntaAleatoria]}: ")
        preguntas.append(bancoPreguntas[preguntaAleatoria])
        respuestas.append(respuestaUsuario)
        indice += 1
    bancoRespuestas['preguntas'] = preguntas
    bancoRespuestas['respuestas'] = respuestas
    excel = pd.DataFrame(bancoRespuestas, columns = ['email', 'nombre', 'preguntas', 'respuestas'])
    excel.to_excel('respuestaEncuesta.xlsx', sheet_name='respuestaEncuesta')
    print("\nEnviando email...\n")
    enviarEmail(email, f"Formulario de {nombre}")
    print("Tu registro se ha completado con exito!")
    print("Gracias por responder")
    remove("respuestaEncuesta.xlsx")
if opcionCE == 2:
  intentos = 3
  while True:
    premiumPassword = input("Digite la contraseña del servidor: ")
    if serverPassword == SERVER_PASSWORD:
      break
    elif intentos == 3:
      print("Contraseña incorrecta")
    elif intentos == 2:
      print("Contraseña incorrecta")
      print("El programa se cerrara la proxima vez que se equivoque")
    elif intentos == 1:
      exit()
    intentos -= 1
    print(f"Intentos restastes: {intentos}\n")       
  opcion = None
  pacientes = []
  if path.exists("pacientes"):
    archivo = open("pacientes","br")
    pacientes = marshal.load(archivo)
    archivo.close()
  else:
    archivo = open("pacientes","bw")
    marshal.dump(pacientes,archivo)
    archivo.close()
  while opcion != 0:
    menu()
    while True:
      try:
        opcion = int(input("\nDigite el numero deseado [0,1,2,3,4,5]: "))
        print("")
      except ValueError:
        print("\nSolo se recibe numeros enteros")
      else:
        if opcion >=0 and opcion <= 5:
          break
        else:
          print("Numero invalido")
          print("Por favor digitelo nuevamente")
    if opcion == 1:
      paciente = []
      nombreCompleto = input("Digite su nombre completo: ")
      cedula = None
      encontroCedula = None
      while True:
        try:
          cedula = int(input("Digite su cedula: "))
        except ValueError:
          print("\nSolo se recibe numeros enteros")
        else:
          for i in range(len(pacientes)):
            if pacientes[i][0] == cedula:
              print(f"La cedula {cedula} ya esta registrada")
              encontroCedula = 1
              break
          if encontroCedula is None:
            break
      print(f"\nEl paciente {nombreCompleto}")
      print("Ha sido registrado con exito!")
      paciente.append(cedula)
      paciente.append(nombreCompleto)
      pacientes.append(paciente)
      archivo = open("pacientes","bw")
      marshal.dump(pacientes,archivo)
      archivo.close()
    if opcion == 2:
      if len(pacientes) > 0:
        cedula = None
        while True:
          try:
            cedula = int(input("Digite la cedula a buscar : "))
          except ValueError:
            print("\nSolo se recibe numeros enteros")
          else:
            break
        encontroCedula = None
        for i in range(len(pacientes)):
          if pacientes[i][0] == cedula:
            print(f"El nombre del paciente es: {pacientes[i][1]}")
            encontroCedula = 1
            break
        if encontroCedula is None:
          print("No se ha encontrado la cedula")
      else:
        print("No hay ningun paciente registrado")
    if opcion == 3:
      if len(pacientes) > 0:
        cedula = None
        while True:
          try:
            cedula = int(input("Digite la cedula a borrar : "))
          except ValueError:
            print("\nSolo se recibe numeros enteros")
          else:
            break
        encontroCedula = None
        for i in range(len(pacientes.copy())):
          if pacientes[i][0] == cedula:
            print(f"El paciente {pacientes[i][1]} con cedula {pacientes[i][0]}")
            print("Ha sido borrado con exito!")
            pacientes.pop(i)
            encontroCedula = 1
            break
        if encontroCedula is None:
          print("No se ha encontrado la cedula")
      else:
        print("No hay ningun paciente registrado")
    if opcion == 4:
      if len(pacientes) > 0:
        pacientes.sort()
        print("——— Pacientes ———\n")
        print(f"Total: {len(pacientes)}")
        for i in range(len(pacientes)):
          print(f"{i+1}. Nombre: {pacientes[i][1]} | Cedula: {pacientes[i][0]}")
          #print(f"Problemas: {pacientes[i][2]}")
        print("")
      else:
        print("No hay ningun paciente registrado")
    if opcion == 5:
      if len(pacientes) > 0:
        borrarDatos = None
        while True:
          borrarDatos = input("Estas seguro de borrar todos los datos? [ Si / No ]: ")
          if borrarDatos == "Si" or borrarDatos == "sI" or borrarDatos == "SI" or borrarDatos == "si":
            remove("pacientes")
            break
          elif borrarDatos == "No" or borrarDatos == "nO" or borrarDatos == "NO" or borrarDatos == "no":
            break
          else:
            print("Caracter invalido")
            print("Por favor digitelo nuevamente")
      else:
        print("No hay ningun dato para borrar")
if opcionCE == 0:
  exit()
