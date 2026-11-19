import json

FILENAME = "notes.json"

def save_notes(notes: list[str]):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(notes, file, indent=2, ensure_ascii=False)

def load_notes():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            contents = file.read()
            return json.loads(contents) if contents.strip() else []
    except FileNotFoundError:
        return []

def main():
    notes = load_notes()

    while True: 
        print("Vad vill du göra?")
        print("1. Visa anteckningar")
        print("2. Lägg till amnteckningar")
        print("3. Ta bort alla")
        print("4.Avsluta")

        choice = input("Välj ett av alternativen [1-4]")

        if choice == "1":
            print("\nDina anteckningar")
            if not notes:
                print("Du har inga")
            else:
                for i, note in enumerate(notes, start=1):
                    print(f"{i}. {note}")

        elif choice == "2":
            text = input("skriv en anteckning: ")
            notes.append(text)
            save_notes(notes)
            print("Anteckningen är sparad")

        elif choice == "3":
            notes.clear()
            save_notes(notes)
            print("Alla anteckningar är raderade")

        elif choice == "4":
            print("Avslutar...")
            break
        else:
            print("skriv [1-4] hur svårt kan det vara")

if __name__ == "__main__":
    main()