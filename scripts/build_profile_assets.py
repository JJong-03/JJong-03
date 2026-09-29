#!/usr/bin/env python3
"""Build the profile README images (desktop and mobile, light and dark).

Text is drawn as Pretendard outlines, because SVG files shown through <img>
cannot load web fonts and Korean text would otherwise fall back to whatever
font each viewer has installed. Each glyph is defined once and reused.

Usage:
    FONT_DIR=~/.local/share/fonts python3 scripts/build_profile_assets.py

Requires fontTools and Pretendard-{Regular,Medium,SemiBold,Bold,ExtraBold}.ttf.
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from xml.sax.saxutils import escape

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
FONT_DIR = Path(os.path.expanduser(os.environ.get("FONT_DIR", "~/.local/share/fonts")))
WEIGHTS = {400: "Regular", 500: "Medium", 600: "SemiBold", 700: "Bold", 800: "ExtraBold"}

LIGHT = {
    "panel": "#f6f8fa", "panel_line": "#d1d9e0", "card": "#ffffff", "card_line": "#d1d9e0",
    "ink": "#1f2328", "body": "#3d444d", "muted": "#59636e",
    "accent": "#0f766e", "accent_fill": "#0f766e", "on_fill": "#ffffff", "on_fill_soft": "#d7f5f0",
    "soft_bg": "#e3f4f1", "soft_text": "#0b5f58", "dash": "#8c959f",
}
DARK = {
    "panel": "#151b23", "panel_line": "#3d444d", "card": "#0d1117", "card_line": "#3d444d",
    "ink": "#f0f6fc", "body": "#d1d7e0", "muted": "#9198a1",
    "accent": "#2dd4bf", "accent_fill": "#115e59", "on_fill": "#ffffff", "on_fill_soft": "#c9f2ec",
    "soft_bg": "#0f2d2a", "soft_text": "#5eead4", "dash": "#6e7681",
}


class Face:
    def __init__(self, weight: int):
        font = TTFont(FONT_DIR / f"Pretendard-{WEIGHTS[weight]}.ttf")
        self.weight = weight
        self.upm = font["head"].unitsPerEm
        self.cmap = font.getBestCmap()
        self.glyphs = font.getGlyphSet()
        self.hmtx = font["hmtx"]
        self._paths: dict[str, str] = {}

    def name(self, ch: str) -> str:
        glyph = self.cmap.get(ord(ch))
        if glyph is None:
            raise KeyError(f"Pretendard has no glyph for {ch!r}")
        return glyph

    def advance(self, glyph: str) -> int:
        return self.hmtx[glyph][0]

    def path(self, glyph: str) -> str:
        if glyph not in self._paths:
            pen = SVGPathPen(self.glyphs, ntos=lambda v: str(round(v)))
            self.glyphs[glyph].draw(pen)
            self._paths[glyph] = pen.getCommands()
        return self._paths[glyph]


FACES = {w: Face(w) for w in WEIGHTS}


def measure(text: str, size: float, weight: int = 400, track: float = 0.0) -> float:
    face = FACES[weight]
    width = sum(face.advance(face.name(ch)) for ch in text) * size / face.upm
    return width + track * max(len(text) - 1, 0)


def wrap(text: str, size: float, weight: int, max_width: float) -> list[str]:
    lines: list[str] = []
    current = ""
    for word in text.split(" "):
        trial = f"{current} {word}".strip()
        if current and measure(trial, size, weight) > max_width:
            lines.append(current)
            current = word
        else:
            current = trial
    if current:
        lines.append(current)
    return lines


class Canvas:
    def __init__(self, width: float, height: float, palette: dict[str, str]):
        self.width, self.height, self.c = width, height, palette
        self.defs: dict[str, str] = {}
        self.items: list[str] = []

    def add(self, markup: str) -> None:
        self.items.append(markup)

    def rect(self, x, y, w, h, fill, rx=0, stroke=None, width=1.0):
        line = f' stroke="{self.c[stroke]}" stroke-width="{width}"' if stroke else ""
        paint = self.c.get(fill, fill)
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{paint}"{line}/>')

    def line(self, x1, y1, x2, y2, color, width=1.0, dash=None):
        extra = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<path d="M{x1:.1f} {y1:.1f}L{x2:.1f} {y2:.1f}" stroke="{self.c[color]}" stroke-width="{width}"{extra}/>')

    def text(self, x, y, text, size, weight=400, color="ink", anchor="start", track=0.0) -> float:
        face = FACES[weight]
        scale = size / face.upm
        width = measure(text, size, weight, track)
        if anchor == "middle":
            x -= width / 2
        elif anchor == "end":
            x -= width
        uses = []
        cursor = x
        for ch in text:
            glyph = face.name(ch)
            outline = face.path(glyph)
            if outline:
                ident = f"g{weight}-" + re.sub(r"[^A-Za-z0-9_.-]", "_", glyph)
                self.defs[ident] = outline
                uses.append(
                    f'<use xlink:href="#{ident}" transform="translate({cursor:.1f} {y:.1f}) scale({scale:.5f} {-scale:.5f})"/>'
                )
            cursor += face.advance(glyph) * scale + track
        self.add(f'<g fill="{self.c.get(color, color)}">{"".join(uses)}</g>')
        return width

    def svg(self, title: str) -> str:
        defs = "".join(f'<path id="{k}" d="{v}"/>' for k, v in self.defs.items())
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'width="{self.width:.0f}" height="{self.height:.0f}" viewBox="0 0 {self.width:.0f} {self.height:.0f}" '
            f'role="img" aria-label="{escape(title)}"><title>{escape(title)}</title>'
            f"<defs>{defs}</defs>{''.join(self.items)}</svg>\n"
        )


# ---------------------------------------------------------------- content
# Every statement below matches the portfolio and the career guides.

NAME = "김종원"
NAME_EN = "Kim Jongwon"
EYEBROW = "CLOUD INFRASTRUCTURE / DEVOPS"
ROLE = "클라우드 인프라 / DevOps 신입 엔지니어"
PITCH = [
    "Terraform으로 AWS와 GCP 인프라를 만들고 Kubernetes로 서비스를 배포했습니다.",
    "요청이 실패하면 막힌 구간을 찾아 고치고, 고친 뒤 무엇을 확인했는지 기록합니다.",
]
META = ["인천대학교 임베디드시스템공학과 졸업 (2026.08)", "메가존클라우드 MSP 솔루션 아키텍트 양성과정 8기 수료"]

FLOW = [("코드", "Terraform"), ("배포", "Argo CD"), ("확인", "테스트")]
FLOW_CAPTION = "만들고, 배포하고, 확인합니다"

FOCUS = [
    ("01  /  만들기", "코드로 만드는 인프라", ["Terraform으로 AWS, GCP 구성", "VPC 3개 분리, 모듈과 dev/prod"]),
    ("02  /  배포", "배포와 실행 자동화", ["Kubernetes Job, Argo CD GitOps", "키 파일 없는 배포 (WIF)"]),
    ("03  /  원인 찾기", "막힌 요청의 원인 찾기", ["504 두 건과 멈춘 롤아웃 해결", "로컬 부하 측정으로 병목 확인"]),
]

PROJECTS = [
    ("2026.05 ~ 06  /  2인 팀  /  AWS", "Aegis-Pi Risk Twin", "이력 조회 504를 풀고, 사라진 위험 신호를 되살림", "최우수팀", "fill"),
    ("2026.02 ~ 03  /  개인  /  Kubernetes", "Kubernetes 백테스트 플랫폼", "요청마다 Job, run_id 추적, 설정 조정으로 로컬 처리량 58% 향상", "우수상", "fill"),
    ("2026.03 ~ 04  /  개인  /  AWS", "AWS Multi-VPC 인프라", "VPC 3개로 경로를 나누고, EKS 504의 두 원인을 복구", "PoC", "soft"),
    ("2026.04  /  개인  /  GCP", "GCP GKE GitOps", "키 파일 없는 배포, 노드 2대에서 멈춘 롤아웃 해결", "실습", "soft"),
    ("2026.04 ~ 05  /  2인 팀  /  GCP", "LawMainRoad", "근거 법령과 함께 답하는 AI 서비스를 GCP로 이전", "공모전 출품", "soft"),
]

TOOLS = [
    ("AWS", "VPC, EKS, ECS Fargate, ALB, CloudFront, DynamoDB, Lambda, Cognito, Bedrock"),
    ("GCP", "GKE, Cloud Run, Cloud SQL, Artifact Registry"),
    ("IaC와 배포", "Terraform (모듈, dev/prod 분리), GitHub Actions, Argo CD, WIF"),
    ("실행과 관측", "Linux, Docker, Kubernetes, Prometheus, Grafana"),
    ("개발", "Python (FastAPI, Flask), React, MySQL, Redis"),
]

TITLE = "김종원, 클라우드 인프라와 DevOps 신입 엔지니어 프로필 카드"


def pill(cv: Canvas, right: float, center_y: float, label: str, style: str) -> None:
    size = 11
    w = measure(label, size, 700) + 24
    x = right - w
    if style == "fill":
        cv.rect(x, center_y - 12, w, 24, "accent_fill", rx=12)
        cv.text(x + w / 2, center_y + 4, label, size, 700, "on_fill", "middle")
    else:
        cv.rect(x, center_y - 12, w, 24, "soft_bg", rx=12)
        cv.text(x + w / 2, center_y + 4, label, size, 700, "soft_text", "middle")


def flow_diagram(cv: Canvas, x: float, y: float, w: float, h: float) -> None:
    cv.rect(x, y, w, h, "card", rx=12, stroke="card_line")
    cv.text(x + w - 14, y + 24, "HOW I WORK", 9.5, 700, "muted", "end", track=1.3)
    cy = y + h * 0.47
    xs = [x + w * 0.16, x + w * 0.5, x + w * 0.84]
    for a, b in zip(xs, xs[1:]):
        mid = (a + b) / 2
        cv.add(
            f'<path d="M{a + 9:.1f} {cy:.1f}C{mid - 10:.1f} {cy - 22:.1f} {mid + 10:.1f} {cy + 22:.1f} {b - 9:.1f} {cy:.1f}" '
            f'fill="none" stroke="{cv.c["dash"]}" stroke-width="1.6" stroke-dasharray="3 4"/>'
        )
    for i, (px, (label, sub)) in enumerate(zip(xs, FLOW)):
        if i == len(xs) - 1:
            cv.add(f'<circle cx="{px:.1f}" cy="{cy:.1f}" r="9" fill="{cv.c["accent_fill"]}"/>')
            cv.add(
                f'<path d="M{px - 4:.1f} {cy:.1f}l3 3 5.5-6" fill="none" stroke="{cv.c["on_fill"]}" '
                f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
            )
        else:
            cv.add(f'<circle cx="{px:.1f}" cy="{cy:.1f}" r="7.5" fill="{cv.c["card"]}" stroke="{cv.c["ink"]}" stroke-width="1.6"/>')
        cv.text(px, cy + 30, label, 12, 800, "ink", "middle")
        cv.text(px, cy + 46, sub, 9.5, 500, "muted", "middle")
    cv.text(x + 14, y + h - 14, FLOW_CAPTION, 10.5, 700, "accent")


def section_title(cv: Canvas, x: float, y: float, eyebrow: str, title: str, size: float = 20) -> float:
    cv.text(x, y, eyebrow, 10.5, 700, "muted", track=1.5)
    cv.text(x, y + 28, title, size, 800, "ink")
    return y + 44


def focus_card(cv: Canvas, x, y, w, h, item, highlighted: bool, compact: bool = False) -> None:
    label, title, body = item
    if highlighted:
        cv.rect(x, y, w, h, "accent_fill", rx=12)
        colors = ("on_fill_soft", "on_fill", "on_fill_soft", "on_fill")
    else:
        cv.rect(x, y, w, h, "card", rx=12, stroke="card_line")
        colors = ("accent", "ink", "muted", "accent")
    cv.text(x + 18, y + 27, label, 10.5, 700, colors[0], track=0.6)
    cv.text(x + 18, y + 54, title, 17, 800, colors[1])
    for i, line in enumerate(body):
        cv.text(x + 18, y + 79 + i * 19, line, 12.5, 500, colors[2])
    cv.rect(x + 18, y + h - 16, 36, 3, colors[3], rx=1.5)


# ---------------------------------------------------------------- desktop
def desktop(palette: dict[str, str]) -> str:
    W, PAD = 880.0, 32.0
    rows_h, row_gap = 58.0, 10.0
    tools_row = 34.0
    y_focus = 244.0
    y_proj = y_focus + 132 + 40
    y_rows = y_proj + 44
    y_tools = y_rows + len(PROJECTS) * (rows_h + row_gap) - row_gap + 40
    y_tools_panel = y_tools + 44
    H = y_tools_panel + len(TOOLS) * tools_row + 12 + PAD
    cv = Canvas(W, H, palette)
    cv.rect(0.5, 0.5, W - 1, H - 1, "panel", rx=18, stroke="panel_line")

    # header
    diag_w = 236.0
    text_right = W - PAD - diag_w - 24
    cv.rect(PAD, 34, 4, 184, "accent_fill", rx=2)
    x = PAD + 24
    cv.text(x, 52, EYEBROW, 11, 700, "accent", track=1.6)
    name_w = cv.text(x, 104, NAME, 46, 800, "ink")
    cv.text(x + name_w + 14, 104, NAME_EN, 17, 600, "muted")
    cv.text(x, 138, ROLE, 17, 700, "ink")
    for i, line in enumerate(PITCH):
        assert measure(line, 13.5, 400) <= text_right - x, line
        cv.text(x, 168 + i * 21, line, 13.5, 400, "body")
    meta = META[0] + "   /   " + META[1]
    assert measure(meta, 11, 500) <= text_right - x, meta
    cv.text(x, 216, meta, 11, 500, "muted")
    flow_diagram(cv, W - PAD - diag_w, 34, diag_w, 184)

    # focus cards
    gap = 14.0
    card_w = (W - 2 * PAD - 2 * gap) / 3
    for i, item in enumerate(FOCUS):
        focus_card(cv, PAD + i * (card_w + gap), y_focus, card_w, 132, item, highlighted=(i == 2))

    # projects
    section_title(cv, PAD, y_proj, "SELECTED PROJECTS", "대표 프로젝트")
    for i, (meta_line, name, desc, badge, style) in enumerate(PROJECTS):
        ry = y_rows + i * (rows_h + row_gap)
        cv.rect(PAD, ry, W - 2 * PAD, rows_h, "card", rx=10, stroke="card_line")
        cv.text(PAD + 18, ry + 22, meta_line, 10.5, 600, "accent", track=0.3)
        nw = cv.text(PAD + 18, ry + 44, name, 15, 800, "ink")
        limit = W - PAD - 18 - (measure(badge, 11, 700) + 24) - 16
        assert PAD + 18 + nw + 12 + measure(desc, 12.5, 500) <= limit, desc
        cv.text(PAD + 18 + nw + 12, ry + 44, desc, 12.5, 500, "muted")
        pill(cv, W - PAD - 18, ry + rows_h / 2, badge, style)

    # tools
    section_title(cv, PAD, y_tools, "TOOLCHAIN", "프로젝트에서 직접 쓴 기술")
    panel_h = len(TOOLS) * tools_row + 12
    cv.rect(PAD, y_tools_panel, W - 2 * PAD, panel_h, "card", rx=12, stroke="card_line")
    for i, (label, value) in enumerate(TOOLS):
        ty = y_tools_panel + 6 + i * tools_row
        if i:
            cv.line(PAD + 18, ty, W - PAD - 18, ty, "card_line")
        cv.text(PAD + 18, ty + 22, label, 11, 700, "accent", track=0.4)
        assert PAD + 128 + measure(value, 12.5, 600) <= W - PAD - 18, value
        cv.text(PAD + 128, ty + 22, value, 12.5, 600, "ink")
    return cv.svg(TITLE)


# ---------------------------------------------------------------- mobile
def mobile(palette: dict[str, str]) -> str:
    W, PAD = 400.0, 18.0
    inner = W - 2 * PAD
    cv_items: list[tuple] = []  # layout first, then draw with the final height

    y = 30.0
    header = []
    header.append(("text", PAD + 20, y + 14, EYEBROW, 10, 700, "accent", 1.3))
    header.append(("text", PAD + 20, y + 58, NAME, 40, 800, "ink", 0))
    header.append(("text", PAD + 20, y + 82, NAME_EN, 14, 600, "muted", 0))
    ty = y + 110
    for line in wrap(ROLE, 15.5, 700, inner - 20):
        header.append(("text", PAD + 20, ty, line, 15.5, 700, "ink", 0))
        ty += 22
    ty += 4
    for para in PITCH:
        for line in wrap(para, 13, 400, inner - 20):
            header.append(("text", PAD + 20, ty, line, 13, 400, "body", 0))
            ty += 19.5
    ty += 6
    for line in META:
        for piece in wrap(line, 10.5, 500, inner - 20):
            header.append(("text", PAD + 20, ty, piece, 10.5, 500, "muted", 0))
            ty += 16
    bar_bottom = ty - 8
    y_diag = ty + 12
    diag_h = 150.0
    y_focus = y_diag + diag_h + 16
    focus_h = 132.0
    y_proj = y_focus + 3 * (focus_h + 12) - 12 + 34
    y_rows = y_proj + 44
    rows = []
    ry = y_rows
    for meta_line, name, desc, badge, style in PROJECTS:
        desc_lines = wrap(desc, 12.5, 500, inner - 32)
        name_lines = wrap(name, 15, 800, inner - 32 - measure(badge, 11, 700) - 30)
        h = 26 + len(name_lines) * 21 + len(desc_lines) * 18 + 14
        rows.append((ry, h, meta_line, name_lines, desc_lines, badge, style))
        ry += h + 10
    y_tools = ry - 10 + 34
    y_tools_panel = y_tools + 44
    tool_rows = []
    tpy = y_tools_panel + 6
    for label, value in TOOLS:
        lines = wrap(value, 12.5, 600, inner - 32)
        h = 24 + len(lines) * 18 + 8
        tool_rows.append((tpy, h, label, lines))
        tpy += h
    panel_end = tpy + 6
    H = panel_end + PAD

    cv = Canvas(W, H, palette)
    cv.rect(0.5, 0.5, W - 1, H - 1, "panel", rx=16, stroke="panel_line")
    cv.rect(PAD, y + 2, 4, bar_bottom - y, "accent_fill", rx=2)
    for kind, x, yy, text, size, weight, color, track in header:
        cv.text(x, yy, text, size, weight, color, track=track)
    flow_diagram(cv, PAD, y_diag, inner, diag_h)
    for i, item in enumerate(FOCUS):
        focus_card(cv, PAD, y_focus + i * (focus_h + 12), inner, focus_h, item, highlighted=(i == 2))
    section_title(cv, PAD, y_proj, "SELECTED PROJECTS", "대표 프로젝트")
    for ry, h, meta_line, name_lines, desc_lines, badge, style in rows:
        cv.rect(PAD, ry, inner, h, "card", rx=10, stroke="card_line")
        cv.text(PAD + 16, ry + 22, meta_line, 10, 600, "accent", track=0.2)
        pill(cv, W - PAD - 14, ry + 18, badge, style)
        ly = ry + 44
        for line in name_lines:
            cv.text(PAD + 16, ly, line, 15, 800, "ink")
            ly += 21
        ly -= 1
        for line in desc_lines:
            cv.text(PAD + 16, ly, line, 12.5, 500, "muted")
            ly += 18
    section_title(cv, PAD, y_tools, "TOOLCHAIN", "직접 쓴 기술", size=19)
    cv.rect(PAD, y_tools_panel, inner, panel_end - y_tools_panel, "card", rx=12, stroke="card_line")
    for i, (tpy, h, label, lines) in enumerate(tool_rows):
        if i:
            cv.line(PAD + 16, tpy, W - PAD - 16, tpy, "card_line")
        cv.text(PAD + 16, tpy + 20, label, 10.5, 700, "accent", track=0.4)
        for j, line in enumerate(lines):
            cv.text(PAD + 16, tpy + 40 + j * 18, line, 12.5, 600, "ink")
    return cv.svg(TITLE)


# ---------------------------------------------------------------- contact buttons
ICONS = {
    "globe": '<circle cx="0" cy="0" r="9"/><ellipse cx="0" cy="0" rx="4" ry="9"/><path d="M-9 0H9M-7.5-5H7.5M-7.5 5H7.5"/>',
    "doc": '<path d="M-7-10H3L8-5V10H-7Z"/><path d="M3-10V-5H8M-3.5-1H4.5M-3.5 3H4.5M-3.5 7H1.5"/>',
    "mail": '<rect x="-9.5" y="-7" width="19" height="14" rx="2"/><path d="M-9-6L0 1 9-6"/>',
}

BUTTONS = [
    ("portfolio", "globe", "웹 포트폴리오", "kjw-cloud-portfolio.vercel.app"),
    ("resume", "doc", "이력서", "웹에서 보기"),
    ("email", "mail", "이메일", "jowon7602@gmail.com"),
]


def button(palette: dict[str, str], icon: str, label: str, value: str) -> str:
    W, H = 262.0, 58.0
    cv = Canvas(W, H, palette)
    cv.rect(0.5, 0.5, W - 1, H - 1, "card", rx=10, stroke="card_line")
    cv.rect(10, 14, 3, H - 28, "accent_fill", rx=1.5)
    cv.add(
        f'<g transform="translate(36 29)" fill="none" stroke="{palette["accent"]}" stroke-width="1.6" '
        f'stroke-linecap="round" stroke-linejoin="round">{ICONS[icon]}</g>'
    )
    cv.text(58, 24, label, 11, 700, "muted", track=0.3)
    size = 13.0
    while measure(value, size, 700) > W - 58 - 14:
        size -= 0.5
    cv.text(58, 43, value, size, 700, "ink")
    return cv.svg(f"{label}: {value}")


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    outputs = {}
    for scheme, palette in (("light", LIGHT), ("dark", DARK)):
        outputs[f"profile-desktop-{scheme}.svg"] = desktop(palette)
        outputs[f"profile-mobile-{scheme}.svg"] = mobile(palette)
        for key, icon, label, value in BUTTONS:
            outputs[f"contact-{key}-{scheme}.svg"] = button(palette, icon, label, value)
    for name, svg in outputs.items():
        (ASSETS / name).write_text(svg, encoding="utf-8")
        print(f"{name}: {len(svg.encode()) / 1024:.0f} KB")


if __name__ == "__main__":
    main()
