def response(hey_bob):
    clean_input = hey_bob.strip()

    if not clean_input:
        return 'Fine. Be that way!'
    if clean_input.isupper() and clean_input.endswith('?'):
        return "Calm down, I know what I'm doing!"
    if clean_input.isupper():
        return 'Whoa, chill out!'
    if clean_input.endswith('?'):
        return 'Sure.'

    return 'Whatever.'
