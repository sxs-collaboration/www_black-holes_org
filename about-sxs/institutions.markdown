---
layout: post
title: Our Institutions
joomla_id: 179
joomla_url: our-institutions
date: 2016-02-03 21:54:39.000000000 +00:00
paginate_from_menu: true
---
The SXS project is a collaborative research effort involving members
from multiple institutions. These links give you more information
about our members' homes.

{%- assign sorted = site.institutions | sort: 'name' -%}
{%- for inst in sorted %}
<div class="institution">
  <h2 class="inst-name">{{ inst.name }}

  <img class="inst_logo_r" src="{{ site.baseurl }}/images/institutions/{{ inst.logo_src }}"
  {%- if inst.logo_alt %}
       alt="{{ inst.logo_alt }}"
  {% endif -%}{%- if inst.logo_w %}
       width="{{ inst.logo_w }}"
  {% endif -%}{%- if inst.logo_h %}
       height="{{ inst.logo_h }}" 
  {% endif -%}/>
  </h2>

  <a href="{{ inst.home_url }}">{{ inst.home_link_text }}</a>

  {{ inst.content }}

</div>
{%- endfor -%}
