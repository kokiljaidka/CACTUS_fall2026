const SVG_CACTUS = '<svg viewBox="0 0 40 40" aria-hidden="true"><rect x="7" y="14" width="6" height="12" rx="3" fill="var(--accent)"/><rect x="10" y="22" width="10" height="6" rx="3" fill="var(--accent)"/><rect x="28" y="10" width="6" height="12" rx="3" fill="var(--accent)"/><rect x="22" y="18" width="9" height="6" rx="3" fill="var(--accent)"/><rect x="15" y="5" width="12" height="30" rx="6" fill="var(--accent)"/><circle cx="18.5" cy="17" r="1.6" fill="var(--bg)"/><circle cx="23.5" cy="17" r="1.6" fill="var(--bg)"/><circle cx="21" cy="3.5" r="2.6" fill="var(--sun)"/><rect x="11" y="33" width="20" height="6" rx="2" fill="var(--sun)"/></svg>';
const SVG_DROP = '<svg viewBox="0 0 40 40" aria-hidden="true"><path d="M20 4 C20 4 9 17 9 25 a11 11 0 0 0 22 0 C31 17 20 4 20 4Z" fill="var(--water)"/><path d="M15 26 a5 5 0 0 0 4 5" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round" opacity=".7"/></svg>';
const SVG_ROCK = '<svg viewBox="0 0 40 40" aria-hidden="true"><path d="M5 32 C5 20 12 11 22 11 C31 11 36 20 35 32Z" fill="var(--muted)" opacity=".75"/></svg>';

/* ---------- content ---------- */
const WORLDS = [
  { name: "Exact instructions", blurb: "Order matters",
    idea: "A computer does exactly what you tell it, in exactly the order you tell it. It cannot guess what you meant.",
    where: "In the notebook: a cell runs top to bottom, and one wrong character changes everything." },
  { name: "Variables", blurb: "Named boxes",
    idea: "A variable is a named box. The name stays put and the value inside can change. Quotes make a value text; no quotes make it a number.",
    where: "In the notebook: API_KEY, data and table are all variables." },
  { name: "Lists and dictionaries", blurb: "Ordered and labeled",
    idea: "A list holds items in order, counted from 0. A dictionary holds labeled slots: ask for a label, get a value.",
    where: "In the notebook: a search response is a dictionary. One row of your data is a dictionary too." },
  { name: "Functions", blurb: "Machines with dials",
    idea: "A function is a machine with dials. The dials are called parameters. You set them, and the function does the work.",
    where: "In the notebook: search(q, gl, hl) is a function. q, gl and hl are its dials." },
  { name: "Repeat", blurb: "Loops",
    idea: "A loop repeats steps so you do not write them out. A for-each loop does the same thing to every item in a list.",
    where: "In the notebook: turning every search result into a table row is a loop." },
  { name: "Read the response", blurb: "Follow the path",
    idea: "An API response is dictionaries and lists nested inside one another. To reach a value, follow the path from the outside in, one key or number at a time.",
    where: "In the notebook: data[\"organic_results\"][0][\"title\"] is a path like the ones below." },
  { name: "Your project", blurb: "Break it down",
    idea: "Breaking a big question into small, checkable steps is the same skill as writing sub-questions for your project card.",
    where: "In your project: each sub-question should map to steps you can run and check." },
  { name: "Take it to Colab", blurb: "Real code",
    idea: "The puzzles are over. Now the same ideas run on real data in Colab. Keep this page open as a reference.",
    where: "You will use your project row and the search response from Step 3 of the notebook." }
];

const DATA = {
  search_parameters: { q: "artificial intelligence", gl: "sg", hl: "en" },
  organic_results: [
    { position: 1, title: "AI for beginners: a plain guide", link: "https://example.com/ai-guide" },
    { position: 2, title: "How AI is used in Singapore", link: "https://example.com/ai-sg" }
  ]
};
const PLACES = ["Singapore", "Hong Kong", "Taiwan"];
const GL = { sg: "Singapore", hk: "Hong Kong", tw: "Taiwan" };
const HL = { en: "English", "zh-tw": "Traditional Chinese", "zh-cn": "Simplified Chinese" };
const pyType = v => typeof v === "number" ? "int" : "str";

const LEVELS = [
  { w: 0, kind: "grid", title: "Water the cactus", cols: 5, rows: 3, start: [0, 2], goal: [3, 0], rocks: [], max: 14,
    allowed: ["R", "L", "U", "D"],
    task: "Drag blocks into the program so the cactus reaches the water. Each block is one step.",
    hint: "Count the squares. The water is 3 to the right and 2 up.",
    win: "The cactus did exactly what the blocks said, nothing more. That is all a program is: precise steps in order." },
  { w: 0, kind: "grid", title: "Around the rocks", cols: 5, rows: 4, start: [0, 3], goal: [4, 3], rocks: [[1, 3], [2, 3]], max: 14,
    allowed: ["R", "L", "U", "D"],
    task: "Rocks block the way, and the cactus cannot guess a detour. Plan every step, tap the square where you think it will stop, then run.",
    hint: "Go up first, then across, then back down.",
    win: "You planned the whole route before running. Predicting the result first is the habit we use all series." },

  { w: 1, kind: "slots", title: "Name the boxes", predict: true,
    task: "Fill the two boxes so the program prints: Searching in Taiwan using Chinese",
    code: [["city = ", 0], ["language = ", 1], ['print("Searching in", city, "using", language)']],
    toks: ["Taiwan", "Singapore", "Chinese", "English"],
    compute: t => `Searching in ${t[0].v} using ${t[1].v}`,
    expect: "Searching in Taiwan using Chinese",
    hint: "city goes in the first box and language in the second.",
    miss: () => "Not quite. The names city and language decide which box matters for which word in the sentence.",
    win: "Variables let you change one value in one place and the whole program follows." },
  { w: 1, kind: "slots", title: "Quotes matter", predict: true,
    task: "Make the program print 3.",
    code: [["a = ", 0], ["b = ", 1], ["print(a + b)"]],
    toks: [1, 2, "1", "2"],
    compute: t => {
      const a = t[0].v, b = t[1].v;
      if (typeof a !== typeof b) return `TypeError: unsupported operand type(s) for +: '${pyType(a)}' and '${pyType(b)}'`;
      return String(a + b);
    },
    expect: "3",
    hint: "Pieces with quotes are text. Pieces without quotes are numbers.",
    miss: o => o === "12" ? "Those are text because of the quotes. Text sticks together, so \"1\" + \"2\" makes 12. Use numbers (no quotes) to add." : o.startsWith("TypeError") ? "That error means you mixed text and a number. Read the last line: it names the two types." : "Check which pieces have quotes.",
    win: "Without quotes, 1 + 2 is 3. With quotes, \"1\" + \"2\" would be 12. Many silent data bugs come from numbers stored as text." },

  { w: 2, kind: "slots", title: "One row, as a dictionary", predict: true,
    task: "This comment came from Vietnam. It says Love the new cups. 3.2% of its words are positive. Fill the row to match, then predict what the three print lines show.",
    code: ["row = {", ['    "country": ', 0, ","], ['    "text": ', 1, ","], ['    "tone_pos": ', 2, ","], "}", 'print(row["country"])', 'print(row["text"])', 'print(row["tone_pos"])'],
    toks: ["Vietnam", "Thailand", "Love the new cups", "Too expensive now", 3.2, 32],
    compute: t => [t[0].v, t[1].v, t[2].v].join("\n"),
    expect: "Vietnam\nLove the new cups\n3.2",
    hint: "Each label (country, text, tone_pos) needs the value that describes it.",
    miss: () => "One value is in the wrong slot or does not match the comment described above.",
    win: "A row of your data is a dictionary: labels on the left, values on the right. A table is just many rows like this." },
  { w: 2, kind: "slots", title: "Counting from zero", predict: true,
    task: "Fill the boxes so the program prints Singapore, then Taiwan, one per line.",
    code: [['places = ["Singapore", "Hong Kong", "Taiwan"]'], ["print(places[", 0, "])"], ["print(places[", 1, "])"]],
    toks: [0, 1, 2, 3],
    compute: t => t.map(x => x.v < PLACES.length ? PLACES[x.v] : "IndexError: list index out of range").join("\n"),
    expect: "Singapore\nTaiwan",
    hint: "The first item is number 0, not 1.",
    miss: o => o.includes("IndexError") ? "That list has 3 items, numbered 0, 1 and 2. Number 3 is past the end." : "Remember: the first item is 0, the second is 1.",
    win: "Lists count from 0. This one fact explains a lot of \"off by one\" mistakes in AI-written code." },

  { w: 3, kind: "slots", title: "Set the dials", predict: true,
    task: "Show what people in Taiwan see when they search 人工智慧, in Traditional Chinese.",
    code: [["search(q=", 0, ", gl=", 1, ", hl=", 2, ")"]],
    toks: [{ v: "artificial intelligence", k: "q" }, { v: "人工智慧", k: "q" }, { v: "sg", k: "gl" }, { v: "hk", k: "gl" }, { v: "tw", k: "gl" }, { v: "en", k: "hl" }, { v: "zh-tw", k: "hl" }, { v: "zh-cn", k: "hl" }],
    slotKinds: ["q", "gl", "hl"],
    compute: t => {
      const names = ["q", "gl", "hl"];
      for (let i = 0; i < 3; i++) if (t[i].k !== names[i]) return `ValueError: ${names[i]} cannot be ${t[i].label}`;
      return `Google results for "${t[0].v}" as seen from ${GL[t[1].v]}, in ${HL[t[2].v]}`;
    },
    expect: 'Google results for "人工智慧" as seen from Taiwan, in Traditional Chinese',
    hint: "q is the query, gl is the country, hl is the language.",
    miss: o => o.startsWith("ValueError") ? "Each dial accepts one kind of value. q takes a search phrase, gl a country code, hl a language code." : "Compare the output with the task, one dial at a time: query, country, language.",
    win: "Changing one dial changes what comes back. Week 1's notebook compares Singapore, Hong Kong and Taiwan this way." },
  { w: 3, kind: "slots", title: "Order of the dials", predict: true,
    task: "The function is defined first, then called. Make it print: Comparing AI in Singapore",
    code: ["def compare(place, topic):", ['    print("Comparing", topic, "in", place)'], " ", ["compare(", 0, ", ", 1, ")"]],
    toks: ["Singapore", "AI", "Taiwan", "coffee"],
    compute: t => `Comparing ${t[1].v} in ${t[0].v}`,
    expect: "Comparing AI in Singapore",
    hint: "Values go to parameters by position. The first value goes to place.",
    miss: o => o === "Comparing Singapore in AI" ? "The values arrived in swapped places. The first value goes to place, the second to topic." : "Check which value is the place and which is the topic.",
    win: "Values are matched to parameters by position (or by name). Swapped arguments are a classic bug that still runs without an error." },

  { w: 4, kind: "grid", title: "Say it once", cols: 8, rows: 3, start: [0, 2], goal: [7, 2], rocks: [], max: 3,
    allowed: ["R", "U", "rep"],
    task: "The water is 7 steps away, but you only get 3 blocks. A Repeat block runs the blocks inside it again and again.",
    hint: "Put a Right block inside a Repeat block and set the count to 7.",
    win: "Two blocks instead of seven. Loops make long, repetitive work short." },
  { w: 4, kind: "grid", title: "The staircase", cols: 6, rows: 5, start: [0, 4], goal: [4, 0], rocks: [[0, 3], [1, 2], [2, 1], [3, 0]], max: 3,
    allowed: ["R", "U", "rep"],
    task: "Climb the staircase with only 3 blocks. Look for the pattern that repeats.",
    hint: "The pattern is Right, Up. Repeat it 4 times.",
    win: "You spotted a repeating pattern and wrote it once. This is how you will process thousands of posts." },
  { w: 4, kind: "slots", title: "For each comment", predict: true,
    task: "The program should print how many comments there are. Choose the line that goes inside the loop.",
    code: [['comments = ["love it", "too sweet", "love the cups"]'], ["count = 0"], ["for c in comments:"], ["    ", 0], ["print(count)"]],
    toks: [{ v: "inc", label: "count = count + 1" }, { v: "one", label: "count = 1" }, { v: "zero", label: "count = 0" }, { v: "print", label: "print(c)" }],
    compute: t => {
      let count = 0; const out = [];
      for (const c of ["love it", "too sweet", "love the cups"]) {
        const a = t[0].v;
        if (a === "inc") count += 1; else if (a === "one") count = 1; else if (a === "zero") count = 0; else out.push(c);
      }
      out.push(String(count)); return out.join("\n");
    },
    expect: "3",
    hint: "The line should build on the old value of count each time around.",
    miss: o => o.includes("love it") ? "That prints each comment, but count never changes." : "That line sets count to a fixed number every time, so earlier rounds are forgotten. It needs to use its old value.",
    win: "count = count + 1 runs once per item, so it counts the list. Counting things is the first step of many analyses." },

  { w: 5, kind: "path", title: "First title", target: "AI for beginners: a plain guide",
    task: "Build the path to the title of the first search result.",
    toks: ["search_parameters", "organic_results", "position", "title", "link", "q", "gl", "hl", 0, 1],
    hint: "Start with the list of results, pick the first item (number 0), then ask for its title.",
    win: "Path: organic_results, then 0, then title. Outside in, one step at a time." },
  { w: 5, kind: "path", title: "Second link", target: "https://example.com/ai-sg",
    task: "Build the path to the link of the second result.",
    toks: ["search_parameters", "organic_results", "position", "title", "link", "q", "gl", "hl", 0, 1],
    hint: "The second item is number 1.",
    win: "Same idea, different item. You counted from 0 correctly." },
  { w: 5, kind: "path", title: "Which country?", target: "sg",
    task: "Build the path to the country code that was searched.",
    toks: ["search_parameters", "organic_results", "position", "title", "link", "q", "gl", "hl", 0, 1],
    hint: "Country is the gl dial. It lives in the search parameters, not in the results.",
    win: "Responses also repeat back the settings you sent. That is how you check what you really asked for." },

  { w: 6, kind: "slots", title: "Put the steps in order", predict: false, runLabel: "Check order",
    task: "Your project question is: \"How do people in Singapore and Taiwan talk about AI?\" Drag the steps into an order that works.",
    code: [["Step 1  ", 0], ["Step 2  ", 1], ["Step 3  ", 2], ["Step 4  ", 3]],
    toks: ["Compare the two tables", "Put each place's results in a table", "Pick the places to compare", "Search for AI in each place"],
    ordered: ["Pick the places to compare", "Search for AI in each place", "Put each place's results in a table", "Compare the two tables"],
    hint: "You cannot compare until the data is in a table, and you cannot tabulate before searching.",
    miss: () => "Not yet. Ask of each step: what does it need that an earlier step produces?",
    win: "Each small step can be run and checked on its own. Sub-questions on your project card work the same way." },
  { w: 6, kind: "row", title: "Your project row",
    task: "Build one row of your own data as a dictionary. Add at least three fields and give each a realistic example value." ,
    win: "Copy this into your project card under \"What one row is\". In the notebook you will turn rows like this into a table." },
  { w: 7, kind: "bridge", bridge: true, title: "Three short tasks in Colab",
    task: "Open the Week 1 notebook, go to Step 3b, and do these three tasks. Each one ends with a check that tells you whether it worked." }
];

/* ---------- grid levels ---------- */
const MOVES = { R: ["Right", "→", [1, 0]], L: ["Left", "←", [-1, 0]], U: ["Up", "↑", [0, -1]], D: ["Down", "↓", [0, 1]] };
const countBlocks = arr => arr.reduce((n, it) => n + 1 + (it.body ? countBlocks(it.body) : 0), 0);
const freshItem = t => t === "rep" ? { id: uid(), t: "rep", n: 2, body: [] } : { id: uid(), t };
function flatten(arr, out = []) {
  for (const it of arr) {
    if (out.length > 300) break;
    if (it.t === "rep") for (let k = 0; k < it.n; k++) flatten(it.body, out); else out.push(it);
  }
  return out;
}
function buildGrid(def) {
  const st = L = { def, prog: [], pos: def.start.slice(), pred: null, busy: false, token: 0 };
  const board = h("div", { class: "board", style: `aspect-ratio:${def.cols}/${def.rows}` });
  const cells = h("div", { class: "cells", style: `grid-template-columns:repeat(${def.cols},1fr);grid-template-rows:repeat(${def.rows},1fr)` });
  for (let r = 0; r < def.rows; r++) for (let c = 0; c < def.cols; c++) {
    const cell = h("button", { class: "cell", type: "button", "aria-label": `Predict: column ${c + 1}, row ${r + 1}`, onclick: () => { if (!st.busy) { st.pred = [c, r]; placeSprite(predEl, st.pred); predEl.hidden = false; } } });
    if (def.rocks.some(k => k[0] === c && k[1] === r)) cell.append(svgEl("", SVG_ROCK));
    if (def.goal[0] === c && def.goal[1] === r) cell.append(svgEl("", SVG_DROP));
    cells.append(cell);
  }
  const sprite = (cls, inner) => { const e = h("div", { class: "sprite " + cls, style: `width:${100 / def.cols}%;height:${100 / def.rows}%` }); if (typeof inner === "string") e.innerHTML = inner; else e.append(inner); return e; };
  const cactus = sprite("", SVG_CACTUS);
  const predEl = sprite("pred", ""); predEl.append(h("div", { class: "qmark" }, "?")); predEl.hidden = true;
  const placeSprite = (el, p, dx = 0, dy = 0) => { el.style.transform = `translate(${(p[0] + dx) * 100}%, ${(p[1] + dy) * 100}%)`; };
  placeSprite(cactus, st.pos);
  board.append(cells, predEl, cactus);

  const progWrap = h("div"), countEl = h("p", { class: "count" });
  const renderProg = () => {
    progWrap.replaceChildren(makeZone(st.prog, "Drag blocks here"));
    const n = countBlocks(st.prog);
    countEl.textContent = def.max ? `Blocks used: ${n} of ${def.max} allowed` : `Blocks used: ${n}`;
    countEl.classList.toggle("full", !!def.max && n >= def.max);
  };
  function makeZone(arr, hint) {
    const z = h("div", { class: "zone", "data-hint": hint });
    arr.forEach(it => z.append(blockEl(it, arr)));
    makeDrop(z, (p, pt) => {
      const item = p.item || freshItem(p.fresh);
      if (def.max && countBlocks(st.prog) + countBlocks([item]) > def.max) { setFb("warn", `The limit is ${def.max} blocks for this level. Try a Repeat block.`); renderProg(); return; }
      const kids = [...z.children].filter(c => c.classList.contains("blk"));
      let idx = kids.findIndex(c => { const r = c.getBoundingClientRect(); return pt.y < r.top + r.height / 2; });
      if (idx < 0) idx = arr.length;
      arr.splice(idx, 0, item); renderProg();
    });
    return z;
  }
  function blockEl(it, arr) {
    const remove = () => { const k = arr.indexOf(it); if (k >= 0) arr.splice(k, 1); renderProg(); };
    const x = h("button", { class: "x", type: "button", "data-nodrag": true, "aria-label": "Remove block", onclick: remove }, "×");
    let el;
    if (it.t === "rep") {
      const stepper = d => h("button", { class: "step", type: "button", "data-nodrag": true, "aria-label": d > 0 ? "More times" : "Fewer times", onclick: () => { it.n = Math.max(2, Math.min(9, it.n + d)); renderProg(); } }, d > 0 ? "+" : "−");
      el = h("div", { class: "blk rep", "data-bid": it.id },
        h("div", { class: "rep-head" }, "Repeat", stepper(-1), h("b", {}, String(it.n)), stepper(1), "times", x),
        makeZone(it.body, "Drop blocks inside"));
    } else {
      const m = MOVES[it.t];
      el = h("div", { class: "blk mv", "data-bid": it.id }, h("span", { class: "arr" }, m[1]), m[0], x);
    }
    makeDraggable(el, { payload: { item: it }, pickup: () => { const k = arr.indexOf(it); if (k >= 0) arr.splice(k, 1); renderProg(); } });
    return el;
  }
  const palette = h("div", { class: "items" });
  def.allowed.forEach(t => {
    const lbl = t === "rep" ? "Repeat" : `${MOVES[t][1]} ${MOVES[t][0]}`;
    const e = h("span", { class: "blk mv" }, lbl);
    makeDraggable(e, { payload: { fresh: t }, tap: () => {
      const item = freshItem(t);
      if (def.max && countBlocks(st.prog) + 1 > def.max) { setFb("warn", `The limit is ${def.max} blocks for this level. Try a Repeat block.`); return; }
      st.prog.push(item); renderProg();
    } });
    palette.append(e);
  });
  renderProg();

  const clearHi = () => $$(".blk.running").forEach(e => e.classList.remove("running"));
  const run = async () => {
    if (st.busy) return;
    const steps = flatten(st.prog);
    if (!steps.length) { setFb("warn", "Add at least one block first."); return; }
    st.busy = true; const tk = ++st.token; st.pos = def.start.slice(); placeSprite(cactus, st.pos); setFb("info", "Running…");
    let [x, y] = def.start, problem = null;
    for (const s of steps) {
      if (L !== st || tk !== st.token) return;
      clearHi(); $$(`.blk[data-bid="${s.id}"]`).forEach(e => e.classList.add("running"));
      const d = MOVES[s.t][2], nx = x + d[0], ny = y + d[1];
      if (nx < 0 || ny < 0 || nx >= def.cols || ny >= def.rows) { problem = "the edge of the garden"; placeSprite(cactus, [x, y], d[0] * .3, d[1] * .3); await sleep(220); placeSprite(cactus, [x, y]); break; }
      if (def.rocks.some(k => k[0] === nx && k[1] === ny)) { problem = "a rock"; placeSprite(cactus, [x, y], d[0] * .3, d[1] * .3); await sleep(220); placeSprite(cactus, [x, y]); break; }
      x = nx; y = ny; placeSprite(cactus, [x, y]); await sleep(380);
    }
    if (L !== st) return;
    clearHi(); st.busy = false;
    const reached = !problem && x === def.goal[0] && y === def.goal[1];
    let predNote = "";
    if (st.pred) predNote = (st.pred[0] === x && st.pred[1] === y) ? " Your prediction matched where it stopped." : " Your prediction was a different square. Look at the first step where your plan and the cactus part ways.";
    if (reached) {
      const used = countBlocks(st.prog); solved();
      setFb("good", def.win + ` You used ${used} block${used === 1 ? "" : "s"}.` + predNote, true);
    } else if (problem) setFb("bad", `The cactus bumped into ${problem} and stopped at column ${x + 1}, row ${y + 1}.` + predNote);
    else setFb("bad", `The cactus stopped at column ${x + 1}, row ${y + 1}, not at the water. Compare your blocks with the path you wanted.` + predNote);
  };
  const reset = () => { st.token++; st.busy = false; st.prog.length = 0; st.pos = def.start.slice(); placeSprite(cactus, st.pos); clearHi(); renderProg(); const f = $("#fb"); if (f) { f.className = "fb"; f.replaceChildren(); } };
  const left = [board, h("p", { class: "tipline" }, "Tap a square to predict where the cactus will stop (optional).")];
  const right = [
    h("div", { class: "tray" }, h("p", { class: "label" }, "Blocks"), palette, h("p", { class: "tipline" }, "Drag into the program, or tap to add.")),
    h("div", { class: "prog" }, h("p", { class: "label" }, "Program"), progWrap, countEl),
    h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: run }, "Run"), h("button", { class: "btn", type: "button", onclick: reset }, "Clear"), hintBtn(def)),
    h("div", { id: "fb", class: "fb", "aria-live": "polite" })
  ];
  return { left, right };
}

/* ---------- token helpers ---------- */
function makeTokens(def) {
  return def.toks.map((x, i) => {
    const o = (x && typeof x === "object") ? x : { v: x };
    return { id: i, v: o.v, k: o.k, label: o.label || (typeof o.v === "string" ? JSON.stringify(o.v) : String(o.v)) };
  });
}
const tokChip = (tok, info, small) => makeDraggable(h("span", { class: "tok" + (small ? " small" : "") }, tok.label), info);
const normTxt = s => s.replace(/["']/g, "").replace(/\s+/g, " ").trim().toLowerCase();

/* ---------- slot levels (fill the boxes) ---------- */
function buildSlots(def) {
  const toks = makeTokens(def);
  const n = def.code.reduce((c, line) => c + (Array.isArray(line) ? line.filter(p => typeof p === "number").length : 0), 0);
  const st = L = { def, toks, vals: Array(n).fill(null), pred: "", token: 0 };
  const codeWrap = h("div"), outEl = h("div", { class: "outbox", "aria-live": "polite" }, "Output appears here after you run.");
  const renderCode = () => {
    const pre = h("pre", { class: "code" });
    def.code.forEach(line => {
      const parts = Array.isArray(line) ? line : [line];
      const d = h("div", { class: "line" });
      if (!parts.length) d.append(" ");
      parts.forEach(p => {
        if (typeof p === "string") d.append(p);
        else {
          const i = p, tid = st.vals[i];
          const slot = h("span", { class: "slot" + (tid != null ? " filled" : ""), "aria-label": `Box ${i + 1}` });
          if (tid != null) slot.append(tokChip(toks[tid], { payload: { tok: tid }, tap: () => { st.vals[i] = null; renderCode(); }, pickup: () => { st.vals[i] = null; renderCode(); } }, true));
          else slot.textContent = "drop here";
          makeDrop(slot, p2 => { st.vals[i] = p2.tok; renderCode(); });
          d.append(slot);
        }
      });
      pre.append(d);
    });
    codeWrap.replaceChildren(pre);
  };
  renderCode();
  const palette = h("div", { class: "items" });
  toks.forEach(t => palette.append(tokChip(t, { payload: { tok: t.id }, tap: () => { const k = st.vals.indexOf(null); if (k >= 0) { st.vals[k] = t.id; renderCode(); } } })));
  const pred = h("textarea", { id: "pred", rows: 2, placeholder: "Type your guess, then run…", oninput: e => { st.pred = e.target.value; } });
  const run = () => {
    if (st.vals.some(v => v == null)) { setFb("warn", "Fill every box first."); return; }
    if (def.predict && !st.pred.trim()) { setFb("warn", "Type your prediction first. A guess is fine."); pred.focus(); return; }
    const t = st.vals.map(i => toks[i]);
    let out, ok;
    if (def.ordered) { out = t.map(x => x.label).join("\n"); ok = out === def.ordered.join("\n"); }
    else { out = def.compute(t); ok = out === def.expect; }
    outEl.textContent = out; outEl.classList.toggle("err", /^[A-Za-z]*Error/.test(out));
    let note = "";
    if (def.predict) note = normTxt(st.pred) === normTxt(out) ? " Your prediction matched." : " Your prediction was different. Compare it line by line with the output.";
    if (ok) { solved(); setFb("good", def.win + note, true); }
    else setFb("bad", def.miss(out, t) + note);
  };
  const left = [h("p", { class: "label" }, "Program"), codeWrap, h("p", { class: "tipline" }, "Tap a filled box to empty it.")];
  const right = [
    h("div", { class: "tray" }, h("p", { class: "label" }, "Pieces"), palette, h("p", { class: "tipline" }, "Drag a piece into a box, or tap it to fill the next empty box.")),
    def.predict ? h("div", { class: "predict" }, h("label", { class: "label", for: "pred" }, "Before you run: what will it print?"), pred) : null,
    h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: run }, def.runLabel || "Run"), h("button", { class: "btn", type: "button", onclick: () => { st.vals.fill(null); renderCode(); outEl.textContent = "Output appears here after you run."; outEl.classList.remove("err"); } }, "Clear"), hintBtn(def)),
    h("p", { class: "label" }, def.ordered ? "Your plan" : "Output"), outEl,
    h("div", { id: "fb", class: "fb", "aria-live": "polite" })
  ];
  return { left, right };
}

/* ---------- path levels (build a path into nested data) ---------- */
function walkPath(data, keys) {
  let v = data;
  for (const k of keys) {
    if (Array.isArray(v)) {
      if (typeof k !== "number") return { err: "TypeError: list indices must be integers, not str" };
      if (k >= v.length) return { err: "IndexError: list index out of range" };
    } else if (v && typeof v === "object") {
      if (typeof k !== "string") return { err: `KeyError: ${k}` };
      if (!(k in v)) return { err: `KeyError: '${k}'` };
    } else return { err: "TypeError: you are already at a single value; it has no more keys to follow" };
    v = v[k];
  }
  return { v };
}
function buildPath(def) {
  const toks = makeTokens(def);
  const st = L = { def, toks, path: [], token: 0 };
  const outEl = h("div", { class: "outbox", "aria-live": "polite" }, "Output appears here after you run.");
  const zoneWrap = h("div");
  const renderZone = () => {
    const z = h("span", { class: "pathzone" });
    st.path.forEach((tid, i) => z.append(tokChip(toks[tid], { payload: { tok: tid }, tap: () => { st.path.splice(i, 1); renderZone(); }, pickup: () => { st.path.splice(i, 1); renderZone(); } }, true)));
    makeDrop(z, (p, pt) => {
      const kids = [...z.children];
      let idx = kids.findIndex(c => { const r = c.getBoundingClientRect(); return pt.x < r.left + r.width / 2; });
      if (idx < 0) idx = st.path.length;
      st.path.splice(idx, 0, p.tok); renderZone();
    });
    const pre = h("pre", { class: "code" }, h("div", { class: "line" }, "print(data", z, ")"));
    zoneWrap.replaceChildren(pre);
  };
  renderZone();
  const palette = h("div", { class: "items" });
  toks.forEach(t => palette.append(tokChip(t, { payload: { tok: t.id }, tap: () => { st.path.push(t.id); renderZone(); } })));
  const run = () => {
    const r = walkPath(DATA, st.path.map(i => toks[i].v));
    const out = r.err ? r.err : (typeof r.v === "string" ? r.v : JSON.stringify(r.v));
    outEl.textContent = out; outEl.classList.toggle("err", !!r.err);
    if (!r.err && r.v === def.target) { solved(); setFb("good", def.win, true); }
    else if (r.err) setFb("bad", "That path hit an error. Read the last line: it says which key or number does not exist at that point.");
    else setFb("bad", "That path leads to a different value. Compare what it printed with the task.");
  };
  const left = [h("p", { class: "label" }, "The response (data)"), h("pre", { class: "datapre" }, JSON.stringify(DATA, null, 2)), h("p", { class: "label" }, "Program"), zoneWrap];
  const right = [
    h("div", { class: "tray" }, h("p", { class: "label" }, "Keys and numbers"), palette, h("p", { class: "tipline" }, "Drag into the program in order, or tap to add to the end. Tap a placed piece to remove it.")),
    h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: run }, "Run"), h("button", { class: "btn", type: "button", onclick: () => { st.path.length = 0; renderZone(); outEl.textContent = "Output appears here after you run."; outEl.classList.remove("err"); } }, "Clear"), hintBtn(def)),
    h("p", { class: "label" }, "Output"), outEl,
    h("div", { id: "fb", class: "fb", "aria-live": "polite" })
  ];
  return { left, right };
}

/* ---------- your project row ---------- */
const FIELD_PRESETS = [["post_id", "p_1042"], ["date", "2026-11-17"], ["text", "Love the new cups"], ["country", "Vietnam"], ["language", "vi"], ["user_id", "user_0007"], ["likes", "12"]];
function buildRow(def) {
  const st = L = { def, fields: [{ k: "text", v: "Love the new cups" }, { k: "country", v: "Vietnam" }], token: 0 };
  const zone = h("div", { class: "rowzone" }), pre = h("pre", { class: "code" }), copyMsg = h("p", { class: "tipline", "aria-live": "polite" });
  const lit = v => (v.trim() !== "" && /^-?\d+(\.\d+)?$/.test(v.trim())) ? v.trim() : JSON.stringify(v);
  const codeText = () => "row = {\n" + st.fields.map(f => `    ${JSON.stringify(f.k)}: ${lit(f.v)},`).join("\n") + (st.fields.length ? "\n" : "") + "}";
  const refreshCode = () => {
    pre.textContent = codeText(); S.rowCode = codeText();
    if (st.fields.length >= 3) { if (!S.done.has(S.i)) { solved(); } setFb("good", def.win); }
    else setFb("info", `Add ${3 - st.fields.length} more field${3 - st.fields.length === 1 ? "" : "s"} to complete this level.`);
  };
  const addField = (k, v) => {
    k = k.toLowerCase().replace(/[^a-z0-9]+/g, "_").replace(/^_+|_+$/g, "");
    if (!k || st.fields.some(f => f.k === k)) return;
    st.fields.push({ k, v: v || "" }); renderFields(); refreshCode();
  };
  let fid = 0;
  const renderFields = () => {
    zone.replaceChildren();
    st.fields.forEach((f, i) => {
      const id = "fv" + (++fid);
      zone.append(h("div", { class: "field" },
        h("code", {}, f.k),
        h("input", { id, "aria-label": `Example value for ${f.k}`, value: f.v, oninput: e => { f.v = e.target.value; pre.textContent = codeText(); } }),
        h("button", { class: "x", type: "button", "aria-label": `Remove ${f.k}`, onclick: () => { st.fields.splice(i, 1); renderFields(); refreshCode(); } }, "×")));
    });
  };
  makeDrop(zone, p => addField(p.field[0], p.field[1]));
  const palette = h("div", { class: "items" });
  FIELD_PRESETS.forEach(fp => palette.append(makeDraggable(h("span", { class: "tok" }, fp[0]), { payload: { field: fp }, tap: () => addField(fp[0], fp[1]) })));
  const newName = h("input", { id: "newfield", placeholder: "your own field, e.g. platform", "aria-label": "Custom field name" });
  const add = () => { addField(newName.value, ""); newName.value = ""; };
  newName.addEventListener("keydown", e => { if (e.key === "Enter") { e.preventDefault(); add(); } });
  const copy = async () => {
    const txt = codeText();
    try { await navigator.clipboard.writeText(txt); copyMsg.textContent = "Copied. Paste it into your project card."; }
    catch (e) { const r = document.createRange(); r.selectNodeContents(pre); const s = getSelection(); s.removeAllRanges(); s.addRange(r); copyMsg.textContent = "Select and copy the code above (Ctrl+C or Cmd+C)."; }
  };
  const left = [h("p", { class: "label" }, "Your row"), zone, h("div", { class: "addfield" }, newName, h("button", { class: "btn", type: "button", onclick: add }, "Add"))];
  const right = [
    h("div", { class: "tray" }, h("p", { class: "label" }, "Common fields"), palette, h("p", { class: "tipline" }, "Drag or tap to add. Numbers stay numbers; anything else becomes text.")),
    h("p", { class: "label" }, "Python"), pre,
    h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: copy }, "Copy code")), copyMsg,
    h("div", { id: "fb", class: "fb", "aria-live": "polite" })
  ];
  renderFields();
  queueMicrotask(refreshCode);
  return { left, right };
}


/* ---------- Colab bridge ---------- */
const DEFAULT_ROW = 'row = {\n    "text": "Love the new cups",\n    "country": "Vietnam",\n    "likes": 12,\n}';
function buildBridge(def) {
  const usingOwn = !!S.rowCode;
  const t1 = (S.rowCode || DEFAULT_ROW) + '\nprint(list(row.keys()))\nprint(row[list(row.keys())[0]])\nassert len(row) >= 3, "Add at least three fields"';
  const t2 = '# Run Step 3 first, so that data and table exist.\nfirst_title = data["organic_results"][0]["title"]\nprint(first_title)\nassert first_title == table.loc[0, "title"], "Not the same as the table: check your path"';
  const prompt = 'I have a Python dictionary called data from a SerpAPI Google search. Write one line of Python that gets the link of the second organic result. Explain each [ ] in plain English.';
  const t3 = 'second_link = ...   # paste the AI\'s line here, replacing the dots\nprint(second_link)\nassert second_link == table.loc[1, "link"], "Not the same as the table: check the path"';
  const left = [
    codeCard("Task 1: your project row", t1, usingOwn ? "This is the row you built in level 16. Paste it into the Task 1 cell and run it." : "You have not built your row yet, so this is an example. Go back to level 16 to build yours, then return here."),
    codeCard("Task 2: read the response", t2, "Predict what it will print, then run it. The path is the one you practiced in world 6.")
  ];
  const right = [
    codeCard("Task 3: ask an AI, then check it", prompt, "First write down your own path to the second result's link. Then paste this prompt into your AI assistant."),
    codeCard("Task 3 check", t3, "Paste the AI's line, run it, and compare with your own guess."),
    h("div", { class: "tray" }, h("p", { class: "label" }, "Log it"), h("p", {}, "In the notebook's verification log (row 3b), write your prediction, what the AI wrote, and the check you ran.")),
    h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: () => { solved(); setFb("good", "Done. In Step 4 you will change the search itself and see the response change."); } }, "I ran all three")),
    h("div", { id: "fb", class: "fb", "aria-live": "polite" })
  ];
  return { left, right };
}

BUILDERS.grid = buildGrid; BUILDERS.slots = buildSlots; BUILDERS.path = buildPath; BUILDERS.row = buildRow; BUILDERS.bridge = buildBridge;
boot("cactus-garden-done");
