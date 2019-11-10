# Vicon

A package to read in Vicon data for analysis. This package can be used to read in a CSV file generated from 
the Vicon motion capture system

##NOTE
There is a strange bug when reading in the file. It will throw and error if you try to read in the raw file. 
To solve this problem. Open up the CSV file in libreoffice or Excel and resave the file. Make sure its a CSV file. 


### Playing the markers


```python
file = "path to CSV file"
data = Vicon.Vicon(file)
markers = data.get_markers()
markers.smart_sort() # sort the markers into bodies by the names 
markers.play()
```


## Get rigid body
Rigid bodies are organized  by marker then frame. 
The markers are of type Point. 

```python
file = "path to CSV file"
data = Vicon.Vicon(file)
markers = data.get_markers()
markers.smart_sort() # optional param to remove subject name
shank_frame = markers.get_rigid_body("name of body") # returns an array of markers 
## Get the X corr of a marker 2 in frame 100
x = shank_frame[2][100].x
```


## Get rigid body transform
Rigid bodies are organized  by marker then frame. 
The markers are of type Point. 

```python
file = "path to CSV file"
data = Vicon.Vicon(file)
markers = data.get_markers()
markers.smart_sort() # optional param to remove subject name

# Do severial bodies, use the marker location on the rigidbody
frames["hip"] = [core.Point(0.0, 0.0, 0.0),
                 core.Point(70.0, 0, 0.0),
                 core.Point(0, 42.0, 0),
                 core.Point(35.0, 70.0, 0.0)]

frames["RightThigh"] = [core.Point(0.0, 0.0, 0.0),
                        core.Point(56.0, 0, 0.0),
                        core.Point(0, 49.0, 0),
                        core.Point(56.0, 63.0, 0.0)]

frames["RightShank"] = [core.Point(0.0, 0.0, 0.0),
                        core.Point(56.0, 0, 0.0),
                        core.Point(0, 42.0, 0),
                        core.Point(56.0, 70.0, 0.0)]

markers.auto_make_transform(frames)


# Get just one transform and the RMSE error 
# Can be used to get the transformation between ANY two sets of markers 
 m = markers.get_rigid_body("ben:hip")
 f = [m[0][frame], m[1][frame], m[2][frame], m[3][frame]]
 T, err = Markers.cloud_to_cloud(hip_marker, f)
```

## Get model outputs 
only works with lowerbody model currently

```python
from Vicon import Vicon
file = "path to CSV file"
data = Vicon.Vicon(file)
model = data.get_model_output()
model.get_left_leg().hip.angle.x
```

## Get force plates

```python
from Vicon import Vicon
file = "path to CSV file"
data = Vicon.Vicon(file)
data = Vicon.Vicon("/home/nathaniel/git/Gait_Analysis_Toolkit/testing_data/stairclimb03.csv")
fp = data.get_force_plate(1).get_forces() # pass in 1 or 2 to get the foce plates
```


