/* Week 4: Before You Collect. Uses the shared engine (practice/shared/engine.js). */

const WORLDS = [
  { name: "What to keep", blurb: "Fields",
    idea: "Collect and keep only what your question needs. Every extra field is a risk to the people in the data, and a cost to you if you have to protect it.",
    where: "In the notebook: Exercise 3 removes identifying fields, and the data card says what you left out and why." },
  { name: "Who can be found", blurb: "Re-identification",
    idea: "Removing the username does not make people anonymous. A distinctive post, an exact time and a small place can still point to one person.",
    where: "In the notebook: Exercise 3 checks the text, the timestamp and the columns, not just the username." },
  { name: "Plan the pull", blurb: "Limits",
    idea: "A request limit is a plan, not a surprise. Choose a page size and a pause so you stay inside it, and save the raw response before you do anything else.",
    where: "In the notebook: the warm-up stub saves raw first, logs the query, and pauses between requests." },
  { name: "Ask first", blurb: "Terms and ethics",
    idea: "Public does not mean free to use. Terms, consent and your ethics process decide what you may collect. When you are unsure, ask before you collect.",
    where: "In your data card: which terms and which ethics process apply, and what you did about them." },
  { name: "Take it to Colab", blurb: "Real code",
    idea: "You have planned the pull. Now run a stub that saves the raw response first.",
    where: "The Week 4 notebook has a warm-up cell like this one." }
];

S.plan = { pageSize: 50, pause: 2 };

const choose = (opts, onpick) => {
  const wrap = h("div", { class: "choice", role: "group" }); let cur = null; const btns = [];
  opts.forEach(o => {
    const b = h("button", { class: "pill", type: "button", onclick: () => { cur = o.v; btns.forEach(x => x.classList.toggle("on", x === b)); onpick && onpick(cur); } }, o.t);
    btns.push(b); wrap.append(b);
  });
  wrap.get = () => cur; return wrap;
};

/* ---------- level data ---------- */
const FIELDS = [
  { k: "Username (@handle)", a: "change", why: "You need to count authors, so keep a stand-in: replace it with an ID like author_0001. The username itself identifies someone." },
  { k: "Display name", a: "drop", why: "Not needed to answer the question, and it often contains a real name." },
  { k: "Profile link", a: "drop", why: "A link straight to a person's profile. Never keep it in a shared table." },
  { k: "Comment text", a: "change", why: "You need the words, but @handles and links inside the text can identify people. Remove them first." },
  { k: "Exact time posted", a: "change", why: "The date is enough for this question. Exact times make a person easier to find." },
  { k: "Like count", a: "keep", why: "Useful, and it identifies no one." },
  { k: "Language of the comment", a: "keep", why: "Useful for the question, and it identifies no one." },
  { k: "Profile bio text", a: "drop", why: "Free text about a person. Not needed, and high risk." },
  { k: "City tag on the post", a: "drop", why: "Not needed for a question about Singapore as a whole, and it narrows down who the person is." },
  { k: "Image attached", a: "drop", why: "Images can show faces and places. Not needed for a question about text." },
  { k: "Device used (phone model)", a: "drop", why: "Not needed, and it adds one more detail that narrows down a person." },
  { k: "ID of the comment it replies to", a: "keep", why: "Useful for seeing conversations, and it identifies no one on its own." }
];
const SORT_OPTS = [{ v: "keep", t: "Keep" }, { v: "change", t: "Change first" }, { v: "drop", t: "Drop" }];

const RISKS = [
  { k: "Username", pts: 4, why: "It names the person." },
  { k: "Display name", pts: 3, why: "Often a real name." },
  { k: "Profile link", pts: 4, why: "A direct link to the person." },
  { k: "Profile bio text", pts: 3, why: "Free text about the person." },
  { k: "City tag", pts: 2, why: "A small place narrows the crowd." },
  { k: "Exact time of posting", pts: 2, why: "A precise moment can be matched to a public post." },
  { k: "Image attached", pts: 2, why: "Faces and places." }
];

const SCENARIOS = [
  { q: "Public comments under a news outlet's video, collected through the platform's official API. You will report counts and themes, and quote no one.", a: "ok", why: "Public, official route, and you report aggregates. Still check the platform's terms and your ethics process." },
  { q: "Posts from a private group you joined as a member, because you are curious how the members talk about AI.", a: "no", why: "Members posted in a private space and did not agree to be studied. Do not collect it. You would need permission from the group and your ethics process." },
  { q: "Public posts from a support forum about a medical condition. You want to quote some of them in your paper.", a: "check", why: "Sensitive subject, and an exact quote can be searched and traced back to the person. Check with your ethics office before you collect or quote." },
  { q: "A website whose terms say automated collection is not allowed. Your script could collect it easily.", a: "no", why: "Being technically able to is not permission. Do not collect it. Ask the site for permission, or find another source." }
];
const ASK_OPTS = [{ v: "ok", t: "Usually fine, still check terms and ethics" }, { v: "check", t: "Check first" }, { v: "no", t: "Do not collect" }];

const LEVELS = [
  { w: 0, kind: "sort", title: "Keep, change, or drop",
    task: "Your question: \"How do people in Singapore talk about AI tools in school?\" You will share the table with classmates. For each field in a typical post export, decide whether to keep it, change it first, or drop it.",
    hint: "Ask for each field: does the question need it? If yes, does it identify someone, and can I change it so it does not?",
    win: "You kept what the question needs, changed what identifies people, and dropped the rest. That is the idea of collecting only what you need." },
  { w: 1, kind: "meter", title: "Who could be found?",
    task: "Switch fields on and off in your shared table and watch the risk. You must keep the comment text, the date, and the like count. Get the risk to Low.",
    hint: "Each identifying field adds risk, and some combine to add more. Remove the ones the question does not need.",
    win: "Removing the username was not enough. You had to remove the whole set of details that could point to one person, and even then the text is searchable." },
  { w: 2, kind: "plan", title: "Plan the pull",
    task: "You need about 2,000 comments. The platform returns up to 100 items per request, allows 50 requests per day, and asks for at least 2 seconds between requests. (These limits are invented; check your platform's real ones.) Choose a page size and a pause that fit, then say what you do with each response first.",
    hint: "Requests needed = comments divided by page size. Keep it within the daily limit, and keep the pause at or above the minimum.",
    win: "A limit is a plan: the right page size and pause fit the quota, and you save the raw response before you parse anything." },
  { w: 3, kind: "ask", title: "Should you collect it?",
    task: "Four short scenarios. For each, choose: usually fine (still check terms and ethics), check first, or do not collect.",
    hint: "Ask: is it public? Did people agree to this use? Do the terms allow it? Is the topic sensitive? Can quotes be traced?",
    win: "You judged each case on public versus private, consent, terms, and sensitivity. When unsure, asking first is always the right move." },
  { w: 4, kind: "bridge", bridge: true, title: "Run a collection stub",
    task: "Open the Week 4 notebook, find the warm-up cell, and run the stub there with your own settings." }
];

/* level 1 */
function buildSort(def) {
  const st = L = { def, token: 0 };
  const picks = FIELDS.map(f => choose(SORT_OPTS));
  const rows = FIELDS.map((f, i) => h("div", { class: "frow", id: "f" + i }, h("code", {}, f.k), picks[i]));
  const check = () => {
    if (picks.some(p => !p.get())) { setFb("warn", "Choose Keep, Change first, or Drop for every field."); return; }
    let all = true; const wrong = [];
    FIELDS.forEach((f, i) => {
      const ok = picks[i].get() === f.a; all = all && ok;
      const el = rows[i]; el.className = "frow " + (ok ? "right" : "wrong");
      el.querySelector(".why")?.remove();
      el.append(h("p", { class: "why" }, (ok ? "Right. " : "Not quite. ") + f.why));
      if (!ok) wrong.push(f.k);
    });
    if (all) { solved(); setFb("good", def.win, true); } else setFb("bad", `${wrong.length} field${wrong.length === 1 ? "" : "s"} to rethink. Read the notes under each one.`);
  };
  const left = [h("div", { class: "givens" }, "Typical post export: " + FIELDS.map(f => f.k.toLowerCase()).join(", ") + "."), ...rows];
  const right = [h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: check }, "Check my choices"), hintBtn(def)), h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  return { left, right };
}

/* level 2 */
function buildMeter(def) {
  const st = L = { def, token: 0 }, on = RISKS.map(() => true);
  const bar = h("div", { class: "meter" }, h("i")), label = h("p", { class: "label" }), why = h("p", { class: "tipline" });
  const calc = () => {
    let pts = 1; const bits = ["The comment text itself can be searched (+1)"];
    RISKS.forEach((r, i) => { if (on[i]) { pts += r.pts; bits.push(`${r.k} (+${r.pts}): ${r.why}`); } });
    const timeOn = on[5], cityOn = on[4];
    if (timeOn && cityOn) { pts += 2; bits.push("Exact time plus a city: a distinctive post can narrow to one person (+2)"); }
    return { pts, bits };
  };
  const render = () => {
    const { pts, bits } = calc(), level = pts <= 2 ? "Low" : pts <= 6 ? "Medium" : "High";
    bar.className = "meter " + (level === "Low" ? "" : level === "Medium" ? "med" : "high");
    bar.firstChild.style.width = Math.min(100, (pts / 20) * 100) + "%";
    label.textContent = `Risk: ${level} (${pts} points)`;
    why.textContent = bits.join(" · ");
    if (level === "Low") { solved(); setFb("good", def.win, true); } else setFb("info", `Risk is ${level.toLowerCase()}. Remove fields the question does not need.`);
  };
  const togs = RISKS.map((r, i) => h("label", { class: "tog" }, h("input", { type: "checkbox", checked: true, onchange: e => { on[i] = e.target.checked; render(); } }), h("span", {}, r.k, h("small", {}, r.why))));
  const fixed = h("div", { class: "givens" }, "Always kept (the question needs them): comment text, date, like count.");
  const left = [fixed, h("p", { class: "label" }, "Include in the shared table"), h("div", { class: "togs" }, togs)];
  const right = [label, bar, why, h("div", { class: "row" }, hintBtn(def)), h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  render();
  return { left, right };
}

/* level 3 */
function buildPlan(def) {
  const st = L = { def, token: 0 }, P = S.plan, NEED = 2000, DAILY = 50, MINPAUSE = 2, MAXPAGE = 100;
  const stats = h("div", { class: "stats" });
  const first = choose([{ v: "raw", t: "Save the raw response" }, { v: "parse", t: "Parse it into a table" }, { v: "anon", t: "Delete the usernames" }]);
  const slider = (id, label, min, max, step, val, key, fmt) => {
    const v = h("b", {}, fmt(val));
    return h("div", { class: "ctrl" }, h("div", { class: "row2" }, h("label", { for: id }, label), v),
      h("input", { id, type: "range", min, max, step, value: val, "aria-label": label, oninput: e => { P[key] = +e.target.value; v.textContent = fmt(P[key]); render(); } }));
  };
  const render = () => {
    const req = Math.ceil(NEED / P.pageSize), days = Math.ceil(req / DAILY), mins = Math.round(req * P.pause / 60 * 10) / 10;
    stats.replaceChildren(
      h("div", { class: "stat" + (req > DAILY ? " bad" : "") }, h("small", {}, "Requests needed"), h("b", {}, String(req))),
      h("div", { class: "stat" + (days > 1 ? " bad" : "") }, h("small", {}, "Days at 50 a day"), h("b", {}, String(days))),
      h("div", { class: "stat" + (P.pause < MINPAUSE ? " bad" : "") }, h("small", {}, "Time spent waiting"), h("b", {}, mins + " min")));
  };
  const check = () => {
    const req = Math.ceil(NEED / P.pageSize), msgs = [];
    if (P.pause < MINPAUSE) msgs.push(`The platform asks for at least ${MINPAUSE} seconds between requests. Faster than that can get you blocked.`);
    if (req > DAILY) msgs.push(`That needs ${req} requests but only ${DAILY} are allowed per day, so it would take ${Math.ceil(req / DAILY)} days. Raise the page size (up to ${MAXPAGE}).`);
    if (!first.get()) msgs.push("Choose what you do with each response first.");
    else if (first.get() !== "raw") msgs.push("Not that one first. If you parse or change data before saving the raw response, you cannot go back and check what you lost. Save the raw response first.");
    if (msgs.length) setFb("bad", msgs.join(" ")); else { solved(); setFb("good", def.win, true); }
  };
  const left = [h("div", { class: "givens" }, `Need about ${NEED} comments. Up to ${MAXPAGE} per request, ${DAILY} requests per day, at least ${MINPAUSE} seconds between requests. (Invented limits.)`),
    slider("ps", "Page size (items per request)", 25, 100, 25, P.pageSize, "pageSize", v => String(v)),
    slider("pa", "Pause between requests (seconds)", 0, 10, 1, P.pause, "pause", v => v + " s"), stats];
  const right = [h("p", { class: "label" }, "With each response, what do you do first?"), first,
    h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: check }, "Check my plan"), hintBtn(def)),
    h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  render();
  return { left, right };
}

/* level 4 */
function buildAsk(def) {
  const st = L = { def, token: 0 }, picks = SCENARIOS.map(() => choose(ASK_OPTS));
  const cards = SCENARIOS.map((c, i) => h("div", { class: "scn", id: "s" + i }, h("p", { class: "label" }, "Scenario " + (i + 1)), h("blockquote", {}, c.q), picks[i]));
  const check = () => {
    if (picks.some(p => !p.get())) { setFb("warn", "Choose an answer for every scenario."); return; }
    let all = true; const out = [];
    SCENARIOS.forEach((c, i) => {
      const ok = picks[i].get() === c.a; all = all && ok; cards[i].className = "scn " + (ok ? "right" : "wrong");
      out.push(`Scenario ${i + 1}: ${ok ? "right. " : "not quite. "}${c.why}`);
    });
    if (all) { solved(); setFb("good", def.win + " " + out.join(" "), true); } else setFb("bad", out.join(" "));
  };
  const left = cards;
  const right = [h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: check }, "Check my answers"), hintBtn(def)),
    h("div", { class: "tray" }, h("p", { class: "label" }, "Who to ask"), h("p", {}, "Your supervisor or your university's ethics office. These are rules of thumb for discussion, not legal advice.")),
    h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  return { left, right };
}

/* bridge */
function stubCode() {
  const P = S.plan;
  return [
    "import datetime, json, os, time", "", 'os.makedirs("raw", exist_ok=True)', "",
    'log = {"query": "YOUR QUERY", "tool": "YOUR TOOL", "collected_on": str(datetime.date.today()),',
    `       "page_size": ${P.pageSize}, "pause_seconds": ${P.pause}, "pages": 0, "items": 0}`, "",
    "def collect_page(cursor):", "    # replace with your platform's request, or use sample_api from the notebook", "    raise NotImplementedError", "",
    "cursor, n = None, 0", "while n < 3:   # the first three pages", "    page = collect_page(cursor)",
    '    with open(f"raw/page_{n + 1:03d}.json", "w", encoding="utf-8") as f:',
    "        json.dump(page, f, ensure_ascii=False, indent=2)   # raw, untouched, before anything else",
    '    log["pages"] += 1', '    log["items"] += len(page["items"])', '    cursor = page.get("next_cursor")', "    n += 1",
    '    time.sleep(log["pause_seconds"])', "",
    'with open("raw/collection_log.json", "w", encoding="utf-8") as f:', "    json.dump(log, f, indent=2)", "print(log)"
  ].join("\n");
}
function buildBridge(def) {
  const prompt = "Write a Python loop that collects pages from an API using a next-page cursor, saves each raw JSON response to a file before doing anything else, waits between requests, and writes a log with the query, the date and the number of pages and items. Explain each line in one sentence. Do not include any real API key.";
  const left = [codeCard("Task 1: your collection stub", stubCode(), "This uses the page size and pause you chose in level 3. Paste it into the notebook's warm-up cell, and change the one function that talks to the platform.")];
  const right = [
    codeCard("Task 2: ask an AI, then compare", prompt, "Paste this into your AI assistant. Does its code save the raw response first? Does it pause?"),
    h("div", { class: "tray" }, h("p", { class: "label" }, "Task 3: check"), h("p", {}, "After it runs, count the files in raw/ and compare with the log. Log one check you ran. Never paste a key into an AI chat.")),
    h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: () => { solved(); setFb("good", "Done. In Exercise 2 you will compare the raw counts with your parsed table."); } }, "I ran all three")),
    h("div", { id: "fb", class: "fb", "aria-live": "polite" })
  ];
  return { left, right };
}

BUILDERS.sort = buildSort; BUILDERS.meter = buildMeter; BUILDERS.plan = buildPlan; BUILDERS.ask = buildAsk; BUILDERS.bridge = buildBridge;
boot("cactus-before-you-collect-done");
