"""AP CSA authoring helpers. Every output shown in a question is produced by compiling and running the
code with a real JDK (set JAVA_HOME, or the scratch JDK path below), and every wrong choice is the output of
a deliberately mutated program, so each distractor is a specific, reproducible mistake."""
import glob, os, subprocess, sys, tempfile, textwrap

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from authoring import *

SCRATCH = "/private/tmp/claude-501/-Users-viraj-Desktop-Claude-AP-Study-app/7e393e46-94d2-46d7-9276-a5e1e012aa5f/scratchpad/jdk"


def _java_home():
    if os.environ.get("JAVA_HOME"):
        return os.environ["JAVA_HOME"]
    found = glob.glob(os.path.join(SCRATCH, "jdk-*", "Contents", "Home"))
    if not found:
        raise RuntimeError("No JDK found: set JAVA_HOME")
    return found[0]


JH = _java_home()
JAVA, JAVAC = os.path.join(JH, "bin", "java"), os.path.join(JH, "bin", "javac")


def program(body="", members="", classes=""):
    """A full source file. Main comes first (single-file launch mode runs the first class)."""
    return f"import java.util.*;\n\npublic class Main {{\n{members}\n    public static void main(String[] args) {{\n{body}\n    }}\n}}\n{classes}\n"


def run(src, timeout=60):
    """Compile and run a complete source file; return stdout with trailing whitespace stripped."""
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "Main.java")
        with open(path, "w") as fh:
            fh.write(src)
        p = subprocess.run([JAVA, "-Xshare:auto", "-XX:TieredStopAtLevel=1", path], capture_output=True, text=True, timeout=timeout)
        if p.returncode != 0:
            raise RuntimeError(f"Java failed:\n{p.stderr}\n--- source ---\n{src}")
        return p.stdout.rstrip()


def compile_error(src):
    """Return the compiler's error output for a source file, or None if it compiles."""
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "Main.java")
        with open(path, "w") as fh:
            fh.write(src)
        p = subprocess.run([JAVAC, "-d", d, path], capture_output=True, text=True, timeout=60)
        return None if p.returncode == 0 else p.stderr


def code(text):
    return "```java\n" + text.strip("\n") + "\n```"


def shown(body="", members="", classes=""):
    """The code displayed in a stem: the class definitions and methods first, then the segment that runs."""
    parts = []
    first = "\n\n".join(textwrap.dedent(x).strip("\n") for x in (classes, members) if x.strip())
    if first:
        parts.append(code(first))
    if body.strip():
        parts.append(code(body))
    return "\n\n".join(parts)


def mutate(src, old, new, count=1):
    assert old in src, f"mutation target not found: {old!r}"
    return src.replace(old, new, count)


def out_text(o):
    """Output as a choice text: multi-line output keeps its line breaks."""
    return o


def trace(B, topic, question, body="", members="", classes="", mutants=(), manual=(), explanation="", correct_expl="", tail=""):
    """Ask what a program prints. `mutants` are (old, new, why) replacements applied to the full source; each
    mutant's real output becomes a wrong choice, and `why` explains the mistake that would produce it."""
    base = program(body, members, classes)
    right = run(base)
    wrongs, seen = [], {right}
    for old, new, why in mutants:
        w = run(mutate(base, old, new))
        assert w not in seen, f"mutant output repeats an existing choice ({w!r}) for: {old!r} -> {new!r}"
        seen.add(w)
        wrongs.append(ch(w, why))
    for text, why in manual:
        assert text not in seen, f"manual wrong choice repeats an output: {text!r}"
        seen.add(text)
        wrongs.append(ch(text, why))
    stem = question + "\n\n" + shown(body, members, classes) + (("\n\n" + tail) if tail else "")
    B.mcq(topic, stem, ch(right, correct_expl or f"Tracing the code gives exactly this output."), wrongs, explanation)
    return right


def bank(n, slug):
    return Bank("ap-csa", "ap-csa", n, slug)


def verify(members, tests, classes=""):
    """Run each test expression with the given methods/classes and check every printed value."""
    body = "\n".join(f"        System.out.println({expr});" for expr, _ in tests)
    got = run(program(body, members, classes)).split("\n")
    want = [str(w) for _, w in tests]
    assert got == want, f"verification failed:\n got  {got}\n want {want}"
