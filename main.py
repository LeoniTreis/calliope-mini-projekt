def on_forever():
    while calliBot2.entfernung(C2Einheit.CM) > 10:
        calliBot2.motor(C2Motor.BEIDE, C2Dir.VORWAERTS, 50)
    calliBot2.motor_stop(C2Motor.BEIDE, C2Stop.BREMSEN)
    calliBot2.set_rgb_led1(C2RgbLed.ALL, 0x00ffdc, 8)
    calliBot2.motor(C2Motor.BEIDE, C2Dir.RUECKWAERTS, 50)
    calliBot2.warte(C2SensorWait.DISTANCE_CM, C2Check.EQUAL, 10)
    calliBot2.motor_stop(C2Motor.BEIDE, C2Stop.BREMSEN)
    calliBot2.motor(C2Motor.LINKS, C2Dir.VORWAERTS, 50)
    calliBot2.motor(C2Motor.RECHTS, C2Dir.RUECKWAERTS, 50)
    basic.pause(300)
    calliBot2.motor_stop(C2Motor.BEIDE, C2Stop.BREMSEN)
    if Math.random_boolean():
        calliBot2.set_rgb_led1(C2RgbLed.ALL, 0x0000ff, 8)
        calliBot2.motor(C2Motor.LINKS, C2Dir.VORWAERTS, 50)
        calliBot2.motor(C2Motor.RECHTS, C2Dir.RUECKWAERTS, 50)
    else:
        calliBot2.set_rgb_led1(C2RgbLed.ALL, 0xffff00, 8)
basic.forever(on_forever)
