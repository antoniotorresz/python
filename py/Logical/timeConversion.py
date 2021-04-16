def timeConversion(s): #07:05:45PM
    hora = s[0:2]
    min_seg = s[2:8]
    ab = s[8:10]

    if ab == 'PM' and hora == '12': return hora + min_seg
    elif ab == 'AM' and hora == '12': return '00' + min_seg
    elif ab == 'PM': return str(int(hora) + 12) + min_seg
    else: return hora + min_seg

print(timeConversion('07:05:45PM'))