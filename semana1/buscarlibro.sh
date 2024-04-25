#!/bin/bash

echo -n "Por favor, introduce la palabra a buscar: "
read palabraClave
echo -n "Los libros que contienen la palabra buscada son: "
grep -l " $palabraClave" data/*