def get_range_for_difficulty(difficulty: str):
    """Return the inclusive lower and upper bounds for a difficulty level.

    Args:
        difficulty: one of "Easy", "Normal", or "Hard".

    Returns:
        A tuple (low, high) describing the secret-number range.
    """

    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    # default to normal range if something unexpected is passed
    return 1, 100


def parse_guess(raw: str):
    """
    Parse a raw string from the input widget into an integer guess.

    Returns a triple ``(ok, guess_int, error_message)`` where ``ok`` is ``True``
    when the conversion succeeded, ``guess_int`` holds the converted integer, and
    ``error_message`` contains a user-facing message when parsing failed.
    """

    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare a guess to the secret value.

    The application exercises a very odd glitch: on every second attempt the
    secret is converted to a string.  ``check_guess`` used to rely on a
    ``try/except`` around a numeric comparison which meant a string secret
    triggered lexicographic ordering ("10" < "2").  The result was wildly
    misleading hints.

    To fix it we normalise both values by coercing anything that *looks like* an
    integer back into an ``int`` before performing any comparisons.  This keeps
    the exterior behaviour identical while making the logic resilient to the
    type flip.

    Args:
        guess: the user's guess (usually an ``int`` from ``parse_guess``).
        secret: the secret value, which may be an ``int`` or a string.

    Returns:
        ``(outcome, message)`` where ``outcome`` is one of ``"Win"``,
        ``"Too High"`` or ``"Too Low"`` and ``message`` contains the hint
        string with emojis.
    """

    def _normalise(x):
        try:
            return int(x)
        except Exception:
            return x

    g = _normalise(guess)
    s = _normalise(secret)

    if g == s:
        return "Win", "🎉 Correct!"

    # numeric comparison should now work even if one of the inputs was a
    # string containing digits
    try:
        if g > s:
            # guess is higher than secret
            return "Too High", "📉 Go LOWER!"
        else:
            # guess is lower than secret
            return "Too Low", "📈 Go HIGHER!"
    except Exception:
        # fall back to string comparison to at least return something sensible
        if str(g) > str(s):
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Return an updated score after a single guess.

    ``attempt_number`` should be the 1‑based index of the guess (first guess is
    attempt 1).  The geometry of the game is intentionally glitchy, so the
    scoring rules are a bit odd but they are preserved here:

    * ``Win`` – award ``100 - 10 * (attempt_number - 1)`` points.  There is a
      floor of 10 points, so the value never goes below 10.
    * ``Too High`` – if the guess occurred on an even attempt, add 5 points;
      otherwise subtract 5 points.
    * ``Too Low`` – always subtract 5 points.
    * Any other ``outcome`` leaves the score unchanged.
    """

    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
