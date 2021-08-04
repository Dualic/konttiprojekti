# assesment-test

Tämä harjoitus käyttää Flaskia https://flask.palletsprojects.com/en/2.0.x/

## Asennus

1. Aloita asentamalla riippuvuudet `pip install flask`.
2. Aja `flask run --host=0.0.0.0 --port=80 --reload`. `--reload` parametri käynnistää projektin uusiksi aina kun lähdekoodi muuttuu. Samalla resetoituu tietokanta alkuperäiseen tilaansa.
3. Avaa selain omalla koneella ja kohdista se osoitteeseen http://localhost

Taustalla on SQLLite tietokanta, joka ei vaadi käyttäjältä erillistä serveriä. Kaikki tallennetaan lokaaliin tiedostoon ja luetaan sieltä.
Syntaksi on hyvin pitkälti samankaltainen kuin PostgreSQL:ssä.

Tutustu koodiin ja siinä oleviin kommentteihin. Niistä voi olla apua tehtävän kannalta.

## Tehtävänanto

### Vaihe 1

Korjaa seuraavat bugit:

- Päivämäärä blogiviestissä on eri formaatissa kuin blogiviestilistassa
- Yhden viestin poistaminen poistaa koko blogin.

### Vaihe 2

Asenna tämän repositoryn Python ohjelma virtuaalikoneelle GCP:n niin, että se kuuntelee porttia 80. Tämä tapahtuu ajamalla virtuaalikoneella `flask run --host=0.0.0.0 --port=80`. Tämä ei ole suositeltu tapa Flaskin ajamiseksi tuotannossa, mutta koska kyseessä on kurssin ulkopuolinen aihealue, emme syvenny tarkemmin tähän tässä tehtävässä. Virtuaalikoneen tulee vastata HTTP kutsuihin porttiin 80 eli jos virtuaalikoneen IP on 123.123.123.123 on osoitteen http://123.123.123.123 avattava tämä blogisofta.

## Palautus

Virtuaalikoneen IP-osoite johon ohjelma on deployattu ja linkki Github repositoryyn, jossa tarvittavat korjaukset.
