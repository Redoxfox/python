with open(".passwd") as f:
    passwd = f.readline().strip()
    try:
        if (p == int(passwd)):
            print ("Well done ! You can validate with this password !")
    except:
        youLose()

        