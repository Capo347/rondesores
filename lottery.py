# Rondesores Lottery Generator
# Use the last eleven saved drawings to create a new selection.

import random  # Provide random selection from our historical number pools.


# Return five main numbers and one separate ball for the selected game.
def generate_numbers(game):  # Receive the game identified by Rondesores.
    game = game.strip().lower().replace(" ", "_")  # Normalize its name.

    if game == "superlotto_plus":  # Select SuperLotto Plus.
        history = SUPERLOTTO_HISTORY  # Use its saved drawing results.
        special_name = "Mega"  # Identify its separate ball.

    elif game == "powerball":  # Select Powerball.
        history = POWERBALL_HISTORY  # Use its saved drawing results.
        special_name = "Powerball"  # Identify its separate ball.

    elif game == "mega_millions":  # Select Mega Millions.
        history = MEGA_MILLIONS_HISTORY  # Use its saved drawing results.
        special_name = "Mega Ball"  # Identify its separate ball.

    else:  # Handle an unrecognized game.
        raise ValueError("Choose SuperLotto Plus, Powerball, or Mega Millions.")  # Explain valid choices.

    recent_draws = history[-11:]  # Select the eleven newest saved drawings.
    main_pool = set()  # Collect distinct main numbers from those drawings.
    special_pool = set()  # Collect their separate balls in a different pool.

    for main_numbers, special_ball in recent_draws:  # Examine all six numbers in each drawing.
        main_pool.update(main_numbers)  # Add its five main numbers without duplicates.
        special_pool.add(special_ball)  # Add its separate ball to the separate pool.

    numbers = sorted(random.sample(sorted(main_pool), 5))  # Select five distinct historical main numbers.
    special_ball = random.choice(sorted(special_pool))  # Select one historical separate ball.

    return {  # Supply the generated selection to Rondesores.
        "game": game,  # Identify the game.
        "numbers": numbers,  # Supply the five selected main numbers.
        "special_name": special_name,  # Label the separate ball.
        "special_ball": special_ball,  # Supply its selected value.
    }

    # Keep the real SuperLotto Plus results from oldest to newest.
# Format: ([five main numbers], separate Mega number).
SUPERLOTTO_HISTORY = [
    ([1, 9, 17, 34, 38], 20),  # May 20, 2026.
    ([10, 15, 18, 27, 33], 16),  # May 23, 2026.
    ([3, 8, 36, 45, 46], 6),  # May 27, 2026.
    ([1, 2, 22, 26, 27], 21),  # May 30, 2026.
    ([3, 15, 17, 36, 41], 13),  # June 3, 2026.
    ([5, 8, 10, 22, 45], 4),  # June 6, 2026.
    ([3, 16, 22, 29, 42], 5),  # June 10, 2026.
    ([12, 14, 38, 41, 43], 13),  # June 13, 2026.
    ([4, 6, 22, 23, 40], 6),  # June 17, 2026.
    ([4, 7, 20, 33, 43], 21),  # June 20, 2026.
    ([14, 19, 23, 32, 39], 17),  # June 24, 2026.
    ([16, 21, 22, 25, 34], 27),  # June 27, 2026.
    ([2, 17, 24, 31, 35], 5),  # July 1, 2026.
    ([11, 18, 21, 23, 38], 10),  # July 4, 2026.
    ([18, 22, 28, 33, 38], 15),  # July 8, 2026.
    ([1, 4, 21, 36, 44], 20),  # July 11, 2026.
    ([2, 5, 34, 36, 37], 3),  # July 15, 2026.
    ([2, 3, 10, 27, 37], 7),  # July 18, 2026.
    ([5, 16, 29, 30, 35], 17),  # July 22, 2026.
    ([3, 27, 28, 29, 34], 12),  # July 25, 2026.
    ([5, 13, 19, 22, 27], 7),  # July 29, 2026.
    ([29, 30, 37, 41, 44], 18),  # August 1, 2026.
    ([2, 4, 9, 13, 20], 5),  # August 5, 2026.
    ([1, 23, 25, 40, 46], 11),  # August 8, 2026.
    ([3, 4, 14, 35, 40], 20),  # August 12, 2026.
    ([6, 8, 17, 18, 31], 19),  # August 15, 2026.
    ([4, 12, 18, 34, 36], 13),  # August 19, 2026.
    ([11, 16, 21, 28, 37], 19),  # August 22, 2026.
    ([25, 26, 30, 37, 38], 23),  # August 26, 2026.
    ([2, 6, 7, 35, 44], 13),  # August 29, 2026.
    ([12, 17, 18, 35, 40], 9),  # September 2, 2026.
    ([8, 9, 19, 38, 42], 16),  # September 5, 2026.
    ([9, 24, 28, 34, 41], 6),  # September 9, 2026.
    ([13, 26, 29, 35, 47], 8),  # September 12, 2026.
    ([26, 28, 33, 35, 41], 16),  # September 16, 2026.
    ([9, 11, 12, 14, 30], 21),  # September 19, 2026.
    ([13, 20, 29, 30, 45], 13),  # September 23, 2026.
    ([1, 9, 26, 35, 36], 27),  # September 26, 2026.
    ([2, 10, 12, 23, 39], 2),  # September 30, 2026.
    ([14, 19, 23, 26, 33], 25),  # October 3, 2026.
    ([19, 25, 27, 33, 37], 9),  # October 7, 2026.
    ([1, 5, 23, 34, 47], 27),  # October 10, 2026.
    ([7, 18, 23, 46, 47], 12),  # October 14, 2026.
    ([3, 25, 27, 29, 37], 17),  # October 17, 2026.
]

# Count main numbers and special balls in their separate pools.
def count_numbers(history, main_limit, special_limit):  # Receive results and game limits.
    main_counts = {}  # Store each main number's appearance count.
    special_counts = {}  # Store each special ball's appearance count.

    for number in range(1, main_limit + 1):  # Visit every allowed main number.
        main_counts[number] = 0  # Begin its count at zero.

    for number in range(1, special_limit + 1):  # Visit every allowed special ball.
        special_counts[number] = 0  # Begin its count at zero.

    for main_numbers, special_ball in history:  # Read one historical drawing.
        for number in main_numbers:  # Read its five main numbers individually.
            main_counts[number] += 1  # Record this main number's appearance.
        special_counts[special_ball] += 1  # Record the separate ball's appearance.

    return main_counts, special_counts  # Return both completed counts.

# Measure how many draws have passed since each number last appeared.
def find_gaps(history, main_limit, special_limit):  # Receive the history and game limits.
    main_gaps = {}  # Store gaps for the five-main-number pool.
    special_gaps = {}  # Store gaps for the separate-ball pool.

    for number in range(1, main_limit + 1):  # Visit every allowed main number.
        main_gaps[number] = None  # Mark it as unseen until an appearance is found.

    for number in range(1, special_limit + 1):  # Visit every allowed special ball.
        special_gaps[number] = None  # Mark it as unseen until an appearance is found.

    for gap, draw in enumerate(reversed(history)):  # Read newest first, counting from zero.
        main_numbers, special_ball = draw  # Separate the main numbers from the special ball.

        for number in main_numbers:  # Examine each main number in this drawing.
            if main_gaps[number] is None:  # Record only its most recent appearance.
                main_gaps[number] = gap  # Store the number of draws since that appearance.

        if special_gaps[special_ball] is None:  # Record this special ball's latest appearance.
            special_gaps[special_ball] = gap  # Store its gap separately.

    return main_gaps, special_gaps  # Return both sets of calculated gaps.

# Count how often each pair of main numbers appeared together.
def count_pairs(history):  # Receive the saved drawing history.
    pair_counts = {}  # Store each pair and its appearance count.

    for main_numbers, _special_ball in history:  # Read the main numbers; exclude the special ball.
        numbers = sorted(main_numbers)  # Give every pair a consistent smaller-first order.

        for first in range(len(numbers) - 1):  # Select the first number's position.
            for second in range(first + 1, len(numbers)):  # Select each later position once.
                pair = (numbers[first], numbers[second])  # Form the two-number pair.
                pair_counts[pair] = pair_counts.get(pair, 0) + 1  # Add one appearance.

    return pair_counts  # Return all observed pairs and their counts.

# Describe the number patterns found in each historical drawing.
def analyze_patterns(history):  # Receive the saved drawing history.
    patterns = []  # Collect the results for each drawing.

    for main_numbers, _special_ball in history:  # Analyze only the five main numbers.
        numbers = sorted(main_numbers)  # Arrange the numbers from smallest to largest.
        total = sum(numbers)  # Add the five main numbers together.
        odd_count = 0  # Begin counting odd numbers.
        consecutive_pairs = []  # Collect neighboring numbers such as 25 and 26.

        for number in numbers:  # Examine each main number.
            if number % 2 != 0:  # Check whether division by two leaves a remainder.
                odd_count += 1  # Count this number as odd.

        even_count = len(numbers) - odd_count  # Count the remaining numbers as even.

        for position in range(len(numbers) - 1):  # Compare neighboring positions.
            if numbers[position + 1] == numbers[position] + 1:  # Check for consecutive values.
                consecutive_pairs.append((numbers[position], numbers[position + 1]))  # Save the pair.

        patterns.append({  # Store this drawing's calculated results.
            "numbers": numbers,  # Identify the five main numbers.
            "total": total,  # Record their sum.
            "odd_count": odd_count,  # Record how many are odd.
            "even_count": even_count,  # Record how many are even.
            "consecutive_pairs": consecutive_pairs,  # Record any consecutive pairs.
        })

    return patterns  # Return the descriptions in the same order as the history.

# Gather the historical calculations into one result for Rondesores.
def analyze_history(history, main_limit, special_limit):  # Receive the drawings and game limits.
    main_counts, special_counts = count_numbers(history, main_limit, special_limit)  # Count appearances.
    main_gaps, special_gaps = find_gaps(history, main_limit, special_limit)  # Calculate appearance gaps.
    pairs = count_pairs(history)  # Count main numbers that appeared together.
    patterns = analyze_patterns(history)  # Calculate totals, odd/even counts, and consecutive pairs.

    return {  # Return all calculations together with descriptive labels.
        "draw_count": len(history),  # Identify how many drawings were analyzed.
        "main_counts": main_counts,  # Include main-number appearance counts.
        "special_counts": special_counts,  # Include separate-ball appearance counts.
        "main_gaps": main_gaps,  # Include draws since each main number appeared.
        "special_gaps": special_gaps,  # Include draws since each special ball appeared.
        "pairs": pairs,  # Include pair appearance counts.
        "patterns": patterns,  # Include the description of each drawing.
    }

# Store the 66 collected Powerball drawings, oldest first.
# Format: ([five main numbers], separate Powerball number).
POWERBALL_HISTORY = [
    ([4, 13, 34, 61, 65], 12),  # May 18, 2026.
    ([10, 28, 30, 46, 57], 25),  # May 20, 2026.
    ([4, 16, 41, 48, 66], 26),  # May 23, 2026.
    ([17, 32, 48, 60, 64], 10),  # May 25, 2026.
    ([5, 14, 21, 31, 51], 13),  # May 27, 2026.
    ([1, 27, 35, 44, 52], 12),  # May 30, 2026.
    ([2, 42, 47, 57, 58], 14),  # June 1, 2026.
    ([14, 16, 38, 55, 64], 12),  # June 3, 2026.
    ([16, 32, 55, 59, 64], 3),  # June 6, 2026.
    ([3, 24, 34, 43, 49], 20),  # June 8, 2026.
    ([12, 31, 38, 60, 66], 14),  # June 10, 2026.
    ([3, 13, 44, 50, 53], 2),  # June 13, 2026.
    ([25, 55, 57, 60, 62], 23),  # June 15, 2026.
    ([3, 26, 49, 53, 61], 12),  # June 17, 2026.
    ([16, 20, 44, 48, 50], 15),  # June 20, 2026.
    ([17, 19, 21, 45, 48], 13),  # June 22, 2026.
    ([13, 14, 16, 21, 38], 14),  # June 24, 2026.
    ([3, 16, 28, 30, 59], 11),  # June 27, 2026.
    ([10, 14, 41, 53, 59], 3),  # June 29, 2026.
    ([2, 6, 26, 39, 68], 6),  # July 1, 2026.
    ([17, 38, 46, 50, 69], 20),  # July 4, 2026.
    ([17, 44, 63, 66, 67], 4),  # July 6, 2026.
    ([12, 29, 37, 43, 55], 18),  # July 8, 2026.
    ([8, 10, 14, 45, 59], 5),  # July 11, 2026.
    ([5, 25, 36, 40, 48], 3),  # July 13, 2026.
    ([2, 7, 18, 29, 38], 16),  # July 15, 2026.
    ([9, 14, 44, 50, 56], 3),  # July 18, 2026.
    ([2, 9, 44, 53, 59], 8),  # July 20, 2026.
    ([4, 5, 22, 50, 58], 1),  # July 22, 2026.
    ([3, 4, 24, 36, 47], 17),  # July 25, 2026.
    ([6, 26, 46, 58, 65], 25),  # July 27, 2026.
    ([30, 36, 40, 42, 57], 2),  # July 29, 2026.
    ([6, 17, 27, 48, 50], 5),  # August 1, 2026.
    ([8, 30, 41, 48, 54], 4),  # August 3, 2026.
    ([14, 20, 59, 60, 61], 25),  # August 5, 2026.
    ([5, 9, 35, 54, 63], 7),  # August 8, 2026.
    ([6, 37, 54, 55, 64], 10),  # August 10, 2026.
    ([4, 26, 66, 67, 69], 9),  # August 12, 2026.
    ([5, 8, 27, 29, 63], 13),  # August 15, 2026.
    ([8, 15, 25, 49, 65], 22),  # August 17, 2026.
    ([10, 21, 58, 61, 64], 17),  # August 19, 2026.
    ([13, 31, 54, 57, 65], 23),  # August 22, 2026.
    ([3, 16, 33, 38, 68], 2),  # August 24, 2026.
    ([12, 32, 45, 50, 58], 2),  # August 26, 2026.
    ([18, 56, 62, 65, 67], 18),  # August 29, 2026.
    ([11, 17, 25, 37, 49], 10),  # August 31, 2026.
    ([3, 10, 29, 58, 64], 14),  # September 2, 2026.
    ([15, 40, 47, 53, 59], 9),  # September 5, 2026.
    ([15, 19, 28, 39, 56], 3),  # September 7, 2026.
    ([9, 40, 42, 55, 65], 23),  # September 9, 2026.
    ([14, 16, 23, 58, 69], 3),  # September 12, 2026.
    ([19, 20, 57, 61, 67], 22),  # September 14, 2026.
    ([2, 21, 24, 25, 64], 7),  # September 16, 2026.
    ([18, 30, 41, 45, 68], 10),  # September 19, 2026.
    ([2, 7, 9, 17, 58], 20),  # September 21, 2026.
    ([5, 15, 26, 29, 30], 14),  # September 23, 2026.
    ([14, 40, 52, 55, 57], 24),  # September 26, 2026.
    ([17, 21, 29, 42, 49], 7),  # September 28, 2026.
    ([4, 6, 23, 33, 44], 13),  # September 30, 2026.
    ([4, 42, 44, 55, 59], 14),  # October 3, 2026.
    ([16, 23, 32, 36, 54], 9),  # October 5, 2026.
    ([11, 13, 14, 21, 65], 19),  # October 7, 2026.
    ([1, 4, 19, 33, 51], 15),  # October 10, 2026.
    ([22, 28, 38, 51, 69], 9),  # October 12, 2026.
    ([3, 34, 37, 42, 46], 20),  # October 14, 2026.
    ([12, 13, 24, 32, 35], 11),  # October 17, 2026.
]

# Store the 44 collected Mega Millions drawings, oldest first.
# Format: ([five main numbers], separate Mega Ball number).
MEGA_MILLIONS_HISTORY = [
    ([10, 26, 34, 56, 64], 6),  # May 19, 2026.
    ([3, 22, 34, 54, 61], 8),  # May 22, 2026.
    ([1, 5, 49, 51, 59], 7),  # May 26, 2026.
    ([19, 24, 47, 59, 65], 7),  # May 29, 2026.
    ([15, 26, 43, 48, 60], 12),  # June 2, 2026.
    ([13, 30, 50, 52, 66], 2),  # June 5, 2026.
    ([9, 30, 36, 38, 40], 3),  # June 9, 2026.
    ([9, 17, 24, 39, 51], 3),  # June 12, 2026.
    ([12, 20, 53, 67, 70], 12),  # June 16, 2026.
    ([13, 16, 21, 26, 50], 12),  # June 19, 2026.
    ([48, 51, 60, 63, 66], 20),  # June 23, 2026.
    ([5, 13, 30, 33, 52], 6),  # June 26, 2026.
    ([26, 41, 50, 53, 62], 12),  # June 30, 2026.
    ([5, 9, 29, 47, 57], 16),  # July 3, 2026.
    ([2, 31, 35, 36, 63], 12),  # July 7, 2026.
    ([2, 39, 44, 46, 56], 23),  # July 10, 2026.
    ([2, 4, 10, 48, 56], 22),  # July 14, 2026.
    ([22, 34, 45, 48, 55], 14),  # July 17, 2026.
    ([25, 37, 59, 68, 70], 10),  # July 21, 2026.
    ([2, 5, 42, 44, 60], 1),  # July 24, 2026.
    ([34, 48, 49, 59, 70], 12),  # July 28, 2026.
    ([4, 18, 26, 43, 51], 4),  # July 31, 2026.
    ([14, 21, 51, 55, 65], 21),  # August 4, 2026.
    ([17, 20, 32, 54, 57], 23),  # August 7, 2026.
    ([1, 20, 30, 46, 68], 17),  # August 11, 2026.
    ([3, 23, 27, 46, 60], 11),  # August 14, 2026.
    ([5, 19, 30, 38, 59], 12),  # August 18, 2026.
    ([1, 25, 34, 48, 57], 24),  # August 21, 2026.
    ([7, 10, 47, 48, 50], 14),  # August 25, 2026.
    ([8, 17, 29, 42, 55], 2),  # August 28, 2026.
    ([1, 22, 51, 61, 63], 17),  # September 1, 2026.
    ([6, 26, 34, 59, 61], 24),  # September 4, 2026.
    ([17, 30, 43, 58, 66], 20),  # September 8, 2026.
    ([3, 30, 33, 53, 62], 22),  # September 11, 2026.
    ([27, 36, 43, 57, 58], 16),  # September 15, 2026.
    ([4, 9, 24, 56, 68], 1),  # September 18, 2026.
    ([7, 13, 26, 37, 68], 8),  # September 22, 2026.
    ([25, 57, 58, 67, 68], 16),  # September 25, 2026.
    ([10, 15, 16, 27, 64], 23),  # September 29, 2026.
    ([6, 37, 40, 41, 55], 10),  # October 2, 2026.
    ([26, 32, 42, 51, 54], 22),  # October 6, 2026.
    ([2, 7, 16, 63, 70], 8),  # October 9, 2026.
    ([11, 12, 15, 40, 66], 17),  # October 13, 2026.
    ([2, 15, 31, 41, 68], 11),  # October 16, 2026.
]

# Select a game's history and return its complete analysis.
def get_lottery_analysis(game):  # Receive the game requested by Rondesores.
    game = game.strip().lower().replace(" ", "_")  # Normalize the game name.

    if game == "superlotto_plus":  # Select SuperLotto Plus history and limits.
        return analyze_history(SUPERLOTTO_HISTORY, 47, 27)  # Return its historical calculations.

    elif game == "powerball":  # Select Powerball history and limits.
        return analyze_history(POWERBALL_HISTORY, 69, 26)  # Return its historical calculations.

    elif game == "mega_millions":  # Select Mega Millions history and limits.
        return analyze_history(MEGA_MILLIONS_HISTORY, 70, 24)  # Return its historical calculations.

    else:  # Handle an unsupported game name.
        raise ValueError("Choose SuperLotto Plus, Powerball, or Mega Millions.")  # Explain valid choices.
    

# Prepare the lottery response that Rondesores will display.
def lottery_reply(game, previous_reply=""):  # Receive the game and previous response.
    for attempt in range(100):  # Allow up to 100 attempts to produce a different selection.
        result = generate_numbers(game)  # Generate using the game's last eleven saved drawings.
        title = result["game"].replace("_", " ").title()  # Create a readable game label.
        numbers = ", ".join(str(number) for number in result["numbers"])  # Format the five main numbers.
        special_name = result["special_name"]  # Identify the separate ball.
        special_ball = result["special_ball"]  # Retrieve its selected number.
        reply = (  # Build the message displayed in the conversation.
            f"{title}: Your generated numbers are {numbers}. "  # Display the main selection.
            f"{special_name}: {special_ball}. Play again?"  # Display the separate ball and invitation.
        )
        if reply != previous_reply:  # Check that this differs from the previous response.
            return reply  # Send the new selection back to Rondesores.

    return "I couldn't create a different selection. Please try again."  # Handle exhausted attempts.