# Caesar Cipher Encoding and Decoding

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
again="yes"
while again=="yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  def caesar(text,shift,direction):
    ed_text=""
    if direction=="decode":
      shift*= -1
    for char in text:
      if char in text:
        position = alphabet.index(char)
        if shift>26:
          shift %= 26
        new_position = position + shift
        ed_text += alphabet[new_position]
      else:
        ed_text+=char
    print(f"The {direction}d text is {ed_text}")

  caesar(text,shift,direction)
  again=input("Type 'yes' if you want to go again, otherwise type 'no'.\n")