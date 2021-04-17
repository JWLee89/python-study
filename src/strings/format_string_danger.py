from string import Template

SECRET = "YEE-secret"


class Error:
    def __init__(self):
        pass

err = Error()


if __name__ == "__main__":
    # Can access other variables using format
    user_input = '{error.__init__.__globals__[SECRET]}'
    input_1 = user_input.format(error=err)
    print(input_1)
    # Rule of thumb - use template strings when generating
    # strings from user input
    input_2 = Template(user_input).substitute(error=err)
    print(input_2)
