---
title: Members of the SXS collaboration
---
Please click on the name tabs to read more about our group members.

{% assign group_types = "faculty|academic_staff|postdocs|graduate_students|alumni" | split: "|" %}
{% for group_type in group_types %}
<div id="{{ group_type }}" class="people_group">
<details><summary>{{ group_type | replace: "_", " " | capitalize }}</summary>
    {% include people.html groups=group_type %}
</details>
</div>
{% endfor %}
