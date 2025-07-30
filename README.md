# Radar_Data_Visulizer
This is a simple Radar data visualization tool made for visualizing radar data from DIY radars especially arduino radars with HC SR04 ultrasonic sensor.

### `rdv( title = String , refreash_rate = Int , data_visualization_scope = Int , max_distance = Int ):`
`rdv()` is the class intialization. It accepts three inputs explained below :-
- The `title` parameter has a `String` datatype and is the title of window. The defaut value of this parameter is `radar_visualizer`.
- The `refreash_rate` parameter has a `Int` datatype and is the refresh rate of the screen. The defaut value of this parameter is `0.00125`.
- The `data_visualization_scope` parameter has a `Int` datatype and is amount data lines displayed at once. The defaut value of this parameter is `30`.
- The `max_distance` parameter has a `Int` datatype and is maximum distance the radar can detect. The defaut value of this parameter is `180`.

### `.start():`
The `start()` method internally runs the the`.__run()` method which begins the GUI interface. 

### `.add_data( data = String ):`
The `add_data()` method accepts a `String` datatype value in the format of `"angle,length"`. This value is then turned into tuple and stored in the `self.angle_data` attribute.

## GUI usage
The buttons present on the GUI of the tool are described below,
- The first input box can be used to change the `max_distance` parameter.
- The option menu can be used to change between `semi circle` and `circle` display type.
- The `Ok` button is used to apply the changes.

## Installation
This tool can be easily installed with `pip` using this command
```python
pip install 
```

# Example
```python
import radar_data_visualizer as rdv

app = rdv.rdv()

app.start()

# Since I currently don't have the hardware to show an live example so I will use the below code to give an example

for i in range(0, 180):
    app.add_data(f"{i},180")
    time.sleep(0.2) # assuming the sensor has some delay

```
# Demonstration
https://github.com/user-attachments/assets/41118aba-22fd-4dbd-b413-07314cf93d0a

##### Note: The program might take sometime after terminating to close down but it can also be stopped earlier than that with crtl + C without any issues.