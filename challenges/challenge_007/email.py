def hide_email(email):
    s = email.split("@")
    s[0] = s[0][0] +  (len(s[0][1:]) * "*")
    hidden = "@".join(s)
    return hidden


if __name__ == "__main__":
    email = input("Enter your email address: ")
    hidden_mail = hide_email(email)
    print(hidden_mail)