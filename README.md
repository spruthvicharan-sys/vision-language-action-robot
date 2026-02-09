# Vision-Language-Action Robot

This repository explores **vision-language-action (VLA)** learning for robotic manipulation:
mapping a robot’s **visual observation + a natural language instruction** to **action outputs**.

## Goal
Build a simple, research-oriented baseline that can be extended toward:
- multimodal policies (vision + language → control)
- imitation learning / reinforcement learning
- manipulation tasks in simulation

## What’s inside (planned)
- **Perception**: image encoder (CNN/ViT baseline)
- **Language**: text encoder (transformer-style embedding)
- **Policy**: action predictor (MLP / transformer policy head)
- **Training**: minimal training loop + evaluation script
- **Results**: saved metrics + examples

## Why this matters
Robots operating in the real world need to understand both **what they see** and **what humans ask**.
VLA models are a promising step toward general-purpose robotic behavior.

## Tech
Python • PyTorch • (Simulation added next)

## Status
Work in progress — starting with a clean baseline and improving iter
