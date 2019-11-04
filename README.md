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
markers.smart_sort()
markers.play()
```


## Create rigid transforms

To create transform from the global frame to a rigid body. 
```python
file = "path to CSV file"
data = Vicon.Vicon(file)
markers = data.get_markers()
markers.smart_sort()
markers.play()
```
