"""Genera la web estática (ES + EN) en docs/.
Uso: python -I tools/build.py [URL_BASE]   p. ej. https://usuario.github.io/conxegal-web/"""
import json, os, shutil, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import T, PAGES, NAV  # textos

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
BASE = (sys.argv[1] if len(sys.argv) > 1 else "https://example.github.io/conxegal-web/").rstrip("/") + "/"
import time
VER = str(int(time.time()))
IMGS = json.load(open(os.path.join(ROOT, "tools", "images.json")))

# Analítica sin cookies (GoatCounter). Preparada pero DESACTIVADA: pon tu código y True para activarla.
GOATCOUNTER_CODE = "numarsi"
GOATCOUNTER_ON = False

ICONS = {
 "fillet": '<path d="M3 12c3-5 9-7 14-5l4-3v16l-4-3c-5 2-11 0-14-5z"/><path d="M8 9.5c1 1.5 1 3.5 0 5M12 8.5c1 2 1 5 0 7"/>',
 "squid": '<path d="M12 2c3 2 4 5 4 9H8c0-4 1-7 4-9z"/><path d="M8 11c0 4-2 6-3 9M10 11c0 4-1 7-1 10M14 11c0 4 1 7 1 10M16 11c0 4 2 6 3 9"/><circle cx="10.5" cy="8" r=".6"/><circle cx="13.5" cy="8" r=".6"/>',
 "cut": '<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M9 6v12M15 6v12M3 12h18"/>',
 "snow": '<path d="M12 2v20M4.9 6.5l14.2 11M19.1 6.5 4.9 17.5"/><path d="m9 3 3 2 3-2M9 21l3-2 3 2M3 9.5l3.5.5L5 13M21 9.5l-3.5.5L19 13M3 14.5l3.5-.5M21 14.5l-3.5-.5"/>',
 "box": '<path d="M3 7l9-4 9 4v10l-9 4-9-4z"/><path d="M3 7l9 4 9-4M12 11v10"/>',
 "lab": '<path d="M9 3h6M10 3v6L4.5 19a1.5 1.5 0 0 0 1.3 2h12.4a1.5 1.5 0 0 0 1.3-2L14 9V3"/><path d="M7 15h10"/>',
 "shield": '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m8.5 12 2.5 2.5 4.5-5"/>',
 "lock": '<rect x="5" y="10" width="14" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "tag": '<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8" r="1.5"/>',
 "factory": '<path d="M3 21V10l6 4V10l6 4V6h6v15z"/><path d="M7 18h2M12 18h2M17 18h2"/>',
 "store": '<path d="M4 9l1.5-5h13L20 9"/><path d="M4 9h16v2a3 3 0 0 1-6 0 3 3 0 0 1-4 0 3 3 0 0 1-6 0z"/><path d="M5 13v8h14v-8"/>',
 "handshake": '<path d="m2 12 4-4 4 2 4-3 4 3 4 2"/><path d="m7 15 3 3 2-1 2 2 3-3M2 12l5 5M22 12l-5 5"/>',
 "doc": '<path d="M6 2h9l5 5v15H6z"/><path d="M14 2v6h6M9 13h8M9 17h8"/>',
 "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
 "pin": '<path d="M12 22s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
 "phone": '<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2z"/>',
 "snowbox": '<rect x="3" y="4" width="18" height="17" rx="2"/><path d="M3 9h18M12 12v6M9.4 13.5l5.2 3M14.6 13.5l-5.2 3"/>',
 "download": '<path d="M12 3v12m-5-5 5 5 5-5M4 21h16"/>',
}
def icon(name, size=None):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{ICONS[name]}</svg>'

# Ilustraciones de formatos de envasado (propias)
PACK = {
 "bag": '<rect x="30" y="18" width="90" height="120" rx="10" fill="#e3f1fa" stroke="#1d4288" stroke-width="4"/><path d="M30 38h90" stroke="#1d4288" stroke-width="4"/><rect x="48" y="58" width="54" height="34" rx="6" fill="#fff" stroke="#199ad6" stroke-width="3"/><text x="75" y="80" text-anchor="middle" font-size="12" font-weight="700" fill="#1d4288" font-family="Inter,Arial">TU MARCA</text><circle cx="60" cy="112" r="7" fill="#199ad6"/><circle cx="78" cy="118" r="7" fill="#199ad6" opacity=".7"/><circle cx="94" cy="110" r="7" fill="#199ad6" opacity=".5"/>',
 "skin": '<rect x="18" y="40" width="114" height="80" rx="8" fill="#fff" stroke="#1d4288" stroke-width="4"/><path d="M34 92c10-30 72-30 82 0z" fill="#f3d9c7" stroke="#c98e6b" stroke-width="3"/><path d="M26 98c16-46 82-46 98 0" fill="none" stroke="#199ad6" stroke-width="3" stroke-dasharray="6 5"/>',
 "vacuum": '<rect x="24" y="30" width="102" height="100" rx="16" fill="#e3f1fa" stroke="#1d4288" stroke-width="4"/><rect x="44" y="56" width="62" height="48" rx="10" fill="#f3d9c7" stroke="#c98e6b" stroke-width="3"/><path d="M24 50l-10-8M126 50l10-8M24 110l-10 8M126 110l10 8" stroke="#199ad6" stroke-width="4" stroke-linecap="round"/>',
 "carton": '<path d="M20 52l55-24 55 24v62l-55 24-55-24z" fill="#fff" stroke="#1d4288" stroke-width="4" stroke-linejoin="round"/><path d="M20 52l55 24 55-24M75 76v62" stroke="#1d4288" stroke-width="4"/><rect x="88" y="88" width="30" height="18" rx="3" fill="#199ad6"/>',
 "bulk": '<path d="M22 60h106l-10 70H32z" fill="#e3f1fa" stroke="#1d4288" stroke-width="4" stroke-linejoin="round"/><g fill="#fff" stroke="#199ad6" stroke-width="3"><circle cx="50" cy="52" r="11"/><circle cx="74" cy="46" r="11"/><circle cx="98" cy="52" r="11"/><circle cx="62" cy="36" r="10"/><circle cx="86" cy="34" r="10"/></g>',
}
def pack_svg(k, label):
    return f'<svg viewBox="0 0 150 150" role="img" aria-label="{html.escape(label)}">{PACK[k]}</svg>'

def picture(name, alt, sizes="(min-width: 900px) 50vw, 100vw", eager=False, cls=""):
    m = IMGS[name]; ws = m["widths"]; big = ws[-1]
    h = round(m["h"] * big / m["w"])
    srcset = ", ".join(f"assets/img/{name}-{w}.webp {w}w" for w in ws)
    load = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    return (f'<img src="{{P}}assets/img/{name}-{ws[min(1,len(ws)-1)]}.webp" srcset="{srcset}" sizes="{sizes}" '
            f'width="{big}" height="{h}" alt="{html.escape(alt)}" {load}{(" class=%s" % cls) if cls else ""}>').replace(
            "assets/img/", "{P}assets/img/").replace("{P}{P}", "{P}")

def ctx(lang):
    t = T[lang]
    return dict(t=t, icon=icon, pack=pack_svg, pic=picture, lang=lang)

def page_url(lang, key):
    fn = PAGES[key][lang]["file"]
    return ("" if lang == "es" else "en/") + fn

def render(lang, key):
    t = T[lang]; pg = PAGES[key][lang]
    P = "" if lang == "es" else "../"
    other = "en" if lang == "es" else "es"
    to_other = ("en/" if lang == "es" else "../") + PAGES[key][other]["file"]
    title = pg["title"]
    full_title = f'{title} | Numarsi' if key != "home" else t["home_title"]
    nav_items = "".join(
        f'<li><a href="{P if lang=="es" else ""}{PAGES[k][lang]["file"]}"{" aria-current=\"page\"" if k==key else ""}>{PAGES[k][lang]["nav"]}</a></li>'
        for k in NAV)
    body = pg["body"](ctx(lang))
    contact_href = PAGES["contact"][lang]["file"]
    gc = ""
    if GOATCOUNTER_ON:
        gc = f'<script data-goatcounter="https://{GOATCOUNTER_CODE}.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>'
    else:
        gc = f'<!-- Analítica sin cookies (GoatCounter) preparada y desactivada. Para activarla: GOATCOUNTER_ON = True en tools/build.py -->'
    canon = BASE + page_url(lang, key)
    alt_es = BASE + page_url("es", key); alt_en = BASE + page_url("en", key)
    out = f'''<!doctype html>
<html lang="{lang}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(pg["desc"])}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#1d4288">
<link rel="alternate" hreflang="es" href="{alt_es}">
<link rel="alternate" hreflang="en" href="{alt_en}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Numarsi">
<meta property="og:title" content="{html.escape(full_title)}">
<meta property="og:description" content="{html.escape(pg["desc"])}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{BASE}assets/img/og-numarsi.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{html.escape(t["og_alt"])}">
<meta property="og:locale" content="{"es_ES" if lang=="es" else "en_GB"}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" sizes="32x32" href="{P}assets/favicon-32.png">
<link rel="apple-touch-icon" href="{P}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"></noscript>
<link rel="stylesheet" href="{P}assets/css/styles.css?v={VER}">
{gc}
</head>
<body>
<a class="skip" href="#main">{t["skip"]}</a>
<header class="site-header">
 <div class="wrap header-in">
  <a class="brand" href="{P if lang=="es" else ""}index.html"><img src="{P}assets/img/numarsi-logo.webp" width="240" height="120" alt="{t["logo_alt"]}"></a>
  <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav"><span class="bars" aria-hidden="true"></span>{t["menu"]}</button>
  <nav id="site-nav" class="site-nav" aria-label="{t["nav_label"]}"><ul>{nav_items}</ul></nav>
  <div class="lang" aria-label="{t["lang_label"]}">
   <a href="{to_other if lang=="en" else pg["file"]}" lang="es" hreflang="es" {"aria-current=\"true\"" if lang=="es" else ""}><span class="visually-hidden">Español </span>ES</a>
   <a href="{to_other if lang=="es" else pg["file"]}" lang="en" hreflang="en" {"aria-current=\"true\"" if lang=="en" else ""}><span class="visually-hidden">English </span>EN</a>
  </div>
  <a class="btn btn-primary btn-sm header-cta" href="{contact_href}#formulario">{t["cta_main"]}</a>
 </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
 <div class="wrap">
  <div class="footer-grid">
   <div class="footer-brand">
    <img src="{P}assets/img/numarsi-logo-blanco.png" width="164" height="100" alt="Numarsi — nuestro mar de siempre" loading="lazy">
    <p>{t["footer_about"]}</p>
   </div>
   <div>
    <h2>{t["footer_nav"]}</h2>
    <ul>
     <li><a href="{PAGES["services"][lang]["file"]}">{PAGES["services"][lang]["nav"]}</a></li>
     <li><a href="{PAGES["quality"][lang]["file"]}">{PAGES["quality"][lang]["nav"]}</a></li>
     <li><a href="{PAGES["facilities"][lang]["file"]}">{PAGES["facilities"][lang]["nav"]}</a></li>
     <li><a href="{PAGES["about"][lang]["file"]}">{PAGES["about"][lang]["nav"]}</a></li>
     <li><a href="{P}assets/{t["catalog_file"]}" download>{t["cta_catalog"]} (PDF)</a></li>
    </ul>
   </div>
   <div>
    <h2>{t["footer_contact"]}</h2>
    <ul>
     <li><a href="mailto:{t["email"]}">{t["email"]}</a></li>
     <li><a href="tel:+34986090189">+34 986 090 189</a></li>
     <li>{t["location"]}</li>
     <li><a href="https://www.linkedin.com/company/numarsi/" rel="noopener">{t["linkedin"]}</a></li>
    </ul>
   </div>
  </div>
  <p class="copy">© 2026 Nuestro Mar de Siempre, S.L. · <a href="{PAGES["legal"][lang]["file"]}#aviso">{t["legal"]}</a> · <a href="{PAGES["legal"][lang]["file"]}#privacidad">{t["privacy"]}</a> · <a href="{PAGES["legal"][lang]["file"]}#cookies">{t["cookies"]}</a> · <a href="{PAGES["legal"][lang]["file"]}#canal-etico">{t["ethics"]}</a></p>
  <p class="copy academic-note">{t["academic"]}</p>
 </div>
</footer>
<script src="{P}assets/js/main.js?v={VER}" defer></script>
</body>
</html>
'''
    # rutas relativas: {P} en imágenes/enlaces generados por el contenido
    out = out.replace("{P}", P)
    path = os.path.join(DOCS, page_url(lang, key))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(out)

def main():
    os.makedirs(os.path.join(DOCS, "assets", "css"), exist_ok=True)
    os.makedirs(os.path.join(DOCS, "assets", "js"), exist_ok=True)
    shutil.copy(os.path.join(ROOT, "src", "styles.css"), os.path.join(DOCS, "assets", "css", "styles.css"))
    shutil.copy(os.path.join(ROOT, "src", "main.js"), os.path.join(DOCS, "assets", "js", "main.js"))
    for lang in ("es", "en"):
        for key in PAGES:
            render(lang, key)
    open(os.path.join(DOCS, "robots.txt"), "w").write("# Propuesta académica: no indexar\nUser-agent: *\nDisallow: /\n")
    open(os.path.join(DOCS, ".nojekyll"), "w").write("")
    print("OK ->", DOCS, "base:", BASE)

if __name__ == "__main__":
    main()
