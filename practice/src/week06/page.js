/* Week 6: Can You Trust the Labeler? Uses the shared engine (practice/shared/engine.js). All messages and numbers are invented. */

const WORLDS = [
  { name: "Accuracy", blurb: "Counts of hits and misses",
    idea: "When the thing you look for is rare, a labeler that says \"no\" every time has high accuracy and finds nothing. Accuracy alone cannot tell a useful labeler from a useless one.",
    where: "In the notebook: Exercise 1 compares accuracy with the \"always no\" baseline, then adds precision and recall." },
  { name: "Beyond chance", blurb: "Kappa",
    idea: "Two labelers who each say \"no\" most of the time will agree often by luck. Cohen's kappa asks how much they agree beyond what chance alone gives.",
    where: "In the notebook: Exercise 1 computes kappa for two labels." },
  { name: "Why they disagree", blurb: "Error analysis",
    idea: "A disagreement can mean the labeler is wrong, the codebook did not say, or the human label is questionable. You only learn which by reading the cases.",
    where: "In the notebook: Exercise 2 asks you to read disagreements and sort them." },
  { name: "Say what you found", blurb: "Claims",
    idea: "A result supports some claims and not others. Say what the numbers show, with the sample size and what you compared against.",
    where: "In the notebook: Exercise 4 is a bug hunt on an evaluation that looks fine." },
  { name: "Take it to Colab", blurb: "Real code",
    idea: "You have judged a result by eye. Now compute the measures on 20 labels.",
    where: "The Week 6 notebook warm-up uses the same kind of lists." }
];

const choose = (opts, onpick) => {
  const wrap = h("div", { class: "choice", role: "group" }); let cur = null; const btns = [];
  opts.forEach(o => {
    const b = h("button", { class: "pill", type: "button", onclick: () => { cur = o.v; btns.forEach(x => x.classList.toggle("on", x === b)); onpick && onpick(cur); } }, o.t);
    btns.push(b); wrap.append(b);
  });
  wrap.get = () => cur; return wrap;
};
const pct = x => (isFinite(x) ? Math.round(x * 100) + "%" : "n/a");
function metrics(tp, fn, fp, tn) {
  const n = tp + fn + fp + tn, po = (tp + tn) / n, ph = (tp + fn) / n, pl = (tp + fp) / n, pe = ph * pl + (1 - ph) * (1 - pl);
  return { n, acc: po, base: Math.max(ph, 1 - ph), prec: tp + fp ? tp / (tp + fp) : NaN, rec: tp + fn ? tp / (tp + fn) : NaN, kappa: pe === 1 ? 0 : (po - pe) / (1 - pe) };
}
const f2 = x => (isFinite(x) ? x.toFixed(2) : "n/a");
const matrix = (tp, fn, fp, tn) => h("table", { class: "mx" },
  h("tr", {}, h("th", {}), h("th", {}, "Labeler: yes"), h("th", {}, "Labeler: no")),
  h("tr", {}, h("th", {}, "Truly abusive"), h("td", {}, String(tp)), h("td", {}, String(fn))),
  h("tr", {}, h("th", {}, "Not abusive"), h("td", {}, String(fp)), h("td", {}, String(tn))));
const mets = m => h("div", { class: "mets" },
  h("div", {}, h("small", {}, "Accuracy"), h("b", {}, pct(m.acc))), h("div", {}, h("small", {}, "Finds"), h("b", {}, pct(m.rec))),
  h("div", {}, h("small", {}, "Flags right"), h("b", {}, pct(m.prec))), h("div", {}, h("small", {}, "Kappa"), h("b", {}, f2(m.kappa))));

/* ---------- level 1: accuracy ---------- */
const LABELERS = [
  { k: "A", name: "Labeler A", tp: 0, fn: 6, fp: 0, tn: 94, note: "Says \"not abusive\" every time." },
  { k: "B", name: "Labeler B", tp: 5, fn: 1, fp: 24, tn: 70, note: "Flags a lot." },
  { k: "C", name: "Labeler C", tp: 4, fn: 2, fp: 4, tn: 90, note: "Flags fewer, and about half are right." }
];
function buildAcc(def) {
  L = { def, token: 0 };
  let pick = null; const cards = {};
  const render = () => LABELERS.forEach(l => cards[l.k].classList.toggle("on", pick === l.k));
  const left = LABELERS.map(l => {
    const m = metrics(l.tp, l.fn, l.fp, l.tn);
    cards[l.k] = h("div", { class: "lab" }, h("h4", {}, l.name + ": " + l.note), matrix(l.tp, l.fn, l.fp, l.tn), mets(m),
      h("button", { class: "btn", type: "button", onclick: () => { pick = l.k; render(); } }, "Use " + l.name));
    return cards[l.k];
  });
  const check = () => {
    if (!pick) { setFb("warn", "Pick a labeler first."); return; }
    if (pick === "C") { solved(); setFb("good", def.win, true); }
    else if (pick === "A") setFb("bad", "A has the highest accuracy (tied with C) but finds none of the 6 abusive messages: its \"Finds\" is 0%. Accuracy hides that.");
    else setFb("bad", "B finds 5 of 6, but 24 of the 29 messages it flags are not abusive. A reviewer would drown. Compare \"Flags right\" across the three.");
  };
  const right = [h("div", { class: "givens" }, "Three labelers each read the same 100 invented messages. 6 of them are truly abusive. A person will review every message the labeler flags. Which labeler would you use to find the abusive ones?"),
    h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: check }, "Check my pick"), hintBtn(def)), h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  return { left, right };
}

/* ---------- level 2: kappa ---------- */
function buildKappa(def) {
  L = { def, token: 0 };
  const P = { p: 6, s: 80, t: 80 };
  const stats = h("div", { class: "stats" }), note = h("p", { class: "tipline" });
  const slider = (id, label, min, max, key, fmt) => {
    const v = h("b", {}, fmt(P[key]));
    return h("div", { class: "ctrl" }, h("div", { class: "row2" }, h("label", { for: id }, label), v),
      h("input", { id, type: "range", min, max, step: 1, value: P[key], "aria-label": label, oninput: e => { P[key] = +e.target.value; v.textContent = fmt(P[key]); render(); } }));
  };
  const calc = () => {
    const p = P.p / 100, s = P.s / 100, t = P.t / 100, tp = p * s, fn = p * (1 - s), fp = (1 - p) * (1 - t), tn = (1 - p) * t;
    return metrics(tp, fn, fp, tn);
  };
  const render = () => {
    const m = calc();
    stats.replaceChildren(h("div", { class: "stat" }, h("small", {}, "Accuracy"), h("b", {}, pct(m.acc))),
      h("div", { class: "stat" }, h("small", {}, "Always-no baseline"), h("b", {}, pct(m.base))),
      h("div", { class: "stat" }, h("small", {}, "Kappa"), h("b", {}, f2(m.kappa))));
    note.textContent = m.acc >= .9 && m.kappa < .2 ? "High accuracy, and kappa shows almost no agreement beyond chance." : "";
  };
  const check = () => {
    const m = calc();
    if (m.acc >= .9 && m.kappa < .2) { solved(); setFb("good", def.win, true); }
    else if (m.acc < .9) setFb("bad", `Accuracy is ${pct(m.acc)}. Get it to 90% or more first.`);
    else setFb("bad", `Kappa is ${f2(m.kappa)}. You need it under 0.20 while accuracy stays at 90% or more. Try a labeler that misses most of the abusive messages.`);
  };
  const left = [h("div", { class: "givens" }, "Set how rare abuse is, and how good the labeler is at finding it (sensitivity) and at leaving alone what is fine (specificity). Make a labeler that looks great on accuracy but is no better than chance."),
    slider("pp", "Share of messages that are abusive", 1, 50, "p", v => v + "%"),
    slider("ps", "Finds abusive ones (sensitivity)", 0, 100, "s", v => v + "%"),
    slider("pt", "Leaves the rest alone (specificity)", 0, 100, "t", v => v + "%")];
  const right = [stats, note, h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: check }, "Check my labeler"), hintBtn(def)), h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  render();
  return { left, right };
}

/* ---------- level 3: why they disagree ---------- */
const CODEBOOK = "Codebook line: \"Abusive = insults or attacks a person. Criticizing an idea or a policy, even harshly, is not abusive.\"";
const CASES = [
  { q: "Your plan is idiotic.", h: 0, m: 1, a: "labeler", why: "The insult is aimed at a plan, not at a person, so the codebook says no. The labeler was wrong." },
  { q: "Typical politician. Lies every time he opens his mouth.", h: 0, m: 1, a: "codebook", why: "An attack on a person, or a general claim about a group? The codebook does not say. That is a codebook gap." },
  { q: "You are a clown.", h: 0, m: 1, a: "human", why: "A plain insult to a person. The human label of 0 looks like a mistake or a different rule." },
  { q: "People who think like you are why this country is broken.", h: 1, m: 0, a: "codebook", why: "An attack on a group of people, or on a view? The codebook does not say." },
  { q: "Thanks, that is a helpful point.", h: 1, m: 0, a: "human", why: "Nothing abusive here. The human label of 1 looks like a slip." },
  { q: "This policy is a disaster, and the minister who wrote it is a fool.", h: 1, m: 0, a: "labeler", why: "Calls a person a fool. The codebook says yes, and the labeler missed it." }
];
const CASE_OPTS = [{ v: "labeler", t: "The labeler is wrong" }, { v: "codebook", t: "The codebook does not say" }, { v: "human", t: "The human label is questionable" }];
function buildCases(def) {
  L = { def, token: 0 };
  const picks = CASES.map(() => choose(CASE_OPTS));
  const cards = CASES.map((c, i) => h("div", { class: "case", id: "c" + i }, h("p", { class: "label" }, "Disagreement " + (i + 1)), h("blockquote", {}, c.q),
    h("p", { class: "lbl" }, `Human: ${c.h ? "abusive" : "not abusive"} · Labeler: ${c.m ? "abusive" : "not abusive"}`), picks[i]));
  const check = () => {
    if (picks.some(p => !p.get())) { setFb("warn", "Decide on every disagreement."); return; }
    let n = 0;
    CASES.forEach((c, i) => {
      const ok = picks[i].get() === c.a; if (ok) n++;
      cards[i].className = "case " + (ok ? "right" : "wrong"); cards[i].querySelector(".why")?.remove();
      cards[i].append(h("p", { class: "why" }, (ok ? "Right. " : "Not quite. ") + c.why));
    });
    if (n >= 5) { solved(); setFb("good", def.win + ` You matched ${n} of 6.`, true); } else setFb("bad", `${n} of 6. Read the notes under each case: the codebook line is the test.`);
  };
  const left = [h("div", { class: "givens" }, CODEBOOK), ...cards];
  const right = [h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: check }, "Check my answers"), hintBtn(def)), h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  return { left, right };
}

/* ---------- level 4: claims ---------- */
const CLAIMS = [
  { q: "The labeler is 80% accurate, so we can trust its abuse labels.", a: "no", why: "Always saying \"no\" gets 90% here. Accuracy below the baseline is not evidence of a good labeler." },
  { q: "On abuse, the labeler's accuracy is below the accuracy of always saying \"no\".", a: "yes", why: "80% is less than 90%. That is just reading the table." },
  { q: "Most messages the labeler flags as abusive really are abusive.", a: "no", why: "\"Flags right\" is 30%. Seven in ten flags are false alarms." },
  { q: "The labeler finds most of the truly abusive messages.", a: "yes", why: "\"Finds\" is 75%. It catches three in four, at the cost of many false alarms." },
  { q: "The labeler agrees with people far beyond chance.", a: "no", why: "Kappa is 0.33, which is modest. \"Far beyond chance\" is too strong." },
  { q: "These 200 messages show the labeler works on every platform.", a: "no", why: "200 messages from one source cannot support a claim about every platform." }
];
const CLAIM_OPTS = [{ v: "yes", t: "Supported" }, { v: "no", t: "Not supported" }];
function buildClaims(def) {
  L = { def, token: 0 };
  const picks = CLAIMS.map(() => choose(CLAIM_OPTS));
  const cards = CLAIMS.map((c, i) => h("div", { class: "case", id: "k" + i }, h("blockquote", {}, c.q), picks[i]));
  const check = () => {
    if (picks.some(p => !p.get())) { setFb("warn", "Decide on every claim."); return; }
    let all = true;
    CLAIMS.forEach((c, i) => { const ok = picks[i].get() === c.a; all = all && ok; cards[i].className = "case " + (ok ? "right" : "wrong"); cards[i].querySelector(".why")?.remove(); cards[i].append(h("p", { class: "why" }, (ok ? "Right. " : "Not quite. ") + c.why)); });
    if (all) { solved(); setFb("good", def.win, true); } else setFb("bad", "Check the numbers in the table against each claim. Which number would you point to?");
  };
  const m = metrics(15, 5, 35, 145);
  const left = [h("div", { class: "givens" }, "Invented result: a labeler was run on 200 messages from one forum, and 20 of them (10%) were abusive by the people's labels. The table is below."),
    h("div", { class: "lab" }, h("h4", {}, "Abuse: labeler versus people (200 messages)"), matrix(15, 5, 35, 145),
      h("div", { class: "mets" }, h("div", {}, h("small", {}, "Accuracy"), h("b", {}, pct(m.acc))), h("div", {}, h("small", {}, "Always-no"), h("b", {}, pct(m.base))), h("div", {}, h("small", {}, "Finds"), h("b", {}, pct(m.rec))), h("div", {}, h("small", {}, "Flags right"), h("b", {}, pct(m.prec)))),
      h("p", { class: "tipline" }, "Kappa: " + f2(m.kappa)))];
  const right = [...cards, h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: check }, "Check my answers"), hintBtn(def)), h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  return { left, right };
}

const LEVELS = [
  { w: 0, kind: "acc", title: "Which labeler would you use?",
    task: "Three labelers, one sample of 100 invented messages, 6 truly abusive. Compare their tables and pick the one you would use to find abuse.",
    hint: "Look at \"Finds\" and \"Flags right\" as well as accuracy. What does each labeler miss, and what does it flag by mistake?",
    win: "Labeler C. It has the same accuracy as A, but it finds 4 of the 6 abusive messages and half of what it flags is right. Accuracy alone could not tell A from C." },
  { w: 1, kind: "kappa", title: "High accuracy, no agreement",
    task: "Set the sliders so the labeler has at least 90% accuracy but a kappa under 0.20.",
    hint: "When abuse is rare, a labeler that misses most of it still scores high on accuracy. Lower the sensitivity.",
    win: "You made a labeler that looks great on accuracy and agrees with people no better than chance. That is why you report kappa (or precision and recall) as well." },
  { w: 2, kind: "cases", title: "Why do they disagree?",
    task: "Six invented disagreements between a person and a labeler. For each, decide: the labeler is wrong, the codebook does not say, or the human label is questionable.",
    hint: "Apply the codebook line literally. If it does not settle the case, the codebook is the problem.",
    win: "Disagreement has more than one cause. Only reading the cases tells you whether to change the prompt, the codebook, or the human labels." },
  { w: 3, kind: "claims", title: "What does the result support?",
    task: "Read the table and decide which claims it supports. Use the numbers, not the first impression.",
    hint: "Compare accuracy with the always-no baseline, and use precision, recall, kappa, and the size and source of the sample.",
    win: "You matched each claim to the evidence. A short, honest sentence beats a flattering number." },
  { w: 4, kind: "bridge", bridge: true, title: "Compute the measures on 20 labels",
    task: "Open the Week 6 notebook, find the warm-up cell, and run this there." }
];

/* ---------- bridge ---------- */
const BRIDGE_CODE = [
  "from sklearn.metrics import accuracy_score, cohen_kappa_score, confusion_matrix", "",
  "human = [0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0]",
  "llm   = [0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0]", "",
  "# Predict first: will accuracy be above or below the always-no baseline?",
  'print("accuracy:", accuracy_score(human, llm))',
  'print("always-no baseline:", 1 - sum(human) / len(human))',
  'print("kappa:", cohen_kappa_score(human, llm))',
  "print(confusion_matrix(human, llm))"
].join("\n");
function buildBridge(def) {
  const prompt = "I have two lists of 0/1 labels, one from people and one from an AI. Write Python that prints the confusion matrix, accuracy, precision, recall and Cohen's kappa, and the accuracy of always predicting 0. Then explain what kappa means in one sentence. Use scikit-learn. Do not include any real data or keys.";
  const left = [codeCard("Task 1: the measures", BRIDGE_CODE, "Predict first. Paste it into the warm-up cell of the Week 6 notebook.")];
  const right = [
    codeCard("Task 2: ask an AI, then compare", prompt, "Paste this into your AI assistant. Does its code match what you ran? Did it include the always-0 baseline?"),
    h("div", { class: "tray" }, h("p", { class: "label" }, "Task 3: check"), h("p", {}, "Was accuracy above the baseline? Which of the four counts (the confusion matrix) is largest, and which drives kappa down? Log one sentence on what you would say about this labeler.")),
    h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: () => { solved(); setFb("good", "Done. In the notebook you will run these on 150 real messages, with labels from an AI and from people."); } }, "I ran all three")),
    h("div", { id: "fb", class: "fb", "aria-live": "polite" })
  ];
  return { left, right };
}

BUILDERS.acc = buildAcc; BUILDERS.kappa = buildKappa; BUILDERS.cases = buildCases; BUILDERS.claims = buildClaims; BUILDERS.bridge = buildBridge;
boot("cactus-trust-the-labeler-done");
