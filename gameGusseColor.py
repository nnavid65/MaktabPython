# Make a List with 5 color and randomly make a list
import random


def guess_color():
    color = ['red', 'blue', 'green', 'yellow', 'purple']
    random.shuffle(color)
    return color

def get_color_list():
    # Ask user to input 5 colors
    colors = []
    for i in range(5):
        color = input(f"Enter color {i + 1}: ").strip().lower()
        colors.append(color)
    return colors

def comapre_colors(user_colors, random_colors):
    matched_colors = 0
    for i in range(len(user_colors)):
        if user_colors[i] == random_colors[i]:
            matched_colors += 1
    return matched_colors

def main():
    print("Welcome to the Color Guessing Game!")
    random_colors = guess_color()
    #print("Randomly selected colors are:", random_colors)

    print("You need to guess the colors in the correct order.")
    print("You will input 5 colors, and the game will tell you how many colors you guessed correctly.")
    print("If you guess all colors correctly, you win!")
    print("You have to chose 5 colors. The colors are: red, blue, green, yellow, purple.")
    print("Let's start the game!")

    user_colors = get_color_list()
    print("Your selected colors are:", user_colors)
    
    # Count the trails 
    i = 1
    print(f"Attempt {i}:")
    matched_colors = comapre_colors(user_colors, random_colors)
    while matched_colors != 5:
        print(f"You guessed {matched_colors} colors correctly.")
        print("Please input your colors and Try again!")
        user_colors = get_color_list()
        matched_colors = comapre_colors(user_colors, random_colors)
        print("Your selected colors are:", user_colors)
        i += 1
        print(f"Attempt {i}:")
        
    if matched_colors == 5:
        print("Congratulations! You guessed all colors correctly!")
        print(f"It took you {i} attempts to guess all colors correctly.")
        print("Thank you for playing the Color Guessing Game!")
        print("Goodbye!")

# Run the game
if __name__ == "__main__":
    main()  