# -*- coding: utf-8 -*-
"""Textos de la web de Numarsi (ES / EN) y plantillas de cada página."""
import html as H, json

ADDRESS = "Pol. Ind. O Campiño, Rúa das Mámoas, 28-29 · 36158 Pontevedra"
MAPS = "https://www.google.com/maps/search/?api=1&query=Pol%C3%ADgono+Industrial+O+Campi%C3%B1o+R%C3%BAa+das+M%C3%A1moas+28+36158+Pontevedra"

T = {
 "es": dict(
  home_title="Numarsi | Elaboración por encargo de productos del mar congelados",
  og_site="nuestro mar de siempre", og_alt="Logotipo de Numarsi sobre una línea de producción de pescado congelado",
  skip="Saltar al contenido", menu="Menú", nav_label="Navegación principal", lang_label="Idioma",
  logo_alt="Numarsi, ir al inicio", cta_main="Solicita información", cta_catalog="Descarga el catálogo",
  catalog_file="numarsi-catalogo.pdf",
  footer_about="Elaboramos por encargo productos del mar congelados en Pontevedra. Solo vendemos servicios: no competimos con nuestros clientes.",
  footer_nav="Numarsi", footer_contact="Contacto", email="info@numarsi.com",
  location="Pontevedra, Galicia", linkedin="Numarsi en LinkedIn",
  legal="Aviso legal", privacy="Privacidad", cookies="Cookies", ethics="Canal Ético",
  academic="Propuesta de rediseño elaborada como proyecto académico.",
 ),
 "en": dict(
  home_title="Numarsi | Contract processing of frozen seafood",
  og_site="nuestro mar de siempre", og_alt="Numarsi logo over a frozen fish production line",
  skip="Skip to content", menu="Menu", nav_label="Main navigation", lang_label="Language",
  logo_alt="Numarsi, go to home page", cta_main="Get in touch", cta_catalog="Download the catalogue",
  catalog_file="numarsi-catalogue-en.pdf",
  footer_about="We carry out contract processing of frozen seafood in Pontevedra, Spain. We only sell services: we never compete with our clients.",
  footer_nav="Numarsi", footer_contact="Contact", email="info@numarsi.com",
  location="Pontevedra, Galicia, Spain", linkedin="Numarsi on LinkedIn",
  legal="Legal notice", privacy="Privacy", cookies="Cookies", ethics="Ethics channel",
  academic="Redesign proposal prepared as an academic project.",
 ),
}

# ---------- piezas reutilizables ----------
def cta_band(c, title, text):
    t = c["t"]; contact = PAGES["contact"][c["lang"]]["file"]
    return f'''<section><div class="wrap"><div class="cta-band reveal on-dark">
 <div><h2>{title}</h2><p>{text}</p></div>
 <div class="btns"><a class="btn btn-primary" href="{contact}#formulario">{t["cta_main"]}</a>
 <a class="btn btn-ghost" href="{{P}}assets/{t["catalog_file"]}" download>{c["icon"]("download")}{t["cta_catalog"]}</a></div>
</div></div></section>'''

def page_hero(eyebrow, title, text):
    return f'<section class="page-hero"><div class="wrap"><span class="eyebrow">{eyebrow}</span><h1>{title}</h1><p>{text}</p></div></section>'

def certs(c):
    L = c["lang"]
    data = {
     "es": [("IFS","Food","Norma internacional de seguridad alimentaria reconocida por la GFSI y exigida por la gran distribución."),
            ("MSC","Cadena de custodia","Trazabilidad de productos procedentes de pesquerías sostenibles certificadas."),
            ("ASC","Cadena de custodia","Trazabilidad de productos procedentes de acuicultura responsable certificada."),
            ("Friend of the Sea","Sostenibilidad","Reconocimiento a las prácticas de pesca y acuicultura sostenibles.")],
     "en": [("IFS","Food","International GFSI-recognised food safety standard required by major retailers."),
            ("MSC","Chain of custody","Traceability for products from certified sustainable fisheries."),
            ("ASC","Chain of custody","Traceability for products from certified responsible aquaculture."),
            ("Friend of the Sea","Sustainability","Recognition of sustainable fishing and aquaculture practices.")]}[L]
    return '<div class="grid g4">' + "".join(
        f'<div class="cert reveal"><div class="badge" aria-hidden="true"><span>{n}<small>{s.upper()}</small></span></div><h3>{n}</h3><p>{d}</p></div>'
        for n, s, d in data) + '</div>'

SERV = {
 "es": [
  ("fillet","fileteado","Fileteado y pelado de pescado","puestos-preparacion","Operarias trabajando en los puestos de preparación de la planta de Numarsi",
   "Trabajamos a partir de dos tipos de materia prima. El respeto por la materia prima, la precisión y la meticulosidad son nuestros puntos fuertes.",
   ["Desde pescado entero descabezado y eviscerado (HG): fileteado, o fileteado y pelado","Desde filete fresco o congelado IQF: pelado"]),
  ("squid","cefalopodos","Limpieza, eviscerado y tratamiento de cefalópodos","equipo-planta","Operaria con equipo de protección junto a una caja de producto en la planta",
   "Contamos con una línea específica para el eviscerado y su posterior troceado en anillas.",
   ["Línea específica de eviscerado y troceado en anillas","Salas refrigeradas para realizar los tratamientos que se requieran","Almacenamiento posterior"]),
  ("cut","corte","Corte en diferentes tamaños y formas","linea-sierras","Línea de corte con sierras y porciones de pescado sobre la cinta transportadora",
   "Realizamos una gran variedad de cortes, tanto en forma como en tamaño, con un equipo humano altamente cualificado y equipos automáticos.",
   ["Medallones, rodajas, taquitos y tiras, entre otros","Porcionado automático a partir de bloques de pescado","Gran variedad de formas y tamaños"]),
  ("snow","congelacion","Congelación IQF y glaseado","pescado-congelado","Caja con pescado congelado junto a la línea de producción",
   "Disponemos de dos túneles dinámicos de congelación y otros dos de secado, con una capacidad de 4 t/h, en los que realizamos la congelación y el glaseo.",
   ["Dos túneles dinámicos de congelación y dos de secado","Capacidad de 4 toneladas por hora","Congelación y glaseo","Túneles distribuidos estratégicamente en la fábrica para una mayor eficiencia global del proceso"]),
  ("box","envasado","Envasado en distintos tamaños y formatos","linea-envasado","Línea de envasado con pesadora multicabezal y operarias preparando cajas",
   "Envasamos en el tamaño y el formato que necesita cada cliente.",
   ["Embolsado","Doble piel","Envasado al vacío","Estuchado","A granel"]),
 ],
 "en": [
  ("fillet","filleting","Fish filleting and skinning","puestos-preparacion","Operators working at the preparation stations in the Numarsi plant",
   "We work from two kinds of raw material. Respect for the raw material, precision and meticulous work are our strengths.",
   ["From headed and gutted (HG) fish: filleting, or filleting and skinning","From fresh or IQF fillets: skinning"]),
  ("squid","cephalopods","Cephalopod cleaning, gutting and treatment","equipo-planta","Operator in protective clothing next to a crate of product in the plant",
   "We have a dedicated line for gutting and then cutting into rings.",
   ["Dedicated line for gutting and cutting into rings","Chilled rooms for any treatments required","Subsequent storage"]),
  ("cut","cutting","Cutting in different sizes and shapes","linea-sierras","Cutting line with band saws and fish portions on the conveyor",
   "We offer a wide range of cuts, in both shape and size, with a highly skilled team and automatic equipment.",
   ["Medallions, steaks, cubes and strips, among others","Automatic portioning from fish blocks","A wide variety of shapes and sizes"]),
  ("snow","freezing","IQF freezing and glazing","pescado-congelado","Crate of frozen fish next to the production line",
   "We have two dynamic freezing tunnels and two drying tunnels with a capacity of 4 t/h, where we freeze and glaze.",
   ["Two dynamic freezing tunnels and two drying tunnels","Capacity of 4 tonnes per hour","Freezing and glazing","Tunnels strategically placed in the plant for greater overall efficiency"]),
  ("box","packing","Packing in different sizes and formats","linea-envasado","Packing line with a multihead weigher and operators preparing boxes",
   "We pack in the size and format each client needs.",
   ["Bags","Double skin","Vacuum packs","Cartons","Bulk"]),
 ]}

PACKS = {
 "es":[("bag","Embolsado","Producto en bolsa, en distintos tamaños."),("skin","Doble piel","Envase con film ajustado al producto."),
       ("vacuum","Envasado al vacío","Producto envasado al vacío."),("carton","Estuchado","Producto en estuche de cartón."),
       ("bulk","A granel","Producto a granel.")],
 "en":[("bag","Bags","Product in bags, in different sizes."),("skin","Double skin","Pack with film fitted to the product."),
       ("vacuum","Vacuum packs","Vacuum-packed product."),("carton","Cartons","Product in a cardboard carton."),
       ("bulk","Bulk","Bulk product.")]}

EXTRA = {
 "es": [("snowbox","Almacenamiento en frío","Almacenamos en frío el producto de nuestros clientes."),
        ("chart","Escandallos","Realizamos escandallos de la materia prima de nuestros clientes."),
        ("lab","Muestras a medida","Preparamos muestras comerciales según tu especificación antes de lanzar la producción.")],
 "en": [("snowbox","Cold storage","We provide cold storage for our clients’ products."),
        ("chart","Yield analysis","We carry out yield analyses (escandallos) of our clients’ raw material."),
        ("lab","Tailor-made samples","We prepare commercial samples to your specification before production starts.")]}

def pack_grid(c):
    L = c["lang"]
    alt = {"es":"Máquina de cierre de cajas en la línea de envasado de Numarsi","en":"Box sealing machine on the Numarsi packing line"}[L]
    cards = "".join(f'<li class="pack-item reveal"><h3>{n}</h3><p>{d}</p></li>' for k, n, d in PACKS[L])
    return f'<div class="split pack-split"><div class="photo reveal">{c["pic"]("maquina-envasado", alt, "(min-width: 900px) 45vw, 100vw")}</div><ul class="pack-list">{cards}</ul></div>'

def extra_grid(c):
    return '<div class="grid g3">' + "".join(
        f'<article class="card reveal"><div class="icon">{c["icon"](i)}</div><h3>{a}</h3><p>{b}</p></article>' for i, a, b in EXTRA[c["lang"]]) + '</div>'

ILLU_SQUID = '<svg viewBox="0 0 200 200" role="img" aria-label="{a}"><circle cx="100" cy="100" r="90" fill="#fff" opacity=".6"/><path d="M100 22c22 14 30 38 30 70H70c0-32 8-56 30-70z" fill="#f6e3d6" stroke="#1d4288" stroke-width="5" stroke-linejoin="round"/><path d="M72 92c0 30-14 46-22 70M86 92c0 30-6 52-6 78M114 92c0 30 6 52 6 78M128 92c0 30 14 46 22 70" fill="none" stroke="#1d4288" stroke-width="5" stroke-linecap="round"/><circle cx="90" cy="70" r="5" fill="#1d4288"/><circle cx="110" cy="70" r="5" fill="#1d4288"/><g fill="none" stroke="#199ad6" stroke-width="6"><circle cx="40" cy="48" r="14"/><circle cx="162" cy="56" r="12"/><circle cx="160" cy="150" r="14"/></g></svg>'
ILLU_SNOW = '<svg viewBox="0 0 200 200" role="img" aria-label="{a}"><circle cx="100" cy="100" r="90" fill="#fff" opacity=".6"/><g stroke="#1d4288" stroke-width="7" stroke-linecap="round" fill="none"><path d="M100 30v140M39 65l122 70M161 65 39 135"/><path d="m82 40 18 12 18-12M82 160l18-12 18 12M44 88l20-2-8-18M156 88l-20-2 8-18M44 112l20 2-8 18M156 112l-20 2 8 18"/></g><circle cx="100" cy="100" r="14" fill="#199ad6"/></svg>'

SHORT = {"es": ["Desde pescado entero (HG) o desde filete, fresco o IQF.","Línea propia de eviscerado y troceado en anillas.","Medallones, rodajas, taquitos y tiras, también desde bloque.","Dos túneles dinámicos con una capacidad de 4 t/h.","Embolsado, doble piel, vacío, estuchado y granel."],
         "en": ["From whole (HG) fish or from fresh or IQF fillets.","Dedicated line for gutting and cutting into rings.","Medallions, steaks, cubes and strips, also from blocks.","Two dynamic tunnels with a capacity of 4 t/h.","Bags, double skin, vacuum, cartons and bulk."]}

def service_blocks(c, full=False):
    L = c["lang"]; out = []
    for n, (ic, anchor, title, img, alt, lead, items) in enumerate(SERV[L]):
        if full:
            if img:
                media = f'<div class="service-media">{c["pic"](img, alt)}</div>'
            else:
                a = {"squid":{"es":"Ilustración de un calamar y anillas","en":"Illustration of a squid and rings"},
                     "snow":{"es":"Ilustración de un copo de nieve que representa la congelación","en":"Snowflake illustration representing freezing"}}[ic][L]
                media = f'<div class="service-media illu">{(ILLU_SQUID if ic=="squid" else ILLU_SNOW).format(a=a)}</div>'
            lis = "".join(f"<li>{x}</li>" for x in items)
            out.append(f'<article class="service reveal" id="{anchor}">{media}<div><div class="icon">{c["icon"](ic)}</div><h2>{title}</h2><p>{lead}</p><ul>{lis}</ul></div></article>')
        else:
            more = {"es":"Ver servicio","en":"See service"}[L]
            out.append(f'<article class="card card-photo reveal"><div class="card-media">{c["pic"](img, alt, "(min-width: 960px) 20vw, (min-width: 640px) 50vw, 100vw")}</div><h3>{title}</h3><p>{SHORT[L][n]}</p><a class="more" href="{PAGES["services"][L]["file"]}#{anchor}">{more}<span class="visually-hidden">: {title}</span></a></article>')
    return "".join(out)

def stats(c, light=False):
    L = c["lang"]
    s = {"es":[("2011","año de fundación"),("2","plantas en Pontevedra"),("3.500 m²","de superficie total"),("+180","personas en el equipo"),("4 t/h","de capacidad de congelación IQF")],
         "en":[("2011","founded"),("2","plants in Pontevedra"),("3,500 m²","total floor area"),("180+","people on the team"),("4 t/h","IQF freezing capacity")]}[L]
    return '<ul class="stats stats-5">' + "".join(f'<li class="reveal"><strong>{a}</strong><span>{b}</span></li>' for a, b in s) + '</ul>'

def pillars(c):
    L = c["lang"]
    p = {"es":[("handshake","No comercializamos","Únicamente vendemos servicios: no competimos con nuestros clientes."),
               ("factory","Especialistas en elaboración","Dedicamos todo nuestro tiempo a dar soluciones a las necesidades de producción de cada cliente."),
               ("shield","Filosofía de calidad","Altos estándares de calidad y seguridad alimentaria, con un Departamento de Calidad que controla todo el proceso."),
               ("clock","Servicios adicionales y plazos","Almacenamiento en frío, escandallos y muestras a medida, con entrega en el plazo acordado.")],
         "en":[("handshake","We don’t sell products","We only sell services, so we never compete with our clients."),
               ("factory","Processing specialists","We devote all our time to solving each client’s production needs."),
               ("shield","Quality philosophy","High quality and food safety standards, with a Quality Department that checks the whole process."),
               ("clock","Extra services and deadlines","Cold storage, yield analysis and tailor-made samples, delivered on the agreed date.")]}[L]
    return '<div class="why">' + "".join(f'<div class="why-item reveal"><div class="icon icon-dark">{c["icon"](i)}</div><h3>{a}</h3><p>{b}</p></div>' for i, a, b in p) + '</div>'

# ---------- páginas ----------
def home(c):
    t = c["t"]; L = c["lang"]; contact = PAGES["contact"][L]["file"]
    S = {"es": dict(
            eyebrow="Elaboración por encargo · Pontevedra",
            h1="Especialistas en la elaboración de productos del mar",
            lead="Elaboramos productos del mar congelados para que nuestros clientes lleguen al consumidor con el mejor producto. Nos adaptamos a las necesidades de cada uno, manteniendo la calidad de su materia prima.",
            facts=["Solo vendemos servicios","Certificación IFS Food","Desde 2011"],
            alt="Línea de corte de Numarsi con porciones de pescado congelado sobre la cinta",
            serv=("Qué hacemos", "Realizamos una parte del proceso o el producto completo: de la materia prima al producto congelado y envasado."),
            all_serv="Ver todos los servicios",
            why=("Nuestro valor diferencial", "Una empresa de servicios que complementa los procesos productivos de sus clientes y forma parte de su cadena de valor."),
            adapt=("Nos adaptamos a cada cliente", "Cada cliente tiene su especificación, su marca y su mercado. Trabajamos con tu materia prima, con el corte y el formato que necesitas, y guardamos la confidencialidad de tus productos.",
                   ["Procesos a medida, desde un servicio hasta el producto terminado","Envasado en el tamaño y el formato que necesites","Muestras comerciales antes de producir","Confidencialidad sobre tus productos y especificaciones"]),
            cert=("Calidad certificada", "Un Departamento de Calidad propio aplica controles rigurosos en todo el proceso productivo."),
            fac=("Nuestras instalaciones", "Dos fábricas en Pontevedra que suman 3.500 m², con líneas de fileteado, cefalópodo, corte, congelación IQF y envasado.", "Conoce las instalaciones"),
            cta=("¿Hablamos de tu producción?", "Cuéntanos qué necesitas y te proponemos cómo hacerlo, con muestras si lo necesitas.")),
         "en": dict(
            eyebrow="Contract processing · Pontevedra, Spain",
            h1="Specialists in seafood processing",
            lead="We process frozen seafood so our clients can reach consumers with the best product. We adapt to each client’s needs while preserving the quality of their raw material.",
            facts=["We only sell services","IFS Food certified","Since 2011"],
            alt="Numarsi cutting line with frozen fish portions on the conveyor",
            serv=("What we do", "We handle one step of the process or the complete product: from raw material to frozen, packed product."),
            all_serv="See all services",
            why=("What sets us apart", "A service company that complements its clients’ production processes and is part of their value chain."),
            adapt=("We adapt to every client", "Every client has its own specification, brand and market. We work with your raw material, with the cut and format you need, and we keep your products confidential.",
                   ["Tailor-made processes, from a single service to the finished product","Packed in the size and format you need","Commercial samples before production","Confidentiality for your products and specifications"]),
            cert=("Certified quality", "Our own Quality Department applies strict checks throughout the production process."),
            fac=("Our facilities", "Two factories in Pontevedra totalling 3,500 m², with filleting, cephalopod, cutting, IQF freezing and packing lines.", "Discover our facilities"),
            cta=("Shall we talk about your production?", "Tell us what you need and we’ll propose how to do it, with samples if required."))}[L]
    facts = "".join(f"<li>{x}</li>" for x in S["facts"])
    adapt_li = "".join(f"<li>{x}</li>" for x in S["adapt"][2])
    return f'''
<section class="hero on-dark"><div class="wrap hero-in">
 <div><span class="eyebrow">{S["eyebrow"]}</span><h1>{S["h1"]}</h1><p class="lead">{S["lead"]}</p>
  <div class="btns"><a class="btn btn-primary" href="{contact}#formulario">{t["cta_main"]}</a>
  <a class="btn btn-ghost" href="{{P}}assets/{t["catalog_file"]}" download>{c["icon"]("download")}{t["cta_catalog"]}</a></div>
  <ul class="hero-facts">{facts}</ul></div>
 <div class="hero-media">{c["pic"]("linea-corte", S["alt"], "(min-width: 900px) 45vw, 100vw", eager=True)}</div>
</div>
<svg class="hero-wave" viewBox="0 0 1440 48" preserveAspectRatio="none" aria-hidden="true"><path fill="currentColor" d="M0 48h1440V20c-240 26-480 30-720 12S240 4 0 24z"/></svg></section>
<section class="stats-band"><div class="wrap">{stats(c)}</div></section>
<section class="section-soft"><div class="wrap"><div class="section-head reveal"><h2>{S["serv"][0]}</h2><p>{S["serv"][1]}</p></div><div class="grid g5">{service_blocks(c)}</div>
 <p class="center reveal"><a class="btn btn-ghost" href="{PAGES["services"][L]["file"]}">{S["all_serv"]}</a></p></div></section>
<section class="section-dark"><div class="wrap"><div class="section-head reveal"><h2>{S["why"][0]}</h2><p>{S["why"][1]}</p></div>{pillars(c)}</div></section>
<section><div class="wrap split">
 <div class="photo reveal">{c["pic"]("control-calidad", {"es":"Técnica de calidad revisando los registros de control junto a un compañero","en":"Quality technician reviewing control records with a colleague"}[L], "(min-width: 900px) 40vw, 100vw")}</div>
 <div class="reveal"><h2>{S["adapt"][0]}</h2><p>{S["adapt"][1]}</p><ul class="checks">{adapt_li}</ul></div>
</div></section>
<section class="section-soft"><div class="wrap"><div class="section-head reveal"><h2>{S["cert"][0]}</h2><p>{S["cert"][1]}</p></div>{certs(c)}</div></section>
<section><div class="wrap split">
 <div class="reveal"><h2>{S["fac"][0]}</h2><p>{S["fac"][1]}</p><a class="btn btn-ghost" href="{PAGES["facilities"][L]["file"]}">{S["fac"][2]}</a></div>
 <div class="photo reveal">{c["pic"]("planta-aerea", {"es":"Vista aérea de una de las plantas de Numarsi, con placas solares en la cubierta","en":"Aerial view of one of the Numarsi plants, with solar panels on the roof"}[L], "(min-width: 900px) 45vw, 100vw")}</div>
</div></section>
{cta_band(c, S["cta"][0], S["cta"][1])}'''

def services(c):
    L = c["lang"]
    if L == "es":
        h = page_hero("Servicios", "Nos adaptamos a las necesidades de cada cliente", "Manteniendo la calidad de sus materias primas. Puedes contratar cada servicio por separado o combinarlos para recibir tu producto terminado, congelado y envasado.")
        gal = ("Formatos de envasado", "Estas son algunas de las alternativas de envasado que ofrecemos.")
        ext = ("Servicios adicionales", "Además, ofrecemos otros servicios exclusivos para nuestros clientes.")
        cta = ("¿Qué servicio necesitas?", "Cuéntanos el producto, el proceso y el formato, y te enviamos una propuesta.")
    else:
        h = page_hero("Services", "We adapt to each client’s needs", "While preserving the quality of their raw materials. Book each service separately or combine them to receive your product finished, frozen and packed.")
        gal = ("Packing formats", "These are some of the packing options we offer.")
        ext = ("Additional services", "We also offer other exclusive services for our clients.")
        cta = ("Which service do you need?", "Tell us the product, process and format, and we’ll send you a proposal.")
    return f'''{h}
<section><div class="wrap">{service_blocks(c, full=True)}</div></section>
<section class="section-soft" id="formatos"><div class="wrap"><div class="section-head reveal"><h2>{gal[0]}</h2><p>{gal[1]}</p></div>{pack_grid(c)}</div></section>
<section id="adicionales"><div class="wrap"><div class="section-head reveal"><h2>{ext[0]}</h2><p>{ext[1]}</p></div>{extra_grid(c)}</div></section>
{cta_band(c, cta[0], cta[1])}'''

def quality(c):
    L = c["lang"]
    if L == "es":
        h = page_hero("Calidad", "Una filosofía de calidad en todo el proceso", "Aplicamos altos estándares de calidad y seguridad alimentaria. Nuestro Departamento de Calidad realiza controles rigurosos desde la recepción de la materia prima hasta la expedición.")
        ctrl_h = "Controles en cada etapa"
        ctrl = [("Recepción","Control de la materia prima a su llegada a la planta."),("Proceso","Controles durante la elaboración de cada producto."),
                ("Congelación y glaseo","Control de los procesos de congelación y glaseo."),("Producto terminado","Control del producto antes de su expedición.")]
        cert_h = ("Certificaciones", "Trabajamos según los estándares que exige la distribución europea.")
        conf = ("Confidencialidad y transparencia", "Somos totalmente transparentes con nuestros clientes en cuanto a procesos y controles de producción, y mantenemos en privado los detalles y especificaciones de sus productos.")
        alt = "Técnica de calidad con equipo de protección en la sala de producción"
        cta = ("¿Quieres saber más sobre nuestra calidad?", "Escríbenos y te informamos.")
    else:
        h = page_hero("Quality", "A quality philosophy across the whole process", "We apply high quality and food safety standards. Our Quality Department carries out strict checks from raw material intake to dispatch.")
        ctrl_h = "Checks at every stage"
        ctrl = [("Intake","Checks on the raw material when it arrives at the plant."),("Processing","Checks while each product is being processed."),
                ("Freezing and glazing","Control of the freezing and glazing processes."),("Finished product","Checks on the product before dispatch.")]
        cert_h = ("Certifications", "We work to the standards European retail requires.")
        conf = ("Confidentiality and transparency", "We are fully transparent with our clients about processes and production controls, and keep the details and specifications of their products private.")
        alt = "Quality technician in protective clothing on the production floor"
        cta = ("Want to know more about our quality?", "Write to us and we’ll tell you more.")
    cl = "".join(f'<li class="reveal"><h3>{a}</h3><p>{b}</p></li>' for a, b in ctrl)
    return f'''{h}
<section><div class="wrap"><div class="section-head reveal"><h2>{ctrl_h}</h2></div><ol class="steps">{cl}</ol></div></section>
<section class="section-soft"><div class="wrap"><div class="section-head reveal"><h2>{cert_h[0]}</h2><p>{cert_h[1]}</p></div>{certs(c)}</div></section>
<section><div class="wrap split">
 <div class="photo reveal">{c["pic"]("equipo-planta", alt, "(min-width: 900px) 40vw, 100vw")}</div>
 <div class="reveal"><div class="icon">{c["icon"]("lock")}</div><h2>{conf[0]}</h2><p>{conf[1]}</p></div>
</div></section>
{cta_band(c, cta[0], cta[1])}'''

def development(c):
    L = c["lang"]
    if L == "es":
        h = page_hero("Mejora y Desarrollo", "Te acompañamos desde la idea hasta la producción", "Nuestro departamento de Mejora y Desarrollo asesora y acompaña a cada cliente en cuatro áreas.")
        items = [("lab","Nuevos productos y procesos","Creación de nuevos productos y procesos para ampliar tu gama o mejorar los que ya tienes."),
                 ("box","Muestras comerciales a medida","Realización de muestras comerciales adaptadas a las necesidades y especificaciones de cada cliente."),
                 ("doc","Diseño de envase y embalaje","Diseño del envase y del embalaje, adaptados a tu marca y a tu logística."),
                 ("chart","Proyectos integrales","Proyectos adaptados a cada cliente: pruebas de validación, análisis de datos y escalado a producción.")]
        how_h = "Cómo trabajamos"
        how = [("Necesidad","Nos cuentas el producto, el mercado y el formato que buscas."),("Pruebas","Hacemos ensayos en planta y te enviamos muestras."),
               ("Validación","Ajustamos con tus comentarios y validamos rendimientos con datos."),("Producción","Pasamos a la producción del producto validado.")]
        cta = ("¿Tienes un proyecto en mente?", "Cuéntanoslo y empezamos con una primera muestra.")
    else:
        h = page_hero("Product development", "We support you from idea to production", "Our Improvement and Development department advises and supports each client in four areas.")
        items = [("lab","New products and processes","Creating new products and processes to extend your range or improve existing ones."),
                 ("box","Tailor-made commercial samples","Commercial samples adapted to each client’s needs and specifications."),
                 ("doc","Pack and outer case design","Packaging and outer case design adapted to your brand and logistics."),
                 ("chart","End-to-end projects","Projects adapted to each client: validation trials, data analysis and scale-up to production.")]
        how_h = "How we work"
        how = [("Need","You tell us the product, market and format you’re looking for."),("Trials","We run plant trials and send you samples."),
               ("Validation","We fine-tune with your feedback and validate yields with data."),("Production","We move the validated product into production.")]
        cta = ("Got a project in mind?", "Tell us about it and we’ll start with a first sample.")
    it = "".join(f'<article class="card reveal"><div class="icon">{c["icon"](i)}</div><h3>{a}</h3><p>{b}</p></article>' for i, a, b in items)
    hw = "".join(f'<li class="reveal"><h3>{a}</h3><p>{b}</p></li>' for a, b in how)
    return f'''{h}
<section><div class="wrap"><div class="grid g4">{it}</div></div></section>
<section class="section-soft"><div class="wrap"><div class="section-head reveal"><h2>{how_h}</h2></div><ol class="steps">{hw}</ol></div></section>
{cta_band(c, cta[0], cta[1])}'''

def facilities(c):
    L = c["lang"]
    if L == "es":
        hh = ("Instalaciones", "Instalaciones pensadas para un servicio de calidad", "Nuestras instalaciones y equipos están pensados para ofrecer servicios de calidad que respondan a las necesidades del consumidor y a las tendencias del mercado.")
        lines_h = "Líneas y equipos"
        lines = ["Fileteado y pelado de pescado","Línea específica de cefalópodo","Porcionado automático desde bloque","2 túneles de congelación IQF y 2 de secado","Salas refrigeradas para tratamientos y almacenamiento","Líneas de envasado con pesadora multicabezal"]
        gal_h = "Un recorrido por la planta"
        gal = [("linea-corte","Línea de porcionado a partir de bloque congelado","Porciones de pescado congelado saliendo de la línea de corte"),
               ("linea-envasado","Línea de envasado","Línea de envasado con pesadora multicabezal y operarias"),
               ("puestos-limpieza","Puestos de preparación","Operarias trabajando en puestos individuales de la línea de preparación"),
               ("planta-aerea","Vista aérea de la planta","Vista aérea de la nave con placas solares en la cubierta"),
               ("fachada-muelles","Muelles de carga","Fachada de la planta con camiones frigoríficos en los muelles"),
               ("cartel-numarsi","Entrada a la planta","Cartel con el logotipo de Numarsi en la entrada de la planta")]
        vid = ("Vídeo de la planta de Numarsi: fachada, vista aérea y cartel de entrada", "Pausar vídeo", "Reproducir vídeo")
        cta = ("¿Hablamos de tu producción?", "Cuéntanos qué necesitas y te proponemos cómo hacerlo.")
    else:
        hh = ("Facilities", "Facilities designed for quality service", "Our facilities and equipment are designed to deliver quality services that meet consumer needs and market trends.")
        lines_h = "Lines and equipment"
        lines = ["Filleting and skinning line","Dedicated cephalopod line","Automatic portioning from blocks","2 IQF freezing tunnels and 2 drying tunnels","Chilled rooms for treatments and storage","Packing lines with multihead weigher"]
        gal_h = "A tour of the plant"
        gal = [("linea-corte","Portioning line for frozen blocks","Frozen fish portions coming off the cutting line"),
               ("linea-envasado","Packing line","Packing line with a multihead weigher and operators"),
               ("puestos-limpieza","Preparation stations","Operators working at individual stations on the preparation line"),
               ("planta-aerea","Aerial view of the plant","Aerial view of the building with solar panels on the roof"),
               ("fachada-muelles","Loading docks","Plant façade with refrigerated lorries at the loading docks"),
               ("cartel-numarsi","Plant entrance","Sign with the Numarsi logo at the plant entrance")]
        vid = ("Video of the Numarsi plant: façade, aerial view and entrance sign", "Pause video", "Play video")
        cta = ("Shall we talk about your production?", "Tell us what you need and we’ll propose how to do it.")
    ln = "".join(f"<li>{x}</li>" for x in lines)
    gl = "".join(f'<figure class="reveal"><div class="photo">{c["pic"](n, alt, "(min-width: 700px) 50vw, 100vw")}</div><figcaption>{cap}</figcaption></figure>' for n, cap, alt in gal)
    return f'''<section class="page-hero has-video on-dark">
 <video autoplay muted loop playsinline preload="metadata" poster="{{P}}assets/video/instalaciones-poster.webp" aria-label="{vid[0]}">
  <source src="{{P}}assets/video/instalaciones.webm" type="video/webm"><source src="{{P}}assets/video/instalaciones.mp4" type="video/mp4"></video>
 <div class="ph-shade" aria-hidden="true"></div>
 <div class="wrap"><span class="eyebrow">{hh[0]}</span><h1>{hh[1]}</h1><p>{hh[2]}</p></div>
 <button class="video-ctrl" type="button" data-pause="{vid[1]}" data-play="{vid[2]}">{vid[1]}</button>
</section>
<section class="stats-band"><div class="wrap">{stats(c)}</div></section>
<section><div class="wrap"><div class="section-head reveal"><h2>{lines_h}</h2></div><ul class="chips">{ln}</ul></div></section>
<section class="section-soft"><div class="wrap"><div class="section-head reveal"><h2>{gal_h}</h2></div><div class="gallery">{gl}</div></div></section>
{cta_band(c, cta[0], cta[1])}'''

def about(c):
    L = c["lang"]
    if L == "es":
        h = page_hero("Quiénes somos", "Una empresa de servicios al servicio de sus clientes", "Numarsi nació en 2011 para responder a la necesidad de muchos fabricantes y distribuidores de pescado de externalizar parte de sus procesos productivos.")
        story = ("Elaboración por encargo", "Ofrecemos servicios de elaboración por encargo (maquila) a quienes necesitan fabricar sus productos. Somos una empresa de servicios que complementa los procesos productivos de sus clientes y forma parte de su cadena de valor. Hoy contamos con dos fábricas que suman 3.500 m² y un equipo de más de 180 personas.")
        diff = ("Valor diferencial", "Lo que nos convierte en un aliado para nuestros clientes.")
        vals_h = "Nuestros compromisos"
        vals = [("handshake","Confianza a través de la calidad","Buscamos la máxima confianza de nuestros clientes con un servicio excelente y un producto que cumple al cien por cien sus necesidades."),
                ("doc","Compromiso","Nuestro compromiso con los clientes es total: cumplimos todo lo acordado."),
                ("lock","Confidencialidad","Mantenemos en privado los detalles y especificaciones de los productos de nuestros clientes."),
                ("chart","Transparencia","Somos totalmente transparentes en cuanto a procesos y controles de producción."),
                ("clock","Especialización y fiabilidad","Ser especialistas nos permite actuar con rapidez y entregar en el plazo acordado.")]
        alt = "Operarios con equipo de protección trabajando en la línea de producción"
        cta = ("Hablemos de tu producción", "Cuéntanos qué necesitas y te proponemos cómo hacerlo.")
    else:
        h = page_hero("About us", "A service company at its clients’ service", "Numarsi was founded in 2011 to meet the need of many fish processors and distributors to outsource part of their production processes.")
        story = ("Contract processing", "We offer contract processing services to companies that need their products made. We are a service company that complements our clients’ production processes and forms part of their value chain. Today we have two factories totalling 3,500 m² and a team of more than 180 people.")
        diff = ("What sets us apart", "What makes us an ally for our clients.")
        vals_h = "Our commitments"
        vals = [("handshake","Trust through quality","We seek our clients’ full trust through excellent service and a product that fully meets their needs."),
                ("doc","Commitment","Our commitment to clients is total: we honour every agreement."),
                ("lock","Confidentiality","We keep the details and specifications of our clients’ products private."),
                ("chart","Transparency","We are fully transparent about processes and production controls."),
                ("clock","Specialisation and reliability","Being specialists lets us act quickly and deliver on the agreed date.")]
        alt = "Operators in protective clothing working on the production line"
        cta = ("Let’s talk about your production", "Tell us what you need and we’ll propose how to do it.")
    vl = "".join(f'<article class="card reveal"><div class="icon">{c["icon"](i)}</div><h3>{a}</h3><p>{b}</p></article>' for i, a, b in vals)
    return f'''{h}
<section><div class="wrap split">
 <div class="reveal"><h2>{story[0]}</h2><p>{story[1]}</p></div>
 <div class="photo reveal">{c["pic"]("equipo-planta", alt, "(min-width: 900px) 40vw, 100vw")}</div>
</div></section>
<section class="section-dark" id="valor-diferencial"><div class="wrap"><div class="section-head reveal"><h2>{diff[0]}</h2><p>{diff[1]}</p></div>{pillars(c)}</div></section>
<section class="section-soft"><div class="wrap"><div class="section-head reveal"><h2>{vals_h}</h2></div><div class="grid g5">{vl}</div></div></section>
{cta_band(c, cta[0], cta[1])}'''

def contact(c):
    t = c["t"]; L = c["lang"]
    if L == "es":
        h = page_hero("Contacto", "Hablemos de tu producción", "Escríbenos o rellena el formulario para pedir información, un presupuesto o muestras. Te respondemos lo antes posible.")
        F = dict(title="Solicitud de información", empresa="Empresa", nombre="Nombre y apellidos", email="Correo electrónico", tel="Teléfono",
                 motivo="Motivo", motivos=["Información general","Presupuesto","Solicitud de muestras","Otro"], elige="Elige una opción",
                 servicio="Servicio de interés", servicios=["Fileteado y pelado","Cefalópodos","Corte","Congelación IQF","Envasado","Varios / producto completo"],
                 producto="Producto", producto_ph="Ej.: merluza, calamar, pota…", volumen="Volumen aproximado", volumen_ph="Ej.: 20 t al año",
                 msg="Mensaje", legal="He leído y acepto la política de privacidad.", send="Enviar solicitud",
                 subject="Solicitud desde la web", ok="Se ha abierto tu programa de correo con la solicitud. Si no se abre, escríbenos a info@numarsi.com.", req="obligatorio")
        info = ("Datos de contacto","Razón social","Dirección","Teléfono","Correo","Cómo llegar")
    else:
        h = page_hero("Contact", "Let’s talk about your production", "Write to us or fill in the form to ask for information, a quote or samples. We’ll get back to you as soon as possible.")
        F = dict(title="Information request", empresa="Company", nombre="Full name", email="Email", tel="Phone",
                 motivo="Reason", motivos=["General information","Quote","Sample request","Other"], elige="Choose an option",
                 servicio="Service of interest", servicios=["Filleting and skinning","Cephalopods","Cutting","IQF freezing","Packing","Several / complete product"],
                 producto="Product", producto_ph="E.g. hake, squid, jumbo squid…", volumen="Approximate volume", volumen_ph="E.g. 20 t per year",
                 msg="Message", legal="I have read and accept the privacy policy.", send="Send request",
                 subject="Website enquiry", ok="Your email app has opened with the request. If it didn’t, write to info@numarsi.com.", req="required")
        info = ("Contact details","Company name","Address","Phone","Email","Get directions")
    labels = json.dumps({"empresa":F["empresa"],"nombre":F["nombre"],"email":F["email"],"telefono":F["tel"],"motivo":F["motivo"],"servicio":F["servicio"],"producto":F["producto"],"volumen":F["volumen"],"mensaje":F["msg"]}, ensure_ascii=False)
    r = f'<span class="req" aria-hidden="true">*</span><span class="visually-hidden"> ({F["req"]})</span>'
    mot = "".join(f"<option>{x}</option>" for x in F["motivos"])
    srv = "".join(f"<option>{x}</option>" for x in F["servicios"])
    legal = PAGES["legal"][L]["file"]
    pol = {"es":"política de privacidad","en":"privacy policy"}[L]
    legal_txt = F["legal"].replace(pol, f'<a href="{legal}#privacidad">{pol}</a>')
    return f'''{h}
<section id="formulario"><div class="wrap split" style="align-items:start">
<form class="form reveal" id="sample-form"
  data-to="{t["email"]}" data-subject="{F["subject"]}" data-ok="{H.escape(F["ok"])}" data-labels='{H.escape(labels)}'>
 <h2>{F["title"]}</h2>
 <div class="row">
  <div class="field"><label for="f-empresa">{F["empresa"]} {r}</label><input id="f-empresa" name="empresa" required autocomplete="organization"></div>
  <div class="field"><label for="f-nombre">{F["nombre"]} {r}</label><input id="f-nombre" name="nombre" required autocomplete="name"></div>
 </div>
 <div class="row">
  <div class="field"><label for="f-email">{F["email"]} {r}</label><input id="f-email" name="email" type="email" required autocomplete="email"></div>
  <div class="field"><label for="f-tel">{F["tel"]}</label><input id="f-tel" name="telefono" type="tel" autocomplete="tel"></div>
 </div>
 <div class="row">
  <div class="field"><label for="f-motivo">{F["motivo"]} {r}</label><select id="f-motivo" name="motivo" required><option value="">{F["elige"]}</option>{mot}</select></div>
  <div class="field"><label for="f-servicio">{F["servicio"]}</label><select id="f-servicio" name="servicio"><option value="">{F["elige"]}</option>{srv}</select></div>
 </div>
 <div class="row">
  <div class="field"><label for="f-producto">{F["producto"]}</label><input id="f-producto" name="producto" placeholder="{F["producto_ph"]}"></div>
  <div class="field"><label for="f-volumen">{F["volumen"]}</label><input id="f-volumen" name="volumen" placeholder="{F["volumen_ph"]}"></div>
 </div>
 <div class="field"><label for="f-msg">{F["msg"]} {r}</label><textarea id="f-msg" name="mensaje" rows="5" required></textarea></div>
 <div class="field"><label class="check"><input type="checkbox" required> <span>{legal_txt} {r}</span></label></div>
 <button class="btn btn-primary" type="submit">{c["icon"]("mail")}{F["send"]}</button>
 <p class="form-msg" id="form-msg" role="status" aria-live="polite"></p>
 <noscript><p class="fine">{ {"es":"Si el formulario no funciona en tu navegador, escríbenos a","en":"If the form doesn’t work in your browser, write to"}[L] } <a href="mailto:{t["email"]}">{t["email"]}</a>.</p></noscript>
</form>
<div class="reveal">
 <div class="contact-box"><h2>{info[0]}</h2><dl>
  <dt>{info[1]}</dt><dd>Nuestro Mar de Siempre, S.L.</dd>
  <dt>{info[2]}</dt><dd>{ADDRESS}</dd>
  <dt>{info[3]}</dt><dd><a href="tel:+34986090189">+34 986 090 189</a></dd>
  <dt>{info[4]}</dt><dd><a href="mailto:{t["email"]}">{t["email"]}</a></dd></dl>
  <div class="btns" style="margin-top:8px"><a class="btn btn-ghost btn-sm" href="{MAPS}" rel="noopener">{c["icon"]("pin")}{info[5]}</a>
  <a class="btn btn-ghost btn-sm" href="{{P}}assets/{t["catalog_file"]}" download>{c["icon"]("download")}{t["cta_catalog"]}</a></div>
 </div>
 <div class="photo" style="margin-top:24px">{c["pic"]("fachada-muelles", {"es":"Fachada de la planta de Numarsi con camiones en los muelles de carga","en":"Numarsi plant façade with lorries at the loading docks"}[L], "(min-width: 900px) 45vw, 100vw")}</div>
</div>
</div></section>'''

def legal(c):
    L = c["lang"]
    if L == "es":
        return page_hero("Información legal", "Aviso legal, privacidad, cookies y Canal Ético", "Información sobre el titular de la web y el tratamiento de tus datos.") + f'''
<section><div class="wrap prose">
<h2 id="aviso">Aviso legal</h2><p>Titular: Nuestro Mar de Siempre, S.L. (Numarsi) · {ADDRESS} · info@numarsi.com · +34 986 090 189.</p>
<p>El acceso a esta web atribuye la condición de usuario e implica la aceptación de este aviso legal. Los contenidos (textos, imágenes, vídeos y logotipos) son propiedad de Numarsi o se usan con autorización, y no pueden reproducirse sin permiso.</p>
<h2 id="privacidad">Política de privacidad</h2><p>Responsable: Nuestro Mar de Siempre, S.L. Finalidad: atender las consultas y solicitudes que nos envíes. Base legal: tu consentimiento y la aplicación de medidas precontractuales. No se ceden datos a terceros salvo obligación legal. Conservamos los datos el tiempo necesario para responder y cumplir las obligaciones legales.</p>
<p>Puedes ejercer tus derechos de acceso, rectificación, supresión, oposición, limitación y portabilidad escribiendo a info@numarsi.com, y reclamar ante la Agencia Española de Protección de Datos.</p>
<p>El formulario de contacto de esta web no guarda datos: prepara un correo en tu propio programa de correo y tú decides si lo envías.</p>
<h2 id="cookies">Política de cookies</h2><p>Esta web no utiliza cookies propias ni de terceros con fines publicitarios o de análisis. Por eso no necesitas aceptar ningún aviso para navegar.</p>
<h2 id="canal-etico">Canal Ético</h2><p>Numarsi dispone de un Canal Ético para comunicar de forma confidencial cualquier posible irregularidad. Las comunicaciones se tratan con total confidencialidad y sin represalias.</p>
</div></section>'''
    return page_hero("Legal information", "Legal notice, privacy, cookies and ethics channel", "Information about the website owner and how your data is handled.") + f'''
<section><div class="wrap prose">
<h2 id="aviso">Legal notice</h2><p>Owner: Nuestro Mar de Siempre, S.L. (Numarsi) · {ADDRESS} (Spain) · info@numarsi.com · +34 986 090 189.</p>
<p>Accessing this website makes you a user and implies acceptance of this legal notice. Its contents (texts, images, videos and logos) belong to Numarsi or are used with permission and may not be reproduced without authorisation.</p>
<h2 id="privacidad">Privacy policy</h2><p>Controller: Nuestro Mar de Siempre, S.L. Purpose: to answer the enquiries and requests you send us. Legal basis: your consent and pre-contractual measures. Data is not shared with third parties unless legally required, and is kept only as long as needed to answer and meet legal obligations.</p>
<p>You can exercise your rights of access, rectification, erasure, objection, restriction and portability by writing to info@numarsi.com, and complain to the Spanish Data Protection Agency.</p>
<p>The contact form on this website does not store data: it prepares an email in your own email app and you decide whether to send it.</p>
<h2 id="cookies">Cookie policy</h2><p>This website does not use first- or third-party cookies for advertising or analytics, so you don’t need to accept any banner to browse.</p>
<h2 id="canal-etico">Ethics channel</h2><p>Numarsi has an ethics channel to report any possible irregularity confidentially. Reports are handled in full confidence and without retaliation.</p>
</div></section>'''

PAGES = {
 "home":        {"es": dict(file="index.html", nav="Inicio", title="Inicio", desc="Numarsi: elaboración por encargo de productos del mar congelados en Pontevedra. Fileteado, cefalópodos, corte, congelación IQF y envasado. No competimos con nuestros clientes.", body=home),
                 "en": dict(file="index.html", nav="Home", title="Home", desc="Numarsi: contract processing of frozen seafood in Pontevedra, Spain. Filleting, cephalopods, cutting, IQF freezing and packing. We never compete with our clients.", body=home)},
 "services":    {"es": dict(file="servicios.html", nav="Servicios", title="Servicios", desc="Fileteado y pelado, limpieza de cefalópodos, corte en diferentes formas, congelación IQF, envasado en varios formatos y servicios adicionales.", body=services),
                 "en": dict(file="services.html", nav="Services", title="Services", desc="Filleting and skinning, cephalopod cleaning, cutting, IQF freezing, packing in several formats and additional services.", body=services)},
 "quality":     {"es": dict(file="calidad.html", nav="Calidad", title="Calidad y certificaciones", desc="Departamento de Calidad con controles en todo el proceso y certificaciones IFS, MSC, ASC y Friend of the Sea.", body=quality),
                 "en": dict(file="quality.html", nav="Quality", title="Quality & certifications", desc="A Quality Department with checks throughout the process and IFS, MSC, ASC and Friend of the Sea certification.", body=quality)},
 "development": {"es": dict(file="mejora-y-desarrollo.html", nav="Mejora y Desarrollo", title="Mejora y Desarrollo", desc="Nuevos productos y procesos, muestras comerciales a medida, diseño de envase y embalaje y proyectos integrales.", body=development),
                 "en": dict(file="product-development.html", nav="Development", title="Product development", desc="New products and processes, tailor-made commercial samples, packaging design and end-to-end projects.", body=development)},
 "facilities":  {"es": dict(file="instalaciones.html", nav="Instalaciones", title="Instalaciones", desc="Dos plantas en Pontevedra con 3.500 m², líneas de fileteado, cefalópodo, corte, congelación IQF y envasado.", body=facilities),
                 "en": dict(file="facilities.html", nav="Facilities", title="Facilities", desc="Two plants in Pontevedra with 3,500 m², filleting, cephalopod, cutting, IQF freezing and packing lines.", body=facilities)},
 "about":       {"es": dict(file="quienes-somos.html", nav="Quiénes somos", title="Quiénes somos", desc="Numarsi nació en 2011 para que fabricantes y distribuidores de pescado externalicen parte de su producción. Más de 180 personas en Pontevedra.", body=about),
                 "en": dict(file="about.html", nav="About us", title="About us", desc="Numarsi was founded in 2011 so fish processors and distributors could outsource part of their production. 180+ people in Pontevedra.", body=about)},
 "contact":     {"es": dict(file="contacto.html", nav="Contacto", title="Contacto", desc="Contacta con Numarsi: información, presupuestos, muestras y visitas a planta. Pontevedra, +34 986 090 189, info@numarsi.com.", body=contact),
                 "en": dict(file="contact.html", nav="Contact", title="Contact", desc="Contact Numarsi for information, quotes, samples and plant visits. Pontevedra, Spain, +34 986 090 189, info@numarsi.com.", body=contact)},
 "legal":       {"es": dict(file="legal.html", nav="Legal", title="Aviso legal, privacidad y Canal Ético", desc="Aviso legal, política de privacidad, política de cookies y Canal Ético de Numarsi.", body=legal),
                 "en": dict(file="legal.html", nav="Legal", title="Legal notice, privacy and ethics channel", desc="Legal notice, privacy policy, cookie policy and ethics channel of Numarsi.", body=legal)},
}
NAV = ["home", "services", "quality", "development", "facilities", "about", "contact"]
