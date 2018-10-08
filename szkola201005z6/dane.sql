
DROP TABLE IF EXISTS uczniowie;
DROP TABLE IF EXISTS przedmioty;
DROP TABLE IF EXISTS oceny;

CREATE TABLE uczniowie (
    id_ucznia INTEGER PRIMARY KEY,
    imie_ucz TEXT (15),
    nazwisko_ucz TEXT (30),
    ulica TEXT (15),
    dom INTEGER (5),
    klasa TEXT (5)
);


CREATE TABLE przedmioty (
    id_przedmiotu INTEGER PRIMARY KEY,
    nazwaprzedmiotu TEXT (20),
    nazwisko_naucz TEXT (20),
    imie_naucz TEXT (20)
);


CREATE TABLE oceny (
    id_ucznia INTEGER PRIMARY KEY,
    ocena INTEGER (5),
    data_ DATE,
    id_przedmiotu INTEGER,
    FOREIGN KEY (id_ucznia) REFERENCES uczniowie(id_ucznia),
    FOREIGN KEY (id_przedmiotu) REFERENCES przedmioty(id_przedmiotu)
);
