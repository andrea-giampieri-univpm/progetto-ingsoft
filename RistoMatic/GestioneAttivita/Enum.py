from enum import Enum

class Zone(Enum):
    CUCINA = 1
    BAR = 2
    FORNO = 3

class StatoComanda(Enum):
    CREATA = 0
    IN_PREPARAZIONE = 1
    COMPLETATA = 2
    ANNULLATA = 3

class StatoTavolo(Enum):
    UTILIZZABILE = "Libero"
    OCCUPATO = "Occupato"
    PRENOTATO = "Prenotato"

class StatoPrenotazione(Enum):
    CONFERMATA = "Confermata"
    NON_CONFERMATA = "Non Confermata"
