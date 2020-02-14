---
layout: default
title: Tous les épisodes
---

<h1 class="post-title">Hackers publics</h1>

Avec Hackers publics, partez à la rencontre celles et ceux qui transforment la culture numérique de l’administration.

Prenez une grande bouffée d’inspiration et découvrez l’avant-garde de l’innovation publique.

Si vous êtes dans l’administration, vous verrez que vous n’êtes pas seul à essayer de changer les choses.

Si vous n’en faites pas (encore) partie, vous découvrirez qu’il est possible d’innover tout en ayant un travail qui a du sens ! Et qui sait, ça vous donnera peut-être envie de nous rejoindre pour nous donner un coup de main ?


<div class="posts">
  {% for episode in site.hackerspublics %}
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
