import random

# Welcome message
name = input("What is your name? ")
print("Hello, " + name + "! Time to play Hangman!")
print("Start guessing...\n")

# Word list
words = ['python', 'programming', 'treasure', 'creative', 'medium', 'horror',"Mountain","Clockwork","Velvet","Serendipity","Algorithm",
         "Banana","Jubilee","Chameleon","Fractal","Gazebo","Ignition","Kettle","Labyrinth","Muffin","Nostalgia","Opal","Penguin","Quiver",
         "Rhinoceros","Satellite","Tundra","Utopia","Vortex","Wanderlust","Xenon","Yacht","Zephyr","Acoustic","Blossom","Caramel","Dolphin"
         ,"Ember","Fjord","Glimmer","Harbor","Inkwell","Jigsaw","Koala","Lollipop","Meadow","Nutmeg","Orchid","Parachute","Quill","Rocket",
         "Sparrow","Tangerine","Umbrella","Violin","Waffle","Xylophone","Yoga","Zigzag","Aubergine","Bubble","Canyon","Denim","Eyelash",
         "Fountain","Grapefruit","Hurricane","Ivory","Jungle","Kiwi","Lemonade","Mustard","Noodle","Octopus","Pajamas","Quartz","Rainbow"
         ,"Scarf","Trombone","Unicorn","Volcano","Willow","X-ray","Yogurt","Zodiac","Albatross","Biscuit","Cucumber","Dandelion","Emerald",
         "Feather","Globule","Honeycomb","Island","Jellyfish","Knapsack","Lavender","Marmalade","Nightingale","Oasis","Peacock","Question",
         "Rifle","Seashell","Tapestry","Unison","Vulture","Wren","Yew","Zither"]
word = random.choice(words)

guesses = ''
turns = 5

# Hangman drawings
hangman = [
    '''
       -----
       |   |
           |
           |
           |
           |
    --------
    ''',
    '''
       -----
       |   |
       O   |
           |
           |
           |
    --------
    ''',
    '''
       -----
       |   |
       O   |
       |   |
           |
           |
    --------
    ''',
    '''
       -----
       |   |
       O   |
      /|   |
           |
           |
    --------
    ''',
    '''
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    --------
    ''',
    '''
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    --------
    '''
]

# Game loop
while turns > 0:
    failed = 0
    
    # Show hangman
    print(hangman[5 - turns])
    
    # Display word with blanks
    print("\nWord: ", end="")
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    
    # Check if won
    if failed == 0:
        print("\n\n*** YOU WON! ***")
        print("The word was: " + word)
        break
    
    # Show remaining turns
    print("\n\nLives left: " + "❤ " * turns)
    print("Guessed letters: " + guesses)
    
    # Get guess
    guess = input("\nGuess a letter: ").lower()
    
    # Validate input
    if len(guess) != 1:
        print("Please enter only one letter!")
        continue
    
    if guess in guesses:
        print("You already guessed that letter!")
        continue
    
    # Add to guesses
    guesses += guess
    
    # Check if wrong
    if guess not in word:
        turns -= 1
        print("\n❌ Wrong!")
        print("You have " + str(turns) + " guesses left")
        
        if turns == 0:
            print(hangman[5])
            print("\n*** YOU LOSE! ***")
            print("The word was: " + word)
