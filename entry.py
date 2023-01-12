import firstpartyaspect

print("Welcome to the aspects system. Here you can choose a base set of software to include with your system.")
print("Answer with the option number. E.g if the question was (1) Blah Blah Blah, you would enter 1.")
print("If you don't understand something, just use the default option.")

print("""
First choose if you want to use:
(1) A first party aspect (default)
(2) A third party aspect
(3) A custom aspect
""")
choice = input("> ")
if choice == "2":
    pass
elif choice == "3":
    pass
else: # Including 1
    firstpartyaspect.main()