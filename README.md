Online Multiplayer Tic-Tac-Toe with Firebase.
A real-time, networked implementation of Tic-Tac-Toe built in Python, leveraging Firebase Realtime Database for synchronized multiplayer gameplay. Designed as a proof-of-concept for turn-based online games, this project demonstrates secure Web API integration, state management, and event-driven architecture.

Core Components
  *Firebase Integration
      -Uses firebase-admin SDK with service account authentication.
  *Game Logic
    -Host/Join System: Players create or join rooms via CLI.
    -Input Handling: Position validation and board updates with atomic Firebase writes.
    -State Polling: Active waiting for opponent moves via Firebase round flag checks.

  *Error Resilience
    -Handles duplicate moves and invalid inputs client-side.
    -Firebase rules enforce data consistency (recommended: add server-side validation).
