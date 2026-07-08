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

# Step 3 - pay_per_reroll_die_game
import numpy as np
def pay_per_reroll_die_game(sides, reroll_cost):
    
    best_value = -float('inf')
    best_threshold = None
    
    # calculate optimal value for every k and select the largest

    for k in range(1,sides+1):
        keep_sum = sum(range(k,sides+1))
        reroll_faces = k-1

        numerator = keep_sum - (reroll_faces*reroll_cost)
        denominator = sides - reroll_faces
        curr_value = numerator/denominator
        
        if curr_value > best_value:
            best_value = curr_value
            best_threshold = k 
    return {
        'threshold': int(best_threshold),
        'value': float(best_value)
    }        


    # TODO: return {'threshold': t, 'value': V} for the pay-per-reroll die game under the optimal threshold policy.
    pass

# Step 4 - red_black_card_game_value
import numpy as np
def red_black_card_game_value(num_red, num_black):
    """
    Calculates the expected payout of the red-black card game under optimal play
    using dynamic programming.
    
    Returns a dict: {'value': float, 'stop_now': bool}
    """
    # Create a 2D grid to store the optimal value at each (r, b) state
    dp = np.zeros((num_red + 1, num_black + 1))
    
    # Fill the DP table iteratively
    for r in range(num_red + 1):
        for b in range(num_black + 1):
            if r == 0 and b == 0:
                continue
                
            total_cards = r + b
            ev_draw = 0.0
            
            # If we draw a red card
            if r > 0:
                ev_draw += (r / total_cards) * (1.0 + dp[r - 1, b])
                
            # If we draw a black card
            if b > 0:
                ev_draw += (b / total_cards) * (-1.0 + dp[r, b - 1])
                
            # Optimal choice: choose between drawing or stopping (0)
            dp[r, b] = max(0.0, ev_draw)
            
    # Determine the initial step action from the full deck state
    # We re-calculate the draw value at the start to check for ties/stopping
    initial_total = num_red + num_black
    if initial_total == 0:
        return {'value': 0.0, 'stop_now': True}
        
    initial_ev_draw = 0.0
    if num_red > 0:
        initial_ev_draw += (num_red / initial_total) * (1.0 + dp[num_red - 1, num_black])
    if num_black > 0:
        initial_ev_draw += (num_black / initial_total) * (-1.0 + dp[num_red, num_black - 1])
        
    # As per the rules: ties (continuation value <= 0) resolve as stopping
    stop_now = initial_ev_draw <= 0.0
    final_value = dp[num_red, num_black]
    
    return {
        'value': float(final_value),
        'stop_now': bool(stop_now)
    }
           

    

    # TODO: return {'value': expected payout under optimal stopping, 'stop_now': whether to stop immediately}.
    pass

# Step 5 - make_quotes
def make_quotes(fair_value, spread_width):
    bid = fair_value - (spread_width)/2
    ask = fair_value + (spread_width)/2
    return {
        'bid': float(bid),
        'ask': float(ask)
    }
    # TODO: return a dict with 'bid' and 'ask' symmetric around fair_value with total width spread_width
    pass

# Step 6 - execute_trade
def execute_trade(state, side, bid, ask, size=1):

    if side =='buy':
        cash = state["cash"] + ask * size
        inventory = state["inventory"] - size
    elif side =='sell':
        cash = state["cash"] - bid * size
        inventory = state["inventory"] + size

    return {
        'cash': float(cash),
        'inventory': float(inventory)
    }        
    # TODO: apply a counterparty trade against your bid/ask and return updated state
    pass

# Step 7 - mark_to_market_pnl
def mark_to_market_pnl(cash, inventory, settlement_value):
    pnl = cash + (inventory * settlement_value)
    return float(pnl)
    # TODO: return total P&L given cash, remaining inventory, and settlement value.
    pass

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

