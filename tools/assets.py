"""Prepara imágenes (WebP responsive), logos, vídeo de cabecera e imagen Open Graph.
Uso: python -I tools/assets.py  (desde la carpeta conxegal-web)"""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_origen")
OUT = os.path.join(ROOT, "docs", "assets")
IMG = os.path.join(OUT, "img")
VID = os.path.join(OUT, "video")
os.makedirs(IMG, exist_ok=True); os.makedirs(VID, exist_ok=True)

# nombre: (archivo origen, recorte (x0,y0,x1,y1) o None)
PHOTOS = {
    "linea-corte":     ("frames/f_6.2.jpg", None),
    "web-filete":      ("web/fotos/2023_10_numarsi_servicios_02.jpg", None),
    "web-calamar":     ("web/fotos/2024_03_numarsi_servicios_03-1.jpg", None),
    "web-calamar-bandeja": ("web/fotos/2023_09_numarsi_home_servicios_02.jpg", None),
    "web-sierras":     ("web/fotos/2023_10_numarsi_servicios_04.jpg", None),
    "web-iqf":         ("web/fotos/2023_10_numarsi_servicios_05.jpg", None),
    "web-barquetas":   ("web/fotos/2023_09_numarsi_home_servicios_03.jpg", None),
    "web-langostinos": ("web/fotos/2024_02_numarsi_servicios_06_montaje_ALB.jpg", None),
    "web-porcionado":  ("web/fotos/2023_09_numarsi_home_servicios.jpg", None),
    "web-linea-calamar": ("web/fotos/2024_02_numarsi_servicios_01_montaje_ALB.jpg", None),
    "web-embalaje":    ("web/fotos/2024_03_numarsi_home_calidad_01.jpg", None),
    "web-control":     ("web/fotos/2023_09_numarsi_sobre_valor_diferencial_01.jpg", None),
    "web-edificio":    ("web/fotos/2023_10_numarsi_contacto.jpg", None),
    "web-fachada":     ("web/fotos/2024_03_numarsi_instalaciones_02-1.jpg", None),
    "web-filete-mano": ("web/fotos/2023_09_numarsi_home_valor_diferencial.jpg", None),
    "linea-sierras":   ("frames/f_1.9.jpg", (90, 0, 1920, 1030)),
    "pescado-congelado":("frames/f_4.3.jpg", None),
    "maquina-envasado":("frames/f_7.6.jpg", None),
    "puestos-preparacion":("frames/f_8.6.jpg", None),
    "linea-envasado":  ("frames/f_2.6.jpg", None),
    "puestos-limpieza":("frames/f_9.6.jpg", None),
    "planta-aerea":    ("frames/f_15.4.jpg", None),
    "fachada-muelles": ("frames/f_12.4.jpg", None),
    "cartel-numarsi":  ("frames/f_16.6.jpg", None),
    "equipo-planta":   ("numarsi_al_servicio_1a3c7a.jpg", (83, 183, 540, 660)),
    "control-calidad": ("numarsi_socio_1a3c7a.jpg", (83, 263, 540, 742)),
}
WIDTHS = [480, 960, 1440]
meta = {}
for name, (f, crop) in PHOTOS.items():
    im = Image.open(os.path.join(SRC, f)).convert("RGB")
    if crop: im = im.crop(crop)
    ws = [w for w in WIDTHS if w < im.width] + [min(im.width, WIDTHS[-1])]
    ws = sorted(set(ws))
    for w in ws:
        h = round(im.height * w / im.width)
        im.resize((w, h), Image.LANCZOS).save(os.path.join(IMG, f"{name}-{w}.webp"), "WEBP", quality=78, method=6)
    meta[name] = {"w": im.width, "h": im.height, "widths": ws}

# Logos originales (fondo blanco → se usan sobre blanco; versión blanca con transparencia para el pie)
L = os.path.join(SRC, "logos")
Image.open(os.path.join(L, "numarsi_sticky_retina_logo.png")).convert("RGB").save(os.path.join(IMG, "numarsi-logo.webp"), "WEBP", quality=92)
Image.open(os.path.join(L, "numarsi_sticky_retina_logo.png")).convert("RGB").save(os.path.join(IMG, "numarsi-logo.png"), optimize=True)
Image.open(os.path.join(L, "numarsi_logo_white-01.png")).save(os.path.join(IMG, "numarsi-logo-blanco.png"), optimize=True)
Image.open(os.path.join(L, "apple-touch-icon.png")).save(os.path.join(OUT, "apple-touch-icon.png"))
Image.open(os.path.join(L, "favicon-32x32-1.png")).convert("RGBA").save(os.path.join(OUT, "favicon-32.png"))

# Imagen Open Graph 1200x630
og = Image.new("RGB", (1200, 630), "#0e2350")
d = ImageDraw.Draw(og)
bg = Image.open(os.path.join(SRC, "frames/f_6.2.jpg")).convert("RGB").resize((1120, 630))
og.paste(bg, (480, 0))
grad = Image.new("L", (1200, 1))
for x in range(1200): grad.putpixel((x, 0), 255 if x < 520 else max(0, int(255 - (x - 520) * 0.55)))
og.paste(Image.new("RGB", (1200, 630), "#0e2350"), (0, 0), grad.resize((1200, 630)))
logo = Image.open(os.path.join(L, "numarsi_logo_white-01.png")).convert("RGBA")
logo = logo.resize((246, 150), Image.LANCZOS)
og.paste(logo, (70, 60), logo)
try:
    fb = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 58)
    fr = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 30)
except OSError:
    fb = fr = ImageFont.load_default()
d.text((70, 270), "Especialistas en|la elaboración de|productos del mar".replace("|", chr(10)), font=fb, fill="white", spacing=8)
d.text((70, 520), "Elaboración por encargo · Pontevedra", font=fr, fill="#8fd3f5")
og.save(os.path.join(IMG, "og-numarsi.jpg"), quality=86)

# Vídeo de cabecera de Instalaciones: 12–18 s (fachada, vista aérea, cartel), sin audio
src_v = os.path.join(SRC, "NUEVO_NUMARSI_INSTALACIONES_Comp.mp4")
common = ["ffmpeg", "-v", "error", "-y", "-ss", "12", "-t", "6", "-i", src_v, "-an", "-vf", "scale=1280:-2,fps=25"]
subprocess.run(common + ["-c:v", "libx264", "-crf", "28", "-preset", "slow", "-pix_fmt", "yuv420p", "-movflags", "+faststart", os.path.join(VID, "instalaciones.mp4")], check=True)
subprocess.run(common + ["-c:v", "libvpx-vp9", "-crf", "38", "-b:v", "0", "-row-mt", "1", os.path.join(VID, "instalaciones.webm")], check=True)
Image.open(os.path.join(SRC, "frames/f_12.4.jpg")).convert("RGB").resize((1280, 720)).save(os.path.join(VID, "instalaciones-poster.webp"), "WEBP", quality=72)

json.dump(meta, open(os.path.join(ROOT, "tools", "images.json"), "w"), indent=1)
print(json.dumps(meta))
for f in sorted(os.listdir(VID)): print(f, os.path.getsize(os.path.join(VID, f)) // 1024, "KB")
