import pandas as pd
from platepals import PlatePals

def main():
    data = pd.read_csv("test.csv")
    platepalsgame = PlatePals(data)
    platepalsgame.write_to_csv("test_results")

if __name__ == "__main__":
    main()