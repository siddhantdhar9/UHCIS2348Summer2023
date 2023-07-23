# Siddhant Dhar - PSID: 1512852
# Zylabs 12.7:  Fat-burning heart rate

def get_age():
    age = int(input())
    if age <= 18 or age >= 75:
        raise ValueError("Invalid age.")
    else:
        # Raise exception for invalid ages
        return age


def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * .7
    return heart_rate


if __name__ == "__main__":
    # call get_age() with a variable = "check_age" and fat_burning_heart_rate() as "burning_rate"
    try:
        check_age = get_age()
        burning_rate = fat_burning_heart_rate(check_age)
        print("Fat burning heart rate for a", check_age, "year-old:", burning_rate, "bpm")
    # Handle the exception
    except ValueError as excpt:
        print(excpt)
        print("Could not calculate heart rate info.\n")
