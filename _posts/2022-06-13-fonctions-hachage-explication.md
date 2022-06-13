---
title: "Les fonctions de hachage, expliquées simplement"
description: "Sans fonctions de hachage, il n'y aurait pas de sécurité sur Internet. Ni de blockchain. Autant dire que c'est un concept plutôt important ! Mais qu'est-ce que c'est une fonction de hachage ?"
image: https://images.unsplash.com/photo-1553991562-5ee67c3adc35?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1200&q=60
tags: [Cryptographie, Internet, Blockchain, Hachage, Empreinte]
---

Sans les fonctions de hachage, pas de sécurité sur Internet, ni de *blockchains*, ni de signature électronique. C'est une des briques fondamentales de la sécurité en ligne. Mais qu'est-ce que c'est une fonction de hachage ? Et à quoi servent-elles ?

Une fonction de hachage, c'est un peu comme un hachoir à viande, mais pour les données. Dans un hachoir à viande, vous pouvez mettre du bœuf, du poulet, du porc… vous obtiendrez toujours la même chose : de la viande hachée.

* `🐄` ➔ `🥩`
* `🐓` ➔ `🥩`
* `🐖` ➔ `🥩`

Dans une fonction de hachage, vous pouvez mettre n'importe quel texte, vous obtiendrez toujours la même chose : du texte illisible (appelé empreinte ou *hash*)

* `Longtemps je me suis couché de bonne heure` ➔ `F151075AF003B1E0D5E80147DBF14DAE`
* `Longtemps je me suis couché 2 bonne heure` ➔ `DAB780064C91AA5A4D93DA6BC34245E9`
* `gm` ➔ `92073D2FE26E543CE222CC0FB0B7D7A0`

Quand vous avez de la viande hachée, vous ne pouvez pas « dé-hacher » la viande. C'est pareil pour les fonctions de hachages : vous ne pouvez pas revenir en arrière et retrouver les données initiales. Ça ne fonctionne que dans un sens.

La seule manière de retrouver un message à partir de son empreinte, c'est de tester plein de messages en espérant tomber sur la même empreinte. Ça s'appelle une attaque par force brute et ça porte plutôt bien son nom : c'est très long et très coûteux.

Pourquoi ? Parce que les fonctions de hachage sont bien faites. En regardant les exemples proposés plus haut, on voit en effet que :
 * en changeant un seul mot (`deux` qui devient `2`), on obtient une empreinte complètement différente (ça s'appelle l'effet avalanche ❄️)
 * quelque soit la longueur du message d'entrée, l'empreinte est toujours de la même taille 🐾

Mais au final, pourquoi transformer de la belle prose en une vilaine chaîne de caractère ? Parce que ça permet de faire plein de choses pardi ! Prenons les mots de passe par exemple : ils ne sont pas stockés tel quel sur Internet. Ils sont hachés avant d'être enregistrés : `azerty123456` devient `E4B4C6324ED01B8EDF3139C32C413C00`. Ainsi, personne ne peut connaître votre mot de passe, même pas la personne qui gère la base de données dans laquelle il est sauvegardé.

Et quand vous voulez vous connecter ? Rien de plus simple : vous tapez votre mot de passe, il est haché, et si son empreinte est la même que l'empreinte enregistrée vous pouvez entrer. Parce qu'une autre propriété des fonctions de hachage est qu'elles sont déterministes : le même message produit toujours la même empreinte. C'est pour celà qu'on les utilise aussi pour la signature électronique ou pour vérifier qu'un logiciel téléchargé n'a pas été modifié.

Enfin, les fonctions de hachage sont très rapides à calculer. C'est pour cela qu'on les utilise dans les *blockchains*. En effet, on a besoin de s'assurer que l'historique des transactions n'a pas été changé. Pour cela, à chaque bloc de transaction, on calcule une nouvelle empreinte à partir du bloc et de l'empreinte du bloc précédent. N'importe qui peut donc vérifier que rien n'a été changé dans l'historique des transactions très rapidement : il suffit de recalculer les empreintes successives, ce qui est beaucoup plus rapide que de vérifier une à une toutes les transactions.