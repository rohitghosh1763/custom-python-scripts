import os
import shutil
import sys
from pathlib import Path

def get_spotify_cache_paths():
    """Get common Spotify cache directory paths for Windows."""
    username = os.getenv('USERNAME')
    
    cache_paths = [
        # Main Spotify cache directory
        f"C:\\Users\\{username}\\AppData\\Local\\Spotify\\Data",
        # Browser cache (if using web player)
        f"C:\\Users\\{username}\\AppData\\Local\\Spotify\\Browser",
        # Storage directory
        f"C:\\Users\\{username}\\AppData\\Local\\Spotify\\Storage",
        # Temp files
        f"C:\\Users\\{username}\\AppData\\Local\\Temp\\Spotify",
        # Additional cache locations
        f"C:\\Users\\{username}\\AppData\\Roaming\\Spotify",
    ]
    
    return cache_paths

def remove_directory_contents(path):
    """Remove all contents of a directory but keep the directory itself."""
    try:
        if os.path.exists(path):
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                else:
                    os.remove(item_path)
            return True
        return False
    except PermissionError:
        print(f"Permission denied: {path}")
        return False
    except Exception as e:
        print(f"Error removing {path}: {e}")
        return False

def is_spotify_running():
    """Check if Spotify is currently running."""
    try:
        import psutil
        for proc in psutil.process_iter(['pid', 'name']):
            if 'spotify' in proc.info['name'].lower():
                return True
        return False
    except ImportError:
        print("psutil not installed. Cannot check if Spotify is running.")
        print("Please manually close Spotify before running this script.")
        return None

def clear_spotify_cache():
    """Main function to clear Spotify cache."""
    print("Spotify Cache Cleaner")
    print("=" * 30)
    
    # Check if Spotify is running
    spotify_running = is_spotify_running()
    if spotify_running:
        print("⚠️  Spotify is currently running!")
        print("Please close Spotify before clearing cache.")
        response = input("Continue anyway? (y/N): ").lower()
        if response != 'y':
            print("Cache clearing cancelled.")
            return
    elif spotify_running is None:
        print("⚠️  Please make sure Spotify is closed before proceeding.")
        response = input("Continue? (y/N): ").lower()
        if response != 'y':
            print("Cache clearing cancelled.")
            return
    
    cache_paths = get_spotify_cache_paths()
    total_size_before = 0
    cleared_paths = []
    
    # Calculate total size before clearing
    for path in cache_paths:
        if os.path.exists(path):
            try:
                size = sum(os.path.getsize(os.path.join(dirpath, filename))
                          for dirpath, dirnames, filenames in os.walk(path)
                          for filename in filenames)
                total_size_before += size
            except:
                pass
    
    print(f"Total cache size before clearing: {total_size_before / (1024*1024):.2f} MB")
    print("\nClearing cache directories...")
    
    # Clear each cache directory
    for path in cache_paths:
        if os.path.exists(path):
            print(f"Clearing: {path}")
            if remove_directory_contents(path):
                cleared_paths.append(path)
                print(f"✅ Cleared: {path}")
            else:
                print(f"❌ Failed to clear: {path}")
        else:
            print(f"⚠️  Path not found: {path}")
    
    # Summary
    print("\n" + "=" * 50)
    print("Cache Clearing Summary:")
    print(f"Directories processed: {len(cache_paths)}")
    print(f"Successfully cleared: {len(cleared_paths)}")
    print(f"Cache size freed: ~{total_size_before / (1024*1024):.2f} MB")
    
    if cleared_paths:
        print("\n✅ Spotify cache has been cleared successfully!")
        print("You can now restart Spotify.")
    else:
        print("\n⚠️  No cache directories were cleared.")

def main():
    """Main entry point with error handling."""
    try:
        # Check if running on Windows
        if sys.platform != 'win32':
            print("This script is designed for Windows. For other OS:")
            print("macOS: ~/Library/Caches/com.spotify.client/")
            print("Linux: ~/.cache/spotify/")
            return
        
        clear_spotify_cache()
        
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        print("Please run the script as administrator if permission issues persist.")

if __name__ == "__main__":
    main()