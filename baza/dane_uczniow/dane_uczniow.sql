
DROP TABLE IF EXISTS nazwiska;
CREATE TABLE nazwiska (
    id INTEGER PRIMARY KEY,
	nazwisko TEXT,
	imie1 TEXT,
	imie2 TEXT
);



DROP TABLE IF EXISTS dane_osobowe;
CREATE TABLE dane_osobowe (
	id INTEGER PRIMARY KEY,
	dzien INTEGER,
	miesiac INTEGER,
	rok INTEGER,
	m_urodzenia TEXT,
    wojewodztwo TEXT,
    FOREIGN KEY (id) REFERENCES nazwiska(id)
);



DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny (
	id INTEGER PRIMARY KEY,
	zachowanie TEXT,
    rel_ety VARCHAR,
    jpol VARCHAR,
    jang VARCHAR,
    jniem VARCHAR,
    mat VARCHAR,
    hist VARCHAR,
    geog VARCHAR,
    biol VARCHAR,
    fiz VARCHAR,
    che VARCHAR,
    tech VARCHAR,
    info VARCHAR,
    plas VARCHAR,
    po VARCHAR,
    wf VARCHAR,
    FOREIGN KEY (id) REFERENCES nazwiska(id)
);
