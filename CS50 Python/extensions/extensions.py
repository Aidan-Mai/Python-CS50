File = input('what type of document are you looking for?: ')

File = File.lower()

if '.gif' in File:
    print('image/gif')
elif '.jpg' in File:
    print('image/jpeg')
elif '.jpeg' in File:
    print('image/jpeg')
elif '.pdf' in File:
    print('application/pdf')
elif '.png' in File:
    print('image/png')
elif '.txt' in File:
    print('text/plain')
elif '.zip' in File:
    print('application/zip')
else:
    print('application/octet-stream')