# s28675_2025.py
# Cel programu: Tworzy losową sekwencje DNA i zapisuje jej w standarcie formatu FASTA. Uzyttkownik poprzez konsole podaje długość sekwencji, ID, opis oraz imie
# Kontekst zastosowania: Bioinformatyka - może być użyty do testowania narzędzi i analiz korzystających z danych genetycznych zapisanych w formacie FASTA
# Program pyta użytkownika o podanie kilku informacji (dlugosc sekwencji,ID,opis sekwencji,imie). Nastpęnie generuje sekwencję DNA, zapisuje to do pliku, wyświetla statystyki zawartości poszczególnych nukleotydów. Imie uzytkownika wstawiane jest w losowe miejsce w sekwencji (nie wplywa to na wyniki obliczenia)

import random  # Importowanie library do generowania wartości losowych


# Funkcja do generowania losowej sekwencji DNA
def generate_dna_sequence(length):
    return ''.join(random.choices('ACGT', k=length))

# Funkcja do obliczania statystyk sekwencji
def calculate_statistics(sequence):
    total = len(sequence)
    stats = {nuc: (sequence.count(nuc) / total) * 100 for nuc in 'ACGT'}
    cg_ratio = (sequence.count('C') + sequence.count('G')) / total * 100
    return stats, cg_ratio

# Główna część programu
def main():
    # Pobranie danych od użytkownika
    length = int(input("Podaj długość sekwencji: "))
    seq_id = input("Podaj ID sekwencji: ")
    description = input("Podaj opis sekwencji: ")
    name = input("Podaj imię: ")

    # Generowanie sekwencji
    # ORIGINAL:
    # sequence = generate_dna_sequence(length)
    # MODIFIED (dodanie zabezpieczenia, nie można wprowadzić sekwencji mniejszej niż 0):
    if length <= 0:
        print("Długość sekwencji musi być większa niż 0.")
        return
    sequence = generate_dna_sequence(length)

    # Wstawienie imienia w losowe miejsce (bez wpływu na statystyki)
    insert_pos = random.randint(0, len(sequence))
    sequence_with_name = sequence[:insert_pos] + name + sequence[insert_pos:]

    # Obliczanie statystyk (bez liter imienia)
    stats, cg_ratio = calculate_statistics(sequence)

    # Zapis do pliku w formacie FASTA
    filename = f"{seq_id}.fasta"

    # ORIGINAL:
    # with open(filename, 'w') as f:
    #     f.write(f">{seq_id} {description}\n")
    #     f.write(sequence_with_name + "\n")
    # MODIFIED (dzieli sekwencje na linie po 60 znakow, ulatwia czytelność i jest zgodne z dobrymi praktykami FASTA ):
    with open(filename, 'w') as f:
        f.write(f">{seq_id} {description}\n")
        for i in range(0, len(sequence_with_name), 60):
            f.write(sequence_with_name[i:i+60] + "\n")

    print(f"Sekwencja została zapisana do pliku {filename}")
    print("Statystyki sekwencji:")
    for nuc in 'ACGT':
        print(f"{nuc}: {stats[nuc]:.1f}%")
    print(f"%CG: {cg_ratio:.1f}")

# ORIGINAL:
# if __name__ == "__main__":
#     main()
# MODIFIED (dodałem osbługe błędów na wejsciu):
if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("Wprowadź poprawną liczbę całkowitą jako długość sekwencji ")
