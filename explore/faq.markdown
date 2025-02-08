---
paginate_from_menu: true
---
# Frequently Asked Questions

{% assign groups = site.faq | map: 'group' | uniq %}
{% for group in groups %}
<div id="{{ group }}" class="people_group">
<details open><summary>{{ group }}</summary>
    {% include faq.html group=group %}
</details>
</div>
{% endfor %}
