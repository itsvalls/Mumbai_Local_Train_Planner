// Mumbai local train stations data
const mumbaiStations = [
  // Western Line
  { id: "churchgate", name: "Churchgate", lat: 18.9322, lng: 72.8264, crowdLevel: 0.8, line: "Western" },
  { id: "marine_lines", name: "Marine Lines", lat: 18.9431, lng: 72.8253, crowdLevel: 0.5, line: "Western" },
  { id: "charni_road", name: "Charni Road", lat: 18.952, lng: 72.8187, crowdLevel: 0.6, line: "Western" },
  { id: "grant_road", name: "Grant Road", lat: 18.9641, lng: 72.8146, crowdLevel: 0.4, line: "Western" },
  { id: "mumbai_central", name: "Mumbai Central", lat: 18.9712, lng: 72.819, crowdLevel: 0.9, line: "Western" },
  { id: "mahalaxmi", name: "Mahalaxmi", lat: 18.9865, lng: 72.8296, crowdLevel: 0.7, line: "Western" },
  { id: "lower_parel", name: "Lower Parel", lat: 18.9977, lng: 72.8335, crowdLevel: 0.8, line: "Western" },
  { id: "elphinstone", name: "Elphinstone Road", lat: 19.0088, lng: 72.8362, crowdLevel: 0.7, line: "Western" },
  { id: "dadar_w", name: "Dadar (Western)", lat: 19.0178, lng: 72.8478, crowdLevel: 0.9, line: "Western" },
  { id: "matunga_road", name: "Matunga Road", lat: 19.0283, lng: 72.8469, crowdLevel: 0.5, line: "Western" },
  { id: "mahim", name: "Mahim", lat: 19.0367, lng: 72.8425, crowdLevel: 0.6, line: "Western" },
  { id: "bandra", name: "Bandra", lat: 19.0545, lng: 72.8412, crowdLevel: 0.8, line: "Western" },
  { id: "khar_road", name: "Khar Road", lat: 19.069, lng: 72.8371, crowdLevel: 0.5, line: "Western" },
  { id: "santacruz", name: "Santacruz", lat: 19.0804, lng: 72.8379, crowdLevel: 0.6, line: "Western" },
  { id: "vile_parle", name: "Vile Parle", lat: 19.0969, lng: 72.8394, crowdLevel: 0.7, line: "Western" },
  { id: "andheri", name: "Andheri", lat: 19.1197, lng: 72.8467, crowdLevel: 0.9, line: "Western" },

  // Central Line
  { id: "cst", name: "Chhatrapati Shivaji Terminus", lat: 18.9398, lng: 72.8354, crowdLevel: 0.9, line: "Central" },
  { id: "masjid", name: "Masjid", lat: 18.945, lng: 72.8399, crowdLevel: 0.5, line: "Central" },
  { id: "sandhurst_road", name: "Sandhurst Road", lat: 18.957, lng: 72.8399, crowdLevel: 0.4, line: "Central" },
  { id: "byculla", name: "Byculla", lat: 18.9764, lng: 72.833, crowdLevel: 0.6, line: "Central" },
  { id: "chinchpokli", name: "Chinchpokli", lat: 18.9864, lng: 72.833, crowdLevel: 0.5, line: "Central" },
  { id: "currey_road", name: "Currey Road", lat: 18.9942, lng: 72.833, crowdLevel: 0.4, line: "Central" },
  { id: "parel", name: "Parel", lat: 19.0015, lng: 72.8414, crowdLevel: 0.7, line: "Central" },
  { id: "dadar_c", name: "Dadar (Central)", lat: 19.0218, lng: 72.8439, crowdLevel: 0.9, line: "Central" },
  { id: "matunga", name: "Matunga", lat: 19.0283, lng: 72.855, crowdLevel: 0.6, line: "Central" },
  { id: "sion", name: "Sion", lat: 19.0379, lng: 72.8691, crowdLevel: 0.7, line: "Central" },
  { id: "kurla", name: "Kurla", lat: 19.0647, lng: 72.8891, crowdLevel: 0.8, line: "Central" },
  { id: "vidyavihar", name: "Vidyavihar", lat: 19.0797, lng: 72.8991, crowdLevel: 0.5, line: "Central" },
  { id: "ghatkopar", name: "Ghatkopar", lat: 19.0858, lng: 72.9081, crowdLevel: 0.8, line: "Central" },

  // Harbor Line
  { id: "wadala", name: "Wadala", lat: 19.0178, lng: 72.865, crowdLevel: 0.6, line: "Harbor" },
  { id: "sewri", name: "Sewri", lat: 19.005, lng: 72.855, crowdLevel: 0.4, line: "Harbor" },
  { id: "cotton_green", name: "Cotton Green", lat: 18.995, lng: 72.85, crowdLevel: 0.3, line: "Harbor" },
  { id: "reay_road", name: "Reay Road", lat: 18.985, lng: 72.845, crowdLevel: 0.4, line: "Harbor" },
  { id: "dockyard_road", name: "Dockyard Road", lat: 18.975, lng: 72.84, crowdLevel: 0.5, line: "Harbor" },
  {
    id: "sandhurst_road_h",
    name: "Sandhurst Road (Harbor)",
    lat: 18.957,
    lng: 72.8399,
    crowdLevel: 0.4,
    line: "Harbor",
  },
  { id: "cst_h", name: "CST (Harbor)", lat: 18.9398, lng: 72.8354, crowdLevel: 0.9, line: "Harbor" },
  { id: "kurla_h", name: "Kurla (Harbor)", lat: 19.065, lng: 72.8895, crowdLevel: 0.8, line: "Harbor" },
]

// Connection data between stations
const connections = [
  // Western Line connections
  { from: "churchgate", to: "marine_lines", time: 3 },
  { from: "marine_lines", to: "charni_road", time: 3 },
  { from: "charni_road", to: "grant_road", time: 3 },
  { from: "grant_road", to: "mumbai_central", time: 3 },
  { from: "mumbai_central", to: "mahalaxmi", time: 4 },
  { from: "mahalaxmi", to: "lower_parel", time: 3 },
  { from: "lower_parel", to: "elphinstone", time: 3 },
  { from: "elphinstone", to: "dadar_w", time: 3 },
  { from: "dadar_w", to: "matunga_road", time: 3 },
  { from: "matunga_road", to: "mahim", time: 3 },
  { from: "mahim", to: "bandra", time: 4 },
  { from: "bandra", to: "khar_road", time: 3 },
  { from: "khar_road", to: "santacruz", time: 3 },
  { from: "santacruz", to: "vile_parle", time: 4 },
  { from: "vile_parle", to: "andheri", time: 4 },

  // Central Line connections
  { from: "cst", to: "masjid", time: 3 },
  { from: "masjid", to: "sandhurst_road", time: 3 },
  { from: "sandhurst_road", to: "byculla", time: 4 },
  { from: "byculla", to: "chinchpokli", time: 3 },
  { from: "chinchpokli", to: "currey_road", time: 3 },
  { from: "currey_road", to: "parel", time: 3 },
  { from: "parel", to: "dadar_c", time: 4 },
  { from: "dadar_c", to: "matunga", time: 3 },
  { from: "matunga", to: "sion", time: 4 },
  { from: "sion", to: "kurla", time: 5 },
  { from: "kurla", to: "vidyavihar", time: 3 },
  { from: "vidyavihar", to: "ghatkopar", time: 3 },

  // Harbor Line connections
  { from: "cst_h", to: "sandhurst_road_h", time: 4 },
  { from: "sandhurst_road_h", to: "dockyard_road", time: 3 },
  { from: "dockyard_road", to: "reay_road", time: 3 },
  { from: "reay_road", to: "cotton_green", time: 3 },
  { from: "cotton_green", to: "sewri", time: 3 },
  { from: "sewri", to: "wadala", time: 4 },

  // Interchange connections
  { from: "dadar_w", to: "dadar_c", time: 7 }, // Interchange at Dadar
  { from: "dadar_c", to: "dadar_w", time: 7 },
  { from: "cst", to: "cst_h", time: 5 }, // Interchange at CST
  { from: "cst_h", to: "cst", time: 5 },
  { from: "sandhurst_road", to: "sandhurst_road_h", time: 5 }, // Interchange at Sandhurst Road
  { from: "sandhurst_road_h", to: "sandhurst_road", time: 5 },
  { from: "kurla", to: "kurla_h", time: 6 }, // Interchange at Kurla
]

// Export the data for use in other files
if (typeof module !== "undefined") {
  module.exports = {
    stations: mumbaiStations,
    connections: connections,
  }
}
