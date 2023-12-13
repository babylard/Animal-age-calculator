import PySimpleGUI as sg

class Animals:
    
    def calculate_cat_age(age):
        if age == str(1):
            print("Your cat is approximately 15 years old in cat years.")
        elif age == str(2):
            print("Your cat is approximately 24 years old in cat years.")
        else:
            cat_years = 24 + (int(age) - 2) * 4
            print(f"Your cat is approximately {cat_years} years old in cat years.")

    def calculate_dog_age(age):
        if age == str(1):
            print("Your dog is approximately 7 years old in dog years.")
        elif age == str(2):
            print("Your dog is approximately 14 years old in dog years.")
        else:
            dog_years = 14 + (int(age) - 2) * 7
            print(f"Your dog is approximately {dog_years} years old in dog years.")

    def calculate_chicken_age(age):
        if age == str(1):
            print("Your chicken is approximately 15 years old in chicken years.")
        elif age == str(2):
            print("Your chicken is approximately 24 years old in chicken years.")
        else:
            chicken_years = 24 + (int(age) - 2) * 5
            print(f"Your chicken is approximately {chicken_years} years old in chicken years.")
    
    def calculate_cow_age(age):
        if age == str(1):
            print("Your cow is approximately 18 years old in cow years.")
        elif age == str(2):
            print("Your cow is approximately 28 years old in cow years.")
        else:
            cow_years = 28 + (int(age) - 2) * 4
            print(f"Your cow is approximately {cow_years} years old in cow years.")
    
    def calculate_sheep_age(age):
        if age == str(1):
            print("Your sheep is approximately 15 years old in sheep years.")
        elif age == str(2):
            print("Your sheep is approximately 24 years old in sheep years.")
        else:
            sheep_years = 24 + (int(age) - 2) * 6
            print(f"Your sheep is approximately {sheep_years} years old in sheep years.")

    def calculate_pig_age(age):
        if age == str(1):
            print("Your pig is approximately 18 years old in pig years.")
        elif age == str(2):
            print("Your pig is approximately 30 years old in pig years.")
        else:
            pig_years = 30 + (int(age) - 2) * 5
            print(f"Your pig is approximately {pig_years} years old in pig years.")
    
    def calculate_horse_age(age):
        if age == str(1):
            print("Your horse is approximately 15 years old in horse years.")
        elif age == str(2):
            print("Your horse is approximately 24 years old in horse years.")
        else:
            horse_years = 24 + (int(age) - 2) * 3
            print(f"Your horse is approximately {horse_years} years old in horse years.")
    
    def calculate_goat_age(age):
        if age == str(1):
            print("Your goat is approximately 15 years old in goat years.")
        elif age == str(2):
            print("Your goat is approximately 24 years old in goat years.")
        else:
            goat_years = 24 + (int(age) - 2) * 4
            print(f"Your goat is approximately {goat_years} years old in goat years.")
    
    def calculate_rabbit_age(age):
        if age == str(1):
            print("Your rabbit is approximately 15 years old in rabbit years.")
        elif age == str(2):
            print("Your rabbit is approximately 24 years old in rabbit years.")
        else:
            rabbit_years = 24 + (int(age) - 2) * 6
            print(f"Your rabbit is approximately {rabbit_years} years old in rabbit years.")

    def calculate_duck_age(age):
        if age == str(1):
            print("Your duck is approximately 12 years old in duck years.")
        elif age == str(2):
            print("Your duck is approximately 20 years old in duck years.")
        else:
            duck_years = 20 + (int(age) - 2) * 5
            print(f"Your duck is approximately {duck_years} years old in duck years.")

    def calculate_turkey_age(age):
        if age == str(1):
            print("Your turkey is approximately 10 years old in turkey years.")
        elif age == str(2):
            print("Your turkey is approximately 18 years old in turkey years.")
        else:
            turkey_years = 18 + (int(age) - 2) * 5
            print(f"Your turkey is approximately {turkey_years} years old in turkey years.")

    def calculate_guinea_pig_age(age):
        if age == str(1):
            print("Your guinea pig is approximately 6 years old in guinea pig years.")
        elif age == str(2):
            print("Your guinea pig is approximately 12 years old in guinea pig years.")
        else:
            guinea_pig_years = 12 + (int(age) - 2) * 4
            print(f"Your guinea pig is approximately {guinea_pig_years} years old in guinea pig years.")

    def calculate_cattle_age(age):
        if age == str(1):
            print("Your cattle is approximately 18 years old in cattle years.")
        elif age == str(2):
            print("Your cattle is approximately 30 years old in cattle years.")
        else:
            cattle_years = 30 + (int(age) - 2) * 5
            print(f"Your cattle is approximately {cattle_years} years old in cattle years.")

    def calculate_donkey_age(age):
        if age == str(1):
            print("Your donkey is approximately 15 years old in donkey years.")
        elif age == str(2):
            print("Your donkey is approximately 24 years old in donkey years.")
        else:
            donkey_years = 24 + (int(age) - 2) * 4
            print(f"Your donkey is approximately {donkey_years} years old in donkey years.")

    def calculate_geese_age(age):
        if age == str(1):
            print("Your goose is approximately 10 years old in goose years.")
        elif age == str(2):
            print("Your goose is approximately 18 years old in goose years.")
        else:
            goose_years = 18 + (int(age) - 2) * 5
            print(f"Your goose is approximately {goose_years} years old in goose years.")


class GUI:

    def main():
        sg.theme("Reddit")

        animal = [
        "Cat",
        "Dog",
        "Chicken",
        "Cow",
        "Sheep",
        "Pig",
        "Horse",
        "Goat",
        "Rabbit",
        "Duck",
        "Turkey",
        "Guinea pig",
        "Common Cattle",
        "Donkey",
        "Goose"
    ]

        layout = [
            [sg.Text("Input age:           Choose an Animal:")],
            [sg.Input(key="-IN-", size=(13,1)), sg.Combo(animal, key="-ANIMAL-")],
            [sg.Output(key="-OUT-", size=(40,10))],
            [sg.Button("Calculate", key="-CALC-")]
        ]

        window = sg.Window('Animal age Calculator', layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED:
                break
            elif event == '-CALC-':
                window['-OUT-'].update("")
                if values["-ANIMAL-"] == "Cat":
                    Animals.calculate_cat_age(values["-IN-"])
                elif values["-ANIMAL-"] == "Dog":
                    Animals.calculate_dog_age(values["-IN-"])
                elif values["-ANIMAL-"] == "Chicken":
                    Animals.calculate_chicken_age(values["-IN-"])
                elif values["-ANIMAL-"] == "Cow":
                    Animals.calculate_cow_age(values["-IN-"])
                elif values["-ANIMAL-"] == "Sheep":
                    Animals.calculate_sheep_age(values["-IN-"])
                elif values["-ANIMAL-"] == "Pig":
                    Animals.calculate_pig_age(values["-IN-"])
                elif values["-ANIMAL-"] == "Horse":
                    Animals.calculate_horse_age(values["-IN-"])
                elif values["-ANIMAL-"] == "Goat":
                    Animals.calculate_goat_age(values["-IN-"])
                elif values["-ANIMAL-"] == "Rabbit":
                    Animals.calculate_rabbit_age(values["-IN-"])
                elif values["-ANIMAL-"] == "Duck":
                    Animals.calculate_duck_age(values["-IN-"])
                elif values["-ANIMAL-"] == "Turkey":
                    Animals.calculate_turkey_age(values["-IN-"])
                elif values["-ANIMAL-"] == "Guinea pig":
                    Animals.calculate_guinea_pig_age(values["-IN-"])
                elif values["-ANIMAL-"] == "Common Cattle":
                    Animals.calculate_cattle_age(values["-IN-"])
                elif values["-ANIMAL-"] == "Donkey":
                    Animals.calculate_donkey_age(values["-IN-"])
                elif values["-ANIMAL-"] == "Goose":
                    Animals.calculate_geese_age(values["-IN-"])
                else:
                    pass

if __name__ == "__main__":
    GUI.main()