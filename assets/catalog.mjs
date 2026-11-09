/** Dependency-free catalog browser. The Python catalog JSON remains the source of truth. */
export const PAGE_SIZE = 24;
export const FACETS = {scale: 'scales', domain: 'domains', ecosystem: 'ecosystems', type: 'artifact_type', modality: 'modalities', task: 'tasks', status: 'maturity'};
const SCALE_LABELS = {'molecular':'分子・オミクス', 'cellular':'細胞', 'tissue':'組織', 'organ-system':'臓器・生体信号', 'whole-person':'個人・身体', 'behavioral':'行動・心理', 'clinical':'臨床', 'population':'集団・疫学', 'environmental':'環境', 'infrastructure':'解析基盤'};
const TYPE_LABELS = {library:'ライブラリ',tool:'ツール',workflow:'ワークフロー',standard:'標準',platform:'プラットフォーム',ecosystem:'エコシステム'};
const FIELD_LABELS = {scale:'スケール',domain:'分野',ecosystem:'実行環境',type:'種類',modality:'データ',task:'タスク',status:'状態'};
export const normalize = value => String(value ?? '').normalize('NFKC').toLocaleLowerCase('en').trim();
export function readState(search = '') {
  const params = new URLSearchParams(search);
  const state = {q:params.get('q') || '', sort:params.get('sort') === 'source' ? 'source' : 'name', page:Math.max(1, Number.parseInt(params.get('page'),10) || 1), hideArchived:params.get('hideArchived') === '1', entry:params.get('entry') || ''};
  for (const key of Object.keys(FACETS)) state[key] = params.get(key) || '';
  return state;
}
export function serializeState(state) {
  const params = new URLSearchParams();
  for (const key of ['q', ...Object.keys(FACETS), 'entry']) if (state[key]) params.set(key,state[key]);
  if (state.hideArchived) params.set('hideArchived','1');
  if (state.sort === 'source') params.set('sort','source');
  if (state.page > 1) params.set('page',String(state.page));
  return params.toString();
}
export function filterEntries(entries, state) {
  const terms = normalize(state.q).split(/\s+/u).filter(Boolean);
  const filtered = entries.filter(entry => {
    if (state.entry && entry.id !== state.entry) return false;
    if (state.hideArchived && entry.maturity === 'archived') return false;
    for (const [key, field] of Object.entries(FACETS)) {
      if (!state[key]) continue;
      const values = Array.isArray(entry[field]) ? entry[field] : [entry[field]];
      if (!values.includes(state[key])) return false;
    }
    const haystack = normalize(Object.values(entry).flat().join(' '));
    return terms.every(term => haystack.includes(term));
  });
  return state.sort === 'source' ? filtered : filtered.sort((a,b) => a.name.localeCompare(b.name,'en',{sensitivity:'base'}) || a.id.localeCompare(b.id));
}
export function facetValues(entries, field) {
  const counts = new Map();
  for (const entry of entries) for (const value of new Set([entry[field]].flat().filter(Boolean))) counts.set(value,(counts.get(value)||0)+1);
  return [...counts.entries()].sort(([a],[b]) => a.localeCompare(b,'en',{sensitivity:'base'}));
}
export function safeURL(value) {
  try { const url = new URL(value); return ['http:', 'https:'].includes(url.protocol) ? url.href : null; } catch { return null; }
}

function init() {
  const $ = id => document.getElementById(id);
  const results = $('results');
  if (!results) return;
  let entries = [];
  let state = readState(location.search);
  let searchTimer;
  const number = value => value.toLocaleString('ja-JP');
  function element(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
  }
  function link(label, href, className = '') {
    const node = element('a',className,label);
    node.href = href;
    return node;
  }
  function syncURL(mode = 'replace') {
    const query = serializeState(state);
    // Keep the current project subpath, including custom-domain GitHub Pages deployments.
    const url = location.pathname + (query ? `?${query}` : '') + (state.entry ? `#${encodeURIComponent(state.entry)}` : '');
    if (url !== location.pathname + location.search + location.hash) history[`${mode}State`](null,'',url);
  }
  function syncControls() {
    $('query').value = state.q;
    $('sort').value = state.sort;
    $('hide-archived').checked = state.hideArchived;
    for (const key of Object.keys(FACETS)) {
      $(key).value = state[key];
      if ($(key).selectedIndex < 0) { $(key).value = ''; state[key] = ''; }
    }
    if (['type','modality','task','status'].some(key => state[key]) || state.hideArchived) $('advanced-filters').open = true;
  }
  function readControls() {
    state.q = $('query').value.trim();
    state.sort = $('sort').value;
    state.hideArchived = $('hide-archived').checked;
    state.entry = '';
    state.page = 1;
    for (const key of Object.keys(FACETS)) state[key] = $(key).value;
  }
  function card(entry) {
    const node = element('article','catalog-card'); node.id = entry.id;
    const top = element('div','card-top');
    const heading = element('div');
    heading.append(element('p','card-kind',TYPE_LABELS[entry.artifact_type] || entry.artifact_type));
    const title = element('h3');
    const official = safeURL(entry.official_url), repo = safeURL(entry.repo_url);
    title.append(official ? link(entry.name,official) : document.createTextNode(entry.name));
    heading.append(title); top.append(heading);
    if (entry.maturity === 'archived') top.append(element('span','archived-badge','アーカイブ済み'));
    node.append(top,element('p','card-summary',entry.summary_ja));
    const tags = element('ul','card-tags'); tags.setAttribute('aria-label','主な分類');
    for (const tag of [...entry.scales.map(value => SCALE_LABELS[value] || value),...entry.ecosystems]) tags.append(element('li','',tag));
    node.append(tags);
    const bottom = element('div','card-bottom');
    if (official) bottom.append(link('公式サイト ↗',official));
    if (repo) bottom.append(link('リポジトリ ↗',repo));
    const permalink = link('項目リンク',`?entry=${encodeURIComponent(entry.id)}#${encodeURIComponent(entry.id)}`,'entry-link');
    permalink.setAttribute('aria-label',`${entry.name} の項目リンク`); bottom.append(permalink); node.append(bottom);
    const details = element('details','card-details'); details.append(element('summary','','分類・ライセンス・詳細'));
    const dl = element('dl');
    for (const [label,value] of [['ID',entry.id],['分野',entry.domains],['データ種別',entry.modalities],['処理タスク',entry.tasks],['実行環境',entry.ecosystems],['スケール',entry.scales],['ライセンス',entry.license || '未確認'],['状態',entry.maturity || '未確認'],['備考',entry.notes || '記載なし']]) dl.append(element('dt','',label),element('dd','',Array.isArray(value) ? value.join(' / ') : value));
    details.append(dl); node.append(details);
    return node;
  }
  function render(mode = 'replace', focusResults = false) {
    const matches = filterEntries(entries,state);
    const pages = Math.max(1,Math.ceil(matches.length / PAGE_SIZE));
    state.page = Math.min(state.page,pages);
    const start = (state.page - 1) * PAGE_SIZE;
    results.replaceChildren(...matches.slice(start,start+PAGE_SIZE).map(card));
    results.setAttribute('aria-busy','false');
    $('result-count').textContent = `${number(matches.length)} 件${matches.length ? ` / ${number(entries.length)} 件中　${number(start+1)}–${number(Math.min(start+PAGE_SIZE,matches.length))} 件を表示` : ''}`;
    const active = [];
    if (state.q) active.push(`「${state.q}」`);
    if (state.entry) active.push(`項目: ${state.entry}`);
    for (const key of Object.keys(FACETS)) if (state[key]) active.push(`${FIELD_LABELS[key]}: ${state[key]}`);
    if (state.hideArchived) active.push('アーカイブ済みを除外');
    $('active-filters').textContent = active.length ? active.join(' · ') : 'すべての項目を表示しています';
    $('empty-state').hidden = matches.length > 0;
    $('pagination').hidden = pages < 2;
    $('previous').disabled = state.page === 1;
    $('next').disabled = state.page === pages;
    $('page-label').textContent = `${state.page} / ${pages} ページ`;
    $('reset').disabled = active.length === 0 && state.sort === 'name';
    syncURL(mode);
    if (focusResults) { $('result-count').tabIndex = -1; $('result-count').focus({preventScroll:true}); $('result-count').scrollIntoView({block:'start'}); }
  }
  function reset() {
    clearTimeout(searchTimer); state = readState(); syncControls(); render('push'); $('query').focus();
  }
  async function load() {
    $('load-error').hidden = true; $('retry').disabled = true; results.setAttribute('aria-busy','true');
    $('result-count').textContent = 'カタログを読み込んでいます…';
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(),15000);
    try {
      const response = await fetch('src/human_data_lib/data/libraries.json',{signal:controller.signal});
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const data = await response.json();
      if (!Array.isArray(data.entries) || !data.entries.length || !data.entries.every(entry => typeof entry.id === 'string' && typeof entry.name === 'string' && typeof entry.summary_ja === 'string' && ['scales','domains','modalities','tasks','ecosystems'].every(field => Array.isArray(entry[field])))) throw new Error('Invalid catalog');
      entries = data.entries;
      for (const [key,field] of Object.entries(FACETS)) {
        const select = $(key); while (select.options.length > 1) select.remove(1);
        for (const [value,count] of facetValues(entries,field)) {
          const label = key === 'scale' ? `${SCALE_LABELS[value] || value} / ${value}` : key === 'type' ? `${TYPE_LABELS[value] || value} / ${value}` : value;
          const option = element('option','',`${label} (${number(count)})`); option.value = value; select.append(option);
        }
      }
      $('total-count').textContent = number(entries.length);
      $('domain-count').textContent = number(facetValues(entries,'domains').length);
      $('updated-at').textContent = data.generated_at || '不明';
      if (/^\d{4}-\d{2}-\d{2}$/.test(data.generated_at)) $('updated-at').dateTime = data.generated_at;
      $('search-controls').disabled = false; $('sort').disabled = false;
      syncControls(); render();
    } catch {
      $('load-error').hidden = false; $('result-count').textContent = '読み込みに失敗しました'; $('updated-at').textContent = '取得できませんでした'; results.setAttribute('aria-busy','false');
    } finally { clearTimeout(timeout); $('retry').disabled = false; }
  }
  $('search-form').addEventListener('submit',event => {event.preventDefault(); clearTimeout(searchTimer); readControls(); render('push');});
  $('query').addEventListener('input',() => {clearTimeout(searchTimer); searchTimer = setTimeout(() => {readControls(); render();},180);});
  for (const key of [...Object.keys(FACETS),'sort','hide-archived']) $(key).addEventListener('change',() => {clearTimeout(searchTimer); readControls(); render('push');});
  for (const button of document.querySelectorAll('[data-query]')) button.addEventListener('click',() => {clearTimeout(searchTimer); state = readState(); state.q = button.dataset.query; syncControls(); render('push');});
  $('reset').addEventListener('click',reset); $('empty-reset').addEventListener('click',reset);
  $('previous').addEventListener('click',() => {state.page--; render('push',true);});
  $('next').addEventListener('click',() => {state.page++; render('push',true);});
  $('retry').addEventListener('click',load);
  window.addEventListener('popstate',() => {clearTimeout(searchTimer); state = readState(location.search); if (entries.length) {syncControls(); render();}});
  load();
}
if (typeof document !== 'undefined') init();
