#  Mumbai Local Train Route Planner


---

##  Project Overview

The **Mumbai Local Train Route Planner** is a responsive, web-based application that allows users to:
- View Mumbai's Western, Central, and Harbor train lines
-  Plan routes between stations
-  Visualize crowd levels at each station
-  Avoid crowded stations in real time using simulated data


---

## Screenshots

![image](https://github.com/user-attachments/assets/13e3a6b1-63bd-4e27-a44a-f886373e9469)

![image](https://github.com/user-attachments/assets/3731ce54-100b-426f-a656-6aa58a19cf4d)


---

##  Tech Stack

### Backend
- Python 3.8+
- Flask
- Dijkstra's Algorithm for route finding

### Frontend
- HTML5, CSS3, JavaScript
- Bootstrap for UI
- Leaflet.js for interactive maps
- OpenStreetMap for base tiles

###  Data
- Station data & connections stored as JSON-like structures in `map.js`

---

##  Features

-  Dynamic map visualization of Mumbai local train routes
-  Real-time route computation
-  Avoid crowded stations option
-  Crowd level simulation with backend API
-  Responsive design (mobile-friendly!)

---

##  Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/mumbai-train-planner.git
   cd mumbai-train-planner
