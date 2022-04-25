# Glossary of Terms

# W1
Overview

## Terms
- Driving Task
- Operational Design Domain


## Components
- Lateral Control: steering
  - example: changing lanes
- Longitudinal Control: breaking, accelerating
  - example: maintaing spped
- Obj and Event Detection and Response: detection, reaction
  - Emergency Response
  - Complete vs Restricted ODD
- Planning: long / short term
  - long term example: finding route
- Miscellaneous


## L1~L5
L3 cannot handle emergencies automatically, need full user alertness
L5 operate any weather condition + any road type or surface + any scenario and remain safe


## Perception
- Environment and ourselves
  - Identification
    - Static objects
      - On Road
        - road and lane markings
        - Construction signs, obstructions
      - Off Road
        - Crubs
        - Traffic lights
        - Road signs
    - Dynamic objects
      - Vehicles
      - Pedestrians
    - Ego localization
      - Global Navigation Satellite System (GNSS)
  - Understanding Motion
    - example: perception in adaptive cruise control

Challenges


## Decision and Actions
- By window of time
  - long / short / immediate planning
- Predictive Planning
  - Based on predictions of the actions of others
  - Moving pedestrian
  - Stopped car


# W2
## Sensors for perception
Camera
perceiving environment
- exteroceptive
- resolution
- field of view
- dynamic range

Stero Cameras

Lidar
For 3d scene geometry
- exteroceptive
- number of beams
- points per second
- rotation rate
- field of view

Solid state Lidar

Radar
Robust obj detection and relative speed estimation
- exteroceptive
- range
- field of view
- position and speed accuracy

Ultra Sonic
Short range distance measurement
- exteroceptive
- range
- field of view
- cost

GNSS / IMU

Whell Odometry


## Computing Hardware
Computer
GPU
FPGA
ASIC
Hardware Sync


## Hardware Design and Scenarios
Highway
- Emergency stop
- Maintain speed
- Lane change

Urban
- Emergency stop
- Maintain speed
- Lane change
- Overtaking
- Turing, crossing at intersections
- Passing roundabouts


## Software Architecture
- Environment perception
- Environment mapping
- Motion planning
- Controller
- System supervisor
