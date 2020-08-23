set_user_name = input('請設定您的使用者帳號: ')
set_password = input('請設定密碼:')
error_count = 3
print('設定完成...請重新登入!')
x = input('請選擇您接下來要執行的動作:')
if x == '1':
	user_name = input('請輸入您的使用者帳號: ')
	if user_name == set_user_name:
		while error_count > 0:
			error_count = error_count -1
			password = input('請輸入密碼:')
			if password != set_password:
				print('密碼錯誤!')
				if error_count > 0:
					print('還有', error_count, '次機會')
				else:
					print('密碼錯誤超過3次!!帳號已被鎖!')
					break
			else:
				print('登入成功!!!')
				break
	else:
		print('使用者帳號錯誤!!!')
		raise SystemExit
else:
	raise SystemExit