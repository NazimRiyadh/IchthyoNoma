#!/usr/bin/env python3
"""Validate the seven-class image counts used in the IchthyoNoma paper."""
from __future__ import annotations
import argparse
import re
import unicodedata
from pathlib import Path

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".webp", ".tif", ".tiff"}
CLASSES = ["Rui", "Katla", "Mrigal", "Tilapia", "Pabda", "Ilish", "Koi"]
EXPECTED = {
    "BFF-15": {"Rui":514,"Katla":427,"Mrigal":317,"Tilapia":383,"Pabda":348,"Ilish":233,"Koi":434},
    "SylFishBD": {"Rui":1670,"Katla":1133,"Mrigal":1293,"Tilapia":1326,"Pabda":862,"Ilish":789,"Koi":592},
}
ALIASES = {
    "Rui": ["rui","rohu","labeo rohita","labeo_rohita"],
    "Katla": ["katla","catla","catla catla","catla_catla"],
    "Mrigal": ["mrigal","mrigel","mrigal carp","cirrhinus cirrhosus","cirrhinus_cirrhosus"],
    "Tilapia": ["tilapia","tilapia fish","telapia","telapia fish","telapiya","telapiya fish","tilapiya","tilapiya fish","nile tilapia","oreochromis niloticus","oreochromis_niloticus"],
    "Pabda": ["pabda","pabda catfish","ompok pabda","ompok_pabda"],
    "Ilish": ["ilish","hilsa","tenualosa ilisha","tenualosa_ilisha"],
    "Koi": ["koi","climbing perch","anabas testudineus","anabas_testudineus"],
}
EXCLUDE = {"mask","masks","segmentation","segmentations","annotation","annotations","bbox","bboxes","bounding box","bounding boxes"}

def norm(x: str) -> str:
    x = unicodedata.normalize("NFKC", str(x)).lower().strip()
    return re.sub(r"[\s\-_]+", " ", x)

alias_to_class = {}
for cls, vals in ALIASES.items():
    alias_to_class[norm(cls)] = cls
    for val in vals:
        alias_to_class[norm(val)] = cls

def excluded(p: Path) -> bool:
    return any(norm(part) in EXCLUDE for part in p.parts)

def infer(p: Path):
    tokens = [norm(x) for x in list(p.parts) + [p.stem]]
    for token in reversed(tokens):
        if token in alias_to_class:
            return alias_to_class[token]
    for token in reversed(tokens):
        for alias, cls in alias_to_class.items():
            if len(alias) >= 3 and re.search(rf"(^| ){re.escape(alias)}($| )", token):
                return cls
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", type=Path)
    ap.add_argument("--target", required=True, choices=EXPECTED)
    args = ap.parse_args()
    counts = {c: 0 for c in CLASSES}
    for p in args.root.rglob("*"):
        if p.is_file() and p.suffix.lower() in IMAGE_EXTS and not excluded(p):
            cls = infer(p)
            if cls:
                counts[cls] += 1
    exp = EXPECTED[args.target]
    ok = True
    print(f"Target: {args.target}\nRoot: {args.root}\n")
    print(f"{'Class':10s} {'Expected':>10s} {'Found':>10s} {'Match':>8s}")
    for cls in CLASSES:
        match = counts[cls] == exp[cls]
        ok &= match
        print(f"{cls:10s} {exp[cls]:10d} {counts[cls]:10d} {str(match):>8s}")
    print(f"{'TOTAL':10s} {sum(exp.values()):10d} {sum(counts.values()):10d} {str(ok):>8s}")
    raise SystemExit(0 if ok else 1)

if __name__ == "__main__":
    main()
