import torch
import torch.nn as nn

class VisionLanguageActionModel(nn.Module):
    def __init__(self, image_dim=128, text_dim=128, action_dim=4):
        super().__init__()

        # Simple visual encoder (placeholder)
        self.vision_encoder = nn.Sequential(
            nn.Linear(image_dim, 256),
            nn.ReLU()
        )

        # Simple language encoder (placeholder)
        self.language_encoder = nn.Sequential(
            nn.Linear(text_dim, 256),
            nn.ReLU()
        )

        # Policy head
        self.policy = nn.Sequential(
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, action_dim)
        )

    def forward(self, image_features, text_features):
        v = self.vision_encoder(image_features)
        l = self.language_encoder(text_features)
        fused = torch.cat([v, l], dim=1)
        action = self.policy(fused)
        return action
