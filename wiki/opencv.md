# OpenCV: calibration and object finding

OpenCV is the tool we use for object detection. Here will be displayed some info about the steps and strategies taken to accomplish the goal.

## Calibration

Calibration is done thanks to a calibration board ressembling a chess board. Here are some specs:

- **Board dimension** : 6 by 7 square intersections
- **Square dimension** : 10cm each side

Here is some vocabulary that will be used in the following explanations :

- `world_space` (or `camera_space`): The 3D system that the camera works with.
- `world_coordinate` (or `world_point`): A point in the `world_space`
- `image_space`: The 2D projected space of the `world_space`
- `image_point`: A point in the `image_space`
- `object_point`: An *relative* world-space 3D coordinate. It represents the relative position from the center of the designed object. For exemple, the `object_point` of one of the corner of a square of side-length `20.0` situated at the world-coordinate `(21.5, 74.99, -125.4)` is `(10.0, 10.0, 0)` (note that the `object_point` has absolutly no correlation with the `world_coordinate`).
- `camera_matrix`: The 3x3 matrix calculated by the calibration algorithm. It represents a mixture of intrinsic and extrinsic parameters.
- `distortion_coefficients`: An array of ditortion parameters. This matrix should always be sent along with the `camera_matrix` since they work togheter.

The algorithm works by associating each specified `object_point` of the chessboard corners with the `image_points` found by OpenCV's detection algorithm. The combination is then used to calculate the `camera_matrix`. For good viable results, it is **important** to take at least 20 **non-coplanar** chessboard pictures (meaning that if the board lay on the same surface twice, it only counts for 1 picture).

## Aruco markers

Aruco markers are pictures of encoded bits represented by white squares on a black background (or the inverse, whatever). Each marker represents a number (has an id) and each marker is predefined and unique. The grid of the bits can be either 4x4 or 6x6. Since we have a low-resolution camera and need less than 10 markers, it is better to use the 4x4 grid since the inner squares will be bigger and thus the edges will be more precise.

### Creation

OpenCV offers different dictionnaries that contains predefined sets of markers. The nomenclature is the following: `DICT_<grid_dimensions>_<number_of_markers>`. For better clarity and since we don't need a lot of markers, we will use the `DICT_4x4_50` dictionnary.

When printing the markers, it is **extremely important** to left at least 5-10 mm of white padding around the black border. Without the white padding, OpenCV won't be able to detect the markers (trust me, I've had the problem).

### Detection

For detecting the aruco markers, it is **extremely important** to use the same dictionnary as the one used for the creation of the markers. Else, OpenCV won't event try to find them.

The detection needs a few parameters to work:

- **Marker's dictionnary**: The dictionnary containing the set of markers to detect
- **Marker's side-length**: The length of one side of the marker (including the black border, but excluding the white padding). Note: this is NOT the size of one inner square, but rather the size of the entire marker.
- **An image**: an image containing the markers to identify
- **Camera matrix**
- **Distortion coefficients**

The algorithm returns the 3D positions (rotation and translation vectors) of each founded marker. We can then easily show the corresponding 3D axes on the captured image.

## Pillars detection

The detection of the pillars directly uses the aruco markers detection. We then simply remove the pillar's height (41 cm) along the Z axis to find the position of the pillar **at the bottom** (e.g. on the table). Note that we remove and not add the height because the Z axis is **inverted** (along with the Y axis actually). 

[BACK](./README.md)
