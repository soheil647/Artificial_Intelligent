from code import Decoder

encoded_text = open("./Attachment/encoded_text.txt").read()
d = Decoder(encoded_text)
decoded_text = d.decode()
print(decoded_text)
