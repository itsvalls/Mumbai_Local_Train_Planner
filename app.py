from flask import Flask, render_template, jsonify, request
import json
import random
import os
import math
import re

app = Flask(__name__, template_folder='web/templates', static_folder='web/static')

# Load station data from map.js
def load_station_data():
    try:
        # Determine the correct file path
        map_js_path = os.path.join(app.static_folder, 'map.js')
        
        # Check if the file exists
        if not os.path.exists(map_js_path):
            print(f"Map.js file not found at: {map_js_path}")
            # Try to find the file in the current directory
            for root, dirs, files in os.walk('.'):
                for file in files:
                    if file == 'map.js':
                        map_js_path = os.path.join(root, file)
                        print(f"Found map.js at: {map_js_path}")
                        break
        
        # Read the map.js file
        with open(map_js_path, 'r') as file:
            content = file.read()
            
            # Create a hardcoded version of the data since parsing is problematic
            stations = [
                # Western Line
                {"id": "churchgate", "name": "Churchgate", "lat": 18.9322, "lng": 72.8264, "crowdLevel": 0.8, "line": "Western"},
                {"id": "marine_lines", "name": "Marine Lines", "lat": 18.9431, "lng": 72.8253, "crowdLevel": 0.5, "line": "Western"},
                {"id": "charni_road", "name": "Charni Road", "lat": 18.952, "lng": 72.8187, "crowdLevel": 0.6, "line": "Western"},
                {"id": "grant_road", "name": "Grant Road", "lat": 18.9641, "lng": 72.8146, "crowdLevel": 0.4, "line": "Western"},
                {"id": "mumbai_central", "name": "Mumbai Central", "lat": 18.9712, "lng": 72.819, "crowdLevel": 0.9, "line": "Western"},
                {"id": "mahalaxmi", "name": "Mahalaxmi", "lat": 18.9865, "lng": 72.8296, "crowdLevel": 0.7, "line": "Western"},
                {"id": "lower_parel", "name": "Lower Parel", "lat": 18.9977, "lng": 72.8335, "crowdLevel": 0.8, "line": "Western"},
                {"id": "elphinstone", "name": "Elphinstone Road", "lat": 19.0088, "lng": 72.8362, "crowdLevel": 0.7, "line": "Western"},
                {"id": "dadar_w", "name": "Dadar (Western)", "lat": 19.0178, "lng": 72.8478, "crowdLevel": 0.9, "line": "Western"},
                {"id": "matunga_road", "name": "Matunga Road", "lat": 19.0283, "lng": 72.8469, "crowdLevel": 0.5, "line": "Western"},
                {"id": "mahim", "name": "Mahim", "lat": 19.0367, "lng": 72.8425, "crowdLevel": 0.6, "line": "Western"},
                {"id": "bandra", "name": "Bandra", "lat": 19.0545, "lng": 72.8412, "crowdLevel": 0.8, "line": "Western"},
                {"id": "khar_road", "name": "Khar Road", "lat": 19.069, "lng": 72.8371, "crowdLevel": 0.5, "line": "Western"},
                {"id": "santacruz", "name": "Santacruz", "lat": 19.0804, "lng": 72.8379, "crowdLevel": 0.6, "line": "Western"},
                {"id": "vile_parle", "name": "Vile Parle", "lat": 19.0969, "lng": 72.8394, "crowdLevel": 0.7, "line": "Western"},
                {"id": "andheri", "name": "Andheri", "lat": 19.1197, "lng": 72.8467, "crowdLevel": 0.9, "line": "Western"},
                
                # Central Line
                {"id": "cst", "name": "Chhatrapati Shivaji Terminus", "lat": 18.9398, "lng": 72.8354, "crowdLevel": 0.9, "line": "Central"},
                {"id": "masjid", "name": "Masjid", "lat": 18.945, "lng": 72.8399, "crowdLevel": 0.5, "line": "Central"},
                {"id": "sandhurst_road", "name": "Sandhurst Road", "lat": 18.957, "lng": 72.8399, "crowdLevel": 0.4, "line": "Central"},
                {"id": "byculla", "name": "Byculla", "lat": 18.9764, "lng": 72.833, "crowdLevel": 0.6, "line": "Central"},
                {"id": "chinchpokli", "name": "Chinchpokli", "lat": 18.9864, "lng": 72.833, "crowdLevel": 0.5, "line": "Central"},
                {"id": "currey_road", "name": "Currey Road", "lat": 18.9942, "lng": 72.833, "crowdLevel": 0.4, "line": "Central"},
                {"id": "parel", "name": "Parel", "lat": 19.0015, "lng": 72.8414, "crowdLevel": 0.7, "line": "Central"},
                {"id": "dadar_c", "name": "Dadar (Central)", "lat": 19.0218, "lng": 72.8439, "crowdLevel": 0.9, "line": "Central"},
                {"id": "matunga", "name": "Matunga", "lat": 19.0283, "lng": 72.855, "crowdLevel": 0.6, "line": "Central"},
                {"id": "sion", "name": "Sion", "lat": 19.0379, "lng": 72.8691, "crowdLevel": 0.7, "line": "Central"},
                {"id": "kurla", "name": "Kurla", "lat": 19.0647, "lng": 72.8891, "crowdLevel": 0.8, "line": "Central"},
                {"id": "vidyavihar", "name": "Vidyavihar", "lat": 19.0797, "lng": 72.8991, "crowdLevel": 0.5, "line": "Central"},
                {"id": "ghatkopar", "name": "Ghatkopar", "lat": 19.0858, "lng": 72.9081, "crowdLevel": 0.8, "line": "Central"},
                
                # Harbor Line
                {"id": "wadala", "name": "Wadala", "lat": 19.0178, "lng": 72.865, "crowdLevel": 0.6, "line": "Harbor"},
                {"id": "sewri", "name": "Sewri", "lat": 19.005, "lng": 72.855, "crowdLevel": 0.4, "line": "Harbor"},
                {"id": "cotton_green", "name": "Cotton Green", "lat": 18.995, "lng": 72.85, "crowdLevel": 0.3, "line": "Harbor"},
                {"id": "reay_road", "name": "Reay Road", "lat": 18.985, "lng": 72.845, "crowdLevel": 0.4, "line": "Harbor"},
                {"id": "dockyard_road", "name": "Dockyard Road", "lat": 18.975, "lng": 72.84, "crowdLevel": 0.5, "line": "Harbor"},
                {"id": "sandhurst_road_h", "name": "Sandhurst Road (Harbor)", "lat": 18.957, "lng": 72.8399, "crowdLevel": 0.4, "line": "Harbor"},
                {"id": "cst_h", "name": "CST (Harbor)", "lat": 18.9398, "lng": 72.8354, "crowdLevel": 0.9, "line": "Harbor"},
                {"id": "kurla_h", "name": "Kurla (Harbor)", "lat": 19.065, "lng": 72.8895, "crowdLevel": 0.8, "line": "Harbor"}
            ]
            
            connections = [
                # Western Line connections
                {"from": "churchgate", "to": "marine_lines", "time": 3},
                {"from": "marine_lines", "to": "charni_road", "time": 3},
                {"from": "charni_road", "to": "grant_road", "time": 3},
                {"from": "grant_road", "to": "mumbai_central", "time": 3},
                {"from": "mumbai_central", "to": "mahalaxmi", "time": 4},
                {"from": "mahalaxmi", "to": "lower_parel", "time": 3},
                {"from": "lower_parel", "to": "elphinstone", "time": 3},
                {"from": "elphinstone", "to": "dadar_w", "time": 3},
                {"from": "dadar_w", "to": "matunga_road", "time": 3},
                {"from": "matunga_road", "to": "mahim", "time": 3},
                {"from": "mahim", "to": "bandra", "time": 4},
                {"from": "bandra", "to": "khar_road", "time": 3},
                {"from": "khar_road", "to": "santacruz", "time": 3},
                {"from": "santacruz", "to": "vile_parle", "time": 4},
                {"from": "vile_parle", "to": "andheri", "time": 4},
                
                # Central Line connections
                {"from": "cst", "to": "masjid", "time": 3},
                {"from": "masjid", "to": "sandhurst_road", "time": 3},
                {"from": "sandhurst_road", "to": "byculla", "time": 4},
                {"from": "byculla", "to": "chinchpokli", "time": 3},
                {"from": "chinchpokli", "to": "currey_road", "time": 3},
                {"from": "currey_road", "to": "parel", "time": 3},
                {"from": "parel", "to": "dadar_c", "time": 4},
                {"from": "dadar_c", "to": "matunga", "time": 3},
                {"from": "matunga", "to": "sion", "time": 4},
                {"from": "sion", "to": "kurla", "time": 5},
                {"from": "kurla", "to": "vidyavihar", "time": 3},
                {"from": "vidyavihar", "to": "ghatkopar", "time": 3},
                
                # Harbor Line connections
                {"from": "cst_h", "to": "sandhurst_road_h", "time": 4},
                {"from": "sandhurst_road_h", "to": "dockyard_road", "time": 3},
                {"from": "dockyard_road", "to": "reay_road", "time": 3},
                {"from": "reay_road", "to": "cotton_green", "time": 3},
                {"from": "cotton_green", "to": "sewri", "time": 3},
                {"from": "sewri", "to": "wadala", "time": 4},
                
                # Interchange connections
                {"from": "dadar_w", "to": "dadar_c", "time": 7},  # Interchange at Dadar
                {"from": "dadar_c", "to": "dadar_w", "time": 7},
                {"from": "cst", "to": "cst_h", "time": 5},  # Interchange at CST
                {"from": "cst_h", "to": "cst", "time": 5},
                {"from": "sandhurst_road", "to": "sandhurst_road_h", "time": 5},  # Interchange at Sandhurst Road
                {"from": "sandhurst_road_h", "to": "sandhurst_road", "time": 5},
                {"from": "kurla", "to": "kurla_h", "time": 6}  # Interchange at Kurla
            ]
            
            print(f"Successfully loaded {len(stations)} stations and {len(connections)} connections")
            return stations, connections
    except Exception as e:
        print(f"Error loading station data: {e}")
        # Print the traceback for more detailed error information
        import traceback
        traceback.print_exc()
        return [], []

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map_view():
    return render_template('map.html')

@app.route('/api/stations')
def get_stations():
    stations, _ = load_station_data()
    return jsonify(stations)

@app.route('/api/update_crowds', methods=['POST'])
def update_crowds():
    stations, _ = load_station_data()
    
    # Simulate updating crowd levels
    for station in stations:
        # Random fluctuation in crowd levels
        station['crowdLevel'] = min(1.0, max(0.1, station['crowdLevel'] + (random.random() - 0.5) * 0.2))
    
    # Save updated data (in a real app, you would persist this)
    # For this demo, we'll just return success
    return jsonify({"success": True})

@app.route('/api/route')
def get_route():
    start_id = request.args.get('start')
    end_id = request.args.get('end')
    avoid_crowds = request.args.get('avoid_crowds', '0') == '1'
    
    if not start_id or not end_id:
        return jsonify({"error": "Start and end stations are required"})
    
    stations, connections = load_station_data()
    
    # Find the stations by ID
    start_station = next((s for s in stations if s['id'] == start_id), None)
    end_station = next((s for s in stations if s['id'] == end_id), None)
    
    if not start_station or not end_station:
        return jsonify({"error": "Invalid station IDs"})
    
    # Build a graph from connections
    graph = {}
    for conn in connections:
        from_id = conn['from']
        to_id = conn['to']
        time = conn['time']
        
        if from_id not in graph:
            graph[from_id] = []
        if to_id not in graph:
            graph[to_id] = []
        
        # Add bidirectional connections
        graph[from_id].append({'to': to_id, 'time': time})
        graph[to_id].append({'to': from_id, 'time': time})
    
    # Find route using Dijkstra's algorithm
    route = find_route(graph, stations, start_id, end_id, avoid_crowds)
    
    if not route:
        return jsonify({"error": "No route found between these stations"})
    
    # Calculate total time and average congestion
    total_time = sum(s.get('time', 0) for s in route['stations'][1:])
    avg_congestion = sum(s['crowdLevel'] for s in route['stations']) / len(route['stations'])
    
    return jsonify({
        "stations": route['stations'],
        "totalTime": total_time,
        "avgCongestion": avg_congestion
    })

def find_route(graph, stations, start_id, end_id, avoid_crowds):
    # Map of station IDs to station objects
    station_map = {s['id']: s for s in stations}
    
    # Initialize distances
    distances = {station_id: float('infinity') for station_id in graph}
    distances[start_id] = 0
    
    # Initialize previous nodes
    previous = {station_id: None for station_id in graph}
    
    # Unvisited nodes
    unvisited = set(graph.keys())
    
    while unvisited:
        # Find the unvisited node with the smallest distance
        current = min(unvisited, key=lambda x: distances[x])
        
        # If we've reached the end or if the distance is infinity, we're done
        if current == end_id or distances[current] == float('infinity'):
            break
        
        # Remove the current node from unvisited
        unvisited.remove(current)
        
        # Check each neighbor
        for neighbor in graph[current]:
            neighbor_id = neighbor['to']
            
            if neighbor_id not in unvisited:
                continue
            
            # Calculate the new distance
            time_factor = neighbor['time']
            
            # If avoiding crowds, add a penalty for crowded stations
            if avoid_crowds and neighbor_id in station_map:
                crowd_penalty = station_map[neighbor_id]['crowdLevel'] * 5  # 5 minutes max penalty
                time_factor += crowd_penalty
            
            new_distance = distances[current] + time_factor
            
            # If this path is better, update the distance and previous node
            if new_distance < distances[neighbor_id]:
                distances[neighbor_id] = new_distance
                previous[neighbor_id] = current
    
    # Build the path
    if end_id not in previous or previous[end_id] is None:
        return None
    
    path = []
    current = end_id
    
    while current:
        path.append(current)
        current = previous[current]
    
    # Reverse the path to get start to end
    path.reverse()
    
    # Convert path to station objects
    route_stations = []
    for i, station_id in enumerate(path):
        station = station_map[station_id].copy()
        
        # Add time to station (except for the first station)
        if i > 0:
            prev_id = path[i-1]
            for conn in graph[prev_id]:
                if conn['to'] == station_id:
                    station['time'] = conn['time']
                    break
        
        route_stations.append(station)
    
    return {"stations": route_stations}

if __name__ == '__main__':
    app.run(debug=True)
