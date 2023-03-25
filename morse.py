def encode(message):
    """
    This function takes a string message and encodes it into Morse code.
    """
    # Dictionary of Morse code
    morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                  'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
                  'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
                  '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                  '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
    
    # Convert message to uppercase and split into words
    words = message.upper().split()
    
    # Encode each word into Morse code
    encoded_words = []
    for word in words:
        encoded_letters = []
        for letter in word:
            encoded_letters.append(morse_code[letter])
        encoded_words.append(' '.join(encoded_letters))
    
    # Join encoded words with '/' to represent spaces between words
    encoded_message = ' / '.join(encoded_words)
    
    return encoded_message
def decode(message):
    # Dictionary of Morse code (reversed from Task 2)
    morse_code = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
                  '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
                  '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
                  '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0',
                  '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
                  '--...': '7', '---..': '8', '----.': '9'}
    

    # Split message into words and letters
    words = message.split(' / ')
    decoded_words = []  # Rename this variable from 'decoded_letters' to 'decoded_words'
    for word in words:
        letters = word.split()
        decoded_letters = []
        for letter in letters:
            decoded_letters.append(morse_code[letter])
        decoded_words.append(''.join(decoded_letters))

    # Join decoded words into a plain text message and convert it to lowercase
    decoded_message = ' '.join(decoded_words).lower()

    return decoded_message



