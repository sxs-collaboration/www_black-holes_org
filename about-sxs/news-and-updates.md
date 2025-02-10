# News and Updates

{% for post in site.posts %}
## [{{ post.title }}]({{ site.baseurl }}{{ post.url }})

Created on {{ post.date | date: "%B %-d, %Y" }}
{: class="dt-published"}

<div class="latest-research">{{ post.excerpt }}</div>

[Read more…]({{ site.baseurl }}{{ post.url }})
{% endfor %}
