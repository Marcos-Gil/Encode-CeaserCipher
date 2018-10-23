# Intro formatting for user
print('=====================')
print('   Ceaser Encoding   ')
print('=====================')

# Assigning required variables and asking user for required inputs to begin
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cipherAlphabet = ''
userKey = input('Please enter an integer between 1 and 25 as your key: ')

# While loop ensuring that the user enters an integer between 1 and 25
while(not userKey.isdigit() or int(userKey)<= 0 or int(userKey)>25):
    print('Sorry, that is invalid. Must enter an integer between 1 and 25. ')
    userKey = input('Please enter an integer between 1 and 25 as your key: ')

# Making userKey into an integer
userKeyInt = int(userKey)

# Print commands so user can see the plaintext alphabet and the ciphertext alphabet
print('Plaintext Alphabet: ',alphabet.upper())
print('Ciphertext Alphabet: ', end = '')

# For loop to go through the alphabet string and change it into ciphertext
for x in alphabet:
    if x in alphabet:
        cipherAlphabet = alphabet[(alphabet.index(x)+userKeyInt)%(len(alphabet))]
        print(cipherAlphabet.upper(), end = '')
        
# Asking user for the word/sentence they want to be encoded then making it all uppercase letters
userSentence = input('\n\nPlease type the string to be encoded: ')
userSentence = userSentence.upper()

# Print commands so user can see the plaintext and ciphertext version of the word/message they entered
print('\nPlaintext: ', userSentence)
print('Ciphertext: ', end ='')

# For loop used to make translate the users word/mesasge into ciphertext
for y in userSentence:
    if y in alphabet:
        b = ord(y) + userKeyInt
        if b > 90:
            b = b - 26
            print(chr(b), end = '')
        else:
            print(chr(b), end = '')
    else:
        print(y, end = '')
print('')