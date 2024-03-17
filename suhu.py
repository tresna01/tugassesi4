suhu_input = float(input("masukan suhu :"))
satuan_input = input ("masukan satuan suhu fahrenheit atau celcius? (F/C) :" )

if satuan_input == 'C':
    suhu_fahrenheit = (suhu_input * 9/5) + 32
    print(f"{suhu_input} °C sama dengan {suhu_fahrenheit:.1f} F°")
elif satuan_input == 'F':
    suhu_celcius = (suhu_input -32) * 5/9
    print(f"{suhu_input}°F sama dengan {suhu_celcius:.1f} C°")
else:
    print("INVALID:TOLONG MASUKAN SUHU F/C F UNTUK(FAHRENHEIT) ATAU C UNTUK (CELCIUS)")

