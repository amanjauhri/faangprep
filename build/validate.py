#!/usr/bin/env python3
"""Validate a lesson file (data/lessons/day-NN.json) or data/news.json.
Usage: python3 build/validate.py data/lessons/day-01.json [data/news.json ...]
Exits non-zero with a list of problems if anything is off."""
import json, sys

BLOCKS = {
    "p": ["text"], "steps": ["items"], "list": ["items"], "table": ["head", "rows"],
    "code": ["code"], "flow": ["items"], "callout": ["title", "text"], "compare": ["items"],
}
TRACKS = ["dsa", "java", "design", "ai"]

def err(errs, where, msg):
    errs.append(f"{where}: {msg}")

def need(errs, obj, keys, where):
    for k in keys:
        if k not in obj or obj[k] in (None, "", []):
            err(errs, where, f"missing '{k}'")

def check_blocks(errs, blocks, where):
    if not isinstance(blocks, list) or not blocks:
        err(errs, where, "blocks must be a non-empty list"); return
    for i, b in enumerate(blocks):
        w = f"{where}.blocks[{i}]"
        t = b.get("type")
        if t not in BLOCKS:
            err(errs, w, f"unknown type {t!r}"); continue
        need(errs, b, BLOCKS[t], w)
        if t == "table":
            n = len(b.get("head", []))
            for r in b.get("rows", []):
                if len(r) != n: err(errs, w, "row length != head length")
        if t == "flow":
            for it in b.get("items", []):
                if "label" not in it: err(errs, w, "flow item needs label")
        if t == "compare":
            for it in b.get("items", []):
                need(errs, it, ["title", "points"], w + ".compare")

def check_lesson(errs, L, path):
    need(errs, L, ["day", "date", "phase", "headline", "intro", "tracks", "glossary"], path)
    for t in TRACKS:
        T = L.get("tracks", {}).get(t)
        w = f"{path}.tracks.{t}"
        if not T:
            err(errs, w, "missing track"); continue
        need(errs, T, ["title", "minutes", "level", "why", "builds_on", "next", "subtopics", "interview_qa", "takeaways", "resources"], w)
        need(errs, T.get("interview_angle", {}), ["asked_at", "how_it_comes_up", "strong_answer", "pitfalls"], w + ".interview_angle")
        subs = T.get("subtopics", [])
        if len(subs) < 3: err(errs, w, "needs at least 3 subtopics")
        ids = set()
        for i, s in enumerate(subs):
            sw = f"{w}.subtopics[{i}]"
            need(errs, s, ["id", "title", "in_one_line", "blocks"], sw)
            if s.get("id") in ids: err(errs, sw, "duplicate id")
            ids.add(s.get("id"))
            check_blocks(errs, s.get("blocks"), sw)
        for i, q in enumerate(T.get("interview_qa", [])):
            need(errs, q, ["q", "a"], f"{w}.interview_qa[{i}]")
        for i, r in enumerate(T.get("resources", [])):
            need(errs, r, ["title", "url"], f"{w}.resources[{i}]")
            if not str(r.get("url", "")).startswith("https://"): err(errs, f"{w}.resources[{i}]", "url must be https")
        if t == "dsa":
            P = T.get("problems", [])
            if not P and L.get("day") not in (54, 55, 57, 58, 59, 60): err(errs, w, "dsa needs problems")
            for i, p in enumerate(P):
                pw = f"{w}.problems[{i}]"
                need(errs, p, ["num", "title", "url", "difficulty", "statement", "example", "how_to_think", "hints", "solution"], pw)
                if p.get("difficulty") not in ("Easy", "Medium", "Hard"): err(errs, pw, "difficulty must be Easy/Medium/Hard")
                need(errs, p.get("solution", {}), ["approach", "code", "time", "space"], pw + ".solution")
        if t == "ai":
            need(errs, T, ["prompt"], w)
    for i, g in enumerate(L.get("glossary", [])):
        need(errs, g, ["term", "meaning"], f"{path}.glossary[{i}]")

def check_news(errs, N, path):
    need(errs, N, ["updated", "items"], path)
    if len(N.get("items", [])) != 2: err(errs, path, "news must have exactly 2 items")
    for i, it in enumerate(N.get("items", [])):
        need(errs, it, ["date", "tag", "headline", "summary", "why", "source", "url"], f"{path}.items[{i}]")

def main(paths):
    errs = []
    for p in paths:
        try:
            with open(p) as f: data = json.load(f)
        except Exception as e:
            errs.append(f"{p}: cannot parse JSON: {e}"); continue
        (check_news if p.endswith("news.json") else check_lesson)(errs, data, p)
    if errs:
        print("INVALID\n" + "\n".join(errs)); sys.exit(1)
    print("OK", ", ".join(paths))

if __name__ == "__main__":
    main(sys.argv[1:])
