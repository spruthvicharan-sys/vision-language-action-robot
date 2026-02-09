import torch
from model import VisionLanguageActionModel

def main():
    model = VisionLanguageActionModel()
    model.eval()

    image_features = torch.randn(1, 128)
    text_features = torch.randn(1, 128)

    with torch.no_grad():
        action = model(image_features, text_features)

    print("Predicted action:", action)

if __name__ == "__main__":
    main()
