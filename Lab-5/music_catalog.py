"""Manage an in-memory song catalog and JSON-encoded playlists."""

import json
import secrets
import sqlite3

CONNECTION = sqlite3.connect(":memory:")
CONNECTION.execute("CREATE TABLE songs (id INTEGER PRIMARY KEY, title TEXT, artist TEXT, plays INTEGER)")


def add_song(title, artist, plays=0, playlist=None):
    """Store a song and append its title to a caller-supplied or new playlist."""
    if playlist is None:
        playlist = []
    CONNECTION.execute(
        "INSERT INTO songs (title, artist, plays) VALUES (?, ?, ?)",
        (title, artist, plays),
    )
    playlist.append(title)
    return playlist


def shuffle_pick():
    """Return a random song ID, or None when the catalog is empty."""
    song_ids = [row[0] for row in CONNECTION.execute("SELECT id FROM songs")]
    return secrets.choice(song_ids) if song_ids else None


def popularity(title):
    """Classify a title as popular, niche or unknown; popular means >100 plays."""
    row = CONNECTION.execute("SELECT plays FROM songs WHERE title = ?", (title,)).fetchone()
    if row is None:
        return "unknown"
    return "popular" if row[0] > 100 else "niche"


def save_playlist(playlist):
    """Serialize a list of song titles to UTF-8 JSON bytes, not executable pickle."""
    if not isinstance(playlist, list) or not all(
        isinstance(title, str) for title in playlist
    ):
        raise ValueError("A playlist must be a list of song-title strings.")
    return json.dumps(playlist).encode("utf-8")


def load_playlist(blob):
    """Load UTF-8 JSON bytes, rejecting values other than lists of strings."""
    playlist = json.loads(blob.decode("utf-8"))
    if not isinstance(playlist, list) or not all(
        isinstance(title, str) for title in playlist
    ):
        raise ValueError("A playlist must be a list of song-title strings.")
    return playlist


def total_plays():
    """Return total plays, or zero for no songs; propagate database errors."""
    row = CONNECTION.execute("SELECT COALESCE(SUM(plays), 0) FROM songs").fetchone()
    return row[0]


def main():
    """Demonstrate catalog operations and a playlist serialization round trip."""
    playlist = add_song("Aurora", "Nila", 250)
    add_song("Monsoon", "Kavya", 40, playlist)
    blob = save_playlist(playlist)
    loaded_playlist = load_playlist(blob)
    if len(loaded_playlist) > 1:
        print("multi-song playlist")
    print(popularity("Aurora"), popularity("Monsoon"), shuffle_pick(), total_plays())


if __name__ == "__main__":
    try:
        main()
    finally:
        CONNECTION.close()
