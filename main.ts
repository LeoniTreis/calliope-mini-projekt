basic.forever(function () {
    while (calliBot2.entfernung(C2Einheit.cm) > 10) {
        calliBot2.motor(C2Motor.beide, C2Dir.vorwaerts, 50)
    }
    calliBot2.motorStop(C2Motor.beide, C2Stop.Bremsen)
    calliBot2.setRgbLed1(C2RgbLed.All, 0x00ffdc, 8)
    calliBot2.motor(C2Motor.beide, C2Dir.rueckwaerts, 50)
    calliBot2.warte(C2SensorWait.distanceCm, C2Check.equal, 10)
    calliBot2.motorStop(C2Motor.beide, C2Stop.Bremsen)
    calliBot2.motor(C2Motor.links, C2Dir.vorwaerts, 50)
    calliBot2.motor(C2Motor.rechts, C2Dir.rueckwaerts, 50)
    basic.pause(300)
    calliBot2.motorStop(C2Motor.beide, C2Stop.Bremsen)
    if (Math.randomBoolean()) {
        calliBot2.setRgbLed1(C2RgbLed.All, 0x0000ff, 8)
        calliBot2.motor(C2Motor.links, C2Dir.vorwaerts, 50)
        calliBot2.motor(C2Motor.rechts, C2Dir.rueckwaerts, 50)
    } else {
        calliBot2.setRgbLed1(C2RgbLed.All, 0xffff00, 8)
    }
})
