import random
import string


def letterChange(passToChange):  # replaces certain letters with symbols
    if 'i' in passToChange:
        passToChange = passToChange.replace(
            passToChange[passToChange.lower().find('i')], "1")

    if 'a' in passToChange:
        passToChange = passToChange.replace(
            passToChange[passToChange.lower().find('a')], "@")

    if 'o' in passToChange:
        passToChange = passToChange.replace(
            passToChange[passToChange.lower().find('o')], "0")

    if 's' in passToChange:
        passToChange = passToChange.replace(
            passToChange[passToChange.lower().find('s')], "$")

    if 'h' in passToChange:
        passToChange = passToChange.replace(
            passToChange[passToChange.lower().find('h')], "#")

    if 'e' in passToChange:
        passToChange = passToChange.replace(
            passToChange[passToChange.lower().find('e')], "3")

    return passToChange


def passphraseGenerator(passphrase1, passphrase2, passphrase3):
    # choices a random number to select a letter at that index number
    randNum1 = random.randint(0, (len(passphrase1) - 1))
    randNum2 = random.randint(0, (len(passphrase2) - 1))
    randNum3 = random.randint(0, (len(passphrase3) - 1))

    # uses the random number as an index in the string and 
    # changes the letter at that index uppercase
    pass1 = passphrase1.replace(
        passphrase1[randNum1], passphrase1[randNum1].upper(), 1)
    pass2 = passphrase2.replace(
        passphrase2[randNum2], passphrase2[randNum2].upper(), 1)
    pass3 = passphrase3.replace(
        passphrase3[randNum3], passphrase3[randNum3].upper(), 1)

    # uses letterChange function to change certain numbers
    finalPass1 = letterChange(pass1)
    finalPass2 = letterChange(pass2)
    finalPass3 = letterChange(pass3)

    # new password is generated
    return finalPass1 + "_" + finalPass2 + "_" + finalPass3


adjectives = ["adorable", "adventurous", "aggressive", "agreeable", "alert", "alive", "amused", "angry", "annoyed", "annoying", "anxious", "arrogant", "ashamed", "attractive", "average", "awful", "bad", "beautiful", "better", "bewildered", "black", "bloody", "blue", "blue-eyed", "blushing", "bored", "brainy", "brave", "breakable", "bright", "busy", "calm", "careful", "cautious", "charming", "cheerful", "clean", "clear", "clever", "cloudy", "clumsy", "colorful", "combative", "comfortable", "concerned", "condemned", "confused", "cooperative", "courageous", "crazy", "creepy", "crowded", "cruel", "curious", "cute", "dangerous", "dark", "dead", "defeated", "defiant", "delightful", "depressed", "determined", "different", "difficult", "disgusted", "distinct", "disturbed", "dizzy", "doubtful", "drab", "dull", "eager", "easy", "elated", "elegant", "embarrassed", "enchanting", "encouraging", "energetic", "enthusiastic", "envious", "evil", "excited", "expensive", "exuberant", "fair", "faithful", "famous", "fancy", "fantastic", "fierce", "filthy", "fine", "foolish", "fragile", "frail", "frantic", "friendly", "frightened", "funny", "gentle", "gifted", "glamorous", "gleaming", "glorious", "good", "gorgeous", "graceful", "grieving", "grotesque",
              "grumpy", "handsome", "happy", "healthy", "helpful", "helpless", "hilarious", "homeless", "homely", "horrible", "hungry", "hurt", "ill", "important", "impossible", "inexpensive", "innocent", "inquisitive", "itchy", "jealous", "jittery", "jolly", "joyous", "kind", "lazy", "light", "lively", "lonely", "long", "lovely", "lucky", "magnificent", "misty", "modern", "motionless", "muddy", "mushy", "mysterious", "nasty", "naughty", "nervous", "nice", "nutty", "obedient", "obnoxious", "odd", "old-fashioned", "open", "outrageous", "outstanding", "panicky", "perfect", "plain", "pleasant", "poised", "poor", "powerful", "precious", "prickly", "proud", "putrid", "puzzled", "quaint", "real", "relieved", "repulsive", "rich", "scary", "selfish", "shiny", "shy", "silly", "sleepy", "smiling", "smoggy", "sore", "sparkling", "splendid", "spotless", "stormy", "strange", "stupid", "successful", "super", "talented", "tame", "tasty", "tender", "tense", "terrible", "thankful", "thoughtful", "thoughtless", "tired", "tough", "troubled", "ugliest", "ugly", "uninterested", "unsightly", "unusual", "upset", "uptight", "vast", "victorious", "vivacious", "wandering", "weary", "wicked", "wide-eyed", "wild", "witty", "worried", "worrisome", "wrong", "zany", "zealous"]
animals = ["weasel", "jerboa", "hedgehog", "walrus", "bear", "pronghorn", "deer", "ape", "anteater", "aoudad", "peccary", "aardvark", "guanaco", "cat", "mandrill", "dingo", "camel", "rhinoceros", "quagga", "fish", "marmoset", "burro", "addax", "owl", "oryx", "otter", "cow", "ermine", "zebra", "crocodile", "bird", "chamois", "wolf", "kangaroo", "baboon", "colt", "deer", "lovebird", "orangutan", "gemsbok", "chicken", "tapir", "shrew", "kitten", "cheetah", "monkey", "elephant", "gazelle",
           "monster", "chinchilla", "pig", "parakeet", "moose", "hartebeest", "skunk", "mongoose", "hyena", "waterbuck", "porcupine", "tiger", "rat", "goat", "antelope", "okapi", "puma", "wombat", "capybara", "coati", "armadillo", "woodchuck", "salamander", "jaguar", "leopard", "ox", "marten", "mustang", "turtle", "mole", "mouse", "bighorn", "eland", "mink", "platypus", "dormouse", "sloth", "cow", "sheep", "opossum", "starfish", "ram", "alligator", "muskrat", "dog", "ocelot", "bison"]
inputCheck = True

# Looks for user choice and loops if the user choose the right input


def passphrase():
    passphrase1 = adjectives[random.randint(0, len(adjectives) - 1)]
    passphrase2 = adjectives[random.randint(0, len(adjectives) - 1)]
    passphrase3 = animals[random.randint(0, len(animals) - 1)]
    return passphraseGenerator(passphrase1, passphrase2, passphrase3)


def password(len, type, upper, lower, nums, symbols):
    length = int(len)
    if type == "say":
        if upper == True and lower == True:
            return str(''.join(random.choices(string.ascii_letters, k=length)))
        elif upper == True:
            return str(''.join(random.choices(string.ascii_uppercase, k=length)))
        else:
            return str(''.join(random.choices(string.ascii_lowercase, k=length)))

    if type == "all":
        if upper == True and lower == True and nums == True and symbols == True:
            return str(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length)))
        elif upper == True and lower == True and nums == True and symbols == False:
            return str(''.join(random.choices(string.ascii_letters + string.digits, k=length)))
        elif upper == True and lower == True and nums == False and symbols == False:
            return str(''.join(random.choices(string.ascii_letters, k=length)))
        elif upper == True and lower == False and nums == False and symbols == False:
            return str(''.join(random.choices(string.ascii_uppercase, k=length)))
        elif upper == True and lower == False and nums == False and symbols == True:
            return str(''.join(random.choices(string.ascii_uppercase + string.punctuation, k=length)))
        elif upper == True and lower == False and nums == True and symbols == False:
            return str(''.join(random.choices(string.ascii_uppercase + string.digits, k=length)))
        elif upper == False and lower == True and nums == False and symbols == False:
            return str(''.join(random.choices(string.ascii_lowercase, k=length)))
        elif upper == False and lower == True and nums == True and symbols == False:
            return str(''.join(random.choices(string.ascii_lowercase + string.digits, k=length)))
        elif upper == False and lower == True and nums == True and symbols == True:
            return str(''.join(random.choices(string.ascii_lowercase + string.digits + string.punctuation, k=length)))
        elif upper == False and lower == False and nums == True and symbols == False:
            return str(''.join(random.choices(string.digits, k=length)))
        elif upper == False and lower == False and nums == True and symbols == True:
            return str(''.join(random.choices(string.digits + string.punctuation, k=length)))
        elif upper == False and lower == False and nums == False and symbols == True:
            return str(''.join(random.choices(string.punctuation, k=length)))
        elif upper == False and lower == True and nums == False and symbols == True:
            return str(''.join(random.choices(string.punctuation + string.ascii_lowercase, k=length)))
        elif upper == True and lower == True and nums == False and symbols == True:
            return str(''.join(random.choices(string.punctuation + string.ascii_letters, k=length)))
        elif upper == True and lower == False and nums == True and symbols == True:
            return str(''.join(random.choices(string.punctuation + string.ascii_uppercase + string.digits, k=length)))
        else:
            return "Please select an Ease of Use Type"
    if type == "read":
        if upper == True and lower == True and nums == True and symbols == True:
            return str(''.join(random.choices('23456789abcdefghijkmnopqrstuvwxyz \
            ABCDEFGHJKLMNPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~', k=length)))
        elif upper == True and lower == True and nums == True and symbols == False:
            return str(''.join(random.choices('23456789abcdefghijkmnopqrstuvwxyz\
            ABCDEFGHJKLMNPQRSTUVWXYZ', k=length)))
        elif upper == True and lower == True and nums == False and symbols == False:
            return str(''.join(random.choices('abcdefghijkmnopqrstuvwxyz\
            ABCDEFGHJKLMNPQRSTUVWXYZ', k=length)))
        elif upper == True and lower == False and nums == False and symbols == False:
            return str(''.join(random.choices('ABCDEFGHJKLMNPQRSTUVWXYZ', k=length)))
        elif upper == True and lower == False and nums == False and symbols == True:
            return str(''.join(random.choices('ABCDEFGHJKLMNPQRSTU\
            VWXYZ!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~', k=length)))
        elif upper == True and lower == False and nums == True and symbols == False:
            return str(''.join(random.choices('23456789ABCDEFGHJK\
            LMNPQRSTUVWXYZ~', k=length)))
        elif upper == False and lower == True and nums == False and symbols == False:
            return str(''.join(random.choices('abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ', k=length)))
        elif upper == False and lower == True and nums == True and symbols == False:
            return str(''.join(random.choices('23456789abcdefghijkmnopqrstuvwxyz', k=length)))
        elif upper == False and lower == True and nums == True and symbols == True:
            return str(''.join(random.choices('23456789abcdefghijkmnopqrstuvw\
            xyz!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~', k=length)))
        elif upper == False and lower == False and nums == True and symbols == False:
            return str(''.join(random.choices('23456789', k=length)))
        elif upper == False and lower == False and nums == True and symbols == True:
            return str(''.join(random.choices('23456789!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~', k=length)))
        elif upper == False and lower == False and nums == False and symbols == True:
            return str(''.join(random.choices(string.punctuation, k=length)))
        elif upper == False and lower == True and nums == False and symbols == True:
            return str(''.join(random.choices('abcdefghijkmnopqrstuvwxyz!"#$%&\'()*+,-./:;\
            <=>?@[\]^_`{|}~', k=length)))
        elif upper == True and lower == True and nums == False and symbols == True:
            return str(''.join(random.choices('ABCDEFGHJKLMNPQRSTUVWXYZ!"#$%&\'()*+,-./:;\
            <=>?@[\]^_`{|}~', k=length)))
        elif upper == True and lower == False and nums == True and symbols == True:
            return str(''.join(random.choices('23456789ABCDEFGHJKLMNPQRSTUVWXYZ!"#$%&\'()*+,\
            -./:;<=>?@[\]^_`{|}~', k=length)))
        else:
            return "Please select an Ease of Use Type"
