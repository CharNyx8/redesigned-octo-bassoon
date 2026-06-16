import random


def i_like_the_color_yellow_but_blue_is_so_pretty_yk(x):
    RANDO = {
        "career": ["You are getting fired.", "You are getting promoted!"],
        "love": ["Your crush will say Hi!", "You and your significant other need to break up.",
                 "your significant other is going to propose."],
        "health": [
            "Your health is taking a turn for the worst.", "Your health is looking brighter!",
            "Lets get a bit healthier"],
        "life": [
            "Move to a new country!",
            "Everything will be better soon.",
            "A new adventure awaits. "]
    }
    if x not in RANDO:
        category = "life"
    return random.choice(RANDO[x])
def why_was_six_scared_of_seven_cause_seven_eight_nine():
    return sorted(random.sample(range(1, 51), 5))
def cool_beans_rando_stuff():
    colors = ["Blue", "Green", "Orange", "Purple", "Gold"]
    return random.choice(colors)
def idk():
    whatever_xyz = input("Choose a category (career, love, health, life): ").lower()
    numbers = sorted(random.sample(range(1, 51), 5))
    color = random.choice(["Blue", "Green", "Orange", "Purple", "Gold"])
    fortune = i_like_the_color_yellow_but_blue_is_so_pretty_yk(whatever_xyz)
    print(f"\nFortune: {fortune}")
    print(f"Lucky Color: {color}")
    print(f"Lucky Numbers: {numbers}")
if __name__ == "__main__":
    idk()