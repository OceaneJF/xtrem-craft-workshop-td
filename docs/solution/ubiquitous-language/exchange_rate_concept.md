# Concept

> definition Exchange Rate permet de convertir une monnaie à une autre.

## Properties

- taux cohéficient multiplicateur à appliquer pour faire la conversion
- from_currency monnaie que l'on souhaite convertir
- to_currency monnaie que l'on souhaite obtenir

## Responsibilities

- S'assurer que la conversion se fait correctement avec des monnaies valides

## Invariants

- Il faut deux monnaies et un taux non null
- Le taux ne peut pas être négatif ou null

## Collaborators

- bank
