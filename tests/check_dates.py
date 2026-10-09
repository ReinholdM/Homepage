"""Regression checks for date clarity. Run: python3 tests/check_dates.py"""
from pathlib import Path
from html import unescape
import re
s=(Path(__file__).resolve().parents[1]/'index.html').read_text()
assert 'To appear' not in s and 'One paper about' not in s
assert 'I have served as a reviewer' in s
assert '<span>Education</span>PhD' in s
assert 'News archive' in s and 'Talks &amp; notes archive' in s and 'CV archive' in s
assert 'Archived English CV' in s and '中文简历（历史版本）' in s
assert '2021-03-05' in s and '2020-02-24' in s and '2020-03-01' in s
assert 'not confirmed as a current mailing address' in s
papers=re.findall(r'<li class="publication"[^>]*>(.*?)</li>',s,re.S)
years=[]
for paper in papers:
    venue=re.search(r'<p class="venue">(.*?)</p>',paper,re.S).group(1)
    years.append(int(re.search(r'20\d{2}',venue).group()))
assert years==sorted(years,reverse=True), years
assert len(papers)==14
assert 'Machine Intelligence Research · 2023' in s
assert 'Earlier preprint (2021)' in s
assert 'M3: Modularization for Multi-task and Multi-agent Offline Pre-training' in s
assert 'Accepted manuscript · 2026' in s and 'arXiv preprint · 2025' in s
print('PASS: 14 publications in descending publication-year order; journal/preprint distinction; dated and undated archives; education/current-status clarity.')

assert 'Qwen Team, Alibaba' in s and 'Mentor: Junyang Lin.' in s
assert 'Microsoft Research Asia' in s and 'Worked on speech research.' in s
experience = re.search(r'id="experience".*?</section>', s, re.S).group()
assert len(re.findall('Research Intern', experience)) == 2
assert not re.search(r'\b(?:Led|lead)\b', experience, re.I)
assert 'Early–late 2020' in experience and 'Mentor: Xu Tan.' in experience
print('PASS: user-confirmed internships, mentors and dates; modest ERNIE wording.')

about = re.search(r'id="about".*?</section>', s, re.S).group()
chronology = ['July 2019', 'early to late 2020', '2023–2024', 'CASIA) in 2024', 'In 2024–2025', 'Until January 2026']
positions = [about.index(value) for value in chronology]
assert positions == sorted(positions)
assert 'Until January 2026, I worked on reinforcement learning for subjective and objective tasks, including mathematics, coding, and instruction following, in the ERNIE Bot (Wenxin Yiyan) Sys2 team.' in about
assert not re.search(r'\b(?:Led|lead)\b', about, re.I)
print('PASS: About chronology, exact Sys2 scope/end date, and restrained contribution wording.')
