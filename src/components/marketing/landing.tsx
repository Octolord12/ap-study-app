import Link from "next/link";
import { getDb } from "@/lib/db";
import { listCourses } from "@/lib/study/queries";
import { countWord } from "@/lib/count-word";
import { describeExamFormat, formatDuration } from "@/lib/content/exam-format";
import { TESTIMONIALS } from "@/lib/marketing/testimonials";
import { MINIMUM_AGE } from "@/lib/age";
import { LandingWaitlist } from "@/components/marketing/landing-waitlist";
import styles from "./landing.module.css";

const FAQ = [
  {
    q: "Are these College Board questions?",
    a: "No. They are original practice questions and may contain mistakes. AP® is a College Board trademark, and this site is not affiliated with it.",
  },
  { q: "Who can use the app?", a: `Anyone ${MINIMUM_AGE} or older.` },
  { q: "How are free-response answers graded?", a: "You grade your own work against the rubric and a sample answer." },
  {
    q: "How does the exam score estimate work?",
    a: "It estimates a score range from your multiple-choice accuracy and labels it as an estimate.",
  },
  {
    q: "Is the leaderboard optional?",
    a: "Yes. Leaderboards cover friends and classes, and you can opt out in Settings.",
  },
];

// Signed-out landing page, ported from the taste-skill prototype (design/taste-landing handoff). Every
// number it states about the question bank is read from the database, so the copy can't drift from it.
// The screens in it are drawn examples: a real CSA-style question, the real Calc AB bank question, and
// illustrative review, exam, rubric and level panels (labelled as examples on the page).
export async function Landing() {
  const db = getDb();
  const [courses, mcqCounts, frqCounts] = await Promise.all([
    listCourses(),
    db.question.groupBy({ by: ["courseId"], _count: { _all: true } }),
    db.fRQPrompt.groupBy({ by: ["courseId"], _count: { _all: true } }),
  ]);
  const countFor = (rows: { courseId: string; _count: { _all: number } }[], courseId: string) =>
    rows.find((r) => r.courseId === courseId)?._count._all ?? 0;
  const totalMcq = mcqCounts.reduce((sum, r) => sum + r._count._all, 0);
  const totalFrq = frqCounts.reduce((sum, r) => sum + r._count._all, 0);
  const examsWord = countWord(courses.length);
  const quote = TESTIMONIALS[0];

  return (
    <div className={styles.lp}>
      <section className={styles.hero} aria-labelledby="hero-h">
        <div className={styles.wrap}>
          <div className={styles.heroText}>
            <a className={styles.pill} href="#exams">
              <span>{countWord(courses.length, true)} AP exams</span>
              <span>See the formats</span>
            </a>
            <span className={styles.ghost} aria-hidden="true">
              AP
            </span>
            <h1 id="hero-h" className={styles.h1}>
              <span className={styles.line}>
                <span style={{ ["--i" as string]: 0 }}>AP practice</span>
              </span>{" "}
              <span className={styles.line}>
                <span style={{ ["--i" as string]: 1 }}>that explains</span>
              </span>{" "}
              <span className={styles.line}>
                <span style={{ ["--i" as string]: 2 }}>
                  <span className="hl">every miss</span>
                </span>
              </span>
            </h1>
            <span className={`sticker ${styles.heroSticker}`} aria-hidden="true">
              {countWord(courses.length, true)}
              <br />
              AP exams
            </span>
            <p className={styles.heroLead}>
              Answer a question, then read why each choice is right or wrong. {totalMcq.toLocaleString("en-US")} multiple-choice questions and {totalFrq}{" "}
              free-response prompts across {examsWord} exams.
            </p>
            <div className={styles.btnRow}>
              <Link href="/signup" className={`${styles.btn} ${styles.btnPrimary}`}>
                Create an account
              </Link>
              <a href="#explained" className={`${styles.btn} ${styles.btnGhost}`}>
                See an explained answer
              </a>
            </div>
          </div>
          <div className={styles.frame}>
            <div
              className={`${styles.screen} ${styles.win}`}
              role="img"
              aria-label="An AP Computer Science A question answered wrong, with the reason shown for every choice"
            >
              <div className={styles.winBar} aria-hidden="true">
                <span className={styles.winDots}>
                  <i />
                  <i />
                  <i />
                </span>
                <b>AP Computer Science A</b>
                <span className={styles.winHide}>Unit 1 · Primitive types</span>
                <span className={styles.sp} />
                <span>Question 4 of 30</span>
              </div>
              <div className={styles.winBody} aria-hidden="true">
                <ol className={styles.winList}>
                  <li>
                    <span className={`${styles.dot} ${styles.dotOk}`}>&#10003;</span>Integer division
                  </li>
                  <li>
                    <span className={`${styles.dot} ${styles.dotOk}`}>&#10003;</span>Casting a double
                  </li>
                  <li>
                    <span className={`${styles.dot} ${styles.dotBad}`}>&#10005;</span>Compound assignment
                  </li>
                  <li className={styles.isOn}>
                    <span className={styles.dot}>4</span>Division and remainder
                  </li>
                  <li>
                    <span className={styles.dot}>5</span>Parsing a String
                  </li>
                  <li>
                    <span className={styles.dot}>6</span>Overflow of an int
                  </li>
                </ol>
                <div className={styles.winQ}>
                  <p className={styles.qStem}>
                    What does <code>System.out.println(7 / 2 + 7 % 2);</code> print?
                  </p>
                  <ul className={styles.qCh}>
                    <li>
                      <b>A</b>
                      <span className={styles.mono}>3.5</span>
                      <em>Integer division drops the .5, so 7 / 2 is 3.</em>
                    </li>
                    <li className={styles.isBad}>
                      <b>B</b>
                      <span className={styles.mono}>3</span>
                      <em>Right for 7 / 2, but 7 % 2 adds another 1.</em>
                      <span className={styles.tag}>Your answer</span>
                    </li>
                    <li className={styles.isOk}>
                      <b>C</b>
                      <span className={styles.mono}>4</span>
                      <em>3 from 7 / 2, plus 1 from 7 % 2.</em>
                      <span className={styles.tag}>Correct</span>
                    </li>
                    <li>
                      <b>D</b>
                      <span className={styles.mono}>4.5</span>
                      <em>Neither term is a decimal, so no .5 appears.</em>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className={styles.section} id="explained" aria-labelledby="explained-h">
        <div className={styles.wrap}>
          <div className={styles.grid2}>
            <div className={styles.stack}>
              <h2 id="explained-h" className={styles.h2}>
                Every answer choice explained
              </h2>
              <p className={styles.lead}>
                A wrong pick is not a dead end. Each choice shows the mistake behind it, so you learn what to fix instead of only what to remember.
              </p>
              <p>
                <a className={styles.link} href="#practice">
                  See how review works
                </a>
              </p>
            </div>
            <div
              className={`${styles.screen} ${styles.qcard}`}
              role="img"
              aria-label="An AP Calculus AB question with the reason shown under every answer choice"
            >
              <p className={styles.qcardMeta}>AP Calculus AB · Unit 2 · Medium</p>
              <p className={styles.qcardStem}>How is the instantaneous rate of change of f(x) at x = a defined, in terms of a limit?</p>
              <ul aria-hidden="true">
                <li className={styles.isOk}>
                  <b>A</b>
                  <span>lim h&#8594;0 [f(a + h) &#8722; f(a)] / h</span>
                  <p>The standard difference-quotient definition of the derivative at x = a.</p>
                </li>
                <li>
                  <b>B</b>
                  <span>lim h&#8594;0 [f(a) + h]</span>
                  <p>This only adds h to f(a). It is not a rate of change.</p>
                </li>
                <li>
                  <b>C</b>
                  <span>f(a) / a</span>
                  <p>The value divided by the x-value has nothing to do with a rate of change.</p>
                </li>
                <li>
                  <b>D</b>
                  <span>lim h&#8594;&#8734; [f(a + h) &#8722; f(a)] / h</span>
                  <p>The interval must shrink toward 0, not grow without bound.</p>
                </li>
              </ul>
            </div>
          </div>
          {quote ? (
            <figure className={styles.quote}>
              <blockquote>&ldquo;{quote.quote}&rdquo;</blockquote>
              <figcaption>
                {quote.name}
                {quote.course ? ` · ${quote.course}` : ""}
                {quote.apScore ? ` · Scored ${quote.apScore}` : ""}
              </figcaption>
            </figure>
          ) : null}
        </div>
      </section>

      <section className={`${styles.section} ${styles.band}`} id="practice" aria-labelledby="practice-h">
        <div className={styles.wrap}>
          <div className={styles.bandHead}>
            <h2 id="practice-h" className={styles.h2}>
              Practice that follows your misses
            </h2>
            <a className={styles.link} href="#exams">
              See the exam formats
            </a>
          </div>
          <div className={styles.cards}>
            <article className={styles.card}>
              <h3>Brings missed questions back</h3>
              <p>A miss returns the next day. Questions you answer right come back later.</p>
              <div className={styles.panel}>
                <div className={`${styles.screen} ${styles.mini}`} role="img" aria-label="Example review queue: four topics due today">
                  <h4>Due for review today</h4>
                  <div className={styles.row}>
                    <span>Compound assignment</span>
                    <span>missed 2 times</span>
                  </div>
                  <div className={styles.row}>
                    <span>Integer division</span>
                    <span>missed once</span>
                  </div>
                  <div className={styles.row}>
                    <span>Recursion base cases</span>
                    <span>due today</span>
                  </div>
                  <div className={styles.row}>
                    <span>2D array traversal</span>
                    <span>due today</span>
                  </div>
                </div>
              </div>
            </article>
            <article className={styles.card}>
              <h3>Runs a timed full exam</h3>
              <p>Real section counts and one clock, then an estimated score range.</p>
              <div className={styles.panel}>
                <div className={`${styles.screen} ${styles.mini}`} role="img" aria-label="Example exam clock at 3:09:59 for AP Calculus AB">
                  <h4>AP Calculus AB · Full exam</h4>
                  <p className={styles.big}>3:09:59</p>
                  <div className={styles.row}>
                    <span>Multiple choice</span>
                    <span>42 questions</span>
                  </div>
                  <div className={styles.row}>
                    <span>Free response</span>
                    <span>6 questions</span>
                  </div>
                  <div className={styles.bar} aria-hidden="true">
                    <i style={{ width: "0%" }} />
                  </div>
                </div>
              </div>
            </article>
            <article className={styles.card}>
              <h3>Grades free-response practice by rubric</h3>
              <p>Each prompt has a rubric and a sample answer. You mark your own points.</p>
              <div className={styles.panel}>
                <div className={`${styles.screen} ${styles.mini}`} role="img" aria-label="Example rubric with three of four points checked">
                  <h4>Rubric · 4 points</h4>
                  <div className={styles.chk}>
                    <span className={`${styles.box} ${styles.boxOn}`} />
                    <span>States the claim</span>
                    <span>1</span>
                  </div>
                  <div className={styles.chk}>
                    <span className={`${styles.box} ${styles.boxOn}`} />
                    <span>Cites specific evidence</span>
                    <span>1</span>
                  </div>
                  <div className={styles.chk}>
                    <span className={`${styles.box} ${styles.boxOn}`} />
                    <span>Links evidence to the claim</span>
                    <span>1</span>
                  </div>
                  <div className={styles.chk}>
                    <span className={styles.box} />
                    <span>Addresses a counterargument</span>
                    <span>0</span>
                  </div>
                </div>
              </div>
            </article>
            <article className={styles.card}>
              <h3>Rewards a daily practice streak</h3>
              <p>Earn XP for correct answers. Beat a unit&apos;s boss battle with 70% or more.</p>
              <div className={styles.panel}>
                <div className={`${styles.screen} ${styles.mini}`} role="img" aria-label="Example level and streak with a boss battle for Unit 3">
                  <h4>Level 4 · 280 of 400 XP</h4>
                  <div className={styles.bar} aria-hidden="true">
                    <i style={{ width: "70%" }} />
                  </div>
                  <div className={styles.row}>
                    <span>Streak</span>
                    <span className={styles.tally} aria-hidden="true">
                      <i className={styles.on} />
                      <i className={styles.on} />
                      <i className={styles.on} />
                      <i className={styles.on} />
                      <i className={styles.on} />
                      <i />
                      <i />
                    </span>
                  </div>
                  <div className={styles.row}>
                    <span>Unit 3 boss battle</span>
                    <span>pass at 70%</span>
                  </div>
                </div>
              </div>
            </article>
          </div>
          <p className={`${styles.fineprint} ${styles.examples}`}>The screens on this page are examples, not a real student&apos;s results.</p>
        </div>
      </section>

      <section className={styles.section} id="exams" aria-labelledby="exams-h">
        <div className={styles.wrap}>
          <div className={styles.grid2}>
            <div className={styles.stack}>
              <h2 id="exams-h" className={styles.h2}>
                {countWord(courses.length, true)} AP exams
              </h2>
              <p className={styles.lead}>Each exam keeps its real section counts and timing. A full simulation gives an estimated score range.</p>
              <div
                className={`${styles.screen} ${styles.mini} ${styles.est}`}
                role="img"
                aria-label="Example AP Biology exam results: estimated score 4 to 5 and the units where points were lost"
              >
                <h4>Example · AP Biology exam results</h4>
                <p className={styles.big}>Estimated score 4 to 5</p>
                <div className={styles.bar} aria-hidden="true">
                  <i style={{ width: "78%" }} />
                </div>
                <p className={styles.fineprint}>An estimate from multiple-choice accuracy, not a prediction.</p>
                <h4 className={styles.estHead}>Where you lost points</h4>
                <div className={styles.row}>
                  <span>Unit 4 · Cell communication and cell cycle</span>
                  <span>5 missed</span>
                </div>
                <div className={styles.row}>
                  <span>Unit 6 · Gene expression and regulation</span>
                  <span>4 missed</span>
                </div>
                <div className={styles.row}>
                  <span>Unit 3 · Cellular energetics</span>
                  <span>2 missed</span>
                </div>
                <div className={styles.row}>
                  <span>Unit 8 · Ecology</span>
                  <span>1 missed</span>
                </div>
              </div>
            </div>
            <div>
              <p className={`${styles.fineprint} ${styles.rowsKey}`}>Questions + free-response prompts in each exam.</p>
              <ul className={styles.rows}>
                {courses.map((course) => {
                  const format = course.examFormat as unknown as Parameters<typeof describeExamFormat>[0];
                  return (
                    <li key={course.id}>
                      <span className={styles.rowsName}>{course.name}</span>
                      <span className={styles.rowsValue}>
                        {countFor(mcqCounts, course.id)} + {countFor(frqCounts, course.id)}
                      </span>
                      <p>
                        {describeExamFormat(format)} · {formatDuration(format.totalDurationMinutes)}
                      </p>
                    </li>
                  );
                })}
              </ul>
            </div>
          </div>
        </div>
      </section>

      <section className={`${styles.statement}`} id="learn" aria-label="Learn from every miss">
        <div className={styles.wrap}>
          <h2 className={styles.statementType}>Learn from every miss</h2>
          <p>Each wrong choice comes with the mistake behind it, so the next question on that idea goes better.</p>
        </div>
      </section>

      <section className={styles.section} id="questions" aria-labelledby="questions-h">
        <div className={styles.wrap}>
          <div className={styles.grid2}>
            <div className={styles.stack}>
              <h2 id="questions-h" className={styles.h2}>
                Questions
              </h2>
              <p className={styles.lead}>Found a mistake? Report it from the question you are on.</p>
              <div className={`${styles.screen} ${styles.mini} ${styles.rep}`} role="img" aria-label="Links shown under every question: review this concept and report a problem">
                <h4>Under every question</h4>
                <div className={styles.row}>
                  <span>Review this concept</span>
                  <span>topic refresher</span>
                </div>
                <div className={styles.row}>
                  <span>Report a problem</span>
                  <span>sent by email</span>
                </div>
              </div>
              <LandingWaitlist />
            </div>
            <div className={styles.faq}>
              {FAQ.map((item) => (
                <div key={item.q} className={styles.faqItem}>
                  <h3>{item.q}</h3>
                  <p>{item.a}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      <section className={styles.closing} aria-labelledby="close-h">
        <div className={styles.wrap}>
          <h2 id="close-h" className={styles.h2}>
            Start practicing for your AP exam
          </h2>
          <p className={styles.lead}>For students {MINIMUM_AGE} and older.</p>
          <Link href="/signup" className={`${styles.btn} ${styles.btnPrimary} ${styles.btnXl}`}>
            Create an account
          </Link>
          <Link href="/login" className={styles.link}>
            I already have one
          </Link>
        </div>
      </section>
    </div>
  );
}
