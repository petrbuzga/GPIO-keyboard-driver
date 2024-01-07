import RPi.GPIO as GPIO
import time
import datetime

from evdev import UInput, ecodes as e

ui = UInput(name = "GPIO Keyboard")

column_pin_numbers = [4, 17, 27, 22, 5, 6, 13, 19]
row_pin_numbers = [18, 23, 24, 25, 12, 16, 20, 21]
Shift_State = False

keymap = {
   (column_pin_numbers[5], row_pin_numbers[0]): (e.KEY_A),
   (column_pin_numbers[4], row_pin_numbers[0]): (e.KEY_B),
   (column_pin_numbers[3], row_pin_numbers[0]): (e.KEY_C),
   (column_pin_numbers[2], row_pin_numbers[0]): (e.KEY_D),
   (column_pin_numbers[1], row_pin_numbers[0]): (e.KEY_E),
   (column_pin_numbers[0], row_pin_numbers[0]): (e.KEY_ESC),

   (column_pin_numbers[5], row_pin_numbers[1]): (e.KEY_F),
   (column_pin_numbers[4], row_pin_numbers[1]): (e.KEY_G),
   (column_pin_numbers[3], row_pin_numbers[1]): (e.KEY_H),
   (column_pin_numbers[2], row_pin_numbers[1]): (e.KEY_I),
   (column_pin_numbers[1], row_pin_numbers[1]): (e.KEY_J),
   (column_pin_numbers[0], row_pin_numbers[1]): (e.KEY_DELETE),

   (column_pin_numbers[5], row_pin_numbers[2]): (e.KEY_K),
   (column_pin_numbers[4], row_pin_numbers[2]): (e.KEY_L),
   (column_pin_numbers[3], row_pin_numbers[2]): (e.KEY_M),
   (column_pin_numbers[2], row_pin_numbers[2]): (e.KEY_N),
   (column_pin_numbers[1], row_pin_numbers[2]): (e.KEY_O),
   (column_pin_numbers[0], row_pin_numbers[2]): (e.KEY_INSERT),

   (column_pin_numbers[5], row_pin_numbers[3]): (e.KEY_P),
   (column_pin_numbers[4], row_pin_numbers[3]): (e.KEY_Q),
   (column_pin_numbers[3], row_pin_numbers[3]): (e.KEY_R),
   (column_pin_numbers[2], row_pin_numbers[3]): (e.KEY_S),
   (column_pin_numbers[1], row_pin_numbers[3]): (e.KEY_T),
   (column_pin_numbers[0], row_pin_numbers[3]): (e.KEY_BACKSPACE),

   (column_pin_numbers[0], row_pin_numbers[4]): (e.KEY_PAGEUP),
   (column_pin_numbers[0], row_pin_numbers[5]): (e.KEY_SPACE),
   (column_pin_numbers[0], row_pin_numbers[7]): (e.KEY_PAGEDOWN),

   (column_pin_numbers[2], row_pin_numbers[4]): (e.KEY_SLASH),
   (column_pin_numbers[3], row_pin_numbers[4]): (e.KEY_9),
   (column_pin_numbers[4], row_pin_numbers[4]): (e.KEY_8),
   (column_pin_numbers[5], row_pin_numbers[4]): (e.KEY_7),

   (column_pin_numbers[2], row_pin_numbers[5]): (e.KEY_KPPLUS),
   (column_pin_numbers[3], row_pin_numbers[5]): (e.KEY_6),
   (column_pin_numbers[4], row_pin_numbers[5]): (e.KEY_5),
   (column_pin_numbers[5], row_pin_numbers[5]): (e.KEY_4),

   (column_pin_numbers[3], row_pin_numbers[6]): (e.KEY_3),
   (column_pin_numbers[4], row_pin_numbers[6]): (e.KEY_2),
   (column_pin_numbers[5], row_pin_numbers[6]): (e.KEY_1),

   (column_pin_numbers[3], row_pin_numbers[7]): (e.KEY_ENTER),
   (column_pin_numbers[4], row_pin_numbers[7]): (e.KEY_DOT),
   (column_pin_numbers[5], row_pin_numbers[7]): (e.KEY_0),
   (column_pin_numbers[1], row_pin_numbers[4]): (e.KEY_LEFTCTRL),
   (column_pin_numbers[1], row_pin_numbers[5]): (e.KEY_LEFTALT),

   (column_pin_numbers[1], row_pin_numbers[6]): (e.KEY_UP),
   (column_pin_numbers[2], row_pin_numbers[6]): (e.KEY_DOWN),
   (column_pin_numbers[2], row_pin_numbers[7]): (e.KEY_LEFT),
   (column_pin_numbers[0], row_pin_numbers[6]): (e.KEY_RIGHT),

   (column_pin_numbers[6], row_pin_numbers[0]): (e.KEY_F1),
   (column_pin_numbers[7], row_pin_numbers[0]): (e.KEY_F2),
   (column_pin_numbers[7], row_pin_numbers[1]): (e.KEY_F3),
   (column_pin_numbers[7], row_pin_numbers[2]): (e.KEY_F4),
   (column_pin_numbers[7], row_pin_numbers[3]): (e.KEY_F5),
   (column_pin_numbers[7], row_pin_numbers[4]): (e.KEY_F6),
   (column_pin_numbers[7], row_pin_numbers[5]): (e.KEY_F7),
   (column_pin_numbers[7], row_pin_numbers[6]): (e.KEY_F8),
   (column_pin_numbers[7], row_pin_numbers[7]): (e.KEY_F9),
   (column_pin_numbers[6], row_pin_numbers[7]): (e.KEY_F10),
}

shift_keymap = {
   (column_pin_numbers[5], row_pin_numbers[0]): (e.KEY_U),
   (column_pin_numbers[4], row_pin_numbers[0]): (e.KEY_V),
   (column_pin_numbers[3], row_pin_numbers[0]): (e.KEY_W),
   (column_pin_numbers[2], row_pin_numbers[0]): (e.KEY_X),
   (column_pin_numbers[1], row_pin_numbers[0]): (e.KEY_Y),
   (column_pin_numbers[0], row_pin_numbers[0]): (e.KEY_ESC),

   (column_pin_numbers[5], row_pin_numbers[1]): (e.KEY_Z),
   (column_pin_numbers[4], row_pin_numbers[1]): (e.KEY_COMMA),
   (column_pin_numbers[3], row_pin_numbers[1]): (e.KEY_LEFTSHIFT, e.KEY_SEMICOLON),
   (column_pin_numbers[2], row_pin_numbers[1]): (e.KEY_0),
   (column_pin_numbers[1], row_pin_numbers[1]): (e.KEY_LEFTSHIFT, e.KEY_8),
   (column_pin_numbers[0], row_pin_numbers[1]): (e.KEY_DELETE),

   (column_pin_numbers[5], row_pin_numbers[2]): (e.KEY_LEFTSHIFT, e.KEY_COMMA),
   (column_pin_numbers[4], row_pin_numbers[2]): (e.KEY_LEFTSHIFT, e.KEY_DOT),
   (column_pin_numbers[3], row_pin_numbers[2]): (e.KEY_SLASH),
   (column_pin_numbers[2], row_pin_numbers[2]): (e.KEY_BACKSLASH),
   (column_pin_numbers[1], row_pin_numbers[2]): (e.KEY_LEFTBRACE),
   (column_pin_numbers[0], row_pin_numbers[2]): (e.KEY_INSERT),

   (column_pin_numbers[5], row_pin_numbers[3]): (e.KEY_LEFTSHIFT, e.KEY_1),
   (column_pin_numbers[4], row_pin_numbers[3]): (e.KEY_LEFTSHIFT, e.KEY_SLASH),
   (column_pin_numbers[3], row_pin_numbers[3]): (e.KEY_LEFTSHIFT, e.KEY_4),
   (column_pin_numbers[2], row_pin_numbers[3]): (e.KEY_LEFTSHIFT, e.KEY_5),
   (column_pin_numbers[1], row_pin_numbers[3]): (e.KEY_RIGHTBRACE),
   (column_pin_numbers[0], row_pin_numbers[3]): (e.KEY_BACKSPACE),

   #dále jsou stejné jako bez shiftu

   (column_pin_numbers[0], row_pin_numbers[4]): (e.KEY_PAGEUP),
   (column_pin_numbers[0], row_pin_numbers[5]): (e.KEY_SPACE),
   (column_pin_numbers[0], row_pin_numbers[7]): (e.KEY_PAGEDOWN),

   (column_pin_numbers[2], row_pin_numbers[4]): (e.KEY_SLASH),
   (column_pin_numbers[3], row_pin_numbers[4]): (e.KEY_9),
   (column_pin_numbers[4], row_pin_numbers[4]): (e.KEY_8),
   (column_pin_numbers[5], row_pin_numbers[4]): (e.KEY_7),

   (column_pin_numbers[2], row_pin_numbers[5]): (e.KEY_KPPLUS),
   (column_pin_numbers[3], row_pin_numbers[5]): (e.KEY_6),
   (column_pin_numbers[4], row_pin_numbers[5]): (e.KEY_5),
   (column_pin_numbers[5], row_pin_numbers[5]): (e.KEY_4),

   (column_pin_numbers[3], row_pin_numbers[6]): (e.KEY_3),
   (column_pin_numbers[4], row_pin_numbers[6]): (e.KEY_2),
   (column_pin_numbers[5], row_pin_numbers[6]): (e.KEY_1),

   (column_pin_numbers[3], row_pin_numbers[7]): (e.KEY_ENTER),
   (column_pin_numbers[4], row_pin_numbers[7]): (e.KEY_DOT),
   (column_pin_numbers[5], row_pin_numbers[7]): (e.KEY_0),
   (column_pin_numbers[1], row_pin_numbers[4]): (e.KEY_LEFTCTRL),
   (column_pin_numbers[1], row_pin_numbers[5]): (e.KEY_LEFTALT),

   (column_pin_numbers[1], row_pin_numbers[6]): (e.KEY_UP),
   (column_pin_numbers[2], row_pin_numbers[6]): (e.KEY_DOWN),
   (column_pin_numbers[2], row_pin_numbers[7]): (e.KEY_LEFT),
   (column_pin_numbers[0], row_pin_numbers[6]): (e.KEY_RIGHT),

   (column_pin_numbers[6], row_pin_numbers[0]): (e.KEY_F1),
   (column_pin_numbers[7], row_pin_numbers[0]): (e.KEY_F2),
   (column_pin_numbers[7], row_pin_numbers[1]): (e.KEY_F3),
   (column_pin_numbers[7], row_pin_numbers[2]): (e.KEY_F4),
   (column_pin_numbers[7], row_pin_numbers[3]): (e.KEY_F5),
   (column_pin_numbers[7], row_pin_numbers[4]): (e.KEY_F6),
   (column_pin_numbers[7], row_pin_numbers[5]): (e.KEY_F7),
   (column_pin_numbers[7], row_pin_numbers[6]): (e.KEY_F8),
   (column_pin_numbers[7], row_pin_numbers[7]): (e.KEY_F9),
   (column_pin_numbers[6], row_pin_numbers[7]): (e.KEY_F10),
}

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(column_pin_numbers, GPIO.OUT)
GPIO.output(column_pin_numbers, 0)
GPIO.setup(row_pin_numbers, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#funkce, která řeší zápis klávesy po zmáčknutí tlačítka shift
def Write_Shift_Presed_Key():
   GPIO.output(column_pin_numbers[1], 0)
   while 1:
      time.sleep(1/60)
      for column_pin in column_pin_numbers:
         GPIO.output(column_pin, 1)
         for row_pin in row_pin_numbers:
            if GPIO.input(row_pin) == 1 and row_pin != row_pin_numbers[7]:
                  if isinstance(shift_keymap[column_pin,row_pin], tuple):
                     ui.write(e.EV_KEY, shift_keymap[column_pin,row_pin][0], 1)
                     ui.write(e.EV_KEY, shift_keymap[column_pin,row_pin][1], 1)
                     ui.write(e.EV_KEY, shift_keymap[column_pin,row_pin][0], 0)
                     GPIO.wait_for_edge(row_pin, GPIO.FALLING, timeout = 500)
                     ui.write(e.EV_KEY, shift_keymap[column_pin,row_pin][1], 0)
                     ui.syn()
                     return
                  else:
                     Write_Input(column_pin,row_pin, shift_keymap)
                     return
         GPIO.output(column_pin, 0)

#funkce, která zapíše zmáčknutí klávesy do systemd 
def Write_Input(column_pin, row_pin, keys_mapping):
   ui.write(e.EV_KEY, keys_mapping[column_pin,row_pin], 1)
   GPIO.wait_for_edge(row_pin, GPIO.FALLING, timeout = 500)
   ui.write(e.EV_KEY, keys_mapping[column_pin,row_pin], 0)
   ui.syn()
   return

#nekonečný cyklus, který zajišťuje skenování klávesnice
while 1:
   time.sleep(1/60)
   for column_pin in column_pin_numbers:
      GPIO.output(column_pin, 1)
      for row_pin in row_pin_numbers:
         if GPIO.input(row_pin) == 1:
            if row_pin == row_pin_numbers[7] and column_pin == column_pin_numbers[1]:
               Write_Shift_Presed_Key()
            else:
               Write_Input(column_pin, row_pin, keymap)    
      GPIO.output(column_pin, 0)