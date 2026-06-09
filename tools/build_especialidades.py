# -*- coding: utf-8 -*-
"""
Generador de páginas de especialidad para MIT Medical Tower.
Toma los datos de SPECS + una plantilla y escribe /especialidades/<slug>.html
Ejecutar:  python tools/build_especialidades.py
Editar contenido aquí y regenerar; el layout (header/footer) vive en js/layout.js
"""
import os
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "especialidades")

WA = "https://wa.me/525528380715"

ICONS = {
 "cardiologia": '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"/>',
 "urologia": '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M12 3.75s6 5.25 6 9.75a6 6 0 11-12 0c0-4.5 6-9.75 6-9.75z"/>',
 "psicologia": '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09z"/>',
 "ginecologia": '<circle cx="12" cy="8" r="4.5" stroke-width="1.6"/><path stroke-linecap="round" stroke-width="1.6" d="M12 12.5V21M9 18h6"/>',
 "traumatologia-ortopedia": '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M7 17l10-10M6.5 4.5a2.12 2.12 0 113 3L7 10 4 7l2.5-2.5zM17.5 19.5a2.12 2.12 0 01-3-3L17 14l3 3-2.5 2.5z"/>',
 "neurologia": '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M15.5 7.5A3.5 3.5 0 0012 4a3.5 3.5 0 00-3.5 3.5M8 9.5A3 3 0 005 12a3 3 0 003 3m8-5.5a3 3 0 013 2.5 3 3 0 01-3 3M12 4v16m0 0a3 3 0 003-3m-3 3a3 3 0 01-3-3"/>',
 "nefrologia": '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M8 4c-2.5 0-4 2-4 5s2 8 4 8 2.5-2 4-2 1.5 2 4 2 4-5 4-8-1.5-5-4-5-3 2-4 2-1.5-2-4-2z"/>',
 "gastroenterologia": '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M9 4v4a4 4 0 004 4h2a3 3 0 013 3v1a4 4 0 01-4 4 5 5 0 01-5-5V9"/>',
 "angiologia": '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M3 12h4l2-7 4 14 2-7h6"/>',
 "otorrinolaringologia": '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M7 9a5 5 0 0110 0c0 3-2 4-3 5s-1 3-3 3a3 3 0 01-3-3"/><circle cx="11.5" cy="9.5" r="1.5" stroke-width="1.6"/>',
 "oncologia": '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M12 21s-1-7 0-10c.7-2.1 3-3 4.5-1.5S17 14 12 21zM12 21s1-7 0-10C11.3 8.9 9 8 7.5 9.5S7 14 12 21z"/>',
 "pediatria": '<circle cx="12" cy="7" r="3.5" stroke-width="1.6"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M6 21a6 6 0 0112 0"/>',
 "dermatologia": '<circle cx="12" cy="12" r="4" stroke-width="1.6"/><path stroke-linecap="round" stroke-width="1.6" d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/>',
 "cirugia-plastica": '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M12 4l1.6 4.4L18 10l-4.4 1.6L12 16l-1.6-4.4L6 10l4.4-1.6L12 4zM18 14l.8 2L21 17l-2.2.9L18 20l-.8-2.1L15 17l2.2-1L18 14z"/>',
 "medicina-interna": '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6" d="M6 4v5a4 4 0 008 0V4M10 17a4 4 0 008 0v-1.5"/><circle cx="18" cy="13.5" r="2" stroke-width="1.6"/>',
}

CHECK = '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"/></svg>'
ICON_BUILDING = '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0H5m14 0h2M5 21H3m6-14h1m4 0h1M9 11h1m4 0h1M9 15h1m4 0h1M12 3v4"/></svg>'
ICON_FACILITY = '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3.75 21h16.5M4.5 3h15M5.25 3v18m13.5-18v18M9 6.75h1.5m-1.5 3h1.5m-1.5 3h1.5m3-6H15m-1.5 3H15m-1.5 3H15M9 21v-3.375c0-.621.504-1.125 1.125-1.125h3.75c.621 0 1.125.504 1.125 1.125V21"/></svg>'
ICON_SPECIALIST = '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.5 20.25a8.25 8.25 0 0115 0"/></svg>'
ICON_BADGE = '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>'
ICON_HEART = '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"/></svg>'

def p(t): return ("p", t)
def h(t): return ("h", t)
def ul(items): return ("ul", items)

SPECS = [
 {"slug":"dermatologia","name":"Dermatología",
  "lead":"El área de Dermatología en MIT Medical Tower cuida de ti con un equipo de especialistas y tecnología médica de vanguardia; la prevención es tu mejor aliada. Un dermatólogo es un médico especialista en el diagnóstico y tratamiento de enfermedades de la piel, el cabello y las uñas.",
  "includes":["Acné","Eczema","Psoriasis","Dermatitis","Cáncer de piel","Envejecimiento prematuro de la piel"],
  "body":[
    p("Contamos con un equipo de dermatólogos altamente calificados y experimentados, junto con tecnología de vanguardia, para ofrecerte la mejor atención integral en el diagnóstico, tratamiento y prevención de enfermedades dermatológicas."),
    p("Brindamos una evaluación completa de tu piel, considerando tu tipo de piel, historial médico, factores de riesgo y estilo de vida. Diseñamos un plan de tratamiento personalizado, utilizando las técnicas más adecuadas para tu caso, ya sean tratamientos tópicos, procedimientos dermatológicos o cambios en tu estilo de vida."),
    p("Te ayudamos a prevenir el desarrollo de enfermedades dermatológicas o a controlarlas de manera efectiva si ya las padeces, y te guiamos en la adopción de hábitos saludables para mantener una piel sana y radiante."),
    p("Contamos con equipos de última tecnología para realizar estudios diagnósticos precisos, como dermatoscopías, biopsias de piel y análisis de laboratorio. Esto nos permite detectar problemas dermatológicos en sus primeras etapas y brindarte un tratamiento oportuno."),
    p("En MIT Medical Tower nos preocupamos por tu bienestar integral. Te ofrecemos un trato cálido y humano, brindándote el apoyo emocional y la orientación que necesitas para afrontar cualquier desafío relacionado con la salud de tu piel."),
  ]},
 {"slug":"pediatria","name":"Pediatría",
  "lead":"El área de Pediatría en MIT Medical Tower cuida del bienestar de tus hijos con un equipo de especialistas y tecnología médica de vanguardia. Un pediatra es un médico que se especializa en la salud y el bienestar de los niños desde el nacimiento hasta la adolescencia.",
  "includes":["Atención prenatal","Parto","Vacunas","Exámenes físicos","Diagnóstico y tratamiento de enfermedades infantiles"],
  "body":[
    p("Nuestro pediatra está a la vanguardia de su campo, actualizado en las últimas técnicas y avances médicos para brindar un diagnóstico preciso, un tratamiento efectivo y un seguimiento personalizado a tus hijos. Se dedica a comprender a fondo el historial médico de tu hijo, sus necesidades específicas y el contexto familiar para diseñar un plan de atención integral que se adapte a su desarrollo y crecimiento."),
    h("Atención en todas las etapas"),
    ul(["Neonatología: cuidado de recién nacidos, prematuros y bebés con condiciones especiales.",
        "Pediatría general: atención preventiva, control de crecimiento y desarrollo, diagnóstico y tratamiento de enfermedades comunes.",
        "Especialidades pediátricas: cardiología, neumología, gastroenterología, endocrinología, neurología, alergología e inmunología pediátrica, entre otras."]),
    h("Servicios integrales para tus hijos"),
    ul(["Consultas pediátricas: evaluación general, control de crecimiento, detección de enfermedades, vacunas y asesoría en nutrición.",
        "Vacunación: aplicación de todas las vacunas del calendario nacional para proteger a tus hijos.",
        "Pruebas de laboratorio y diagnóstico: análisis de sangre, estudios de orina, radiografías y otras pruebas.",
        "Cirugía pediátrica: atención quirúrgica especializada para diversas afecciones.",
        "Urgencias pediátricas: atención inmediata y de calidad ante cualquier emergencia."]),
  ]},
 {"slug":"oncologia","name":"Oncología",
  "lead":"El área de Oncología en MIT Medical Tower diagnostica y da tratamiento al cáncer, incluyendo la oncología médica. Un oncólogo es un médico que se especializa en el diagnóstico y tratamiento del cáncer.",
  "includes":["Quimioterapia","Radioterapia","Inmunoterapia","Cirugía oncológica"],
  "body":[
    p("Contamos con un equipo de oncólogos altamente especializados y experimentados, junto con tecnología de vanguardia, para ofrecerte la mejor atención integral en el diagnóstico, tratamiento y seguimiento del cáncer."),
    p("Nuestros oncólogos están a la vanguardia de su campo, actualizados en las últimas técnicas y avances médicos para brindar un diagnóstico preciso, un tratamiento efectivo y un seguimiento personalizado. Se dedican a comprender a fondo tu historial médico, tipo de cáncer, estadio de la enfermedad y estilo de vida para diseñar un plan de tratamiento integral."),
    h("Atendemos una amplia gama de tipos de cáncer"),
    ul(["Cáncer de pulmón","Cáncer de mama","Cáncer de colon y recto","Cáncer de próstata","Cáncer de piel","Cáncer de sangre (leucemia, linfoma)","Tumores cerebrales","Otros tipos de cáncer"]),
    p("El cáncer es una enfermedad compleja, pero con el diagnóstico y tratamiento adecuados, las posibilidades de curación y supervivencia son cada vez más altas. En MIT Medical Tower estamos aquí para apoyarte y brindarte la mejor atención para enfrentar el cáncer con esperanza y optimismo."),
  ]},
 {"slug":"neurologia","name":"Neurología",
  "lead":"El área de Neurología en MIT Medical Tower previene, diagnostica, trata y rehabilita las enfermedades que involucran al sistema nervioso central, periférico y autónomo. Un neurólogo es un médico que se especializa en el diagnóstico y tratamiento de las enfermedades del sistema nervioso.",
  "includes":["Enfermedades cerebrovasculares","Enfermedades neurodegenerativas","Epilepsia","Esclerosis múltiple","Tumores cerebrales"],
  "body":[
    p("Entendemos la importancia del sistema nervioso para coordinar cada función del cuerpo, desde el pensamiento y el movimiento hasta los sentidos y las emociones. Por eso contamos con un equipo de neurólogos altamente capacitados y con experiencia, apoyados por tecnología avanzada, para brindarte atención integral en el diagnóstico, tratamiento y seguimiento de trastornos neurológicos."),
    p("Realizamos una evaluación neurológica completa que toma en cuenta tu historial clínico, síntomas, estilo de vida y necesidades específicas. Diseñamos un plan de tratamiento personalizado que puede incluir terapia farmacológica, rehabilitación neurológica o intervenciones específicas según tu diagnóstico."),
    h("Procedimientos con tecnología de vanguardia"),
    ul(["Electroencefalograma (EEG): para estudiar la actividad eléctrica del cerebro y detectar trastornos como la epilepsia.",
        "Electromiografía (EMG): para evaluar la salud de los músculos y los nervios que los controlan."]),
    p("La salud neurológica es esencial para una vida plena y funcional. Si presentas dolores de cabeza persistentes, pérdida de memoria, debilidad muscular o cambios en la coordinación, es importante consultar con un especialista."),
  ]},
 {"slug":"otorrinolaringologia","name":"Otorrinolaringología",
  "lead":"El área de Otorrinolaringología en MIT Medical Tower estudia las enfermedades del oído (auditivas y del equilibrio), de las vías respiratorias superiores y parte de las inferiores —nariz, senos paranasales, faringe y laringe—, así como la cirugía relacionada con la glándula tiroides. El otorrino es un médico especializado en el oído, la nariz y la garganta.",
  "includes":["Infecciones del oído","Pérdida auditiva","Tinnitus","Problemas de la nariz","Problemas de la garganta"],
  "body":[
    p("Nuestro otorrinolaringólogo está a la vanguardia de su campo, actualizado en las últimas técnicas y avances médicos para brindar un diagnóstico preciso y un tratamiento efectivo. Se dedica a comprender a fondo tu historial médico, síntomas y estilo de vida para diseñar un plan de tratamiento personalizado."),
    h("Tratamos una amplia gama de padecimientos"),
    ul(["Problemas auditivos: pérdida auditiva, tinnitus, infecciones del oído, enfermedad de Menière.",
        "Problemas nasales: alergias, sinusitis, rinitis, desviaciones del tabique nasal, pólipos nasales.",
        "Problemas de garganta: amigdalitis, faringitis, laringitis, reflujo gastroesofágico.",
        "Trastornos del equilibrio: vértigo, mareos.",
        "Trastornos del sueño: apnea del sueño."]),
    h("Procedimientos con tecnología de última generación"),
    ul(["Audiometrías: para evaluar la audición.",
        "Timpanometrías: para evaluar la función del oído medio.",
        "Nasofibroscopías: para examinar el interior de la nariz y la garganta.",
        "Laringoscopías: para examinar la laringe.",
        "Cirugías otorrinolaringológicas: extracción de amígdalas, cirugía de senos paranasales, timpanoplastia y mastoidectomía."]),
    p("Te ofrecemos un trato cálido y humano, brindándote el apoyo y la orientación que necesitas para afrontar cualquier desafío relacionado con tu salud otorrinolaringológica."),
  ]},
 {"slug":"nefrologia","name":"Nefrología",
  "lead":"El área de Nefrología en MIT Medical Tower se enfoca en los riñones y su estructura. Un nefrólogo es un médico que se especializa en el diagnóstico y tratamiento de las enfermedades del riñón.",
  "includes":["Enfermedad renal crónica","Cálculos renales","Infección del tracto urinario (ITU)"],
  "body":[
    p("Comprendemos la importancia de los riñones para filtrar la sangre, eliminar toxinas y mantener el equilibrio de líquidos y electrolitos en tu cuerpo. Por eso contamos con un equipo de nefrólogos altamente calificados y experimentados, junto con tecnología de vanguardia, para ofrecerte la mejor atención integral en el diagnóstico, tratamiento y prevención de enfermedades renales."),
    p("Brindamos una evaluación nefrológica completa, considerando tu historial médico, síntomas, estilo de vida y necesidades específicas. Diseñamos un plan de tratamiento personalizado, ya sean tratamientos farmacológicos, terapias de reemplazo renal (como diálisis o trasplante renal) o cambios en tu estilo de vida."),
    h("Procedimientos con tecnología de última generación"),
    ul(["Análisis de sangre y orina: para evaluar la función renal y detectar posibles problemas.",
        "Ecografías renales: para evaluar el tamaño, estructura y flujo sanguíneo de los riñones.",
        "Biopsias renales: para obtener una muestra de tejido renal para su análisis.",
        "Cateterismos renales: para drenar la orina o realizar procedimientos diagnósticos.",
        "Fístulas arteriovenosas: para facilitar el acceso a la sangre durante la diálisis."]),
    p("La salud renal es fundamental para mantener una vida sana y activa. Es importante prevenir enfermedades renales y consultar con un especialista si presentas cualquier síntoma o inquietud."),
  ]},
 {"slug":"gastroenterologia","name":"Gastroenterología",
  "lead":"El área de Gastroenterología en MIT Medical Tower cuida tu sistema digestivo con un equipo de especialistas y tecnología médica de vanguardia; la prevención es tu mejor aliada. Un gastroenterólogo es un médico que se especializa en el diagnóstico y tratamiento de las enfermedades del sistema digestivo.",
  "includes":["Enfermedad por reflujo gastroesofágico (ERGE)","Úlceras pépticas","Enfermedad inflamatoria intestinal (EII)","Cáncer de colon","Hepatitis"],
  "body":[
    p("Reconocemos el papel crucial que desempeña el sistema digestivo en tu bienestar general. Nuestros gastroenterólogos están a la vanguardia de su campo, actualizados en las últimas técnicas y avances médicos para brindar un diagnóstico preciso y un tratamiento efectivo, diseñando un plan personalizado que se adapte a tus necesidades."),
    h("Procedimientos con tecnología de última generación"),
    ul(["Endoscopías: para examinar el interior del tracto digestivo (esofagogastroduodenoscopia y colonoscopia).",
        "Biopsias: para obtener muestras de tejido para su análisis.",
        "Pruebas de función hepática: para evaluar la función del hígado.",
        "Ecografías abdominales: imágenes del hígado, vesícula biliar, páncreas y otros órganos.",
        "Tomografías (TC) y resonancias magnéticas (RMN): imágenes detalladas del tracto digestivo."]),
    p("La salud digestiva es fundamental para mantener una vida sana y activa. Es importante prevenir enfermedades digestivas y consultar con un especialista si presentas cualquier síntoma o inquietud."),
  ]},
 {"slug":"medicina-interna","name":"Medicina Interna",
  "lead":"El médico internista especializado en Infectología diagnostica y trata infecciones en adultos. El internista es el especialista en el diagnóstico y manejo integral del paciente adulto.",
  "includes":["Infecciones respiratorias (neumonía, bronquitis)","Infecciones de transmisión sexual","Infecciones de la piel y tejidos blandos","Infecciones por hongos","Infecciones por virus (VIH, hepatitis)"],
  "body":[
    p("Contamos con un especialista en Medicina Interna altamente capacitado, junto con tecnología de vanguardia y un enfoque integral, para ofrecerte la mejor atención en el diagnóstico, tratamiento y seguimiento de enfermedades del adulto, con especial atención a las enfermedades infecciosas."),
    p("El internista es el médico de cabecera del adulto: evalúa de forma global tu estado de salud, coordina el manejo de enfermedades crónicas y agudas, e integra la información de distintos órganos y sistemas para llegar a un diagnóstico certero."),
    h("Áreas de atención"),
    ul(["Infecciones respiratorias como neumonía y bronquitis.",
        "Infecciones de transmisión sexual.",
        "Infecciones de la piel y tejidos blandos.",
        "Infecciones por hongos.",
        "Infecciones virales como VIH y hepatitis.",
        "Control de enfermedades crónicas: diabetes, hipertensión y más."]),
    p("Te brindamos una atención personalizada y te acompañamos en todo el proceso para garantizar tu bienestar, ayudándote a tomar decisiones informadas sobre tu salud."),
  ]},
 {"slug":"ginecologia","name":"Ginecología",
  "lead":"El área de Ginecología en MIT Medical Tower cuida tu sistema reproductor femenino, atendiendo las patologías relacionadas con el útero, la vagina y los ovarios, con un equipo de ginecólogos altamente calificados. Un ginecólogo es un médico que se especializa en la salud reproductiva de la mujer.",
  "includes":["Atención prenatal","Parto","Planificación familiar","Menopausia","Enfermedades del útero y los ovarios","Enfermedades de transmisión sexual (ETS)"],
  "body":[
    p("La salud de tu sistema reproductor femenino es nuestra prioridad. Contamos con un equipo de ginecólogos altamente calificados y experimentados, junto con tecnología de vanguardia, para ofrecerte la mejor atención integral en el diagnóstico, tratamiento y prevención de enfermedades ginecológicas. Diseñamos un plan de tratamiento personalizado, ya sean procedimientos mínimamente invasivos, tratamientos farmacológicos o cambios en tu estilo de vida."),
    h("Procedimientos ginecológicos"),
    ul(["Citologías y colposcopías: detección temprana de cáncer de cuello uterino y otras enfermedades.",
        "Ecografías pélvicas: evaluación de útero, ovarios y trompas de Falopio.",
        "Mamografías: detección temprana de cáncer de mama.",
        "Biopsias: diagnóstico de diversas afecciones ginecológicas.",
        "Histeroscopias: para examinar el interior del útero.",
        "Laparoscopías: procedimientos quirúrgicos mínimamente invasivos.",
        "Cirugías ginecológicas: miomas uterinos, quistes ováricos, endometriosis y cáncer ginecológico."]),
    p("La salud ginecológica es fundamental para el bienestar general de la mujer. Es importante realizar chequeos regulares y consultar con un especialista ante cualquier síntoma o inquietud."),
  ]},
 {"slug":"traumatologia-ortopedia","name":"Traumatología y Ortopedia",
  "lead":"El área de Traumatología y Ortopedia en MIT Medical Tower cuida y corrige el sistema músculo-esquelético, evitando deformaciones y tratando traumas. Un traumatólogo es un médico que se especializa en el diagnóstico y tratamiento de las lesiones del sistema músculo-esquelético.",
  "includes":["Fracturas","Esguinces","Tendinitis","Artritis","Dolor de espalda","Lesiones deportivas"],
  "body":[
    p("Nuestros especialistas en traumatología y ortopedia están altamente calificados y experimentados, junto con tecnología de vanguardia, para ofrecerte la mejor atención integral en el diagnóstico, tratamiento y prevención de lesiones y enfermedades óseas, musculares y articulares. Diseñamos un plan de tratamiento personalizado, ya sean tratamientos conservadores como fisioterapia o medicamentos, o procedimientos quirúrgicos mínimamente invasivos o complejos."),
    h("Procedimientos con tecnología de última generación"),
    ul(["Radiografías y tomografías: para diagnosticar fracturas, luxaciones, artrosis y otras afecciones.",
        "Artroscopias: para examinar el interior de las articulaciones y realizar reparaciones.",
        "Cirugía de fracturas: técnicas mínimamente invasivas o abiertas.",
        "Reemplazo de articulaciones: prótesis para articulaciones dañadas.",
        "Cirugía de ligamentos y tendones: reparación de lesiones.",
        "Cirugía de columna: hernias discales, escoliosis y más."]),
    p("La salud músculo-esquelética es fundamental para realizar tus actividades diarias y disfrutar de una vida activa. Consulta con un especialista si presentas cualquier síntoma o dolor."),
  ]},
 {"slug":"cirugia-plastica","name":"Cirugía Plástica",
  "lead":"En el área de Cirugía Plástica de MIT Medical Tower cuidamos tu imagen y bienestar personal con un equipo de especialistas y tecnología médica de vanguardia. Un cirujano plástico es un especialista en la reparación y reconstrucción de los tejidos blandos del cuerpo, con el objetivo de mejorar la función y la apariencia.",
  "includes":["Cirugía plástica","Rellenos faciales","Bótox","Láser","Cirugía estética","Liposucción","Abdominoplastia","Aumento de senos"],
  "body":[
    p("Comprendemos la importancia que tiene la imagen y el bienestar personal para la autoestima y la calidad de vida. Por eso contamos con un cirujano plástico altamente especializado y experimentado, junto con tecnología de vanguardia y un enfoque personalizado, para ofrecerte la mejor atención en el diagnóstico, tratamiento y seguimiento de procedimientos quirúrgicos."),
    h("¿Qué hace un cirujano plástico?"),
    ul(["Cirugía reconstructiva: corrige defectos congénitos, traumatismos o enfermedades que afectan la forma y función de las estructuras corporales.",
        "Cirugía estética: mejora la apariencia del rostro, busto, abdomen, extremidades y piel."]),
    p("Nuestros cirujanos no solo se enfocan en realizar procedimientos exitosos, sino que también consideran tus necesidades individuales, expectativas y estilo de vida. Te acompañan en todo el proceso, desde la consulta inicial hasta el seguimiento postoperatorio, para garantizar tu satisfacción y bienestar."),
  ]},
 {"slug":"cardiologia","name":"Cardiología",
  "lead":"El área de Cardiología en MIT Medical Tower cuida tu corazón con un equipo de especialistas y tecnología médica de vanguardia; la prevención es tu mejor aliada. Un cardiólogo es un médico que se especializa en el diagnóstico y tratamiento de las enfermedades del corazón y del sistema circulatorio.",
  "includes":["Enfermedades coronarias","Arritmias cardíacas","Valvulopatías","Cardiomiopatías","Insuficiencia cardíaca","Enfermedades congénitas del corazón"],
  "body":[
    p("Contamos con un equipo de cardiólogos altamente calificados y experimentados, junto con tecnología de vanguardia, para ofrecerte la mejor atención integral en el diagnóstico, tratamiento y prevención de enfermedades cardíacas. Brindamos una evaluación completa de tu salud cardiovascular, considerando tu historial médico, factores de riesgo y estilo de vida, y diseñamos un plan de tratamiento personalizado, ya sean procedimientos mínimamente invasivos o tratamientos farmacológicos."),
    p("Contamos con equipos de última tecnología para realizar estudios diagnósticos precisos, como electrocardiogramas, ecocardiogramas, pruebas de esfuerzo y cateterismos cardíacos. Esto nos permite detectar problemas cardíacos en sus primeras etapas y brindarte un tratamiento oportuno."),
    p("Te ofrecemos un trato cálido y humano, brindándote el apoyo emocional y la orientación que necesitas para afrontar cualquier desafío relacionado con tu salud cardíaca."),
  ]},
 {"slug":"angiologia","name":"Angiología",
  "lead":"El área de Angiología en MIT Medical Tower cuida tu sistema circulatorio y linfático con un equipo de especialistas y tecnología médica de vanguardia. Un angiólogo es un médico que se especializa en el diagnóstico y tratamiento de las enfermedades del sistema circulatorio, incluyendo venas y arterias.",
  "includes":["Enfermedad venosa","Enfermedad arterial"],
  "body":[
    p("Comprendemos la importancia crucial que desempeña el sistema vascular para tu salud y bienestar general. Nuestro angiólogo está a la vanguardia de su campo, actualizado en las últimas técnicas y avances médicos para brindar un diagnóstico preciso y un tratamiento efectivo, con un plan personalizado para tus necesidades."),
    h("Atendemos una amplia gama de enfermedades vasculares"),
    ul(["Enfermedad arterial periférica (EAP)","Várices y arañas vasculares","Aneurisma aórtico","Enfermedad carótida","Trombosis venosa profunda (TVP) y embolia pulmonar (EP)","Pie diabético"]),
    h("Procedimientos con tecnología de última generación"),
    ul(["Ecografías vasculares: imágenes de las arterias y venas.",
        "Doppler vascular: evaluación del flujo sanguíneo.",
        "Angioplastia y colocación de stents: para abrir arterias obstruidas.",
        "Cirugía vascular: aneurismas, enfermedad carótida, TVP y otras afecciones."]),
    p("Te ofrecemos un trato cálido y humano, brindándote el apoyo y la orientación que necesitas para afrontar cualquier desafío relacionado con tu salud vascular."),
  ]},
 {"slug":"urologia","name":"Urología",
  "lead":"El área de Urología en MIT Medical Tower cuida tu sistema urinario y reproductor con un equipo de especialistas y tecnología médica de vanguardia. Un urólogo es un médico que se especializa en el diagnóstico y tratamiento de las enfermedades del sistema urinario en hombres y mujeres, y del sistema reproductor masculino.",
  "includes":["Cáncer de próstata","Disfunción eréctil y enfermedad de Peyronie","Cáncer de testículo y varicocele","Incontinencia urinaria y cáncer de vejiga","Cálculos renales y enfermedad renal crónica","Enfermedades de transmisión sexual (ETS)"],
  "body":[
    p("La salud de tu sistema urinario y reproductor es nuestra prioridad. Contamos con un equipo de urólogos altamente calificados y experimentados, junto con tecnología de vanguardia, para ofrecerte la mejor atención integral en el diagnóstico, tratamiento y prevención de enfermedades urológicas. Diseñamos un plan de tratamiento personalizado, ya sean procedimientos mínimamente invasivos o tratamientos farmacológicos."),
    p("Contamos con equipos de última tecnología para realizar estudios diagnósticos precisos, como uroanálisis, ecografías urológicas, cistoscopias y biopsias de próstata. Esto nos permite detectar problemas urológicos en sus primeras etapas y brindarte un tratamiento oportuno."),
    p("Te ofrecemos un trato cálido y humano, brindándote el apoyo emocional y la orientación que necesitas para afrontar cualquier desafío relacionado con tu salud urológica."),
  ]},
 {"slug":"psicologia","name":"Psicología",
  "lead":"El área de Psicología en MIT Medical Tower cuida tu salud mental con un equipo de psicólogos altamente calificados y experimentados. Un psicólogo es un profesional de la salud mental que se especializa en la evaluación, diagnóstico y tratamiento de los trastornos mentales y del comportamiento.",
  "includes":["Ansiedad","Depresión","Trastorno bipolar","Esquizofrenia"],
  "body":[
    p("Comprendemos que la salud mental es tan importante como la salud física. Ofrecemos una evaluación psicológica completa, considerando tu historia personal, situación actual, necesidades y objetivos. Diseñamos un plan de tratamiento personalizado, utilizando las técnicas terapéuticas más adecuadas para tu caso, como terapia cognitivo-conductual, terapia psicodinámica, terapia familiar o terapia de pareja."),
    p("Te ayudamos a prevenir problemas de salud mental y a promover tu bienestar emocional, brindándote herramientas y estrategias para manejar el estrés, las emociones difíciles y las relaciones interpersonales."),
    p("Garantizamos un entorno seguro y confidencial donde puedas expresar tus pensamientos, sentimientos y experiencias con total libertad. Nuestro equipo está comprometido con el respeto y la ética profesional, ofreciéndote un trato cálido y humano en todo momento."),
  ]},
]

def bold_label(s):
    if ":" in s:
        i = s.index(":")
        label, rest = s[:i], s[i+1:]
        if len(label.split()) <= 4:
            return "<strong>" + label + ":</strong>" + rest
    return s

def render_body(nodes):
    out = []
    for n in nodes:
        t = n[0]
        if t == "p":
            out.append("<p>" + n[1] + "</p>")
        elif t == "h":
            out.append("<h3>" + n[1] + "</h3>")
        elif t == "ul":
            lis = "".join("<li>" + bold_label(i) + "</li>" for i in n[1])
            out.append("<ul>" + lis + "</ul>")
    return "".join(out)

def contact_section(name):
    waname = WA + "?text=" + quote("Hola, me interesa una cita de " + name)
    return f'''<section class="contact section" id="contacto">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Contacto</span>
        <h2>Póngase en contacto con nosotros</h2>
        <p>Estamos aquí para ti. Contáctanos hoy mismo y agenda tu consulta de {name}.</p>
      </div>
      <div class="contact-grid">
        <form class="contact-form" id="contact-form" novalidate>
          <h3>Agenda tu cita de {name}</h3>
          <p class="sub">Déjanos tus datos y te contactamos a la brevedad.</p>
          <div class="field-row">
            <div class="field"><label for="nombre">Nombre completo</label><input type="text" id="nombre" name="nombre" placeholder="Tu nombre" required></div>
            <div class="field"><label for="telefono">Teléfono</label><input type="tel" id="telefono" name="telefono" placeholder="55 0000 0000" required></div>
          </div>
          <div class="field-row">
            <div class="field"><label for="email">Email</label><input type="email" id="email" name="email" placeholder="tu@correo.com"></div>
            <div class="field"><label for="asunto">Asunto</label><input type="text" id="asunto" name="asunto" placeholder="Motivo de tu consulta"></div>
          </div>
          <div class="field"><label for="mensaje">Mensaje</label><textarea id="mensaje" name="mensaje" placeholder="Cuéntanos cómo podemos ayudarte"></textarea></div>
          <button type="submit" class="btn btn-primary btn-lg" style="width:100%">Enviar mensaje</button>
          <p class="form-status" role="status" aria-live="polite"></p>
        </form>
        <div class="contact-info">
          <div class="info-card"><span class="ic"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg></span><div><h4>Ubicación</h4><p>Blvrd Prados de Aragón 8B, Prados de Aragón, 57179 Cdad. Nezahualcóyotl, Méx.</p></div></div>
          <div class="info-card"><span class="ic"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg></span><div><h4>Email</h4><a href="mailto:mitmedicalt@yahoo.com">mitmedicalt@yahoo.com</a></div></div>
          <div class="info-card"><span class="ic"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg></span><div><h4>Teléfono</h4><a href="tel:+525528380715">(+52) 552 838 0715</a></div></div>
          <a class="btn btn-whatsapp" href="{waname}" target="_blank" rel="noopener" style="width:100%">Agendar por WhatsApp</a>
        </div>
      </div>
    </div>
  </section>'''

TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} | MIT Medical Tower</title>
<meta name="description" content="{meta}">
<link rel="canonical" href="https://medtower.com.mx/especialidades/{slug}.html">
<meta property="og:type" content="website">
<meta property="og:title" content="{name} | MIT Medical Tower">
<meta property="og:description" content="{meta}">
<meta property="og:locale" content="es_MX">
<link rel="icon" href="../assets/logo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/styles.css">
</head>
<body>
<div id="site-header"></div>
<main>
  <section class="page-hero">
    <div class="hero-bg"></div><div class="hero-overlay"></div>
    <div class="container">
      <nav class="breadcrumb" aria-label="Ruta"><a href="../index.html">Inicio</a><span>&rsaquo;</span><a href="../index.html#especialidades">Especialidades</a><span>&rsaquo;</span><span>{name}</span></nav>
      <div class="page-hero-grid">
        <div>
          <div class="ic-badge"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24">{icon}</svg></div>
          <h1>{name}</h1>
          <p class="lead">{lead}</p>
          <ul class="includes"><li class="includes-title">Esto incluye</li>{includes}</ul>
          <a href="{wa}" target="_blank" rel="noopener" class="btn btn-accent btn-lg">Agendar cita</a>
        </div>
        <div class="page-hero-media"><div class="frame"><img class="site-img" src="../assets/especialidades/{slug}.png" alt="{name} — MIT Medical Tower"></div></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="content-grid">
        <div>
          <span class="eyebrow">Área de {name}</span>
          <div class="rich">{body}</div>
          <a href="{wa}" target="_blank" rel="noopener" class="btn btn-primary" style="margin-top:1.25rem">Agendar mi cita</a>
        </div>
        <aside class="media-stack">
          <div class="frame"><img class="site-img" src="../assets/imagenes/quirofano-2.jpeg" alt="Instalaciones MIT Medical Tower"></div>
          <div class="frame"><img class="site-img" src="../assets/imagenes/habitacion-completa.jpeg" alt="Habitación de hospital MIT Medical Tower"></div>
        </aside>
      </div>
    </div>
  </section>

  <section class="why-band section">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Especialistas</span>
        <h2>¿Por qué elegir a nuestros especialistas?</h2>
        <p>Nuestros especialistas se mantienen actualizados con los últimos avances médicos y técnicas para garantizar que recibas el mejor tratamiento posible.</p>
      </div>
      <div class="why-grid">
        <div class="why-card">
          <div class="ic">{badge}</div>
          <h3>Expertos que marcan la diferencia</h3>
          <p>En MIT Medical Tower seleccionamos cuidadosamente a nuestros especialistas para asegurarnos de que posean la experiencia y las habilidades necesarias para brindar atención médica excepcional. Nuestro equipo de cirujanos plásticos, cardiólogos, ginecólogos y médicos internistas son líderes en sus respectivas áreas.</p>
        </div>
        <div class="why-card">
          <div class="ic">{heart}</div>
          <h3>Atención cálida y humana</h3>
          <p>Nos preocupamos por tu bienestar integral. Te ofrecemos un trato cercano y humano, brindándote el apoyo y la orientación que necesitas en cada paso de tu atención médica.</p>
        </div>
      </div>
    </div>
  </section>

  {contact}
</main>

<section class="cta-band">
  <div class="blob"></div>
  <div class="container">
    <h2>Agenda tu cita de {name}</h2>
    <p>Da el primer paso hacia tu bienestar. Te atendemos con calidez y profesionalismo.</p>
    <a href="{wa}" target="_blank" rel="noopener" class="btn btn-accent btn-lg">Agendar por WhatsApp</a>
  </div>
</section>

<div id="site-footer"></div>
<script src="../js/layout.js"></script>
<script src="../js/main.js"></script>
</body>
</html>
'''

def build():
    os.makedirs(OUT, exist_ok=True)
    count = 0
    for s in SPECS:
        name = s["name"]
        meta = (s["lead"][:155].rsplit(" ", 1)[0]) + "…"
        includes = "".join('<li><span class="dot">' + CHECK + "</span>" + it + "</li>" for it in s["includes"])
        wa = WA + "?text=" + quote("Hola, me interesa una cita de " + name)
        html = TEMPLATE.format(
            name=name, slug=s["slug"], meta=meta, lead=s["lead"],
            icon=ICONS[s["slug"]], includes=includes, wa=wa,
            building=ICON_BUILDING, facility=ICON_FACILITY, specialist=ICON_SPECIALIST,
            badge=ICON_BADGE, heart=ICON_HEART,
            body=render_body(s["body"]), contact=contact_section(name),
        )
        path = os.path.join(OUT, s["slug"] + ".html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        count += 1
        print("  +", s["slug"] + ".html")
    print("Generadas", count, "paginas en", OUT)

if __name__ == "__main__":
    build()
