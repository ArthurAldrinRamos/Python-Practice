name = "Arthur"


def another():
    def greeting(firstName):
        color = "blue"
        print(color)
        print(name)
        print(firstName)

    greeting("Arthur")


another()
