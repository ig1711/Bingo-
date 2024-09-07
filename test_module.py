class PR_TEST:
    def __init__(this, tries):
        this.tries = tries

    def start(this):
        for i in range(this.tries):
            print(f'Attempt #{i + 1}: Test success.')
