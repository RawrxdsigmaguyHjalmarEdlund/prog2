
import json
import os

FIL = "sysslor.json"

KATEGORIER = [
    "Skola",
    "Hem",
    "Träning",
    "Fritid",
    "Övrigt"
]


def ladda_sysslor():
    if os.path.exists(FIL):
        with open(FIL, "r", encoding="utf-8") as fil:
            return json.load(fil)
    return []


def spara_sysslor():
    with open(FIL, "w", encoding="utf-8") as fil:
        json.dump(sysslor, fil, ensure_ascii=False, indent=4)


def visa_sysslor():
    print("\n===== MIN PLANERING =====")

    for kategori in KATEGORIER:
        print(f"\n--- {kategori} ---")

        hittade = False

        for i, syssla in enumerate(sysslor):
            if syssla["kategori"] == kategori:
                status = "✅ Klar" if syssla["klar"] else "⏳ Inte klar"
                print(f"{i + 1}. {syssla['namn']} - {status}")
                hittade = True

        if not hittade:
            print("Inga sysslor här.")


def lagg_till():
    print("\nVälj kategori:")

    for i, kategori in enumerate(KATEGORIER):
        print(f"{i + 1}. {kategori}")

    try:
        val = int(input("Kategori: "))

        if val < 1 or val > len(KATEGORIER):
            print("Ogiltig kategori!")
            return

        namn = input("Vad ska du göra? ")

        if not namn.strip():
            print("Du måste skriva ett namn!")
            return

        sysslor.append({
            "namn": namn,
            "kategori": KATEGORIER[val - 1],
            "klar": False
        })

        spara_sysslor()
        print("Sysslan har lagts till!")

    except ValueError:
        print("Skriv en siffra!")


def markera_klar():
    visa_sysslor()

    try:
        val = int(input("\nVilken syssla är klar? "))

        if 1 <= val <= len(sysslor):
            sysslor[val - 1]["klar"] = True
            spara_sysslor()
            print("Sysslan är nu klar! 🎉")
        else:
            print("Ogiltigt nummer!")

    except ValueError:
        print("Skriv en siffra!")


def ta_bort():
    visa_sysslor()

    try:
        val = int(input("\nVilken syssla vill du ta bort? "))

        if 1 <= val <= len(sysslor):
            borttagen = sysslor.pop(val - 1)
            spara_sysslor()
            print(f"{borttagen['namn']} har tagits bort!")
        else:
            print("Ogiltigt nummer!")

    except ValueError:
        print("Skriv en siffra!")


sysslor = ladda_sysslor()

while True:
    print("\n====== PLANERINGSAPP ======")
    print("1. Visa sysslor")
    print("2. Lägg till syssla")
    print("3. Markera syssla som klar")
    print("4. Ta bort syssla")
    print("5. Avsluta")

    val = input("\nVälj ett alternativ: ")

    if val == "1":
        visa_sysslor()
    elif val == "2":
        lagg_till()
    elif val == "3":
        markera_klar()
    elif val == "4":
        ta_bort()
    elif val == "5":
        print("Tack för att du använde planeringsappen!")
        break
    else:
        print("Ogiltigt val, försök igen.")
