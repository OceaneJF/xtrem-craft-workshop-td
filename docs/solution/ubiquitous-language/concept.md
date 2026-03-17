# Concept

> definition : Portfolio est un porte-feuille qui est relié à une banque et qui contient les differents types de monnaies d'une personne (exemple : 5 eur, 8 usd ect...)

## Properties

- money_dict : Dictionnaire des differentes monnaies presentent dans le portfolio 

## Responsibilities

- Pouvoir deposer de l'argent dans un portfolio avec une monnaie existante.
- On peut aussi evaluer le portfolio pour savoir combien d'argent on a dans une monnaie demandé

## Invariants

- Bank qui est toujours la meme pour un portfolio
- Currency qui sont celle definit dans l'énumeration Currency

## Collaborators

- Currency
- Bank
- Money
- taux de change
