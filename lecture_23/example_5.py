

class Human:
    def __init__(self):
        self._name = None # protected attribute

    def set_name(self, v):
        self._name = v  # protected attribute

    def get_name(self):
        return self._name


    def __str__(self):
        return f"Human({self._name})"


def main():
    h = Human()
    h.set_name("Giorgi")
    print(h)


if __name__ == "__main__":
    main()
