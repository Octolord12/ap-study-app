"""Writes content/ap-csa/refreshers/unit-N.json from the u1.py..u10.py scripts in this folder (see ../refreshers_lib.py).

Every Java example in a refresher goes through `code(...)`, which returns the fenced block for the markdown AND records the
complete program with the output the text claims. `finish(unit, entries)` writes the JSON and, when a JDK is available
(JAVA_HOME, or a Temurin JDK unpacked in the session scratch folder), compiles and runs every recorded program and fails
if the real output differs from the text. With no JDK it says how many examples were NOT machine-checked, so the number
is never a surprise. Edit the scripts, not the JSON.

Layout of every refresher: ### The idea, ### Key facts, ### Watch out for, ### Worked example.
Avoid "$" in examples (the validator counts it as an unclosed math delimiter, even in code).
"""
import glob, os, re, subprocess, sys, tempfile, textwrap

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import refreshers_lib

SCRATCH = "/private/tmp/claude-501/-Users-viraj-Desktop-Claude-AP-Study-app/7e393e46-94d2-46d7-9276-a5e1e012aa5f/scratchpad/jdk"
_checks = []


def _java_home():
    if os.environ.get("JAVA_HOME") and os.path.exists(os.path.join(os.environ["JAVA_HOME"], "bin", "javac")):
        return os.environ["JAVA_HOME"]
    found = glob.glob(os.path.join(SCRATCH, "jdk-*", "Contents", "Home")) + glob.glob(os.path.join(SCRATCH, "jdk-*"))
    return next((f for f in found if os.path.exists(os.path.join(f, "bin", "javac"))), None)


def program(body="", members="", classes=""):
    """A full source file. Main comes first (single-file launch mode runs the first class)."""
    return f"import java.util.*;\n\npublic class Main {{\n{members}\n    public static void main(String[] args) {{\n{body}\n    }}\n}}\n{classes}\n"


def code(body, out=None, members="", classes="", show_classes=False, show_members=False):
    """The fenced ```java block for `body`. `out` is the exact stdout the text claims (None = only check it compiles).
    `members` are static helpers inside Main and `classes` are extra top-level classes; either is shown above the
    body when show_classes / show_members is true, otherwise it only exists for the check."""
    body = textwrap.dedent(body).strip("\n")
    members = textwrap.dedent(members).strip("\n")
    classes = textwrap.dedent(classes).strip("\n")
    parts = []
    if show_classes and classes:
        parts.append(classes)
    if show_members and members:
        parts.append(members)
    parts.append(body)
    shown = "\n\n".join(parts)
    # A top-level class can only be public in a file of its own name; the check puts everything in Main.java.
    check_classes = re.sub(r"^public class", "class", classes, flags=re.M)
    indent = lambda text, n: "\n".join((" " * n + l) if l else l for l in text.split("\n"))
    _checks.append({"src": program(indent(body, 8), indent(members, 4), check_classes), "out": out, "label": body.split("\n")[0][:60]})
    return "```java\n" + shown + "\n```"


def finish(unit_number, entries):
    refreshers_lib.write("ap-csa", unit_number, entries)
    checks = list(_checks)
    jh = _java_home()
    if not jh:
        print(f"  {len(checks)} Java example(s) NOT machine-checked (no JDK found: set JAVA_HOME)")
        return
    for c in checks:
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "Main.java")
            open(path, "w").write(c["src"])
            p = subprocess.run([os.path.join(jh, "bin", "java"), path], capture_output=True, text=True, timeout=60)
        assert p.returncode == 0, f"Java failed for '{c['label']}':\n{p.stderr}\n{c['src']}"
        if c["out"] is not None:
            assert p.stdout.rstrip() == c["out"].rstrip(), f"'{c['label']}': printed\n{p.stdout!r}\nbut the text says\n{c['out']!r}"
    print(f"  {len(checks)} Java example(s) compiled and run: output matches the text")
