import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from config import get_settings
settings = get_settings()

def main():
    print(settings.google_api_key)

if __name__ == "__main__":
    main()