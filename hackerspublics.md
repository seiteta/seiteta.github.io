---
layout: default
title: Tous les épisodes
---

<h1 class="post-title">Hackers publics</h1>

Avec Hackers publics, partez à la rencontre celles et ceux qui transforment la culture numérique de l’administration.

Prenez une grande bouffée d’inspiration et découvrez l’avant-garde de l’innovation publique.

Si vous êtes dans l’administration, vous verrez que vous n’êtes pas seul à essayer de changer les choses.

Si vous n’en faites pas (encore) partie, vous découvrirez qu’il est possible d’innover tout en ayant un travail qui a du sens ! Et qui sait, ça vous donnera peut-être envie de nous rejoindre pour nous donner un coup de main ?

Accéder au podcast sur <a href="https://open.spotify.com/show/17E4Bxj2VOnE4esRGJ5yAg?si=yl3yH7zpQ3ePml-juvNFpw">Spotify</a>, <a href="https://podcasts.apple.com/fr/podcast/hackers-publics/id1498775170">iTunes</a> ou via votre <a href="{{ site.url }}/hackerspublics.rss">application de podcast préférée</a>.

<div class="posts">
  {% for episode in site.hackerspublics reversed %}
  <div class="post">
    <h1 class="post-title">
      <a href="{{ episode.url }}">
        {{ episode.title }}
      </a>
    </h1>
    {{ episode.content }}
    Téléchargez l'épisode <a href="https://hackerspublics.s3.fr-par.scw.cloud/{{ page.file }}">ici</a> ou écoutez-le sur <a href="{{ page.spotify_url }}">Spotify</a>, <a href="{{ page.itunes_url }}">iTunes</a> ou votre <a href="{{ site.url }}/hackerspublics.rss">application de podcast préférée</a>.
    <span class="post-date">{% include date-fr.html date=episode.date %}</span>
    {% include share-buttons.html %}
  </div>
  {% endfor %}
</div>
