---
layout: default
title: Tous les épisodes
---

<div class="posts">
  {% for episode in site.episodes %}
  <div class="post">
    <h1 class="post-title">
      <a href="{{ episode.file }}">
        {{ episode.title }}
      </a>
    </h1>
    {{ post.content }}
    <span class="post-date">{% include date-fr.html date=post.date %}</span>
  </div>
  {% endfor %}
</div>
