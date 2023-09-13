def callMe():
    # print('Called you!')
    try:
        email = input("Enter your email id: ")
        # print(email)
        (name,tail) = (email.split('@'))
        # print(name,tail)
        (domainName, domainExtension) = (tail.split('.'))
        print("Your Name = ", name)
        print("Your Domain = ", domainName)
        print("Your Domain Extension = ", domainExtension)
    except:
        print('Invalid email Id has been provided!')

callMe()