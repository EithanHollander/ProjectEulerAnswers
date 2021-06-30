from enum import IntEnum, Enum

if __name__ == '__main__':
    poker_values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    poker_suits = ["H", "S", "C", "D"]

    class PokerHandRanking(IntEnum):
        HighCard = 1
        OnePair = 2
        TwoPairs = 3
        ThreeOfAKind = 4
        Straight = 5
        Flush = 6
        FullHouse = 7
        FourOfAKind = 8
        StraightFlush = 9
        RoyalFlush = 10

    class PokerCard:
        def __init__(self, str_of_value_and_suit):
            self.value = str_of_value_and_suit[0].upper()
            self.suit = str_of_value_and_suit[1].upper()

        def __lt__(self, another_card):
            return poker_values.index(self.value) < poker_values.index(another_card.value)

        def __gt__(self, another_card):
            return poker_values.index(self.value) > poker_values.index(another_card.value)

        def __eq__(self, another_card):
            return poker_values.index(self.value) == poker_values.index(another_card.value)

        def __repr__(self):
            return self.value + self.suit

    def determine_which_ranking(poker_hand):
        poker_hand = sorted(poker_hand)
        all_same_suit = poker_hand[0].suit == poker_hand[1].suit == poker_hand[2].suit == poker_hand[3].suit == poker_hand[4].suit
        how_many_of_each_value = [[card.value for card in poker_hand].count(value) for value in poker_values]
        if how_many_of_each_value[poker_values.index("T")] == 1 and \
            how_many_of_each_value[poker_values.index("J")] == 1 and \
            how_many_of_each_value[poker_values.index("Q")] == 1 and \
            how_many_of_each_value[poker_values.index("K")] == 1 and \
            how_many_of_each_value[poker_values.index("K")] == 1 and \
            all_same_suit:
            return PokerHandRanking.RoyalFlush, how_many_of_each_value
        if poker_values.index(poker_hand[0].value) + 1 == poker_values.index(poker_hand[1].value) and \
            poker_values.index(poker_hand[1].value) + 1 == poker_values.index(poker_hand[2].value) and \
            poker_values.index(poker_hand[2].value) + 1 == poker_values.index(poker_hand[3].value) and \
            poker_values.index(poker_hand[3].value) + 1 == poker_values.index(poker_hand[4].value):

            if all_same_suit:
                return PokerHandRanking.StraightFlush, how_many_of_each_value
            else:
                return PokerHandRanking.Straight, how_many_of_each_value
        if how_many_of_each_value.count(4) == 1:
            return PokerHandRanking.FourOfAKind, how_many_of_each_value
        if how_many_of_each_value.count(3) == 1 and \
            how_many_of_each_value.count(2) == 1:
            return PokerHandRanking.FullHouse, how_many_of_each_value
        if all_same_suit:
            return PokerHandRanking.Flush, how_many_of_each_value
        if how_many_of_each_value.count(3) == 1:
            return PokerHandRanking.ThreeOfAKind, how_many_of_each_value
        if how_many_of_each_value.count(2) == 2:
            return PokerHandRanking.TwoPairs, how_many_of_each_value
        if how_many_of_each_value.count(2) == 1:
            return PokerHandRanking.OnePair, how_many_of_each_value
        return PokerHandRanking.HighCard, how_many_of_each_value

    def does_first_hand_win_when_equal(poker_hand_1, values_amounts_1, poker_hand_2, values_amounts_2, ranking):
        if ranking == PokerHandRanking.HighCard or \
            ranking == PokerHandRanking.Flush:
            for position_in_hand in range(4, -1, -1):
                if poker_hand_1[position_in_hand] > poker_hand_2[position_in_hand]:
                    return True
                if poker_hand_1[position_in_hand] < poker_hand_2[position_in_hand]:
                    return False
            # Shouldn't ever come here because the hands are promised to not be totally equal but just for the good code
            return True

        if ranking == PokerHandRanking.OnePair:
            value_1_placement_which_has_the_pair = values_amounts_1.index(2)
            value_2_placement_which_has_the_pair = values_amounts_2.index(2)
            if value_1_placement_which_has_the_pair > value_2_placement_which_has_the_pair:
                return True
            elif value_1_placement_which_has_the_pair < value_2_placement_which_has_the_pair:
                return False
            for position_in_hand in range(4, -1, -1):
                if poker_hand_1[position_in_hand] > poker_hand_2[position_in_hand]:
                    return True
                if poker_hand_1[position_in_hand] < poker_hand_2[position_in_hand]:
                    return False
            # Shouldn't ever come here because the hands are promised to not be totally equal but just for the good code
            return True

        if ranking == PokerHandRanking.TwoPairs:
            have_we_found_first_pair_in_hand_1 = have_we_found_first_pair_in_hand_2 = False
            for card in poker_hand_1:
                if values_amounts_1[card.value] == 1:
                    value_1_which_is_the_high_card = card.value
                elif values_amounts_1[card.value] == 2:
                    if not have_we_found_first_pair_in_hand_1:
                            have_we_found_first_pair_in_hand_1 = True
                            smaller_value_1_which_has_the_pair = card.value
                    else:
                        bigger_value_1_which_has_the_pair = card.value

            for card in poker_hand_2:
                if values_amounts_2[card.value] == 1:
                    value_2_which_is_the_high_card = card.value
                elif values_amounts_2[card.value] == 2:
                    if not have_we_found_first_pair_in_hand_2:
                            have_we_found_first_pair_in_hand_2 = True
                            smaller_value_2_which_has_the_pair = card.value
                    else:
                        bigger_value_2_which_has_the_pair = card.value

            if poker_values.index(bigger_value_1_which_has_the_pair) > poker_values.index(bigger_value_2_which_has_the_pair):
                return True
            if poker_values.index(bigger_value_1_which_has_the_pair) < poker_values.index(bigger_value_2_which_has_the_pair):
                return False
            if poker_values.index(smaller_value_1_which_has_the_pair) > poker_values.index(smaller_value_2_which_has_the_pair):
                return True
            if poker_values.index(smaller_value_1_which_has_the_pair) < poker_values.index(smaller_value_2_which_has_the_pair):
                return False
            if poker_values.index(value_1_which_is_the_high_card) > poker_values.index(value_2_which_is_the_high_card):
                return True
            if poker_values.index(value_1_which_is_the_high_card) < poker_values.index(value_2_which_is_the_high_card):
                return False
            #  Shouldn't ever come here because the hands are promised to not be totally equal but just for the good code
            return True

        if ranking == PokerHandRanking.ThreeOfAKind:
            value_1_placement_which_has_the_three = values_amounts_1.index(3)
            value_2_placement_which_has_the_three = values_amounts_2.index(3)
            if value_1_placement_which_has_the_three > value_2_placement_which_has_the_three:
                return True
            elif value_1_placement_which_has_the_three < value_2_placement_which_has_the_three:
                return False
            for position_in_hand in range(4, -1, -1):
                if poker_hand_1[position_in_hand] > poker_hand_2[position_in_hand]:
                    return True
                if poker_hand_1[position_in_hand] < poker_hand_2[position_in_hand]:
                    return False
            # Shouldn't ever come here because the hands are promised to not be totally equal but just for the good code
            return True

        if ranking == PokerHandRanking.FullHouse:
            value_1_placement_which_has_the_pair = values_amounts_1.index(2)
            value_1_placement_which_has_the_three = values_amounts_1.index(3)

            value_2_placement_which_has_the_pair = values_amounts_2.index(2)
            value_2_placement_which_has_the_three = values_amounts_2.index(3)

            if value_1_placement_which_has_the_three > value_2_placement_which_has_the_three:
                return True
            if value_1_placement_which_has_the_three < value_2_placement_which_has_the_three:
                return True
            if value_1_placement_which_has_the_pair > value_2_placement_which_has_the_pair:
                return True
            if value_1_placement_which_has_the_pair < value_2_placement_which_has_the_pair:
                return True
            # Shouldn't ever come here because the hands are promised to not be totally equal but just for the good code
            return True

        if ranking == PokerHandRanking.FourOfAKind:
            value_1_placement_which_has_the_high = values_amounts_1.index(1)
            value_1_placement_which_has_the_four = values_amounts_1.index(4)

            value_2_placement_which_has_the_high = values_amounts_2.index(1)
            value_2_placement_which_has_the_four = values_amounts_2.index(4)

            if value_1_placement_which_has_the_four > value_2_placement_which_has_the_four:
                return True
            if value_1_placement_which_has_the_four < value_2_placement_which_has_the_four:
                return True
            if value_1_placement_which_has_the_high > value_2_placement_which_has_the_high:
                return True
            if value_1_placement_which_has_the_high < value_2_placement_which_has_the_high:
                return True
            # Shouldn't ever come here because the hands are promised to not be totally equal but just for the good code
            return True

        if ranking == PokerHandRanking.Straight or \
            ranking == PokerHandRanking.StraightFlush:
            if poker_hand_1[-1] < poker_hand_2[-1]:
                return False
            # Shouldn't ever come here because the hands are promised to not be totally equal but just for the good code
            return True

        #  if ranking == PokerHandRanking.RoyalFlush Shouldn't happen
        #  because the hands are promised to not be totally equal but just for the good code
        return True


    def does_first_hand_win(sorted_poker_hand_1, sorted_poker_hand_2):
        ranking_1, values_amounts_1 = determine_which_ranking(sorted_poker_hand_1)
        ranking_2, values_amounts_2 = determine_which_ranking(sorted_poker_hand_2)
        if ranking_1 > ranking_2:
            return True
        if ranking_1 < ranking_2:
            return False
        return does_first_hand_win_when_equal(sorted_poker_hand_1, values_amounts_1, sorted_poker_hand_2, values_amounts_2, ranking_1)

    how_many_games_did_player1_win = 0
    with open("problem_54_hands.txt") as hands:
        all_hands_raw = []
        for line in hands.readlines():
            raw_cards = line.split(" ")
            player1_hand = sorted([PokerCard(raw_card) for raw_card in raw_cards[:5]])
            player2_hand = sorted([PokerCard(raw_card) for raw_card in raw_cards[5:10]])
            if does_first_hand_win(player1_hand, player2_hand):
                how_many_games_did_player1_win += 1
        print(how_many_games_did_player1_win)