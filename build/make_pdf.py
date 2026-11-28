#!/usr/bin/env python3
"""Build the downloadable full-day lesson PDF: pdf/FAANG-Prep-Day-NN.pdf

Usage:  python3 build/make_pdf.py            # every day that has a lesson file
        python3 build/make_pdf.py 4 5        # only these days

It opens the real site in a headless browser, so the PDF looks exactly like
the lesson pages (with every hint, solution and answer expanded), then joins
a cover page and the four tracks into one file.
Needs: pip install playwright pypdf --break-system-packages && playwright install chromium
"""
import functools, html, http.server, io, json, pathlib, sys, threading
from playwright.sync_api import sync_playwright
from pypdf import PdfWriter, PdfReader

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "pdf"
TRACKS = [("dsa", "Coding patterns", "#0f7a55"), ("java", "Java & Spring", "#0e7490"),
          ("design", "System design", "#6d28d9"), ("ai", "AI skills", "#c2410c")]
EXPAND = """() => {document.querySelectorAll('details').forEach(d=>d.open=true);
 document.querySelectorAll('[hidden]').forEach(e=>e.hidden=false);}"""


def serve():
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
    h = functools.partial(Quiet, directory=str(ROOT))
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), h)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def cover(les, n):
    e = html.escape
    rows = "".join(
        f'<li style="border-left:6px solid {c}"><b>{e(name)}</b><span>{e(les["tracks"][t]["title"])}</span>'
        f'<small>{les["tracks"][t].get("minutes","")} min · {e(str(les["tracks"][t].get("level","")))}</small></li>'
        for t, name, c in TRACKS)
    return f"""<!doctype html><meta charset=utf-8><style>
body{{font-family:Inter,Arial,sans-serif;color:#111;margin:0;padding:40mm 18mm}}
h1{{font-family:Georgia,serif;font-size:30pt;margin:6px 0 10px}}p{{font-size:12pt;line-height:1.5;color:#333}}
.k{{font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#555;font-size:10pt}}
ul{{list-style:none;padding:0;margin-top:28px}}li{{padding:10px 14px;margin:10px 0;background:#f5f5f4;border-radius:8px}}
li b{{display:block;font-size:10pt;color:#555}}li span{{display:block;font-size:13pt;font-weight:600;margin:3px 0}}li small{{color:#666}}
</style><div class=k>FAANG Prep · Day {n} of 60 · {e(les.get("date",""))}</div>
<h1>{e(les.get("headline",""))}</h1><p>{e(les.get("intro","")).replace("**","")}</p><ul>{rows}</ul>"""


def build(days):
    OUT.mkdir(exist_ok=True)
    srv = serve(); base = f"http://127.0.0.1:{srv.server_address[1]}"
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": 1100, "height": 1400}, color_scheme="light")
        ctx.add_init_script("try{localStorage.setItem('fp_seenGuide','true')}catch(e){}")
        pg = ctx.new_page()          # the site
        cv = ctx.new_page()          # cover pages (kept separate so the site page keeps its URL)
        for n in days:
            f = ROOT / "data" / "lessons" / f"day-{n:02d}.json"
            if not f.exists():
                print(f"Day {n}: no lesson file, skipped"); continue
            les = json.loads(f.read_text())
            w = PdfWriter()
            cv.set_content(cover(les, n)); cv.emulate_media(media="print")
            w.append(PdfReader(io.BytesIO(cv.pdf(format="A4"))))
            for t, _, _ in TRACKS:
                pg.emulate_media(media="screen")
                pg.goto(f"{base}/#lesson-{t}-{n}"); pg.wait_for_selector(".band", timeout=15000)
                pg.wait_for_timeout(300); pg.evaluate(EXPAND); pg.emulate_media(media="print")
                w.append(PdfReader(io.BytesIO(pg.pdf(format="A4", print_background=True,
                         margin={"top": "14mm", "bottom": "14mm", "left": "12mm", "right": "12mm"}))))
            w.add_metadata({"/Title": f"FAANG Prep — Day {n}: {les.get('headline','')}"})
            out = OUT / f"FAANG-Prep-Day-{n:02d}.pdf"
            with open(out, "wb") as fh: w.write(fh)
            print(f"Day {n}: {out.relative_to(ROOT)} ({len(w.pages)} pages)")
        b.close()
    srv.shutdown()


if __name__ == "__main__":
    args = [int(a) for a in sys.argv[1:]]
    if not args:
        args = sorted(int(x.stem[4:]) for x in (ROOT / "data" / "lessons").glob("day-*.json"))
    build(args)
