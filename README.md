# Numarsi — propuesta académica de rediseño web

Proyecto académico para un plan de comunicación. **No es la web oficial de Numarsi.**

- Web estática (HTML, CSS y JS sin frameworks) publicada desde `docs/` con GitHub Pages.
- Español en la raíz y la versión en inglés en `docs/en/`.
- Configurada con `noindex, nofollow` y un `robots.txt` que bloquea los buscadores.

## Regenerar
```
python tools/assets.py     # imágenes WebP, vídeo de cabecera e imagen Open Graph (requiere _origen/)
python tools/build.py https://sergiofergaone-beep.github.io/numarsi-web/
python tools/catalog.py    # catálogos PDF
```

Analítica: GoatCounter queda preparado pero desactivado (`GOATCOUNTER_ON` en `tools/build.py`).
