"""
Market-Making & Betting-Game Simulator

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - expected_value
import numpy as np
def expected_value(values, probabilities):
    # convert inputs to numpy arrays for element wise multiplication
    val_array = np.asarray(values, dtype=float)
    prob_array = np.asarray(probabilities, dtype=float)
    
    # calculate ev
    ev = np.sum(val_array*prob_array)

    return float(ev)




    # TODO: return the expected value of the discrete distribution (values, probabilities).
    pass

# Step 2 - one_reroll_die_value
import numpy as np
def one_reroll_die_value(sides):
    values = np.arange(1,sides+1)
    prob = np.full(sides,1/(sides))

    ev1 = expected_value(values, prob)

    reroll_faces = [int(val) for val in values if val < ev1]

    optimal_values = [ev1 if val < ev1 else val for val in values]
    
    value = expected_value(optimal_values,prob)

    return {
        'value': float(value),
        'reroll_faces': sorted(reroll_faces)
    }
            
    


    # TODO: return {'value': expected winnings under optimal reroll policy, 'reroll_faces': sorted faces to reroll}
    pass

# Step 3 - pay_per_reroll_die_game (not yet solved)
# TODO: implement

# Step 4 - red_black_card_game_value (not yet solved)
# TODO: implement

# Step 5 - make_quotes (not yet solved)
# TODO: implement

# Step 6 - execute_trade (not yet solved)
# TODO: implement

# Step 7 - mark_to_market_pnl (not yet solved)
# TODO: implement

# Step 8 - adverse_selection_loss (not yet solved)
# TODO: implement

# Step 9 - uncertainty_spread (not yet solved)
# TODO: implement

# Step 10 - inventory_skewed_quotes (not yet solved)
# TODO: implement

# Step 11 - update_fair_value_from_trade (not yet solved)
# TODO: implement

# Step 12 - update_remaining_card_value (not yet solved)
# TODO: implement

# Step 13 - run_market_making_episode (not yet solved)
# TODO: implement

# Step 14 - summarize_episode_pnls (not yet solved)
# TODO: implement

