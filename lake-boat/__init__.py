from enum import Enum
from ruddercontrol import rudder

class Direction(Enum):
    FORWARD = 1,
    BACKWARD = 2

class Actions(Enum):
    CAPTURE_IMAGE = 1,
    CAPTURE_TEMP = 2,
    CAPTURE_HUMIDITY = 3,

class LakeBoat:
    def __init__(self):
        self.speed = 0
        self.direction = Direction.FORWARD
        self.is_camera_on = False
        self.is_alarm_on = False
        self.temperature = 0
        self.humidity = 0
        self.rotation = 0
        self.actions = []
        self.image_snapshot = ""

    # rotation functions

    def set_rotation(self, amount = 0):
        self.rotation = amount

    # ----- FUNCTIONS TO HANDLE ACCELERATION AND DIRECTION

    def set_acceleration(self, amount = 1):
        print('Updating speed to', amount)
        self.speed = amount

    def stop(self):
        print('Stopping the boat')
        self.speed = 0

    def set_direction_forward(self):
        print('Setting forward direction')
        self.direction = Direction.FORWARD

    def set_direction_backward(self):
        print('Setting backward direction')
        self.direction = Direction.BACKWARD

    # ----- FUNCTIONS THAT UPDATE THE BOAT STATE OR ADD ACTIONS TO THE QUEUE

    def camera_on(self):
        self.is_camera_on = True

    def camera_off(self):
        self.is_camera_on = False

    def alert_on(self):
        self.is_alarm_on = True

    def alert_off(self):
        self.is_alarm_on = False

    def collect_temperature(self):
        self.actions.append(Actions.CAPTURE_TEMP)

    def collect_snapshot(self):
        self.actions.append(Actions.CAPTURE_IMAGE)

    def collect_humidity(self):
        self.actions.append(Actions.CAPTURE_HUMIDITY)

    # ----- FUNCTIONS TO HANDLE DATA COLLECTION -----

    def handle_collect_temperature(self):
        print('Collecting temperature')
        # TODO add hardware logic to collect temperature and save to `self.temperature` variable
        # TODO save the data to file using the `storage.py` functions

    def handle_collect_humidity(self):
        print("Collecting humidity")
        # TODO add hardware logic to collection humidity and save to `self.humidity` variable
        # TODO save data to file using the `storage.py` functions

    def handle_capture_image(self):
        print("Collection image snapshot")
        # TODO add hardware logic to collect image snapshot and save to `self.image_snapshot` variable
        # TODO save data to file using the `storage.py` functions

    # ----- FUNCTIONS THAT UPDATE THE BOAT BASED ON THE VARIABLES DEFINED IN THE CLASS -----

    def update_speed(self):
        print('updating speed', self.speed)
        # TODO add logic to update hardware boat speed based on the `speed` variable

    def update_rotation(self):
        print('updating rotation', self.rotation)
        # TODO add logic to update hardware boat rotation based on the `speed` variable

    def update_direction(self):
        print('updating direction')
        # TODO add logic to update hardware boat forward or reverse based on `direction` variable

    def update_alarm_state(self):
        print('Updating the alarm')
        # TODO add logic to update hardware boat alarm based on the `is_alarm_on` variable

    def update_camera_state(self):
        print('Updating camera state')
        # TODO add logic to trigger the camera on and off based on the `is_camera_on` variable

    ## The function below should be run in an event loop

    def process_action_handlers(self):
        actions = list(self.actions)  # create copy so I don't update the original yet
        for action in actions:
            if action == Actions.CAPTURE_TEMP:
                self.handle_collect_temperature()
            elif action == Actions.CAPTURE_HUMIDITY:
                self.handle_collect_humidity()
            elif action == Actions.CAPTURE_IMAGE:
                self.handle_capture_image()
        actions.clear()  # TODO there is a better way to do this, but we can change it later

    def update(self):
        #Rudder does not have to be in here b/c 
        self.update_speed()
        self.update_rotation()
        self.update_direction()
        self.update_alarm_state()
        self.update_camera_state()
        self.process_action_handlers()
    
boat = LakeBoat()
    
if __name__ == '__main__':
        while True:
            boat.update()
