"""Genera los SVG pixel-art retro del perfil de GitHub de Darwin.
Todo el texto se dibuja como pixeles (rects) para que se vea igual en GitHub,
sin depender de fuentes externas."""
import os

OUT = os.path.join(os.path.dirname(__file__), "assets")

# Paleta retro
BG = "#5ccbc5"
PANEL = "#1f5a5f"
PANEL2 = "#15434a"
GOLD = "#ff6fb5"
GOLD_D = "#8c1f5e"
RED = "#c8186a"
CREAM = "#fff4ee"
MUTED = "#b9ece6"
GREEN = "#a6f7e4"
CYAN = "#ffc2e0"
INK = "#1e1533"
PURPLE = "#5a2b8a"

# Fuente bitmap 5x7
F = {
 'A': ["01110","10001","10001","11111","10001","10001","10001"],
 'B': ["11110","10001","10001","11110","10001","10001","11110"],
 'C': ["01110","10001","10000","10000","10000","10001","01110"],
 'D': ["11110","10001","10001","10001","10001","10001","11110"],
 'E': ["11111","10000","10000","11110","10000","10000","11111"],
 'F': ["11111","10000","10000","11110","10000","10000","10000"],
 'G': ["01110","10001","10000","10111","10001","10001","01111"],
 'H': ["10001","10001","10001","11111","10001","10001","10001"],
 'I': ["01110","00100","00100","00100","00100","00100","01110"],
 'J': ["00111","00010","00010","00010","00010","10010","01100"],
 'K': ["10001","10010","10100","11000","10100","10010","10001"],
 'L': ["10000","10000","10000","10000","10000","10000","11111"],
 'M': ["10001","11011","10101","10101","10001","10001","10001"],
 'N': ["10001","10001","11001","10101","10011","10001","10001"],
 'O': ["01110","10001","10001","10001","10001","10001","01110"],
 'P': ["11110","10001","10001","11110","10000","10000","10000"],
 'Q': ["01110","10001","10001","10001","10101","10010","01101"],
 'R': ["11110","10001","10001","11110","10100","10010","10001"],
 'S': ["01111","10000","10000","01110","00001","00001","11110"],
 'T': ["11111","00100","00100","00100","00100","00100","00100"],
 'U': ["10001","10001","10001","10001","10001","10001","01110"],
 'V': ["10001","10001","10001","10001","10001","01010","00100"],
 'W': ["10001","10001","10001","10101","10101","10101","01010"],
 'X': ["10001","10001","01010","00100","01010","10001","10001"],
 'Y': ["10001","10001","01010","00100","00100","00100","00100"],
 'Z': ["11111","00001","00010","00100","01000","10000","11111"],
 '0': ["01110","10001","10011","10101","11001","10001","01110"],
 '1': ["00100","01100","00100","00100","00100","00100","01110"],
 '2': ["01110","10001","00001","00010","00100","01000","11111"],
 '3': ["11111","00010","00100","00010","00001","10001","01110"],
 '4': ["00010","00110","01010","10010","11111","00010","00010"],
 '5': ["11111","10000","11110","00001","00001","10001","01110"],
 '6': ["00110","01000","10000","11110","10001","10001","01110"],
 '7': ["11111","00001","00010","00100","01000","01000","01000"],
 '8': ["01110","10001","10001","01110","10001","10001","01110"],
 '9': ["01110","10001","10001","01111","00001","00010","01100"],
 ' ': ["00000"]*7,
 '.': ["00000","00000","00000","00000","00000","01100","01100"],
 ',': ["00000","00000","00000","00000","01100","00100","01000"],
 ':': ["00000","01100","01100","00000","01100","01100","00000"],
 '-': ["00000","00000","00000","11111","00000","00000","00000"],
 '/': ["00001","00010","00010","00100","01000","01000","10000"],
 '!': ["00100","00100","00100","00100","00100","00000","00100"],
 '?': ["01110","10001","00001","00010","00100","00000","00100"],
 '+': ["00000","00100","00100","11111","00100","00100","00000"],
 '>': ["01000","00100","00010","00001","00010","00100","01000"],
 '<': ["00010","00100","01000","10000","01000","00100","00010"],
 '#': ["01010","01010","11111","01010","11111","01010","01010"],
 '(': ["00010","00100","01000","01000","01000","00100","00010"],
 ')': ["01000","00100","00010","00010","00010","00100","01000"],
 '·': ["00000","00000","00000","01100","01100","00000","00000"],
 '★': ["00100","00100","11111","01110","01110","11011","10001"],
  '%': ["11001","11010","00010","00100","01000","01011","10011"],
 '_': ["00000","00000","00000","00000","00000","00000","11111"],
 '|': ["00100","00100","00100","00100","00100","00100","00100"],
}
ACC = {'Á':'A','É':'E','Í':'I','Ó':'O','Ú':'U'}


def text_pixels(s, x, y, px):
    """Devuelve lista de (x, y) de pixeles y el ancho total."""
    pts = []
    cx = x
    for ch in s.upper():
        base = ch
        accent = None
        if ch in ACC:
            base, accent = ACC[ch], 'acute'
        elif ch == 'Ñ':
            base, accent = 'N', 'tilde'
        g = F.get(base, F['?'])
        for r, row in enumerate(g):
            for c, v in enumerate(row):
                if v == '1':
                    pts.append((cx + c * px, y + r * px))
        if accent == 'acute':
            pts += [(cx + 3 * px, y - 2 * px), (cx + 2 * px, y - px)]
        elif accent == 'tilde':
            pts += [(cx + 1 * px, y - 2 * px), (cx + 2 * px, y - 2 * px), (cx + 3 * px, y - px), (cx + 4 * px, y - 2 * px)]
        cx += 6 * px
    return pts, cx - x - px


def path(pts, px):
    return "".join(f"M{x} {y}h{px}v{px}h-{px}z" for x, y in pts)


def text(s, x, y, px, fill, shadow=None, anchor="start"):
    pts, w = text_pixels(s, 0, 0, px)
    if anchor == "middle":
        x = x - w // 2
    elif anchor == "end":
        x = x - w
    out = ""
    if shadow:
        sp = [(a + x + px, b + y + px) for a, b in pts]
        out += f'<path fill="{shadow}" d="{path(sp, px)}"/>'
    p = [(a + x, b + y) for a, b in pts]
    out += f'<path fill="{fill}" d="{path(p, px)}"/>'
    return out


def width(s, px):
    return text_pixels(s, 0, 0, px)[1]


def sprite(rows, x, y, px, colors):
    out = ""
    for key, col in colors.items():
        pts = [(x + c * px, y + r * px) for r, row in enumerate(rows) for c, v in enumerate(row) if v == key]
        if pts:
            out += f'<path fill="{col}" d="{path(pts, px)}"/>'
    return out

# Sprites originales
CROWN = [
 "1...1...1",
 "11.111.11",
 "111111111",
 "121131121",
 "111111111",
 "333333333",
]
TROPHY = [
 "11111111",
 "1.1111.1",
 "1.1111.1",
 ".111111.",
 "..1111..",
 "...11...",
 "..2222..",
 ".222222.",
]
SWORD = [
 "......11",
 ".....131",
 "....131.",
 "2..131..",
 ".2131...",
 "..22....",
 ".2.2....",
 "2.......",
]
CHEST = [
 ".222222.",
 "21111112",
 "21111112",
 "22233222",
 "21131112",
 "21111112",
 "22222222",
]
BUTTER = [
 "11.....11",
 "121...121",
 "1221.1221",
 "122131221",
 ".1213121.",
 "..12312..",
 ".1213121.",
 "1221.1221",
 ".11...11.",
]
CTR = {'1': GOLD, '2': RED, '3': GOLD_D}


def defs(w, h):
    return f'''<defs>
<pattern id="dither" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="2" height="2" fill="#ffffff" opacity=".05"/><rect x="2" y="2" width="2" height="2" fill="#ffffff" opacity=".05"/></pattern>
<pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="2" fill="#000" opacity=".10"/></pattern>
</defs>
<style>@keyframes b{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}.blink{{animation:b 1.1s steps(1) infinite}}
@keyframes f{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-4px)}}}}.float{{animation:f 2.4s steps(2) infinite}}</style>'''


def frame(w, h, inner):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" shape-rendering="crispEdges">'
            + defs(w, h)
            + f'<rect width="{w}" height="{h}" fill="{BG}"/><rect width="{w}" height="{h}" fill="url(#dither)"/>'
            + f'<rect x="4" y="4" width="{w-8}" height="{h-8}" fill="none" stroke="{INK}" stroke-width="4"/>'
            + f'<rect x="12" y="12" width="{w-24}" height="{h-24}" fill="none" stroke="{RED}" stroke-width="4"/>'
            + inner
            + f'<rect width="{w}" height="{h}" fill="url(#scan)"/></svg>')


def title_bar(w, label, y=28):
    tw = width(label, 4)
    x = (w - tw) // 2
    return (f'<rect x="{x-20}" y="{y-8}" width="{tw+40}" height="44" fill="{RED}"/>'
            f'<rect x="{x-20}" y="{y+28}" width="{tw+40}" height="8" fill="#6e1449"/>'
            + text(label, w // 2, y + 4, 4, CREAM, shadow="#4a0c30", anchor="middle"))


def banner():
    w, h = 900, 310
    s = ""
    # estrellas pixel de fondo
    import random
    random.seed(7)
    for _ in range(70):
        x, y = random.randrange(20, w - 20, 4), random.randrange(20, h - 20, 4)
        s += f'<rect x="{x}" y="{y}" width="4" height="4" fill="{MUTED}" opacity="{random.choice([.3,.5,.8])}"/>'
    s += f'<g class="float">{sprite(CROWN, 414, 34, 8, {"1": GOLD, "2": RED, "3": GOLD_D})}</g>'
    s += text("DARWIN MENDOZA", w // 2, 110, 9, GOLD, shadow=RED, anchor="middle")
    s += text("DESARROLLADOR DE SOFTWARE JUNIOR", w // 2, 192, 4, CREAM, anchor="middle")
    s += text("PHP · LARAVEL · MYSQL · JAVASCRIPT", w // 2, 232, 3, CYAN, anchor="middle")
    s += f'<g class="blink">{text("> PRESS START  ·  BOGOTÁ, CO", w // 2, 264, 3, MUTED, anchor="middle")}</g>'
    return frame(w, h, s)


LOGROS = [
    ("ABR 2026", "PRIMER TRABAJO EN TI", "INGRESÓ COMO PRACTICANTE SENA", "ORGANIZACIÓN CÁRDENAS"),
    ("2026", "LEVEL UP: AUXILIAR DE TI", "DE PRACTICANTE A AUXILIAR", "DE TECNOLOGÍA"),
    ("OCT 2026", "TECNÓLOGO ADSO", "GRADUADO DEL SENA EN ANÁLISIS", "Y DESARROLLO DE SOFTWARE"),
    ("2026", "NUEVO MUNDO: INGENIERÍA", "1ER SEMESTRE INGENIERÍA DE", "SOFTWARE · U. MANUELA BELTRÁN"),
    ("SENA", "PROYECTO SCORD", "SISTEMA DE RENDIMIENTO DEPORTIVO", "EQUIPO DE 4 DESARROLLADORES"),
    ("SHOPIFY", "TIENDA JS KIRIOS", "TEMA PERSONALIZADO + PAGO", "CONTRAENTREGA Y PEDIDOS"),
]


def logros():
    w = 900
    rowh = 112
    top = 96
    h = top + rowh * len(LOGROS) + 30
    s = title_bar(w, "LOGROS DESBLOQUEADOS")
    for i, (tag, name, l1, l2) in enumerate(LOGROS):
        y = top + i * rowh
        s += f'<rect x="40" y="{y}" width="{w-80}" height="{rowh-14}" fill="{PANEL}"/>'
        s += f'<rect x="40" y="{y+rowh-22}" width="{w-80}" height="8" fill="{PANEL2}"/>'
        s += f'<rect x="56" y="{y+14}" width="64" height="62" fill="{BG}"/>'
        s += sprite(TROPHY, 64, y + 20, 6, {"1": GOLD, "2": GOLD_D})
        s += text(f"#{i+1:02d}", 88, y + 64, 1, MUTED, anchor="middle") if False else ""
        s += text(name, 140, y + 14, 4, GOLD, shadow="#3d0d29")
        s += text(l1, 140, y + 52, 2, CREAM)
        s += text(l2, 140, y + 74, 2, CREAM)
        s += text(tag, w - 60, y + 14, 3, CYAN, anchor="end")
        s += text("100%", w - 60, y + 60, 2, GREEN, anchor="end")
    return frame(w, h, s)


INV = [
    ("BACKEND", ["PHP", "LARAVEL", "NODE.JS", "APIS REST"], RED),
    ("FRONTEND", ["HTML5", "CSS3", "BOOTSTRAP", "JAVASCRIPT"], PURPLE),
    ("DATOS", ["MYSQL", "SQL", "PHPMYADMIN"], GOLD),
    ("MÓVIL", ["FLUTTER", "DART"], GOLD_D),
    ("HERRAMIENTAS", ["GIT", "GITHUB", "VS CODE", "SCRUM"], INK),
]


def inventario():
    w = 900
    top = 100
    rowh = 74
    h = top + rowh * len(INV) + 30
    s = title_bar(w, "INVENTARIO")
    for i, (cat, items, col) in enumerate(INV):
        y = top + i * rowh
        s += sprite(CHEST, 44, y + 6, 5, {"1": GOLD_D, "2": col, "3": GOLD})
        s += text(cat, 96, y + 14, 3, INK)
        x = 340
        for it in items:
            tw = width(it, 2)
            s += f'<rect x="{x}" y="{y+4}" width="{tw+24}" height="38" fill="{PANEL}"/>'
            s += f'<rect x="{x}" y="{y+42}" width="{tw+24}" height="6" fill="{PANEL2}"/>'
            s += f'<rect x="{x}" y="{y+4}" width="4" height="38" fill="{col}"/>'
            s += text(it, x + 14, y + 16, 2, CREAM)
            x += tw + 36
    return frame(w, h, s)


MISIONES = [
    ("SCORD", "COMPLETADA", GREEN, [
        "SISTEMA WEB PARA UNA ESCUELA DE FÚTBOL EN KENNEDY",
        "REGISTRA GOLES, ASISTENCIAS Y MINUTOS JUGADOS",
        "REPORTES, COMPARACIÓN DE JUGADORES Y CRONOGRAMA",
        "MÓDULO DE SUGERENCIAS CON IA · DISEÑO RESPONSIVE",
    ]),
    ("JS KIRIOS", "EN CURSO", CYAN, [
        "TIENDA SHOPIFY DE BELLEZA CON TEMA PERSONALIZADO",
        "PAGO CONTRAENTREGA Y DESCUENTOS POR CANTIDAD",
        "GESTIÓN DE PEDIDOS CONECTADA A DROPI",
    ]),
    ("PRIMER ROL DEV JUNIOR", "SIGUIENTE", RED, [
        "OBJETIVO: PASAR DE SOPORTE TI A DESARROLLO",
        "BACKEND PHP / LARAVEL EN UN EQUIPO ÁGIL",
    ]),
]


def misiones():
    w = 900
    top = 96
    blocks = []
    y = top
    for name, status, col, lines in MISIONES:
        bh = 56 + 22 * len(lines) + 16
        blocks.append((y, bh, name, status, col, lines))
        y += bh + 18
    h = y + 20
    s = title_bar(w, "MISIONES")
    for y, bh, name, status, col, lines in blocks:
        s += f'<rect x="40" y="{y}" width="{w-80}" height="{bh}" fill="{PANEL}"/>'
        s += f'<rect x="40" y="{y}" width="{w-80}" height="6" fill="{col}"/>'
        s += sprite(SWORD, 56, y + 18, 4, {"1": CREAM, "2": GOLD_D, "3": MUTED})
        s += text(name, 100, y + 20, 4, CREAM, shadow="#000")
        sw = width(status, 2)
        s += f'<rect x="{w-60-sw-20}" y="{y+16}" width="{sw+20}" height="26" fill="{col}"/>'
        s += text(status, w - 70, y + 22, 2, INK, anchor="end")
        for j, ln in enumerate(lines):
            s += text("> " + ln, 100, y + 62 + j * 22, 2, MUTED if j % 2 else CREAM)
    return frame(w, h, s)



DISC = [
 "..1111..",
 ".122221.",
 "12233221",
 "12344321",
 "12344321",
 "12233221",
 ".122221.",
 "..1111..",
]


def portada():
    w, h = 900, 420
    s = ""
    import random
    random.seed(5)
    for _ in range(40):
        x, y = random.randrange(24, w - 24, 4), random.randrange(24, h - 24, 4)
        s += f'<rect x="{x}" y="{y}" width="4" height="4" fill="{RED}" opacity="{random.choice([.2,.35,.5])}"/>'
    bc = {"1": INK, "2": RED, "3": PURPLE}
    for (x, y, px) in [(190, 34, 4), (676, 30, 5), (44, 296, 5), (806, 290, 5), (110, 366, 3), (760, 372, 3)]:
        s += f'<g class="float">{sprite(BUTTER, x, y, px, bc)}</g>'
    s += text("VOL. 01", 40, 36, 3, INK)
    s += text("2026", w - 40, 36, 3, INK, anchor="end")
    s += text("DARWIN MENDOZA", w // 2, 120, 9, INK, shadow=RED, anchor="middle")
    s += f'<rect x="200" y="202" width="500" height="4" fill="{RED}"/>'
    s += text("DESARROLLADOR DE SOFTWARE JUNIOR", w // 2, 226, 4, INK, anchor="middle")
    s += text("PHP · LARAVEL · MYSQL · JAVASCRIPT", w // 2, 272, 3, PURPLE, anchor="middle")
    s += f'<g class="blink">{text("> PRESS START  ·  BOGOTÁ, CO", w // 2, 340, 3, RED, anchor="middle")}</g>'
    return frame(w, h, s)


def intro():
    w = 900
    lines = [
        ("> TECNÓLOGO EN ANÁLISIS Y DESARROLLO DE SOFTWARE · SENA", CREAM),
        ("> AUXILIAR DE TECNOLOGÍA · ORGANIZACIÓN CÁRDENAS", CREAM),
        ("> ESTUDIANTE DE INGENIERÍA DE SOFTWARE · U. MANUELA BELTRÁN", CREAM),
        ("> RUMBO A DESARROLLADOR BACKEND PHP / LARAVEL", GOLD),
    ]
    h = 100 + 34 * len(lines) + 40
    s = title_bar(w, "INTRO")
    s += f'<rect x="40" y="90" width="{w-80}" height="{34*len(lines)+24}" fill="{PANEL}"/>'
    for i, (ln, col) in enumerate(lines):
        s += text(ln, 64, 108 + i * 34, 2, col)
    return frame(w, h, s)


def discografia():
    w = 900
    rowh = 112
    top = 96
    h = top + rowh * len(LOGROS) + 30
    s = title_bar(w, "DISCOGRAFÍA · LOGROS")
    for i, (tag, name, l1, l2) in enumerate(LOGROS):
        y = top + i * rowh
        s += f'<rect x="40" y="{y}" width="{w-80}" height="{rowh-14}" fill="{PANEL}"/>'
        s += f'<rect x="40" y="{y+rowh-22}" width="{w-80}" height="8" fill="{PANEL2}"/>'
        s += sprite(DISC, 58, y + 18, 7, {"1": INK, "2": "#2a1f45", "3": RED, "4": GOLD})
        s += text(f"{i+1:02d}", 86, y + 2, 1, MUTED) if False else ""
        s += text(name, 140, y + 14, 4, GOLD, shadow="#3d0d29")
        s += text(l1, 140, y + 52, 2, CREAM)
        s += text(l2, 140, y + 74, 2, CREAM)
        s += text(tag, w - 60, y + 14, 3, CYAN, anchor="end")
        s += text("LOGRO 100%", w - 60, y + 60, 2, GREEN, anchor="end")
    return frame(w, h, s)


TRACKS = [
    ("01", "SCORD", "COMPLETADA", GREEN, [
        "SISTEMA WEB PARA UNA ESCUELA DE FÚTBOL EN KENNEDY",
        "REGISTRA GOLES, ASISTENCIAS Y MINUTOS JUGADOS",
        "REPORTES, COMPARACIÓN DE JUGADORES Y CRONOGRAMA",
        "MÓDULO DE SUGERENCIAS CON IA · DISEÑO RESPONSIVE",
    ]),
    ("02", "JS KIRIOS", "EN CURSO", CYAN, [
        "TIENDA SHOPIFY DE BELLEZA CON TEMA PERSONALIZADO",
        "PAGO CONTRAENTREGA Y DESCUENTOS POR CANTIDAD",
        "GESTIÓN DE PEDIDOS CONECTADA A DROPI",
    ]),
    ("03", "PRIMER ROL DEV JUNIOR", "PRÓXIMAMENTE", GOLD, [
        "DE SOPORTE TI A DESARROLLO BACKEND",
        "PHP / LARAVEL EN UN EQUIPO ÁGIL",
    ]),
]


def tracklist():
    w = 900
    top = 96
    blocks = []
    y = top
    for num, name, status, col, lines in TRACKS:
        bh = 56 + 22 * len(lines) + 16
        blocks.append((y, bh, num, name, status, col, lines))
        y += bh + 18
    h = y + 20
    s = title_bar(w, "TRACKLIST · PROYECTOS")
    for y, bh, num, name, status, col, lines in blocks:
        s += f'<rect x="40" y="{y}" width="{w-80}" height="{bh}" fill="{PANEL}"/>'
        s += f'<rect x="40" y="{y}" width="{w-80}" height="6" fill="{col}"/>'
        s += text(num, 60, y + 20, 4, GOLD)
        s += text(name, 124, y + 20, 4, CREAM, shadow="#000")
        sw = width(status, 2)
        s += f'<rect x="{w-60-sw-20}" y="{y+16}" width="{sw+20}" height="26" fill="{col}"/>'
        s += text(status, w - 70, y + 22, 2, INK, anchor="end")
        for j, ln in enumerate(lines):
            s += text("> " + ln, 124, y + 62 + j * 22, 2, MUTED if j % 2 else CREAM)
    return frame(w, h, s)


def sello():
    w, h = 900, 200
    s = title_bar(w, "SELLO ACTUAL")
    s += f'<rect x="40" y="92" width="{w-80}" height="80" fill="{PANEL}"/>'
    s += sprite(BUTTER, 58, 104, 5, {"1": CREAM, "2": GOLD, "3": PURPLE})
    s += text("ORGANIZACIÓN CÁRDENAS", 124, 106, 4, GOLD, shadow="#3d0d29")
    s += text("AUXILIAR DE TECNOLOGÍA · DESDE ABR 2026", 124, 148, 2, CREAM)
    return frame(w, h, s)


def creditos():
    w = 900
    top = 100
    rowh = 74
    h = top + rowh * len(INV) + 30
    s = title_bar(w, "CRÉDITOS · STACK")
    for i, (cat, items, col) in enumerate(INV):
        y = top + i * rowh
        s += sprite(CHEST, 44, y + 6, 5, {"1": GOLD_D, "2": col, "3": GOLD})
        s += text(cat, 96, y + 14, 3, INK)
        x = 340
        for it in items:
            tw = width(it, 2)
            s += f'<rect x="{x}" y="{y+4}" width="{tw+24}" height="38" fill="{PANEL}"/>'
            s += f'<rect x="{x}" y="{y+42}" width="{tw+24}" height="6" fill="{PANEL2}"/>'
            s += f'<rect x="{x}" y="{y+4}" width="4" height="38" fill="{col}"/>'
            s += text(it, x + 14, y + 16, 2, CREAM)
            x += tw + 36
    return frame(w, h, s)


def boton(label, col):
    w = width(label, 3) + 64
    h = 64
    s = f'<rect x="12" y="12" width="{w-24}" height="{h-24}" fill="{PANEL}"/><rect x="12" y="{h-18}" width="{w-24}" height="6" fill="{col}"/>'
    s += text(label, w // 2, 22, 3, CREAM, anchor="middle")
    return frame(w, h, s)


def firma():
    w, h = 900, 200
    bc = {"1": INK, "2": RED, "3": PURPLE}
    s = sprite(BUTTER, w // 2 - 27, 24, 6, bc)
    s += text("DARWIN MENDOZA", w // 2, 92, 5, INK, shadow=RED, anchor="middle")
    s += f'<g class="blink">{text("GRACIAS POR ESCUCHAR · FIN DEL VOL. 01", w // 2, 148, 2, PURPLE, anchor="middle")}</g>'
    return frame(w, h, s)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    piezas = [("portada", portada), ("intro", intro), ("discografia", discografia), ("tracklist", tracklist),
              ("sello", sello), ("creditos", creditos), ("firma", firma),
              ("red-github", lambda: boton("GITHUB", GOLD)), ("red-linkedin", lambda: boton("LINKEDIN", PURPLE)),
              ("red-email", lambda: boton("EMAIL", RED))]
    for f in os.listdir(OUT):
        os.remove(os.path.join(OUT, f))
    for name, fn in piezas:
        with open(os.path.join(OUT, f"{name}.svg"), "w") as fh:
            fh.write(fn())
        print("ok", name)
