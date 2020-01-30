---
layout: default
title: Tous les épisodes
---

<div class="posts">
  {% for episode in site.hackers_publics %}
  <div class="post">
    <h1 class="post-title">
      <a href="{{ episode.url }}">
        {{ episode.title }}
      </a>
    </h1>
    {{ episode.content }}
    <span class="post-date">{% include date-fr.html date=episode.date %}</span>
  </div>
  {% endfor %}
</div>
