# Online Multiplayer Tic-Tac-Toe with Firebase 🎮

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://python.org)
[![Firebase](https://img.shields.io/badge/Firebase-Realtime_Database-orange?logo=firebase)](https://firebase.google.com)

A real-time networked implementation of Tic-Tac-Toe using Python and Firebase Realtime Database, demonstrating synchronized multiplayer gameplay with turn-based architecture.

## ✨ Features

- **Online PvP Battles**: Play against friends in real-time
- **Room-based Matchmaking**: Host or join games via CLI
- **Atomic State Management**: Firebase-enforced move validation
- **Cross-platform**: Works on any system with Python 3.8+

## 🛠 Core Components

### 🔥 Firebase Integration
- **Secure Authentication**: Service account SDK (`firebase-admin`)
- **Realtime Sync**: Instant board state updates
- **Data Structure**:
  ```json
  {
    "game": {
      "room_id": {
        "Map": ["X", "O", " ", ...],
        "round": 1|2  // Turn tracker
      }
    }
  }
