"""Catálogo PDF de 3 páginas (ES y EN) con servicios y formatos."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from content import SERV, PACKS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "docs", "assets", "img")
SRC = os.path.join(ROOT, "_origen")
pdfmetrics.registerFont(TTFont("S", "C:/Windows/Fonts/segoeui.ttf"))
pdfmetrics.registerFont(TTFont("SB", "C:/Windows/Fonts/segoeuib.ttf"))
NAVY = (14/255, 35/255, 80/255); BLUE = (29/255, 66/255, 136/255); SKY = (25/255, 154/255, 214/255)
INK = (.09, .14, .23); MUTED = (.29, .35, .44); SOFT = (.95, .97, .98)
W, H = A4; M = 42

TX = {
 "es": dict(file="numarsi-catalogo.pdf", sub="Catálogo de servicios 2026", claim="Especialistas en la elaboración de productos del mar",
   intro="Elaboramos por encargo productos del mar congelados. No comercializamos producto propio: solo vendemos servicios, así que nunca competimos con nuestros clientes.",
   who=[("No comercializamos","Solo vendemos servicios: no competimos con nuestros clientes."),("Especialistas","Todo nuestro tiempo, dedicado a las necesidades de producción de cada cliente."),("Calidad","Departamento de Calidad con controles en todo el proceso.")],
   facts=[("2011","fundación"),("2","plantas · 3.500 m²"),("+180","personas"),("4 t/h","congelación IQF")],
   s_title="Servicios", f_title="Formatos de envasado", p_title="Cómo trabajamos",
   steps=["Recepción y control de la materia prima","Proceso a medida: fileteado, limpieza o corte","Congelación IQF y glaseo","Envasado en el tamaño y formato elegidos","Control y liberación por Calidad","Almacenamiento en frío y expedición"],
   c_title="Calidad certificada", certs="IFS Food · MSC · ASC · Friend of the Sea", conf="Servicios adicionales: almacenamiento en frío, escandallos y muestras comerciales a medida. Confidencialidad sobre los productos y especificaciones de cada cliente.",
   cta="Hablemos de tu producción", contact="info@numarsi.com · +34 986 090 189 · O Campiño, Pontevedra",
   foot="Nuestro Mar de Siempre, S.L. · www.numarsi.com", page="Página"),
 "en": dict(file="numarsi-catalogue-en.pdf", sub="Services catalogue 2026", claim="Specialists in seafood processing",
   intro="We carry out contract processing of frozen seafood. We don’t sell our own products, only services, so we never compete with our clients.",
   who=[("We don’t sell products","We only sell services: we never compete with our clients."),("Specialists","All our time devoted to each client’s production needs."),("Quality","A Quality Department checking the whole process.")],
   facts=[("2011","founded"),("2","plants · 3,500 m²"),("180+","people"),("4 t/h","IQF freezing")],
   s_title="Services", f_title="Packing formats", p_title="How we work",
   steps=["Raw material intake and checks","Tailor-made processing: filleting, cleaning or cutting","IQF freezing and glazing","Packing in the chosen size and format","Quality checks and release","Cold storage and dispatch"],
   c_title="Certified quality", certs="IFS Food · MSC · ASC · Friend of the Sea", conf="Additional services: cold storage, yield analysis and tailor-made commercial samples. Confidentiality for each client’s products and specifications.",
   cta="Let’s talk about your production", contact="info@numarsi.com · +34 986 090 189 · Pontevedra, Galicia, Spain",
   foot="Nuestro Mar de Siempre, S.L. · www.numarsi.com", page="Page"),
}

def wrap(c, text, x, y, w, font="S", size=10, lead=14, color=INK):
    c.setFont(font, size); c.setFillColorRGB(*color)
    words = text.split(); line = ""
    for wd in words:
        t = (line + " " + wd).strip()
        if pdfmetrics.stringWidth(t, font, size) > w:
            c.drawString(x, y, line); y -= lead; line = wd
        else: line = t
    if line: c.drawString(x, y, line); y -= lead
    return y

def footer(c, t, n):
    c.setFillColorRGB(*MUTED); c.setFont("S", 8)
    c.drawString(M, 24, t["foot"]); c.drawRightString(W - M, 24, f'{t["page"]} {n}/3')

def photo(c, name, x, y, w, h):
    from PIL import Image as PI
    src = os.path.join(IMG, f"{name}-960.webp")
    if not os.path.exists(src): src = os.path.join(IMG, f"{name}-457.webp")
    jpg = os.path.join(ROOT, "tools", "_tmp_" + name + ".jpg")
    PI.open(src).convert("RGB").save(jpg, "JPEG", quality=78)
    im = ImageReader(jpg)
    iw, ih = im.getSize(); s = max(w / iw, h / ih)
    p = c.beginPath(); p.roundRect(x, y, w, h, 8); c.saveState(); c.clipPath(p, stroke=0)
    c.drawImage(jpg, x + (w - iw * s) / 2, y + (h - ih * s) / 2, iw * s, ih * s); c.restoreState()

def build(lang):
    t = TX[lang]; out = os.path.join(ROOT, "docs", "assets", t["file"])
    c = canvas.Canvas(out, pagesize=A4)
    c.setTitle(f'Numarsi — {t["sub"]}'); c.setAuthor("Numarsi"); c.setSubject(t["claim"])
    # ---- Página 1: portada
    c.setFillColorRGB(*NAVY); c.rect(0, H - 430, W, 430, stroke=0, fill=1)
    photo(c, "linea-corte", W * 0.6, H - 400, W * 0.4 - M, 330)
    c.drawImage(os.path.join(IMG, "numarsi-logo-blanco.png"), M, H - 140, 164, 100, mask="auto")
    c.setFillColorRGB(.56, .83, .96); c.setFont("SB", 10); c.drawString(M, H - 170, t["sub"].upper())
    y = H - 205
    for ln in t["claim"].replace(", ", ",|").replace(" en la ", "| en la ").replace(" elaboración de", " elaboración|de").replace(" in seafood", "|in seafood").split("|"):
        c.setFillColorRGB(1, 1, 1); c.setFont("SB", 24); c.drawString(M, y, ln.strip()); y -= 30
    wrap(c, t["intro"], M, y - 10, W * 0.6 - M - 30, size=10.5, lead=15, color=(.85, .9, .96))
    y = H - 470
    for i, (a, b) in enumerate(t["who"]):
        x = M + i * ((W - 2 * M) / 3)
        c.setFillColorRGB(*SOFT); c.roundRect(x, y - 92, (W - 2 * M) / 3 - 12, 92, 8, stroke=0, fill=1)
        c.setFillColorRGB(*SKY); c.rect(x, y - 4, 40, 4, stroke=0, fill=1)
        c.setFillColorRGB(*BLUE); c.setFont("SB", 11.5); c.drawString(x + 12, y - 26, a)
        wrap(c, b, x + 12, y - 46, (W - 2 * M) / 3 - 36, size=10, lead=14, color=INK)
    y -= 128
    for i, (a, b) in enumerate(t["facts"]):
        x = M + i * ((W - 2 * M) / 4)
        c.setFillColorRGB(*NAVY); c.setFont("SB", 26); c.drawString(x, y, a)
        c.setFillColorRGB(*MUTED); c.setFont("S", 10); c.drawString(x, y - 16, b)
    photo(c, "linea-envasado", M, 50, (W - 2 * M) / 2 - 6, 150)
    photo(c, "planta-aerea", W / 2 + 6, 50, (W - 2 * M) / 2 - 6, 150)
    footer(c, t, 1); c.showPage()
    # ---- Página 2: servicios + formatos
    c.setFillColorRGB(*NAVY); c.setFont("SB", 22); c.drawString(M, H - 70, t["s_title"])
    c.setFillColorRGB(*SKY); c.rect(M, H - 82, 50, 3, stroke=0, fill=1)
    y = H - 110
    for ic, anchor, title, img, alt, lead, items in SERV[lang]:
        c.setFillColorRGB(*BLUE); c.setFont("SB", 12.5); c.drawString(M, y, title)
        y2 = wrap(c, lead, M, y - 17, W - 2 * M, size=10, lead=13.5, color=MUTED)
        y = wrap(c, "  ·  ".join(items), M, y2 - 2, W - 2 * M, size=9.5, lead=13, color=INK) - 16
    y -= 4
    c.setFillColorRGB(*NAVY); c.setFont("SB", 18); c.drawString(M, y, t["f_title"]); y -= 18
    bw = (W - 2 * M) / 5
    for i, (k, n, d) in enumerate(PACKS[lang]):
        x = M + i * bw
        c.setFillColorRGB(*SOFT); c.roundRect(x, y - 124, bw - 8, 124, 8, stroke=0, fill=1)
        c.setFillColorRGB(*SKY); c.circle(x + 20, y - 22, 8, stroke=0, fill=1)
        c.setFillColorRGB(*NAVY); c.setFont("SB", 10.5); c.drawString(x + 10, y - 48, n)
        wrap(c, d, x + 10, y - 64, bw - 26, size=8.6, lead=11.5, color=MUTED)
    photo(c, "linea-corte", M, 50, W - 2 * M, y - 140 - 50)
    footer(c, t, 2); c.showPage()
    # ---- Página 3: proceso cefalópodo, calidad, contacto
    c.setFillColorRGB(*NAVY); c.setFont("SB", 22); c.drawString(M, H - 70, t["p_title"])
    c.setFillColorRGB(*SKY); c.rect(M, H - 82, 50, 3, stroke=0, fill=1)
    y = H - 115
    for i, s in enumerate(t["steps"], 1):
        c.setFillColorRGB(*NAVY); c.circle(M + 12, y + 4, 12, stroke=0, fill=1)
        c.setFillColorRGB(1, 1, 1); c.setFont("SB", 11); c.drawCentredString(M + 12, y, str(i))
        c.setFillColorRGB(*INK); c.setFont("S", 11.5); c.drawString(M + 34, y, s)
        y -= 34
    photo(c, "puestos-limpieza", W / 2 + 20, H - 330, W / 2 - M - 20, 220)
    y -= 10
    c.setFillColorRGB(*SOFT); c.roundRect(M, y - 120, W - 2 * M, 120, 10, stroke=0, fill=1)
    c.setFillColorRGB(*NAVY); c.setFont("SB", 15); c.drawString(M + 18, y - 30, t["c_title"])
    c.setFillColorRGB(*BLUE); c.setFont("SB", 12); c.drawString(M + 18, y - 52, t["certs"])
    wrap(c, t["conf"], M + 18, y - 76, W - 2 * M - 36, size=10, lead=14, color=MUTED)
    y -= 160
    c.setFillColorRGB(*NAVY); c.roundRect(M, y - 130, W - 2 * M, 130, 12, stroke=0, fill=1)
    c.setFillColorRGB(1, 1, 1); c.setFont("SB", 22); c.drawString(M + 24, y - 48, t["cta"])
    c.setFillColorRGB(.56, .83, .96); c.setFont("S", 12); c.drawString(M + 24, y - 76, t["contact"])
    c.drawImage(os.path.join(IMG, "numarsi-logo-blanco.png"), W - M - 130, y - 112, 107, 65, mask="auto")
    footer(c, t, 3); c.showPage(); c.save()
    print("PDF:", out, os.path.getsize(out) // 1024, "KB")

for L in ("es", "en"): build(L)
