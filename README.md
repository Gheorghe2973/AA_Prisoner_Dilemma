# истеричка

## Description

The `истеричка` algorithm is a reactive strategy designed for the Iterated Prisoner's Dilemma tournament. It starts by cooperating and continues to do so as long as the opponent also cooperates. However, the moment the opponent defects even once, истеричка immediately switches to an unpredictable behavior — a simulated "chaos mode" that uses pseudo-random logic to determine its next move.

## Strategy Logic

- **Friendly start**: Always cooperates until the opponent defects.
- **Triggered chaos**: As soon as a single defection is detected from the opponent, the algorithm no longer tries to cooperate and instead chooses between cooperation and defection in a pseudo-random way (using internal state like history sums).
- **Round 3 logic**: In the version with opponent selection, it prefers to play with cooperative opponents and avoids those who defect or have reached the round limit.

## Character

истеричка is emotionally volatile — calm, trusting, and friendly at first, but extremely sensitive to betrayal. Once hurt, it spirals into erratic behavior, incapable of trust again.

---

### Submission Files

- `истеричка.py` – Strategy for Part 1
- `истеричка_round_3.py` – Strategy for Part 2
