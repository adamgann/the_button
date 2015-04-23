#
# Top level code for passing button data to Arduino 


from thebutton import TheButton
import math
import serial # if you have not already done so


class ButtonApp():
    def __init__(self):
        # Create a new instance of the button client. Does nothing until start() is called
        self.the_button = TheButton()
        self.last_lowest = 60.0

        self.ser = serial.Serial('/dev/tty.usbmodem621', 57600)
        
        self.prev_color = 0
        self.color_list = ['Purple','Blue','Green','Yellow','Orange','Red']


    def run(self):
        self.the_button.start()
        try:
            while True: 
                curr_color = self.the_button.colour
                if curr_color != self.prev_color:
                    self.prev_color = curr_color
                    print self.color_list[curr_color-2]
                    self.ser.write(str(curr_color))


        except KeyboardInterrupt:
            pass
        self.close()


    def close(self):
        self.the_button.close()

    def assignColor(self, button_sec):
        if 51.01 <= button_sec <= 60.00:
            button_color = 2
        elif 41.01 <= button_sec <= 51.00:
            button_color = 3
        elif 31.01 <= button_sec <= 41.00:
            button_color = 4
        elif 21.01 <= button_sec <= 31.00:
            button_color = 5
        elif 11.01 <= button_sec <= 21.00:
            button_color = 6 
        elif 0.01 <= button_sec <= 11.00:
            button_color = 7
        else:
            button_color = 0

        return button_color



if __name__ == "__main__":
    button_app = ButtonApp()
    button_app.run()
