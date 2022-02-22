## Force Brut

Avec la méthode de force brute notre algorithme vas tester l'intégralité des possibiltées.

Donc pour une liste d'actions comprenant 5 actions nous aurons 31 possibiltées soit **p = 2^5-1**. si nous ajoutons une actions de plus nous doublons les possibilitées **p = 2^6-1** soit 63. 

Notre Résultat est exponentiel et avec une combinaison de 20 actions nous aurons donc 1.048.575 possibilitées.

Après éxécution de l'algorithme écrit avec un dataset de 20 actions l'éxécution de celle ci prend 2.34 secondes si nous ajoutons 2 actions en plus l'éxecution du script prend maintenant 9.16 secondes

![graph force brute](./doc/force_brute.png "graph force brute")