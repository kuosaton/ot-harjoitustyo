```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Monopolipeli "1" -- "1" Aloitusruutu
    Monopolipeli "1" -- "1" Vankila
    Pelilauta "1" -- "40" Ruutu

    Sattuma -- "16" Toimintokortti
    Yhteismaa -- "16" Toimintokortti
    Toimintokortti "1" -- "1" Toiminto

    Ruutu "1" -- "1" Toiminto
    Ruutu "1" -- "1" Ruutu : Seuraava
    Ruutu -- Vankila
    Ruutu -- Aloitusruutu
    Ruutu -- "3" Sattuma 
    Ruutu -- "3" Yhteismaa
    Ruutu -- "4" Asema
    Ruutu -- "2" Laitos
    Ruutu -- "22" Katu
    Ruutu "1" -- "0..8" Pelinappula

    Katu "1" -- "0..4" Talo
    Katu "1" -- "0..1" Hotelli
    Katu "1" -- "1" Katu : Nimi

    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Pelaaja "1" -- Katu
    Pelaaja "1" -- Raha
```

