def card_value(card):
    card_map = {
        "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7,
        "8" : 8, "9" : 9, "10" : 10, "J" : 11, "Q" : 12, "K" : 13, "A" : 14
    }
    return card_map.get(card, 0) #不存在返回0

def  find_sequences(card_numbers):
    sequences = []
    used = [False] * len(card_numbers)
    for i in range(len(card_numbers)):
        if used[i]:
            continue

        current_sequence = [card_numbers[i]]
        used[i] = True

        for j in range(i+1, len(card_numbers)):
            if used[j]:
                continue
            if card_numbers[j] == current_sequence[-1] + 1:
                current_sequence.append(card_numbers[j])
                used[j] = True
            elif card_numbers[j] >= current_sequence[-1] + 1:
                break
        
        if len(current_sequence) >= 5:
            sequences.append(current_sequence)
        else:
            for num in current_sequence:
                used[card_numbers.index(num)] = False
    return sequences

def main():
    input_cards = input().split()

    card_numbers = [card_value(card) for card in input_cards if card_value(card) != 0]
    card_numbers.sort()

    sequences = find_sequences(card_numbers)

    if not sequences:
        print("No")
    else:
        for seq in sequences:
            output = []
            for value in seq:
                if value == 11:
                    output.append("J")
                elif value == 12:
                    output.append("Q")
                elif value == 13:
                    output.append("K")
                elif value == 14:
                    output.append("A")
                else:
                    output.append(str(value))
            print(' '.join(output))

if __name__ == "__main__":
    main()