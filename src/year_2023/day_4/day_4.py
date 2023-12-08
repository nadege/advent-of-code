def compute_part1(lines: list[str]) -> int:
    score = 0

    for line in lines:
        line = line.split(": ")[1]
        winning = line.split(" | ")[0].split(" ")
        owned = line.split(" | ")[1].split(" ")
        card_score = 0
        for number in owned:
            if number != "" and number in winning:
                card_score += 1
                    
        score += pow(2, (card_score - 1)) if card_score else 0
        
    return score


def compute_part2(lines: list[str]) -> int:
    score = 0

    # We start with on of each card
    card_quantity = [1] * len(lines)
    
    for i in range(len(lines) - 1, -1, -1):   
        line = lines[i].split(": ")[1]
        winning = line.split(" | ")[0].split(" ")
        owned = line.split(" | ")[1].split(" ")
        card_score = 0
        for number in owned:
            if number != "" and number in winning:
                card_score += 1
            
            #print(f"{lines[i].split(': ')[0]}, number: {number}, score: {card_score}")

        cards_from_below = [card_quantity[i+j] for j in range(1, card_score+1, 1) if i+1 < len(lines)]
        print(f"cards_from_below: {cards_from_below}")
        card_quantity[i] += sum(cards_from_below)


    print(f"card_quantity: {card_quantity}")

    return sum(card_quantity)


def main(lines: list[str]):
    print(f"Part 1: {compute_part1(lines)}")
    print(f"Part 2: {compute_part2(lines)}")
