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


def decode_line_morze(morse_code):
    line = list(morse_code)
    print(line)
    count = 0
    for i in range(len(line)):
        uni = ''.join(map(str, line[:count + 1]))
        if uni in MORSE_CODE:
            print(MORSE_CODE[uni], end=' ')
            count += 1
            decode_line_morze(morse_code[len(uni):])
        else:
            print('______uni_not_in_dict______')


print(decode_line_morze('.--...'))
#print(decode_line_morze('--.--.--...-..---.-.'))
#print(decode_normal_morze('.... . -.--   .--- ..- -.. .'))