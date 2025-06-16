def shutdown(user_input):
    user_input = user_input()
    if user_input == "yes":
        return "Shutting down"
    elif user_input == "no":
        return "Abort shut down"
    else:
        return "Sorry."
