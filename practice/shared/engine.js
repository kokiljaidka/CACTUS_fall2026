"use strict";
/* ---------- helpers ---------- */
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const sleep = ms => new Promise(r => setTimeout(r, ms));
let _id = 0; const uid = () => "b" + (++_id);
function h(tag, attrs = {}, ...kids) {
  const e = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === "class") e.className = v;
    else if (k.startsWith("on")) e.addEventListener(k.slice(2), v);
    else if (v === true) e.setAttribute(k, "");
    else if (v !== false && v != null) e.setAttribute(k, v);
  }
  for (const kid of kids.flat()) { if (kid == null || kid === false) continue; e.append(kid.nodeType ? kid : document.createTextNode(kid)); }
  return e;
}
const svgEl = (cls, html) => { const s = h("span", { class: cls }); s.innerHTML = html; return s; };
/* ---------- drag engine (pointer events: mouse, touch and pen) ---------- */
const dragReg = new WeakMap(), dropReg = new WeakMap();
let drag = null;
function makeDraggable(el, info) {
  el.setAttribute("data-dragitem", ""); el.setAttribute("role", "button"); el.tabIndex = 0;
  dragReg.set(el, info);
  el.addEventListener("keydown", e => { if ((e.key === "Enter" || e.key === " ") && !e.target.closest("[data-nodrag]")) { e.preventDefault(); info.tap && info.tap(); } });
  return el;
}
const makeDrop = (el, drop) => { dropReg.set(el, { drop }); return el; };
const dropTargetAt = (x, y) => { let el = document.elementFromPoint(x, y); while (el) { if (dropReg.has(el)) return el; el = el.parentElement; } return null; };
let lastOver = null;
function setOver(t) { if (lastOver === t) return; if (lastOver) lastOver.classList.remove("over"); lastOver = t; if (t) t.classList.add("over"); }
document.addEventListener("pointerdown", e => {
  if (e.button > 0 || e.target.closest("[data-nodrag]")) return;
  const el = e.target.closest("[data-dragitem]"); if (!el) return;
  const info = dragReg.get(el); if (!info) return;
  drag = { el, info, x0: e.clientX, y0: e.clientY, active: false, ghost: null };
});
window.addEventListener("pointermove", e => {
  if (!drag) return;
  if (!drag.active) {
    if (Math.hypot(e.clientX - drag.x0, e.clientY - drag.y0) < 6) return;
    drag.active = true;
    const r = drag.el.getBoundingClientRect();
    drag.ox = drag.x0 - r.left; drag.oy = drag.y0 - r.top;
    const g = drag.el.cloneNode(true); g.removeAttribute("data-dragitem"); g.classList.add("ghost"); g.style.width = r.width + "px";
    document.body.append(g); drag.ghost = g; document.body.classList.add("dragging");
    if (drag.info.pickup) drag.info.pickup();
  }
  drag.ghost.style.transform = `translate(${e.clientX - drag.ox}px, ${e.clientY - drag.oy}px)`;
  setOver(dropTargetAt(e.clientX, e.clientY));
  e.preventDefault();
}, { passive: false });
function endDrag(e, cancelled) {
  if (!drag) return;
  const d = drag; drag = null; setOver(null); document.body.classList.remove("dragging");
  if (d.ghost) d.ghost.remove();
  if (!d.active) { if (!cancelled && d.info.tap) d.info.tap(); return; }
  const t = cancelled ? null : dropTargetAt(e.clientX, e.clientY);
  if (t) dropReg.get(t).drop(d.info.payload, { x: e.clientX, y: e.clientY });
  else if (d.info.discard) d.info.discard();
}
window.addEventListener("pointerup", e => endDrag(e, false));
window.addEventListener("pointercancel", e => endDrag(e, true));


/* ---------- level framework (pages define WORLDS, LEVELS, BUILDERS, then call boot) ---------- */
const S = { i: 0, done: new Set(), rowCode: null };
let L = null;
const BUILDERS = {};
let STORE_KEY = "cactus-practice";
const save = () => { try { localStorage.setItem(STORE_KEY, JSON.stringify([...S.done])); } catch (e) {} };
const puzzleCount = () => LEVELS.filter(l => !l.bridge).length;

function renderMap() {
  const m = $("#map"); m.replaceChildren();
  WORLDS.forEach((w, wi) => {
    const ol = h("ol");
    LEVELS.forEach((lv, i) => { if (lv.w === wi) ol.append(h("li", {}, h("button", { class: "dot", "data-i": i, "aria-label": `Level ${i + 1}: ${lv.title}`, title: lv.title, onclick: () => go(i) }, String(i + 1)))); });
    m.append(h("div", { class: "world" }, h("h3", {}, w.name), h("small", {}, w.blurb), ol));
  });
  updateMap();
}
function updateMap() {
  $$(".dot").forEach(b => { const i = +b.dataset.i; b.classList.toggle("done", S.done.has(i)); b.classList.toggle("cur", i === S.i); });
  $("#count").textContent = String([...S.done].filter(i => LEVELS[i] && !LEVELS[i].bridge).length);
  $("#total").textContent = String(puzzleCount());
}
function go(i) {
  if (L) L.token = (L.token || 0) + 1;
  S.i = Math.max(0, Math.min(LEVELS.length - 1, i));
  try { history.replaceState(null, "", "#l-" + (S.i + 1)); } catch (e) {}
  renderLevel(); updateMap();
}
function setFb(type, msg, next) {
  const box = $("#fb"); if (!box) return;
  box.className = "fb " + type; box.replaceChildren(h("p", {}, msg));
  if (next && S.i < LEVELS.length - 1) box.append(h("button", { class: "btn primary", type: "button", onclick: () => go(S.i + 1) }, "Next level"));
}
function solved() { S.done.add(S.i); save(); updateMap(); }
function renderLevel() {
  const def = LEVELS[S.i], wd = WORLDS[def.w];
  const { left, right } = BUILDERS[def.kind](def);
  const nav = h("div", { class: "lvlnav" },
    h("button", { class: "btn", type: "button", disabled: S.i === 0, onclick: () => go(S.i - 1) }, "Previous"),
    h("button", { class: "btn", type: "button", disabled: S.i === LEVELS.length - 1, onclick: () => go(S.i + 1) }, "Next"));
  $("#stage").replaceChildren(h("section", { class: "lvl" },
    h("p", { class: "eyebrow" }, `World ${def.w + 1} · ${wd.name} · Level ${S.i + 1}`),
    h("h2", {}, def.title),
    h("div", { class: "idea" }, h("p", {}, h("b", {}, "The idea. "), wd.idea), h("p", { class: "where" }, wd.where)),
    h("p", { class: "task" }, def.task),
    h("div", { class: "play" }, h("div", { class: "col" }, left), h("div", { class: "col" }, right)),
    nav));
}
const hintBtn = def => h("button", { class: "btn", type: "button", onclick: () => setFb("info", "Hint: " + def.hint) }, "Hint");

/* A block of code with a Copy button. Used by the Colab bridge screens. */
function codeCard(title, text, note) {
  const msg = h("span", { class: "tipline", "aria-live": "polite" });
  const pre = h("pre", { class: "code tight" }, text);
  const copy = async () => {
    try { await navigator.clipboard.writeText(text); msg.textContent = "Copied."; }
    catch (e) { const r = document.createRange(); r.selectNodeContents(pre); const s = getSelection(); s.removeAllRanges(); s.addRange(r); msg.textContent = "Selected. Press Ctrl+C or Cmd+C to copy."; }
  };
  return h("div", { class: "col" }, h("p", { class: "label" }, title), note ? h("p", {}, note) : null, pre,
    h("div", { class: "row" }, h("button", { class: "btn", type: "button", onclick: copy }, "Copy code"), msg));
}

function boot(storeKey) {
  STORE_KEY = storeKey;
  try { JSON.parse(localStorage.getItem(STORE_KEY) || "[]").forEach(n => S.done.add(n)); } catch (e) {}
  $("#resetProg").addEventListener("click", () => { S.done.clear(); save(); updateMap(); });
  renderMap();
  const m = /^#l-(\d+)$/.exec(location.hash || "");
  go(m ? +m[1] - 1 : 0);
  window.addEventListener("hashchange", () => { const m2 = /^#l-(\d+)$/.exec(location.hash || ""); if (m2 && +m2[1] - 1 !== S.i) go(+m2[1] - 1); });
}
