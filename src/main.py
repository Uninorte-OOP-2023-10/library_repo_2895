import pandas as pd
from files.file_manager import FileManager

def main() -> None:
    print(FileManager.DATA_PATH)
    file_manager = FileManager('netflix_titles.csv')
    df = pd.read_csv(file_manager.generate_path())
    print(df)

if __name__ == '__main__':
    main()