import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {readState,serializeState,filterEntries,facetValues,safeURL,PAGE_SIZE} from '../assets/catalog.mjs';
const {entries} = JSON.parse(readFileSync(new URL('../src/human_data_lib/data/libraries.json',import.meta.url)));
const state = values => ({...readState(),...values});
test('empty search preserves every catalog entry and does not mutate source order',() => {
  const original = entries.map(e => e.id);
  assert.equal(filterEntries(entries,state({})).length,entries.length);
  assert.deepEqual(entries.map(e => e.id),original);
  assert.equal(PAGE_SIZE,24);
});
test('multi-term, Japanese and full-width search find expected entries',() => {
  const matches = filterEntries(entries,state({q:'ＥＥＧ Python'}));
  assert(matches.length > 0);
  assert(matches.every(e => JSON.stringify(e).toLowerCase().includes('eeg') && e.ecosystems.includes('Python')));
  assert(filterEntries(entries,state({q:'脳波'})).length > 0);
  assert.equal(filterEntries(entries,state({q:'no-such-catalog-item-987654321'})).length,0);
});
test('facets intersect and source sorting preserves JSON order',() => {
  const matches = filterEntries(entries,state({scale:'organ-system',ecosystem:'Python',sort:'source'}));
  assert(matches.length > 0);
  assert(matches.every(e => e.scales.includes('organ-system') && e.ecosystems.includes('Python')));
  assert.deepEqual(matches,entries.filter(e => e.scales.includes('organ-system') && e.ecosystems.includes('Python')));
});
test('permalinks select exactly one entry',() => {
  assert.deepEqual(filterEntries(entries,state({entry:'biopython'})).map(e=>e.id),['biopython']);
  assert.equal(filterEntries(entries,state({entry:'missing'})).length,0);
});
test('archive filter is opt-in and state round-trips',() => {
  const fixture = [{...entries[0],maturity:'archived'},{...entries[1],maturity:'stable'}];
  assert.equal(filterEntries(fixture,state({})).length,2);
  assert.equal(filterEntries(fixture,state({hideArchived:true})).length,1);
  const original = state({q:'脳波 Python',scale:'organ-system',sort:'source',page:2,hideArchived:true});
  assert.deepEqual(readState(serializeState(original)),original);
  assert.equal(readState('?page=-4').page,1);
  assert.equal(readState('?sort=unexpected').sort,'name');
});
test('facet counts and safe outbound URLs',() => {
  assert.equal(facetValues(entries,'domains').find(([tag])=>tag === 'genomics')[1],entries.filter(e=>e.domains.includes('genomics')).length);
  assert.equal(safeURL('javascript:alert(1)'),null);
  assert.equal(safeURL('https://example.com/path'),'https://example.com/path');
  assert.equal(safeURL('//example.com'),null);
});
