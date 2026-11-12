/* Week 3: Planted-Effect Lab. Uses the shared engine (practice/shared/engine.js). */

const WORLDS = [
  { name: "One study", blurb: "Noise",
    idea: "An estimate comes from one sample, so it is noisy. When we plant the true effect ourselves, we can see how far one study lands from it.",
    where: "In the notebook: simulate(n, true_effect) does exactly this, and you check the estimate against the truth." },
  { name: "Many studies", blurb: "Intervals",
    idea: "Run the same study again and again and the estimates scatter. A bigger sample shrinks the scatter. A 95% interval should contain the truth about 95 times in 100.",
    where: "In the notebook: the warm-up repeats a study 100 times and counts how often the interval contains the truth." },
  { name: "A confounder", blurb: "Who gets treated",
    idea: "If the people who get the treatment differ from those who do not, a plain comparison mixes the treatment effect with who was treated. Adding the confounder to the model can fix it.",
    where: "In the notebook: Exercise 3 compares a naive and an adjusted estimate on survey data." },
  { name: "Judge the claim", blurb: "Over-claiming",
    idea: "Check what an answer claims, not only the number. Certainty, size, and cause each need their own evidence.",
    where: "In the notebook: Exercise 2 asks you to find the mistakes in an AI-written analysis." },
  { name: "Take it to Colab", blurb: "Real code",
    idea: "You have seen the simulation work. Now run it as real code and check it against the same rule: about 95 in 100.",
    where: "The Week 3 notebook has a warm-up cell like this one." }
];

/* ---------- statistics helpers ---------- */
const randn = () => { let u = 0; while (u === 0) u = Math.random(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * Math.random()); };
const tcrit = df => 1.96 + 2.4 / df + 4.5 / (df * df);
function invert(M) {
  const n = M.length, A = M.map((r, i) => r.concat(Array.from({ length: n }, (_, j) => (i === j ? 1 : 0))));
  for (let i = 0; i < n; i++) {
    let p = i; for (let r = i + 1; r < n; r++) if (Math.abs(A[r][i]) > Math.abs(A[p][i])) p = r;
    [A[i], A[p]] = [A[p], A[i]];
    const d = A[i][i]; for (let c = 0; c < 2 * n; c++) A[i][c] /= d;
    for (let r = 0; r < n; r++) if (r !== i) { const f = A[r][i]; for (let c = 0; c < 2 * n; c++) A[r][c] -= f * A[i][c]; }
  }
  return A.map(r => r.slice(n));
}
function ols(X, y) {
  const n = X.length, k = X[0].length;
  const A = Array.from({ length: k }, () => Array(k).fill(0)), b = Array(k).fill(0);
  for (let i = 0; i < n; i++) for (let a = 0; a < k; a++) { b[a] += X[i][a] * y[i]; for (let c = 0; c < k; c++) A[a][c] += X[i][a] * X[i][c]; }
  const inv = invert(A), beta = inv.map(row => row.reduce((s, v, c) => s + v * b[c], 0));
  let rss = 0; for (let i = 0; i < n; i++) { const f = X[i].reduce((s, v, c) => s + v * beta[c], 0); rss += (y[i] - f) ** 2; }
  const df = n - k, s2 = rss / df;
  return { beta, se: inv.map((r, i) => Math.sqrt(s2 * r[i])), df };
}
function oneStudy(n, effect, noise) {
  for (;;) {
    const X = [], y = []; let n1 = 0;
    for (let i = 0; i < n; i++) { const t = Math.random() < 0.5 ? 1 : 0; n1 += t; X.push([1, t]); y.push(5 + effect * t + noise * randn()); }
    if (n1 < 2 || n - n1 < 2) continue;
    const r = ols(X, y), m = tcrit(r.df) * r.se[1];
    return { est: r.beta[1], lo: r.beta[1] - m, hi: r.beta[1] + m };
  }
}
const f2 = v => (Math.round(v * 100) / 100).toFixed(2).replace("-", "−");
const f1 = v => (Math.round(v * 10) / 10).toFixed(1).replace("-", "−");

/* ---------- chart ---------- */
const tickLabel = t => (Math.abs(t) < 1e-9 ? "0" : String(Math.round(t * 100) / 100).replace("-", "−"));
function niceStep(range) { const raw = range / 5; for (const s of [0.1, 0.2, 0.25, 0.5, 1, 2, 5, 10, 20]) if (s >= raw) return s; return 50; }
function chartSvg(o) {
  const W = 640, pad = 26, rowH = o.rowH, H = o.rows.length * rowH + pad + 40, [a, b] = o.domain;
  const sx = v => pad + ((v - a) / (b - a)) * (W - 2 * pad);
  let s = `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${o.label}" style="width:100%;height:auto;max-width:760px"><rect x="0" y="0" width="${W}" height="${H}" rx="10" style="fill:var(--surface);stroke:var(--line)"/>`;
  const st = niceStep(b - a);
  for (let t = Math.ceil(a / st) * st; t <= b + 1e-9; t += st) {
    const x = sx(t);
    s += `<line x1="${x}" y1="${pad - 8}" x2="${x}" y2="${H - 28}" style="stroke:var(--line);stroke-width:1"/><text x="${x}" y="${H - 10}" text-anchor="middle" font-size="12" style="fill:var(--muted)">${tickLabel(t)}</text>`;
  }
  (o.lines || []).forEach(l => {
    const x = sx(l.x);
    s += `<line x1="${x}" y1="${pad - 8}" x2="${x}" y2="${H - 28}" style="stroke:${l.color};stroke-width:${l.w || 2}" ${l.dash ? 'stroke-dasharray="5 5"' : ""}/>`;
  });
  o.rows.forEach((r, i) => {
    const y = pad + i * rowH + rowH / 2, col = `var(${r.color})`;
    s += `<line x1="${sx(r.lo)}" y1="${y}" x2="${sx(r.hi)}" y2="${y}" style="stroke:${col};stroke-width:${o.rows.length > 30 ? 2 : 5};stroke-linecap:round"/><circle cx="${sx(r.est)}" cy="${y}" r="${o.rows.length > 30 ? 2.2 : 6}" style="fill:${col}"/>`;
  });
  return s + "</svg>";
}
const svgBox = html => { const d = h("div"); d.innerHTML = html; return d; };

/* ---------- widgets ---------- */
function slider(id, label, min, max, step, value, fmt, onchange) {
  const val = h("b", {}, fmt(value));
  const inp = h("input", { id, type: "range", min, max, step, value, "aria-label": label,
    oninput: e => { val.textContent = fmt(+e.target.value); onchange(+e.target.value); } });
  return h("div", { class: "ctrl" }, h("div", { class: "row2" }, h("label", { for: id }, label), val), inp);
}
function choice(opts, onpick) {
  const wrap = h("div", { class: "choice", role: "group" }); let cur = null; const btns = [];
  opts.forEach(o => {
    const b = h("button", { class: "pill", type: "button", onclick: () => { cur = o.v; btns.forEach(x => x.classList.toggle("on", x === b)); onpick && onpick(cur); } }, o.t);
    btns.push(b); wrap.append(b);
  });
  wrap.get = () => cur; wrap.reset = () => { cur = null; btns.forEach(x => x.classList.remove("on")); };
  return wrap;
}
S.lab = { effect: -0.6, n: 100, noise: 2 };
const legend = items => h("div", { class: "legend" }, items.map(([c, t]) => h("span", {}, h("i", { style: `background:var(${c})` }), t)));

/* ---------- levels ---------- */
const LEVELS = [
  { w: 0, kind: "study", title: "One study, known answer",
    task: "Set a true effect, a sample size and the noise. Predict whether the interval will contain the truth, then run a study. Run at least three, changing one setting each time.",
    hint: "Try a small sample first (for example 20), then a large one (for example 300). What happens to how wide the interval is?",
    win: "The estimate is never exactly the truth, and that is not a mistake. A small sample makes it noisier. You can see this in your own runs." },
  { w: 1, kind: "many", title: "Run it 100 times",
    task: "Run the same study 100 times. Predict how many intervals will contain the truth. Then find a sample size where 10 or fewer of the 100 estimates land more than 0.5 away from the true effect.",
    hint: "A bigger sample makes the estimates cluster closer to the truth. Keep increasing it until the count of far-off estimates drops to 10 or fewer.",
    win: "Roughly 95 in 100 intervals contain the truth, and a bigger sample shrinks the scatter. This is the check you will run in Colab." },
  { w: 2, kind: "confound", title: "Who gets the treatment?",
    task: "In this made-up study, students who struggle more are more likely to attend tutoring. The true effect of tutoring is +2 points. Raise the confounding and compare the naive estimate with the adjusted one. Find a setting where the naive estimate has the wrong sign.",
    hint: "With confounding at 0, tutoring is assigned at random and both estimates are close. Raise it until the naive estimate goes below zero.",
    win: "With strong confounding the naive comparison pointed the wrong way, while adjusting for who needed help recovered the truth. A plain comparison mixes the effect with who chose the treatment." },
  { w: 3, kind: "judge", title: "What does each answer claim?",
    task: "An experiment of 40 people, with random assignment, finds that a label raised sharing intent by 0.9 points (95% interval 0.1 to 1.7). Three AI answers describe it. For each, pick the problem, or say there is none.",
    hint: "Ask three questions: does it claim more certainty than one small study can give? Does it treat 'significant' as 'large'? Does it say anything the design cannot support?",
    win: "You checked what each answer claims, not just the number. That is the habit for any statistics an AI reports." },
  { w: 4, kind: "bridge", bridge: true, title: "Run it as real code",
    task: "Open the Week 3 notebook, find the warm-up cell, and run the same simulation there with your own settings." }
];

/* level 1 */
function buildStudy(def) {
  const st = L = { def, runs: 0, token: 0 };
  const chart = h("div"), stats = h("div", { class: "stats" });
  const pred = choice([{ v: "yes", t: "Yes, it will contain the truth" }, { v: "no", t: "No, it will miss the truth" }]);
  const lab = S.lab;
  const ctrls = [
    slider("effect", "True effect", -2, 2, 0.1, lab.effect, f1, v => { lab.effect = v; }),
    slider("n", "People in the study", 10, 400, 10, lab.n, v => String(v), v => { lab.n = v; }),
    slider("noise", "Noise (spread of scores)", 0.5, 4, 0.5, lab.noise, f1, v => { lab.noise = v; })
  ];
  const run = () => {
    const g = pred.get();
    if (!g) { setFb("warn", "Predict first: will the interval contain the true effect?"); return; }
    const r = oneStudy(lab.n, lab.effect, lab.noise), hit = r.lo <= lab.effect && lab.effect <= r.hi;
    const span = Math.max(1.2, Math.abs(lab.effect) + 2.5 * (lab.noise * 2 / Math.sqrt(lab.n)) + 0.5);
    chart.replaceChildren(svgBox(chartSvg({ label: "One simulated study: the estimate and its interval, with the true effect marked", domain: [lab.effect - span, lab.effect + span], rowH: 40,
      lines: [{ x: lab.effect, color: "var(--accent)", w: 3 }, { x: 0, color: "var(--muted)", dash: true }], rows: [{ est: r.est, lo: r.lo, hi: r.hi, color: hit ? "--accent" : "--bad" }] })));
    stats.replaceChildren(
      h("div", { class: "stat truth" }, h("small", {}, "True effect"), h("b", {}, f2(lab.effect))),
      h("div", { class: "stat" }, h("small", {}, "Estimate"), h("b", {}, f2(r.est))),
      h("div", { class: "stat" }, h("small", {}, "Interval"), h("b", {}, `${f2(r.lo)} to ${f2(r.hi)}`)),
      h("div", { class: "stat" }, h("small", {}, "Contains truth?"), h("b", {}, hit ? "Yes" : "No")));
    st.runs++; pred.reset();
    const note = (g === "yes") === hit ? "Your prediction was right." : "Your prediction was different this time.";
    if (st.runs >= 3) { solved(); setFb("good", def.win + " " + note, true); }
    else setFb("info", `Run ${st.runs} of at least 3. ${note} Change one setting and run again.`);
  };
  const left = [h("p", { class: "label" }, "Result"), chart, legend([["--accent", "interval contains the truth"], ["--bad", "interval misses it"]]), stats];
  const right = [...ctrls,
    h("div", { class: "predict" }, h("p", { class: "label" }, "Before you run: will the interval contain the true effect?"), pred),
    h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: run }, "Run one study"), hintBtn(def)),
    h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  chart.append(h("p", { class: "tipline" }, "Pick a prediction, then run a study."));
  return { left, right };
}

/* level 2 */
function buildMany(def) {
  const st = L = { def, token: 0 };
  const chart = h("div"), stats = h("div", { class: "stats" }), lab = S.lab;
  const guess = h("input", { id: "guess", class: "numin", type: "number", min: "0", max: "100", inputmode: "numeric", placeholder: "0 to 100" });
  const ctrls = [
    slider("effect2", "True effect", -2, 2, 0.1, lab.effect, f1, v => { lab.effect = v; }),
    slider("n2", "People in each study", 10, 400, 10, lab.n, v => String(v), v => { lab.n = v; }),
    slider("noise2", "Noise (spread of scores)", 0.5, 4, 0.5, lab.noise, f1, v => { lab.noise = v; })
  ];
  const run = () => {
    if (guess.value === "") { setFb("warn", "Predict first: how many of 100 intervals will contain the true effect?"); guess.focus(); return; }
    const rows = [], truth = lab.effect; let covered = 0, far = 0, lo = Infinity, hi = -Infinity;
    for (let i = 0; i < 100; i++) {
      const r = oneStudy(lab.n, truth, lab.noise), hit = r.lo <= truth && truth <= r.hi;
      covered += hit; far += Math.abs(r.est - truth) > 0.5; lo = Math.min(lo, r.est); hi = Math.max(hi, r.est);
      rows.push({ est: r.est, lo: r.lo, hi: r.hi, color: hit ? "--accent" : "--bad" });
    }
    const span = 3.2 * (lab.noise * 2 / Math.sqrt(lab.n)) + 0.3;
    chart.replaceChildren(svgBox(chartSvg({ label: "One hundred simulated studies. Each line is an interval; the vertical line is the true effect", domain: [truth - span, truth + span], rowH: 5.5,
      lines: [{ x: truth, color: "var(--accent)", w: 2 }], rows })));
    stats.replaceChildren(
      h("div", { class: "stat" }, h("small", {}, "Contain the truth"), h("b", {}, `${covered} / 100`)),
      h("div", { class: "stat" }, h("small", {}, "Estimates range"), h("b", {}, `${f2(lo)} to ${f2(hi)}`)),
      h("div", { class: "stat" }, h("small", {}, "More than 0.5 away"), h("b", {}, `${far} / 100`)));
    const g = parseInt(guess.value, 10), note = Math.abs(g - covered) <= 5 ? `You predicted ${g}: close.` : `You predicted ${g}; it was ${covered}.`;
    if (far <= 10) { solved(); setFb("good", def.win + " " + note, true); }
    else setFb("info", `${note} ${far} of 100 estimates are more than 0.5 from the truth. Change the sample size and try again to get that to 10 or fewer.`);
  };
  const left = [h("p", { class: "label" }, "One hundred studies"), chart, legend([["--accent", "interval contains the truth"], ["--bad", "interval misses it"]]), stats];
  const right = [...ctrls,
    h("div", { class: "predict" }, h("label", { class: "label", for: "guess" }, "Before you run: how many of 100 intervals will contain the truth?"), guess),
    h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: run }, "Run 100 studies"), hintBtn(def)),
    h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  chart.append(h("p", { class: "tipline" }, "Enter a prediction, then run 100 studies."));
  return { left, right };
}

/* level 3 */
function buildConfound(def) {
  const st = L = { def, runs: 0, flipped: false, token: 0 }, TRUE = 2;
  let s = 0;
  const chart = h("div"), stats = h("div", { class: "stats" });
  const pred = choice([{ v: "naive", t: "The naive estimate will be closer" }, { v: "adj", t: "The adjusted estimate will be closer" }, { v: "same", t: "About the same" }]);
  const ctrl = slider("conf", "Confounding (how strongly need predicts attending)", 0, 2, 0.1, s, f1, v => { s = v; });
  const run = () => {
    const g = pred.get();
    if (!g) { setFb("warn", "Predict first: which estimate will be closer to the truth?"); return; }
    const n = 600, X1 = [], X2 = [], y = [];
    for (let i = 0; i < n; i++) {
      const need = Math.floor(Math.random() * 4), p = 1 / (1 + Math.exp(-(-0.2 + s * (need - 1.5)))), t = Math.random() < p ? 1 : 0;
      X1.push([1, t]); X2.push([1, t, need]); y.push(70 - 6 * need + TRUE * t + 6 * randn());
    }
    const a = ols(X1, y), b = ols(X2, y), m1 = tcrit(a.df) * a.se[1], m2 = tcrit(b.df) * b.se[1];
    const naive = a.beta[1], adj = b.beta[1];
    chart.replaceChildren(svgBox(chartSvg({ label: "Naive and adjusted estimates of the effect of tutoring, with the true effect marked", domain: [-10, 5], rowH: 44,
      lines: [{ x: TRUE, color: "var(--accent)", w: 3 }, { x: 0, color: "var(--muted)", dash: true }],
      rows: [{ est: naive, lo: naive - m1, hi: naive + m1, color: "--sun" }, { est: adj, lo: adj - m2, hi: adj + m2, color: "--water" }] })));
    stats.replaceChildren(
      h("div", { class: "stat truth" }, h("small", {}, "True effect"), h("b", {}, "+2.00")),
      h("div", { class: "stat" }, h("small", {}, "Naive (top)"), h("b", {}, f2(naive))),
      h("div", { class: "stat" }, h("small", {}, "Adjusted (bottom)"), h("b", {}, f2(adj))));
    st.runs++; pred.reset();
    const closer = Math.abs(adj - TRUE) < Math.abs(naive - TRUE) ? "adj" : "naive";
    const note = (g === closer || (g === "same" && Math.abs(Math.abs(adj - TRUE) - Math.abs(naive - TRUE)) < 0.5)) ? "Your prediction was right." : "Your prediction was different this time.";
    if (naive < 0) st.flipped = true;
    if (st.flipped && st.runs >= 2) { solved(); setFb("good", def.win + " " + note, true); }
    else setFb("info", `${note} ${st.flipped ? "" : "Raise the confounding and run again until the naive estimate goes below zero."}`);
  };
  const left = [h("p", { class: "label" }, "Naive (yellow) versus adjusted (blue)"), chart, legend([["--sun", "naive: tutoring only"], ["--water", "adjusted: tutoring plus how much help a student needed"]]), stats];
  const right = [ctrl,
    h("div", { class: "givens" }, "600 students. Exam score = 70, minus 6 for each level of need, plus 2 if they attended tutoring, plus noise. Students with more need are more likely to attend."),
    h("div", { class: "predict" }, h("p", { class: "label" }, "Before you run: which will be closer to the truth?"), pred),
    h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: run }, "Run study"), hintBtn(def)),
    h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  chart.append(h("p", { class: "tipline" }, "Set the confounding, make a prediction, then run."));
  return { left, right };
}

/* level 4 */
const CLAIMS = [
  { q: "The label increased sharing by 0.9 points, which proves that labels make people share more.", ans: "certain", why: "\"Proves\" claims more certainty than one small study can give. The interval runs from 0.1 to 1.7, so the true effect could be small." },
  { q: "In this study, people who saw the label shared more, by about 0.9 points (interval 0.1 to 1.7). With only 40 people the estimate is imprecise, so the true effect could be small.", ans: "ok", why: "This reports the estimate and its uncertainty, and says what the sample size means. Random assignment supports a causal reading, which it does not overstate." },
  { q: "The result is statistically significant, so the effect is large and important.", ans: "size", why: "Significant does not mean large. The estimate is 0.9 points on a 0 to 10 scale, with an interval from 0.1 to 1.7. The size has to be judged from the estimate, not from the p-value." }
];
const ISSUES = [{ v: "ok", t: "No problem" }, { v: "certain", t: "Claims too much certainty from one small study" }, { v: "size", t: "Treats “significant” as “large”" }, { v: "design", t: "Ignores that people were not randomly assigned" }];
function buildJudge(def) {
  const st = L = { def, token: 0 }, picks = CLAIMS.map(() => choice(ISSUES));
  const cards = CLAIMS.map((c, i) => h("div", { class: "claim", id: "claim" + i }, h("p", { class: "label" }, "Answer " + "ABC"[i]), h("blockquote", {}, c.q), picks[i]));
  const check = () => {
    if (picks.some(p => !p.get())) { setFb("warn", "Pick a problem (or No problem) for every answer."); return; }
    const msgs = []; let all = true;
    CLAIMS.forEach((c, i) => {
      const ok = picks[i].get() === c.ans; all = all && ok;
      cards[i].className = "claim " + (ok ? "right" : "wrong");
      msgs.push(`Answer ${"ABC"[i]}: ${ok ? "right. " : "not quite. "}${c.why}`);
    });
    if (all) { solved(); setFb("good", def.win + " " + msgs.join(" "), true); } else setFb("bad", msgs.join(" "));
  };
  const left = [h("div", { class: "givens" }, "The study: 40 people, randomly assigned to see an AI label or not. Outcome: sharing intent, 0 to 10. Estimate +0.9, 95% interval 0.1 to 1.7."), ...cards];
  const right = [h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: check }, "Check my answers"), hintBtn(def)), h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  return { left, right };
}

/* bridge */
function labCode() {
  const l = S.lab;
  return [
    "import numpy as np", "import pandas as pd", "import statsmodels.formula.api as smf", "",
    "rng = np.random.default_rng()", "",
    `TRUE_EFFECT = ${l.effect}`, `N = ${l.n}`, `NOISE = ${l.noise}`, "",
    "def simulate(n, true_effect, noise):", "    treated = rng.integers(0, 2, n)", "    y = 5 + true_effect * treated + rng.normal(0, noise, n)",
    '    return pd.DataFrame({"treated": treated, "y": y})', "",
    "covered = 0", "for _ in range(100):", '    fit = smf.ols("y ~ treated", data=simulate(N, TRUE_EFFECT, NOISE)).fit()',
    '    lo, hi = fit.conf_int().loc["treated"]', "    covered += lo <= TRUE_EFFECT <= hi", "",
    'print("Intervals that contained the truth:", covered, "out of 100")',
    'assert 85 <= covered <= 100, "A 95% interval should contain the truth about 95 times in 100."'
  ].join("\n");
}
function buildBridge(def) {
  const prompt = "Write Python that simulates a two-group study with a known true effect, fits a regression with statsmodels, and repeats it 100 times to count how often the 95% interval contains the true effect. Explain each line in one sentence.";
  const left = [codeCard("Task 1: your simulation as code", labCode(), "This uses the settings you chose in levels 1 and 2. Paste it into the notebook's warm-up cell and run it.")];
  const right = [
    codeCard("Task 2: ask an AI, then compare", prompt, "Paste this into your AI assistant. Is its code the same as Task 1? Does it check against the known truth?"),
    h("div", { class: "tray" }, h("p", { class: "label" }, "Task 3: check"), h("p", {}, "Run it a few times. The count should be close to 95. If it is far from 95, something is wrong with the code. Log one check you ran.")),
    h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: () => { solved(); setFb("good", "Done. In Exercise 2 you will test AI-written code against a known answer, the same way."); } }, "I ran all three")),
    h("div", { id: "fb", class: "fb", "aria-live": "polite" })
  ];
  return { left, right };
}

BUILDERS.study = buildStudy; BUILDERS.many = buildMany; BUILDERS.confound = buildConfound; BUILDERS.judge = buildJudge; BUILDERS.bridge = buildBridge;
boot("cactus-planted-effect-done");
