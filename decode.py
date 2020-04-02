from morze_dict import MORSE_CODE


def decode_normal_morze(morse_code):
    line = [i.split(' ') for i in morse_code.strip().split('   ')]
    print(line)
    for i in range(len(line)):
        for j in range(len(line[i])):
            line[i][j] = MORSE_CODE[line[i][j]]
    output_text = ' '.join(map(str, [''.join(map(str, line[i])) for i in range(len(line))]))
    print(output_text)
    return output_text


def letters(morse_code):
    output = []
    count = 0
    for i in range(len(morse_code)):
        symbols = morse_code[:count + 1]
        if symbols in MORSE_CODE:
            output.append(MORSE_CODE[symbols])
            count += 1
    return output


print(letters('.--...'))
#print(decode_line_morze('--.--.--...-..---.-.'))
#print(decode_normal_morze('.... . -.--   .--- ..- -.. .'))