if input_state == False:
      print('Button Pressed')
      time.sleep(0.2)
      GPIO.output(ledGreen, 1)
      time.sleep(1)
      GPIO.output(ledGreen, 0)
      GPIO.output(ledYellow, 1)
      time.sleep(1)
      GPIO.output(ledYellow, 0)
      GPIO.output(ledRed, 1)
    else: 
      GPIO.output(ledGreen, 0)
      GPIO.output(ledYellow, 0)
      GPIO.output(ledRed, 0)
