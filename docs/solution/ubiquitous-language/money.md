# Concept

> Un Money représente un montant dans une devise spécifique. C'est un objet valeur immuable.

## Properties

- `amount` : le montant (nombre positif ou nul)
- `currency` : la devise (instance de `Currency`)

## Responsibilities

- Additionner deux Money de même devise
- Multiplier un Money par un nombre
- Diviser un Money par un nombre
- Comparer deux Money (égalité sur le montant et la devise)

## Invariants

- Le montant ne peut pas être négatif
- La devise doit être une instance de `Currency` (pas une chaîne de caractères)
- On ne peut pas additionner deux Money de devises différentes
- On ne peut pas multiplier ou diviser par autre chose qu'un nombre (`int` ou `float`)

## Collaborators

- `Currency` : définit la devise du Money
- `Portfolio` : contient une collection de Money dans différentes devises
- `Bank` : convertit un Money d'une devise vers une autre
- `ExchangeRate` : taux utilisé par la Bank pour convertir un Money
