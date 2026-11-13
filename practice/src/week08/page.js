/* Week 8: Run It from Scratch. Uses the shared engine (practice/shared/engine.js). All notebooks, paths and keys on this page are invented. */

const WORLDS = [
  { name: "Order", blurb: "Top to bottom",
    idea: "A notebook remembers what you ran, in the order you ran it. A fresh runtime runs only what is written, top to bottom. If the order is wrong, it fails.",
    where: "In your own notebook: Runtime, then Restart session and run all." },
  { name: "Hidden state", blurb: "What the session remembers",
    idea: "A variable can exist in your session after you delete the cell that made it. Your notebook still seems to work, but nobody else can run it.",
    where: "In your own notebook: the first error after a restart is the finding." },
  { name: "Paths", blurb: "Where the data lives",
    idea: "A path that only exists on your computer breaks for everyone else. Say where the data comes from, and use a path that works after they put it in the same place.",
    where: "In your README: where to get the data, and where to put it." },
  { name: "Secrets", blurb: "Keys and private data",
    idea: "A key or private data in a shared notebook is already shared. Keep keys in Colab Secrets. If one leaks, replace it. Deleting the file does not undo it.",
    where: "In your repository: search it before you share the link." },
  { name: "Take it to Colab", blurb: "Your notebook",
    idea: "You have fixed made-up notebooks. Now rerun your own from scratch and write down how to rerun it.",
    where: "Do this before Week 8, so your partner can rerun it." }
];

const choose = (opts, onpick) => {
  const wrap = h("div", { class: "choice", role: "group" }); let cur = null; const btns = [];
  opts.forEach(o => {
    const b = h("button", { class: "pill", type: "button", onclick: () => { cur = o.v; btns.forEach(x => x.classList.toggle("on", x === b)); onpick && onpick(cur); } }, o.t);
    btns.push(b); wrap.append(b);
  });
  wrap.get = () => cur; return wrap;
};

/* ---------- level 1: order ---------- */
const CELLS = [
  { id: "A", code: "import pandas as pd", needs: [], defs: ["pd"], out: "" },
  { id: "B", code: "df = pd.read_csv(\"data/posts.csv\")", needs: ["pd"], defs: ["df"], out: "" },
  { id: "C", code: "clean = df.drop_duplicates()", needs: ["df"], defs: ["clean"], out: "" },
  { id: "D", code: "print(len(clean))", needs: ["clean"], defs: [], out: "812" },
  { id: "E", code: "clean.to_csv(\"data/posts_clean.csv\")", needs: ["clean"], defs: [], out: "" }
];
function buildOrder(def) {
  L = { def, token: 0 };
  let order = ["B", "D", "A", "C", "E"];
  const list = h("div", { class: "togs" }), result = h("p", { class: "tipline", "aria-live": "polite" });
  const byId = id => CELLS.find(c => c.id === id);
  function run() {
    const have = new Set(); const rows = [];
    for (let i = 0; i < order.length; i++) {
      const c = byId(order[i]); const miss = c.needs.find(n => !have.has(n));
      if (miss) { rows.push({ i, err: `NameError: name '${miss}' is not defined` }); return rows; }
      c.defs.forEach(d => have.add(d)); rows.push({ i, out: c.out });
    }
    return rows;
  }
  function draw(rows) {
    list.replaceChildren(...order.map((id, i) => {
      const c = byId(id), r = rows && rows.find(x => x.i === i);
      const cls = "nbcell" + (r ? (r.err ? " err" : " ok") : "");
      return h("div", { class: cls },
        h("span", { class: "idx" }, `[${i + 1}]`), h("code", {}, c.code),
        h("span", { class: "mv" },
          h("button", { class: "btn", type: "button", "aria-label": "Move up", disabled: i === 0, onclick: () => { [order[i - 1], order[i]] = [order[i], order[i - 1]]; draw(null); } }, "↑"),
          h("button", { class: "btn", type: "button", "aria-label": "Move down", disabled: i === order.length - 1, onclick: () => { [order[i + 1], order[i]] = [order[i], order[i + 1]]; draw(null); } }, "↓")),
        r ? h("span", { class: "out" + (r.err ? " bad" : "") }, r.err || (r.out ? "→ " + r.out : "ran")) : null);
    }));
  }
  const restart = () => {
    const rows = run(); draw(rows);
    const bad = rows.find(r => r.err);
    if (bad) setFb("bad", `Restart and run all stopped at cell ${bad.i + 1}: ${bad.err}. The cells above it have not made that name yet. Which cell does?`);
    else { solved(); setFb("good", def.win, true); }
  };
  draw(null);
  const left = [h("div", { class: "givens" }, "A student's five-cell notebook, saved in a mixed-up order. It worked on her laptop because she ran the cells in a good order by hand. A fresh runtime runs them top to bottom. Use the arrows to put them in an order that runs."), list, result];
  const right = [h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: restart }, "Restart and run all"), hintBtn(def)), h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  return { left, right };
}

/* ---------- level 2: hidden state ---------- */
const FIX_OPTS = [
  { v: "put", t: "Put the line back in a cell above, and restart and run all" },
  { v: "hope", t: "Leave it. It works on my laptop" },
  { v: "paste", t: "Type the number 812 into the next cell by hand" }
];
function buildHidden(def) {
  L = { def, token: 0 };
  const pick = choose(FIX_OPTS);
  const left = [h("div", { class: "givens" }, "Last week this notebook worked. This week she tidied it up and deleted the middle cell. On her laptop it still prints 812. On her partner's laptop it fails."),
    h("div", { class: "togs" },
      h("div", { class: "nbcell" }, h("span", { class: "idx" }, "[1]"), h("code", {}, "df = pd.read_csv(\"data/posts.csv\")")),
      h("div", { class: "nbcell gone" }, h("span", { class: "idx" }, "[ ]"), h("code", {}, "# deleted: clean = df.drop_duplicates()")),
      h("div", { class: "nbcell" }, h("span", { class: "idx" }, "[3]"), h("code", {}, "print(len(clean))"), h("span", { class: "out" }, "→ 812 on her laptop (the session still remembers `clean`)")),
      h("div", { class: "nbcell err" }, h("span", { class: "idx" }, "[3]"), h("code", {}, "print(len(clean))"), h("span", { class: "out bad" }, "NameError: name 'clean' is not defined   (fresh runtime)")))];
  const check = () => {
    const v = pick.get();
    if (!v) { setFb("warn", "Pick a fix first."); return; }
    if (v === "put") { solved(); setFb("good", def.win, true); }
    else if (v === "hope") setFb("bad", "A notebook that only works in your own session cannot be rerun by anyone else, and may not rerun for you tomorrow. Restart and run all is the honest test.");
    else setFb("bad", "A number typed in by hand is a result nobody can check. If the data changes, it will be silently wrong.");
  };
  const right = [pick, h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: check }, "Check my fix"), hintBtn(def)), h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  return { left, right };
}

/* ---------- level 3: paths ---------- */
const PATHS = [
  { q: "pd.read_csv(\"/Users/aisha/Documents/cactus/posts.csv\")", a: "me", why: "A folder on one person's computer." },
  { q: "pd.read_csv(\"data/posts.csv\")   # README: put posts.csv in a folder called data", a: "all", why: "A relative path, and the README says where the file comes from and where to put it." },
  { q: "pd.read_csv(\"C:\\\\Users\\\\raj\\\\Downloads\\\\posts.csv\")", a: "me", why: "A Windows folder on one person's computer." },
  { q: "pd.read_csv(\"/content/drive/MyDrive/cactus/posts.csv\")", a: "me", why: "Only works if the partner has the same Drive folder, which they do not. Use a shared link or a README." },
  { q: "pd.read_csv(\"https://example.org/cactus/posts.csv\")   # a public link", a: "all", why: "Works for anyone, as long as the data is allowed to be public." },
  { q: "os.chdir(\"/home/raj/project\")", a: "me", why: "Changes to a folder that exists only on one machine." }
];
const PATH_OPTS = [{ v: "all", t: "Works for a partner" }, { v: "me", t: "Only works for me" }];
function buildPaths(def) {
  L = { def, token: 0 };
  const picks = PATHS.map(() => choose(PATH_OPTS));
  const cards = PATHS.map((c, i) => h("div", { class: "case", id: "p" + i }, h("blockquote", {}, h("code", {}, c.q)), picks[i]));
  const check = () => {
    if (picks.some(p => !p.get())) { setFb("warn", "Decide on every line."); return; }
    let n = 0;
    PATHS.forEach((c, i) => { const ok = picks[i].get() === c.a; if (ok) n++; cards[i].className = "case " + (ok ? "right" : "wrong"); cards[i].querySelector(".why")?.remove(); cards[i].append(h("p", { class: "why" }, (ok ? "Right. " : "Not quite. ") + c.why)); });
    if (n === 6) { solved(); setFb("good", def.win, true); } else setFb("bad", `${n} of 6. Ask of each line: if my partner has only the notebook and the README, will this line find the file?`);
  };
  const left = [h("div", { class: "givens" }, "Six lines that load data. Your partner will rerun your notebook on their own computer, with only your notebook and your README. Which lines will work for them?")];
  const right = [...cards, h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: check }, "Check my answers"), hintBtn(def)), h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  return { left, right };
}

/* ---------- level 4: secrets ---------- */
const SECRETS = [
  { q: "API_KEY = \"sk-live-83hd9s0a7x2k\"", a: "no", why: "A key written into the notebook. Anyone with the link has it." },
  { q: "key = userdata.get(\"SERPAPI_KEY\")", a: "ok", why: "Reads the key from Colab Secrets. The key itself is not in the notebook." },
  { q: "df.head()   # the output shows ten rows with full names and handles", a: "no", why: "Saved outputs travel with the notebook. Personal data in an output is shared too." },
  { q: "# the key is stored in Colab Secrets under the name SERPAPI_KEY", a: "ok", why: "A note that says where the key lives, not the key." },
  { q: "print(os.environ)   # the saved output lists every environment variable", a: "no", why: "Environment variables can include tokens. Do not print them into a shared notebook." },
  { q: "requests.get(url, params={\"api_key\": key})", a: "ok", why: "Uses the variable. The key is not written here." }
];
const SECRET_OPTS = [{ v: "ok", t: "Fine to share" }, { v: "no", t: "Must not be shared" }];
const LEAK_OPTS = [
  { v: "delete", t: "Delete the file and push again" },
  { v: "revoke", t: "Revoke the key and make a new one" },
  { v: "hope", t: "Nothing. Nobody has looked" }
];
function buildSecrets(def) {
  L = { def, token: 0 };
  const picks = SECRETS.map(() => choose(SECRET_OPTS));
  const cards = SECRETS.map((c, i) => h("div", { class: "case", id: "s" + i }, h("blockquote", {}, h("code", {}, c.q)), picks[i]));
  const leak = choose(LEAK_OPTS);
  const leakCard = h("div", { class: "case", id: "leak" }, h("p", { class: "label" }, "A key was in a notebook you already pushed to GitHub. What do you do first?"), leak);
  const check = () => {
    if (picks.some(p => !p.get()) || !leak.get()) { setFb("warn", "Decide on every line and the last question."); return; }
    let n = 0;
    SECRETS.forEach((c, i) => { const ok = picks[i].get() === c.a; if (ok) n++; cards[i].className = "case " + (ok ? "right" : "wrong"); cards[i].querySelector(".why")?.remove(); cards[i].append(h("p", { class: "why" }, (ok ? "Right. " : "Not quite. ") + c.why)); });
    const lk = leak.get() === "revoke"; leakCard.className = "case " + (lk ? "right" : "wrong"); leakCard.querySelector(".why")?.remove();
    leakCard.append(h("p", { class: "why" }, lk ? "Right. A pushed key stays in the history, and may already have been copied. Replace the key first; then clean up." : "Deleting the file does not remove it from the history, and the key may already have been copied. Revoke it and make a new one."));
    if (n === 6 && lk) { solved(); setFb("good", def.win, true); } else setFb("bad", `${n} of 6 lines${lk ? "" : ", and the last question needs another look"}. Is the secret itself in the notebook, or only a way to reach it?`);
  };
  const left = [h("div", { class: "givens" }, "Six lines or outputs from notebooks about to be shared. Which are safe to share, and which are not? Then one question about a leak.")];
  const right = [...cards, leakCard, h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: check }, "Check my answers"), hintBtn(def)), h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  return { left, right };
}

const LEVELS = [
  { w: 0, kind: "order", title: "Restart and run all",
    task: "Put the five cells in an order that runs from a fresh runtime. Press Restart and run all to see where it stops.",
    hint: "A cell can only use names that a cell above it has made. Which cell makes `pd`? Which makes `df`?",
    win: "Top to bottom works. The first error after a restart tells you which cell used a name too early." },
  { w: 1, kind: "hidden", title: "The cell you deleted",
    task: "Her notebook works on her laptop and fails on her partner's. Choose the fix.",
    hint: "Where did `clean` come from? Who else has it?",
    win: "The session remembered `clean` after the cell was gone. The fix is to put the line back and to test with a restart, so it fails for you first." },
  { w: 2, kind: "paths", title: "Paths that only work for you",
    task: "Six lines that load data. Decide which will work on a partner's computer.",
    hint: "Think of a partner with only your notebook and your README. Does the line find the file?",
    win: "Relative paths and public links travel. Folders on your computer do not. Say in the README where the data comes from and where to put it." },
  { w: 3, kind: "secrets", title: "Keys and private data",
    task: "Sort six lines, then decide what to do about a leaked key.",
    hint: "Is the secret itself written in the line or the output, or does the line only read it from somewhere safe?",
    win: "Keys live in Colab Secrets. Outputs travel with the notebook. If a key leaks, replace it first." },
  { w: 4, kind: "bridge", bridge: true, title: "Rerun your own notebook",
    task: "Do this on your own notebook before Week 8." }
];

/* ---------- bridge ---------- */
const BRIDGE_STEPS = [
  "1. In Colab: Runtime, then Restart session and run all.",
  "2. Note the first error: the cell number, the last line of the message, and why it happened.",
  "3. Fix it and restart again. Repeat until it runs top to bottom.",
  "4. Check the outputs: do the numbers and charts match what you meant to show?",
  "5. Search the notebook and the outputs for keys, names, handles and local paths."
].join("\n");
const README_TEXT = [
  "# How to rerun this project", "",
  "1. Get the data: <where it comes from, and the file name>.",
  "2. Put it in a folder called data/ next to the notebook.",
  "3. Open the notebook in Colab. Runtime, then Restart session and run all.",
  "4. It takes about <N> minutes. It needs these packages: <list>.",
  "5. The keys it needs are named <NAME> in Colab Secrets. They are not in this repository.",
  "6. Model and date for any AI step: <model, date>."
].join("\n");
function buildBridge(def) {
  const prompt = "Here is the list of cells in my notebook (code only, no data, no keys, no real names). Tell me what would stop it from running top to bottom in a fresh runtime for someone else: names used before they are made, absolute paths, packages not installed, and anything that looks like a key. Do not guess at data you have not seen.";
  const left = [codeCard("Task 1: restart and run all", BRIDGE_STEPS, "Do this on your own notebook, in Colab."), codeCard("Task 3: write the README", README_TEXT, "Fill in the blanks for your own project.")];
  const right = [
    codeCard("Task 2: ask an AI to look for problems", prompt, "Paste this with your cells' code only (no data, no keys). Check what it says against what you found in Task 1."),
    h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: () => { solved(); setFb("good", "Done. In Week 8 a partner reruns your notebook with only the notebook and your README, then you present."); } }, "I did all three")),
    h("div", { id: "fb", class: "fb", "aria-live": "polite" })
  ];
  return { left, right };
}

BUILDERS.order = buildOrder; BUILDERS.hidden = buildHidden; BUILDERS.paths = buildPaths; BUILDERS.secrets = buildSecrets; BUILDERS.bridge = buildBridge;
boot("cactus-run-it-from-scratch-done");
