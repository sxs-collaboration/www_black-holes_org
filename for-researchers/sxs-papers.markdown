---
layout: post
title: SXS Papers
date: 2013-04-16 01:37:02.000000000 +00:00
---

Numerical Relativity papers published by members of the SXS Collaboration in reverse chronological order.

<div id="year_link">
{% capture written_year %}'None'{% endcapture %}
{%- assign sorted = site.papers | sort: 'date' -%}
{%- for paper in sorted reversed %}
  {% capture year %}{{ paper.date | date: '%Y' }}{% endcapture %}
  {% if year != written_year %}
  <a href="#{{ year }}">{{ year }}</a>
  {% endif %}
  {% capture written_year %}{{ year }}{% endcapture %}
{%- endfor -%}
</div>

{% capture written_year %}'None'{% endcapture %}
{%- assign sorted = site.papers | sort: 'date' -%}
{%- for paper in sorted reversed %}
  {% capture year %}{{ paper.date | date: '%Y' }}{% endcapture %}
  {% if year != written_year %}
<h2 id="{{ year | slugify }}" class="paper_year"><a href="#{{ year | slugify }}">#{{ year }}</a></h2>
  {% endif %}
  {% capture written_year %}{{ year }}{% endcapture %}
<div class="paper">
  <h3>{{ paper.title }}</h3>
  <p class="paper_authors">{{ paper.authors | join: ", "}}</p>
  {% if paper.jref %}
  <p class="paper_jref">
  {% if paper.doi %}<a href="http://dx.doi.org/{{ paper.doi }}">{% endif %}{{ paper.jref }}{% if paper.doi %}</a>{% endif %}
  </p>
  {% endif %}
  <p class="paper_arxiv"><i class="ai ai-arxiv"></i>
  [<a href="https://arxiv.org/abs/{{ paper.arxiv }}">arXiv:{{ paper.arxiv }}</a>]</p>
  <details>
  <summary>Abstract</summary>
  <div class="paper_abstract">{{ paper.abstract }}</div>
  </details>
</div>
{%- endfor -%}
