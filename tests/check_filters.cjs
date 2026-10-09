// Dependency-free interaction logic test. Run: node tests/check_filters.cjs
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const html = fs.readFileSync(path.join(__dirname, '..', 'index.html'), 'utf8');
const source = html.match(/<script>([\s\S]*?)<\/script>/)[1];
const papers = [...html.matchAll(/class="publication" data-topic="([^"]+)"/g)].map(([,topic]) => ({dataset: {topic}, hidden:false}));
const buttons = [...html.matchAll(/data-filter="([^"]+)"/g)].map(([,filter])=>({dataset:{filter},attrs:{},setAttribute(k,v){this.attrs[k]=v},addEventListener(_,callback){this.click=callback}}));
const controls = {hidden:true}, status = {};
const document = {
  querySelector: selector => selector === '.publication-tools' ? controls : status,
  querySelectorAll: selector => selector === '[data-filter]' ? buttons : papers
};
vm.runInNewContext(source, {document});
assert.equal(controls.hidden,false);
assert.equal(papers.filter(p=>!p.hidden).length,papers.length);
for (const topic of ['reasoning','multi-agent','other','all','all','reasoning','all']) {
  const button = buttons.find(b=>b.dataset.filter===topic);
  button.click();
  const expected = papers.filter(p=>topic==='all' || p.dataset.topic===topic).length;
  assert.equal(papers.filter(p=>!p.hidden).length,expected);
  assert.equal(status.textContent,`${expected} ${expected===1?'publication':'publications'}`);
  assert.equal(buttons.filter(b=>b.attrs['aria-pressed']==='true').length,1);
  assert.equal(button.attrs['aria-pressed'],'true');
}
console.log(`PASS: ${papers.length} publications; all topic filters, repeated clicks, restoring all, live count, and pressed state.`);
