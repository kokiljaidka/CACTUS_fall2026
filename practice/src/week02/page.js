/* Week 2: Silent Changes. Uses the shared engine (practice/shared/engine.js). */

const TOY = /*__TOY_JSON__*/;
const COLS = ["id", "date", "comment", "country", "tone_pos"];

const WORLDS = [
  { name: "Build the pipeline", blurb: "Row counts",
    idea: "Every cleaning step keeps, changes, or removes rows. A step that removes rows needs a reason you can say out loud. Code can run with no error and still change your answer.",
    where: "In the notebook: print len(df) after each step. That one habit catches most silent changes." },
  { name: "Find the bug", blurb: "No error shown",
    idea: "Bugs that change the answer rarely raise an error. You find them by asking what each line does to the rows and numbers, then proving it with a check.",
    where: "In the notebook: a row count, a hand count of a few rows, or a second method are all checks." },
  { name: "Take it to Colab", blurb: "Real code",
    idea: "You have seen the pipeline work. Now write it as real code and check it against the same numbers.",
    where: "The Week 2 notebook has a warm-up cell with this exact table, before Exercise 1." }
];

/* ---------- pipeline cards ---------- */
const CARDS = {
  dedupe: { label: "Remove exact duplicate rows", code: "df = df.drop_duplicates()" },
  blank: { label: "Remove rows with no comment text", code: 'df = df.dropna(subset=["comment"])' },
  date: { label: "Turn the date text into real dates", code: 'df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d", errors="coerce")' },
  tone: { label: "Turn tone_pos text into numbers", code: 'df["tone_pos"] = pd.to_numeric(df["tone_pos"], errors="coerce")' },
  dropTone: { label: "Drop rows where tone_pos is missing", code: 'df = df.dropna(subset=["tone_pos"])', trap: true },
  fillZero: { label: "Fill missing tone_pos with 0", code: 'df["tone_pos"] = df["tone_pos"].fillna(0)', trap: true },
  head20: { label: "Keep only the first 20 rows", code: "df = df.head(20)", trap: true }
};
const GOOD = ["dedupe", "blank", "date", "tone"];
const CARD_ORDER = ["head20", "tone", "dropTone", "dedupe", "fillZero", "date", "blank"];

const isNumText = v => /^-?\d+(\.\d+)?$/.test(String(v).trim());
const blankTone = r => r.tone_pos === null || r.tone_pos === "";
const rowKey = r => JSON.stringify([r.id, r.date, r.comment, r.country, r.tone_pos]);

function simulate(keys) {
  let rows = TOY.map(r => ({ ...r }));
  const steps = []; let toneNum = false, dateParsed = false;
  for (const k of keys) {
    const before = rows.length; let note = "";
    if (k === "dedupe") {
      const seen = new Set();
      rows = rows.filter(r => { const key = rowKey(r); if (seen.has(key)) return false; seen.add(key); return true; });
    } else if (k === "blank") {
      rows = rows.filter(r => String(r.comment).trim() !== "");
    } else if (k === "date") {
      let bad = 0;
      rows.forEach(r => { if (r.date !== null && !/^\d{4}-\d{2}-\d{2}$/.test(String(r.date))) { r.date = null; bad++; } });
      dateParsed = true;
      if (bad) note = `${bad} date${bad === 1 ? "" : "s"} were written another way (like 13/10/2024) and became blank. The rows are kept, but you would look at them.`;
    } else if (k === "tone") {
      let bad = 0;
      rows.forEach(r => { if (r.tone_pos === null) { bad++; return; } if (isNumText(r.tone_pos)) r.tone_pos = parseFloat(r.tone_pos); else { r.tone_pos = null; bad++; } });
      toneNum = true;
      if (bad) note = `${bad} score${bad === 1 ? "" : "s"} could not be read as numbers ("unknown", "-", or empty) and became blank. The rows are kept.`;
    } else if (k === "dropTone") {
      rows = rows.filter(r => !blankTone(r));
      note = toneNum ? "These comments were fine. Only the score was missing." : "While tone_pos is still text, only truly empty cells count as missing. \"unknown\" and \"-\" stayed.";
    } else if (k === "fillZero") {
      rows.forEach(r => { if (blankTone(r)) r.tone_pos = toneNum ? 0 : "0"; });
      note = "Unknown became 0, which means \"no positive words\". That is invented data.";
    } else if (k === "head20") {
      rows = rows.slice(0, 20);
      note = "Everything after row 20 is gone, including whole groups of comments.";
    }
    steps.push({ key: k, before, after: rows.length, note });
  }
  return { rows, steps, toneNum, dateParsed };
}
const numericTones = rows => rows.filter(r => typeof r.tone_pos === "number");
const meanOf = a => a.length ? a.reduce((s, v) => s + v, 0) / a.length : null;
const fmt = x => x === null ? "n/a" : x.toFixed(1);
function summarize(res) {
  const t = numericTones(res.rows);
  const by = {};
  ["SG", "TH", "HK"].forEach(c => { by[c] = meanOf(t.filter(r => r.country === c).map(r => r.tone_pos)); });
  return { overall: meanOf(t.map(r => r.tone_pos)), by };
}
function pipelineCode(keys) {
  const out = ["import io", "import pandas as pd", "", "# TOY_CSV is defined in the notebook warm-up cell", "df = pd.read_csv(io.StringIO(TOY_CSV))", 'counts = {"start": len(df)}'];
  keys.forEach((k, i) => { out.push(CARDS[k].code); out.push(`counts[${JSON.stringify((i + 1) + ". " + CARDS[k].label)}] = len(df)`); });
  out.push("print(counts)");
  return out.join("\n");
}

const LEVELS = [
  { w: 0, kind: "pipeline", title: "Clean the café table",
    task: "This table of 30 comments is messy. Drag cards into the pipeline so the table is clean and every row you lose has a good reason. Some cards look helpful but quietly damage the data.",
    hint: "Look at the table: repeated rows, empty comments, text where numbers or dates should be. Then ask of each card: does it fix a real problem, or does it throw away good data?",
    win: "Clean, and every removed row had a reason. Two steps removed rows. Two only changed types, and the values that could not be read were flagged as blank instead of being thrown away or invented." },

  { w: 1, kind: "bug", title: "The average that is off",
    task: "An AI assistant wrote this analysis of café comments. It runs and prints a number. Click the line that makes the number misleading, then pick the check that would prove it.",
    code: ['import pandas as pd', 'df = pd.read_csv("cafe_comments.csv")', 'by_country = df.groupby("country")["tone_pos"].mean()', 'print(by_country)', 'overall = by_country.mean()', 'print("Average positivity (%):", round(overall, 1))'],
    output: "country\nHK    12.0\nSG     6.0\nTH     4.0\nName: tone_pos, dtype: float64\nAverage positivity (%): 7.3",
    bug: 4,
    explain: { 2: "That line is fine: it averages within each country.", 3: "That only prints the three country averages.", 5: "That only prints the number from the line above it." },
    checks: [
      { label: "Count the rows in each country with df[\"country\"].value_counts() and compare with the average", ok: true, why: "Group sizes are HK 3, SG 6, TH 21. A mean of the three averages gives HK's 3 comments the same weight as TH's 21. Averaging all 30 rows gives 5.2, not 7.3." },
      { label: "Run the same cell again and see whether the answer changes", ok: false, why: "The code is not random, so the same wrong number comes back every time. A rerun proves nothing." },
      { label: "Check the column names are spelled correctly", ok: false, why: "A misspelled column would have raised an error. This bug runs without one." }
    ],
    hint: "What does by_country.mean() treat as equal: comments, or countries?",
    win: "An average of averages ignores group sizes. Check the counts behind any average before you trust it." },

  { w: 1, kind: "bug", title: "The missing comments",
    task: "The file has 30 comments. Find the line that quietly loses some of them, then pick the check that proves it.",
    code: ['import pandas as pd', 'comments = pd.read_csv("cafe_comments.csv")   # 30 rows', 'places = pd.read_csv("places.csv")            # country_code, region', 'merged = comments.merge(places, on="country_code")', 'print(len(merged), "comments analysed")', 'print(merged.groupby("region")["tone_pos"].mean().round(1))'],
    output: "24 comments analysed\nregion\nEast Asia          5.4\nSoutheast Asia    4.6\nName: tone_pos, dtype: float64",
    bug: 3,
    explain: { 1: "That line only reads the file. The comment says 30 rows.", 2: "That line only reads a small lookup table.", 4: "That line prints the count honestly. Look at what it prints compared with line 2.", 5: "That line only summarizes what is in merged." },
    checks: [
      { label: "Print len(comments) next to len(merged), and list the country codes in comments that are missing from places", ok: true, why: "30 rows went in and 24 came out. By default merge keeps only matching rows, and six comments used lowercase codes like \"th\" that did not match \"TH\". Nothing warned you." },
      { label: "Sort the output by region and see if it looks tidier", ok: false, why: "Sorting changes the order, not what is missing." },
      { label: "Check the merged table has the right column names", ok: false, why: "The columns are fine. The problem is which rows survived." }
    ],
    hint: "Compare the number printed on line 5 with the number in the comment on line 2.",
    win: "A merge is a silent filter. Print the row count before and after, and look at the keys that did not match." },

  { w: 1, kind: "bug", title: "The count that is too low",
    task: "The code reports how many comments mention the café. The real number looks higher. Find the line and the check.",
    code: ['import pandas as pd', 'df = pd.read_csv("cafe_comments_clean.csv")   # 30 rows, no missing text', 'mentions = df[df["comment"].str.contains("Brew Lane")]', 'print(len(mentions), "of", len(df), "comments mention Brew Lane")'],
    output: "18 of 30 comments mention Brew Lane",
    bug: 2,
    explain: { 1: "That line only reads the file.", 3: "That line only prints the count from the line above." },
    checks: [
      { label: "Search a few spellings by hand (\"brew lane\", \"BREW LANE\") and compare the counts", ok: true, why: "str.contains is case sensitive. Matching ignoring case finds 27, because 9 comments wrote \"brew lane\" in lowercase. Use case=False, or lowercase the text first." },
      { label: "Print the first five rows of the table", ok: false, why: "Five rows will not show which spellings exist in the other 25." },
      { label: "Check that df has 30 rows", ok: false, why: "It does have 30 rows. The loss happens in the filter, not the load." }
    ],
    hint: "How many ways can people spell a name?",
    win: "Text matching is literal. Try variants before you trust a count of mentions." },

  { w: 2, kind: "bridge", bridge: true, title: "Rebuild it in Colab",
    task: "Open the Week 2 notebook, find the warm-up cell before Exercise 1, and write the pipeline you built here as real code." }
];

/* ---------- pipeline level ---------- */
function buildPipeline(def) {
  const st = L = { def, keys: [], pred: "", token: 0 };
  const toy = h("div", { class: "toywrap" }, h("table", { class: "toytable" },
    h("thead", {}, h("tr", {}, COLS.map(c => h("th", {}, c)))),
    h("tbody", {}, TOY.map(r => h("tr", {}, COLS.map(c => h("td", { class: c === "tone_pos" ? "num" : "" }, r[c] === "" ? "(empty)" : String(r[c]))))))));
  const zoneWrap = h("div"), resultWrap = h("div");
  const cardBody = (k, extra) => {
    const c = CARDS[k];
    return h("div", { class: "cardtext" }, c.label, h("small", {}, c.code));
  };
  const renderZone = () => {
    S.pipeKeys = st.keys.slice();
    const z = h("div", { class: "zone", "data-hint": "Drag cards here, in the order they should run" });
    st.keys.forEach((k, i) => {
      const el = h("div", { class: "card" + (CARDS[k].trap ? " trap" : "") }, h("b", {}, String(i + 1) + "."), cardBody(k),
        h("button", { class: "x", type: "button", "data-nodrag": true, "aria-label": "Remove card", onclick: () => { st.keys.splice(i, 1); renderZone(); } }, "×"));
      makeDraggable(el, { payload: { card: k }, pickup: () => { st.keys.splice(i, 1); renderZone(); } });
      z.append(el);
    });
    makeDrop(z, (p, pt) => {
      if (st.keys.includes(p.card)) { renderZone(); return; }
      const kids = [...z.children].filter(c => c.classList.contains("card"));
      let idx = kids.findIndex(c => { const r = c.getBoundingClientRect(); return pt.y < r.top + r.height / 2; });
      if (idx < 0) idx = st.keys.length;
      st.keys.splice(idx, 0, p.card); renderZone();
    });
    zoneWrap.replaceChildren(z);
  };
  renderZone();
  const palette = h("div", { class: "opts" });
  CARD_ORDER.forEach(k => {
    const el = h("div", { class: "card" + (CARDS[k].trap ? " trap" : "") }, cardBody(k));
    makeDraggable(el, { payload: { card: k }, tap: () => { if (!st.keys.includes(k)) { st.keys.push(k); renderZone(); } } });
    palette.append(el);
  });
  const predIn = h("input", { id: "predrows", class: "numin", type: "number", min: "0", inputmode: "numeric", placeholder: "rows", oninput: e => { st.pred = e.target.value; } });

  const run = () => {
    if (!st.keys.length) { setFb("warn", "Drag at least one card into the pipeline first."); return; }
    if (st.pred.trim() === "") { setFb("warn", "Type your prediction first: how many rows will be left? A guess is fine."); predIn.focus(); return; }
    const res = simulate(st.keys), ref = simulate(GOOD), sm = summarize(res), rs = summarize(ref);
    const tbody = h("tbody", {}, h("tr", {}, h("td", {}, "Start"), h("td", { class: "n" }, String(TOY.length)), h("td", {}, "")));
    res.steps.forEach((s, i) => {
      const lost = s.before - s.after;
      tbody.append(h("tr", {}, h("td", {}, `${i + 1}. ${CARDS[s.key].label}`, s.note ? h("span", { class: "note" }, s.note) : null),
        h("td", { class: "n" }, `${s.before} → ${s.after}`), h("td", { class: "n" + (lost ? " lost" : "") }, lost ? `−${lost}` : "0")));
    });
    const by = ["SG", "TH", "HK"].map(c => `${c} ${fmt(sm.by[c])}`).join(" · ");
    resultWrap.replaceChildren(
      h("table", { class: "waterfall" }, h("thead", {}, h("tr", {}, h("th", {}, "Step"), h("th", {}, "Rows"), h("th", {}, "Lost"))), tbody),
      h("div", { class: "summary" }, h("div", {}, h("b", {}, `${res.rows.length} rows`), ` · average positive-word share ${fmt(sm.overall)}%`), h("div", {}, "By country: " + by),
        h("div", { class: "tipline" }, `Honest pipeline for comparison: ${ref.rows.length} rows · ${fmt(rs.overall)}%`)));
    const n = res.rows.length, predNote = (parseInt(st.pred, 10) === n) ? " Your prediction matched." : ` You predicted ${st.pred}; the pipeline leaves ${n}.`;
    const traps = st.keys.filter(k => CARDS[k].trap), missing = GOOD.filter(k => !st.keys.includes(k));
    if (traps.length) {
      const costs = traps.map(k => ({ head20: "Keeping only 20 rows drops whole stretches of the data", dropTone: "Dropping rows with a missing score throws away comments that were fine", fillZero: "Filling with 0 invents data and pulls the average down" })[k]);
      setFb("bad", costs.join(". ") + `. Your result: ${n} rows and ${fmt(sm.overall)}%, against ${ref.rows.length} rows and ${fmt(rs.overall)}% for the honest pipeline.` + predNote);
    } else if (missing.length) {
      const seen = new Set(), dups = res.rows.filter(r => { const k = rowKey(r); if (seen.has(k)) return true; seen.add(k); return false; }).length;
      const left = [];
      if (missing.includes("dedupe")) left.push(`${dups} duplicate rows are still there`);
      if (missing.includes("blank")) left.push(`${res.rows.filter(r => String(r.comment).trim() === "").length} rows have no comment text`);
      if (missing.includes("date")) left.push("dates are still text");
      if (missing.includes("tone")) left.push("tone_pos is still text, so averages would be wrong or fail");
      setFb("info", "Still to fix: " + left.join("; ") + "." + predNote);
    } else { solved(); setFb("good", def.win + predNote, true); }
  };
  const left = [h("p", { class: "label" }, "The table (30 rows, as loaded)"), toy, h("p", { class: "tipline" }, "Fictional café comments. SG, TH, and HK are countries. tone_pos is the share of positive words.")];
  const right = [
    h("div", { class: "tray" }, h("p", { class: "label" }, "Cards"), palette, h("p", { class: "tipline" }, "Drag into the pipeline, or tap to add.")),
    h("p", { class: "label" }, "Pipeline (runs top to bottom)"), zoneWrap,
    h("div", { class: "predict" }, h("label", { class: "label", for: "predrows" }, "Before you run: how many rows will be left?"), predIn),
    h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: run }, "Run pipeline"), h("button", { class: "btn", type: "button", onclick: () => { st.keys.length = 0; renderZone(); resultWrap.replaceChildren(); const f = $("#fb"); if (f) { f.className = "fb"; f.replaceChildren(); } } }, "Clear"), hintBtn(def)),
    resultWrap,
    h("div", { id: "fb", class: "fb", "aria-live": "polite" })
  ];
  return { left, right };
}

/* ---------- bug-hunt levels ---------- */
function buildBug(def) {
  const st = L = { def, lineOk: false, picked: null, token: 0 };
  const linesWrap = h("div", { class: "codelines" }), optsWrap = h("div", { class: "opts" });
  const renderLines = () => {
    linesWrap.replaceChildren(...def.code.map((t, i) => {
      const cls = "cl" + (st.lineOk && i === def.bug ? " right" : (st.picked === i ? " picked" : ""));
      return h("button", { class: cls, type: "button", "aria-label": `Line ${i + 1}`, onclick: () => pickLine(i) }, h("span", { class: "no" }, String(i + 1)), h("span", {}, t));
    }));
  };
  const renderOpts = () => {
    optsWrap.replaceChildren();
    if (!st.lineOk) { optsWrap.append(h("p", { class: "tipline" }, "Click a line of code on the left to start.")); return; }
    optsWrap.append(h("p", { class: "label" }, "Which check would prove it?"));
    def.checks.forEach((c, i) => {
      const b = h("button", { class: "opt", type: "button", onclick: () => {
        if (c.ok) { b.classList.add("right"); solved(); setFb("good", c.why + " " + def.win, true); }
        else { b.classList.add("wrong"); setFb("bad", c.why); }
      } }, c.label);
      optsWrap.append(b);
    });
  };
  const pickLine = i => {
    if (st.lineOk) return;
    st.picked = i;
    if (i === def.bug) { st.lineOk = true; setFb("info", "That is the line. Now pick the check that would prove it."); }
    else setFb("warn", (def.explain && def.explain[i]) || "That line does what it says. Look for the line that decides which rows or numbers the answer is based on.");
    renderLines(); renderOpts();
  };
  renderLines(); renderOpts();
  const left = [h("p", { class: "label" }, "AI-written code"), linesWrap, h("p", { class: "label" }, "What it printed"), h("div", { class: "outbox" }, def.output)];
  const right = [optsWrap, h("div", { class: "row" }, hintBtn(def)), h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  return { left, right };
}

/* ---------- Colab bridge ---------- */
function buildBridge(def) {
  const own = !!S.pipeKeys && S.pipeKeys.length > 0;
  const keys = own ? S.pipeKeys : GOOD;
  const prompt = "I have a pandas DataFrame df read from a CSV with columns id, date, comment, country, tone_pos. Write pandas code that removes exact duplicate rows, removes rows with no comment, turns date into dates, and turns tone_pos into numbers. Print len(df) after each step. Explain each line in one sentence.";
  const left = [
    codeCard("Task 1: your pipeline as code", pipelineCode(keys), own ? "This is the pipeline from level 1, in the order you built it. Paste it into the notebook's warm-up cell and run it. It prints a row count after each step." : "You have not built a pipeline in level 1 yet, so this is the standard one. Go back to level 1 to build yours.")
  ];
  const right = [
    codeCard("Task 2: ask an AI, then compare", prompt, "Paste this into your AI assistant. Read what it wrote. Is it the same as Task 1? Did it print counts after each step?"),
    h("div", { class: "tray" }, h("p", { class: "label" }, "Task 3: check"), h("p", {}, "Run the notebook's check cell. It tells you if the final table is clean. Then log one check that caught or confirmed something.")),
    h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: () => { solved(); setFb("good", "Done. In Exercise 2 the code you will review runs without errors but changes the answer. Use the same habit: count rows before and after."); } }, "I ran all three")),
    h("div", { id: "fb", class: "fb", "aria-live": "polite" })
  ];
  return { left, right };
}

BUILDERS.pipeline = buildPipeline; BUILDERS.bug = buildBug; BUILDERS.bridge = buildBridge;
boot("cactus-silent-changes-done");
