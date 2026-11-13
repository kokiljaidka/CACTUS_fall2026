/* Week 5: What Counts as a Word? Uses the shared engine (practice/shared/engine.js). All texts are invented. */

const TOKENS = /*__TOKENS_JSON__*/[];

const WORLDS = [
  { name: "What is a token?", blurb: "Tokenizing",
    idea: "A token is the unit you count. The computer needs a rule for where one token ends and the next begins, and the rule changes your numbers. English has spaces. Chinese does not.",
    where: "In the notebook: the warm-up tokenizes five texts two ways, and Exercise 1 counts words." },
  { name: "Counting", blurb: "Counts and settings",
    idea: "Raw counts are dominated by little words. Each cleaning step (lowercasing, removing stopwords, dropping short words) changes the list, and some steps delete things you wanted.",
    where: "In the notebook: Exercise 1 compares raw and cleaned counts, and says what you do not trust." },
  { name: "Dictionaries", blurb: "Sentiment",
    idea: "A sentiment dictionary adds up word scores. It cannot tell a name from a word, sarcasm from praise, or slang from its dictionary meaning.",
    where: "In the notebook: Exercise 2 reads ten texts by hand and compares them with the score." },
  { name: "Read before you name", blurb: "Clusters",
    idea: "A cluster or topic is a list of top words. Before you give it a name, read the examples inside it. Sometimes the cluster is not about content at all.",
    where: "In the notebook: Exercise 4 clusters the Reddit posts, and you read three examples from each cluster before naming it." },
  { name: "Take it to Colab", blurb: "Real code",
    idea: "You have seen what a tokenizer does. Now run two of them on five texts.",
    where: "The Week 5 notebook warm-up has the same five texts." }
];

const choose = (opts, onpick) => {
  const wrap = h("div", { class: "choice", role: "group" }); let cur = null; const btns = [];
  opts.forEach(o => {
    const b = h("button", { class: "pill", type: "button", onclick: () => { cur = o.v; btns.forEach(x => x.classList.toggle("on", x === b)); onpick && onpick(cur); } }, o.t);
    btns.push(b); wrap.append(b);
  });
  wrap.get = () => cur; return wrap;
};
const chips = arr => h("div", { class: "chips" }, arr.map(t => h("span", { class: "chip" }, t)));

/* ---------- level 1: tokenizers ---------- */
const TOK_OPTS = [{ v: "spaces", t: "Split on spaces" }, { v: "words", t: "Regex words" }, { v: "chars", t: "Characters" }, { v: "jieba", t: "jieba (a segmenter)" }];
const TOK_OK = { t1: ["spaces", "words"], t2: ["spaces", "words"], t3: ["jieba"], t4: ["jieba"], t5: ["spaces", "jieba"] };
const TOK_WHY = {
  t1: "Splitting on spaces keeps \"isn't\" whole but leaves punctuation stuck to words (\"teachers,\"). The regex splits \"isn't\" into \"isn\" and \"t\". Neither is perfect, so choose by what you need to count. Characters are never the answer for English.",
  t2: "Hyphens, \"#AI\" and \"$5/month\" are all judgement calls. The regex gives clean lowercase words but loses the hashtag. Spaces keep the odd shapes (\"York-based\"). A segmenter is built for Chinese, not for this.",
  t3: "Chinese has no spaces between words, so splitting on spaces gives one giant token, and the regex does the same, because Chinese characters count as word characters. A segmenter like jieba looks up where words end.",
  t4: "Same problem: one giant token without a segmenter, or sixteen single characters (which are not words). jieba finds 大學生, 使用, 人工智慧.",
  t5: "A mix. Splitting on spaces works here only because someone typed spaces. jieba splits 寫功課 as 寫功 + 課, which is wrong. Even a segmenter makes mistakes, especially on Traditional Chinese. None of these is perfect."
};
function buildTok(def) {
  L = { def, token: 0 };
  const picks = {}, cards = {};
  const render = d => {
    const p = picks[d.id].get(), box = cards[d.id].querySelector(".out");
    box.replaceChildren();
    if (p) box.append(chips(d.tokens[p]), h("p", { class: "ncount" }, d.tokens[p].length + " token" + (d.tokens[p].length === 1 ? "" : "s")));
  };
  const left = TOKENS.map((d, i) => {
    picks[d.id] = choose(TOK_OPTS, () => render(d));
    cards[d.id] = h("div", { class: "tcard", id: "tk-" + d.id }, h("p", { class: "label" }, "Text " + (i + 1)), h("p", { class: "src" }, d.text), picks[d.id], h("div", { class: "out" }));
    return cards[d.id];
  });
  const check = () => {
    if (TOKENS.some(d => !picks[d.id].get())) { setFb("warn", "Pick a tokenizer for every text."); return; }
    let all = true, n = 0;
    TOKENS.forEach(d => {
      const ok = TOK_OK[d.id].includes(picks[d.id].get()); all = all && ok; if (!ok) n++;
      cards[d.id].className = "tcard " + (ok ? "right" : "wrong");
      cards[d.id].querySelector(".why")?.remove();
      cards[d.id].append(h("p", { class: "why" }, (ok ? "Fine. " : "Look at the tokens again. ") + TOK_WHY[d.id]));
    });
    if (all) { solved(); setFb("good", def.win, true); } else setFb("bad", `${n} text${n === 1 ? "" : "s"} to rethink. Read the notes under each one.`);
  };
  const right = [h("div", { class: "givens" }, "Pick the tokenizer that gives you the most usable words for each text. Look at the tokens and the count it gives."),
    h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: check }, "Check my choices"), hintBtn(def)),
    h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  return { left, right };
}

/* ---------- level 2: counting ---------- */
const HEADS = [
  "AI tools in schools: what parents need to know",
  "The government plans new rules for AI in the workplace",
  "How AI is changing the way students write essays",
  "AI in the classroom: teachers say the tools are here to stay",
  "Workers in the US fear AI will take their jobs",
  "Why AI matters for all of us",
  "New AI course opens for working adults",
  "Teachers and students learn to use AI tools together",
  "Ministry says AI rules for schools are coming",
  "Companies in the US and Singapore hire for AI skills",
  "Parents ask: is AI homework help cheating?",
  "AI and the future of work in the city"
];
const STOP = new Set("a an the of in on at to for and or but is are was were be been it its this that these those with by as from how why what who will can do does not no all us we our you your they their".split(" "));
function countWords(opts) {
  const m = new Map();
  HEADS.forEach(t => {
    (t.match(/[A-Za-z']+/g) || []).forEach(w0 => {
      const w = opts.lower ? w0.toLowerCase() : w0;
      if (opts.stop && STOP.has(w.toLowerCase()) && (opts.lower || STOP.has(w))) return;
      if (opts.short && w.length < 3) return;
      m.set(w, (m.get(w) || 0) + 1);
    });
  });
  return [...m.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));
}
function buildCount(def) {
  L = { def, token: 0 };
  const o = { lower: false, stop: false, short: false };
  const tbl = h("div"), why = h("p", { class: "tipline" });
  const isFn = w => STOP.has(w.toLowerCase());
  const render = () => {
    const top = countWords(o).slice(0, 8);
    tbl.replaceChildren(h("table", { class: "top" }, h("tr", {}, h("th", {}, "Top 8 words"), h("th", {}, "Count")),
      top.map(([w, n]) => h("tr", { class: w.toLowerCase() === "ai" ? "hit" : isFn(w) ? "fn" : "" }, h("td", {}, w), h("td", { class: "n" }, String(n))))));
    const notes = [];
    if (o.short) notes.push("Dropping words under 3 letters deleted \"AI\" (2 letters).");
    if (o.lower && o.stop) notes.push("Lowercasing turned the country \"US\" into \"us\", and \"us\" is on the stopword list, so the country vanished from the counts.");
    if (o.stop && !o.lower) notes.push("The stopword list is lowercase, so \"The\" at the start of a headline was not removed.");
    why.textContent = notes.join(" ");
  };
  const tog = (key, name, sub) => h("label", { class: "tog" }, h("input", { type: "checkbox", onchange: e => { o[key] = e.target.checked; render(); } }), h("span", {}, name, h("small", {}, sub)));
  const check = () => {
    const top5 = countWords(o).slice(0, 5).map(x => x[0]);
    const hasAI = top5.some(w => w.toLowerCase() === "ai"), fn = top5.filter(isFn);
    if (!hasAI) setFb("bad", "\"AI\" is not in your top 5. Some setting deleted it. Which one?");
    else if (fn.length) setFb("bad", `Your top 5 still has little words: ${fn.join(", ")}. What would remove them? And do they need lowercasing first?`);
    else { solved(); setFb("good", def.win, true); }
  };
  const left = [h("div", { class: "givens" }, "Twelve invented headlines about AI. The table shows the 8 most common words."),
    h("div", { class: "togs" }, [tog("lower", "Lowercase everything", "\"The\" and \"the\" become one word"), tog("stop", "Remove stopwords", "Drop little words (the, of, in, us ...)"), tog("short", "Drop words under 3 letters", "Short words are rarely content")]),
    h("p", { class: "label" }, "The headlines"), h("ul", { class: "heads" }, HEADS.map(t => h("li", {}, t)))];
  const right = [tbl, why, h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: check }, "Check my top 5"), hintBtn(def)), h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  render();
  return { left, right };
}

/* ---------- level 3: a sentiment dictionary ---------- */
const LEX = { great: 3, good: 2, bad: -2, joy: 3, sick: -2 };
const SENT = [
  { t: "This tool is great", want: 1, why: "Works when \"great\" is in the dictionary." },
  { t: "This is not good", want: -1, why: "Needs \"good\" in the dictionary and the negation rule switched on." },
  { t: "Oh great, it deleted my file again", want: -1, why: "Sarcasm. The dictionary sees \"great\" and says positive. No word list can hear the tone." },
  { t: "Joy asked about the results", want: 0, why: "\"Joy\" is a name here. Neutral needs \"joy\" out of the dictionary." },
  { t: "I felt pure joy when it worked", want: 1, why: "Positive needs \"joy\" in the dictionary. D and E pull in opposite directions: the dictionary cannot tell a name from a word." },
  { t: "That demo was sick!", want: 1, why: "Slang. In the dictionary \"sick\" is negative, so this scores negative or neutral, never positive." },
  { t: "I feel sick today", want: -1, why: "Works when \"sick\" is in the dictionary, but now the slang text above is even more wrong." },
  { t: "The service was bad", want: -1, why: "Works when \"bad\" is in the dictionary." }
];
function scoreText(text, on, neg) {
  const ws = text.toLowerCase().match(/[a-z']+/g) || []; let s = 0, flip = false;
  ws.forEach(w => { if (neg && (w === "not" || w === "never")) { flip = true; return; } if (on[w] && LEX[w]) { s += flip ? -LEX[w] : LEX[w]; flip = false; } else if (LEX[w] !== undefined) flip = false; });
  return s;
}
const sign = s => (s > 0 ? 1 : s < 0 ? -1 : 0);
const SLABEL = { "1": "positive", "-1": "negative", "0": "neutral" };
function bestPossible() {
  const ks = Object.keys(LEX); let best = 0;
  for (let m = 0; m < (1 << ks.length); m++) for (const neg of [false, true]) {
    const on = {}; ks.forEach((k, i) => { on[k] = !!(m & (1 << i)); });
    const n = SENT.filter(x => sign(scoreText(x.t, on, neg)) === x.want).length; if (n > best) best = n;
  }
  return best;
}
function buildLex(def) {
  L = { def, token: 0 };
  const on = { great: true, good: true, bad: true, joy: true, sick: true }, st = { neg: false };
  const best = bestPossible(), out = h("div", { class: "togs" }), sum = h("p", { class: "label" });
  const render = () => {
    let n = 0;
    out.replaceChildren(...SENT.map(x => {
      const s = scoreText(x.t, on, st.neg), ok = sign(s) === x.want; if (ok) n++;
      return h("div", { class: "sc " + (ok ? "right" : "wrong") }, h("span", { class: "t" }, x.t), h("span", { class: "r" }, `score ${s} · ${SLABEL[sign(s)]} · should be ${SLABEL[x.want]}`));
    }));
    sum.textContent = `Right: ${n} of ${SENT.length}`; render.n = n;
  };
  const wtog = w => h("label", { class: "tog" }, h("input", { type: "checkbox", checked: true, onchange: e => { on[w] = e.target.checked; render(); } }), h("span", {}, `${w} (${LEX[w] > 0 ? "+" : ""}${LEX[w]})`));
  const ntog = h("label", { class: "tog" }, h("input", { type: "checkbox", onchange: e => { st.neg = e.target.checked; render(); } }), h("span", {}, "Negation rule", h("small", {}, "After \"not\", flip the next word's score")));
  const check = () => {
    if (render.n >= best) { solved(); setFb("good", def.win + " The best any setting of this dictionary can do is " + best + " of " + SENT.length + ". The rest need a human, or a different method.", true); }
    else setFb("bad", `You have ${render.n} right and a better setting exists. Try the negation rule, and each word in turn.`);
  };
  const left = [h("div", { class: "givens" }, "Eight texts, with the label a person would give. Switch words in and out of the dictionary and the negation rule on and off. Get as many right as you can."),
    h("p", { class: "label" }, "The dictionary"), h("div", { class: "togs" }, [...Object.keys(LEX).map(wtog), ntog])];
  const right = [sum, out, h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: check }, "Check my best"), hintBtn(def)), h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  render();
  return { left, right };
}

/* ---------- level 4: read before you name ---------- */
const CLU = [
  { words: "school, students, teachers, exams, homework", ex: ["Teachers say students use AI to finish homework", "Exams change as schools rethink essays", "Parents worry about students and AI tutors", "School leaders set rules for classroom AI", "A teacher's guide to AI and exams"], a: "name", why: "Every example is about AI in education. The top words describe the examples, so you can name it, for example \"AI in education\"." },
  { words: "AI, new, says, report, week", ex: ["A bank says AI use is up, in a new report", "New AI film opens this week", "Football club says new AI scouting tool is ready", "Report on a city's new AI bus routes", "Minister says new AI laws are coming this week"], a: "mixed", why: "The top words are general news words. The examples are about banking, film, football, buses and law. There is no single topic to name." },
  { words: "subscribe, newsletter, sign, free, read", ex: ["Sign up for our free newsletter", "Subscribe to read the full story", "Sign in to read more for free", "Get our newsletter: subscribe today", "Read free for 30 days: sign up"], a: "boiler", why: "This is page boilerplate, not content people wrote about the topic. Remove these texts before you count or cluster, and say you did." }
];
const CLU_OPTS = [{ v: "name", t: "Coherent: name it" }, { v: "mixed", t: "Too mixed to name" }, { v: "boiler", t: "Not content (boilerplate)" }];
function buildClu(def) {
  L = { def, token: 0 };
  const picks = CLU.map(() => choose(CLU_OPTS));
  const cards = CLU.map((c, i) => h("div", { class: "clu", id: "cl" + i }, h("p", { class: "label" }, "Cluster " + (i + 1)), h("p", { class: "words" }, "Top words: " + c.words), h("ul", { class: "heads" }, c.ex.map(t => h("li", {}, t))), picks[i]));
  const check = () => {
    if (picks.some(p => !p.get())) { setFb("warn", "Decide for every cluster."); return; }
    let all = true; const out = [];
    CLU.forEach((c, i) => { const ok = picks[i].get() === c.a; all = all && ok; cards[i].className = "clu " + (ok ? "right" : "wrong"); cards[i].querySelector(".why")?.remove(); cards[i].append(h("p", { class: "why" }, (ok ? "Right. " : "Not quite. ") + c.why)); });
    if (all) { solved(); setFb("good", def.win, true); } else setFb("bad", "Read the notes under each cluster. The examples are the evidence, not the top words.");
  };
  const left = [h("div", { class: "givens" }, "A clustering method grouped invented headlines and printed each cluster's top words. Below each is a sample of its texts. Read them, then decide."), ...cards];
  const right = [h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: check }, "Check my answers"), hintBtn(def)), h("div", { id: "fb", class: "fb", "aria-live": "polite" })];
  return { left, right };
}

const LEVELS = [
  { w: 0, kind: "tok", title: "Pick a tokenizer",
    task: "Five invented texts, four ways to cut them into tokens. For each text, pick the tokenizer that gives usable words. Look at the tokens and the count before you decide.",
    hint: "Ask: would a person call these things words? Does the count match what a reader would count? Chinese is written without spaces.",
    win: "You matched the tokenizer to the language. A segmenter is needed for Chinese, and no tokenizer is perfect on mixed or messy text." },
  { w: 1, kind: "count", title: "Same headlines, different counts",
    task: "Switch the cleaning steps on and off until the top 5 words include AI and no little words. Read the note under the table each time something changes.",
    hint: "Little words are removed by the stopword step, but it only works on lowercase. One of the three steps deletes AI.",
    win: "Cleaning steps are choices. The list you want needed lowercasing and stopword removal, and not the short-word filter. And one of them quietly deleted the country \"US\"." },
  { w: 2, kind: "lex", title: "Fix the dictionary",
    task: "A sentiment dictionary scores eight texts. Edit the dictionary and the negation rule to get as many right as you can.",
    hint: "Some texts need a word in. Some need it out. Some cannot be fixed. When two texts need opposite settings, that is the finding.",
    win: "You found the limit. A dictionary adds up word scores, so it cannot tell a name from a word, hear sarcasm, or know slang." },
  { w: 3, kind: "clu", title: "Read before you name",
    task: "Three clusters came out of a clustering run. Read the examples under each one. Decide whether to name it, call it too mixed, or say it is not content.",
    hint: "The top words are a summary. The examples are the evidence. Do all five examples fit one clear label?",
    win: "You read first. One cluster could be named, one was a bag of unrelated news, and one was page boilerplate that should never have been in the data." },
  { w: 4, kind: "bridge", bridge: true, title: "Tokenize five texts two ways",
    task: "Open the Week 5 notebook, find the warm-up cell, and run this there." }
];

/* ---------- bridge ---------- */
const BRIDGE_CODE = [
  "import re", "",
  "texts = [",
  '    "AI isn\'t replacing teachers, it\'s changing homework.",',
  '    "New York-based startup launches #AI tutor for $5/month",',
  '    "新加坡推出人工智能學習計劃",',
  '    "香港大學生如何使用生成式人工智慧",',
  '    "Singapore 學生 use ChatGPT 寫功課",',
  "]", "",
  "def by_spaces(t):", "    return t.split()", "",
  "def by_words(t):", '    return re.findall(r"\\w+", t.lower())', "",
  "# Predict first: how many tokens will each method give for each text?",
  "for t in texts:", "    print(len(by_spaces(t)), len(by_words(t)), t)"
].join("\n");
function buildBridge(def) {
  const prompt = "Write Python that tokenizes these five texts two ways: by splitting on spaces, and with the jieba library. Print the number of tokens each way. Then explain in two sentences what goes wrong when you split Chinese text on spaces. Do not include any API key.";
  const left = [codeCard("Task 1: two tokenizers", BRIDGE_CODE, "Predict the numbers before you run it. Paste it into the warm-up cell of the Week 5 notebook.")];
  const right = [
    codeCard("Task 2: ask an AI, then compare", prompt, "Paste this into your AI assistant. Does its code match what you ran? Did it use jieba correctly?"),
    h("div", { class: "tray" }, h("p", { class: "label" }, "Task 3: check"), h("p", {}, "For the two Chinese texts, how many tokens did splitting on spaces give? What did you expect? Log one thing that surprised you.")),
    h("div", { class: "row" }, h("button", { class: "btn primary", type: "button", onclick: () => { solved(); setFb("good", "Done. In Exercise 1 you will count words across a whole corpus, and decide which tokenizer to trust."); } }, "I ran all three")),
    h("div", { id: "fb", class: "fb", "aria-live": "polite" })
  ];
  return { left, right };
}

BUILDERS.tok = buildTok; BUILDERS.count = buildCount; BUILDERS.lex = buildLex; BUILDERS.clu = buildClu; BUILDERS.bridge = buildBridge;
boot("cactus-what-counts-as-a-word-done");
