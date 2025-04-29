try:
    import shiba
    shiba.bark()
except ImportError as e:
    print(f"Failed to import 'shiba': {e}")
except Exception as e:
    print(f"An error occurred: {e}")