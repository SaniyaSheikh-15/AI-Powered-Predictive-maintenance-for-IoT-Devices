from src.train import train
from src.predict import predict
from src.utils import save_output

if __name__ == "__main__":
    train("data/sample.csv")

    sample = {"temp":70,"vibration":2.5,"pressure":30}
    pred, prob = predict(sample)

    print("Prediction:",pred,"Confidence:",prob)
    save_output([{"prediction":pred,"confidence":prob}])
