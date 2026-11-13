/* Week 7: Plant It, Find It. Uses the shared engine (practice/shared/engine.js). All posts, comments and numbers are invented. */

const WORLDS = [
  { name: "Plant an answer", blurb: "Simulate, then check",
    idea: "If you plant an effect in simulated data, you know the right answer, so you can see whether a method finds it. Run the study many times and you can see how often it does.",
    where: "In the notebook: the warm-up plants an effect and runs 200 studies." },
  { name: "Rows in groups", blurb: "Posts, threads, accounts",
    idea: "Comments under one post share that post. Ignoring this makes some results look far more certain than they are, mostly for variables that belong to the post, not the comment.",
    where: "In the notebook: Exercise 1 compares naive and clustered standard errors." },
  { name: "Counts and exposure", blurb: "Per follower",
    idea: "A post with more followers gets more comments. To see whether something changes how people respond, compare comments per follower, not comments.",
    where: "In the notebook: Exercise 2 models counts with an offset." },
  { name: "What breaks it", blurb: "Assumptions",
    idea: "Every method assumes something about the rows. Bots, repeats, groups and tiny samples each break a different assumption.",
    where: "In the notebook: Exercise 3 is a bug hunt where the code looks fine and the answer is wrong. Session 2 applies this to your track." },
  { name: "Take it to Colab", blurb: "Real code",
    idea: "You have planted answers on a page. Now plant one in code and compare two kinds of interval.",
    where: "Paste the code into a new cell in the Week 7 notebook." }
];

const choose = (opts, onpick) => {
  const wrap = h("div", { class: "choice", role: "group" }); let cur = null; const btns = [];
  opts.forEach(o => {
    const b = h("button", { class: "pill", type: "button", onclick: () => { cur = o.v; btns.forEach(x => x.classList.toggle("on", x === b)); onpick && onpick(cur); } }, o.t);
    btns.push(b); wrap.append(b);
  });
  wrap.get = () => cur; return wrap;
};

/* ---------- simulation (all in the browser, nothing sent) ---------- */
const randn = () => { let u = 0, v = 0; while (!u) u = Math.random(); while (!v) v = Math.random(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); };
const mean = a => a.reduce((s, x) => s + x, 0) / a.length;
const variance = a => { const m = mean(a); return a.reduce((s, x) => s + (x - m) * (x - m), 0) / (a.length - 1); };
const tcrit = df => 1.96 + 2.4 / Math.max(df, 1);
const POST_SD = 1.5, COMMENT_SD = 2.0;
function simStudy(nPosts, m, effect) {
  const half = Math.floor(nPosts / 2), means = [[], []];
  let s = [0, 0], ss = [0, 0], n = [0, 0];
  for (let i = 0; i < half * 2; i++) {
    const g = i % 2, u = randn() * POST_SD; let tot = 0;
    for (let k = 0; k < m; k++) { const y = effect * g + u + randn() * COMMENT_SD; tot += y; s[g] += y; ss[g] += y * y; n[g]++; }
    means[g].push(tot / m);
  }
  const est = mean(means[1]) - mean(means[0]);
  const seC = Math.sqrt(variance(means[1]) / means[1].length + variance(means[0]) / means[0].length);
  const v = g => (ss[g] - s[g] * s[g] / n[g]) / (n[g] - 1);
  const pooled = (v(0) + v(1)) / 2, seN = Math.sqrt(pooled * (1 / n[0] + 1 / n[1]));
  const df = half * 2 - 2, tc = tcrit(df);
  return { est, loC: est - tc * seC, hiC: est + tc * seC, loN: est - 1.96 * seN, hiN: est + 1.96 * seN };
}

/* ---------- level 1: plant it ---------- */
function buildPlant(def) {
  L = { def, token: 0 };
  const P = { effect: 5, posts: 40, per: 20 }; // effect in tenths
  let last = null;
  const stats = h("div", { class: "stats" }), plot = h("div", {}), note = h("p", { class: "tipline" });
  const slider = (id, label, min, max, key, fmt) => {
    const v = h("b", {}, fmt(P[key]));
    return h("div", { class: "ctrl" }, h("div", { class: "row2" }, h("label", { for: id }, label), v),
      h("input", { id, type: "range", min, max, step: 1, value: P[key], "aria-label": label, oninput: e => { P[key] = +e.target.value; v.textContent = fmt(P[key]); } }));
  };
  const draw = (res, truth) => {
    const W = 600, H = 150, lo = -1.5, hi = Math.max(3, truth + 2), x = v => 10 + (v - lo) / (hi - lo) * (W - 20);
    const shown = res.slice(0, 30), dy = (H - 20) / shown.length;
    let g = `<line class="truth" x1="${x(truth)}" x2="${x(truth)}" y1="2" y2="${H - 14}" stroke-width="1.5"/><line x1="${x(0)}" x2="${x(0)}" y1="2" y2="${H - 14}" stroke="currentColor" stroke-opacity=".25"/>`;
    shown.forEach((r, i) => { const y = 6 + i * dy, ok = r.loC <= truth && truth <= r.hiC; g += `<line class="${ok ? "hit" : "miss"}" x1="${x(Math.max(lo, r.loC))}" x2="${x(Math.min(hi, r.hiC))}" y1="${y}" y2="${y}" stroke-width="2"/>`; });
    g += `<text x="${x(truth) + 4}" y="${H - 3}">planted ${truth.toFixed(1)}</text><text x="${x(0) + 4}" y="${H - 3}">0</text>`;
    plot.innerHTML = `<svg class="ivl" viewBox="0 0 ${W} ${H}" role="img" aria-label="30 of the 100 clustered intervals, with the planted effect marked">${g}</svg>`;
  };
  const run = () => {
    const truth = P.effect / 10, res = [];
    for (let i = 0; i < 100; i++) res.push(simStudy(P.posts, P.per, truth));
    const found = res.filter(r => r.loC > 0).length, nOk = res.filter(r => r.loN <= truth && truth <= r.hiN).length, cOk = res.filter(r => r.loC <= truth && truth <= r.hiC).length;
    last = { truth, posts: P.posts, found };
    stats.replaceChildren(
      h("div", { class: "stat" }, h("small", {}, "Effect found (clustered interval above 0)"), h("b", {}, found + " of 100")),
      h("div", { class: "stat" }, h("small", {}, "Naive intervals that held the truth"), h("b", {}, nOk + " of 100")),
      h("div", { class: "stat" }, h("small", {}, "Clustered intervals that held the truth"), h("b", {}, cOk + " of 100")));
    note.textContent = "Each line below is one study's clustered interval (first 30 of 100). Red lines missed the planted effect.";
    draw(res, truth);
  };
  const check = () => {
    if (!last) { setFb("warn", "Run the 100 studies first."); return; }
    if (last.truth >= 1 && last.found >= 80) { solved(); setFb("good", def.win, true); }
    else if (last.truth < 1) setFb("bad", "Plant an effect of 1.0 or more first, then look for a number of posts that finds it in at least 80 of 100.");
    else setFb("bad", `${last.found} of 100. Not enough yet. What did more comments per post do, and what did more posts do?`);
  };
  const left = [h("div", { class: "givens" }, "Each simulated post has a label (half do, half do not), and every comment under it gets that post's own bump, up or down. You plant the label's effect on comment warmth. Then 100 studies are run, and each study asks: did the clustered 95% interval find an effect above zero?"),
    slider("pe", "Planted effect of the label", 0, 20, "effect", v => (v / 10).toFixed(1)),
    slider("pn", "Number of posts", 10, 120, "posts", v => String(v)),
    slider("pc", "Comments per post", 5, 50, "per", v => String(v))];
  const right = [stats, plot, note, h("div", { class: "row" }, h("button", { class: "btn", type: "button", onclick: run }, "Run 100 studies"), h("button", { class: "btn primary", type: "button", onclick: check }, "Check my setting"), hintBtn(def)), h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  return { left, right };
}

/* ---------- level 2: which variables ---------- */
const VARS = [
  { q: "The post carries an \"AI-generated\" label", a: "big", why: "Every comment under the post has the same value, so there are only as many independent chances as posts." },
  { q: "The comment is long", a: "small", why: "It varies from comment to comment within each post, so the comments do carry separate information." },
  { q: "The post author's number of followers", a: "big", why: "A property of the post, shared by all its comments." },
  { q: "The comment contains a link", a: "small", why: "It varies within a post, comment by comment." },
  { q: "The post went up at night", a: "big", why: "Another property of the post." },
  { q: "The comment replies to another commenter", a: "small", why: "It varies within the thread." }
];
const VAR_OPTS = [{ v: "big", t: "Standard error gets much bigger" }, { v: "small", t: "Barely changes" }];
function buildVars(def) {
  L = { def, token: 0 };
  const picks = VARS.map(() => choose(VAR_OPTS));
  const cards = VARS.map((c, i) => h("div", { class: "case", id: "v" + i }, h("blockquote", {}, c.q), picks[i]));
  const check = () => {
    if (picks.some(p => !p.get())) { setFb("warn", "Decide on every variable."); return; }
    let n = 0;
    VARS.forEach((c, i) => { const ok = picks[i].get() === c.a; if (ok) n++; cards[i].className = "case " + (ok ? "right" : "wrong"); cards[i].querySelector(".why")?.remove(); cards[i].append(h("p", { class: "why" }, (ok ? "Right. " : "Not quite. ") + c.why)); });
    if (n === 6) { solved(); setFb("good", def.win, true); } else setFb("bad", `${n} of 6. Ask of each variable: is it the same for every comment under a post, or does it change from comment to comment?`);
  };
  const left = [h("div", { class: "givens" }, "You have 3,000 invented comments under 80 posts, and you fit a regression of comment warmth on one variable at a time. First ignoring the posts (every comment as independent), then accounting for them (clustering by post). For each variable, what happens to its standard error when you account for the posts?")];
  const right = [...cards, h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: check }, "Check my answers"), hintBtn(def)), h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  return { left, right };
}

/* ---------- level 3: counts and exposure ---------- */
const POSTS = [
  { id: "p1", lab: 0, f: 1000, c: 5 }, { id: "p2", lab: 0, f: 2000, c: 11 }, { id: "p3", lab: 0, f: 1500, c: 8 }, { id: "p4", lab: 0, f: 3500, c: 17 },
  { id: "p5", lab: 1, f: 8000, c: 26 }, { id: "p6", lab: 1, f: 10000, c: 30 }, { id: "p7", lab: 1, f: 6000, c: 21 }, { id: "p8", lab: 1, f: 12000, c: 38 }
];
const COUNT_OPTS = [
  { v: "more", t: "The label makes people comment more" },
  { v: "rate", t: "Labeled posts get more comments, but fewer per follower" },
  { v: "none", t: "No difference" }
];
function buildCounts(def) {
  L = { def, token: 0 };
  let mode = "raw";
  const tbl = h("div", {}), sum = h("div", { class: "stats" });
  const draw = () => {
    const rows = POSTS.map(p => h("tr", { class: p.lab ? "lab1" : "" }, h("td", {}, p.id), h("td", {}, p.lab ? "labeled" : "not labeled"), h("td", { class: "n" }, p.f.toLocaleString()),
      h("td", { class: "n" }, mode === "raw" ? String(p.c) : (p.c / p.f * 1000).toFixed(1))));
    tbl.replaceChildren(h("table", { class: "cnt" }, h("tr", {}, h("th", {}, "Post"), h("th", {}, "Label"), h("th", {}, "Followers"), h("th", {}, mode === "raw" ? "Comments" : "Comments per 1,000 followers")), rows));
    const g = k => { const r = POSTS.filter(p => p.lab === k); return { f: mean(r.map(p => p.f)), raw: mean(r.map(p => p.c)), rate: r.reduce((s, p) => s + p.c, 0) / r.reduce((s, p) => s + p.f, 0) * 1000 }; };
    const a = g(0), b = g(1);
    sum.replaceChildren(h("div", { class: "stat" }, h("small", {}, "Not labeled, average"), h("b", {}, mode === "raw" ? a.raw.toFixed(1) : a.rate.toFixed(1))),
      h("div", { class: "stat" }, h("small", {}, "Labeled, average"), h("b", {}, mode === "raw" ? b.raw.toFixed(1) : b.rate.toFixed(1))));
  };
  const toggle = h("div", { class: "choice", role: "group" });
  const bRaw = h("button", { class: "pill on", type: "button", onclick: () => { mode = "raw"; bRaw.classList.add("on"); bRate.classList.remove("on"); draw(); } }, "Raw comments");
  const bRate = h("button", { class: "pill", type: "button", onclick: () => { mode = "rate"; bRate.classList.add("on"); bRaw.classList.remove("on"); draw(); } }, "Per 1,000 followers");
  toggle.append(bRaw, bRate);
  const pick = choose(COUNT_OPTS);
  const check = () => {
    const v = pick.get();
    if (!v) { setFb("warn", "Pick a statement first."); return; }
    if (v === "rate") { solved(); setFb("good", def.win, true); }
    else if (v === "more") setFb("bad", "Labeled posts do have more comments in the raw table. But they also come from accounts with several times the followers. Switch to \"Per 1,000 followers\" and compare again.");
    else setFb("bad", "There is a difference in both views. Switch between them and see whether it points the same way.");
  };
  draw();
  const left = [h("div", { class: "givens" }, "Eight invented posts. The platform labels posts mostly from bigger accounts. What does the label do to comments? Switch between the raw counts and the rate per follower."), toggle, tbl, sum];
  const right = [pick, h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: check }, "Check my answer"), hintBtn(def)), h("div", { id: "fb", class: "fb", "aria-live": "polite" }),
    h("p", { class: "tipline" }, "In the notebook you tell a model about the denominator with an offset: it models comments per follower, not comments.")];
  return { left, right };
}

/* ---------- level 4: what breaks it ---------- */
const BREAK_OPTS = [
  { v: "indep", t: "Rows are not independent" }, { v: "people", t: "Some accounts are not people" },
  { v: "twice", t: "The same thing is counted many times" }, { v: "few", t: "Too few units" }, { v: "meant", t: "It does not measure what you meant" }
];
const BREAKS = [
  { q: "In a reply network, the most \"central\" account replied to 4,000 different people in one afternoon.", a: "people", why: "Probably automated. Its centrality is real, but it is not a person's influence." },
  { q: "A meme template appears to have 300 posts, but 220 are one image reposted by a handful of accounts.", a: "twice", why: "The same image is counted over and over. Count distinct images, or distinct accounts, as well." },
  { q: "A survey of 2,000 people was run in 12 classrooms and analysed as 2,000 independent people.", a: "indep", why: "People in a classroom share a teacher and a context, so there are nearer 12 independent chances on the classroom-level variables." },
  { q: "An experiment has six people in each condition.", a: "few", why: "The result is too noisy to say much, however clean the method. A known-answer check shows how often it would find a real effect." },
  { q: "Someone reads a high degree (many connections) as \"influence\" without looking at who the connections are.", a: "meant", why: "Degree counts connections. Influence needs more (who they are, whether they respond)." },
  { q: "A permutation test shuffles the label across 3,000 comments that sit in 30 posts.", a: "indep", why: "The label belongs to the post, so shuffling comments breaks the structure. Shuffle the post labels." }
];
function buildBreaks(def) {
  L = { def, token: 0 };
  const picks = BREAKS.map(() => choose(BREAK_OPTS));
  const cards = BREAKS.map((c, i) => h("div", { class: "case", id: "b" + i }, h("blockquote", {}, c.q), picks[i]));
  const check = () => {
    if (picks.some(p => !p.get())) { setFb("warn", "Decide on every case."); return; }
    let n = 0;
    BREAKS.forEach((c, i) => { const ok = picks[i].get() === c.a; if (ok) n++; cards[i].className = "case " + (ok ? "right" : "wrong"); cards[i].querySelector(".why")?.remove(); cards[i].append(h("p", { class: "why" }, (ok ? "Right. " : "Not quite. ") + c.why)); });
    if (n >= 5) { solved(); setFb("good", def.win + ` You matched ${n} of 6.`, true); } else setFb("bad", `${n} of 6. For each case, ask what the method assumes about its rows.`);
  };
  const left = [h("div", { class: "givens" }, "Six invented problems from analyses like the ones in Session 2. For each, say which assumption is broken.")];
  const right = [...cards, h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: check }, "Check my answers"), hintBtn(def)), h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  return { left, right };
}

const LEVELS = [
  { w: 0, kind: "plant", title: "Plant it, then find it",
    task: "Plant an effect of 1.0. Then find a number of posts and comments per post that finds it in at least 80 of 100 studies.",
    hint: "Try 100 posts and see. Then change comments per post from 20 to 50 and compare. Which one moves the number more?",
    win: "More comments per post barely moved it. More posts moved it a lot. When rows come in groups, the number of groups (posts) is what limits you, not the number of rows." },
  { w: 1, kind: "vars", title: "Which variables are hurt?",
    task: "For each variable, say what happens to its standard error when you stop treating comments as independent.",
    hint: "Is the variable the same for every comment under a post, or does it change from comment to comment?",
    win: "Variables that belong to the post (its label, its author, its time) are the ones that look far too certain when you ignore posts. Variables that vary within a post are fine." },
  { w: 2, kind: "counts", title: "Counts need a denominator",
    task: "Compare labeled and unlabeled posts, first by raw comments, then per 1,000 followers. Pick the statement that fits.",
    hint: "Switch the table to \"Per 1,000 followers\". Does the label's group stay ahead?",
    win: "Labeled posts have more comments but fewer per follower. A raw count would give you the wrong sign. Always ask what the count is a count of, and out of what." },
  { w: 3, kind: "breaks", title: "What breaks which method?",
    task: "Six invented problems. For each, say which assumption is broken.",
    hint: "Ask: what does this method assume about its rows (independent, people, counted once, enough, measuring the right thing)?",
    win: "Every method has a quiet assumption. Naming it is half the check." },
  { w: 4, kind: "bridge", bridge: true, title: "Plant an answer in code",
    task: "Open the Week 7 notebook, add a new cell, and run this there." }
];

/* ---------- bridge ---------- */
const BRIDGE_CODE = [
  "import numpy as np, pandas as pd", "import statsmodels.formula.api as smf", "",
  "rng = np.random.default_rng(1)",
  "n_posts, per_post, effect = 40, 20, 0.5          # change these",
  "post = np.repeat(np.arange(n_posts), per_post)",
  "labeled = np.repeat(rng.permutation([0, 1] * (n_posts // 2)), per_post)",
  "post_bump = np.repeat(rng.normal(0, 1.5, n_posts), per_post)",
  "y = 5 + effect * labeled + post_bump + rng.normal(0, 2, n_posts * per_post)",
  "d = pd.DataFrame({\"post\": post, \"labeled\": labeled, \"y\": y})", "",
  "# Predict first: will the naive interval be wider or narrower than the clustered one?",
  "naive = smf.ols(\"y ~ labeled\", d).fit()",
  "clus = smf.ols(\"y ~ labeled\", d).fit(cov_type=\"cluster\", cov_kwds={\"groups\": d[\"post\"]})",
  "print(\"naive:    \", naive.conf_int().loc[\"labeled\"].round(2).values)",
  "print(\"clustered:\", clus.conf_int().loc[\"labeled\"].round(2).values)"
].join("\n");
function buildBridge(def) {
  const prompt = "I have a pandas DataFrame d with columns post (which post a comment is under), labeled (0 or 1, a property of the post) and y (a number). Write Python using statsmodels that fits y ~ labeled twice: once with ordinary standard errors, and once with standard errors clustered by post. Print the two 95% intervals. Then explain in one sentence why they differ. Do not include any real data or keys.";
  const left = [codeCard("Task 1: plant an answer", BRIDGE_CODE, "Predict first. Paste it into a new cell in the Week 7 notebook.")];
  const right = [
    codeCard("Task 2: ask an AI, then compare", prompt, "Paste this into your AI assistant. Did it cluster by the right column? Is its explanation correct?"),
    h("div", { class: "tray" }, h("p", { class: "label" }, "Task 3: check"), h("p", {}, "Which interval is wider? Does each contain the planted 0.5? Change per_post to 100 and run it again. What changes, and what does not?")),
    h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: () => { solved(); setFb("good", "Done. In the notebook you will do this on comments under 80 posts, and fix standard errors, counts and a bug hunt."); } }, "I ran all three")),
    h("div", { id: "fb", class: "fb", "aria-live": "polite" })
  ];
  return { left, right };
}

BUILDERS.plant = buildPlant; BUILDERS.vars = buildVars; BUILDERS.counts = buildCounts; BUILDERS.breaks = buildBreaks; BUILDERS.bridge = buildBridge;
boot("cactus-plant-it-find-it-done");
