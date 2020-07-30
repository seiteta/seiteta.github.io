---
title: "Résumé du livre « Accelerate » (1/n)"
description: "Dans cette première partie, vous apprendrez comment mesurer la performance de production de logiciel et quelle est la culture des équipes les plus performantes. Bonne lecture !"
image: https://images.unsplash.com/photo-1476725994324-6f6833ea0631?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1200&q=80
tags: [Résumé, DevOps, Performance, Cutlure, Développement, Logiciel]
---

> Parce que certaines idées méritent d’être diffusées, je teste un nouveau format d’article : le résumé de livre.
>
> Pour ce premier résumé, j’ai choisi **[Accelerate: Building and Scaling High-Performing Technology Organizations](https://itrevolution.com/book/accelerate/)** que l’on m’a plusieurs fois conseillé. L’idée principale de ce livre est que les organisations ont intérêt à accélérer la livraison de leurs produits numériques car cela améliore leur performance à tous les niveaux. Cette accélération est accompagnée d’une amélioration de la qualité, rendue possible par des changements organisationnels et méthodologiques, regroupés sous le terme DevOps.
>
> Dans cette première partie, vous apprendrez comment mesurer la performance de production de logiciel et quelle est la culture des équipes les plus performantes. Bonne lecture !

## Chapitre 1 - accélérer

Aujourd’hui, tous les secteurs ont tendance à accélérer. Cette accélération est principalement dûe au développement logiciel, qui évolue grâce à des nouvelles pratiques comme le mouvement  [DevOps](https://fr.wikipedia.org/wiki/Devops). Le DevOps est né pour répondre à cette question : comment construire des systèmes sûrs, résilients, évolutifs et distribués, à grande échelle ?

Certaines organisations pratiquent ces méthodes de développement modernes mais beaucoup ne se sont pas ou peu transformées. Une telle transformation nécessite de se concentrer sur ses capacités (i.e. « _comment j'améliore mes résultats clés grâce à mes capacités ?_ ») plutôt que sur sa maturité (i.e. « _où j'en suis dans ma transformation ?_ »). Une organisation ne peut jamais se considérer comme mature : l'environnement change continuellement et livrer rapidement des logiciels fiables est une quête perpétuelle.

La question qui se pose alors est : sur quelles capacités se concentrer ? À travers leurs recherches, les auteurs en ont identifié vingt-quatre, qui seront détaillées dans les chapitres suivants.


## Chapitre 2 - mesurer la performance

Avant toute chose, il faut définir ce qu’est la performance pour une équipe qui produit des logiciels. Les méthodes classiques de mesure de cette performance ont deux problèmes : elles se concentrent sur la production (**output**) plutôt que sur le résultat (**outcome**), et sur des mesures individuelles plutôt qu’en équipe. Pour éviter ces écueils, il faut donc chercher des indicateurs qui se concentrent sur le résultat, et mesurés de manière collective.

Les auteurs ont sélectionnés quatre indicateurs qui possèdent ces caractéristiques :
Le délai de livraison (**delivery lead time**) : le temps qu’il faut pour passer du code archivé (**committed**) au code mis en production avec succès ;
La fréquence de déploiement : la fréquence à laquelle le code est déployé en production ou dans un magasin d’applications ;
Le délai de restauration moyen : le temps moyen nécessaire pour restaurer le service suite à un incident ;
Le taux d’échec de changement : le pourcentage de changement de code qui entraîne une dégradation du service ou exige une réparation comme un retour en arrière (**rollback**).

Pour récolter leurs données, les auteurs ont organisé un sondage annuel de 2014 à 2017 pour savoir comment les organisations se situaient par rapport à ces quatre indicateurs. Ils ont ensuite réalisé une analyse par partitionnement (**cluster analysis**) pour séparer les organisations en trois groupes en fonction de leur performance : bonne, moyenne et mauvaise.

Un point intéressant : les organisations qui sont performantes sont bonnes sur les quatre indicateurs. Il n'y a donc pas de dilemme entre qualité et rapidité ; plus on va vite, plus on fait du bon code. À noter que l’écart de performance entre les organisations se creuse d’année en année.

La performance en livraison logicielle est très importante car elle prédit (au sens statistique) la performance commerciale des entreprises et de la performance non-commercial des autres organisations.

Comment faire alors pour améliorer la performance en livraison logicielle ? Certes, il faut des outils adaptés, mais il est d’abord indispensable d'avoir la bonne culture organisationnelle.


## Chapitre 3 - mesurer et changer la culture

Le sociologue Ron Westrum a développé une typologie pour classer les [cultures organisationnelles](https://qualitysafety.bmj.com/content/13/suppl_2/ii22.short) :

* Pathologique (axé sur le pouvoir) : l'organisation est basée sur la peur et les menaces. Les individus font de la rétention d'informations.
* Bureaucratique (axé sur les règles) : l'organisation protège les départements. Ces départements défendent leur pré carré et agissent selon leur propres règles.
* Générative (axé sur la performance) : l'organisation de concentre sur sa mission. Tout est subordonné à la performance et sur la raison d'être.

Afin d’estimer où se positionnaient les différentes organisations dans ce continuum culturel, les auteurs ont posés des questions pour savoir notamment si les responsabilités étaient partagés, si le travail inter-équipe était encouragé et si les échecs entraînaient une enquête pour améliorer les processus plutôt que pour désigner un coupable.

Les résultats de l’étude montre que la culture organisationnelle prédit la performance en livraison logicielle et la performance commerciale : plus une organisation est générative (et donc plus les informations circulent de manière fluide), plus elle est performante.

Un point à souligner : la culture organisationnelle n’est pas liée au type d’organisation. Il existe des organisations gouvernementales génératives et des startups pathologiques.

La bonne nouvelle, c’est que pour avoir une culture plus générative, il ne faut pas changer les personnes, mais la manière dont elles agissent et leurs interactions au sein des équipes (voir l’[étude de Google en 2015 sur le sujet](https://rework.withgoogle.com/guides/understanding-team-effectiveness/steps/identify-dynamics-of-effective-teams/) ou l'[article de John Shook sur la transformation d'un site de production automobile](https://www.lean.org/Search/Documents/35.pdf)). Les concepts de management _lean_ et de livraison continue, qui seront développés dans les chapitres suivants, prédisent en effet la culture organisationnelle.

> Dans la prochaine partie de ce résumé, vous découvrirez quelles sont les pratiques techniques qui permettent de transformer la culture et d’améliorer la performance de livraison logicielle. À très vite !
